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

| ID | Source | Selection | Why it's here |
| --- | --- | --- | --- |
| matt-pocock | [mattpocock/skills](https://github.com/mattpocock/skills) | All skills (`*`) | Matt Pocock's engineering and productivity workflows. |

`All` means the skills exposed by that source's current installer discovery,
including new additions on a later install/update. It is not a frozen list or a
claim that every workflow supports every agent. A future entry may instead name
specific skills or a repository subdirectory; respect that narrower selection.

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

## Install or update the collection

1. **Resolve the target.** Use the agent and scope the user named. Otherwise use
   the current agent and a user-level/global install for this personal
   collection. State that default before writing. Infer from the actual host,
   not just a model name; if the host cannot be established, ask which agent.
   For project installs, use the requested project root, not this source repo.
2. **Check tooling.** The portable route is the
   [Skills CLI](https://github.com/vercel-labs/skills). Check its current
   requirements and `npx --yes skills@latest --help` (Node.js, npm/npx, and Git
   are needed). If unavailable, explain the specific missing prerequisite;
   do not silently install a runtime or switch to another agent.
3. **Discover and compare.** List each catalog source's selected skills, read
   its installation notes, and inventory the target agent's installed skills,
   plugins, and installer lock records. Inspect both the agent destination and
   any shared canonical skill directory/symlink target. Same-name skills from
   different sources, untracked installs, and local modifications are conflicts,
   not permission to overwrite. Check for collisions between catalog sources,
   too. Keep discovery warnings: malformed or skipped upstream skills must be
   reported, not silently counted as installed. Install the nonconflicting
   remainder and report blocked names.
4. **Install the selected set.** For a clean target, use the commands below for
   each catalog entry. On a repeat install, skip intact matching installations
   and explicitly select only missing skills. On an update request, refresh
   unmodified skills from the catalog's sources and pick up new selected skills;
   preserve local edits. Use explicit `--skill` names when excluding conflicts.
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
catalog entry; repeat for **every** entry using its source and selection.

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

If the host is unsupported or its configured skill path differs from the CLI's
destination, use its documented installation mechanism. A manual fallback must
copy each complete skill folder, including references/scripts/assets, preserve
upstream attribution, and record the source URL and resolved revision. Do not
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
