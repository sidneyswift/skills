# `/goal` examples — weak → strong, by domain

A gallery of vague inputs turned into strong Codex `/goal` specs. Use these as patterns to adapt, not as fill-in-the-blank templates. Every strong version names an **outcome**, a **verification surface**, and at least one **constraint or boundary**.

## Contents

- [Performance tuning](#performance-tuning)
- [Flaky test investigation](#flaky-test-investigation)
- [Dependency / framework migration](#dependency--framework-migration)
- [Multi-step refactor](#multi-step-refactor)
- [Bug hunt requiring reproduction](#bug-hunt-requiring-reproduction)
- [Generated artifact (docs)](#generated-artifact-docs)
- [Research with mixed-confidence evidence](#research-with-mixed-confidence-evidence)

---

## Performance tuning

Weak:

```text
/goal Improve performance
```

Strong:

```text
/goal Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service, its benchmark fixtures, and related tests. Between iterations, record what changed, what the benchmark showed, and the next best experiment to try. If the benchmark cannot run or no valid paths remain, stop with the attempted paths, the evidence gathered, the blocker, and the next input needed.
```

Why it works: a measurable threshold (120 ms), a verification surface (the benchmark), and a hard constraint (correctness stays green). 135 ms is not done; passing the benchmark but failing correctness is not done.

---

## Flaky test investigation

Weak:

```text
/goal Fix the flaky checkout test
```

Strong:

```text
/goal Make `checkout_spec` pass 50 consecutive runs on the current branch, verified by running the suite in a loop, while preserving existing public behavior and not deleting or skipping the test. Use the checkout test files, the code under test, and CI logs. Between iterations, record the failure mode observed and the hypothesis being tested next. If the flake cannot be reproduced or root-caused, stop with the reproduction attempts, the evidence, and what additional logs or access would unlock progress.
```

Why it works: "fix the flaky test" has no finish line; "50 consecutive passes" is auditable, and the constraint forbids the lazy fix (skipping the test).

---

## Dependency / framework migration

Weak:

```text
/goal Upgrade to React 19
```

Strong:

```text
/goal Migrate the app to React 19 with the full test suite green, a clean production build, and no new console warnings, verified by the test run and build output. Use only application code and its dependencies; do not change product behavior or public component APIs. Between iterations, migrate one area at a time and record what changed and what the build/tests showed. If a dependency blocks the upgrade, stop with the blocking package, the error, and the options (patch, replace, or wait).
```

Why it works: names three concrete evidence surfaces (tests, build, console) and forbids behavior/API drift, which is the usual hidden risk in a migration.

---

## Multi-step refactor

Weak:

```text
/goal Refactor the payments module
```

Strong:

```text
/goal Extract the payments module's side-effect-free logic into a separate, unit-tested layer, verified by the existing suite staying green and new unit tests covering the extracted functions, without changing public API behavior. Use only the payments module and its tests. Between iterations, extract one responsibility at a time and confirm the suite stays green. If a piece cannot be cleanly extracted, stop and report which coupling blocks it.
```

Why it works: "refactor" alone has no audit surface; this fixes the end state (extracted, tested layer) and the invariant (public behavior unchanged).

---

## Bug hunt requiring reproduction

Weak:

```text
/goal Fix the intermittent 500 on upload
```

Strong:

```text
/goal Reproduce and fix the intermittent HTTP 500 on file upload, verified by a regression test that fails on the current code and passes after the fix, while keeping the rest of the upload suite green. Use the upload handler, its tests, and server logs. Between iterations, record the reproduction conditions found and the next hypothesis. If the error cannot be reproduced locally, stop with the conditions tried and the logs or data needed to reproduce it.
```

Why it works: forces reproduction-before-fix and bakes the proof (a failing-then-passing regression test) into the verification surface.

---

## Generated artifact (docs)

Weak:

```text
/goal Write docs for this feature
```

Strong:

```text
/goal Produce a docs page for the Goals feature that explains the lifecycle, the command surface, and two worked examples, verified by the page building locally and every referenced command matching current CLI behavior. Use the docs site and the CLI source as ground truth. Between iterations, draft a section, then check its commands against the CLI. If a command's behavior is unclear, stop and list the commands needing confirmation.
```

Why it works: a doc Goal needs an inspectable surface — here, a successful local build plus command-accuracy against the real CLI.

---

## Research with mixed-confidence evidence

This is where Goals earn their keep: the answer is uncertain, so the **evidence standard must be defined before the work** to keep the final report honest.

Weak:

```text
/goal Reproduce Buehler et al., "Deep Hedging"
```

Strong:

```text
/goal Produce the strongest evidence-backed reproduction of Buehler et al., "Deep Hedging," using the available paper materials and local resources. Attempt every headline result, verify outputs where possible, and end with a report that separates reproduced mechanics, approximate trained results, blocked exact replay, and remaining uncertainty. Between iterations, build a claim inventory, map each claim to evidence, and rebuild what can be tested locally. If a claim cannot be reproduced from the available materials (missing seeds, training paths, or checkpoints), label it blocked rather than overstating a match.
```

Why it works: it names the final artifact (a claim-by-claim audit) and four explicit confidence levels, so a plausible reconstruction never gets flattened into a false "exact reproduction." A single ledger entry in that report might read:

```text
Claim: Deep hedging approximates the complete-market Heston hedge without transaction costs.
Route: Rebuilt model mechanics, reference hedge comparison, and trained neural policy.
Evidence surface: Price checks, histograms, and hedge surfaces.
Status: Close approximate reproduction.
Remaining uncertainty: Original training paths, seeds, and checkpoints are unavailable.
```
