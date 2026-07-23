---
name: workspace-os
description: Spin up a complete workspace operating system for any domain that both manages itself and improves itself — from a kickoff input (files, transcripts, or just a prompt). Before scaffolding it deeply interviews the user, scans available connectors/MCPs for context, researches the domain, and has a systems-designer review its plan. Then it scaffolds a lean spine, writes a self-managing and self-updating CLAUDE.md mirrored to AGENTS.md, authors domain skills named {OS}-{area}-{verb}-{noun}, packages them into an installable plugin with a marketplace manifest, wires a never-stale janitor (with a read-only doctor) on a schedule, keeps a PROGRESS.md log, and builds compound-learning and self-improvement loops so the system stays current and gets better at running itself over time. Make sure to use this skill whenever the user wants to set up a workspace, build or scaffold a workspace/operating system, organize a project, turn files or notes into a managed system, or stand up an OS for a new domain — even if they don't say "operating system." Domain-agnostic: consulting, product management, a record label, research, an agency, personal projects, anything.
metadata:
  author: Sidney Swift
  version: "0.11.0"
---

# Workspace OS Builder

**The point is not the folders — it's to scaffold a system that both manages itself and improves
itself.** It keeps its own state current (never-stale) *and* gets better at its own job over time:
compounding knowledge, promoting repeated work into new skills, and improving its own machinery. Hold
that as the goal of every phase below; the structure only exists to serve it.

Concretely, turn a kickoff input into a living operating system: a lean folder structure, a
self-managing **and self-updating** `CLAUDE.md` (mirrored to `AGENTS.md`), a `plugin/` directory (an
in-place installable plugin with skills inside, plus a marketplace manifest), a never-stale janitor
backed by a read-only doctor, an append-only `PROGRESS.md`, a compound-learning loop, and a
self-improvement loop. The plugin is named `{OS}-os` (the OS slug is the owner's name for a personal OS,
the domain for a domain OS) and includes manifests/adapters for Claude, Cursor, and Codex.

This builder skill is for the agent running it. Follow the phases in order. Don't stop halfway — drive to a working OS,
then report. Read the references as you reach each phase.

**Express escape hatch.** The default is the full discovery flow (Phase 0). If the user says "just
build it", "skip discovery", or similar, skip Phase 0's interview/scan/research/review and go straight
to Phase 1 using best-judgment inference from whatever input you have.

## Operating beliefs (apply to every OS you build)

Every belief below serves one goal: a system that **manages itself** (stays current) and **improves
itself** (compounds its knowledge, its capabilities, and its own machinery).

1. **Separate what compounds from what flows.** Compounding = reusable assets that improve every
   time (templates, knowledge base, skills, proof). Flowing = instances moving through stages
   (deals, tickets, releases, experiments). Wire feedback so every flowing instance deposits back
   into a compounding asset.
2. **Never stale.** It is the agent's job to manage state. Any time new input arrives OR the user
   works in the OS, every file/folder that should change gets touched in the same turn. A janitor
   skill + scheduled task is the safety net.
3. **Compound learning.** Every session makes the system smarter — capture decisions, recurring
   answers, and patterns into the knowledge base. Never solve the same thing twice.
4. **Skillify proven repeatable work.** After finishing work, ask whether it will be done again or
   maintained. If yes, promote the proven process into a staged, verified skill in `plugin/skills/`.
   One-off work stays in `work/` (dated) — it never becomes its own top-level folder.
5. **Self-describing and self-updating.** Every folder explains its own purpose; the `CLAUDE.md`
   encodes where new things go — and the agent updates that brain the moment the system changes, so it
   never lies about reality.
6. **Evidence over confidence.** "Done", "consistent", and "reachable" are decided by a checkable
   surface — a doctor run, a skill's verification, a reachable trigger — not the agent's feeling.
7. **Scaffold to the bone; grow on demand.** Start with the minimal spine and let the agent (and each
   organ) create top-level folders the moment real material needs them. A row of empty folders is the
   smell to avoid.

## Phase 0 — Discovery & Design (interview, scan, research, review)

The quality of the OS depends on understanding the person and the domain *before* scaffolding. Read
`references/domain-inference.md`. Do all of the below unless the user invoked the express hatch.

- **0.1 Interview deeply — open-ended, not multiple choice.** Ask broad questions and let the user
  brain-dump; one question at a time, follow the threads. Use the interview technique from the
  `problem-mining` / `finding-unknowns` skills as your model. Cover: what this OS is for, who uses it,
  whether it's a **personal** OS (slug = their name, e.g. `daniel`) or a **domain** OS (slug = the
  domain, e.g. `consulting`), the domains/areas it spans, the recurring work, how they'll run it
  (themselves vs. remote/scheduled agents), and what "good" looks like. Ingest any files/transcripts fully.
