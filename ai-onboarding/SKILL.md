---
name: ai-onboarding
description: Progressive AI onboarding system that meets users where they are and grows with them. Use when onboarding someone to AI tools (Claude, ChatGPT, Cursor, Codex, etc.), assessing their AI maturity, setting up their personal AI workspace, or teaching them to get real value from AI. Triggers on "onboard me", "I'm new to AI", "help me get started with AI", "set up my AI workspace", "what should I learn next", "AI training", or when someone clearly doesn't know how to use AI effectively. Also triggers on "check my progress", "what's my next step", or "AI learning path".
---

# AI Onboarding

A single skill that progressively teaches people to use AI — from first-timer to skill-builder. One entry point, smart internal routing, no dead ends.

## Core Principles

1. **Assess through doing, not asking.** Don't quiz people. Ask one question: "What's a piece of work you'd want AI help with this week?" Their answer reveals everything — vocabulary, specificity, awareness of tools. Branch from there.
2. **Every module ends with real shipped work.** Not toy examples. The user's actual task, completed with AI, using what they just learned.
3. **No walls.** Before suggesting any tool, connector, or workflow — check if they can actually do it. Easy wins first. Blocked paths noted for later. Never let someone hit a permissions wall and blame AI.
4. **The workspace IS the product.** Onboarding provisions a personal project folder that starts as a tutor and becomes their permanent AI operating system. The onboarding is the seed of the lifelong system.
5. **Pick up where they left off.** Read PROGRESS.md before every session. Never re-explain what they've demonstrated they know.

## Setup

**Step 0: Check configuration**

1. Read `~/.config/ai-onboarding/.env`. If it doesn't exist or `SETUP_COMPLETE` is not `true`, this is a first run — proceed to Discovery (below).
2. If setup is complete, read the user's `PROGRESS.md` from their workspace path (stored in `.env` as `WORKSPACE_PATH`). Route to whatever module is next.

## Discovery — First Session

The first session builds context without an interrogation. Do these in order:

### 1. The Opening Question

Ask exactly one question:

> "What's a piece of work you'd want AI help with this week?"

Their answer classifies them. Read `references/discovery/stage-assessment.md` for the classification logic.

### 2. Light Context Gathering

Based on their answer, gather what you need conversationally — not as a form:

- **What they do** — role, domain, daily work. Infer from their answer when possible. Ask only what you can't infer.
- **What tools they use** — not "what AI tools" but "what tools, period." Spreadsheets, email, Slack, specific software. This tells you where connectors matter.
- **What they've tried** — have they used ChatGPT? Claude? Cursor? Nothing? Don't ask "rate your AI experience 1-10." Ask "what have you tried so far?" or infer from vocabulary.

If they share a name, company, or LinkedIn — do a quick web search. Public context (role, industry, company size) saves them from answering obvious questions.

### 3. Connector Feasibility Check

Read `references/discovery/connector-check.md` for the full logic. The short version:

