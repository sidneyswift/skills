---
name: skill-system
description: Cross-environment skill management system. Use when building, extracting, publishing, or installing skills across multiple environments. Triggers on "build a skill", "port this skill", "publish this skill", "clean this up for my portfolio", "install from my skills repo", "make this a general skill", or any skill lifecycle task. Also use when setting up the skills system on a new environment or explaining how the skill portfolio works.
---

# Skill System

Build skills once, personalize anywhere, publish everywhere.

## Setup

Read `~/.config/skill-system/.env`. If it doesn't exist, ask the user for:
- Portfolio repo URL (their public GitHub skills repo)
- Local clone path
- Whether this environment can publish (hub) or only install (spoke)

Write answers to `~/.config/skill-system/.env`.

## Two Config Layers

Skills keep NO personal data in their directory. Config lives in `~/.config/`:

1. **Identity** — `~/.config/<owner>/identity.md` — who the human/brand is. Name, handle, logo, voice, audience. Shared across all skills. Set up once per machine.
2. **Skill config** — `~/.config/<skill-name>/.env` — per-skill settings. Key=value pairs. `SETUP_COMPLETE=true` gate. First run creates it via wizard.

## Building a Skill

1. Build it in your workspace. Make it work. Iterate.
2. When ready, make sure SKILL.md has no personal references. Personal config should come from the two layers above.
3. SKILL.md should instruct the agent to read identity + skill .env on setup.
4. Run lint check to verify no personal references remain.
5. Push to portfolio repo + publish to ClawHub.

## Extracting a Personal Skill

When asked to "clean this up" or "make this general":

1. Find all personal references in SKILL.md (names, paths, keys, brand names, handles)
2. Move structured config to `~/.config/<skill>/.env`
3. Ensure SKILL.md reads identity file for brand/voice context
4. Lint check — run the lint script or grep for personal patterns
5. Push clean version to portfolio repo

## Lint Patterns

Check `~/.config/skill-system/.env` for the `LINT_PATTERNS` value — a comma-separated list of strings that should NOT appear in publishable files.

## Publishing

```bash
# From hub environment
scripts/publish.sh <skill-name> <version>
# Also push to GitHub for skills.sh/agentskill.sh auto-indexing
```

Spokes cannot publish directly. Stage the clean skill and notify the hub owner.

## Skill Structure

```
skill-name/
├── SKILL.md              ← General (no personal data)
├── references/           ← Docs loaded on-demand
├── scripts/              ← Executable code
└── assets/               ← Templates, images, fonts
```

Config lives OUTSIDE the skill:
```
~/.config/<owner>/identity.md    ← Human/brand context (shared)
~/.config/<skill-name>/.env      ← Skill settings (per-skill)
```