- **0.2 Scan connectors/MCPs for context.** Dispatch subagents to enumerate the available MCP
  servers/connectors and, where relevant, use them to pull real context the user didn't think to supply
  (their CRM, tracker, drive, repos, analytics). Fold what they find into the brief.
- **0.3 Research the domain.** Dispatch parallel subagents to research best practices, standard
  lifecycles, and common tooling for the domain(s), so the taxonomy reflects how the domain actually works.
- **0.4 Write the Understanding Brief + a spec plan.** Domain archetype, core unit of work, lifecycle
  stages, entities, compounding assets, recurring tasks (skill candidates), metrics, external tools —
  plus the proposed lean structure and the skills you intend to author.
- **0.5 Adversarial design review.** Dispatch a subagent acting as a skeptical **10x systems designer**
  to challenge the spec: cut over-engineering, confirm the spine is lean, catch missing pieces, and
  push back on complexity. Fold in its notes. Do not over-build.
- **0.6 Confirm the brief** with the user if anything material is ambiguous, then build.

## Phase 1 — Design the taxonomy (lean spine + grow on demand)

Read `references/blueprint.md`.

- The **spine that is always created**: `plugin/` (the in-place plugin), `routines/` (runnable prompts
  for scheduled/remote runs), `scripts/` (reusable executables like `scripts/doctor.py`), `docs/`
  (human-facing docs), `work/` (one-off output), plus the root files `README.md`, `CLAUDE.md`,
  `AGENTS.md`, `PROGRESS.md`.
- **Everything else is created on demand** — `operations/`, `knowledge/`, `library/`, `artifacts/`, the
  flowing `{pipeline}/` and `{entities}/` folders, and optional folders (`reference/ proof/ content/
  business/`). Don't pre-make them; the agent and the organs create each when real material needs it
  (the doctor makes `operations/` on its first run; the learn skill makes `knowledge/` on first capture).
- **Keep every top-level folder AND file name a single lowercase word.** Skill folders under
  `plugin/skills/` are the exception — they follow the 4-word `{OS}-{area}-{verb}-{noun}` convention.
- Predict the domain's flowing structure ({pipeline} stages, {entities}) and compounding assets so the
  agent knows where they'll go, but express that as the brief + `CLAUDE.md` filing tree, not as empty dirs.

## Phase 2 — Scaffold the spine + the brain

- Create only the spine (Phase 1). Give every non-obvious folder a short `README.md` stub.
- Seed `PROGRESS.md` with a header and the first entry (the build itself): `## YYYY-MM-DD` then
  `- **Built the {DOMAIN} OS** — scaffolded the spine, brain, and plugin from {kickoff}.`
- Scaffold `routines/` from `assets/routine.md.tmpl`: seed `routines/janitor.md`, `routines/reflect.md`,
  `routines/capture-learning.md`, plus a stub per recurring remote workflow, and a `routines/README.md`
  index listing each with its cadence + an `armed: no` marker (the doctor reads this).
- Write the self-managing, **self-updating** `CLAUDE.md` from `assets/CLAUDE.md.tmpl`, customized to the
  OS (fill `{OS}`, `{DOMAIN}`, `{PIPELINE}`, `{ENTITY}`). It must carry: the two work modes (one-off vs
  system), the auto-manage loop, the never-stale contract, the self-updating-brain rule, the
  PROGRESS.md append rule, the 4-word skill-naming rule, grow-on-demand, and the filing tree. Read
  `references/self-management.md` for the required contracts.
- Create `AGENTS.md` as a symlink to `CLAUDE.md` (`ln -s CLAUDE.md AGENTS.md`). If symlinks aren't
  supported, write an `AGENTS.md` that says "See CLAUDE.md" — but prefer the symlink.

## Phase 3 — Seed compounding assets (only what has material)

- If the input already contains reusable instruments or settled answers, create `library/` and/or
  `knowledge/` and seed them (templates/checklists in `library/`; faqs/insights/decisions/sops in
  `knowledge/`). If there's nothing real to seed yet, leave them uncreated — the organs make them on
  first use. Rule of thumb: if you'd *use* it to make something it's `library/`; if you'd *consult* it
  it's `knowledge/`.
- With sparse input, seed a few sensible starter templates and mark them "draft — confirm".

## Phase 4 — Author skills (the in-place `plugin/`)

Read `references/skill-authoring.md` (naming convention + roster) and `references/skillifying-work.md`.

- **Name every skill `{OS}-{area}-{verb}-{noun}`** (4 kebab words; maintenance organs use `area = system`).
- Scaffold `plugin/` as a real plugin in place: `plugin/.claude-plugin/plugin.json` from
  `assets/claude-plugin.json.tmpl`, `plugin/.claude-plugin/marketplace.json` from
  `assets/marketplace.json.tmpl`, `plugin/.codex-plugin/plugin.json` from
  `assets/codex-plugin.json.tmpl`, and a `plugin/skills/` directory. The Codex manifest must include
  `"skills": "./skills/"`; all three share the `{OS}-os` name. See `references/packaging.md`.
