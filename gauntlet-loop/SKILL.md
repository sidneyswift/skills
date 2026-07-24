---
name: gauntlet-loop
description: >-
  Run iterative build-critique loops that push AI output past "good enough"
  toward a concrete quality bar. Give a lead agent a goal and a real
  reference to compare against. The agent decomposes the goal into the
  smallest independently-improvable pieces, assigns each piece a builder
  and a separate critic with fresh context, and loops until the output
  matches or exceeds the bar. Use when the first draft is never good
  enough — games, websites, product design, writing, marketing campaigns,
  code, research, or anything where output can be inspected and improved.
metadata:
  author: Sidney Swift
  version: "0.1.0"
  source: "Matt Shumer — 'How to Run a Gauntlet Loop' (somethingbig.ai/gauntlet-loop)"
---

# Gauntlet Loop

## Overview

Most agent workflows produce one result and stop. The result is
usually "pretty good for AI" — and that's where the bar stays.

A Gauntlet Loop raises the bar by adding a concrete reference and an
independent critic. The lead agent breaks the goal into the smallest
pieces that can be improved separately. Each piece gets its own
builder and a separate critic with fresh context. The critic compares
the output against the reference. If the reference wins, the critic
identifies the biggest remaining gap and sends the work back. The
loop continues until the output reaches the bar — or you decide it's
ready.

The method is simple: split, build, judge, repeat. The leverage comes
from the bar being real, the critic being independent, and the loops
running longer than you'd expect.

## When to use

- "Make this actually good, not just AI-good"
- "I want this to compete with the best examples in the category"
- "Keep improving it until it's great"
- "Build something ambitious — a game, a full site, a polished app"
- "The first draft is never good enough"
- Any task where the output can be inspected and iteratively improved
- Any task where you have (or can find) a concrete quality reference

## Core principles

### 1. Use an actual agent

Do not paste a Gauntlet Loop into a normal chat. Run it inside an
agentic harness — Claude Code, Codex, OpenClaw, or any environment
where the model can open files, run code, render results, inspect
screenshots, use tools, and spawn other agents.

Subagents are critical. Each critic should run in its own clean
context window so it judges the artifact independently, without the
builder's history or rationalizations.

### 2. Give it the goal, not the implementation

Tell the agent what you want. Do not tell it how to build it.

The best models are very good at deciding how to approach a large
goal. When you prescribe the architecture, workstreams, and every
step, you replace the model's judgment with your own.

Give it the destination. Let it choose the route.

### 3. Give it a real bar

The bar is the most important part.

"Make it amazing" is not a bar. The agent needs something concrete
it can inspect and compare its work against.

| Domain | Example bar |
|---|---|
| Game | Real Call of Duty screenshots |
| Website | The 5 best real websites in the category |
| Writing | Paragraphs with the clarity level you want (e.g., Paul Graham) |
| Backend code | A test suite, latency target, or reference implementation |
| Design | Screenshots of the design quality you're targeting |
| Marketing | The best-performing campaigns in your space |

A hard bar does not need to be realistically reachable. The game
never became better than Call of Duty — but Call of Duty gave the
agent a direction and kept it from stopping at "pretty good."

When you don't know the right bar, make finding one part of the task:

> Find a concrete comparison or measurement that plays the same role
> for this task that real Call of Duty screenshots played for the
> game. Explain why it is a useful bar, then judge every round
> against it.

### 4. Let the agent split the work

Tell the lead agent to break the goal into the smallest pieces that
can be improved and judged separately.

For a game: gun, hands, trees, lighting, movement, enemy behavior,
sound, effects — each in its own loop.

For an article: argument, opening, examples, sections, paragraphs,
transitions — each judged separately.

Do not decide these pieces in advance. The agent understands the
artifact and can decide which parts should be separated, which should
stay together, and which can run in parallel.

The key insight: "make the game better" is too vague. "Make this one
tree compare favorably with the reference tree" gives the agent a
problem it can repeatedly attack.

### 5. Never let the builder grade itself

The builder and critic must be separate agents.

The builder remembers every decision it made and is very good at
explaining why its work is reasonable. You don't want reasonable. You
want an independent judgment.

Spawn a fresh critic. Give it the goal, the bar, the rules, and the
actual artifact. Do not give it the builder's history or explanation.

