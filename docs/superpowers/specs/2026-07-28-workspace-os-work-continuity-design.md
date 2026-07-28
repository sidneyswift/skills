# Workspace OS Work Continuity Design

- **Date:** 2026-07-28
- **Status:** Approved design; implementation not started
- **Applies to:** `workspace-os` v0.11.1

## Purpose

Workspace OS exists so a fresh human or agent can enter a workspace without relying on chat history,
recover authoritative current state and the next correct action, advance work safely, verify the
outcome, and leave the system more capable than before.

The folders, skills, routines, and reports are implementation details. The system outcome is
**verified continuity across context boundaries**.

## Current gap

The existing system has strong homes for domain state and compounding assets:

- `{pipeline}/` and `{entities}/` hold flowing domain state.
- `knowledge/`, `library/`, `plugin/skills/`, `artifacts/`, and `operations/` hold reusable value.
- `PROGRESS.md` records an append-only workspace history.
- `work/` holds dated one-off output and skillification staging.

It does not have a standard current-state and handoff record for ordinary initiatives. A fresh agent
cannot reliably answer:

- What work is active, blocked, paused, or awaiting review?
- What outcome is expected, and what evidence proves completion?
- What is the exact next action?
- Which file or external system owns each fact?
- What changed when research invalidated the original plan?
- Why was work completed or cancelled?
- What durable knowledge, template, skill, proof, check, or eval came out of it?

`PROGRESS.md` cannot fill this role because it is historical and append-only. Reconstructing current
state from a chronological log is not a reliable handoff process.

## Design principles

1. **Continuity over folder completeness.** Create only enough structure to make consequential work
   resumable and verifiable.
2. **One canonical coordination record.** Initiative status, ownership, acceptance, next action, and
   evidence have one authority.
3. **Coordination overlay, not a second domain system.** Work packages link to domain records and
   external systems instead of copying their state.
4. **Stable identity and paths.** Completion changes status and views; it does not move the canonical
   package by default.
5. **Proportional overhead.** Small same-turn tasks do not create work packages.
6. **Grow on demand.** Plans, research, notes, deliverables, and package-specific instructions exist
   only when real material requires them.
7. **Evidence-gated closure.** Complete means acceptance criteria were evaluated against linked
   evidence.
8. **Event-driven compounding.** Meaningful discoveries and closure events feed learning and system
   improvement; agents do not manufacture a learning every session.
9. **Derived views are not authorities.** Indexes and dashboards may summarize canonical records but
   never own their state.
10. **Fresh-context verification.** The design is proven by unrelated agents resuming and closing
    work, not by documentation inspection alone.

## Decisions

### No root `plans/` directory

A root `plans/` directory groups files by document type and separates each plan from its research,
evidence, decisions, and deliverables. Planning remains local to the initiative it governs.

### Thin work-package kernel

Every initiative that crosses a session or agent boundary, carries meaningful uncertainty or
dependencies, has a review gate, or requires evidence-based acceptance gets one canonical record:

```text
work/{initiative}/README.md
```

`plan.md` and supporting folders are optional.

### Shared lifecycle contract

`work/AGENTS.md` is the canonical runtime instruction contract for managed work. The generated root
`CLAUDE.md` / `AGENTS.md` brain explicitly routes agents to it. A `work/CLAUDE.md` symlink or adapter
ensures Claude loads the same contract.

Package-level `AGENTS.md` files are created only for exceptional constraints. When one exists, create
the matching Claude adapter as well.

### Stable-path archive view

Completed and cancelled packages remain at stable paths. `work/README.md` groups terminal packages by
closure year as a human archive view. Physical archival is deferred until package volume creates
an observed problem and backlink-safe movement exists.

### Field-level authority

The local package always owns coordination and handoff state. Domain records and external systems
continue to own the fields assigned to them.

### Setup dogfoods the system

Workspace OS setup is the first managed initiative. Its package is created before discovery, updated
throughout the build, and closed only after the doctor verifies the generated workspace.

## Information architecture

