# Blindspot pass

Find the user's unknown unknowns in a part of the codebase before they prompt for an implementation there. Works best when the user is entering unfamiliar territory: a module they have never touched, with history they have never read.

Example trigger prompt:

> I'm adding a new SSO auth provider but I've never touched the auth module. Do a blindspot pass: find my unknown unknowns in this part of the codebase, explain each one, and tell me how to prompt you better for the implementation.

## What to scan

Read the target module and its history, not just its current code:

- Git history: reverted PRs (especially reverted attempts at this exact task), stalled migrations, commits whose messages explain a trap
- Stale TODOs with names and dates attached
- Feature flags whose dev and prod values differ
- The "obvious template" file a newcomer would copy, and whether it is actually safe to copy
- Registration and wiring steps that are not discoverable from the code alone (DB rows, fixture lists, config files)
- Event-bus or side-channel contracts that a naive implementation would silently skip
- Concepts the module's interface hides (identity vs account, snapshot vs live read)

## Output shape

Produce a report (HTML artifact or structured markdown) with:

1. **Framing**: what the task sounds like vs what the user is actually walking into. One short paragraph each.
2. **A count line**: e.g. "4 landmines · 2 unwritten conventions · 1 missing concept · 1 reverted attempt at this exact task (PR #2841)".
3. **One card per blindspot**, classified as landmine, unwritten convention, missing concept, or history. Each card has:
   - A specific title naming the trap, with file paths, PR numbers, and flag names
   - **Why it bites**: the exact way the user would discover this the hard way, and why tests would not catch it
   - **A copyable prompt fix**: one or two sentences of constraint, phrased ready to paste into the implementation prompt
4. **The improved prompt**: every fix folded into a single numbered prompt the user should actually give, ending with a work order and an explicit stop point ("stop and show me the plan after X before writing code").

## Quality bar

- Every blindspot must be bought with real evidence from the codebase: a file, a commit, a flag, a table. No generic advice ("consider edge cases").
- Each one should be worth roughly half a day of someone's pain. If it would be obvious within five minutes of opening the file, cut it.
- The improved prompt is the deliverable. The cards exist to justify its sentences.
