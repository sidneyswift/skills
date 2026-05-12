# Module 05: Projects & Memory

Teaches that AI works best with persistent context — and that the workspace they already have IS that persistent context.

## When This Fires

- User starts multiple tasks without referencing prior work
- User asks "why doesn't it remember what I told it last time?"
- User repeats the same context at the start of every session
- User has a complex task that spans multiple sessions

## The Core Insight

By this point, the user already has a workspace with CLAUDE.md and PROGRESS.md. They may not realize those files are what makes their AI sessions coherent. This module makes that explicit and teaches them to maintain their own context.

## The Approach

### 1. Show the Before/After

Open a session WITHOUT the workspace context. Ask a question about their work. The AI gives a generic answer.

Now open a session WITH their workspace loaded. Same question. The AI gives a contextual, personalized answer because it read CLAUDE.md.

"That's the difference. The file you already have is doing this for you every time you start a session here."

### 2. Teach Them to Edit CLAUDE.md

This is the key skill transfer. Walk them through:

- "You told me last week you prefer bullet points over paragraphs. Let's add that to your standing instructions."
- "You mentioned your team uses a specific framework. Let's add that to the context so every AI session knows about it."
- "Open CLAUDE.md. See this section? That's what the AI reads first. Anything you add here, it knows next time."

The moment they edit CLAUDE.md themselves, they understand how context works. It's not magic — it's a file they control.

### 3. Introduce the Project Pattern

For multi-session work:

```
current/
  q3-rebrand/
    CLAUDE.md         # what this project is, goals, constraints
    notes.md          # running notes
    drafts/           # work in progress
```

Each project gets its own context file. When they open that folder, the AI knows the project. When they switch to a different folder, the AI knows THAT project. No re-explaining.

### 4. Knowledge Folder

Show them the knowledge/ folder in their workspace:

- `raw/` — things the AI has observed about how they work
- `synthesized/` — patterns the AI has noticed

"Over time, I learn how you work and write it here. You can read it, edit it, delete anything you don't want me to remember."

This is the transparency piece. AI memory should never be opaque.

## Completion Criteria

- [x] User has edited CLAUDE.md themselves (not just watched)
- [x] User understands that context files are what makes AI sessions persistent
- [x] User has created or used a project folder for a real multi-session task

## Don't

- Don't explain tokens, context windows, or how LLMs work. They don't need to know. "The AI reads this file at the start of every session" is sufficient.
- Don't make this feel like system administration. They're customizing their assistant, not configuring software.
- Don't overload the knowledge/ folder with AI observations early. Let it grow naturally.