```text
work/
├── README.md                         # human navigation; derived from package records
├── AGENTS.md                         # canonical managed-work lifecycle contract
├── CLAUDE.md -> AGENTS.md            # Claude adapter; fallback file if symlinks are unavailable
├── {initiative}/
│   ├── README.md                     # required canonical coordination and handoff record
│   ├── plan.md                       # optional detailed decomposition
│   ├── YYYY-MM-DD-{activity}/        # dated execution material, preserving the existing convention
│   ├── research/                     # optional; only when research exists
│   ├── notes/                        # optional; only when separate notes add value
│   ├── deliverables/                 # optional; outputs owned by this initiative
│   ├── AGENTS.md                     # optional exceptional package constraints
│   └── CLAUDE.md -> AGENTS.md        # created only with package AGENTS.md
└── ...
```

There is no mandatory empty `archive/`, `research/`, `notes/`, or `deliverables/` directory.

## Package creation threshold

Create a package when any of these observable conditions applies:

- another session or agent will probably continue the work;
- the work has a dependency, review gate, or blocker;
- research or uncertainty can materially change the approach;
- completion requires durable evidence or a durable deliverable;
- the user explicitly asks to track the initiative.

Do not create a package for routine same-turn work. Record a material result in `PROGRESS.md` when
appropriate.

The doctor validates packages that exist. It does not guess whether an untracked request was
"non-trivial"; fresh-context behavioral evals test that judgment.

## Canonical package record

Each package README begins with a small machine-readable metadata block:

```yaml
---
id: workspace-memory-rd
status: active
owner: Sidney
updated: 2026-07-28
---
```

Allowed statuses:

- `active` — work can advance now;
- `blocked` — an external dependency prevents progress;
- `paused` — work was intentionally deferred;
- `review` — a named person must evaluate a question or deliverable;
- `complete` — acceptance criteria were evaluated and satisfied;
- `cancelled` — work intentionally stopped without satisfying the original acceptance criteria.

Terminal packages also carry a `closed` date. Reopening `complete` or `cancelled` work requires an
explicit reason in the package history.

### Required human-readable sections

1. **Outcome** — the result this initiative intends to create.
2. **Done when** — observable acceptance criteria.
3. **Current state** — concise, current truth rather than a session narrative.
4. **Next action** — one exact continuation step, or a task ID from `plan.md`.
5. **Blocker or review** — when applicable, including responsible party, unblock/review condition,
   and next check date.
6. **Links and authority** — related domain records, external systems, plans, artifacts, and which
   location owns which fields.
7. **Evidence and outcome** — verification evidence and the final result for terminal work.
8. **Durable value** — disposition into knowledge, library, proof, skill, check/eval, recurring
   artifact, or an explicit "none" with a reason.

Conditional sections may say "not applicable"; they must not contain invented filler.

## Optional `plan.md`

Create `plan.md` only when detailed task decomposition materially improves execution or handoff.

When present, it owns:

- scope and non-goals;
- dependencies and sequencing;
- stable work-item IDs;
- checklists and checkpoints;
- research questions;
- discovered bugs or child initiatives;
- decision and evidence links.

It does not repeat package status, owner, current-state summary, or acceptance outcome. The package
README may point to a current task ID instead of restating the task.

## Authority model

| Surface | Owns | Must not own |
| --- | --- | --- |
| Package `README.md` | initiative status, owner, acceptance, current state, next execution action, evidence, closeout | copied client/release/study lifecycle facts |
| Optional `plan.md` | detailed execution tasks, sequencing, dependencies, research questions | package status or duplicated current-state summaries |
| Domain entity and pipeline | domain lifecycle and domain facts | generic initiative coordination |
| External system | only fields declared in `operations/sync.md` | unspecified local package state |
| `work/README.md` | navigation and derived views | independently edited status |
| Root `PROGRESS.md` | append-only material history | current state or next action |
| `knowledge/` | settled reusable conclusions | raw research or package-only notes |
| `library/` | reusable instruments | completed one-off deliverables |
| `plugin/skills/` | verified repeatable capabilities | half-working drafts |
| `operations/` | workspace health, sync mapping, and system improvements | domain execution state |

