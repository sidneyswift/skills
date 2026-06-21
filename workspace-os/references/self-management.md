# The Self-Management Contract (what CLAUDE.md must enforce)

A workspace OS is only alive if the agent keeps it current. The generated `CLAUDE.md` must encode
three contracts. (`AGENTS.md` is a symlink to `CLAUDE.md`, so this governs every agent runner.)

## 1. The auto-manage loop (run on every new input, without being asked)
When the user adds material (file, transcript, note, result) OR asks for work, run end to end:
1. **Place** the raw file in its correct home, dated `YYYY-MM-DD`.
2. **Read** it.
3. **Extract** reusable value (insights, answers, decisions) into `knowledge-base/`.
4. **Scan** the related entity/pipeline folder; read its README; reconcile against the new info.
5. **Update everything affected** in the same turn: entity `README.md` dashboards, `_board.md`,
   `operating-system/dashboard.html`, metrics. This is the never-stale rule.
6. **Move** folders to match reality (stage changes); update any external system of record.
7. **Mine** for compounding assets (templates, proof, FAQs).
8. **Report** what changed.

## 2. The never-stale contract (state management is the agent's job)
- "Touched the project" = "left it consistent." Never end a turn with a dashboard, board, or README
  that contradicts what just happened.
- After any change, ask: *which other files now disagree with reality?* Update them all.
- The **janitor skill** is the backstop: it reconciles the whole OS and is wired to a scheduled task
  (default weekly) so drift is caught even when no one is looking.
- Staleness signals the janitor hunts: entity READMEs whose "next action" is in the past; items in the
  wrong pipeline stage; un-ingested files in inbox/raw; dashboards that don't match the folders;
  recurring answers not yet in the knowledge base; repeated tasks not yet skills.

## 3. The compound-learning contract (get smarter every session)
- Every work session must deposit at least one durable learning: a decision (`knowledge-base/decisions/`),
  a canonical answer (`knowledge-base/faqs/`), an insight (`knowledge-base/insights/`), or an improved
  template/skill.
- Never solve the same problem twice — search the knowledge base first; if the answer exists, reuse it;
  if it doesn't and the question is recurring, write it down.
- **Anything done more than once becomes a skill.** When a task repeats, author a new skill and
  repackage the plugin so it can trigger automatically.
- Keep `operating-system/rituals.md` with the cadences (e.g. weekly review, periodic value review)
  and prefer wiring the recurring ones as scheduled tasks.

## Filing decision tree (customize labels per domain)
1. Reusable instrument (template/script/checklist)? -> `library/`
2. Repeatable task/capability? -> `skills/` (make it a skill)
3. Reusable answer/insight/decision/SOP? -> `knowledge-base/`
4. A flowing item not yet "done"? -> the staged `{pipeline}/` folder
5. Tied to a core entity? -> `{entities}/{name}/`
6. Outcome/proof? -> `proof/`
7. Raw/idea/draft/published content? -> `content/`
8. Canon/source/spec/brand? -> `reference/`
9. Legal/finance/metrics? -> `business-ops/`
