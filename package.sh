#!/usr/bin/env bash
#
# package.sh — build a versioned, distributable zip for every skill in the repo.
#
# A "skill" is any top-level folder that contains a SKILL.md. For each one this
# builds packages/{skill}-v{version}.zip, with the version read from that skill's own
# SKILL.md frontmatter, so a package filename can never drift from its source.
# Each skill's previous package is removed first (with a precise pattern, so
# similarly-named skills like "workspace" and "workspace-os" never clobber one
# another), leaving exactly one matching zip per skill. Adding a new skill needs
# no edits here: drop in {new-skill}/SKILL.md and re-run.
#
# Usage: ./package.sh
set -euo pipefail

# Operate from the repo root (this script's own directory) regardless of caller.
cd "$(dirname "$0")"

# Built packages live in one place, not scattered at the repo root.
PKG_DIR="packages"
mkdir -p "$PKG_DIR"

# Echo the `version` value from a SKILL.md's YAML frontmatter (the block between
# the first two `---` lines). Prints nothing when absent.
read_version() {
  awk '
    /^---[[:space:]]*$/ { fence++; next }
    fence == 1 && $1 == "version:" { gsub(/"/, "", $2); print $2; exit }
  ' "$1"
}

built=0
failed=0
built_zips=""

# Discover skills: every top-level dir with a SKILL.md. The */ glob ignores
# hidden dirs (.git, .agents, .claude) — none of which are skills.
for skill_md in */SKILL.md; do
  [ -e "$skill_md" ] || continue        # nothing matched: skip the literal glob
  skill="${skill_md%/SKILL.md}"

  version="$(read_version "$skill_md")"
  if [ -z "$version" ]; then
    echo "package.sh: $skill_md has no 'version:' in its frontmatter — skipping" >&2
    failed=$((failed + 1))
    continue
  fi

  zip_name="${skill}-v${version}.zip"

  # Remove only THIS skill's old package(s); the precise "{skill}-v" pattern
  # can't match a different skill that merely shares a name prefix.
  rm -f "$PKG_DIR/${skill}.zip" "$PKG_DIR/${skill}-v"*.zip

  # Zip the shippable files only — exclude dev-only evals and junk caches.
  zip -rq "$PKG_DIR/$zip_name" "$skill" \
    -x "${skill}/evals/*" \
    -x "*/__pycache__/*" \
    -x "*.DS_Store"

  echo "Built $zip_name"
  built=$((built + 1))
  built_zips="${built_zips}${zip_name}
"
done

# Flag any root .zip that no longer matches a current skill+version — a leftover
# from a renamed/removed skill, which is exactly the silent drift this script
# exists to prevent. Reported, not deleted, so the choice stays yours.
for z in "$PKG_DIR"/*.zip; do
  [ -e "$z" ] || continue
  if ! printf '%s' "$built_zips" | grep -qxF "$(basename "$z")"; then
    echo "package.sh: note: '$z' matches no current skill — consider deleting it" >&2
  fi
done

echo "Packaged ${built} skill(s)."
[ "$failed" -eq 0 ] || { echo "${failed} skill(s) skipped (missing version)." >&2; exit 1; }
