# Universal Workspace-OS Anatomy

Every workspace OS shares the same DNA, but **scaffold to the bone**. Create only the minimal spine
that must exist from day one; let the agent grow the rest **on demand** — and let each organ create the
folder it needs the first time it needs it (the doctor makes `operations/` on its first run, the learn
skill makes `knowledge/` on its first capture). The split that matters most: **compounding** (assets
that get better every use) vs **flowing** (instances moving through stages).

- **Always created (the spine):** `plugin/`, `routines/`, `scripts/`, `docs/`, `work/`, plus the root
  files `README.md`, `CLAUDE.md`, `AGENTS.md`, `PROGRESS.md`.
- **Created on demand:** everything else — `operations/`, `knowledge/`, `library/`, `artifacts/`, the
  `{pipeline}/` and `{entities}/` folders, and optional folders (`reference/ proof/ content/
  business/`). Don't pre-make them; add each when there's real material or an organ needs it.
- Keep every top-level **folder and file** name a single lowercase word (`operations`, not
  `operating-system`; `PROGRESS.md`, not `progress-log.md`). Skill folders under `plugin/skills/` are
  the exception — they follow the 4-word skill-naming convention (see `skill-authoring.md`).

```
{workspace}/
├── README.md                 # human entry point: the map + the compounding loop
├── CLAUDE.md                 # the brain (self-updating): filing rules, loops, naming, never-stale
├── AGENTS.md                 # symlink -> CLAUDE.md (same brain for any agent runner)
├── PROGRESS.md               # append-only log: date · what was done · why (1-2 sentences, human+agent)
├── .agents/
│   └── skills -> ../plugin/skills
│
│  # ===== ALWAYS created (the minimal spine) =====
├── plugin/                   # COMPOUNDING capabilities, packaged in place as an installable plugin
│   ├── .claude-plugin/
│   │   ├── plugin.json       #   Claude manifest (name = {OS}-os)
│   │   └── marketplace.json  #   marketplace manifest (lists this plugin, source ".")
│   ├── .codex-plugin/
│   │   └── plugin.json       #   Codex manifest (skills: ./skills/)
│   ├── skills/               #   one folder per skill, named {OS}-{area}-{verb}-{noun}
│   │   ├── {OS}-system-process-input/    #   auto-manage orchestrator (intake)
│   │   ├── {OS}-system-check-health/     #   read-only health check (doctor) — verification surface
│   │   ├── {OS}-system-fix-drift/        #   run doctor, then reconcile + de-stale (janitor)
│   │   ├── {OS}-system-capture-learning/ #   compound-learning capture (learn)
│   │   ├── {OS}-system-improve-machinery/#   improve the OS itself (reflect)
│   │   ├── {OS}-system-promote-skill/    #   promote proven work into a skill (skillify)
│   │   ├── {OS}-system-find-unknowns/    #   pre-work discovery (from finding-unknowns)
│   │   └── {OS}-{area}-{verb}-{noun}/    #   one per recurring domain task
│   └── README.md
├── routines/                 # runnable prompts for scheduled/remote runs (indexed by README.md)
│   ├── README.md             #   index: each routine + cadence + `armed: yes|no` (the doctor reads this)
│   ├── janitor.md reflect.md capture-learning.md    #   maintenance runs
│   └── {workflow}.md         #   one prompt per recurring domain workflow (e.g. weekly-brief)
├── scripts/                  # reusable executable scripts (e.g. scripts/doctor.py — the doctor fast path)
├── docs/                     # human-facing docs about how this OS works
├── work/                     # non-recurring / one-off work, grouped by project + dated
│   └── {project}/YYYY-MM-DD-…/
│
│  # ===== created ON DEMAND (real material, or when an organ first needs it) =====
├── operations/               #   health.md (doctor) · improvements.md (reflect) · .packaged-version · sync.md
├── knowledge/                #   settled answers: faqs/ insights/ decisions/ sops/  (learn creates it)
├── library/                  #   reusable instruments: templates, checklists, boilerplate
├── artifacts/                #   finalized recurring outputs (dashboard.html, reports) kept current
├── {pipeline}/               #   FLOWING staged work: _board.md + 01-…/ 02-…/ (numbered stages)
├── {entities}/               #   FLOWING core-unit records: _TEMPLATE/ + one folder each
└── reference/ proof/ content/ business/   #   only when the domain has real material
```

