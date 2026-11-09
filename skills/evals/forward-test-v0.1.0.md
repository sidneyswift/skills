# Gateway validation — 2026-11-09

## Environment and boundaries

- Skills CLI `1.7.6`, Node `25.9.0`.
- Matt Pocock source checked at
  [`4ae2317`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d).
- Actual installs used a disposable Codex project and temporary CLI state.
  No global skills, live project instructions, plugins, or issue labels changed.
- Agent-runtime discovery was not exercised; file installation and CLI inventory
  were verified. No claim of runtime compatibility for every upstream skill.

## Executed checks

- Skill-creator frontmatter/name/scaffold validation passed.
- Skills CLI discovered the new `skills` gateway in this repository.
- Installed the gateway by name; its `SKILL.md` and UI metadata were preserved.
- Installed the complete upstream discoverable set: 38 skills, with supporting
  files such as the issue-tracker templates present and source provenance in the
  project lock. CLI inventory agreed with the installed set.
- Upstream contains 39 `SKILL.md` files at the checked revision; the CLI skipped
  `software-factory` for invalid YAML. The gateway requires reporting discovery
  warnings; it does not patch third-party skills or hide omissions.
- An initial test assertion incorrectly assumed local-source gateway installs
  were absent from the lock. Inspection showed a valid local-source entry;
  correcting the assertion made the provenance check pass. The install commands
  themselves succeeded on the first run.

## Independent behavioral pass

A fresh evaluator received the skill and four requests, without expected answers:

1. Fresh Claude Code, install everything: selected that agent, defaulted to
   global scope, inspected shared destinations, and did not use `--all`.
2. Codex project with edited `tdd` and an existing Matt plugin: preserved the
   edit, reused the plugin, and reported incomplete coverage rather than adding
   duplicates. The checked plugin exposes 27 skills versus 38 CLI-discoverable
   skills; installed coverage still needs local verification.
3. Add a single-skill URL with only an installed gateway accessible: targeted a
   canonical catalog patch, preserved single-skill selection, and did not claim
   publication or installation. The hypothetical URL was not fetched.
4. Explain the collection: answered read-only; no installation or catalog edit.

No blocking instruction defect was found in these scenarios. The final gateway
also refreshes its canonical catalog when invoked from an installed copy, while
honoring explicit branch/revision/local-development requests and disclosing
cached-catalog fallback. That freshness clause was reviewed directly, not
exercised against a future catalog change.

## Addy Osmani catalog addition — 2026-11-09

- Checked upstream README, universal/host setup guidance, plugin manifests, and
  shared-reference layout at
  [`301b02b`](https://github.com/addyosmani/agent-skills/tree/301b02b12bff98e4688e6984af6556802322bbde).
- Read-only Skills CLI discovery returned 25 skills without a skipped-skill
  warning. Their parsed names do not collide with the first collection's
  previously verified names.
- Added whole-collection selection and source-specific guidance for root-level
  shared checklists, plugin versus file-install capabilities, and avoiding
  contributor instructions or duplicate always-on routers in consumer projects.
- Revalidated the gateway and rebuilt the unreleased v0.1.0 ZIP. This addition
  was not installed into a live host; no native plugin/runtime behavior tested.

## Five-source expansion — 2026-11-09

Read pinned upstream installation documentation, manifests, and resource layouts:

| Source | Checked revision | Exported source inventory / route |
| --- | --- | --- |
| Cloudflare security audit | [`c1c8a8c`](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) | One skill; complete guides/schema/validator bundle |
| Google EGM | [`5382b17`](https://github.com/google/elephant-goldfish-model/tree/5382b17619be07811a14b2146c7672620b34a791) | Seven root skills; native full-plugin route with agents and document standards |
| pstack | [`74dd229`](https://github.com/poteto/plugins/tree/74dd2291e8e37b12fd6dc49b2acbd655c6bdaf12/pstack) | 34 skills in the requested subtree; native Cursor integration or scoped files with limitations |
| gstack | [`10fc9b1`](https://github.com/garrytan/gstack/tree/10fc9b1eab44bc5bb5422bcb3f2f68d3dd381659) | Whole checkout and explicit host setup; not raw folder copying |
| Compound Engineering | [`8e5d1c8`](https://github.com/EveryInc/compound-engineering-plugin/tree/8e5d1c87613f484a5bdfeacedf86a7aaaccfa264) | 37 root skills; native plugin or supported host adapter |

- Parsed frontmatter for the four static skill inventories. Remote CLI discovery
  of the exact pstack tree URL returned its 34 skills without sibling plugins.
- Cross-source raw-name checks exposed pstack/Matt `tdd` and gstack/Matt `retro`.
  Actual collisions depend on host-rendered names and namespaces; the gateway
  inventories these before writing and never chooses by catalog order.
- Documented pstack's marketplace/source mismatch, missing native-agent and
  external-tool dependencies; EGM full-plugin requirements; gstack host/setup
  and multi-registration update scope; CE root-layout and marketplace refresh.
- An independent evaluator checked fresh Codex installation, unsupported EGM on
  OpenClaw, an edited/existing Matt `tdd`, single-host gstack updates, and
  catalog-only additions. No blocking or material issue found in the five new
  routes. Same-name/unsupported items must remain explicit incomplete outcomes.
- Reviewed the Addy reference fallback to make clear that retaining a clone
  does not itself repair copied relative links; the lookup must be recorded and
  tested or the resource reported unavailable.
- Revalidated frontmatter and packaging. No plugin, setup script, audit, design
  workflow, or live installation was run for these additions. Source inspection
  and discovery are not runtime certification.