## Lifecycle contract

### Start

1. Search `work/README.md`, package IDs, domain records, and linked external systems for existing
   equivalent work.
2. Resume an existing package instead of creating a duplicate.
3. If the threshold is met, create the package atomically with its outcome, acceptance criteria,
   authority links, owner, and first next action.
4. Create `plan.md` or supporting folders only when needed.
5. Reconcile the derived work index and append a material start event to `PROGRESS.md`.

### Resume

1. Reread the root brain and `work/AGENTS.md` from disk.
2. Read `work/README.md`, the package README, its optional plan, package-specific instructions, linked
   domain records, and latest evidence.
3. Reconcile the package record with actual artifacts before acting.
4. Continue from the exact next action.

### Advance and discover

1. Update completed work items and evidence.
2. When evidence changes assumptions, scope, acceptance criteria, or sequencing, update the package
   and optional plan in the same turn.
3. Reconcile only domain or external fields that actually changed.
4. Leave one exact next action.

### Handoff and stop

Before ending a meaningful work session, record:

- last known-good state;
- exact next action;
- changed artifacts;
- verification performed;
- blockers, review needs, or restart condition;
- unresolved assumptions.

Use `blocked`, `paused`, or `review` when those states are true. Do not claim completion merely
because an agent must stop.

### Complete or cancel

1. Evaluate each acceptance criterion against linked evidence.
2. Record the outcome and any remaining work.
3. Reconcile linked domain and external state.
4. Decide the durable-value disposition.
5. Set the terminal status and closure date.
6. Reconcile the work index and append the material lifecycle event to `PROGRESS.md`.

### Reopen

Reopening terminal work requires:

- an explicit reason;
- a new next action;
- refreshed acceptance criteria when the intended outcome changed;
- a `PROGRESS.md` entry.

## Instruction hierarchy

### Builder skill

`workspace-os/SKILL.md`:

- creates the minimal work control surface before Phase 0 discovery;
- creates and uses the setup package;
- uses the setup package as the destination for the Understanding Brief, research, reviewed design,
  and build evidence;
- closes setup only after the final doctor run;
- scaffolds the work templates and routes the generated brain to the lifecycle contract.

### Root generated brain

`assets/CLAUDE.md.tmpl`:

- states the continuity purpose;
- defines the package threshold;
- requires reading `work/AGENTS.md` before creating, resuming, changing, or closing managed work;
- defines field-level authority and same-turn reconciliation;
- distinguishes package current state from `PROGRESS.md` history;
- replaces forced per-session learning and the 50/50 quota with event-driven checkpoints.

### Shared work contract

A new `assets/work-AGENTS.md.tmpl` defines:

- search-before-create;
- valid statuses and transitions;
- read order;
- required package fields and sections;
- same-turn update rules;
- handoff and stop ritual;
- evidence-gated completion;
- cancellation and reopening;
- archive views;
- learning, reflect, and skillify triggers.

### Package-specific instructions

Package `AGENTS.md` files contain additive exceptional constraints only. They never carry mutable
status, tasks, history, or copied global rules.

## Compounding loop

The managed-work loop is:

```text
intent → execution → discovery → reconciliation → evidence → outcome → extraction → replay
```

### Meaningful discovery

First update the package truth. Promote a conclusion to `knowledge/` only when it is settled and
reusable. Keep raw findings in the package.

### Closure disposition

Every completed or cancelled package evaluates:

- reusable answer or decision → `knowledge/`;
- reusable instrument → `library/`;
- accepted outcome or proof → `proof/`;
- repeated or maintainable process → skillify;
- recurring output → `artifacts/`;
- recurring inconsistency → doctor check;
- important or recurring failure → eval or regression test;
- observed system friction → reflect;
- nothing reusable → record why and create nothing.

### Improvement verification

System-improvement states are:

```text
proposed → applied → verified
                   ↘ rejected
```

