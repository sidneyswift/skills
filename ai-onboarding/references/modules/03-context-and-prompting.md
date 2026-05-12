# Module 03: Context & Prompting

Teaches that the quality of AI output is proportional to the context you provide. Better inputs, better outputs.

## When This Fires

- User gives vague prompts and gets vague results
- User asks "how do I talk to AI better?"
- User doesn't provide examples, constraints, or audience context
- User asks the same question multiple ways hoping for a better answer (instead of providing better context)

## The Core Insight

Most people think prompting is about finding magic words. It's not. It's about giving the AI the same context you'd give a smart new hire on their first day:

- What's the goal?
- Who's the audience?
- What does good look like? (Examples)
- What constraints exist? (Length, tone, format, must-include/exclude)
- What have you already tried?

## The Approach

### 1. The Side-by-Side

Take a real task from their work. Do it twice:

**Version A — Minimal prompt:**
"Write a project update."

**Version B — Context-rich prompt:**
"Write a project update for my team Slack channel. The project is our Q3 website redesign. Key updates: design mockups approved by stakeholders last Thursday, dev sprint starts Monday, one open question about the hero section copy. Tone: casual but professional — this is an internal update, not a client-facing one. Keep it under 200 words."

Show both outputs. The difference teaches itself.

### 2. The Context Checklist

After the demo, give them a mental checklist for any prompt:

1. **What** — the specific task (not "help me with email" but "write a follow-up email to a client who missed a deadline")
2. **Who** — the audience (internal team? executive? customer? public?)
3. **How** — format, tone, length constraints
4. **Example** — what good looks like (even a rough one helps enormously)
5. **Why** — the purpose behind the task (helps AI make judgment calls)

They don't need all five every time. But they should know to check.

### 3. Practice Round

Let them rewrite a vague prompt they've used before with the checklist. Run both versions. Let the output speak.

### 4. The Context File Concept

Introduce the idea that CLAUDE.md in their workspace is permanent context — things they'd tell every new AI session. If they find themselves repeatedly saying "I work in marketing at a SaaS company" — that goes in the file.

## Completion Criteria

- [x] User has written a context-rich prompt independently
- [x] User has seen the difference between vague and specific prompts on their own work
- [x] User understands that CLAUDE.md is "permanent context" they can edit

## Don't

- Don't teach "prompt engineering" as a discipline. No jailbreaks, no role-play tricks, no "act as a..." preambles. Just: give context, be specific, show examples.
- Don't overwhelm with the checklist. If they naturally provide 3 out of 5, just reinforce what they're doing right and nudge the missing piece.
- Don't make this feel like homework. It should come up naturally from a real task, not as a standalone lesson.
