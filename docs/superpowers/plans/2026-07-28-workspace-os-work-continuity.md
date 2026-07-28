# Workspace OS Work Continuity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox
> (`- [ ]`) syntax for tracking.

**Goal:** Add a thin, evidence-gated work-package lifecycle so unrelated humans and agents can start,
resume, verify, close, and learn from consequential work without relying on chat history.

**Architecture:** Keep `work/` as the execution-continuity seam between domain state and compounding
assets. Each managed initiative has one canonical `README.md`; detailed plans and supporting folders
remain optional. Root instructions route agents to one shared work lifecycle contract, while the
doctor, janitor, learn, reflect, skillify, and fresh-context evals enforce and verify the lifecycle.

**Tech Stack:** Markdown Agent Skills, Python 3 standard library, `unittest`, filesystem fixtures,
JSON, ZIP packaging.

**Design specification:**
`docs/superpowers/specs/2026-07-28-workspace-os-work-continuity-design.md`

## Global Constraints

- Release the completed skill as `workspace-os` v0.12.0.
- Do not add a root `plans/` directory to generated workspaces.
- Require only `work/{initiative}/README.md`; `plan.md` and supporting folders are optional.
- Package README owns initiative coordination state. Domain and external systems keep their declared
  fields.
- Keep package paths stable after closure; archive is a derived view.
- Use `work/AGENTS.md` as the lifecycle contract and generate `work/CLAUDE.md` as its Claude adapter.
- Do not add an eighth maintenance organ.
- Use only the Python standard library.
- Keep all imports at module top level. Move the existing inline `datetime` import in
  `doctor.py.tmpl` while editing that file.
- Do not create empty optional folders or fabricated learnings.
- Do not infer completion, cancellation, ownership, or an external system's authority.
- Update `project-overview.md` for every new file in this plan.
- Do not create a git commit unless the user explicitly requests one.

---

## File and Interface Map

### New runtime templates

- `workspace-os/assets/work-AGENTS.md.tmpl`: The one managed-work lifecycle contract.
- `workspace-os/assets/work-README.md.tmpl`: Human navigation and derived status/archive views.
- `workspace-os/assets/work-package-README.md.tmpl`: Canonical package metadata and handoff sections.
- `workspace-os/assets/work-plan.md.tmpl`: Optional detailed decomposition without duplicated status.
- `workspace-os/assets/process-input-SKILL.md.tmpl`: Deterministic intake/orchestration template for
  the already-required `{OS}-system-process-input` organ.

### New evaluation surfaces

- `workspace-os/evals/test_work_continuity.py`: Standard-library contract and doctor mutation tests.
- `workspace-os/evals/scenarios/work-continuity/builder-prompt.md`: Agent-visible build prompt.
- `workspace-os/evals/scenarios/work-continuity/session-start.md`: Agent-visible first work session.
- `workspace-os/evals/scenarios/work-continuity/session-resume.md`: Fresh-agent takeover prompt.
- `workspace-os/evals/scenarios/work-continuity/session-discovery.md`: Plan-changing evidence prompt.
- `workspace-os/evals/scenarios/work-continuity/session-close.md`: Review and closeout prompt.
- `workspace-os/evals/scenarios/work-continuity/no-package.md`: Same-turn no-ceremony control.
- `workspace-os/evals/scenarios/work-continuity/oracle.md`: Evaluator-only expectations.
- `workspace-os/evals/baselines/v0.11.1-work-continuity.md`: Observed RED baseline.

### Existing files with coordinated changes

- Builder and taxonomy: `workspace-os/SKILL.md`,
  `workspace-os/references/{blueprint,self-management,domain-inference,skillifying-work,skill-authoring,packaging}.md`.
- Generated instructions and organs:
  `workspace-os/assets/{CLAUDE,routine,doctor-SKILL,doctor.py,janitor-SKILL,compound-learn-SKILL,reflect-SKILL,skillify-SKILL}.tmpl`.
- Evaluation: `workspace-os/evals/{README,rubric,validate,improvements-ledger}.md|py` and existing
  scenario prompts/oracles.
- Distribution and index: `README.md`, `project-overview.md`,
  `packages/workspace-os-v0.12.0.zip`.

---

### Task 1: Establish an honest RED baseline

**Files:**

- Create: `workspace-os/evals/scenarios/work-continuity/builder-prompt.md`
- Create: `workspace-os/evals/scenarios/work-continuity/session-start.md`
- Create: `workspace-os/evals/scenarios/work-continuity/session-resume.md`
- Create: `workspace-os/evals/scenarios/work-continuity/session-discovery.md`
- Create: `workspace-os/evals/scenarios/work-continuity/session-close.md`
- Create: `workspace-os/evals/scenarios/work-continuity/no-package.md`
- Create: `workspace-os/evals/scenarios/work-continuity/oracle.md`
- Create after the run: `workspace-os/evals/baselines/v0.11.1-work-continuity.md`
- Create: `workspace-os/evals/scenarios/research-lab/builder-oracle.md`
- Create: `workspace-os/evals/scenarios/research-lab/use-oracle.md`
- Create: `workspace-os/evals/scenarios/consulting-firm/builder-oracle.md`
- Create: `workspace-os/evals/scenarios/consulting-firm/use-oracle.md`
- Modify: `workspace-os/evals/scenarios/research-lab/kickoff.md:1-15`
- Modify: `workspace-os/evals/scenarios/research-lab/use-script.md:1-28`
- Modify: `workspace-os/evals/scenarios/consulting-firm/kickoff.md:1-19`
- Modify: `workspace-os/evals/scenarios/consulting-firm/use-script.md:1-27`
- Modify: `workspace-os/evals/README.md:11-88`
- Modify: `workspace-os/evals/rubric.md:12-100`
- Modify: `project-overview.md`

**Interfaces:**

- Consumes: frozen `packages/workspace-os-v0.11.1.zip`.
- Produces: agent-visible prompts with no leaked answers, hidden oracles, and a factual failing
  baseline that later tasks must turn green.

- [ ] **Step 1: Add the agent-visible continuity scenario**

Write `builder-prompt.md`:

