# Skillifying Work

Skillifying is the promotion path from **work that succeeded once** to **a durable capability the
workspace can reuse**. It is domain-agnostic: a technical workspace may produce scripts and tests; a
marketing workspace may produce a repeatable brief, checklist, examples, and review rubric. The point
is the same: the next agent should not rediscover the process from scratch.

## When to skillify
- Skillify when a task will repeat, must be maintained, or a failure should become structurally hard
  to repeat.
- Do **not** skillify one-off output. Keep it with its source package, evaluate durable value, and stop.
- Ask after meaningful work: **"Will this be done again or need upkeep?"** If yes, offer to
  skillify it.

## Promotion loop
1. **Prove package provenance.** Start from a real closed package, accepted result, artifact, or
   failure. If you cannot identify the evidence and steps that produced it, do not synthesize a skill.
2. **Name the capability.** Choose a short kebab-case name and 3-5 concrete trigger phrases the user
   is likely to say.
3. **Extract the invariant process.** Keep the parts that repeat. Remove chat fragments, false starts,
   and one-off details.
4. **Separate judgment from exact work.** The `SKILL.md` carries the process and decision rules.
   Deterministic or mechanical work belongs in `scripts/`, `assets/`, or templates, with checks where
   practical.
5. **Stage before publishing.** Draft under
   `work/{source-initiative}/YYYY-MM-DD-skillify-{name}/`. If skillification itself crosses the
   managed-work threshold and has no source package, create one first. Never leave a half-working
   skill in `plugin/skills/`.
6. **Verify for the domain.** Use the strongest cheap proof available:
   - code/script skill: unit test or smoke command against a fixture/sample;
   - document/process skill: run it against a sample prompt or prior artifact and compare to the
     accepted result;
   - review/quality skill: write 2-3 scenario prompts or a rubric and confirm the skill catches the
     important failure.
7. **Ask before publishing.** Show the proposed name, triggers, verification result, and destination.
   Only move the staged skill into `plugin/skills/{name}/` after approval.
8. **Repackage and register.** Re-zip `plugin/`, update any plugin README/index, and note the new skill
   in `artifacts/dashboard.html`; if it should run unattended, add a prompt in `routines/` (indexed in
   `routines/README.md`) so the scheduler can run it.

## Minimum skillified bundle
- `plugin/skills/{name}/SKILL.md` with valid frontmatter and trigger-rich description.
- Supporting `scripts/`, `assets/`, or `references/` only when they remove real repetition.
- A verification note in the staging folder or `SKILL.md` describing how it was tested.
- A provenance link from the source package and a durable learning in `knowledge/` only when the
  skill came from a reusable failure or important decision.
