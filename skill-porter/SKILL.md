---
name: skill-porter
description: Cross-environment skill management system. Use when building, extracting, publishing, or installing skills across multiple environments. Triggers on "build a skill", "port this skill", "publish this skill", "clean this up for my portfolio", "install from my skills repo", "make this a general skill", or any skill lifecycle task. Also use when setting up the skills system on a new environment or explaining how the skill portfolio works.
---

# Skill Porter

Manage skills across multiple environments — build once, personalize anywhere, publish everywhere.

**If `{baseDir}/context.md` exists, read it first.** It tells you which environment you're in, where the skill portfolio repo lives, what personal patterns to lint for, and what this environment can and can't do (e.g., publish access).

## Core Concept: context.md

Every skill follows one convention:

1. **SKILL.md** is general — works for anyone, no personal references
2. **context.md** is personal — holds environment-specific config (brand, paths, API keys, preferences)
3. **context.example.md** ships with the skill — shows what to configure
4. Published versions never include context.md (gitignored, lint-checked)

When building or modifying a skill, always structure it so the core workflow lives in SKILL.md and anything environment-specific goes in context.md.

## Workflows

### Building a New Skill

1. Build the skill in the current workspace. Make it work. Iterate.
2. When ready, separate personal from general:
   - Move environment-specific values into context.md
   - SKILL.md should say: "If `{baseDir}/context.md` exists, read it first"
   - Create context.example.md showing what to configure
3. Run the lint check (see below) to verify no personal references remain
4. Push to the portfolio repo (see context.md for repo location)
5. Publish to registries (ClawHub, skills.sh, paid marketplaces)

### Extracting a Skill for the Portfolio

When asked to "clean this up for my portfolio" or "make this general":

1. Identify all personal/environment-specific references in SKILL.md:
   - Personal names, handles, brand names
   - Local file paths
   - API keys, tokens, channel IDs
   - Company names, internal URLs
   - Check context.md for the lint patterns specific to this owner
2. Move those into context.md
3. Replace them in SKILL.md with "read context.md for [this value]"
4. Run lint check
5. Copy the clean skill to the portfolio repo
6. Commit and push
7. Publish to registries

### Installing a Skill

```bash
# From ClawHub (OpenClaw)
openclaw skills install <skill-slug>

# From GitHub (any agent)
npx skills add <owner>/<repo>

# Manual
git clone <portfolio-repo> && copy skill folder to workspace
```

After installing, create `context.md` in the skill's directory with your environment-specific config.

### Lint Check (Pre-Publish)

Before publishing, scan for personal references. Check context.md for the `lint_patterns` list — these are the strings that should NOT appear in publishable files.

If a lint script is available (check context.md for path), run it:
```bash
<lint-script-path> <skill-directory>
```

If not, manually grep for each pattern in the lint list. Fix any findings before publishing.

### Publishing

```bash
# ClawHub
clawhub publish <skill-directory> --slug <skill-name> --version <version>

# GitHub (for skills.sh / agentskill.sh auto-indexing)
cd <portfolio-repo> && git add <skill> && git commit && git push
```

For paid marketplaces (BuySkills.ai, PaperclipSkills, skill.broker, etc.), list manually on each platform.

## Skill Structure

```
skill-name/
├── SKILL.md              ← General instructions (required)
├── context.md            ← Environment-specific config (gitignored, never published)
├── context.example.md    ← Shows what to configure (committed, ships with skill)
├── references/           ← Docs loaded on-demand
├── scripts/              ← Executable code
└── assets/               ← Templates, images, fonts
```

## Environment Roles

Environments fall into two roles based on what's configured in context.md:

**Hub** — full publish access. Can build, extract, lint, push to portfolio repo, publish to registries. Usually the primary workspace.

**Spoke** — installs from the portfolio. Can build skills locally. When a skill is ready for the portfolio, it preps the clean version and notifies the hub owner to pull and publish.

## What NOT To Do

- Don't hardcode personal values in SKILL.md — use context.md
- Don't publish context.md — it has personal/environment-specific data
- Don't create cross-dependencies between skills (each is self-contained)
- Don't build a skill that ONLY works with context.md — it should have sensible defaults or clear instructions without it
