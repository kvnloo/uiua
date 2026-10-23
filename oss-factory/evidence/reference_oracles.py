#!/usr/bin/env python3
"""Fork-only numeric reproductions. Does NOT compile or execute Uiua Rust code.

Run with: python reference_oracles.py
Requires NumPy for an independent matrix reference. Uses POSIX libm.fma.
"""
import ctypes
import ctypes.util
import math
import random
import numpy as np

libm_name = ctypes.util.find_library('m')
if not libm_name:
    raise RuntimeError('POSIX libm is needed for fma verification')
libm = ctypes.CDLL(libm_name)
libm.fma.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double)
libm.fma.restype = ctypes.c_double


def base_digit(n, base):
    q = math.floor(n / base)
    fma_remainder = libm.fma(float(q), -base, n)
    optimized = (fma_remainder if math.isfinite(fma_remainder) and 0 <= fma_remainder < base
                 else math.fmod(n, base))
    return fma_remainder, optimized, math.fmod(n, base)


boundary = base_digit(11.0, 1.1)
assert boundary[0] < 0 and boundary[1] == boundary[2]
assert base_digit(1237.0, 2.7)[1] == base_digit(1237.0, 2.7)[2]
rand = random.Random(17)
for i in range(30_000):
    n = float(rand.randrange(0, 1_000_000)) + (rand.random() if i % 3 == 0 else 0)
    base = 10 ** rand.uniform(-1, 2) * (1 if i % 4 else (1 + rand.random() / 100))
    raw, optimized, reference = base_digit(n, base)
    assert optimized == reference, (n, base, raw, optimized, reference)
print('FMA: forced 11/1.1 negative-remainder case + 30,000 deterministic scalar checks passed')


def lu_solve(a, b):
    """Python transcription of the downstream candidate, for residual checks."""
    a, b = np.array(a, dtype=float, copy=True), np.array(b, dtype=float, copy=True)
    n, m = b.shape
    if not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError('nonfinite data')
    l = np.eye(n)
    permutation = list(range(n))
    for i in range(n):
        pivot = i + int(np.argmax(np.abs(a[i:, i])))
        permutation[i], permutation[pivot] = permutation[pivot], permutation[i]
        l[[i, pivot], :i] = l[[pivot, i], :i]
        a[[i, pivot], i:] = a[[pivot, i], i:]
        if a[i, i] == 0.0:
            raise ValueError('singular pivot')
        for row in range(i + 1, n):
            mul = a[row, i] / a[i, i]
            l[row, i] = mul
            a[row, i:] -= mul * a[i, i:]
    x = b[permutation, :].copy()
    for row in range(n):
        for col in range(m):
            val = x[row, col]
            for j in range(row):
                val -= l[row, j] * x[j, col]
            x[row, col] = val / l[row, row]
    for row in reversed(range(n)):
        for col in range(m):
            val = x[row, col]
            for j in range(row + 1, n):
                val -= a[row, j] * x[j, col]
            x[row, col] = val / a[row, row]
    return x


rng = np.random.default_rng(20261017)
max_residual = 0.0
cases = 0
for n in range(1, 8):
    for m in range(0, 8):
        for _ in range(20):
            a = rng.normal(size=(n, n)) + np.eye(n) * 2
            b = rng.normal(size=(n, m))
            x = lu_solve(a, b)
            np.testing.assert_allclose(a @ x, b, rtol=1e-10, atol=1e-10)
            if m:
                max_residual = max(max_residual, float(np.max(np.abs(a @ x - b))))
            cases += 1
scaled_x = lu_solve([[1e-20, 0], [0, 2e-20]], [[3e-20], [8e-20]])
np.testing.assert_allclose(scaled_x, [[3], [4]], rtol=1e-12, atol=0)
assert lu_solve([[0, 1], [1, 0]], [[1, 2, 3], [4, 5, 6]]).tolist() == [[4, 5, 6], [1, 2, 3]]
print(f'Matrix: {cases} deterministic 1..7 x 0..7 RHS cases; max absolute residual {max_residual:.4e}')
print('These are mathematical reference checks only; Rust compilation and project tests are still required.')
