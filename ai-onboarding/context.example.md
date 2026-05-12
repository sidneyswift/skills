# AI Onboarding — Context Configuration

Optional. Only needed when deploying for a specific organization or team.
For personal use, the skill works without this file.

## Organization

```
ORG_NAME=Acme Corp
ORG_SIZE=50-200
INDUSTRY=SaaS / Marketing
```

## Available Connectors

List connectors your org has approved and available. The skill uses this to avoid suggesting blocked integrations.

```
APPROVED_CONNECTORS=google-workspace,slack,hubspot,notion,github
BLOCKED_CONNECTORS=salesforce (needs enterprise plan),power-bi (IT only)
```

## Custom Modules

Add org-specific module files to `references/modules/` and list them here. They'll be included in the module routing.

```
CUSTOM_MODULES=onboarding-company-tools,security-training
```

## Admin Contact

Who to direct users to when they hit a permissions wall.

```
ADMIN_CONTACT=IT Help Desk — #it-help on Slack
ADMIN_EMAIL=it@acmecorp.com
```

## Provisioning Mode

How workspaces get set up:
- `self-serve` — user runs setup themselves
- `admin-triggered` — admin triggers setup with user context
- `hybrid` — admin provides context file, user runs setup

```
PROVISIONING_MODE=self-serve
```