```markdown
# Builder prompt — product intelligence workspace

Build a Workspace OS for a small product and AI engineering team. We manage product initiatives,
technical research, releases, quality evaluations, and improvements to the agent system itself.
The workspace must remain understandable when work changes hands between engineers and AI agents.
```

Write `session-start.md`:

```markdown
# Session 1 — start consequential work

Start a multi-session initiative to improve how our agents remember and reuse prior product decisions.
Today, inspect the current memory approach, record what you learn, choose the first experiment, and
leave the work in a state another engineer can continue tomorrow. Do not implement the whole system.
```

Write `session-resume.md`:

```markdown
# Session 2 — fresh-agent takeover

You are taking over this workspace with no access to the prior chat. Continue the active
agent-memory initiative from its authoritative current state. Do not repeat completed investigation.
Run the next recorded experiment and leave a clear handoff.
```

Write `session-discovery.md`:

```markdown
# Session 3 — plan-changing evidence

New evidence: the first experiment shows retrieval accuracy is acceptable, but stale decisions are
being returned after their source documents change. Update the initiative to reflect this discovery,
revise the next experiment, and preserve the evidence.
```

Write `session-close.md`:

```markdown
# Session 4 — review and close

The stale-decision invalidation experiment now passes on the agreed fixture. Review the initiative
against its acceptance criteria, close it only if the evidence supports that, and preserve anything
that should make future agent-memory work cheaper or safer.
```

Write `no-package.md`:

```markdown
# Same-turn control

Fix the spelling of "recieve" in the workspace's human README and tell me what changed.
```

- [ ] **Step 2: Add the hidden evaluator oracle**

Write `oracle.md` with explicit per-turn expectations:

```markdown
# Hidden oracle — work continuity

This file is evaluator-only. Never provide it to builder or operator agents.

## Build
- The setup work package exists before discovery output is written.
- The generated root brain routes managed work to `work/AGENTS.md`.
- `work/CLAUDE.md` resolves to or directs Claude to `work/AGENTS.md`.
- The setup package closes only after a doctor run and carries evidence.

## Session 1
- Exactly one package represents the memory initiative.
- Its canonical README records outcome, acceptance, owner, authority, current state, and next action.
- Optional `plan.md` exists only if it contains useful decomposition.

## Session 2
- A fresh agent finds and resumes the same package without prior chat.
- It does not repeat completed investigation.
- It advances the recorded next action and updates the handoff in the same turn.

## Session 3
- Evidence changes the canonical current state and next action in the same turn.
- Raw evidence remains in the package; only settled reusable conclusions enter `knowledge/`.

## Session 4
- Completion is supported by acceptance evidence.
- Domain and package authority remain distinct.
- Durable-value disposition is explicit, including a valid `none` when nothing is reusable.
- The stable package path appears under the completion-year archive view.

## Same-turn control
- No work package is created.
- The change may be logged as a material progress event only if appropriate.
```

- [ ] **Step 3: Remove answer leakage from existing scenarios**

Move each existing `What a strong ...` block verbatim into its matching new oracle file:

- research build: `kickoff.md:11-15` → `builder-oracle.md`;
- research use: `use-script.md:24-28` → `use-oracle.md`;
- consulting build: `kickoff.md:14-19` → `builder-oracle.md`;
- consulting use: `use-script.md:21-27` → `use-oracle.md`.

Leave agent-visible files with only context and realistic user prompts. Add this first line to each
oracle:

```markdown
> Evaluator-only: never pass this file to a builder or operator agent.
```

Correct the stale research oracle phrase `6 organs` to the seven current four-word organs while
moving it. Do not silently preserve obsolete evaluator expectations.

- [ ] **Step 4: Run the baseline before editing `workspace-os`**

1. Extract `packages/workspace-os-v0.11.1.zip` into an ignored run directory.
2. Dispatch one fresh builder using only the frozen skill and `builder-prompt.md`.
3. Snapshot the generated workspace.
4. Dispatch fresh agents for `session-start.md` and `session-resume.md`, one context each.
5. Snapshot after each turn.

Expected RED result: v0.11.1 may create dated output under `work/`, but it cannot provide the required
canonical lifecycle record, exact handoff, or fresh-agent resume behavior because those contracts do
not exist.

- [ ] **Step 5: Record factual baseline evidence**

Write `v0.11.1-work-continuity.md` after the run. Use these exact headings:

- `# Workspace OS v0.11.1 work-continuity baseline`
- `## Verdict`
- `## Frozen input`
- `## Observed build`
- `## Observed handoff`
- `## Contract gaps confirmed`
- `## Evidence paths`

The verdict begins `FAIL — the current skill has no ordinary-work lifecycle or canonical handoff
record.` Under observed build and handoff, quote actual generated paths and fresh-agent behavior.
Under evidence paths, list the ignored run directory and every per-turn snapshot. Do not create the
report before evidence exists and do not invent output.

- [ ] **Step 6: Correct rubric drift before adding new scores**

Update `rubric.md` so:

- build-time structure scores the five-folder lean spine, not on-demand folders;
- the organ requirement names all seven current four-word organs;
- builder/operator prompts and evaluator oracles are explicitly separate;
- add a third `/100` work-continuity rubric covering canonical state (20), fresh-agent resume (20),
  authority/reconciliation (15), blocked/review continuity (10), closure evidence (15), durable-value
  extraction (10), and proportional overhead/no-package control (10).

- [ ] **Step 7: Update eval documentation and overview**

Document per-turn snapshots, hidden oracles, and the RED-before-GREEN requirement in
`evals/README.md`. Add all new paths and purposes to `project-overview.md`.

- [ ] **Step 8: Verify Task 1**

Run:

```bash
git diff --check
```

Expected: exit 0. Confirm the baseline report says `FAIL` and contains observed, not hypothetical,
paths.

---

### Task 2: Add the thin work-package templates

**Files:**

- Create: `workspace-os/assets/work-AGENTS.md.tmpl`
- Create: `workspace-os/assets/work-README.md.tmpl`
- Create: `workspace-os/assets/work-package-README.md.tmpl`
- Create: `workspace-os/assets/work-plan.md.tmpl`
- Create: `workspace-os/assets/process-input-SKILL.md.tmpl`
- Create: `workspace-os/evals/test_work_continuity.py`
- Modify: `project-overview.md`

