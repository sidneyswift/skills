# The Self-Management Contract (what CLAUDE.md must enforce)

A workspace OS is only alive if the agent keeps it current. The generated `CLAUDE.md` must encode
the contracts below. (`AGENTS.md` is a symlink to `CLAUDE.md`, so this governs every agent runner.)
Managed-work details live once in `work/AGENTS.md`; the root brain must route agents there.

## 1. The auto-manage loop (run on every new input, without being asked)
When the user adds material (file, transcript, note, result) OR asks for work, run end to end:
1. **Place** the raw file in its correct home, dated `YYYY-MM-DD`.
2. **Read** it.
3. **Search** managed packages plus the related entity/pipeline; resume equivalent work.
4. **Extract** only settled reusable value into `knowledge/`; raw findings stay with their package.
5. **Reconcile** each authority: package coordination, entity/pipeline domain state, and declared
   external fields.
6. **Update everything affected** in the same turn: package README/optional plan, entity dashboards,
   `_board.md`, recurring artifacts, and metrics.
7. **Move** domain folders to match reality; do not move packages merely to represent archive state.
8. **Mine** for genuinely reusable templates, proof, FAQs, skills, checks, or evals.
9. **Handoff** with one exact next action; reconcile `work/README.md`.
10. **Append** a material lifecycle event to `PROGRESS.md`, then report what changed.

## 2. The never-stale contract (state management is the agent's job)
- "Touched the project" = "left it consistent." Never end a turn with a dashboard, board, or README
  that contradicts what just happened.
- After any change, ask: *which other files now disagree with reality?* Update them all.
- **Consistency is checked, not felt.** The read-only `{OS}-system-check-health` is the verification surface —
  it scores the workspace and writes a punch list to `operations/health.md`. "Left it consistent"
  means a clean doctor run, not a confident summary.
- The **janitor skill** is the backstop: it runs the doctor, fixes what's safe, and is wired to a
  scheduled task (default weekly) — its runnable prompt is `routines/janitor.md` — so drift is caught
  even when no one is looking.
- Staleness signals the doctor hunts: entity READMEs whose "next action" is in the past; items in the
  wrong pipeline stage; un-ingested files in inbox/raw; dashboards that don't match the folders;
  recurring answers not yet in the knowledge base; repeated tasks not yet skills; one-off work left at
  the root instead of `work/`; managed work without an owner/next action; blocked, paused, or review
  work past its check date; terminal work without evidence/disposition; **dark skills**; manifests
  out of version/name parity.

## 3. The compound-learning + self-improvement contract (get smarter from evidence)
- After a meaningful discovery or closure, evaluate whether anything is genuinely reusable: a
  decision, canonical answer, insight, template, skill, proof, check, or eval. Capture it with package
  provenance when yes; record a valid "nothing reusable" disposition when no.
- Never solve the same problem twice — search the knowledge base first; if the answer exists, reuse it;
  if it doesn't and the question is recurring, write it down.
- **Ask "skillify this?"** After finishing work, ask whether it will repeat, need upkeep, or prevent a
  failure from recurring. If yes, run the `{OS}-system-promote-skill` skill; it stages the draft under
  the owning work package, verifies it, asks for approval, then moves it into `plugin/skills/` and
  repackages. **Unattended** (a scheduled
  janitor with no human present): skillify stops at staged + verified + *proposed* (logged to
  `operations/improvements.md`); publishing to `plugin/skills/` waits for approval unless the workspace
  sets an explicit autonomous-publish policy.
- **Improve the system, not just its contents.** `knowledge/` and `plugin/skills/` compound content
  and capabilities; `{OS}-system-improve-machinery` compounds the machinery. After meaningful work,
  inspect whether observed friction justifies a skill, routing row, doctor check, template, eval, or
  `CLAUDE.md` rule. A grounded no-op is valid.
- Keep runnable workflow prompts in `routines/` — one file per scheduled/remote workflow (janitor,
  reflect, learn, and domain runs) — indexed by `routines/README.md` with each one's cadence + arm
  status, and prefer wiring the recurring ones as scheduled tasks.
- **Burn down draft-debt.** When you touch a file/folder carrying "draft — confirm" markers, confirm or
  correct them in the same turn. Sparse-input builds start with many predictions; the doctor counts
  them, and normal work should retire them rather than let them pile up.
- Keep `plugin/skills/` as the source of truth for skills. `.agents/skills` is only the Cursor/Codex
  discovery adapter and should point to or mirror `plugin/skills/`.

## 4. The self-describing contract (brain currency, progress log, grow-on-demand)
- **The brain updates itself.** `CLAUDE.md` must always match the real folders and rules. Whenever the
  system changes — a folder added/renamed, a skill authored, a convention or routine changed — update
  `CLAUDE.md` in the same turn (`AGENTS.md` is its symlink). A stale brain is the highest-severity
  drift; the doctor's brain-currency check gates on it.
- **Append material lifecycle events to `PROGRESS.md`.** The root log is append-only:
  `## YYYY-MM-DD` then `- **{what}** — {why}`. Record starts, blocks, pauses, reviews, closure,
  reopening, direction-changing evidence, promoted assets, and machinery changes. Package README
  files hold current state.
- **Grow on demand, stay lean.** Start from the spine (`plugin/ routines/ scripts/ docs/ work/`); create
  any other top-level folder (`knowledge/`, a pipeline, an entity folder, or a new one-word folder the
  domain needs) only when real material arrives or an organ needs it. Each organ creates the folder it
  writes to on first use. Every top-level folder and file name is a single lowercase word.
- **Three layers.** Domain flow lives in pipeline/entities, consequential execution gets a linked work
  package, and reusable value graduates to knowledge/library/proof/artifacts/skills/machinery.
- **Scripts live in `scripts/`; skills live in `plugin/skills/`** (named `{OS}-{area}-{verb}-{noun}`),
  never elsewhere.

## Filing decision tree (customize labels per domain)
1. Consequential work that must survive context loss? -> follow `work/AGENTS.md`
2. Reusable instrument (template/script/checklist)? -> `library/`
3. A task that will repeat or need upkeep? -> run `{OS}-system-promote-skill`
4. A finalized output you regenerate/keep current? -> `artifacts/`
5. A simple one-off / ad-hoc build? -> `work/{project}/YYYY-MM-DD-…/`
6. Reusable answer/insight/decision/SOP? -> `knowledge/`
7. A flowing item not yet "done"? -> the staged `{pipeline}/` folder
8. Tied to a core entity? -> `{entities}/{name}/`
9. Outcome/proof? -> `proof/`
10. Raw/idea/draft/published content? -> `content/`
11. Canon/source/spec/brand? -> `reference/`
12. Legal/finance/metrics? -> `business/`
13. A workflow to run on a schedule / unattended? -> a routine prompt in `routines/`
    (indexed in `routines/README.md`)

## 5. Managed-work lifecycle (the portable handoff interface)

Create a package when another session/agent is likely, a blocker/review gate exists, research can
change the approach, durable evidence is required, or the user asks to track it. Keep simple same-turn
work package-free.

Use the statuses and transition rules in `work/AGENTS.md`. The package README owns coordination;
optional `plan.md` owns detailed tasks. Before stopping, preserve current state, exact next action,
changed artifacts, verification, blockers/review needs, and unresolved assumptions.

Complete or cancel only after recording closure evidence, outcome, remaining work, and durable-value
disposition. Keep the package path stable and place it under its closure year in the derived
`work/README.md` archive view.
