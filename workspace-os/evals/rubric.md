# Scoring rubric

Two rubrics, each /100. Every item traces to a contract in `workspace-os` (the SKILL phases or the
`references/`), so a low score points at a specific place in the skill to fix.

Severity for findings: **broken** (contradictory/invalid state), **gap** (missing expected thing),
**polish** (works but weak). `validate.py` auto-scores the items marked `[auto]`; the rest are scored
by inspection or by an evaluator subagent.

---

## A. Build-time rubric (is the workspace well-formed?) — /100

### Structure & taxonomy — 20
- **5** `[auto]` Lean spine present: `plugin/`, `routines/`, `scripts/`, `docs/`, and `work/`.
- **5** `[auto]` Every top-level folder name is a single lowercase word.
- **5** No unjustified empty on-demand folders. `operations/`, `knowledge/`, `library/`, `artifacts/`,
  domain pipeline/entities, and optional folders exist only when real material or an organ needs them.
- **5** Domain fit: when a pipeline exists, stages are numbered (`01-`, `02-`) and match the
  archetype; when entities exist, the folder matches the core unit. Their absence is not a build
  failure when the kickoff contains no real instances.

### The brain — 20
- **8** `[auto]` `CLAUDE.md` exists, has no leftover `{DOMAIN}`/`{PIPELINE}`/`{ENTITY}` placeholders,
  and contains the auto-manage, never-stale, event-driven learning, filing, and managed-work routing
  contracts.
- **3** `[auto]` Root `AGENTS.md` mirrors `CLAUDE.md` (symlink preferred; a fallback pointer is partial).
- **5** `[auto]` `work/README.md`, `work/AGENTS.md`, and the `work/CLAUDE.md` adapter exist; the work
  index is explicitly derived rather than independently authoritative.
- **4** `[auto]` `work/workspace-os-setup/README.md` records the live build and closes only after
  verification evidence. `PROGRESS.md` contains material lifecycle entries.

### Skills & plugin — 30
- **10** `[auto]` All seven four-word organs exist under `plugin/skills/`: `*-process-input`,
  `*-check-health`, `*-fix-drift`, `*-capture-learning`, `*-improve-machinery`, `*-promote-skill`,
  and `*-find-unknowns` — plus at least one domain-specific skill.
- **6** `[auto]` Each `SKILL.md` is valid: `name` matches its folder, has a `description`, no angle
  brackets in the description.
- **6** `[auto]` Manifests valid + parity: both exist, same kebab `name` (defaults to `{slug}-os`),
  Codex manifest has `"skills": "./skills/"`.
- **4** `[auto]` `.agents/skills` adapter resolves to / mirrors `plugin/skills`.
- **4** Doctor reads as read-only; janitor explicitly runs the doctor first (by content inspection).

### Compounding assets — 15
- **8** When the input contains settled reusable answers, `knowledge/` captures them with provenance.
  Sparse builds do not manufacture knowledge to earn points.
- **7** When reusable instruments are justified, `library/` contains domain-relevant templates or
  checklists with real content. An absent library is acceptable when no instrument is warranted.

### Hygiene & honesty — 15
- **5** Inferred facts are marked "draft — confirm"; no invented hard facts the user must own.
- **5** No one-off work is promoted to a top-level folder; no empty optional package folders exist;
  `validate.py` checks pass.
- **5** A packaged `{slug}-os.plugin` was produced (or the attempt + outputs noted); intended janitor
  cadence + `armed:` status recorded in `routines/README.md` if no scheduler was available.

---

## B. Use-time rubric (does it manage & improve itself?) — /100

Scored from the `git diff` between the post-build baseline and the post-use state, plus the user
agent's own report. **This is the headline score.**

### Intake & filing — 20
- **10** New input placed in its correct home, dated `YYYY-MM-DD`.
- **10** Input actually read and reconciled against the right entity/pipeline folder (not just dropped).

