# Uiua OSS factory — canonical downstream promotion queue

**Snapshot:** 2026-10-17 (US Central); `uiua-lang/uiua` main `ef1463951b80e67c662964d944cac1a4a13abe59`.
**Scope:** all 21 open upstream issues and 14 open upstream PRs at the snapshot. Track new entries here; do not create parallel queues.
**Location:** this is the per-repo queue because GitHub Issues are disabled on `kvnloo/uiua`. This repository is downstream-only for this wave; do not post upstream, approve, or merge anyone's PR automatically.

## Verified work in our fork

| Fork PR | Source / original contributor | Status and contents |
| --- | --- | --- |
| [#3](https://github.com/kvnloo/uiua/pull/3) | [uiua #668](https://github.com/uiua-lang/uiua/issues/668) | Documentation-only patch clarifying `main` branch and `branch:`/`commit:` limits in web pad. Static source verified; Rust/site validation pending. |
| [#4](https://github.com/kvnloo/uiua/pull/4) | [uiua PR #1036](https://github.com/uiua-lang/uiua/pull/1036), original author **@amatgil** | `A (n×n) \ B (n×m)`: fix RHS stride, number of columns, and output shape; 2 Rust tests for n×3 and n×1 RHS. Independent NumPy expectations verified; Rust tests pending. |
| [#5](https://github.com/kvnloo/uiua/pull/5) | [uiua PR #1037](https://github.com/uiua-lang/uiua/pull/1037), original author **@ndren** | Fall back to Euclidean remainder when FMA yields a negative/out-of-range/nonfinite result for a positive base; 1 Rust regression test. Independent libm reproduction; Rust tests and benchmark pending. |
| [#6](https://github.com/kvnloo/uiua/pull/6) | [uiua PR #1031](https://github.com/uiua-lang/uiua/pull/1031), original author **@Dguto9** | RHS union operand order, transactional union-arm validation, subtype inclusion and dynamic-shape reflexivity; 4 Rust regression tests. Rust tests pending; upstream is a draft. |

**Evidence & environment:** no `rustc`/`cargo` in this execution environment; GitHub Actions on `kvnloo/uiua` returned zero workflow runs (as checked). Do not call these Rust-test-verified or merge-ready. The PRs preserve the original contributors' head commits and authorship. The fork main remains synced to upstream; all changes are on separate branches.

## Upstream PR intake — 14/14 reviewed

| PR | Triage | Evidence and next step |
| --- | --- | --- |
| [#1031](https://github.com/uiua-lang/uiua/pull/1031) | P1, draft, correctness | Union types; run fork [#6](https://github.com/kvnloo/uiua/pull/6), validate nested unions, branch isolation, dyadic operand order and type-join semantics; coordinate with @Dguto9 before any promotion. |
| [#1036](https://github.com/uiua-lang/uiua/pull/1036) | P1, draft, correctness | Matrix left division; fork [#4](https://github.com/kvnloo/uiua/pull/4) fixes rectangular RHS. Also investigate absolute `f64::EPSILON` singular check and nonfinite pivots; tests/benchmark required. |
| [#1037](https://github.com/uiua-lang/uiua/pull/1037) | P1, ready PR with correctness question | Direct div/rem FMA. Fork [#5](https://github.com/kvnloo/uiua/pull/5) guards Euclidean range; benchmark fractional and integer bases and confirm old semantics. |
| [#1033](https://github.com/uiua-lang/uiua/pull/1033) | P2, dependency bot | `nokhwa` 0.10.9→0.10.11, lockfile-only; validate webcam builds/features, platform compatibility, and security advisories before accepting. |
| [#1032](https://github.com/uiua-lang/uiua/pull/1032) | P2, dependency bot / higher risk | `cosmic-text` 0.15→0.19, lockfile transitive changes; check actual API compatibility, font rendering and GUI builds rather than approving blindly. |
| [#1030](https://github.com/uiua-lang/uiua/pull/1030) | P2, small fix | @Dguto9 adjusts scalar/any-shape type-spec output (two lines). Run type-spec round-trip coverage; existing positive feedback, no new duplicate comment needed. |
| [#1003](https://github.com/uiua-lang/uiua/pull/1003) | P1, correctness / tests | @UnrelatedString nested `under`; maintainer @kaikalii specifically requested invalid-use tests in `tests_special/error.ua`. Respect existing discussion; do not post a duplicate request. |
| [#1011](https://github.com/uiua-lang/uiua/pull/1011) | P2, dependency bot | `viuer` 0.9→0.11; `crossterm` is also updated transitively. Verify terminal image integrations and Linux/Windows portability. |
| [#1009](https://github.com/uiua-lang/uiua/pull/1009) | P2, dependency bot | `tokio` 1.47.1→1.53.1; target supported Rust version, async I/O and tests; avoid redundant lockfile-only adjustments. |
| [#1008](https://github.com/uiua-lang/uiua/pull/1008) | P2, dependency bot | `rayon` 1.10→1.12; check parallel interpreter paths and ecosystem compatibility. |
| [#745](https://github.com/uiua-lang/uiua/pull/745) | P3, draft / architectural | @amatgil big rational numbers are explicitly WIP; `RealArrayValue: Copy` ownership question, memory/performance model and type-system agreement before code push. |
| [#779](https://github.com/uiua-lang/uiua/pull/779) | P3, draft / reviewer pushback | @magistau broad linting; @kaikalii explicitly pushed back on `clippy::pedantic` as a standard. Avoid sweeping reformat/refactor PRs; isolate correctness-only changes if requested. |
| [#742](https://github.com/uiua-lang/uiua/pull/742) | P3, workflow debate | @magistau CI expansion; @alex-s168 flagged `needs: test_site` and path/branch semantics. Reconcile job names/triggers before experimenting. |
| [#774](https://github.com/uiua-lang/uiua/pull/774) | P3, major refactor / design discussion | @magistau generator crate; @kaikalii wants tracked generated content and generation in tests to avoid forgetting updates. Minimize scope and honor Nix concerns. |

## Upstream issue intake — 21/21 reviewed

| Issue | Triage and next action |
| --- | --- |
| [#1041](https://github.com/uiua-lang/uiua/issues/1041) | P1: `under indexin` not-found sentinel reaches reverse phase, yielding OOB. Produce minimal tests covering absent needle, unchanged sentinel and changed needle before deciding exact inverse behavior. |
| [#1040](https://github.com/uiua-lang/uiua/issues/1040) | P1: `Or` type requested; already under [PR #1031](https://github.com/uiua-lang/uiua/pull/1031). No parallel feature PR. |
| [#1039](https://github.com/uiua-lang/uiua/issues/1039) | P1: locals + recursion yields interpreter-bug errors; minimize with current dev build and add non-crash tests when reproducible. |
| [#1027](https://github.com/uiua-lang/uiua/issues/1027) | P2: force ANSI colors through pipes. @memark offered to implement `--color=auto|always|never`, preserve `--no-color`; align all subcommands, including `doc`, `eval`, REPL. Avoid duplicate implementation before checking ownership. |
| [#1002](https://github.com/uiua-lang/uiua/issues/1002) | P1: nested `under` context save/restore tracked by [PR #1003](https://github.com/uiua-lang/uiua/pull/1003); prioritize negative test coverage requested by maintainer. |
| [#875](https://github.com/uiua-lang/uiua/issues/875) | P3: version-locked embeds require multi-version interpreter distribution; maintainer noted hosting complexity. Prototype compatibility manifest only after design discussion. |
| [#872](https://github.com/uiua-lang/uiua/issues/872) | No code: marked `not a bug`; examples paste pretty-printed complex values rather than `repr`. Avoid reopening settled semantics. |
| [#861](https://github.com/uiua-lang/uiua/issues/861) | P2: streaming line-transform CLI. Maintainer suggested `uiua line` instead of Perl-style eval switches; prototype bounded stdin behavior/design first. |
| [#709](https://github.com/uiua-lang/uiua/issues/709) | P2: take/dropwhile performance. Maintainer favors possible optimization on an existing idiom rather than new primitive; require controlled benchmark vs `do` loop and prefix scan. |
| [#708](https://github.com/uiua-lang/uiua/issues/708) | P2: binary-search/bisection primitive; interval-tree use case provided. Reuse #709 benchmark, establish sortedness/insertion-bound semantics before new primitive. |
| [#668](https://github.com/uiua-lang/uiua/issues/668) | P1, addressed downstream in [fork PR #3](https://github.com/kvnloo/uiua/pull/3): document that web GitHub imports always fetch `main` and do not accept branch/commit specifiers. |
| [#648](https://github.com/uiua-lang/uiua/issues/648) | P3: unsafe-removal policy; maintainer values performance and does not aim for zero `unsafe`, but may accept targeted `bytemuck` conversions. No blanket rewrites. |
| [#635](https://github.com/uiua-lang/uiua/issues/635) | P2: bit conversion beyond f64 53-bit integer precision; precision-loss warning/docs or explicit arbitrary-precision type design, not a silent cast patch. |
| [#612](https://github.com/uiua-lang/uiua/issues/612) | P3 UX: file sharing between pad instances was called intentional by maintainer. Improve explicit visibility/controls, not silent isolation. |
| [#575](https://github.com/uiua-lang/uiua/issues/575) | P3: reduce-on-multiple-axes syntax has alternative proposals from maintainer; seek design decision before primitive grammar changes. |
| [#569](https://github.com/uiua-lang/uiua/issues/569) | P2 docs: inverse documentation partly addressed in commit `20cfc189`; find concrete remaining under-documented inverses, avoid duplicating existing examples. |
| [#564](https://github.com/uiua-lang/uiua/issues/564) | No work: labeled `wontfix`; runtime blocking in the browser requires workers and maintainer ruled out async interpreter. |
| [#250](https://github.com/uiua-lang/uiua/issues/250) | P3: floating log10 precision; maintainer cautioned about pervasive-operation slowdown and rejected naive integer-log rounding. Benchmark and preserve IEEE semantics. |
| [#489](https://github.com/uiua-lang/uiua/issues/489) | P3: complex math edge cases, error bounds partly fixed by maintainer; remaining NaN/∞ tradeoffs are design/perf sensitive. |
| [#481](https://github.com/uiua-lang/uiua/issues/481) | P3: invertible reshape semantics (`△.` vs `⊃△♭`) undecided; do not implement until agreed. |
| [#338](https://github.com/uiua-lang/uiua/issues/338) | P2 UX bug: docs search clear → reselect same primitive. Needs browser reproduction around `site/src/docs.rs` (`set_timeout`, `Allowed` memo and route changes) before fixing. |

## Repro evidence and review follow-up

1. **#1037:** f64 FMA `10.mul_add(-1.1, 11.0)` gives `-8.881784197001252e-16`; Euclidean remainder `11.0 % 1.1` gives `1.0999999999999992`. In a controlled synthetic sweep of **11,500** positive numbers/bases, **1,109** FMA residues fell outside `[0, base)`; this is NOT a representative workload or speed benchmark. The branch fixes the invariant via guarded fallback.
2. **#1036:** for `A = [[0,1],[1,0]]` and `B = [[1,2,3],[4,5,6]]`, a correct `AX=B` solution has shape `2×3` and rows `[[4,5,6],[1,2,3]]`; for identity `A` and column `B=[[7],[9]]`, output is `2×1`. The old algorithm indexed `B` with `n` columns regardless of `m` and always returned shape of `A`. Python/NumPy oracle validated these cases.
3. **#1031:** `dyadic_pervasive_inner` reversed operands when its RHS was a union; union-arm validation mutated `ch` on failed candidate; dynamic dimension inclusion incorrectly rejected `Dyn ⊇ Dyn`, and a union's subtype inclusion required exact variant equality instead of coverage. All four changes are isolated in downstream fork #6 with Rust tests.
4. **#1003:** await/prepare failure tests for nested `under` in `tests_special/error.ua`; maintainer has explicitly requested them. Avoid untested guessed fixtures.
5. **#338/#1039/#1041:** require true runtime/browser repro before asserting a fix.

## Promotion gates and next waves

- Run `cargo fmt --all --check`, `cargo test --lib`, `cargo clippy --no-deps --all-targets --workspace --all-features -- --deny=warnings` on each isolated code branch; rerun targeted tests. The available runtime has neither `cargo` nor `rustc`, and the fork has no Action runs.
- Verify branch base against fresh upstream main; prefer small commits and no speculative API changes. Benchmark #1037 performance and validate #1036 singular/NaN behavior.
- Fix failing tests in the downstream branch first; do not merge the four draft PRs blindly into fork main. Keep cross-author commits and explicit attribution.
- Before any promotion, check current maintainer feedback; post at most one independent, actionable review per PR, avoid duplicate reports and unrequested approvals. Upstream writes remain out of scope until explicitly authorized.
- Reconcile this single queue on each wave; update existing rows rather than create more queue issues. Link ready changes from the factory-wide index separately only if permitted.

## Historical fork branches

Old `auto-claude/001-*` and `auto-claude/002-*` branches are hundreds of upstream commits behind. The Git-module branch incorrectly claimed web branch/commit support, so its documentation was not promoted. All old branches remain untouched.
