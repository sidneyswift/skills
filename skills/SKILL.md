---
name: skills
description: >-
  Install, list, update, or extend Sidney's curated collection of agent skills.
  Use when asked to install all of Sidney's favorite skills, bootstrap an agent
  from this collection, or add a skill repository to the collection. This is an
  installation gateway, not a skill-authoring or general skill-search workflow.
metadata:
  version: "0.1.0"
---

# Skills — Sidney's collection

One entry point for installing the skills Sidney collects. The catalog below is
the source of truth. Install from the original repositories; do not vendor their
contents here or substitute your own recommendations.

Reading this file alone does not authorize an install. When the user says
"install my skills" or "install everything in this collection", install every
catalog entry, not just this gateway. A request to list or explain is read-only;
a request to add a source changes the catalog, not the user's installed skills.

When invoked from an installed copy, fetch the current
[canonical gateway](https://github.com/sidneyswift/skills/blob/main/skills/SKILL.md)
before an install/update so later catalog additions are included. Honor an
explicitly requested branch, revision, or local development copy instead. If
refresh is unavailable, disclose that the catalog is cached; never claim it is
the latest. Fetching the current catalog does not require installing other skills
from `sidneyswift/skills`.

## Collection

| ID | Source | Selection | Install route | Why it's here |
| --- | --- | --- | --- | --- |
| matt-pocock | [mattpocock/skills](https://github.com/mattpocock/skills) | All skills (`*`) | Skills CLI; reuse existing plugin | Engineering and productivity workflows. |
| addy-osmani | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | All skills (`*`) | Native plugin or Skills CLI with shared references | Engineering lifecycle from specs to shipping. |
| cloudflare-security-audit | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | All skills (`*`; currently `security-audit`) | Skills CLI | Evidence-led security auditing. |
| elephant-goldfish | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Complete EGM plugin | Native plugin; not skill-only copying | Context-rich design with fresh-context review. |
| pstack | [poteto/plugins → pstack](https://github.com/poteto/plugins/tree/main/pstack) | Only the `pstack/` plugin and its skills | Cursor plugin or subtree-scoped skill files | Rigorous engineering workflows and principles. |
| gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | Full suite for the selected host | Whole checkout + host-specific setup | Engineering roles, review, QA, and release workflows. |
| compound-engineering | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | Complete Compound Engineering plugin | Native plugin / upstream host adapter | Plan, build, review, and capture reusable learning. |

`All` means the set exported by the stated installer or plugin, including new
additions on a later install/update. It is not every `SKILL.md` in tests,
contributor tooling, or duplicate distributions. Follow the route in each row:
**do not run a generic Skills CLI loop over native-plugin or setup entries.**
Respect subtree selections and report host-specific limitations; the catalog is
not a claim that every workflow supports every agent.

### Matt Pocock notes

- Use the upstream repository's current README for prerequisites and changes.
  Some discoverable skills live in `in-progress` or `misc`; a whole-repository
  install can include these, not just the skills highlighted in the README.
- Do not install both the native plugin and file-based skills for the same
  collection in the same agent. Reuse an existing plugin installation instead
  of adding duplicate files; verify its coverage against the selected skills
  and report any gap rather than silently calling a subset "everything".
- Upstream recommends `setup-matt-pocock-skills` once per working repository
  before using its engineering workflows. Report that next step after install.
  Do not run it merely to install files: it configures project instructions,
  issue tracking, and labels, which is a separate task.

### Addy Osmani notes

- Follow the upstream [Quick Start](https://github.com/addyosmani/agent-skills#quick-start)
  and the linked setup guide for the target host. The portable Skills CLI
  installs the skill folders; native integrations can also carry pack-level
  resources. Use one installation method per host, not plugin plus duplicate
  file installs.
- Shared checklists in the repository's root `references/` directory are outside
  individual skill folders and are not included by a per-skill CLI install.
  Prefer a whole-repository integration when available; otherwise retain a
  source checkout for shared references and record its location/revision for
  later lookup. A retained clone alone does not repair copied relative links:
  record and test the lookup path from the installed skill, or report the
  checklists as unavailable. Verify reference availability separately from installed skill
  names, and report any missing supplementary resources.
- Install all selected skills, but load them on demand. Do not copy the source
  repo's contributor `AGENTS.md` or `CLAUDE.md` into the user's project, preload
  its meta-router on a host with native routing, or claim that file-only installs
  include native slash commands, hooks, or agent personas.

### Cloudflare security audit notes

- Use the Skills CLI source `cloudflare/security-audit-skill`. Keep the whole
  `skills/security-audit/` folder, including phase guides, report schema, and
  both `.cjs` validators; copying only the entrypoint is incomplete.
- Check the upstream [requirements](https://github.com/cloudflare/security-audit-skill#requirements):
  Node.js, parallel subagents, and an OS-enforced sandbox for executing target
  code. Distinguish installed files from available audit capabilities. Installing
  the skill does not start a security audit or run target code.

### Elephant-Goldfish Model notes

- Install the **complete plugin**, preserving `skills/`, `agents/`, and
  `resources/document_standards/`. A Skills CLI copy of `skills/` alone is not a
  working EGM installation. Follow the current [host guide](https://github.com/google/elephant-goldfish-model/blob/main/docs/harnesses.md).
- Claude Code: `claude plugin marketplace add google/elephant-goldfish-model`,
  then `claude plugin install egm@egm`.
  Codex CLI: `codex plugin marketplace add google/elephant-goldfish-model`,
  then `codex plugin add egm@egm`. Use the host guide for other environments.
- Restart/reload as directed and check plugin discovery plus the shared runtime
  resources. Goldfish reviews require actual fresh-context subagents; report
  their absence instead of simulating independent review in the same context.
  If no supported full-plugin route exists for the target host, report this
  entry as blocked and continue the other entries.

### pstack notes

- The requested source is **`poteto/plugins/tree/main/pstack`**, not the whole
  `poteto/plugins` marketplace. For portable skill files, use that exact URL
  as the Skills CLI source and select `'*'`; verify discovery stays in `pstack/`.
- Upstream's native Cursor install is `/add-plugin pstack`. Verify its source
  before using it: the checked-in manifest advertises `cursor/plugins`, whereas
  this catalog selects `poteto/plugins`. Do not silently replace the requested
  source with a different repository; use the requested subtree or report the
  source mismatch. A file-only install does not register `poteto-agent`.
- The `tdd` name overlaps Matt Pocock's collection. Use a host-supported plugin
  namespace when available; otherwise preserve the existing choice and report
  the conflict. Do not simply rename a folder: internal skill references must
  still resolve. Inspect other cross-source names at install time too.
- Some workflows reference Cursor built-ins and the separate `cursor-team-kit`
  plugin. Report those dependencies, but do not add that unlisted plugin or run
  `/automate-me` or `/setup-pstack` as part of a catalog install.

### gstack notes

- Read upstream [installation](https://github.com/garrytan/gstack/blob/main/docs/install.md)
  and [host support](https://github.com/garrytan/gstack/blob/main/docs/hosts.md).
  Keep a complete checkout; skills depend on shared binaries and generated host
  adapters. A generic skill-folder copy is not the installation method.
- Check the current Bun/Git/toolchain requirements. From the retained checkout,
  run `./setup --host <host>` for the **one requested host**, then verify with
  `./setup --status` and that host's discovery. The setup identifiers differ
  from Skills CLI identifiers: for example, `claude` rather than `claude-code`.
  Do not use `--host auto`, and do not assume bare `./setup` targets this host.
- Respect an existing checkout's edits and registered destinations. Report
  unavailable tools, experimental host support, and router-only/advisory
  capabilities accurately. Team mode, project commits, extra integrations, and
  optional conversation hooks are separate choices, not defaults for this
  personal collection install. Report setup's changes to the selected host.
- Scope updates too: the upstream `/gstack-upgrade` workflow can refresh every
  registered host. Inspect its current behavior before using it for a request
  targeting only one host; do not silently expand the update scope.

### Compound Engineering notes

- Use the current [host install guide](https://github.com/EveryInc/compound-engineering-plugin#install).
  The plugin source is now the **repository root**, not the historical
  `plugins/compound-engineering` directory. Keep the complete skills and their
  local reviewer/research assets; do not flatten away supporting files.
- Claude Code chat: `/plugin marketplace add EveryInc/compound-engineering-plugin`,
  then `/plugin install compound-engineering`.
  Codex CLI: `codex plugin marketplace add EveryInc/compound-engineering-plugin`,
  then `codex plugin add compound-engineering@compound-engineering-plugin`.
  Use the linked guide's native adapter for other hosts.
- On updates, [refresh the marketplace before updating/reinstalling the plugin](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/install/upgrading.md).
  Keep all steps in the same selected host profile. Do not run all-target legacy
  cleanup as a side effect of installing this collection.
- Mention `/ce-setup` as a subsequent per-project step; do not run it, `/lfg`, or
  other workflows just to install the plugin. They perform project work.

## Install or update the collection

1. **Resolve the target.** Use the agent and scope the user named. Otherwise use
   the current agent and a user-level/global install for this personal
   collection. State that default before writing. Infer from the actual host,
   not just a model name; if the host cannot be established, ask which agent.
   For project installs, use the requested project root, not this source repo.
2. **Choose the entry's route and check tooling.** For file-based entries, use the
   [Skills CLI](https://github.com/vercel-labs/skills). Check its current
   requirements and `npx --yes skills@latest --help` (Node.js, npm/npx, and Git
   are needed). For native plugins and gstack, use their host commands and
   prerequisites instead; the Skills CLI is not required for those routes.
   If unavailable, explain the specific missing prerequisite;
   do not silently install a runtime or switch to another agent.
3. **Discover and compare.** List each catalog source's selected skills, read
   its installation notes, and inventory the target agent's installed skills,
   plugins, and installer lock records. Inspect both the agent destination and
   any shared canonical skill directory/symlink target. Same-name skills from
   different sources, untracked installs, and local modifications are conflicts,
   not permission to overwrite. Check all selected sources before writing;
   compare effective host-visible names, including plugin namespaces. For two
   new sources with an unresolved collision, defer those names rather than
   choosing by catalog order. Keep discovery warnings: malformed or skipped
   upstream skills must be reported, not silently counted as installed. Install
   the nonconflicting remainder and report blocked names.
4. **Install the selected set.** For a clean target, follow each entry's route
   and source-specific notes. The portable commands below apply only to
   file-based entries, not to every catalog row.
   For file installs, skip intact matching installations on a repeat run and
   explicitly select only missing skills. For native plugins, use the plugin's
   install/update unit and verify its complete exported set. On an update
   request, refresh unmodified skills from the catalog's sources and pick up
   new selected skills; preserve local edits. Use explicit `--skill` names when
   excluding conflicts.
   Never use an unscoped `skills update` that also changes unrelated collections.
5. **Verify.** Compare the expected names with the installed set, resolve links,
   and check that every installed folder has `SKILL.md` and its supporting
   files. Preserve the CLI's provenance/lock records. Check the host's skill
   discovery if available; otherwise say file installation is verified but
   runtime discovery is unverified and may need a new session. Report failures
   per source and continue independent entries; do not claim full completion
   when anything is missing or blocked.

### Portable commands

Set `target_agent` to the host's CLI identifier, such as `claude-code`, `codex`,
`cursor`, or `openclaw`. Consult the CLI's
[supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
for other hosts and actual install paths. These commands illustrate the first
catalog entry. Repeat for file-based entries using their source and selection;
complete native-plugin/setup entries through their own routes above.

```sh
# Read-only discovery; do not combine --list with --json.
npx --yes skills@latest add mattpocock/skills --list
npx --yes skills@latest list --global --agent "$target_agent"

# Fresh user-level install, after checking existing files and plugins.
npx --yes skills@latest add mattpocock/skills --skill '*' --agent "$target_agent" --global --yes

# Verify the selected agent and scope.
npx --yes skills@latest list --global --agent "$target_agent"
```

For a project install, omit `--global` from both install and inventory commands.
`npx --yes` accepts fetching the CLI; the final `--yes` accepts its install
prompts. Use them only within the user's requested install/update scope.
Quote `'*'` to prevent shell expansion. **Do not use `--all`: it selects all
agents as well as all skills.** Shared-directory hosts can still see the same
files; an agent selector is not a guarantee of filesystem isolation.

For entries that permit file-based installs, if the host is unsupported by the
CLI or its configured skill path differs, use its documented installation
mechanism. Do not downgrade a full-plugin requirement to a skill-only fallback.
A manual fallback must copy each complete skill folder, including
references/scripts/assets, preserve upstream attribution, and record the source
URL and resolved revision. Do not
copy only `SKILL.md`, overwrite existing folders, or claim discovery without
checking the host.

## Add another find

When Sidney supplies a new source for this collection:

1. Open the supplied URL and verify the repository, installable skill paths,
   skill names, and upstream installation instructions.
2. Add one row to **Collection**, with a stable ID, canonical source, selection,
   and a short reason. A whole-repository link defaults to all its skills;
   a link to a particular skill selects only that skill. Do not expand the
   collection to unrelated repositories or recursively follow upstream lists.
3. Deduplicate existing entries. Add source-specific notes only when they
   affect installation, setup, compatibility, or updates. Do not maintain a
   second, stale copy of an upstream skill catalog.
4. Edit the repository-owned source at `sidneyswift/skills`, path
   `skills/SKILL.md`, following that repo's contribution/review workflow. An
   installed copy is not the canonical catalog. If only the installed copy is
   accessible, prepare the exact patch and report that it is not published.

Adding a find does not install it, run its workflows, or authorize merging or
publishing unrelated changes. Never evaluate a catalog URL or name as shell
code; pass it as a quoted argument.

## Completion report

Keep it short: target agent and scope, sources processed, installed/updated/
already-present counts, conflicts or failures, and any reload or project-setup
step. For a catalog edit, link the changed source and give its publication state.
