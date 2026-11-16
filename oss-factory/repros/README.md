# Uiua issue #1041 — missing needles in under indexin

Downstream **diagnostic fixtures**, not accepted tests or a behavior fix. These
files are intentionally outside `tests/` and `tests_special/` because the
inverse semantics are not yet agreed upon.

Source: https://github.com/uiua-lang/uiua/issues/1041

Run each diagnostic separately on a native Uiua build. An expected error stops
a whole-file run before subsequent expressions execute:

```sh
uiua eval '⍜⊗(+0) "bab" "baa"'
uiua eval '⍜⊗(+0) "bab" "bac"'
uiua eval '⍜⊗⇌ "bab" "bac"'
```

The first expression is a control with all needles present. The second
preserves a not-found sentinel through an identity-like update and can
exercise the current out-of-bounds reverse lookup. The third moves a sentinel,
exposing the yet-undecided question of which original needle to recover at a
new position. Verify that optimizer simplification doesn't bypass the
identity-like case. Record Uiua version, stdout/stderr and exit status.

The `+0` operand must be grouped as `(+0)`. Native execution of the original
ungrouped control at `881f24f5` failed with a character/number search type error,
not a missing-sentinel error. The grouped replacement requires fresh native
verification; results belong in the single promotion queue, fork PR #7.

For issue #1039 locals/recursion, use the independent **source-fix and test
branch** in https://github.com/kvnloo/uiua/pull/12 instead of duplicating
its source and regression tests here.

**Gate:** reproduce on current native Uiua; obtain human agreement on the
missing-sentinel behavior; only then add assertions to the main test suite.
No upstream AI contributions.
