# Social Slides — Setup

This skill uses two config layers:

## 1. Identity (shared across all skills)
Create `~/.config/<yourname>/identity.md` with your brand info.
This is read by every skill — set it up once.

See the skill-system skill for the full identity spec.

## 2. Skill config
Create `~/.config/social-slides/.env`:

```
SETUP_COMPLETE=true
DEFAULT_TEMPLATE=elegant-founder
DEFAULT_DIMENSIONS=1080x1350
DEFAULT_PLATFORM=linkedin
```

Or just run the skill — it will walk you through setup on first use.
