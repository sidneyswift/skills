# Use script — consulting firm

The user agent receives the workspace path and the tasks below. It is **not** told about
`workspace-os`, "never-stale", or the doctor by name. Before it runs, the harness drops
`use-input/acme-followup.md` into the workspace (an `inbox/` if one exists, else the root).

Tasks, in order:

1. "New file in the workspace: `acme-followup.md`. It's an update on the Acme deal — process it."

2. "Heads up — we lost the Globex deal. They went with a cheaper competitor. Update the pipeline, and
   make sure we capture *why* so we don't keep losing on price."

3. "Give the whole workspace an audit — is anything inconsistent or stale?"

4. "Reconcile it — fix whatever's safe to fix."

5. (optional) "We rebuild proposals from scratch every time and it's painful. Anything here worth
   turning into something repeatable?"