- Create `.agents/skills` as a symlink to `../plugin/skills`. If symlinks aren't supported, copy and
  note it's a compatibility mirror.
- Always author the maintenance organs from the templates (renamed to the convention):
  - **`{OS}-system-check-health`** (doctor, `assets/doctor-SKILL.md.tmpl`) — read-only verification
    surface (health score + punch list to `operations/health.md`). Also generate `scripts/doctor.py`
    from `assets/doctor.py.tmpl` (fill `PIPELINE`/`ENTITY`/`OS`) as its deterministic fast path.
  - **`{OS}-system-fix-drift`** (janitor, `assets/janitor-SKILL.md.tmpl`) — run the doctor, then fix what's safe.
  - **`{OS}-system-capture-learning`** (learn, `assets/compound-learn-SKILL.md.tmpl`) — capture knowledge.
  - **`{OS}-system-improve-machinery`** (reflect, `assets/reflect-SKILL.md.tmpl`) — improve the OS itself.
  - **`{OS}-system-promote-skill`** (skillify, `assets/skillify-SKILL.md.tmpl`) — promote proven work.
  - **`{OS}-system-process-input`** (intake) — the auto-manage loop as one trigger.
  - **`{OS}-system-find-unknowns`** — pre-work discovery; author it by reading the `finding-unknowns`
    skill at github.com/sidneyswift/skills/tree/main/finding-unknowns and adapting it to this OS's naming.
- For each recurring task in the brief, author `plugin/skills/{OS}-{area}-{verb}-{noun}/SKILL.md`
  (frontmatter `name` + trigger-rich description, then imperative steps referencing the workspace paths).
- **Every skill lives in `plugin/skills/`** — never author one outside the workspace or outside that folder.
- **Routing stays lean:** rely on each skill's `description` while the pack is small; add a
  `plugin/skills/RESOLVER.md` only once descriptions overlap or the doctor flags ambiguity.
- Author a skill only for work that repeats or needs upkeep — one-off builds belong in `work/`. For
  skills from completed work, follow the skillify loop (prove provenance, stage in `work/`, verify, ask, publish).

## Phase 5 — Package the plugin

Read `references/packaging.md`.

- Run the doctor (`{OS}-system-check-health` / `scripts/doctor.py`) first — packaging is gated on a
  clean (or explained) report.
- The workspace `plugin/` directory is already the installable plugin — no copying. Validate: every
  `plugin/skills/*/` has a `SKILL.md` named per the convention; all three manifests are valid JSON and
  share the `{OS}-os` name; the Codex manifest points at `./skills/`; the marketplace manifest lists the
  plugin; **no angle brackets in any description**; no stray non-skill folders in `plugin/skills/`;
  `.agents/skills` resolves to `plugin/skills/`. Fix before packaging.
- `zip` the contents of `plugin/` to `/tmp` first, then copy the `.plugin` to the outputs folder and
  record the packaged version in `operations/.packaged-version`.

## Phase 6 — Wire the never-stale schedule

- Try to create a scheduled task that runs `routines/janitor.md` (the janitor routine, default weekly)
  so the workspace self-reconciles even when the user isn't looking.
- **If no scheduling tool is available, or the user declines:** this is not a failure. Record the
  intended cadence + arm status in `routines/README.md`, AND drop a ready-to-use schedule from
  `assets/janitor-schedule.tmpl` (GitHub Actions / cron / launchd / agent-runner task) so enabling it
  later is a single copy. Until the schedule is armed (`armed: yes` in `routines/README.md`), the doctor
  keeps a standing low "schedule armed" finding.
- Don't block or leave the build "unfinished" over scheduling; treat it as the one optional step.

## Phase 7 — Report

Run the doctor and report its score as the build's verification surface — "done" is a clean (or
explained) doctor run, not a feeling. Append a `PROGRESS.md` entry. Summarize: the structure created,
the skills authored (by their `{OS}-{area}-{verb}-{noun}` names), the plugin + marketplace produced, the
schedule set, and the health score. List what was inferred vs. confirmed so the user can correct any assumptions.

## Guardrails

- Don't invent domain facts the user must own — mark inferred items "draft — confirm".
- Leave nothing stale: if you touched the project, update the affected files, the `CLAUDE.md` brain, and
  `PROGRESS.md` in the same turn.
- Don't pre-create empty folders; grow the structure on demand and keep every top-level name one word.
- Author skills only in `plugin/skills/`, named `{OS}-{area}-{verb}-{noun}`. Prefer improving a
  template/skill over a one-off instance.