`applied` is not `verified`. Verification requires a replay, fresh-context eval, or later work package
showing that the change prevented recurrence or reduced handoff cost.

## Maintenance behavior

### Doctor

The doctor remains report-only. Its deterministic path checks:

- unique package IDs;
- valid statuses and required metadata;
- required sections;
- active work has an owner and exact next action;
- blocked, paused, and review work has a responsible party, condition, and check date;
- terminal work has closure date, evidence, outcome, and durable-value disposition;
- referenced local paths resolve;
- derived work-index entries match package records;
- optional folders are absent or non-empty;
- terminal work is not presented as active.

The doctor skill evaluates semantic quality: whether acceptance criteria and evidence are meaningful,
whether an initiative deserved a package, and whether authority was assigned correctly.

### Janitor

The janitor may:

- refresh the derived work index;
- repair unambiguous internal links;
- flag stale active work and overdue blocked/paused/review work;
- invoke learn, reflect, or skillify after an explicit closure.

It must not:

- invent an owner or next action;
- change initiative status when intent is ambiguous;
- complete or cancel work;
- manufacture a learning or system improvement.

### Learn

Learning is event-driven after a meaningful discovery or closure. A clean "nothing reusable" is valid.
Promoted knowledge links back to package provenance and evidence.

### Reflect

Reflect scans completed, cancelled, and failed work for observed friction. It proposes the smallest
durable change and tracks it through `proposed`, `applied`, `verified`, or `rejected`.

### Skillify

Skillify uses the closed package as provenance and normalizes staging under the package convention.
Half-working skills remain staged and never appear in `plugin/skills/`.

## `PROGRESS.md` role

`PROGRESS.md` remains append-only but stops serving as mandatory prose churn. Record material events:

- initiative started, blocked, paused, entered review, completed, cancelled, or reopened;
- important discovery changed direction;
- durable asset promoted;
- operating-system machinery changed or was verified.

Package README files hold current state. `PROGRESS.md` preserves history.

## Evaluation strategy

### RED baseline

Preserve v0.11.1 as the baseline and run fresh-context scenarios before editing. Expected failures:

- ordinary work has no canonical handoff record;
- a second agent reconstructs state from chat-like history and filesystem inspection;
- blocked and cancelled work lack explicit semantics;
- closure is not evidence-gated;
- learning may be manufactured to satisfy a per-session quota.

### Harness corrections

Before trusting new scores:

- align `evals/rubric.md` with the v0.11.1 lean spine and current seven organ names;
- separate agent-visible scenario prompts from hidden evaluator expectations;
- snapshot after each turn so later janitor work cannot conceal an earlier autonomy failure;
- score filesystem evidence rather than agent self-reports;
- add doctor mutation fixtures;
- keep generated runs auditable enough to support ledger claims.

### Behavioral scenarios

1. Setup package exists before discovery and closes only after verification.
2. A same-turn trivial task correctly creates no package.
3. A one-off deliverable crosses a review boundary and receives a package.
4. Agent A starts multi-session R&D; fresh Agent B resumes without chat history or duplicated work.
5. Package-linked domain work updates the correct authorities without copying domain state.
6. Research changes the plan and acceptance criteria in the same turn.
7. Work becomes blocked, paused, and awaiting review with sufficient continuation details.
8. A discovered bug is handled in scope or becomes a linked child initiative with evidence.
9. Work completes with evidence and durable-value disposition.
10. Work is cancelled without losing salvageable evidence or a restart condition.
11. A genuine learning is extracted and reused by a later fresh agent.
12. A no-learning control creates no filler knowledge.
13. An applied system improvement remains unverified until a replay proves it.

### Mechanical acceptance criteria

- All existing packages have unique IDs and valid lifecycle records.
- A clean fixture produces no work findings.
- Every seeded invalid state produces the intended finding.
- Derived index and package records agree.
- All local links resolve.
- Terminal packages have evidence, outcome, and disposition.
- No optional empty folders are scaffolded.

### Behavioral acceptance criteria

