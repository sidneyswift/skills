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
|-------|-------------|
| [social-slides](./social-slides/) | Generate carousel/slide images for LinkedIn, X, Instagram. HTML → Playwright → PNG. |
| [skill-system](./skill-system/) | Cross-environment skill management. Build skills once, personalize with context.md, publish everywhere. |

## How Personalization Works

Every skill follows the `context.md` convention:

- **SKILL.md** — general instructions that work for anyone
- **context.md** — your personal config (brand, paths, preferences). Create this locally after installing.
- **context.example.md** — shows what to configure

Install a skill, create your own `context.md`, and it's personalized to your setup. No forking required.

## License

MIT
