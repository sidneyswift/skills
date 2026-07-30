---
name: handoff-spec
description: >-
  Produces a single markdown handoff document for a stateless successor agent
  (possibly on a different platform or session) to pick up in-progress work
  with zero conversation context. Combines a stable Goal/Spec section with a
  point-in-time Handoff Status section covering what's done, out-of-scope
  work, remaining required work, nice-to-haves, what's live in production,
  what's merged but not deployed, and what's still in progress. Use when the
  current agent is running low on usage credits, context, or tokens; when the
  user says things like "I'm running out of credits/usage", "we need to hand
  this off", "write a handoff doc/spec", "summarize where we left off for
  another agent", or when wrapping up a session with unfinished work that a
  different agent or session will continue.
metadata:
  author: Sidney Swift
  version: "0.1.0"
---

# Handoff Spec

## Overview

Produces a handoff document that lets a completely stateless successor agent resume in-progress work — it has never seen this conversation, but can read the repo, git history, PRs, and issues.

## Process

1. **Verify current state — don't rely on conversation memory.** Your own recollection of "what I did" can be stale or wrong compared to what's actually on disk or in the tracker. Before writing anything, check the real state:
   - `git status` and `git log --oneline -20`
   - `git diff <base-branch>...HEAD` (or against the last handoff commit, if one exists)
   - `gh pr list --state all --limit 20`, and `gh pr view <n>` for anything relevant
   - `gh issue list` for open issues tied to this work
   - If deploy/production status isn't derivable from the repo (e.g. no CI/CD visible), ask the user rather than guessing.

2. **Decide finished vs. not finished, first.** If there is no required in-scope work remaining, the very top line of the document must say `FINISHED — no in-scope work remains`. Never bury a "we're actually done" under status sections that read as if more work is needed.

3. **Check for a prior handoff doc for this same task.** If one exists (e.g. `HANDOFF-*.md` in the repo, or the user points to one), reuse its **Goal / Spec** section verbatim — that section is the stable north star and should not drift between handoffs. Only the **Handoff Status** section gets rewritten each time.

4. **Copy the template** at [assets/HANDOFF_TEMPLATE.md](assets/HANDOFF_TEMPLATE.md) and fill it in. Don't paraphrase the structure from memory — every section exists to answer a specific question the successor will otherwise have to rediscover:
   - Done / out-of-scope-but-done / remaining-required / remaining-nice-to-have map directly to "what's done, what's scope creep, what's left, what's optional"
   - In-production / merged-not-deployed / still-in-the-works map to "what's live, what's ready to go live, what's unfinished"
   - Gotchas capture anything that looks right but isn't, so the successor doesn't repeat a dead end
   - Delete any subsection explicitly marked as droppable-if-empty rather than leaving a hollow heading.

5. **Write for a reader with zero context.** No "as discussed above," no unexplained shorthand or internal jargon from this conversation, no assuming the reader knows why a decision was made — state it plainly, as if handing this to an engineer who just joined.

6. **Save the file.** Default to `HANDOFF-<short-task-slug>.md` at the repo root unless the user specifies otherwise. If a handoff doc for this task already exists, overwrite it in place (status is a snapshot, not a log) rather than accumulating duplicate handoff files — the Pointers/Goal sections carry forward, only Handoff Status changes.
