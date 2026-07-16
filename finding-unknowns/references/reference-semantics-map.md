# Reference semantics map

Prove understanding of a reference implementation before porting or imitating it. Source code is the best reference there is, even in a different language: it answers questions a written description never will. Use when the user points at existing code ("this Rust crate implements the exact backoff behavior I want") and the task is to reimplement its semantics elsewhere.

Example trigger prompt:

> This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client, but first show me a semantics map so I can confirm you understood it.

## The rule

Nothing gets implemented until the user signs off on the map. The map is the checkpoint where misreadings get caught for the price of a reply instead of a rewrite.

## Output shape

1. **What the reference actually does**: the behaviors and invariants, each stated with its magic numbers and the reason it exists ("refill is lazy and integer-truncated; `last_refill` only advances when at least one whole token is minted, so sub-token elapsed time carries forward"). Include which responsibilities stay with the caller.
2. **Side-by-side pairs**: source excerpt next to the proposed target excerpt, with numbered gotcha notes anchored to specific lines. Gotchas worth hunting for:
   - Integer truncation vs float division
   - Inclusive vs exclusive ranges (a one-character bug magnet)
   - Monotonic clocks vs wall clocks
   - Saturating arithmetic and overflow guards: needed in the target or provably unreachable?
   - Locks and atomicity: what a mutex guaranteed, and what convention must preserve it in a single-threaded runtime (e.g. no `await` between check and debit)
   - Stateful seeds and injectable randomness for deterministic tests
3. **Preserved / deliberately changed / dropped**: three explicit lists. Every dropped item states why it is safe to drop; every change states the equivalence argument.
4. **Edge-case table**: the tricky scenarios (clock skew, burst at t=0, exhaustion, cap behavior), expected behavior on both sides, and whether the match is identical or equivalent-with-a-different-surface. Flag the rows where the port intentionally differs.
5. **Sign-off gate**: ask for "semantics confirmed" or a correction quoting the numbered note or table row to revise.

## Quality bar

- Port the reference's tests first and replay its fixture values verbatim where possible.
- Every gotcha note names the concrete failure mode of getting it wrong, not just the difference.
- "Equivalent" rows must say what differs and why the decision is still the same.
- Keep the caller/library boundary where the reference put it unless the user asks otherwise.
