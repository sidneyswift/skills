---
name: spec-goals
description: "Use when someone asks 'help me write a /goal', 'turn this into a goal', 'draft a goal for Codex', 'spec this for /goal', 'is this a good goal', or 'sharpen this objective'. Turns a defined, durable objective into a ready-to-paste Codex `/goal` with a measurable outcome, verification surface, constraints, boundaries, iteration policy, and blocked-stop condition. If the outcome, evidence, constraints, or approach still contains load-bearing unknowns, use flex-finding-unknowns first. Do NOT use this skill to execute the work."
metadata:
  owner: sswift@swiftdrtv.com
  status: draft
  user-invocable: true
---

# spec-goals — turn a vague idea into a strong Codex `/goal`

A Codex **Goal** is a persistent objective attached to a thread: Codex keeps working toward it across turns, deciding the next action on its own, and only marks it done when **evidence** proves it. A vague prompt ("make it faster," "reproduce this paper") wastes that power because Codex has no finish line to check against.

This skill turns a Goal-shaped task into a `/goal` that is **narrow enough to audit but broad enough for Codex to discover the path.** If the task's outcome, evidence, constraints, or approach still contains load-bearing unknowns, use **flex-finding-unknowns** before drafting the Goal. You produce the text; the user pastes it into Codex.

> Command note: the feature is called **Goals**, but the actual command is singular — `/goal`. Goals require Codex `0.128.0` or newer.

## Step 1 — Check the task is Goal-shaped (do this first, every time)

A Goal is the right tool **only when all three are true**:

1. **Durable objective** — there's one outcome worth holding across many turns.
2. **Evidence-based finish line** — something concrete can prove it's done (a test, a benchmark, a build, a report, command output, an artifact).
3. **Uncertain, multi-turn path** — the next step depends on what Codex learns along the way.

If any of those is missing, **say so and recommend a normal prompt instead** — do not force a Goal.

If the missing piece requires discovery that could change the task's scope or architecture, hand off to **flex-finding-unknowns** instead of trying to resolve it inside this skill. Recommend a normal prompt only when the task is already clear but simply does not need a durable, multi-turn Goal.

| Good fit for `/goal` | Use a normal prompt instead |
| --- | --- |
| Performance / latency tuning to a threshold | A single one-line edit |
| Flaky-test investigation (needs reproduction) | A quick explanation or "what does this do?" |
| Dependency / framework migration | A short code review with one answer |
| Bug hunts that require reproducing the bug | Any task where you want one result, then stop |
| Multi-step refactor with a defined end state | A finish line you can't describe ("make it better") |
| Benchmark-driven optimization | Hiding uncertainty (if data may be missing, that belongs *in* the Goal) |
| Research that must end in a verified artifact | |

If the task fails the gate, stop here. Use **flex-finding-unknowns** when discovery could change the scope or architecture; otherwise hand the user a tightened **normal prompt**, not a Goal.

## Step 2 — The six elements of a strong Goal

A strong Goal is a contract, not a bigger prompt. Aim to define all six. The first four usually need the user; the last two you can almost always supply with a sensible default.

| # | Element | The question it answers |
| --- | --- | --- |
| 1 | **Outcome** | What must be *true* when the work is done? (make it measurable) |
| 2 | **Verification surface** | What concrete evidence proves it? (test, benchmark, build, report, artifact, command output) |
| 3 | **Constraints** | What must NOT regress while Codex works? |
| 4 | **Boundaries** | Which files, tools, data, or repos may Codex touch? |
| 5 | **Iteration policy** | After each attempt, how should Codex choose the next action? |
| 6 | **Blocked-stop condition** | When should Codex stop and report that no defensible path remains — and what would unlock it? |

The two most common weaknesses are a **vague outcome** (element 1) and a **missing verification surface** (element 2). Fix those first.

## Step 3 — Interview only for the load-bearing gaps

Read the user's input and map it onto the six elements. Then:

- **Ask only for the missing elements that genuinely change the Goal** — at most ~3 questions at a time. Do not interrogate.
- If answering a missing element requires a blindspot pass, options exploration, unfamiliar-domain teaching, or reference mapping, stop and use **flex-finding-unknowns** first.
- **Infer the rest** from the repo, the conversation, and common sense (e.g., boundaries often = "the service in question + its tests").
- **Default elements 5 and 6** unless the user has a specific policy. Good defaults:
  - Iteration policy: *"Between iterations, record what changed, what the evidence showed, and the next best experiment to try."*
  - Blocked-stop: *"If you cannot verify or no valid paths remain, stop with the attempted paths, the evidence gathered, the blocker, and the next input needed."*

The single highest-value move is converting a fuzzy outcome into a measurable one:

| User says | Sharpen the outcome to |
| --- | --- |
| "make checkout faster" | "reduce p95 checkout latency below 120 ms on the checkout benchmark" |
| "fix the flaky test" | "make `checkout_spec` pass 50 consecutive runs on the current branch" |
| "upgrade React" | "migrate to React 19 with the full test suite green and no console warnings" |
| "reproduce the paper" | "reproduce the paper's headline results, separating confirmed, approximate, and blocked claims" |

## Step 4 — Assemble the `/goal`

Fit the six elements into this pattern:

```text
/goal <desired end state> verified by <specific evidence> while preserving <constraints>. Use <allowed inputs, tools, or boundaries>. Between iterations, <how Codex should choose the next best action>. If blocked or no valid paths remain, <what Codex should report and what would unlock progress>.
```

Worked example — from vague to strong.

Weak (what the user brought):

```text
/goal Improve performance
```

Strong (what you deliver):

```text
/goal Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service, its benchmark fixtures, and related tests. Between iterations, record what changed, what the benchmark showed, and the next best experiment to try. If the benchmark cannot run or no valid paths remain, stop with the attempted paths, the evidence gathered, the blocker, and the next input needed.
```

Keep it **narrow enough to audit, broad enough to discover.** "Fix the failing checkout test" can be too narrow if the real cause is upstream; "improve the whole system" is too broad to verify. "Make the checkout suite pass on this branch without changing public API behavior" is right.

For more domains (flaky tests, migrations, refactors, docs, and research with mixed-confidence evidence), read `references/examples.md`.

## Step 5 — Deliver

Return three things, in this order:

1. **The ready-to-paste `/goal`** in its own fenced block (one line, so it pastes cleanly into Codex).
2. **A two-line rationale** — name the outcome, the verification surface, and any constraint, so the user can sanity-check the contract.
3. **The lifecycle reminder:**

```text
/goal          View the current Goal
/goal pause    Pause an active Goal
/goal resume   Resume a paused Goal
/goal clear    Remove the current Goal
```

Then remind the user of the one rule that makes Goals trustworthy: **completion is evidence-based.** Codex should mark a Goal done only after checking it against real files, tests, logs, benchmark output, or artifacts — not because it "seems done." Reaching a budget limit is not completion; it's a pause to summarize progress and blockers.

## Quick reference

- **Command:** `/goal <text>` to set; `/goal` to view; `pause` / `resume` / `clear` to manage. (Singular, even though the feature is "Goals.")
- **Version:** Codex `0.128.0`+.
- **Scope:** a Goal lives on the **thread**, not global memory or project instructions — so set it in the thread that holds the relevant context.
- **For research / uncertain evidence:** define the evidence standard *before* the work — what counts as exact reproduction, approximate reconstruction, proxy support, and blocked — so the final report stays honest instead of overclaiming.
