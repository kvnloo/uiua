# Uiua issue #1041 — missing needles in under indexin

Downstream **diagnostic fixtures**, not accepted tests or a behavior fix. These
files are intentionally outside `tests/` and `tests_special/` because the
inverse semantics are not yet agreed upon.

Source: https://github.com/uiua-lang/uiua/issues/1041

Run on a native Uiua build:

```sh
uiua eval "$(cat oss-factory/repros/1041-under-indexin.ua)"
```

The first expression is a control with all needles present. The second
preserves a not-found sentinel through an identity-like update and can
exercise the current out-of-bounds reverse lookup. The third moves a sentinel,
exposing the yet-undecided question of which original needle to recover at a
new position. Verify that optimizer simplification doesn't bypass the
identity-like case. Record Uiua version, stdout/stderr and exit status.

For issue #1039 locals/recursion, use the independent **source-fix and test
branch** in https://github.com/kvnloo/uiua/pull/12 instead of duplicating
its source and regression tests here.

**Gate:** reproduce on current native Uiua; obtain human agreement on the
missing-sentinel behavior; only then add assertions to the main test suite.
No upstream AI contributions.
