# Workspace Setup — Personal AI Folder

This template defines the user's personal AI workspace. It starts as an onboarding environment and evolves into their permanent AI operating system.

## Folder Structure

Create at `~/<username>-ai/` (or wherever they prefer — ask if they have a preference for where projects live).

```
<username>-ai/
├── CLAUDE.md
├── PROGRESS.md
├── README.md
├── inbox/
├── workflows/
├── current/
├── references/
└── knowledge/
    ├── raw/
    └── synthesized/
```

## CLAUDE.md Template

This is the file agents read on every session. Customize from discovery.

```markdown
# [Name]'s AI Workspace

## About Me
- **Role:** [role from discovery]
- **Domain:** [industry/department]
- **Tools I use daily:** [list from discovery]
- **How I work:** [any preferences observed — short sessions vs deep dives, examples vs theory, etc.]

## Standing Instructions
- Read PROGRESS.md before starting any session — know where I left off.
- Don't re-explain concepts I've already demonstrated understanding of.
- When suggesting tools or integrations, check PROGRESS.md "Connectors" section first — don't suggest blocked ones.
- Prefer concrete examples from my actual work over generic demonstrations.
- If I give a vague prompt, help me make it specific instead of guessing.

## My Connectors
[Populated from connector check]
- Google Sheets: ready
- Slack: available, not yet set up
- HubSpot: parked — need API key from IT

## What I'm Learning
See PROGRESS.md for current stage and module history.
```

## PROGRESS.md Template

```markdown
# AI Learning Progress

## Current Stage
[Stage from assessment — e.g., "Stage 2: Chat-only"]

## Assessment Notes
[From discovery — opening answer, signals observed, key context]

## Completed Modules
[Empty at start. Updated as modules complete.]

## In Progress
[Current module, if any]

## Parked
[Things we've identified but can't do yet — blocked connectors, advanced topics for later]

## Connectors
### Ready
[What they can use now]

### Available
[What exists but needs a setup step]

### Parked
[What's blocked and why]

## Next Recommended
[What the system thinks they should do next, and why]

## Session Log
### [Date] — Discovery + First Workflow
- Assessed as Stage [X]
- Opening task: [what they asked for]
- Completed: [what we actually did]
- Observed: [learning style, preferences, struggles]
- Next: [what to do next session]
```

## README.md Template

```markdown
# My AI Workspace

This is your personal AI workspace — a folder where you and your AI assistant work together.

## What's here

- **CLAUDE.md** — Context about you that AI reads at the start of every session. Edit it anytime.
- **PROGRESS.md** — Tracks your learning journey and what tools are available to you.
- **inbox/** — Drop anything here. Screenshots, meeting notes, files you want AI help with.
- **workflows/** — Saved prompts and recipes you use regularly. These grow over time.
- **current/** — Active projects. One folder per project.
- **references/** — Links and notes about tools, dashboards, resources you use.
- **knowledge/** — Things the AI has learned about how you work. It updates this over time.

## How to use it

Open this folder as a project in Claude, Cursor, or any AI tool that supports project context. The AI will read CLAUDE.md and know who you are, where you left off, and what to work on next.

When you want to work on something, put the source material in inbox/ and start a conversation. When you build a repeatable process, save it to workflows/.
```

## Customization Notes

- The CLAUDE.md should feel personal, not templated. Use the user's actual words from discovery where possible.
- Don't fill in sections you don't have data for. Empty sections with placeholders are worse than missing sections.
- The folder names are suggestions. If the user says "I'd call that 'projects' not 'current'" — rename it. It's their workspace.
- If they already have a project folder structure they like, adapt to it rather than imposing this one.

## Evolution Markers

Over time, watch for these signals that the workspace is evolving past onboarding:

- `workflows/` has 3+ saved workflows → they're building process, not just learning
- `current/` has active projects → they're using this as a real workspace
- `knowledge/synthesized/` has entries → the AI is compounding knowledge about them
- They edit `CLAUDE.md` themselves → they understand how context works
- They stop asking "how do I..." and start asking "can you..." → agency shift

When you see these, note it in PROGRESS.md. The system doesn't need to formally "graduate" them — the shift happens naturally.
