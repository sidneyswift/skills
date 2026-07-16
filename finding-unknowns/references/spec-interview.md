# Spec interview

Interview the user about everything still ambiguous in a feature, one question at a time, ordered by how much each answer would change the architecture. Use when a spec is loose, when the user says "interview me", or before finalizing any plan whose open questions would be expensive to reverse.

Example trigger prompt:

> Interview me one question at a time about anything still ambiguous in the annotation-export feature. Prioritize questions where my answer would change the architecture.

## Ordering: blast radius first

Sort questions by how much of the design each answer invalidates:

1. **Architecture-changing** first: sync vs async, job queue or not, new datastore or not ("this decides whether we need a job queue, a notification path, and an artifacts bucket, or none of those; everything else layers on top")
2. **Scope-defining** next: per-item vs bulk, which user populations
3. **Format and data-shape** questions after that
4. **Permission and policy** questions
5. **Naming and convention** questions last

Never ask a question whose answer does not change what gets built.

## Question format

Ask one question at a time. Each question carries:

- **Context**: why this matters and what the answer decides, in one or two lines
- **3 or 4 concrete options**, each with its trade-off and effort implication stated honestly ("simple, but a 400-comment review will blow past the 30s gateway timeout"; "zero new backend, but caps us at formats the browser can assemble")
- Room for a custom answer

Wait for the answer before asking the next question. Adjust later questions based on earlier answers; some become moot, some become load-bearing.

## Ending the interview

After the last question, produce:

1. **A decisions table**: every question, the chosen answer, and its consequence
2. **A ready-to-paste implementation prompt** with all decisions folded in as constraints

## Quality bar

- One question per turn, strictly. The value is focus.
- Options must be real forks with different costs, not one obvious answer padded with strawmen.
- Cap at roughly 7 questions. If more remain, the feature should be split.
- Flag the load-bearing question when one answer would reorder the rest ("the timecode question becomes load-bearing if you pick the editor-focused format").
