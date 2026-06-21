# Packaging the skills/ folder into an installable plugin

## Plugin layout
```
{name}-os/
├── .claude-plugin/
│   └── plugin.json        # required; minimal field is name
├── skills/
│   └── {skill}/SKILL.md   # one folder per skill
└── README.md
```

## plugin.json (minimal)
```json
{
  "name": "{name}-os",
  "version": "0.1.0",
  "description": "Operating system for {domain} — N skills covering …",
  "author": { "name": "{author}" },
  "keywords": ["{domain}", "operating-system"]
}
```
`name` must be kebab-case. Bump the version on each rebuild.

## Validate BEFORE zipping (these are the failures that actually happen)
1. `.claude-plugin/plugin.json` is valid JSON and has a kebab-case `name`.
2. Every `skills/*/` folder contains a `SKILL.md` with valid frontmatter (`name` + `description`).
3. **No `<` or `>` in any skill `description`** (the loader rejects XML-looking tags). Grep for them.
4. No stray non-skill folders inside `skills/` (everything there needs a SKILL.md).

A quick validator (run in the sandbox):
```bash
python3 - <<'PY'
import json,glob,re,sys
plg="/tmp/{name}-os"
d=json.load(open(f"{plg}/.claude-plugin/plugin.json"))
assert re.fullmatch(r"[a-z0-9-]+", d["name"]), "name not kebab-case"
bad=[]
for sk in glob.glob(f"{plg}/skills/*/SKILL.md"):
    fm=re.match(r"^---\n(.*?)\n---", open(sk).read(), re.S).group(1)
    desc=re.search(r"^description:\s*(.+)$", fm, re.M).group(1)
    if "<" in desc or ">" in desc: bad.append(sk)
print("FAIL" if bad else "OK", *bad)
sys.exit(1 if bad else 0)
PY
```

## Package + deliver
Always zip in `/tmp` first, then copy to the outputs folder (writing the zip directly to outputs can
fail on permissions):
```bash
cd /tmp/{name}-os && zip -rq /tmp/{name}-os.plugin . -x "*.DS_Store"
cp /tmp/{name}-os.plugin {OUTPUTS}/{name}-os.plugin
```
Then present the `.plugin` file so the user can install it with the in-chat button. Once installed,
the skills trigger non-deterministically by description.

## AGENTS.md
In the *target workspace* (not inside the plugin), symlink so any agent runner finds the same brain:
```bash
cd {workspace} && ln -s CLAUDE.md AGENTS.md
```
Don't rely on symlinks surviving inside a zipped plugin — create the symlink at workspace build time.
