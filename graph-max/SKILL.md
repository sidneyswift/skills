---
name: graph-max
description: >-
  Turn any hand-drawn workflow graph into a working multi-agent script.
  Draw the graph in any tool (whiteboard, paper, Excalidraw, napkin),
  photograph or screenshot it, send it to a coding agent with a single
  prompt, and get a running orchestration script back. The skill teaches
  graph literacy — how to draw nodes, edges, fan-outs, feedback loops,
  and decision gates so the coding agent can implement them faithfully.
  Use when someone has a workflow in their head but no code, wants to
  orchestrate multiple agents, or asks "how do I wire these steps
  together?"
metadata:
  author: Sidney Swift
  version: "0.1.0"
  source: "@nickcmorrow — 'How to graph-max with Codex and 5.6 Sol'"
---

# Graph-Max

## Overview

Most workflows live in someone's head as a vague sequence. They stay
there because turning them into code feels like a big jump. Graph-max
eliminates that jump entirely:

1. Draw the workflow as a graph.
2. Send the image to a coding agent: *"Write a code mode script that
   implements this workflow. Run it with \<your inputs\>."*
3. There is no step 3.

The graph is the spec. The coding agent reads the topology — nodes,
edges, fan-outs, loops, decision gates — and writes an orchestration
script that runs the whole thing. No framework, no boilerplate, no
intermediate abstraction. Just a picture and a prompt.

This skill teaches you how to draw graphs that coding agents can
implement faithfully, and how to prompt for the result.

## When to use

- "I have a workflow but no code"
- "How do I orchestrate multiple agents?"
- "I want to wire these steps together"
- "How do I build a pipeline with reviewers / validators / loops?"
- "I drew this on a whiteboard, can you implement it?"
- "I need a multi-step agent workflow"
- Any variant of "I know the process, I just need it automated"

## Graph vocabulary

A coding agent can implement any graph, but it needs to understand
what each element means. Use this vocabulary consistently.

### Nodes (the boxes)

Every box is a step that does one thing. Label it with what it does,
not how:

| Shape | Meaning | Example |
|---|---|---|
| Rounded rectangle | Processing step | "Worker", "Planner", "Summarizer" |
| Diamond | Decision gate | "Pass?", "Good enough?", "Approved?" |
| Circle | Terminal (start/end) | "Task" (input), "Send to user" (output) |

Mark node types when agents are involved:

- **Resident agent** (shaded/filled) — persistent, has memory, may be
  called multiple times across the workflow.
- **Ephemeral worker** (outline only) — spawned for one job, returns
  result, dies. Stateless.

### Edges (the arrows)

Arrows are data flow. Label them when the data changes or branches:

| Pattern | What to draw | What it means |
|---|---|---|
| Sequential | A → B | Output of A becomes input of B |
| Fan-out | A → B₁, A → B₂, A → Bₙ | A sends to multiple workers in parallel |
| Fan-in | B₁ → C, B₂ → C | Multiple results converge at C |
| Feedback loop | C → A (labeled "feedback") | C's output routes back to A for revision |
| Conditional | Diamond → X (yes), Diamond → Y (no) | Branch based on a decision |

### Common patterns

These show up constantly. Draw them as building blocks:

*Map-reduce:* One node fans out to N workers, results converge at a
synthesizer. Use for parallel review, multi-perspective analysis, or
any "get N opinions then combine" workflow.

*Feedback loop:* Output goes through a quality gate (diamond). Pass →
continue. Fail → route feedback back to the worker for revision.
Always label the feedback edge.

*Plan-execute-review:* Planner creates a plan → Worker executes →
Plan Reviewer evaluates the plan itself (not just the output) and
sends plan-level feedback. Separates "did we do it right?" from "was
the plan right?"

## Process

### Phase 1: Draw the graph

Use whatever is fastest. Paper and a phone camera works. So does
Excalidraw, tldraw, Miro, or any diagramming tool. The coding agent
reads images — fidelity doesn't matter, clarity does.

Rules for a good graph:

- *One job per node.* If a box does two things, split it into two
  boxes.
- *Label every edge that isn't obvious.* Sequential flow is obvious.
  Feedback, fan-out indices, and conditional branches are not.
- *Mark your decision gates.* Diamonds with yes/no labels. The coding
  agent needs to know what "pass" means.
- *Distinguish agent types.* Shade resident agents, leave ephemeral
  workers as outlines. This tells the coding agent what needs state.
- *Show the terminals.* Where does input enter? Where does output
  leave? Circle them.

### Phase 2: Write the prompt

The prompt is almost always the same:

> Write a code mode script that implements this workflow.
> Run it with \<your inputs\>.

Customize only when needed:

- Specify the language if you care (`"...as a Python script"`)
- Specify the agent provider if relevant (`"use OpenAI for workers,
  Anthropic for the planner"`)
- Specify input format (`"input is a CSV of URLs"`)
- Specify output format (`"output a markdown report"`)

### Phase 3: Send image + prompt to the coding agent

Use any coding agent that accepts images:
- Codex (ChatGPT code mode)
- Claude Code / Claude with artifacts
- Cursor / Windsurf / any IDE agent
- OpenClaw subagent with the image attached

The coding agent reads the graph topology from the image and
generates an orchestration script. It handles:

- Parallelism (fan-out/fan-in)
- Retry loops (feedback edges)
- Decision routing (diamond gates)
- State management (resident vs ephemeral)

### Phase 4: Run and iterate

Run the generated script. If the behavior doesn't match the graph:

1. Check if the graph was ambiguous (unlabeled edges, unclear
   decision criteria)
2. Add the missing labels to the graph
3. Re-send the updated image

Don't debug the script — fix the graph. The graph is the spec.

## Output format

The coding agent produces a single runnable script. No framework
dependencies. The script should:

- Accept input via CLI args, stdin, or a config file
- Print progress as it moves through the graph
- Output the final result to stdout or a specified file
- Exit cleanly on completion

## Anti-patterns

- **Drawing implementation instead of workflow.** Boxes should say
  "Review for tone" not "call openai.chat.completions.create()".
  Describe *what*, not *how*.
- **Skipping edge labels on non-obvious flows.** The coding agent
  will guess, and it will guess wrong. Label feedback loops,
  conditional branches, and fan-out indices.
- **Overcomplicating the graph.** If it has more than ~12 nodes, break
  it into sub-graphs. Each sub-graph becomes a function.
- **Debugging the script instead of the graph.** When the output is
  wrong, the graph is wrong. Fix the spec, regenerate the code.
- **Adding framework abstractions.** The whole point is no framework.
  A script, not a system. If you need a system, you've outgrown
  graph-max and need actual architecture.