### Never-stale — 30  *(the defining property)*
- **10** The affected entity `README.md` / `{pipeline}/_board.md` was updated to match the new reality
  **in the same turn**.
- **10** `artifacts/dashboard.html` was regenerated so its counts/KPIs match the folders.
- **10** No contradiction left behind: a post-hoc doctor run comes back clean (or only flags things
  outside this task).

### Compound learning — 20
- **10** A genuinely reusable discovery was deposited with provenance, **or** the package records a
  justified "nothing reusable" closeout without creating filler.
- **10** A repeated question/decision was written once and reused, or the no-learning control correctly
  produced no knowledge artifact.

### Self-improvement machinery — 20
- **7** The **doctor** runs read-only and writes a sensible score + punch list to
  `operations/health.md` (it changed nothing else).
- **7** The **janitor** fixed safe drift and reported a before/after score.
- **6** Repeated/maintainable work triggered a **skillify** proposal, or **reflect** logged a grounded
  system improvement to `operations/improvements.md` (citing a real friction, not generic advice).

### Autonomy & evidence — 10
- **5** Loops fired **without being told** — given only "here's new material," the agent still updated
  the dashboard/board/knowledge because `CLAUDE.md` told it to. (If it only acted when explicitly
  instructed, score 0 — that's the key failure mode.)
- **5** "Done / consistent" was claimed against a doctor run, not asserted by feel.

---

## C. Work-continuity rubric (can consequential work survive context loss?) — /100

Score from per-turn snapshots and fresh-context operator behavior. Do not use the operator's own
summary as the source of truth.

### Canonical coordination state — 20
- **10** Exactly one managed package represents the initiative, with unique ID, valid status, owner,
  updated date, outcome, and acceptance criteria.
- **10** Current state and exact next action are recoverable from the package README; optional
  `plan.md` adds decomposition without copying package status.

### Fresh-agent resume — 20
- **10** A second agent with no prior chat finds the same package and starts from its recorded next
  action.
- **10** It does not repeat completed investigation or invent missing state.

### Authority + same-turn reconciliation — 15
- **8** Package coordination, domain state, and declared external fields remain in their assigned
  authorities and link to each other instead of copying facts.
- **7** Plan-changing evidence updates package truth and affected authoritative records in the same
  turn.

### Blocked, paused, and review continuity — 10
- **10** Non-active work records the responsible party, condition, check date, preserved progress, and
  exact resume action; no agent falsely completes it.

### Evidence-gated closure — 15
- **8** Complete/cancelled status has a closure date, outcome, evidence, and disposition of remaining
  work.
- **7** The stable package path appears in the closure-year archive view and all local links resolve.

### Durable value — 10
- **5** Reusable value is promoted with package provenance, or a valid no-op is recorded.
- **5** Applied machinery improvements remain unverified until a replay or later run proves them.

### Proportional overhead — 10
- **10** The same-turn control creates no package, empty optional folders, or filler learning.

---

## Reading the scores

- **Build high, Use low** → the scaffold is pretty but inert. The fix is almost always in the
  generated `CLAUDE.md` (`assets/CLAUDE.md.tmpl`) or the organ skill templates — the brain isn't
  compelling the loops. This is the most important failure to hunt.
- **Build low** → the fix is in the SKILL phases / references the builder followed (taxonomy,
  packaging, skill-authoring). Often the skill is ambiguous or too heavy to finish in one context.
- **Both low** → the kickoff was too sparse for the skill's inference rules, or a phase is
  underspecified. Check whether the builder even finished all 7 phases.
- **Use high, Continuity low** → capable agents are reconstructing state ad hoc. Standardize the
  package interface without replacing effective domain pipelines.
- **Continuity shape high, Resume low** → the workspace has paperwork but does not teach a fresh
  agent how to use it. Fix root routing or the shared work contract.

Every finding becomes a row in `improvements-ledger.md`: *finding → evidence (run/agent) → the exact
file in `workspace-os/` to change → status.*
