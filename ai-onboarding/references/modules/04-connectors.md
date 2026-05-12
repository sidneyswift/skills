# Module 04: Connectors

Teaches that AI becomes dramatically more useful when it can access their actual tools and data — and walks them through connecting what's available.

## When This Fires

- User's work involves data or tools that need connecting
- User has "ready" or "available" connectors identified in PROGRESS.md
- User is copy-pasting data into conversations when a connector would be better
- User asks "can it read my [Google Drive / email / calendar / etc.]?"

## Prerequisites

- Connector feasibility check must be done (from Discovery)
- PROGRESS.md must have a Connectors section with at least one "ready" item

## The Core Insight

Most users don't realize AI can connect to their tools. They think it's just a chat box. The moment they see it pull live data from their own Google Sheet or Slack channel, the mental model shifts permanently.

## The Approach

### 1. Start With the Easiest Win

Look at PROGRESS.md → Connectors → Ready. Pick the one that connects to work they've already done in Module 01. If their first workflow was "summarize meeting notes" and they use Google Docs — connect Google Docs.

### 2. Walk Through Setup, Don't Just Explain It

Different AI tools handle connectors differently:

- **Claude Pro/Team:** Projects can have connected tools. Walk through the settings.
- **Claude Code / Cursor:** MCP servers. More technical — only go here if the user is comfortable with a terminal.
- **ChatGPT:** Custom GPTs with actions, or plugins. Walk through the GPT builder.
- **Copilot (Microsoft):** Often pre-connected in enterprise. Check what's already available.

The setup instructions depend on which tool they're using. Ask which tool they primarily work in, then guide accordingly.

### 3. Demonstrate on Real Data

Once connected, immediately use it on real work:
- "OK, your Google Drive is connected. Let me find that Q2 report you mentioned..."
- "Now let's redo that task from our first session, but this time I'm pulling the data live instead of you pasting it."

The comparison with their old workflow is the "aha" moment.

### 4. Update the Map

After connecting something, update PROGRESS.md:
- Move from "Ready" to "Connected" with the date
- Note what workflows it unlocks
- Update CLAUDE.md with the new tool context

## Wall Avoidance — Critical

If a connector is Gated or Blocked, DO NOT try to push through it:

- Don't say "ask your IT team to enable API access" — the user will try, fail, and lose momentum
- DO say "that one needs some setup we can't do right now. Let's work with [fallback] and I'll note it for later"
- Always have the fallback ready BEFORE mentioning the limitation

## Completion Criteria

- [x] User has at least one connector working with real data
- [x] User has seen AI pull live data from their own tools (not copy-pasted)
- [x] User understands the difference between chat-only and connected AI

## Sequencing Notes

This module can fire early (if the user's first workflow naturally needs data from a tool) or late (if they're productive with copy-paste and other modules are more valuable first). Don't force it. Some users are perfectly effective without connectors for weeks.