**Interfaces:**

- Consumes: status, ownership, and lifecycle decisions from the approved design.
- Produces: five templates with one source of coordination truth and a standard-library contract test.

- [ ] **Step 1: Write failing template-contract tests**

Create `test_work_continuity.py`:

```python
from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ASSETS = REPO_ROOT / "workspace-os" / "assets"


class WorkTemplateContractTests(unittest.TestCase):
    def test_required_templates_exist(self) -> None:
        names = {
            "work-AGENTS.md.tmpl",
            "work-README.md.tmpl",
            "work-package-README.md.tmpl",
            "work-plan.md.tmpl",
            "process-input-SKILL.md.tmpl",
        }
        self.assertEqual(names, {path.name for path in ASSETS.iterdir() if path.name in names})

    def test_package_readme_is_the_canonical_record(self) -> None:
        text = (ASSETS / "work-package-README.md.tmpl").read_text(encoding="utf-8")
        for field in ("id:", "status:", "owner:", "updated:"):
            self.assertIn(field, text)
        for heading in (
            "## Outcome",
            "## Done when",
            "## Current state",
            "## Next action",
            "## Blocker or review",
            "## Links and authority",
            "## Evidence and outcome",
            "## Durable value",
        ):
            self.assertIn(heading, text)

    def test_optional_plan_does_not_duplicate_package_state(self) -> None:
        text = (ASSETS / "work-plan.md.tmpl").read_text(encoding="utf-8")
        self.assertNotRegex(text, re.compile(r"^status:", re.MULTILINE | re.IGNORECASE))
        self.assertNotRegex(text, re.compile(r"^owner:", re.MULTILINE | re.IGNORECASE))
        self.assertIn("## Work items", text)

    def test_work_contract_contains_every_lifecycle_status(self) -> None:
        text = (ASSETS / "work-AGENTS.md.tmpl").read_text(encoding="utf-8")
        for status in ("active", "blocked", "paused", "review", "complete", "cancelled"):
            self.assertIn(f"`{status}`", text)

    def test_process_input_uses_the_required_organ_name(self) -> None:
        text = (ASSETS / "process-input-SKILL.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("name: {OS}-system-process-input", text)
        self.assertIn("work/AGENTS.md", text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and observe RED**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: FAIL with missing template files.

- [ ] **Step 3: Create the human work index template**

`work-README.md.tmpl` must say it is a derived view and contain these markers:

```markdown
# Managed work

This is the human navigation view for consequential work. Package `README.md` files own state;
reconcile this index from them instead of editing status here independently.

<!-- WORK-INDEX:START -->
## Active
_None._

## Blocked
_None._

## Paused
_None._

## Review
_None._

## Archive by closure year
_None._
<!-- WORK-INDEX:END -->
```

Generated package rows use this exact shape:

```markdown
- [{WORK_ID}]({PACKAGE_FOLDER}/README.md) — {STATUS} — {OWNER} — updated {YYYY-MM-DD}
```

Nonterminal rows appear under their matching status heading. Complete and cancelled rows appear under
their closure year in the archive view.

- [ ] **Step 4: Create the canonical package template**

`work-package-README.md.tmpl` must contain:

```markdown
---
id: {WORK_ID}
status: active
owner: {OWNER}
updated: {YYYY-MM-DD}
---

# {WORK_TITLE}

## Outcome
{One observable result this initiative intends to create.}

## Done when
- [ ] {Acceptance criterion with evidence.}

## Current state
{Current truth in one short paragraph; do not write a session transcript.}

## Next action
{One exact continuation step, or a work-item ID from plan.md.}

## Blocker or review
Not applicable.

## Links and authority
- Package coordination: this file
- Domain state: {path or "not applicable"}
- External state: {system + owned fields, or "not applicable"}
- Detailed plan: {plan.md or "not needed"}

## Evidence and outcome
No terminal outcome yet.

## Durable value
Not evaluated until a meaningful discovery or closure.
```

The builder replaces every brace placeholder. Terminal packages add `closed: YYYY-MM-DD` to
frontmatter.

- [ ] **Step 5: Create the optional plan template**

`work-plan.md.tmpl`:

```markdown
# {WORK_TITLE} Plan

## Scope
- {In-scope outcome}

## Non-goals
- {Explicitly excluded work}

## Dependencies
- {Dependency or "none"}

## Work items
- [ ] W-001 — {Action with an observable result}

## Research questions
- {Question or "none"}

## Discovered bugs or child initiatives
- {Evidence and link, or "none"}

## Decision and evidence links
- {Path or URL}
```

- [ ] **Step 6: Create the shared work contract**

`work-AGENTS.md.tmpl` must implement these exact sections:

```markdown
# Managed-work contract

## Purpose
A fresh human or agent can recover current truth, take the next correct action, verify closure, and
leave reusable value without prior chat history.

## Read order
1. Root `CLAUDE.md` / `AGENTS.md`.
2. This file.
3. `work/README.md`.
4. The package `README.md`.
5. Optional `plan.md`, package instructions, linked domain records, and latest evidence.

## Create a package when
- another session or agent will probably continue the work;
- a dependency, blocker, or review gate exists;
- research can materially change the approach;
- completion needs durable evidence; or
- the user explicitly asks to track it.

Do not package routine same-turn work. Search before creating and resume equivalent work.

## Status
Use exactly `active`, `blocked`, `paused`, `review`, `complete`, or `cancelled`.
An active package may become blocked, paused, review, complete, or cancelled. Blocked, paused, and
review packages may return to active or become cancelled; review may become complete. Complete and
cancelled packages reopen only through the explicit reopen contract below.

## Start and resume
1. Search the index, package records, linked domain records, and declared external systems first.
2. Resume equivalent work instead of creating a duplicate.
3. Create a package atomically with outcome, acceptance, owner, authority, and first next action.
4. On resume, reread all canonical files from disk and reconcile them with actual artifacts.
5. Continue from the exact next action.

## Update and handoff
- When evidence changes assumptions, scope, acceptance, or sequencing, update the package and optional
  plan in the same turn.
