# Connector Feasibility Check — Wall Avoidance Protocol

Before suggesting any tool, integration, or connector to a user, run this check. The goal: never let someone hit a wall and blame AI.

## The Check

For each potential connector/integration:

### 1. Can they do it themselves?

- Does it need an API key they can generate?
- Does it need admin/IT approval?
- Does it need a paid plan they might not have?
- Does it need technical setup (CLI, environment variables, config files)?

### 2. Classification

| Category | Meaning | Action |
|---|---|---|
| **Ready** | User can set this up right now, no dependencies | Suggest it. Walk them through it. |
| **Available** | Exists but needs a step — a signup, a config change, a download | Offer it. Explain the step. Let them decide. |
| **Gated** | Needs someone else — IT, a manager, a billing admin | Note it in PROGRESS.md. Don't suggest it as a path. Come back to it when the gate opens. |
| **Blocked** | Not possible in their environment — wrong platform, no API, enterprise-only | Skip entirely. Don't even mention it unless they ask. |

### 3. Always Have a Fallback

Every blocked connector has a manual workaround:

| Blocked Path | Fallback |
|---|---|
| Can't connect to CRM API | Export CSV, work with the file |
| Can't install MCP server | Copy-paste the data into the conversation |
| Can't access internal wiki | Ask them to paste the relevant section |
| Can't connect to email | Draft in the chat, they copy to email |
| Can't connect calendar | They tell you their schedule verbally |
| Can't run code locally | Use the AI's built-in code execution |

The fallback is always "we work with what you have." The user should never feel like they can't do something because they're missing a tool.

## Common Walls by Role

### Office/Knowledge Workers
- Google Workspace: usually Ready (personal account) or Available (org account, may need admin to enable API)
- Microsoft 365: usually Gated (admin controls API access)
- Slack: usually Available (user can generate tokens for personal use)
- Notion: usually Ready (personal) or Available (workspace admin needed)
- Salesforce/HubSpot/CRM: usually Gated (API access is admin-controlled)

### Developers
- GitHub: usually Ready
- VS Code / Cursor: usually Ready
- CI/CD: varies — personal repos Ready, org repos often Gated
- Cloud services (AWS, GCP): usually Gated for org accounts

### Creatives
- Figma: usually Ready (personal) or Available (org)
- Adobe Creative Cloud: plugins usually Ready, API access varies
- Canva: usually Ready
- Brand assets: often scattered, not a connector issue but a "where is it" issue

### Managers
- Project management (Asana, Monday, Jira): usually Gated (workspace admin)
- Analytics (GA, Mixpanel): usually Gated
- Reporting tools (Power BI, Tableau, Looker): usually Gated

## How to Ask Without Making It Feel Like a Blocker

Don't say: "Do you have API access to Salesforce?"
The user doesn't know what that means, and it sounds like a barrier.

Do say: "I can work with Salesforce data. The easiest way is to export a report as CSV — have you done that before?"

Start with the easy path. Only explore the harder path if they signal they want it.

## What to Write in PROGRESS.md

```markdown
## Connectors

### Ready
- Google Sheets — user has personal account, can share files directly
- Gmail — accessible, user comfortable with it

### Available
- Slack — user has account, would need to create a bot token (showed interest, parking for Module 04)
- Notion — personal workspace, API key is self-serve

### Parked
- HubSpot — company CRM, user doesn't have API access. IT contact: their manager Sarah
- Monday.com — org workspace, admin-only API. Fallback: export boards as CSV

### Not Relevant
- GitHub — user doesn't code
- Figma — not in their workflow
```

## The Cardinal Rule

If you're about to say "let's connect X" — stop. Run the check. If it's not Ready, offer the fallback first, connector second. The user's first experience with a connector should be one that works on the first try.
