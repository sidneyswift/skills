---
name: sid-skills-system
description: Sidney's cross-environment skills system. Use when building, extracting, publishing, or installing skills for Sidney. Triggers on "build a skill", "port this skill", "publish this skill", "clean this up for my portfolio", "install from my skills repo", "make this a general skill", or any skill lifecycle task. Also use when Sidney asks about how his skills system works or wants to set up skills on a new environment.
---

# Sid's Skills System

Sidney builds skills across multiple environments (OpenClaw instances, Claude Code, client workspaces). This skill teaches you how to participate in his skills ecosystem regardless of which environment you're in.

**If `{baseDir}/context.md` exists, read it first.** It tells you which environment you're in and any local configuration.

## Core Concept: context.md

Every skill Sidney builds follows one convention:

1. **SKILL.md** is general — works for anyone, no personal references
2. **context.md** is personal — holds environment-specific config (brand, paths, API keys, audience)
3. **context.example.md** ships with the skill — shows what to configure
4. Published versions never include context.md (gitignored, lint-checked)

When building or modifying a skill, always structure it so the core workflow lives in SKILL.md and anything environment-specific goes in context.md.

## Sidney's Skill Portfolio

- **Repo:** `github.com/sidneyswift/skills` (public)
- **This is the source of truth** for all general-purpose skills Sidney has built
- Any environment can install skills from here

## Environments Sidney Works In

| Environment | Agent | Purpose |
|-------------|-------|---------|
| Cosmo | OpenClaw (Mac) | Sid's personal system — content, research, business |
| Homa | OpenClaw (Mac) | Homeschooling for Sid's son Story — curriculum, lessons, tracking |
| Client workspaces | Varies | Consulting engagements — skills built for clients |
| Recoupable | Product skills | Music industry product (separate monorepo: github.com/recoupable/skills) |

## Workflows

### Building a New Skill

1. Build the skill in the current workspace. Make it work. Iterate.
2. When ready, separate personal from general:
   - Move environment-specific values into context.md
   - SKILL.md should say: "If `{baseDir}/context.md` exists, read it first"
   - Create context.example.md showing what to configure
3. Run the lint check (see below) to verify no personal references remain in publishable files
4. Push to Sidney's portfolio repo
5. Publish to ClawHub

### Extracting a Skill for the Portfolio

When Sidney says "clean this up for my portfolio" or "make this general":

1. Identify all personal/environment-specific references in SKILL.md:
   - Names (Sidney, Sid, Alessa, Story, Cosmo, Homa)
   - Paths (/Users/..., ~/Documents/...)
   - API keys, tokens, channel IDs
   - Brand names, handles, company names
   - Specific URLs, email addresses
2. Move those into context.md
3. Replace them in SKILL.md with "read context.md for [this value]"
4. Run lint (see below)
5. Copy the clean skill to Sidney's local clone of the portfolio repo
6. Commit and push
7. Publish: `clawhub publish <path> --slug <name> --version <version>`

### Installing a Skill from Sidney's Portfolio

```bash
# On any OpenClaw instance
openclaw skills install <skill-slug>

# Or from GitHub directly
clawhub install <skill-slug>
```

After installing, create `context.md` in the skill's directory with environment-specific config.

### Lint Check (Pre-Publish)

Before publishing, scan for personal references. These patterns should NOT appear in publishable files:

```
Sidney, sidney, Sid (as name), Alessa, Story (as name)
/Users/recoupable, /Users/
Recoupable, recoupable (unless the skill IS about Recoupable)
@sidneyswift, cosmo-, Cosmo, Homa, homa
op://, 1Password
~/Documents/projects/
C0B2 (Slack channel IDs)
Specific client company names
```

If you have access to the lint script: `scripts/lint-for-publish.sh <skill-directory>`

If not, manually grep for the patterns above. Fix any findings before publishing.

### Publishing

```bash
# If publish.sh is available (Cosmo's workspace)
./scripts/publish.sh <skill-name> <version>

# If not (other environments), do it manually:
# 1. Copy skill to temp directory
# 2. Remove context.md from the copy
# 3. Verify lint is clean
# 4. clawhub publish <temp-dir/skill-name> --slug <skill-name> --version <version>
```

Also push to GitHub so skills.sh and agentskill.sh auto-index:
```bash
cd <portfolio-repo>
git add <skill-name>
git commit -m "Add/update <skill-name>"
git push origin main
```

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

## What NOT To Do

- Don't hardcode personal values in SKILL.md — use context.md
- Don't publish context.md — it has personal/environment-specific data
- Don't mix Recoupable product skills with personal portfolio skills
- Don't create cross-dependencies between skills (each is self-contained)
- Don't build a skill that only works with context.md — it should have sensible defaults without it

## Revenue Channels for Published Skills

- **ClawHub** — free distribution (audience growth)
- **skills.sh / agentskill.sh** — free, auto-indexed from GitHub
- **BuySkills.ai** — paid sales, 85% revenue share
- **PaperclipSkills** — paid sales, 80% in USDC
- **Consulting** — custom skill building + context.md setup ($500-2000/session)
