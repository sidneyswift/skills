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
