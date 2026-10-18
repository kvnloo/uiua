# Uiua downstream runtime reproductions

These are **diagnostic fixtures**, not accepted test cases. They are intentionally
outside `tests/` and `tests_special/` because the current upstream behavior
may fail. Do not claim either issue is fixed or reproducible on the current
interpreter without running these cases.

## #1039 — locals + recursion

Source: https://github.com/uiua-lang/uiua/issues/1039

Run from the checkout:

```sh
uiua eval -x "$(cat oss-factory/repros/1039-locals-recursion.ua)"
```

The issue reports two different internal interpreter-bug diagnostics depending
on whether the `F 1` line is active. Compare both variants on the same commit.
Desired behavior is a valid result or ordinary explained runtime error,
not "This is a bug in the interpreter."

## #1041 — under indexin with missing needles

Source: https://github.com/uiua-lang/uiua/issues/1041
Original passing example: `⍤⤙≍ "cbc" ⍜⊗+₁ "abc" "bab"`
(in upstream `tests/under.ua`).

```sh
uiua eval "$(cat oss-factory/repros/1041-under-indexin.ua)"
```

The first expression contains only matching needles; the second retains
the not-found sentinel from `⊗` through an identity-like update and should
not try to index out of bounds if the proposed enhancement is implemented.
The last expression moves the sentinel to a different position; its intended
result is not yet specified. Verify that the interpreter does not optimize
away the identity case before relying on it as a regression. Capture exact
stdout, stderr, version and exit code.

## Gates

* Run on the current upstream base and record which expressions actually fail.
* Reduce reproductions to minimum examples and distinguish compiler errors
  from runtime errors and host panics.
* Only after the intended semantics are agreed, move executable assertions
  into existing tests.
* Keep upstream reviewers/maintainers uncontacted during downstream waves.
