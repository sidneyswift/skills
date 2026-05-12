# Stage Assessment — How to Classify a User

Assess the user's stage from their opening answer and early conversation. Don't ask them to self-assess — infer from signals.

## The Opening Question

> "What's a piece of work you'd want AI help with this week?"

Their answer reveals:

### Signal: Specificity

| Answer Pattern | Likely Stage | Why |
|---|---|---|
| "I don't know" / "make me more productive" / "what can it do?" | Stage 1: Never used | No mental model of AI capabilities |
| "Help me write emails" / "summarize stuff" | Stage 2: Chat-only | Knows AI can do text tasks, hasn't gone deeper |
| "Summarize the Q2 sales folder in Drive" | Stage 3: Tool-connected | Knows where their data lives, has a specific outcome |
| "Every Monday I pull metrics from three dashboards and make a slide deck" | Stage 4: Workflow builder | Sees patterns in their own work, thinks in processes |
| "I built a prompt for this but it's inconsistent" | Stage 4–5: Workflow/Skill builder | Already building, needs refinement |
| "How do I get my team using this?" | Stage 5–6: Skill builder / Fleet manager | Personal use is handled, thinking about scale |

### Signal: Vocabulary

| They say... | Suggests... |
|---|---|
| "AI" / "the chatbot" / "this thing" | Stage 1–2. Generic terms = early |
| "Claude" / "ChatGPT" / "the model" | Stage 2–3. Knows specific tools |
| "Context window" / "tokens" / "system prompt" | Stage 4+. Technical vocabulary |
| "MCP" / "connector" / "agent" / "skill" | Stage 5+. Builder vocabulary |
| "Spreadsheet" vs "model" / "deck" vs "presentation" | Domain vocabulary reveals their world. Not a stage signal but critical for understanding their tools. |

### Signal: Scope Awareness

| Pattern | Interpretation |
|---|---|
| Asks for one impossible thing ("build me an app") | Doesn't understand AI's strengths and limits. Stage 1. Needs first-workflow grounding. |
| Asks for something reasonable but too big | Stage 2–3. Understands capabilities but not iteration. Teach scoping. |
| Asks for something small and achievable | Stage 3+. Good instincts. Get them a win and push to next level. |
| Asks about a process, not a task | Stage 4+. Thinks in workflows already. Skip to skill-building. |

## Confidence Threshold

You don't need perfect classification. Get within one stage. The modules self-correct — if you start someone on Module 03 and they're confused by basics, drop back. If you start someone on Module 01 and they're bored, skip ahead.

## What to Write in PROGRESS.md

After assessment:

```markdown
## Current Stage
Stage 2: Chat-only

## Assessment Notes
- Opening answer: "Help me write better emails to clients"
- Vocabulary: uses "AI" generically, knows ChatGPT by name, hasn't tried Claude
- Scope: reasonable ask, specific enough to act on
- Role: Account manager at a marketing agency (inferred from conversation)
- Key tools: Gmail, Google Sheets, Slack, Monday.com
- Learning style: prefers examples over theory (showed impatience with explanation, engaged when we did a live demo)
```

## Don't Over-Assess

The goal is to start working, not to build a complete profile. Capture what you observe naturally during the first session. The profile gets richer over time as you watch them work.
