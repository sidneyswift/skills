---
name: workspace-os
description: Spin up a complete workspace operating system for any domain that both manages itself and improves itself — from a kickoff input (files, transcripts, or just a prompt). It scaffolds the folders and files, writes a self-managing CLAUDE.md mirrored to AGENTS.md, authors domain skills, packages them into an installable plugin, wires a never-stale janitor (with a read-only doctor) on a schedule, and builds compound-learning and self-improvement loops so the system stays current and gets better at running itself over time. Make sure to use this skill whenever the user wants to set up a workspace, build or scaffold a workspace/operating system, organize a project, turn files or notes into a managed system, or stand up an OS for a new domain — even if they don't say "operating system." Domain-agnostic: consulting, product management, a record label, research, an agency, personal projects, anything.
metadata:
  author: Sidney Swift
  version: "0.10.0"
---

# Workspace OS Builder

**The point is not the folders — it's to scaffold a system that both manages itself and improves
itself.** It keeps its own state current (never-stale) *and* gets better at its own job over time:
compounding knowledge, promoting repeated work into new skills, and improving its own machinery. Hold
that as the goal of every phase below; the structure only exists to serve it.

Concretely, turn a kickoff input into a living operating system: a folder + file structure, a
self-managing `CLAUDE.md` (mirrored to `AGENTS.md`), a `plugin/` directory (an in-place installable
plugin with skills inside), a never-stale janitor backed by a read-only doctor, a compound-learning
loop, and a self-improvement loop. The plugin is named `{DOMAIN_SLUG}-os` by default and includes
manifests/adapters for Claude, Cursor, and Codex.

This builder skill is for the agent running it. Follow the phases in order. Don't stop halfway — drive to a working OS,
then report. Read the references as you reach each phase.

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
   maintained. If yes, promote the proven process into a staged, verified skill before it lands in
   `plugin/skills/`. One-off work stays in `work/` (dated) — it never becomes its own top-level folder.
5. **Self-describing.** Every folder explains its own purpose; `CLAUDE.md` encodes where new things
   go and how to keep the system current.
6. **Evidence over confidence.** "Done", "consistent", and "reachable" are decided by a checkable
   surface — a `{domain}-doctor` run, a skill's verification, a reachable trigger — not the agent's
   feeling. And the OS improves *itself* over time (`{domain}-reflect`), not just its contents.

## Phase 0 — Understand the project deeply (always first)

Read `references/domain-inference.md`.

- Ingest ALL kickoff input (files, transcripts, prompt). If files exist, read them fully.
- Determine the **domain archetype** and the **core unit of work** (e.g. consulting -> deals/clients,
  product -> features/releases, record label -> artists/releases, research -> questions/experiments).
- If input is **rich**, derive structure from the material. If input is **sparse** (just a prompt),
  use best judgment: infer the domain, predict the entities, stages, assets, routines, and metrics
  the project will need, and anticipate them rather than waiting — but express that preparation as
  stubs and subfolders inside a lean root (see Phase 1), not as extra top-level directories.
- Produce a short **Understanding Brief**: domain, core unit, lifecycle stages, key entities,
  compounding assets, recurring tasks (skill candidates), metrics, and likely external tools.
- Confirm the brief with the user only if something material is ambiguous; otherwise proceed.

## Phase 1 — Design the taxonomy

Read `references/blueprint.md`.

- Start from the small **core** the loops maintain: the flowing stores (a staged pipeline folder +
  an entity folder like `clients/` / `artists/` / `features/`), the compounding stores `knowledge/`
  and `library/`, `work/` (non-recurring output, by project), `artifacts/` (finalized recurring
  outputs like the dashboard), `routines/` (runnable prompt instructions for scheduled/remote workflow
  runs), `plugin/` (the in-place plugin), and `operations/` (sync, health, improvements).
- Add an **optional** top-level folder only when the domain has real material for it now —
  `reference/` (canon/source), `proof/` (outcomes), `content/` (a real content motion), `business/`
  (legal/finance/metrics). When unsure, leave it out; adding later is one `mkdir`.
