# Understanding the Project (rich or sparse input)

The quality of the OS depends on how well you understand the project before scaffolding. Always
produce an **Understanding Brief** first.

## Step 1 — Ingest everything
- Read every supplied file/transcript fully (don't skim). Note entities, processes, vocabulary,
  stages, recurring questions, and what the user clearly cares about.
- If the input is a single prompt, treat the prompt as the seed and move to inference.

## Step 2 — Identify the spine
Answer these explicitly:
- **Domain archetype** (consulting, product, label, research, agency, personal, other).
- **Core unit of work** — the thing that recurs and moves through stages (a deal, a feature, a
  release, a study, an account).
- **Lifecycle stages** of that unit, start to finish.
- **Key entities** that own records (clients, artists, teams, products).
- **Compounding assets** the domain reuses (templates, checklists, brand kits, datasets, scripts).
- **Recurring tasks** → these become skills.
- **Metrics** that should be tracked over time.
- **External tools / systems of record** likely in play (CRM, tracker, DAW, repo, drive).

## Step 3 — Handle sparse input with best-judgment prediction
When you only have a thin prompt, do NOT build a minimal stub and wait. Predict the full system:
- Pick the closest archetype from `blueprint.md` and adopt its mappings as a starting point.
- Enumerate the entities/stages/assets/rituals/metrics a competent operator in that domain would
  need within 90 days, and scaffold for all of them.
- Seed starter templates and a `reference/principles.md` with domain best practices, each marked
  **"draft — confirm"** so the user can correct.
- Prefer over-preparing (extra empty, well-labeled folders + stubs) to under-preparing. Empty
  folders with a one-line README cost nothing and teach the user where things go.

## Step 4 — Write the brief
A compact brief, e.g.:
```
Domain: record label (independent)
Core unit: release (single/EP/album)
Stages: demo -> A&R -> signed -> production -> release -> promo -> catalog
Entities: artists/, releases/
Compounding: split sheets, release checklist, promo templates, press kit, contract clauses
Recurring tasks (skills): ingest-demo, build-release-plan, splits-tracker, promo-rollout, royalty-check, janitor, learn
Metrics: releases/quarter, streams, save rate, revenue/release, roster size
External SoR: distributor dashboard, DAW project store, accounting
Confidence: medium (from 1 transcript + roster list)
```
Confirm only material ambiguities; otherwise proceed to scaffold.