## library/ vs knowledge/ vs work/ vs artifacts/
- **library/** = blank **instruments you reuse** — templates, scripts, checklists, boilerplate. If
  you'd *use* it to produce something, it's library (a proposal template, a release checklist).
- **knowledge/** = **settled answers you read back** — faqs, insights, decisions, sops. If you'd
  *consult* it to decide or recall, it's knowledge (why we picked a vendor; how we close a deal).
- **work/** = **non-recurring output** — a one-off deliverable or scratch build, grouped by project
  (`work/{project}/YYYY-MM-DD-…/`), so the root never sprouts a `catalog-builder/`-style folder.
- **artifacts/** = **finalized recurring output you keep current** — the dashboard, a weekly report,
  a recurring export. Produced again and again, not once.
- Rule of thumb: a deliverable's reusable skeleton → `library/`; the lesson learned making it →
  `knowledge/`; a one-time build → `work/{project}/`; an output you regenerate on a cadence →
  `artifacts/`. If the *process* will repeat, don't leave it as a doc — skillify it into `plugin/`.

## The feedback organs (what makes the OS self-managing)
- **doctor** (`plugin/skills/{OS}-system-check-health`) — read-only verification surface; scores the
  workspace and writes a punch list to `operations/health.md`, backed by `scripts/doctor.py` (the fast
  mechanical path). "Consistent" = a clean doctor run, not a feeling.
- **janitor** (`{OS}-system-fix-drift`) — runs the doctor, then fixes what's safe. Gated on the doctor.
- **routines** (`routines/`) — the runnable prompts that let the loops run *unattended*: one markdown
  file per scheduled/remote workflow (janitor, reflect, learn, and domain runs), indexed by
  `routines/README.md` with each one's cadence + arm status. The scheduler executes these; the doctor
  reads that index for its "schedule armed" check.
- **reflect** (`plugin/skills/{OS}-system-improve-machinery`) — improves the *system* (skills, routing,
  checks, templates) into `operations/improvements.md`; the 50/50 budget.
- **resolver** — routing. Each skill's `description` routes it while the pack is small; graduate to an
  explicit `plugin/skills/RESOLVER.md` (trigger -> skill) once descriptions overlap. The doctor's
  reachability check flags any **dark** skill (built but unreachable).

## Domain mappings (core unit -> flowing folders)
| Domain | Pipeline (flowing) | Entities (flowing) | Compounding highlights |
|---|---|---|---|
| Consulting | leads -> qualifying -> discovery -> proposal -> negotiation -> won/lost | clients/ | proposals, pricing, proof |
| Product management | backlog -> discovery -> in-progress -> shipped | features/ or releases/ | PRD templates, specs, decision log |
| Record label | demos -> A&R -> signed -> production -> release -> promo | artists/ | release checklists, splits, assets |
| Research | questions -> lit-review -> experiment -> analysis -> writeup | studies/ | protocols, datasets, findings |
| Agency / creative | brief -> pitch -> production -> delivery | accounts/ | brand kits, asset library, case studies |
| Personal / founder | ideas -> exploring -> building -> launched | projects/ | playbooks, lessons, network |

## Rules
- **Top-level names are one lowercase word — folders AND files** — `operations` (not
  `operating-system`), `knowledge` (not `knowledge-base`), `PROGRESS.md` (not `progress-log.md`). When
  you rename a folder to the domain's language, keep it a single word (`clients/`, `releases/`). Skill
  folders inside `plugin/skills/` are the exception: they follow the 4-word `{OS}-{area}-{verb}-{noun}`
  convention (see `skill-authoring.md`). Hidden agent config dirs (`.agents/`) are compatibility
  adapters, not taxonomy.
- **Scaffold to the bone; grow on demand.** Create only the spine (`plugin/`, `routines/`, `scripts/`,
  `docs/`, `work/` + the root files). Do NOT pre-make `operations/`, `knowledge/`, `library/`,
  `artifacts/`, the pipeline/entity folders, or any optional folder — the agent (and each organ)
  creates a top-level folder the first time real material needs it. A wide row of empty top-level dirs
  is the smell to avoid. The agent is trusted to add a new one-word top-level folder when the domain
  genuinely calls for it, and to record that it did so in `PROGRESS.md` and the `CLAUDE.md` filing tree.
- **One-off work never earns a top-level folder.** Ad-hoc or task-specific work (building a catalog,
  a one-time analysis) goes in `work/{project}/YYYY-MM-DD-…/` — never a new root directory like
  `catalog-builder/`. A finalized output you *regenerate* (the dashboard, a recurring report) goes in
  `artifacts/`; a one-time output stays in `work/`.
- **If work will repeat or needs maintaining, skillify it.** After finishing a task, ask: *will this
  be done again, need upkeep, or prevent a failure from recurring?* If yes, stage a draft under
  `work/YYYY-MM-DD-skillify-{name}/`, verify it with the strongest domain-appropriate check, ask for
  approval, then move it into `plugin/skills/` and repackage instead of leaving a one-off folder
  behind.
- **Name plugins `{OS}-os`** (the OS slug is the owner's name for a personal OS, the domain for a
  domain OS). Use the same kebab name in `plugin/.claude-plugin/plugin.json`,
  `plugin/.claude-plugin/marketplace.json`, and `plugin/.codex-plugin/plugin.json`. The marketplace
  manifest lists this one plugin (`source: "."`) so the workspace is directly installable.
- **Scripts live in `scripts/`.** Reusable executable code (the generated `doctor.py`, any helper) goes
  in the top-level `scripts/`, not scattered in `operations/` or a skill folder.
- **Append to `PROGRESS.md` every session.** A one-word root file, append-only: `date · what was done ·
  why` in 1-2 sentences, pitched between technical and non-technical so humans and agents both read it.
- **The packaged plugin is a transient artifact, not taxonomy.** The `{OS}-os.plugin` zip is a
  release output delivered outside the workspace (via `/tmp`), never a top-level `outputs/` folder —
  `plugin/skills/` is the source of truth. After any in-place skill/manifest change, re-zip and stamp
  `operations/.packaged-version` so `{OS}-system-check-health`'s package-freshness check can tell the installable
  artifact apart from a stale one.
- **Expose skills once for Cursor/Codex.** Use `.agents/skills -> ../plugin/skills` as the shared
  project-skill adapter. Do not also create `.cursor/skills` unless the user explicitly wants a
  Cursor-only mirror, because duplicate discovery can surface the same skill twice.
- **Consistency is evidence-gated.** `{OS}-system-check-health` (read-only) is the verification surface — it
  scores the workspace into `operations/health.md`; the janitor and the build report are gated on it.
  Keep it report-only (a doctor that edits is a cage) and its checks behavioral contracts, not a wall
  of distrust validators.
- **Compound the system, not only its contents.** When friction recurs, `{OS}-system-improve-machinery` turns it
  into a skill / routing row / doctor check / template / rule in `operations/improvements.md` — spend
  ~half the effort on the machinery (50/50). Only on observed repetition, never generic advice.
- Numbered stage prefixes (`01-`, `02-`) for workflow sort order.
- Every entity folder keeps a current `README.md` dashboard (status, owner, value/stakes, next action).
- If an external system of record exists (CRM, issue tracker), it owns *state*; the filesystem owns
  *artifacts*. Document the mapping in `operations/sync.md`.
- Keep the root clean: source/reference material lives under `reference/`, not at the root.