- **Keep every top-level folder name to one lowercase word** (`operations`, not `operating-system`;
  `knowledge`, not `knowledge-base`). Rename to the domain's language but keep it a single word.
  (Skill folders inside `plugin/skills/` stay kebab-case — a different convention.)
- Don't reproduce the whole anatomy by reflex, and **don't promote one-off work to a top-level
  folder** — ad-hoc tasks live in `work/`; only work that repeats or needs upkeep becomes a skill in
  `plugin/`. Push over-preparation into subfolders and stubs, not a row of empty top-level dirs.

## Phase 2 — Scaffold structure + the brain

- Create only the folders the taxonomy calls for (lean root). Give every non-obvious folder a short
  `README.md` stub stating what belongs there.
- Write `artifacts/dashboard.html` from `assets/dashboard.html.tmpl` (HTML, not md). Seed
  `operations/health.md` (empty — the `{domain}-doctor` fills it) and `operations/improvements.md`
  (a header for the `{domain}-reflect` ledger).
- Scaffold `routines/` from `assets/routine.md.tmpl`: seed the maintenance runs `routines/janitor.md`,
  `routines/reflect.md`, and `routines/compound-learn.md`, plus a stub per recurring remote workflow in
  the brief (e.g. `routines/weekly-brief.md`, marked "draft — confirm"). Add a `routines/README.md`
  index listing each routine with its cadence and an `armed: yes|no` marker — the `{domain}-doctor`
  reads this index for its schedule-armed check, so seed it `armed: no` until Phase 6 wires a scheduler.
- Write the self-managing `CLAUDE.md` from `assets/CLAUDE.md.tmpl`, customized to the
  domain (filing decision tree, the auto-manage loop, never-stale contract, repetition-to-skill rule).
  Read `references/self-management.md` for what the contract must contain.
- Create `AGENTS.md` as a symlink to `CLAUDE.md` (`ln -s CLAUDE.md AGENTS.md`) so agent runners that
  look for either file get the same brain. If symlinks aren't supported, write an `AGENTS.md` that
  says "See CLAUDE.md" — but prefer the symlink.

## Phase 3 — Seed compounding assets

- Populate `library/` (blank instruments you reuse — templates, scripts, checklists) and `knowledge/`
  (settled answers you read back — faqs, insights, decisions, sops). Rule of thumb: if you'd *use* it
  to make something it's `library/`; if you'd *consult* it to decide something it's `knowledge/`.
- Extract this material from the input. With sparse input, seed sensible starter templates for the
  domain and mark them "draft — confirm".

## Phase 4 — Author skills (the in-place `plugin/`)

Read `references/skill-authoring.md` and `references/skillifying-work.md` (promotion workflow).

- Derive the plugin name from the domain as `{DOMAIN_SLUG}-os` (kebab-case) unless the user explicitly gave
  a name. Use that same name in every manifest.
- Scaffold `plugin/` as a real plugin in place: `plugin/.claude-plugin/plugin.json` from
  `assets/claude-plugin.json.tmpl`, `plugin/.codex-plugin/plugin.json` from
  `assets/codex-plugin.json.tmpl`, and a `plugin/skills/` directory. The Codex manifest must include
  `"skills": "./skills/"`; see `references/packaging.md`.
- Create `.agents/skills` as a symlink to `../plugin/skills` so Cursor and Codex can discover the same
  project skills. If symlinks aren't supported, copy `plugin/skills/` there and note that it is a
  compatibility mirror.
- For each recurring task in the brief, author `plugin/skills/{name}/SKILL.md` (frontmatter `name` +
  description with real trigger phrases, then imperative steps referencing the workspace paths).
