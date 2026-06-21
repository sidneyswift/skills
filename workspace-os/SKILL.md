---
name: workspace-os
description: Spin up a complete, self-managing workspace operating system for any domain from a kickoff input (files, transcripts, or just a prompt). It scaffolds the folders and files, writes a self-managing CLAUDE.md mirrored to AGENTS.md, authors domain skills, packages them into an installable plugin, wires a never-stale janitor on a schedule, and builds a compound-learning loop. Make sure to use this skill whenever the user wants to set up a workspace, build or scaffold a workspace/operating system, organize a project, turn files or notes into a managed system, or stand up an OS for a new domain — even if they don't say "operating system." Domain-agnostic: consulting, product management, a record label, research, an agency, personal projects, anything.
metadata:
  author: Sidney Swift
  version: "0.2.1"
---

# Workspace OS Builder

Turn a kickoff input into a living operating system: a folder + file structure, a self-managing
`CLAUDE.md` (mirrored to `AGENTS.md`), a `skills/` directory packaged as an installable plugin,
a never-stale janitor on a schedule, and a compound-learning loop so the workspace gets smarter
every time it's used.

This skill is for Claude. Follow the phases in order. Don't stop halfway — drive to a working OS,
then report. Read the references as you reach each phase.

## Operating beliefs (apply to every OS you build)
1. **Separate what compounds from what flows.** Compounding = reusable assets that improve every
   time (templates, knowledge base, skills, proof). Flowing = instances moving through stages
   (deals, tickets, releases, experiments). Wire feedback so every flowing instance deposits back
   into a compounding asset.
2. **Never stale.** It is the agent's job to manage state. Any time new input arrives OR the user
   works in the OS, every file/folder that should change gets touched in the same turn. A janitor
   skill + scheduled task is the safety net.
3. **Compound learning.** Every session makes the system smarter — capture decisions, recurring
   answers, and patterns into the knowledge base. Never solve the same thing twice.
4. **Anything done more than once becomes a skill.** Notice repetition, author a skill, repackage.
5. **Self-describing.** Every folder explains its own purpose; `CLAUDE.md` encodes where new things
   go and how to keep the system current.

## Phase 0 — Understand the project deeply (always first)
Read `references/domain-inference.md`.
- Ingest ALL kickoff input (files, transcripts, prompt). If files exist, read them fully.
- Determine the **domain archetype** and the **core unit of work** (e.g. consulting -> deals/clients,
  product -> features/releases, record label -> artists/releases, research -> questions/experiments).
- If input is **rich**, derive structure from the material. If input is **sparse** (just a prompt),
  use best judgment: infer the domain, predict the entities, stages, assets, rituals, and metrics
  the project will need, and prepare the OS for all of them rather than waiting.
- Produce a short **Understanding Brief**: domain, core unit, lifecycle stages, key entities,
  compounding assets, recurring tasks (skill candidates), metrics, and likely external tools.
- Confirm the brief with the user only if something material is ambiguous; otherwise proceed.

## Phase 1 — Design the taxonomy
Read `references/blueprint.md`.
- Map the brief onto the universal anatomy: `reference/` (canon, read-mostly), compounding stores
  (`library/`, `knowledge-base/`, `proof/` or domain equivalents), flowing stores (a staged
  pipeline-style folder + an entity folder like `clients/` / `artists/` / `features/`), plus
  `content/` if relevant, `business-ops/`, and `operating-system/` (dashboard, rituals, sync).
- Rename folders to the domain's language. Drop sections that don't apply. Add domain-specific ones.

## Phase 2 — Scaffold structure + the brain
- Create the folders. Give every non-obvious folder a short `README.md` stub stating what belongs there.
- Write `operating-system/dashboard.html` from `assets/dashboard.html.tmpl` (HTML, not md).
- Write the self-managing `CLAUDE.md` from `assets/CLAUDE.md.tmpl`, customized to the
  domain (filing decision tree, the auto-manage loop, never-stale contract, repetition-to-skill rule).
  Read `references/self-management.md` for what the contract must contain.
- Create `AGENTS.md` as a symlink to `CLAUDE.md` (`ln -s CLAUDE.md AGENTS.md`) so agent runners that
  look for either file get the same brain. If symlinks aren't supported, write an `AGENTS.md` that
  says "See CLAUDE.md" — but prefer the symlink.

## Phase 3 — Seed compounding assets
- Populate `library/` and `knowledge-base/` with reusable material extracted from the input
  (templates, scripts, SOPs, canonical answers). With sparse input, seed sensible starter templates
  for the domain and mark them "draft — confirm".

## Phase 4 — Author skills
Read `references/skill-authoring.md` (includes the validation rules — most importantly: **no angle
brackets in a skill description**; use `{placeholder}` instead).
- Create a root `skills/` directory in the new workspace.
- For each recurring task in the brief, author `skills/{name}/SKILL.md` (frontmatter `name` +
  description with real trigger phrases, then imperative steps referencing the workspace paths).
- Always include two maintenance skills, generated from the templates:
  - a **janitor** (`assets/janitor-SKILL.md.tmpl`) — reconcile and de-stale the whole OS.
  - a **compound-learn** skill (`assets/compound-learn-SKILL.md.tmpl`) — capture
    decisions/answers/patterns after each work session.
- Also include an orchestrator skill (the auto-manage loop as one trigger) named `{domain}-intake`.

## Phase 5 — Package the skills as a plugin
Read `references/packaging.md`.
- Build `{name}-os/.claude-plugin/plugin.json`, copy the skill folders, add a README.
- Validate (every skill dir has `SKILL.md`; manifest `name` is kebab-case; **no angle brackets in any
  description**). Fix before packaging.
- `zip` to `/tmp` first, then copy the `.plugin` to the outputs folder and present it for install.

## Phase 6 — Wire the never-stale schedule
- Try to create a scheduled task that runs the janitor skill (default weekly) so the workspace
  self-reconciles even when the user isn't looking.
- **If no scheduling tool is available, or the user declines:** this is not a failure. Record the
  intended cadence in `operating-system/rituals.md`, and tell the user the one step to enable it
  later (run the janitor on a schedule). The OS is still complete — the janitor also runs on demand.
- Don't block or leave the build "unfinished" over scheduling; treat it as the one optional step.

## Phase 7 — Report
Summarize: the structure created, the skills authored, the plugin produced, and the schedule set.
List what was inferred vs. confirmed so the user can correct any assumptions.

## Guardrails
- Don't invent domain facts the user must own — mark inferred items "draft — confirm".
- Leave nothing stale: if you touched the project, update the dashboard, boards, and any affected
  README in the same turn.
- Prefer improving a template/skill over a one-off instance.
