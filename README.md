# Skills

AI agent skills — build once, personalize anywhere.

Built by [@sidneyswift](https://x.com/sidneyswift).

## Install

```bash
# OpenClaw
openclaw skills install <skill-name>

# Claude Code / Codex / any agent
npx skills add sidneyswift/skills
```

## Skills

| Skill | Description |
| --- | --- |
| [social-graphics](./social-graphics/) | Generate on-brand social graphics for any platform & format — feed posts, carousels, stories, banners, profile pics, thumbnails, pins, OG cards. Full dimensions/safe-zone reference included. HTML → Playwright → PNG. |
| [workspace-os](./workspace-os/) | Spin up a complete, self-managing workspace operating system for any domain — scaffolds folders, a self-managing CLAUDE.md, domain skills, an installable plugin, a janitor, and a compound-learning loop. |

## How Personalization Works

Every skill follows the `context.md` convention:

- **SKILL.md** — general instructions that work for anyone
- **context.md** — your personal config (brand, paths, preferences). Create this locally after installing.
- **context.example.md** — shows what to configure

Install a skill, create your own `context.md`, and it's personalized to your setup. No forking required.

## License

MIT