- Always include the maintenance skills (the OS's feedback organs), generated from the templates:
  - a **doctor** (`assets/doctor-SKILL.md.tmpl`) — the read-only verification surface (health score +
    punch list to `operations/health.md`); the janitor and the build report are gated on it. Also
    generate `operations/doctor.py` from `assets/doctor.py.tmpl` (fill the `PIPELINE`/`ENTITY`/slug) as
    its deterministic fast path — so the mechanical checks ship with the build instead of being
    reinvented later.
  - a **janitor** (`assets/janitor-SKILL.md.tmpl`) — run the doctor, then reconcile and fix what's safe.
  - a **compound-learn** skill (`assets/compound-learn-SKILL.md.tmpl`) — capture
    decisions/answers/patterns into `knowledge/` after each work session.
  - a **reflect** skill (`assets/reflect-SKILL.md.tmpl`) — improve the OS itself (skills, routing,
    checks, templates) into `operations/improvements.md`; the 50/50 budget.
  - a **skillify** skill (`assets/skillify-SKILL.md.tmpl`) — promote proven repeatable work into
    staged, verified skills.
- Pair the unattended loops with runnable routines: confirm the `routines/` prompts seeded in Phase 2
  (`janitor.md`, `reflect.md`, `compound-learn.md`) each drive the matching skill, and give any domain
  workflow meant to run remotely its own `routines/{workflow}.md`.
- Also include an orchestrator skill (the auto-manage loop as one trigger) named `{domain}-intake`.
- **Routing stays lean:** rely on each skill's `description` for routing while the pack is small; add
  a `plugin/skills/RESOLVER.md` (trigger -> skill table) only once skills grow enough that
  descriptions overlap or the doctor's reachability check flags ambiguity.
- Author a skill only for work that repeats or needs upkeep — one-off builds belong in `work/`, not a
  throwaway skill. For skills created from completed work, follow the skillify loop: prove provenance,
  extract the repeatable process, stage in `work/`, verify with the strongest domain-appropriate check,
  ask before moving into `plugin/skills/`, then repackage.

## Phase 5 — Package the plugin

Read `references/packaging.md`.

- Run `{domain}-doctor` first — packaging is gated on a clean (or explained) report.
- The workspace `plugin/` directory is already the installable plugin — no copying. Validate it: every
  `plugin/skills/*/` has a `SKILL.md`; both plugin manifests are valid JSON and share the `{DOMAIN_SLUG}-os`
  name; the Codex manifest points at `./skills/`; **no angle brackets in any description**; no stray
  non-skill folders in `plugin/skills/`; `.agents/skills` points to or mirrors `plugin/skills/`. Fix
  before packaging.
- `zip` the contents of `plugin/` to `/tmp` first, then copy the `.plugin` to the outputs folder and
  present it for install.

## Phase 6 — Wire the never-stale schedule

- Try to create a scheduled task that runs `routines/janitor.md` (the janitor routine, default weekly)
  so the workspace self-reconciles even when the user isn't looking.
- **If no scheduling tool is available, or the user declines:** this is not a failure. Record the
  intended cadence + arm status in `routines/README.md`, AND drop a ready-to-use schedule from
  `assets/janitor-schedule.tmpl` (GitHub Actions / cron / launchd / agent-runner task) — each snippet
  runs the routine prompt — so enabling it later is a single copy, not a research project. The OS is
  still complete — the routines also run on demand — but until the schedule is armed, the doctor keeps
  a standing low "schedule armed" finding, because "self-reconciles when no one is looking" is only
  true once it actually runs unattended.
- Don't block or leave the build "unfinished" over scheduling; treat it as the one optional step.

## Phase 7 — Report

Run `{domain}-doctor` and report its score as the build's verification surface — "done" is a clean
(or explained) doctor run, not a feeling. Summarize: the structure created, the skills authored, the
plugin produced, the schedule set, and the health score. List what was inferred vs. confirmed so the
user can correct any assumptions.

## Guardrails

- Don't invent domain facts the user must own — mark inferred items "draft — confirm".
- Leave nothing stale: if you touched the project, update the dashboard, boards, and any affected
  README in the same turn.
- Prefer improving a template/skill over a one-off instance.