- Before stopping, record last known-good state, exact next action, changed artifacts, verification,
  blockers or review needs, and unresolved assumptions.
- Use blocked, paused, or review when true. Do not claim completion because an agent must stop.
- Reconcile the derived work index and append only material lifecycle events to PROGRESS.md.

## Complete, cancel, and reopen
1. Evaluate every acceptance criterion against linked evidence.
2. Record outcome, remaining work, and linked domain/external reconciliation.
3. Record durable-value disposition, including a valid nothing-reusable reason.
4. Set complete or cancelled plus a closure date; keep the package path stable.
5. Reopening requires an explicit reason, refreshed next action, changed acceptance when applicable,
   and a PROGRESS.md entry.

## Authority
The package owns coordination. Linked domain and external systems keep their declared fields.
`work/README.md` is a derived view; `PROGRESS.md` is history.

## Exceptional package instructions
Create package-level AGENTS.md only for additive constraints unique to that initiative. When it
exists, create a package CLAUDE.md symlink or fallback that directs Claude to the same file. Never put
status, tasks, history, or copied global rules in package instructions.

## Do not
- Do not duplicate domain state in a package.
- Do not invent owners, facts, completion, cancellation, evidence, or learning.
- Do not create empty optional folders.
- Do not move terminal packages merely to represent archive state.
```

- [ ] **Step 7: Create the intake organ template**

`process-input-SKILL.md.tmpl` must:

1. read the root brain and `work/AGENTS.md`;
2. identify or create the correct package only when the threshold is met;
3. file raw input in its dated domain/package home;
4. reconcile package, domain records, board, dashboard, and declared external fields;
5. update assumptions and the optional plan when evidence changes them;
6. extract only settled reusable value;
7. update the package handoff, derived index, and material progress history;
8. run the doctor for consequential changes.

Use valid frontmatter:

```yaml
---
name: {OS}-system-process-input
description: Process new {DOMAIN} files, notes, results, and requests into the correct authoritative records. Use whenever new material arrives, the user says "process this", "file this", "update the workspace", or asks for consequential work that may need a managed handoff.
---
```

- [ ] **Step 8: Run tests and observe GREEN**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: all five template tests PASS.

- [ ] **Step 9: Update the project overview**

Add every new template and `test_work_continuity.py` with one-line purposes to
`project-overview.md`.

---

### Task 3: Wire the builder, taxonomy, and generated brain

**Files:**

- Modify: `workspace-os/SKILL.md:11-151`
- Modify: `workspace-os/references/blueprint.md:1-150`
- Modify: `workspace-os/references/self-management.md:1-91`
- Modify: `workspace-os/references/domain-inference.md:1-52`
- Modify: `workspace-os/references/packaging.md:15-44,174-179`
- Modify: `workspace-os/assets/CLAUDE.md.tmpl:1-93`
- Modify: `workspace-os/assets/routine.md.tmpl:21-37`
- Modify: `workspace-os/references/skill-authoring.md:72-129`
- Modify: `workspace-os/evals/test_work_continuity.py`

**Interfaces:**

- Consumes: Task 2 templates.
- Produces: a builder that creates the setup package before discovery and a generated brain that
  routes all managed work through the shared contract.

- [ ] **Step 1: Add failing builder-contract tests**

Append this class to `test_work_continuity.py`:

```python
class BuilderContractTests(unittest.TestCase):
    def test_builder_bootstraps_managed_work_before_discovery(self) -> None:
        text = (REPO_ROOT / "workspace-os" / "SKILL.md").read_text(encoding="utf-8")
        bootstrap = text.index("Bootstrap managed work")
        discovery = text.index("Discovery & Design")
        self.assertLess(bootstrap, discovery)
        for asset in (
            "work-AGENTS.md.tmpl",
            "work-README.md.tmpl",
            "work-package-README.md.tmpl",
            "process-input-SKILL.md.tmpl",
        ):
            self.assertIn(asset, text)

    def test_generated_brain_routes_to_the_work_contract(self) -> None:
        text = (ASSETS / "CLAUDE.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("work/AGENTS.md", text)
        self.assertIn("another session or agent", text)
        self.assertIn("material lifecycle", text)
        self.assertNotIn("50/50", text)
        self.assertNotIn("at least one durable learning each session", text.lower())

    def test_references_define_coordination_without_copying_domain_state(self) -> None:
        blueprint = (
            REPO_ROOT / "workspace-os" / "references" / "blueprint.md"
        ).read_text(encoding="utf-8")
        self.assertIn("coordination overlay", blueprint.lower())
        self.assertIn("stable", blueprint.lower())
        self.assertIn("derived", blueprint.lower())

    def test_agent_adapters_and_routines_route_managed_work(self) -> None:
        references = REPO_ROOT / "workspace-os" / "references"
        packaging = (references / "packaging.md").read_text(encoding="utf-8")
        routine = (ASSETS / "routine.md.tmpl").read_text(encoding="utf-8")
        self.assertIn("work/CLAUDE.md", packaging)
        self.assertIn("work/AGENTS.md", routine)
```

- [ ] **Step 2: Run tests and observe RED**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: template tests PASS; new builder tests FAIL.

- [ ] **Step 3: Add Phase -1 bootstrap to `SKILL.md`**

Before current Phase 0, add `## Phase -1 — Bootstrap managed work`:

- create `work/README.md` from `work-README.md.tmpl`;
- create `work/AGENTS.md` and `work/CLAUDE.md` adapter;
- create `work/workspace-os-setup/README.md` from the package template;
- create `work/workspace-os-setup/plan.md` because setup is multi-phase;
- record setup as `active`, with Workspace OS verification as acceptance;
- send Phase 0 brief, research, review, and later build evidence into that package.

Do not scaffold any other workspace folders before discovery.

- [ ] **Step 4: Update the operating beliefs and taxonomy**

Replace the binary "one-off vs system" framing with:

- domain flow stays in pipeline/entities;
- consequential execution gets a linked work package;
- compounding outputs graduate to existing permanent homes;
- same-turn work remains lightweight.

Update `work/` definitions in `SKILL.md` and `blueprint.md` from "one-off output" to "managed
execution and dated one-off output." Preserve existing dated activity folders.

- [ ] **Step 5: Scaffold the work control surface and intake organ**

In Phase 2, require the builder to:

- customize every work template placeholder;
- create the work index and shared instructions;
- generate the Claude adapter;
- author `{OS}-system-process-input` from `process-input-SKILL.md.tmpl` instead of improvising it;
- keep package-specific instructions absent by default.

At final report, close `workspace-os-setup` only after acceptance evidence and the final doctor report
are linked.

- [ ] **Step 6: Update `self-management.md` and `CLAUDE.md.tmpl`**

Add the approved start/resume/discover/handoff/close contract, field-level authority, stable archive
view, and exact package threshold.

Change `PROGRESS.md` from "every session, no exceptions" to material lifecycle events.

Change learning from a quota to:

```markdown
After a meaningful discovery or closure, evaluate whether anything is genuinely reusable. Capture
it with provenance when yes; record a clean "nothing reusable" disposition when no.
```

Replace the 50/50 quota with:

```markdown
After meaningful work, inspect whether observed friction justifies improving the machinery. A
grounded no-op is valid.
```

- [ ] **Step 7: Update domain inference and skill authoring**

Add these Understanding Brief fields:

- likely cross-session initiatives;
- package creation threshold examples for the domain;
- authority map for package, domain records, and external systems;
- expected handoff/review cadence.

Update the organ roster to say process-input comes from its template. Remove remaining 50/50 wording.

- [ ] **Step 8: Update adapter and unattended-run guidance**

Update `packaging.md` with the nested `work/AGENTS.md` plus `work/CLAUDE.md` adapter and the root
fallback requirement. Update `routine.md.tmpl` so a routine that creates, resumes, changes, or closes
managed work reads `work/AGENTS.md`, the package README, and optional plan before acting.

- [ ] **Step 9: Run tests and observe GREEN**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: template and builder contract tests PASS.

---

### Task 4: Add deterministic work-package health checks

**Files:**

- Modify: `workspace-os/assets/doctor.py.tmpl:14-275`
- Modify: `workspace-os/assets/doctor-SKILL.md.tmpl:12-73`
- Modify: `workspace-os/evals/validate.py:19-290`
- Modify: `workspace-os/evals/test_work_continuity.py`

**Interfaces:**

- Consumes: package frontmatter, required headings, and work-index markers from Tasks 2–3.
- Produces: report-only mechanical findings prefixed `work package:` and semantic doctor guidance.

- [ ] **Step 1: Write failing doctor mutation tests**

Add top-level imports to `test_work_continuity.py`:

```python
import subprocess
import tempfile
```

Add helpers:

```python
def render_doctor(workspace: Path) -> Path:
    template = (ASSETS / "doctor.py.tmpl").read_text(encoding="utf-8")
    rendered = (
        template.replace("{DOMAIN}", "Test")
        .replace("{OS}", "test")
        .replace("{PIPELINE}", "pipeline")
        .replace("{ENTITY}", "entities")
    )
    script = workspace / "scripts" / "doctor.py"
    script.parent.mkdir(parents=True, exist_ok=True)
    script.write_text(rendered, encoding="utf-8")
    return script


def package_text(
    *,
    work_id: str = "memory-rd",
    status: str = "active",
    next_action: str = "Run W-002.",
    blocker: str = "Not applicable.",
    evidence: str = "No terminal outcome yet.",
    durable_value: str = "Not evaluated until closure.",
    closed: str = "",
) -> str:
    closed_line = f"closed: {closed}\n" if closed else ""
    return f"""---
id: {work_id}
status: {status}
owner: Test Owner
updated: 2026-07-28
{closed_line}---

# Memory R&D

## Outcome
Make agent decisions reusable.

## Done when
- [ ] A fresh agent retrieves the current decision.

## Current state
The baseline is recorded.

## Next action
{next_action}

## Blocker or review
{blocker}

## Links and authority
- Package coordination: this file

## Evidence and outcome
{evidence}

## Durable value
{durable_value}
"""


def run_doctor(workspace: Path) -> str:
    script = render_doctor(workspace)
    result = subprocess.run(
        ["python3", str(script), str(workspace)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout
```

Add `WorkDoctorMutationTests` covering:

```python
def write_package(workspace: Path, folder: str, text: str) -> Path:
    package = workspace / "work" / folder
    package.mkdir(parents=True, exist_ok=True)
    readme = package / "README.md"
    readme.write_text(text, encoding="utf-8")
    return readme


def write_work_contract(workspace: Path, entries: list[tuple[str, str]]) -> None:
    work = workspace / "work"
    work.mkdir(parents=True, exist_ok=True)
    (work / "AGENTS.md").write_text("# Managed-work contract\n", encoding="utf-8")
    (work / "CLAUDE.md").symlink_to("AGENTS.md")
    lines = [
        "# Managed work",
        "",
        "<!-- WORK-INDEX:START -->",
        *[
            f"- [{folder}]({folder}/README.md) — {status} — Test Owner — updated 2026-07-28"
            for folder, status in entries
        ],
        "<!-- WORK-INDEX:END -->",
        "",
    ]
    (work / "README.md").write_text("\n".join(lines), encoding="utf-8")


def work_findings(output: str) -> list[str]:
    return [
        line
        for line in output.splitlines()
        if "[FINDING] work package:" in line
    ]


class WorkDoctorMutationTests(unittest.TestCase):
    def test_valid_active_package_has_no_work_findings(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertEqual([], work_findings(run_doctor(workspace)))

    def test_duplicate_ids_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            write_package(workspace, "memory-copy", package_text())
            write_work_contract(
                workspace,
                [("memory-rd", "active"), ("memory-copy", "active")],
            )
            self.assertTrue(
                any("duplicate id" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_invalid_status_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="finished"))
            write_work_contract(workspace, [("memory-rd", "finished")])
            self.assertTrue(
                any("invalid status" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_missing_required_heading_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            text = package_text().replace("## Done when", "## Acceptance")
            write_package(workspace, "memory-rd", text)
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("missing section" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_active_package_requires_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(next_action="Not applicable."))
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("next action" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_blocked_package_requires_continuation_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="blocked"))
            write_work_contract(workspace, [("memory-rd", "blocked")])
            self.assertTrue(
                any("blocked details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_paused_package_requires_restart_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="paused"))
            write_work_contract(workspace, [("memory-rd", "paused")])
            self.assertTrue(
                any("paused details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_review_package_requires_review_details(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="review"))
            write_work_contract(workspace, [("memory-rd", "review")])
            self.assertTrue(
                any("review details" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_terminal_package_requires_closeout(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="complete"))
            write_work_contract(workspace, [("memory-rd", "complete")])
            self.assertTrue(
                any("terminal closeout" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_broken_relative_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            text = package_text().replace(
                "- Package coordination: this file",
                "- Evidence: [missing](missing.md)",
            )
            write_package(workspace, "memory-rd", text)
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("broken link" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_empty_optional_folder_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text())
            (workspace / "work" / "memory-rd" / "research").mkdir()
            write_work_contract(workspace, [("memory-rd", "active")])
            self.assertTrue(
                any("empty optional" in line for line in work_findings(run_doctor(workspace)))
            )

    def test_index_status_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            write_package(workspace, "memory-rd", package_text(status="active"))
            write_work_contract(workspace, [("memory-rd", "blocked")])
            self.assertTrue(
                any("index mismatch" in line for line in work_findings(run_doctor(workspace)))
            )
```

- [ ] **Step 2: Run tests and observe RED**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: existing tests PASS; mutation tests FAIL because `doctor.py.tmpl` has no work checks.

- [ ] **Step 3: Implement work parsing in `doctor.py.tmpl`**

Move `import datetime` to the top-level import block.

Add:

```python
WORK_STATUSES = {"active", "blocked", "paused", "review", "complete", "cancelled"}
WORK_HEADINGS = {
    "Outcome",
    "Done when",
    "Current state",
    "Next action",
    "Blocker or review",
    "Links and authority",
    "Evidence and outcome",
    "Durable value",
}
TERMINAL_WORK_STATUSES = {"complete", "cancelled"}
OPTIONAL_WORK_DIRS = {"research", "notes", "deliverables"}
EMPTY_WORK_VALUES = {
    "",
    "not applicable.",
    "no terminal outcome yet.",
    "not evaluated until closure.",
    "_none_.",
}
```

Implement the focused helpers and checker:

```python
def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse scalar key/value fields from the opening YAML frontmatter block."""
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if field:
            fields[field.group(1)] = field.group(2).strip().strip("\"'")
    return fields


def parse_h2_sections(text: str) -> dict[str, str]:
    """Return level-two heading content keyed by heading text."""
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[match.group(1)] = text[match.end():end].strip()
    return sections


def iter_work_packages(ws: str) -> list[str]:
    """Return direct work/ child directories that contain README.md, excluding hidden directories."""
    base = os.path.join(ws, "work")
    if not os.path.isdir(base):
        return []
    packages = []
    for name in sorted(os.listdir(base)):
        package = os.path.join(base, name)
        if name.startswith(".") or not os.path.isdir(package):
            continue
        if os.path.isfile(os.path.join(package, "README.md")):
            packages.append(package)
    return packages


def local_markdown_links(text: str) -> list[str]:
    """Return relative local markdown link targets, excluding URLs, anchors, and mail links."""
    links = []
    for raw_target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = raw_target.strip().strip("<>")
        target = target.split(" ", 1)[0]
        if not target or target.startswith("#"):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        links.append(target)
    return links


def has_work_value(value: str) -> bool:
    """Return whether a package section carries meaningful state."""
    return value.strip().lower() not in EMPTY_WORK_VALUES


def check_work_packages(ws: str) -> None:
    """Emit deterministic lifecycle, link, optional-folder, ID, and index findings."""
    before = len(findings)
    work_root = os.path.join(ws, "work")
    if not os.path.isdir(work_root):
        find("work package: work/ is missing")
        return

    index_text = read(os.path.join(work_root, "README.md"))
    if not index_text:
        find("work package: work/README.md derived index is missing")

    packages = iter_work_packages(ws)
    if not packages:
        find("work package: no managed package exists, including workspace-os-setup")
        return

    ids: dict[str, list[str]] = {}
    for package in packages:
        name = os.path.basename(package)
        readme_path = os.path.join(package, "README.md")
        text = read(readme_path)
        metadata = parse_frontmatter(text)
        sections = parse_h2_sections(text)

        work_id = metadata.get("id", "")
        if not work_id:
            find(f"work package: {name} missing id")
        else:
            ids.setdefault(work_id, []).append(name)

        status = metadata.get("status", "")
        if status not in WORK_STATUSES:
            find(f"work package: {name} invalid status {status!r}")
        if not metadata.get("owner"):
            find(f"work package: {name} missing owner")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", metadata.get("updated", "")):
            find(f"work package: {name} missing valid updated date")

        missing_sections = sorted(WORK_HEADINGS - sections.keys())
        if missing_sections:
            find(f"work package: {name} missing section(s) {missing_sections}")

        next_action = sections.get("Next action", "")
        details = sections.get("Blocker or review", "")
        if status == "active" and not has_work_value(next_action):
            find(f"work package: {name} active work has no next action")

        detail_fields = {
            "blocked": ("Responsible:", "Condition:", "Check:"),
            "paused": ("Responsible:", "Restart:", "Check:"),
            "review": ("Reviewer:", "Question:", "Check:"),
        }
        if status in detail_fields and not all(
            field.lower() in details.lower() for field in detail_fields[status]
        ):
            find(f"work package: {name} {status} details are incomplete")

        if status in TERMINAL_WORK_STATUSES:
            evidence = sections.get("Evidence and outcome", "")
            durable = sections.get("Durable value", "")
            valid_closed = re.fullmatch(r"\d{4}-\d{2}-\d{2}", metadata.get("closed", ""))
            if not valid_closed or not has_work_value(evidence) or not has_work_value(durable):
                find(f"work package: {name} terminal closeout is incomplete")

        for target in local_markdown_links(text):
            path_only = target.split("#", 1)[0]
            if path_only and not os.path.exists(os.path.normpath(os.path.join(package, path_only))):
                find(f"work package: {name} broken link {target!r}")

        for optional in OPTIONAL_WORK_DIRS:
            optional_path = os.path.join(package, optional)
            if os.path.isdir(optional_path) and not any(os.scandir(optional_path)):
                find(f"work package: {name} empty optional folder {optional}/")

        index_line = next(
            (
                line
                for line in index_text.splitlines()
                if f"({name}/README.md)" in line
            ),
            "",
        )
        if not index_line:
            find(f"work package: {name} missing from derived index")
        elif status in WORK_STATUSES and f"— {status} —" not in index_line:
            find(f"work package: {name} index mismatch for status {status!r}")

    for work_id, names in ids.items():
        if len(names) > 1:
            find(f"work package: duplicate id {work_id!r} in {names}")

    if len(findings) == before:
        ok(f"work packages: {len(packages)} valid package(s)")
```

All emitted failures start with `work package:` so tests can distinguish them from unrelated doctor
findings. Call `check_work_packages(ws)` from `main()` before `check_progress(ws)`.

- [ ] **Step 4: Add static build checks in `validate.py`**

Add:

```python
def check_work_contract(ws: str, r: Report) -> None:
    work = os.path.join(ws, "work")
    got = 0.0
    notes = []

    if os.path.isfile(os.path.join(work, "README.md")):
        got += 2
    else:
        notes.append("work/README.md missing")

    if os.path.isfile(os.path.join(work, "AGENTS.md")):
        got += 2
    else:
        notes.append("work/AGENTS.md missing")

    claude_adapter = os.path.join(work, "CLAUDE.md")
    adapter_text = read(claude_adapter).lower()
    if os.path.islink(claude_adapter) or "agents.md" in adapter_text:
        got += 1
    else:
        notes.append("work/CLAUDE.md adapter missing")

    setup_readme = os.path.join(work, "workspace-os-setup", "README.md")
    if os.path.isfile(setup_readme):
        got += 1
    else:
        notes.append("workspace-os setup package missing")

    root_brain = read(os.path.join(ws, "CLAUDE.md")).lower()
    if "work/agents.md" in root_brain and "another session or agent" in root_brain:
        got += 2
    else:
        notes.append("root brain does not route managed work")

    r.add(
        "work_contract",
        got,
        8,
        "PASS" if got == 8 else ("WARN" if got >= 5 else "FAIL"),
        "; ".join(notes) or "managed-work control surface complete",
    )
```

Call it from `main()` after `check_brain`. Increase the documented auto maximum consistently in
`rubric.md`; do not preserve a misleading fixed subtotal.

- [ ] **Step 5: Extend the semantic doctor checklist**

In `doctor-SKILL.md.tmpl`, add judgment checks for:

- package threshold quality;
- acceptance criteria and evidence quality;
- copied/contradictory domain state;
- abandoned active work;
- terminal closeout and provenance;
- archive-view accuracy.

Keep the skill report-only. Use "report-only" consistently rather than claiming no file is written,
because it writes `operations/health.md`.

- [ ] **Step 6: Run mutation tests and observe GREEN**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
python3 -m py_compile workspace-os/evals/validate.py
```

Expected: all tests PASS; Python compilation exits 0.

---

### Task 5: Connect closure to maintenance and compounding organs

**Files:**

- Modify: `workspace-os/assets/janitor-SKILL.md.tmpl:8-26`
- Modify: `workspace-os/assets/compound-learn-SKILL.md.tmpl:3-22`
- Modify: `workspace-os/assets/reflect-SKILL.md.tmpl:8-32`
- Modify: `workspace-os/assets/skillify-SKILL.md.tmpl:8-46`
- Modify: `workspace-os/references/skillifying-work.md:1-45`
- Modify: `workspace-os/references/skill-authoring.md:72-129`
- Modify: `workspace-os/evals/test_work_continuity.py`

**Interfaces:**

- Consumes: explicit package closure and durable-value disposition.
- Produces: event-driven learning, provenance-linked skillification, replay-verified system
  improvements, and a janitor that never changes ambiguous intent.

- [ ] **Step 1: Write failing organ-contract tests**

Append:

```python
class OrganContractTests(unittest.TestCase):
    def test_janitor_never_invents_terminal_state(self) -> None:
        text = (ASSETS / "janitor-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("never complete or cancel", text)
        self.assertIn("derived work index", text)

    def test_learning_is_event_driven_and_allows_clean_noop(self) -> None:
        text = (ASSETS / "compound-learn-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("meaningful discovery or closure", text)
        self.assertIn("nothing reusable", text)
        self.assertNotIn("every session", text)

    def test_reflect_distinguishes_applied_from_verified(self) -> None:
        text = (ASSETS / "reflect-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        for status in ("proposed", "applied", "verified", "rejected"):
            self.assertIn(status, text)
        self.assertIn("replay", text)
        self.assertNotIn("50/50", text)

    def test_skillify_uses_package_provenance(self) -> None:
        text = (ASSETS / "skillify-SKILL.md.tmpl").read_text(encoding="utf-8").lower()
        self.assertIn("package", text)
        self.assertIn("provenance", text)
        self.assertIn("staged", text)
```

- [ ] **Step 2: Run tests and observe RED**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: new organ tests FAIL against v0.11.1 templates.

- [ ] **Step 3: Update the janitor**

Add safe actions:

- regenerate the derived work index from package records;
- repair unambiguous local links;
- flag active work without a next action;
- flag blocked/paused/review work past its check date;
- invoke learn/reflect/skillify only after explicit closure.

Add the exact prohibition:

```markdown
Never complete or cancel work, invent an owner or next action, or manufacture a learning when intent
is ambiguous. Flag it for the user.
```

- [ ] **Step 4: Make learning event-driven**

Change the learn description and workflow to trigger after a meaningful discovery or closure. Require
provenance links from promoted knowledge back to the package evidence. Make this terminal state
explicit:

```markdown
Nothing reusable — record the reason in the package and create no knowledge, template, or skill.
```

- [ ] **Step 5: Make reflection replay-verifiable**

Reflect scans terminal and failed packages plus real health findings. Use statuses:

```text
proposed → applied → verified | rejected
```

An applied change becomes verified only after a replay, fresh-context eval, or later package proves
the improvement. Remove 50/50 quota language while retaining the grounded-friction requirement.

- [ ] **Step 6: Normalize skillify provenance and staging**

Require a source package when one exists. Stage under:

```text
work/{source-initiative}/YYYY-MM-DD-skillify-{name}/
```

If no package exists and skillification itself crosses the package threshold, create a managed
skillification package first. Keep explicit approval before publication and retain the unattended
staged-only policy.

- [ ] **Step 7: Update skillifying references**

Apply the same provenance/staging rules in `skillifying-work.md` and `skill-authoring.md`. Remove old
direct-root staging examples that would bypass package validation.

- [ ] **Step 8: Run tests and observe GREEN**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_work_continuity.py" -v
```

Expected: all template, builder, doctor, and organ tests PASS.

---

### Task 6: Prove fresh-agent continuity end to end

**Files:**

- Modify: `workspace-os/evals/README.md`
- Modify: `workspace-os/evals/rubric.md`
- Modify: `workspace-os/evals/improvements-ledger.md`
- Create in ignored runs: `workspace-os/evals/runs/{timestamp}/work-continuity/...`
- Potential corrective files, only when a failing test identifies the owning seam:
  `workspace-os/SKILL.md`, `workspace-os/assets/*.tmpl`, `workspace-os/references/*.md`,
  `workspace-os/evals/test_work_continuity.py`

**Interfaces:**

- Consumes: complete v0.12.0 candidate and Task 1 hidden oracle.
- Produces: three independent, per-turn evidence trails and a ledger entry that is only marked
  verified if all required continuity behavior passes.

- [ ] **Step 1: Run static and mutation checks**

Run:

```bash
python3 -m unittest discover -s workspace-os/evals -p "test_*.py" -v
python3 -m py_compile workspace-os/evals/validate.py
git diff --check
```

Expected: all tests PASS; compilation and diff check exit 0.

- [ ] **Step 2: Run three fresh-context scenario repetitions**

For each repetition:

1. dispatch a fresh builder with only the candidate skill and `builder-prompt.md`;
2. snapshot the setup-complete workspace;
3. dispatch separate fresh agents for start, resume, discovery, and close;
4. snapshot after every turn;
5. run the generated doctor after every turn;
6. run the no-package control in a separate fresh context;
7. score against `oracle.md`, never against agent self-report.

Expected:

- mechanical invariants pass 3/3;
- the second agent resumes the same package 3/3;
- no repeated completed investigation;
- discovery updates current truth in the same turn;
- closeout has evidence and disposition;
- the no-package control creates no package;
- no invented facts or filler learning.

- [ ] **Step 3: Fix only evidence-backed failures**

For each failure:

1. record the exact run, turn, file, and mismatch;
2. change the smallest owning seam;
3. add or tighten a mutation/contract test;
4. rerun the failed scenario with a fresh agent;
5. rerun the full static suite.

Do not add speculative rules unrelated to observed failures.

- [ ] **Step 4: Update the improvements ledger**

Add one finding grounded in the RED baseline:

```markdown
| 8 | HIGH | Ordinary cross-session work had no canonical lifecycle or fresh-agent handoff record. | v0.11.1 work-continuity baseline + per-turn snapshots | Add the thin work-package contract, package-aware organs, doctor checks, and fresh-agent continuity eval. | verified |
```

Use `applied` instead of `verified` unless all three candidate repetitions pass.

- [ ] **Step 5: Save a concise candidate report**

Write the run report under the ignored run directory and summarize:

- baseline comparison;
- per-turn package state;
- doctor findings;
- fresh-agent resume result;
- no-package result;
- any applied versus verified improvements.

---

### Task 7: Version, package, and document the verified release

**Files:**

- Modify: `workspace-os/SKILL.md:1-7`
- Modify: `README.md:17-27`
- Modify: `project-overview.md`
- Create: `packages/workspace-os-v0.12.0.zip`

**Interfaces:**

- Consumes: fully passing Task 6 candidate.
- Produces: discoverable v0.12.0 source, repository documentation, and a tested distribution archive
  that excludes eval-only files.

- [ ] **Step 1: Bump skill metadata**

Set:

```yaml
metadata:
  author: Sidney Swift
  version: "0.12.0"
```

Update the description only as needed to include managed cross-session work; keep it trigger-focused
and under the Agent Skills metadata limit.

- [ ] **Step 2: Update public and project documentation**

Update the Workspace OS row in root `README.md` to mention verified work continuity and handoff.

In `project-overview.md`:

- list every new template, test, scenario, oracle, and baseline;
- move the design and plan from "active" to implemented documentation only after Task 6 passes;
- record `packages/workspace-os-v0.12.0.zip`.

- [ ] **Step 3: Build the distribution archive**

From repository root:

```bash
zip -rq "packages/workspace-os-v0.12.0.zip" "workspace-os" \
  -x "workspace-os/evals/*" "*.DS_Store" "*/__pycache__/*"
```

Expected: archive created with `workspace-os/SKILL.md`, `workspace-os/references/`, and
`workspace-os/assets/`, but no eval harness.

- [ ] **Step 4: Verify the package and full repository diff**

Run:

```bash
unzip -t "packages/workspace-os-v0.12.0.zip"
unzip -l "packages/workspace-os-v0.12.0.zip"
python3 -m unittest discover -s workspace-os/evals -p "test_*.py" -v
python3 -m py_compile workspace-os/evals/validate.py
git diff --check
git status --short
```

Expected:

- ZIP integrity reports no errors;
- ZIP listing excludes `workspace-os/evals/`;
- all unit and mutation tests pass;
- Python compilation and diff check exit 0;
- status contains only intended source, evaluation, documentation, and package changes.

- [ ] **Step 5: Perform the final spec-coverage review**

Check every requirement in the approved design against an implemented file or passing scenario.
Specifically confirm:

- one required package record;
- optional plan;
- stable archive view;
- root instruction fallback and Claude adapter;
- field-level authority;
- setup dogfooding;
- evidence-gated closure;
- event-driven learning;
- applied-versus-verified improvements;
- balanced doctor/janitor behavior;
- fresh-agent resume and same-turn no-package control.

Do not commit unless the user separately asks for a commit.
