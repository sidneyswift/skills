# Tweakable plan

Write implementation plans sorted by likelihood-of-tweaking, not execution order, so the user's attention lands on the judgment calls and the mechanical work stays out of the way. Use whenever producing an implementation plan a human will review.

Example trigger prompt:

> Write an implementation plan for annotation export, but lead with the decisions I'm most likely to tweak: data model changes, new type interfaces, and anything user-facing. Bury the mechanical refactoring at the bottom. I trust you on that part.

## Structure

Open with a header strip: effort estimate, files touched, risk level, migrations. Then three sections.

### Section A: decisions the user will probably want to change

The judgment calls, each presented with its alternative:

- **Data model choices**: show the schema; flag each contested column with the alternative considered. For each flagged choice give the plan's pick with its reasoning and cost, the alternative with its own merits, a "pick this if" line, and the one-line reply that switches it ("use live join").
- **New type interfaces**: show the actual types with numbered footnotes on the contestable fields: why a union member was included, which field is speculative and what cutting it saves ("if nobody asked for this, cutting it removes half a day"), which defaults are deliberate.
- **User-facing flow**: the steps, with the weakest step explicitly flagged and the nicer-but-costlier alternative priced ("a hybrid, wait up to 4s then fall back to notify, is nicer and adds half a day; your call").

### Section B: sequencing

The build order, numbered, with effort per step. Every step lands green on CI; nothing user-visible ships until the flag flips.

### Section C: mechanical work (trust me)

The refactors and plumbing with no judgment calls: extractions, renames, fixture wiring, flag registration, openapi regeneration. Collapsed or compressed; the user may skip it entirely.

## End with "tweak these three things"

Pre-write the 2 or 3 highest-leverage replies the user could send, each one line, copyable. This converts review from an essay into three taps.

## Quality bar

- Sort strictly by tweak-likelihood. If the user reads only the top third, they should have seen every decision that matters.
- Every flagged choice names its cost in concrete units (KB per row, days of work, seconds of render time).
- Flag your weakest decision yourself. Confessing it invites the correction you need.
- Keep Section C genuinely mechanical. If an item hides a judgment call, promote it to Section A.
