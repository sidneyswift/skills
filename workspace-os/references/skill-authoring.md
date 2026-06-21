# Authoring Skills (aligned to the Agent Skills spec)

Follows the official spec (agentskills.io/specification) and Anthropic's `skill-creator` guidance.

## Anatomy
```
skill-name/
├── SKILL.md          # required: YAML frontmatter + Markdown instructions
├── scripts/          # optional: executable code (deterministic/repetitive work)
├── references/       # optional: docs loaded into context on demand
└── assets/           # optional: TEMPLATES + resources used in output
```
Put document/config **templates in `assets/`** (not `references/`). Put guides/docs the agent reads
in `references/`. Keep file references **one level deep** from SKILL.md — avoid deep chains.

## Frontmatter (spec limits)
```
---
name: kebab-name            # <=64 chars; a-z 0-9 and hyphens; no leading/trailing/double hyphen; matches folder
description: what + when     # <=1024 chars; non-empty; what it does AND when to use it
metadata:                    # optional
  author: name
  version: "0.1.0"
# license, compatibility, allowed-tools are also optional
---
```

## Description = the trigger (make it a little "pushy")
The description is the primary triggering mechanism, and Claude tends to UNDER-trigger skills. Combat
that: state what it does AND explicit contexts, e.g. "...Make sure to use this skill whenever the user
mentions X, Y, or wants Z — even if they don't explicitly say 'X'." Third person, concrete keywords.
- Good: "Draft a release rollout plan for an upcoming single. Use whenever the user says 'plan the
  release', 'build a rollout', mentions a launch timeline, or a release moves to production."
- Weak: "Helps with releases."

## Body
- Imperative, verb-first ("Create the folder", not "You should create").
- **Explain the why** instead of heavy ALL-CAPS MUSTs — modern models follow reasoning better than rules.
- Keep SKILL.md under ~500 lines / <5000 tokens; move depth into `references/` with clear pointers.
- For a reference file over ~300 lines, add a table of contents.
- Include 1-2 input/output examples where useful.

## Validation gotchas (these actually break installs)
- **No angle brackets in `description`** — the loader reads `<...>` as XML tags and rejects it. Use
  `{placeholder}`.
- `name` matches the folder name and obeys the kebab rules above.
- Every skill folder has a `SKILL.md`; don't put loose non-skill folders inside a plugin's `skills/`.
- Validate structure with `skills-ref validate ./my-skill` if available.

## What to author for a new OS
1. An **orchestrator**: `{domain}-intake` — the auto-manage loop as one trigger.
2. One skill per **recurring task** from the brief.
3. A **janitor** (from `assets/janitor-SKILL.md.tmpl`) — never-stale reconcile.
4. A **compound-learn** skill (from `assets/compound-learn-SKILL.md.tmpl`).
5. A **packager** if the user will keep adding skills.
Prefix skills with the domain (e.g. `label-`, `pm-`) so they group together.

## Optional: rigor via the official skill-creator
Anthropic's `skill-creator` skill adds an eval/iterate loop: write 2-3 realistic test prompts, run
with-skill vs. baseline, review outputs, and optimize the description for triggering accuracy. Use it
when a skill is high-value and you want measured quality, not just vibes. It also ships
`scripts/package_skill.py` to produce the `.skill` file.
