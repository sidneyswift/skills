# Options brainstorm

Turn a rough problem into a ladder of codebase-grounded interventions the user can react to. Use when the user has a problem, not a solution: "users churn after onboarding", "the app feels slow", "support tickets are up".

Example trigger prompt:

> Here's my rough problem: users churn after onboarding. Search the codebase and brainstorm 10 places we could intervene, from cheapest to most ambitious. I'll tell you which ones resonate.

## Before writing anything

Search the codebase for the relevant surfaces and read what is actually there. The most valuable finds are retention machinery that already exists but is disconnected:

- Features fully built behind a flag that was never turned on
- Tables the backend writes that no client code reads
- TODO comments from the original author marking the exact gap
- Silent failure paths that log to monitoring but tell the user nothing
- Deliberately crippled capabilities with a "revisit later" comment attached

Cheap options are usually wiring, not building. Surface those first.

## Output shape

A single artifact (HTML preferred) with:

1. **A framing line**: what was searched, and the pattern that emerged.
2. **A ladder visualization**: options 1 to 10 plotted from "ship this afternoon" to "quarter-long bet", tagged by kind (wiring, new UI, new lifecycle, new surface).
3. **One card per option** with:
   - Rank, title, and a size tag (S/M/L/XL)
   - The real file paths involved
   - **Found in code**: the evidence, described specifically (the flag name, the table name, the age of the TODO)
   - **Impact**: who it affects and why it moves the metric
   - A "this resonates" checkbox
4. **A reply assembler**: checked options compose the user's reply.

## Quality bar

- Every option grounded in something real: a file, a flag, a table, a ticket. If an option has no codebase evidence, say so explicitly and mark it as a new surface.
- Order strictly cheapest to most ambitious, and make the cheap end genuinely cheap (flag flips, one-component wiring).
- The expensive end should change the problem's structure, not just add polish (new user populations, new acquisition loops).
- Ten is the target count; fewer is fine if the codebase genuinely offers fewer distinct levers.