The critic should behave like a blind A/B tester: look at the output
and the reference without being told which is which, choose the
better one, and identify the largest meaningful gap when the output
loses.

The critic must inspect the real thing — actual pixels, running
product, rendered page, test results, or finished writing. Never
grade a summary written by the builder.

### 6. Let it keep going

Do not set a fixed number of rounds. Tell it to keep looping. There
is almost always another gap to close.

You stop when:
- You like the result
- Improvements become too small to matter
- You've spent as much compute as you're willing to spend

### 7. Watch without interrupting

For long runs, tell the agent to create a simple live HTML page or
progress document and update it as it works. Open it from your phone.
You can see how the work evolves without interrupting the agent every
twenty minutes.

When you're happy, return and stop the run.

### 8. Optional smoothing pass

When many agents change separate parts of one artifact, the pieces
can become individually good but slightly inconsistent.

At the end of each major wave, spawn one fresh agent to inspect the
complete result and smooth it out. Its job is not to redesign — just
make the pieces work together and feel like one thing.

## Process

### Phase 1: Define the goal and the bar

State the goal clearly. Identify or find a concrete quality
reference the critic can compare against. If no reference exists,
make finding one part of the task.

### Phase 2: Write the prompt

Use the meta-prompt below — or write a short prompt directly. The
prompt should include:

- The goal
- The bar (reference to compare against)
- Instruction to decompose into smallest improvable pieces
- Instruction to use separate builders and critics
- Instruction to keep looping until the bar is met
- Instruction to maintain a live progress page

Keep it short. Let the agent decide the specifics.

### Phase 3: Run it

Send the prompt to a coding agent (Claude Code, Codex, OpenClaw
subagent). Let it run. Watch the progress page. Don't interrupt
unless something is fundamentally wrong.

### Phase 4: Stop when ready

The result will still be improving when you stop. That's fine.
Decide based on quality, time, or compute budget.

## Meta-prompt

Use this to generate a task-specific Gauntlet Loop prompt. Paste it
into a strong model along with your goal, then run the output inside
a coding agent.

```
I want to run a Gauntlet Loop for this goal:

[GOAL]

Possible references or quality bars:

[OPTIONAL REFERENCES]

Choose the strongest concrete bar that an agent can actually inspect
and compare its work against. If I have not supplied one, propose a
useful comp or measurement that plays the same role for this task
that real Call of Duty screenshots played for Matt Shumer's Claude of
Duty game (read the prompt:
https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md).
Explain the bar in one sentence.

Then write a short prompt for Claude Code or Codex in the style of
Matt's prompt (minimal is better — we want the agent to decide the
specifics).

Give the lead agent the goal and the bar, but let it choose the
approach. Tell it to divide the goal into the smallest pieces that
can be improved and judged independently. For each important piece,
it should fan out a builder and a separate critic with fresh context.

Each critic must inspect the real output, compare it directly with
the bar — using a blind A/B comparison when possible — identify the
biggest remaining gap, and send it back for another round. Keep
looping until our output wins or I stop the run.

Have the lead agent maintain a simple live progress page that shows
the work evolving over time.

Have it use subagents and ultracode. Do not prescribe the
architecture, exact decomposition, or a fixed number of rounds.
Keep the final prompt short, just like Matt's.
```

## Output format

A Gauntlet Loop produces:

- The finished artifact (game, site, document, code, design, etc.)
- A progress page showing the evolution over time
- Implicit: a quality bar that can be reused for future iterations

## Anti-patterns

- **Setting a vague bar.** "Make it amazing" or "production-ready"
  gives the critic nothing to compare against. Use a concrete
  reference.
- **Prescribing the decomposition.** Let the agent decide how to
  split the work. It understands the artifact better than a
  predetermined breakdown.
- **Letting the builder grade itself.** The whole point is
  independent judgment. Always spawn a separate critic with fresh
  context.
- **Fixing the number of rounds.** "Do 3 rounds and stop" defeats
  the purpose. Let quality determine when to stop.
- **Interrupting the run.** Watch the progress page. Only intervene
  if something is fundamentally wrong. Frequent interruption breaks
  the agent's autonomy.
- **Debugging the output instead of the bar.** When results are
  underwhelming, the bar is usually too vague or too easy. Fix the
  bar, not the process.