- Based on their role and tools, identify which connectors would be useful.
- For each one, check: can they set it up themselves, or does it need admin/IT?
- Classify as: **ready** (can do now), **available** (exists but needs a step), **blocked** (needs someone else's approval).
- Start with ready. Note available. Park blocked — come back to them later.
- NEVER suggest a connector and let them hit a wall.

### 4. Provision the Workspace

Read `references/templates/workspace-setup.md` for the full folder structure and file templates.

Create their personal AI workspace:

```
~/<username>-ai/
├── CLAUDE.md           # Role context, standing instructions, tools
├── PROGRESS.md         # Journey tracker — stage, completed modules, next steps
├── README.md           # What this folder is, how to use it
├── inbox/              # Dump zone — pastes, screenshots, meeting notes
├── workflows/          # Saved prompts and recipes for recurring work
├── current/            # Active projects (one folder each)
├── references/         # Pointers to tools, dashboards, key resources
└── knowledge/          # Things the AI learns about how they work
    ├── raw/            # Captured observations
    └── synthesized/    # Patterns the AI notices over time
```

Customize `CLAUDE.md` with their role, tools, and preferences from discovery. Write the initial `PROGRESS.md` with their assessed stage and recommended path.

### 5. Save Config

Write `~/.config/ai-onboarding/.env`:

```
SETUP_COMPLETE=true
WORKSPACE_PATH=~/<username>-ai
USER_STAGE=<assessed-stage>
LAST_MODULE=discovery
LAST_SESSION=<ISO-date>
```

### 6. First Win

Don't end the first session with "OK, you're set up!" End it by doing the thing they asked for. Take their opening answer and do it with them. This IS Module 01.

## Modules

Modules are not a linear sequence. The system reads PROGRESS.md and picks the right next module based on what the user has demonstrated, what they're asking for, and what connectors are available.

Load the relevant module from `references/modules/` when needed.

### Module Map

| Module | File | Triggers When |
|--------|------|---------------|
| 01-first-workflow | `references/modules/01-first-workflow.md` | Always first. Uses their opening question as the task. |
| 02-iteration | `references/modules/02-iteration.md` | User treats a bad first output as final, or asks "why isn't this better?" |
| 03-context-and-prompting | `references/modules/03-context-and-prompting.md` | User gives vague prompts, doesn't provide context, or asks how to "talk to AI better." |
| 04-connectors | `references/modules/04-connectors.md` | User's work involves data/tools that need connecting, and they have "ready" connectors. |
| 05-projects-and-memory | `references/modules/05-projects-and-memory.md` | User starts multiple tasks without persistent context, or asks "why doesn't it remember?" |
| 06-building-skills | `references/modules/06-building-skills.md` | User has a repeatable workflow they do manually, or asks "can I automate this?" |
| 07-team | `references/modules/07-team.md` | User manages others and asks about rolling AI out, or demonstrates personal competence. |

### Module Completion

A module is complete when the user has *done the thing*, not just heard about it. Each module's reference file defines what "done" looks like. Update PROGRESS.md when a module completes.

## Stage Ladder

Users sit on a rough maturity curve. The stage informs which modules are relevant:

1. **Never used** — No AI experience. Start with orientation + first workflow.
2. **Chat-only** — Uses ChatGPT/Claude for Q&A but no tools, no context, no memory. Teach iteration, prompting, connectors.
3. **Tool-connected** — Has some integrations working. Teach projects, memory, advanced prompting.
4. **Workflow builder** — Builds repeatable processes. Teach skill-building, scheduling.
5. **Skill builder** — Creates and shares skills/agents. Teach team rollout.
6. **Fleet manager** — Manages AI across a team or org. Consulting-level, not teaching.

The stage assessment happens organically from the opening question + conversation. See `references/discovery/stage-assessment.md`.

## Wall Avoidance

This is critical. Read `references/discovery/connector-check.md` for the full protocol, but the rules are:

1. Before suggesting ANY connector, tool, or integration: verify the user can actually set it up.
2. If it needs admin access they don't have: don't suggest it. Note it in PROGRESS.md under "parked."
3. If it needs a paid plan they might not have: ask before suggesting.
4. If it's technically possible but complex: offer it as an option, don't present it as the path.
5. Always have a fallback. "We can't connect to Salesforce, but you CAN export a CSV and we'll work with that."
6. The user should never feel like AI failed them. If something doesn't work, it's a routing problem, not a capability problem.

## Updating Progress

After every session, update `PROGRESS.md` in the user's workspace:

```markdown
## Current Stage
[stage from ladder]

## Completed
- [x] Module 01: First Workflow — [what they built] — [date]
- [x] Module 03: Context & Prompting — [date]

## In Progress
- [ ] Module 04: Connectors — started [date], blocked on [what]

## Parked
- Salesforce connector — needs admin API key, user doesn't have access
- Power BI — company uses Tableau instead, skip

## Next Recommended
Module 02: Iteration — user accepted a rough first draft last session without pushing back

## Notes
- User is a marketing manager at a 50-person SaaS company
- Primary tools: Google Sheets, Slack, HubSpot, Figma
- Learns best with concrete examples, not theory
- Prefers short sessions over long deep-dives
```

## The Evolution

The workspace starts as an onboarding environment. Over time:

- `workflows/` fills with their recurring AI-assisted processes
- `knowledge/` accumulates how they work, what they've tried, what works
- `current/` becomes where they start new projects
- `CLAUDE.md` becomes richly personalized standing instructions
- `PROGRESS.md` shifts from learning tracker to capability inventory

At some point, they stop "onboarding" and they're just... using their AI workspace. That's the goal. The onboarding dissolves into the operating system.

## Context Personalization

This skill follows the `context.md` convention:

- `SKILL.md` — general instructions (you're reading it)
- `context.md` — deployer's config (org name, available connectors, approved tools, custom modules). Optional. Create it for org-specific deployments.
- `context.example.md` — shows what to configure

For general/personal use, `~/.config/ai-onboarding/.env` is sufficient. `context.md` is for deployers customizing this for a team or organization.