- A fresh second agent resumes the correct package and next action without prior chat.
- Plan-changing evidence updates package truth in the same turn.
- Domain and external state are not duplicated into competing authorities.
- Agents do not falsely complete blocked or paused work.
- Durable assets retain provenance and are reused without re-derivation.
- A trivial same-turn task incurs no package ceremony.

## Expected implementation surface

### Existing files

- `workspace-os/SKILL.md`
- `workspace-os/references/blueprint.md`
- `workspace-os/references/self-management.md`
- `workspace-os/references/domain-inference.md`
- `workspace-os/references/skillifying-work.md`
- `workspace-os/references/packaging.md`
- `workspace-os/assets/CLAUDE.md.tmpl`
- `workspace-os/assets/routine.md.tmpl`
- `workspace-os/assets/doctor-SKILL.md.tmpl`
- `workspace-os/assets/doctor.py.tmpl`
- `workspace-os/assets/janitor-SKILL.md.tmpl`
- `workspace-os/assets/compound-learn-SKILL.md.tmpl`
- `workspace-os/assets/reflect-SKILL.md.tmpl`
- `workspace-os/assets/skillify-SKILL.md.tmpl`
- `workspace-os/evals/README.md`
- `workspace-os/evals/rubric.md`
- `workspace-os/evals/validate.py`
- current eval scenarios and improvements ledger
- root `README.md`

### New files

- `workspace-os/assets/work-AGENTS.md.tmpl`
- `workspace-os/assets/work-README.md.tmpl`
- `workspace-os/assets/work-package-README.md.tmpl`
- `workspace-os/assets/work-plan.md.tmpl`
- `workspace-os/assets/process-input-SKILL.md.tmpl`
- fresh-context work-continuity scenarios and doctor fixtures under `workspace-os/evals/`

Exact scenario and fixture paths belong in the implementation plan.

## Rejected alternatives

### Root `plans/`

Rejected because it separates plans from the initiative context and creates cross-folder archive work.

### Mandatory document bundle

Rejected because required README, plan, research, tasks, handoff, and deliverable files create empty
scaffolding and duplicated mutable state.

### Universal second pipeline

Rejected because `work/active`, `work/blocked`, and similar stage folders duplicate domain pipelines
and change paths on ordinary status transitions.

### External tracker as universal hub

Rejected as a requirement because connectors may not exist and work must remain portable. External
systems may still own declared fields.

### Immediate physical archival

Rejected because path moves break links and add lifecycle work before scale proves it necessary.

### New work-manager organ

Rejected because root routing, one work contract, package records, and existing maintenance organs
already provide the necessary seams.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Agents package every small request | Observable creation threshold; behavioral no-package control |
| Agents avoid packages entirely | Root routing plus fresh-context handoff evals |
| Package and domain status diverge | Field-level authority and link-based reconciliation |
| README and optional plan duplicate state | Strict ownership: README coordinates; plan decomposes |
| Work index becomes stale | Derived view, doctor parity check, janitor refresh |
| Nested instructions are not loaded | Root fallback plus Claude adapter |
| Completed folders accumulate | Archive view now; physical movement only after observed scale pain |
| Learning becomes filler | Event-driven capture and valid "nothing reusable" outcome |
| Improvements are declared successful too early | Separate applied from replay-verified |
| Eval reports look strong without proving handoff | Hidden oracles, per-turn snapshots, fresh agents, mutation tests |

## Non-goals

- Replacing domain pipelines, entity records, or configured external systems.
- Building a general-purpose issue tracker.
- Requiring a formal plan for every request.
- Physically moving completed packages before scale requires it.
- Adding empty folder taxonomies.
- Automatically completing, cancelling, or inventing ownership for ambiguous work.

## Success statement

The change succeeds when an unrelated agent can enter a generated Workspace OS, identify the correct
managed initiative, understand its authoritative current state and exact next action, advance or
close it with evidence, and deposit genuinely reusable value—while a trivial task remains trivial and
the doctor catches stale or contradictory lifecycle records without creating process noise.
