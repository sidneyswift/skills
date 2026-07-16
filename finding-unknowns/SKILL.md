---
name: finding-unknowns
description: >-
  Surface the gaps between what a task description says and what the work
  actually requires, before writing code. Use before implementing anything
  ambiguous, large, or unfamiliar; when the user asks "what am I missing",
  wants options or design directions, needs a mock or plan to react to, wants
  to be interviewed about a spec, is porting from a reference implementation,
  or gives a vague creative request they lack vocabulary for. Make sure to use
  this skill whenever the map (prompt/spec) might not match the territory
  (codebase/real requirements) — even if the user does not say "unknowns."
metadata:
  author: Sidney Swift
  version: "0.1.0"
---

# Finding Unknowns

## Overview

The map is not the territory. The prompt, spec, and context are a map of the work; the codebase and the real requirements are the territory. Output quality is capped by how well the unknowns, the gaps between map and territory, get surfaced before implementation. Unaccounted unknowns fail both ways: the work quietly does the wrong thing, or it stalls on a question nobody asked. The cheapest place to find an unknown is before any code is written.

## The four quadrants

Classify what is known about the task, then pick the discovery move for the weak quadrant:

| Quadrant | What it is | Discovery move |
|---|---|---|
| Known knowns | Already in the prompt or spec | Nothing to do |
| Known unknowns | Open questions everyone is aware of | Ask directly: spec interview, options brainstorm |
| Unknown knowns | Context so obvious to the user they never wrote it down; they recognize it on sight | Give them something to react to: design directions, mocks, tweakable plans |
| Unknown unknowns | Traps nobody has considered | Go find them: blindspot pass, teach-me explainer, reference semantics map |

## Technique selection

| Situation | Technique | Reference |
|---|---|---|
| Implementing in an unfamiliar part of the codebase | Blindspot pass | references/blindspot-pass.md |
| The user lacks vocabulary for the domain ("make it nicer") | Teach-me explainer | references/teach-me-explainer.md |
| The user does not know what they want visually | Design directions | references/design-directions.md |
| UI layout or placement calls are unresolved | Mock before wiring | references/mock-before-wire.md |
| Rough problem, no chosen solution yet | Options brainstorm | references/options-brainstorm.md |
| Spec is ambiguous and answers would change the architecture | Spec interview | references/spec-interview.md |
| A reference implementation exists to port or imitate | Reference semantics map | references/reference-semantics-map.md |
| Writing an implementation plan for review | Tweakable plan | references/tweakable-plan.md |

Read the matching reference before executing the technique. Combine techniques when it helps: an interview after a blindspot pass, a mock after design directions.

## Artifact conventions

Most techniques produce a single self-contained HTML file the user opens and reacts to. Rules that apply to all of them:

- One file, no build step, no dependencies beyond a CDN font or icon set.
- Fake data must look plausible and be labeled as fake. Never touch the real app for a throwaway artifact.
- Every artifact ends with a reply assembler: chips, checkboxes, or copy buttons that compose the user's response for them. The user should never have to write a design brief; their taps write it.
- Sort content by how much it deserves the user's attention, not by build order or category.
- The artifact is disposable. Optimize for the reaction it collects, not for reuse.

## Workflow

1. Decide which quadrant is weakest for this task, then pick techniques from the table.
2. Execute the technique per its reference. Ground everything in the actual codebase: real file paths, real git history, real flags, real data shapes.
3. Collect the user's reactions or answers.
4. Fold everything into a revised implementation prompt or spec: constraints learned, decisions made, work order, stop points.
5. Confirm the revised prompt with the user before implementing.

Source: Thariq Shihipar, "A Field Guide to Fable: Finding Your Unknowns", and the companion examples at thariqs.github.io/html-effectiveness/unknowns/.
