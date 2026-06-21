# Universal Workspace-OS Anatomy

Every workspace OS, regardless of domain, is built from the same skeleton. Rename folders to the
domain's language; drop what doesn't apply; add domain-specific stores. The split that matters most:
**compounding** (assets that get better every use) vs **flowing** (instances moving through stages).

```
{workspace}/
├── README.md                 # human entry point: the map + the compounding loop
├── CLAUDE.md                 # the brain: filing rules, auto-manage loop, never-stale contract
├── AGENTS.md                 # symlink -> CLAUDE.md (same brain for any agent runner)
│
├── reference/                # CANON, read-mostly: source docs, playbooks, specs, brand guides
│   └── principles.md         # distilled 1-page cheat sheet of how this domain works
│
├── library/                  # COMPOUNDING: reusable instruments (templates, scripts, checklists)
├── knowledge-base/           # COMPOUNDING: never-answer-twice
│   ├── faqs/                 #   canonical answers
│   ├── insights/             #   mined explanations / lessons
│   ├── decisions/            #   decision log (what we chose + why) — fuels compound learning
│   └── sops/                 #   repeatable procedures
│
├── {pipeline}/               # FLOWING: staged work (deals / tickets / releases / submissions)
│   ├── _board.md             #   snapshot of the funnel
│   └── 01-…/ 02-…/ …         #   numbered stages for sort order
├── {entities}/               # FLOWING: the core unit's records (clients / artists / features…)
│   └── _TEMPLATE/            #   copyable lifecycle skeleton + dashboard README
│
├── proof/                    # COMPOUNDING: outcomes/credibility (case studies, results, testimonials)
├── content/                  # OPTIONAL flywheel: raw -> ideas -> drafts -> published
├── business-ops/             # back office: legal, finance, metrics (as relevant)
│
├── skills/                   # COMPOUNDING capabilities: one folder per skill (SKILL.md) -> plugin
│   ├── _packaging/           #   how to bundle + install
│   ├── {domain}-intake/      #   the auto-manage orchestrator (ingest anything end to end)
│   ├── {domain}-janitor/     #   never-stale reconcile (scheduled)
│   └── {domain}-learn/       #   compound-learning capture
│
└── operating-system/         # META: keep it compounding
    ├── dashboard.html        #   live snapshot (HTML, not md)
    ├── rituals.md            #   cadences (daily/weekly/periodic)
    └── sync.md               #   how the filesystem maps to any external system of record (CRM, etc.)
```

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
- Numbered stage prefixes (`01-`, `02-`) for workflow sort order.
- Every entity folder keeps a current `README.md` dashboard (status, owner, value/stakes, next action).
- If an external system of record exists (CRM, issue tracker), it owns *state*; the filesystem owns
  *artifacts*. Document the mapping in `operating-system/sync.md`.
- Keep the root clean: source/reference material lives under `reference/`, not at the root.
