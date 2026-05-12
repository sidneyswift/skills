# Module 06: Building Skills

Teaches that repeatable workflows can become reusable skills — and helps them build their first one.

## When This Fires

- User has a workflow they do repeatedly (weekly report, onboarding email, content review)
- User asks "can I automate this?" or "can I save this prompt?"
- User has completed at least Module 01 and demonstrates comfort with prompting
- User is doing the same task for the third time and you notice the pattern

## The Core Insight

A skill is just a set of instructions in a file that the AI reads before doing a task. They've been using one this whole time (CLAUDE.md). A skill is the same concept — but for a specific workflow.

## The Approach

### 1. Identify the Pattern

Don't tell them they should build a skill. Wait until they've done something repeatable, then ask:

- "You've done this three times now. Want me to save a recipe so we can do it faster next time?"
- "This looks like a process. Want to capture it so you don't have to re-explain it?"

The word "skill" can come later. Start with "recipe" or "workflow" or "template."

### 2. Extract the Workflow Together

Walk through what they did:

1. What inputs did you provide?
2. What did you want the AI to do with them?
3. What did the output look like?
4. What did you correct or iterate on?

Turn that into a structured prompt file in `workflows/`:

```markdown
# Weekly Client Update

## What this does
Generates a client-ready project update from my raw notes.

## Inputs needed
- Raw notes from the week (paste or point to file)
- Client name
- Key milestones/dates

## Instructions
1. Read the raw notes and extract: completed items, in-progress items, blockers, next steps.
2. Write a professional but warm email update. Max 300 words.
3. Tone: confident but honest. If there are blockers, name them but include the plan.
4. End with a clear "next steps" section with dates.

## Example output
[Include a real example from their previous iteration]
```

### 3. Run It on New Data

Immediately test the saved workflow on new inputs. They should see: same quality, less effort, no re-explaining.

### 4. The Graduation

Once they've built 2-3 workflows, explain the bigger picture:

"These are skills. Every one you build makes the AI more useful for exactly your work. Some people share these with their teams. Some people publish them. But the core idea is the same — you're teaching the AI how you want things done."

## Completion Criteria

- [x] User has at least one saved workflow in their `workflows/` folder
- [x] User has used a saved workflow on new data (not just created one)
- [x] User understands that skills are just structured instructions, not code

## What Goes in PROGRESS.md

```markdown
### [Date] — Module 06: Building Skills ✓
- First skill: "Weekly Client Update" — saved to workflows/weekly-client-update.md
- Trigger: noticed they'd done this 3 weeks in a row with manual re-prompting
- Key insight: user realized the example output section was what made it consistent
- Next: has mentioned wanting a similar recipe for competitor analysis
```
