# Design directions

Render the same screen four wildly different ways so the user can discover taste they did not know they had. Use when the user wants a UI but cannot describe what they want: "I have no visual taste", "show me what's possible", or any green-field screen where the first design would otherwise be a guess.

Example trigger prompt:

> I want a review-queue dashboard but I have no visual taste and don't know what's possible. Make me one HTML page with 4 wildly different design directions so I can react to them.

## Output shape

One self-contained HTML page containing:

1. **A shared dataset**, stated up front: the same realistic fake data renders in every direction, so design is the only variable.
2. **Four directions**, each with:
   - A name and a one-line design philosophy in quotes ("Your review queue is an operational system. Show everything, waste nothing, let the anomalies pop.")
   - A full frame rendering the shared dataset in that philosophy
   - **Steal/skip chips** under the frame: 2 or 3 specific details worth stealing, and at least one honest self-critique to skip ("skip · low density, dies at 30 items")
3. **A reply assembler** at the bottom: the user taps a winning direction plus any steal chips, and the page composes the reply text to paste back. The user should never have to write a design brief.

## Choosing the four directions

Directions must differ in philosophy, not palette. Vary along axes like:

- Density: dense ops console vs airy editorial
- Metaphor: table vs cards vs board vs timeline vs terminal
- Tone: calm and human vs data-dense and operational vs brutalist
- Interaction: mouse-first vs keyboard-first

If two directions could be confused at a squint, replace one.

## After the reply

Fold the chosen direction plus the stolen details into one refined design and present that single design next. Do not carry all four forward.

## Quality bar

- Identical data everywhere; realistic names, ages, counts, statuses.
- Every direction is a defensible real product choice, not a strawman.
- Include at least one skip chip per direction. Honest self-critique is what makes the chips trustworthy.
