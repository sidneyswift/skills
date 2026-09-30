# Art direction and principles

These are working judgments synthesized for this skill. Linked sources support particular mechanisms, not a universal formula for beauty. The example library supplies precedents, not proof that every piece meets these standards.

## Make the visual idea specific

1. **Describe a picture, not an adjective.** Replace “premium and stunning” with a subject, spatial arrangement, material, light, and action. “A translucent instrument whose internal path illuminates when touched” is implementable; “award-winning UI” is not.
2. **Choose a visual metaphor that carries the content.** A branching flow can explain routing; layers can explain assembly; compression can express pressure. The metaphor should reveal something about the subject rather than add decoration.
3. **Give one thing priority.** Decide what the eye finds first, second, and third through scale, value contrast, negative space, focus, or movement. If every object glows, none gets emphasis.
4. **Choose a coherent material world.** Paper, ink, glass, clay, metal, pixels, and light suggest different edges, highlights, motion, and sound. Describe those properties consistently. Use a second material for a reason, such as a foreground control against a physical scene.
5. **Make style structural.** A watercolor study needs irregular pigment and soft boundaries; a technical drawing needs measured line weights and spatial relationships. A paper texture overlay alone does not establish either style. See [Anidoodle](https://github.com/alexgreensh/anidoodle) for medium-specific drawing approaches and [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) for contrasting film directions.
6. **Detail supports recognition.** Allocate detail where it identifies the subject or rewards attention. Keep distant forms quieter. Review close and wide views; fine texture cannot rescue weak silhouettes. The [Claude Animation kit](https://github.com/buildwithhanif/claude-animation-skill) demonstrates surface detail and reusable anatomical rigs.

## Give motion a job

7. **Match expression to frequency.** A launch reveal can demand attention. A command used fifty times a day should respond promptly and stay out of the way. [Emil Kowalski](https://emilkowal.ski/ui/you-dont-need-animations) explains why repeated interactions often benefit from less motion.
8. **Preserve identity when continuity matters.** Keep an anchor, direction, shape, or selected object traceable across a transition. Morphing works best when the intermediate states remain understandable. See example 2 and [Onetake](https://github.com/feitangyuan/onetake); the latter is a reference, not a required no-cut rule.
9. **Contrast motion with stillness.** Hold before an important action, or after it so the result registers. Vary pacing according to the idea. Do not impose a fixed number of cuts or a numerical rhythm score on every piece.
10. **Motion explains cause and effect.** A selection expands from its source; a release carries momentum; a collision causes a reaction. [Origin-aware interface examples](https://emilkowal.ski/ui/good-vs-great-animations) are useful studies of this relationship.
11. **Use easing as character.** A precise instrument, soft toy, and heavy door should not share the same bounce. Start with clear acceleration and deceleration; add overshoot only where the object or brand supports it. [Carbon](https://carbondesignsystem.com/elements/motion/overview/) distinguishes routine task motion from expressive moments; its restrained brand rules need not govern a cartoon.
12. **Animate the explanation, not just its label.** If the lesson is pressure, flow, scale, or probability, show that relationship changing. Text identifies what the image demonstrates. If a simplified model is used, disclose its limits.

## Make the system believable

13. **A control must change what it claims.** A viscosity slider should affect a modeled property or be relabeled as a visual effect. Decorative counters and disconnected equations break trust.
14. **Keep shared facts in one place.** Derive labels, geometry, charts, event timing, and related sound from shared parameters. A single change should not leave the explanation contradicting itself.
15. **Design the recovery.** Reset, replay, pause, interruption, and re-entry are part of the experience. A toy that works once is unfinished.
16. **Treat camera motion as attention.** Frame the event that matters. Movement needs a destination or reveal; constant orbiting can hide both form and function.
17. **Let sound reinforce the event.** Contact, acceleration, reveal, and release can have distinct sonic roles. Keep the visual argument legible when muted. Reserve silence as a pacing choice.
18. **Review what the audience receives.** Evaluate the actual size, device, loop, compressed export, or interactive path. Source code intent is not visible quality.

## A practical palette of directions

Choose from these as vocabulary, not templates to stamp onto every project:

| Direction | Visual decisions | Motion character | Useful precedent |
|---|---|---|---|
| Printed illustration | Limited inks, registration offsets, tactile edges | Stepped poses, controlled drift | Window Seat, example 30 |
| Mechanical explanation | Cutaways, clear depth layers, sparse labels | Sequenced assembly, deliberate reveals | Lens / engine, examples 13 and 16 |
| Soft physical toy | Rounded volume, compression, readable contact | Deform, release, damp | Strawberry cake, example 63 |
| Quiet environmental scene | Atmospheric layers, a strong light source | Slow local activity, restrained camera | Boat scenes, examples 20–22 |
| Kinetic identity | Strong typography, repeated shapes, tight palette | Rhythm, tension, changing scale | Brand/type, examples 4 and 9 |
| Painterly story | Expressive silhouettes, mark direction, selected detail | Poses and acting before camera flourish | Examples 25–36 and 59 |
| Procedural field | Local forces, density, emergent structure | Continuous response to input | Fluid and particles, examples 23 and 94 |
| Cinematic spatial reveal | Foreground/midground/background, motivated light | A journey through meaningful scales | Examples 53 and 66 |

Avoid treating high engagement as a design principle. Study what is visible, what the author actually documented, and what the new audience needs.

## Turn an abstract theme into an action

In [Diomira](https://invisiblecities.vercel.app/en/diomira/), a faint duplicate city sits apart from a solid city. Selected live samples after tapping showed the duplicate close to the solid geometry and a terrace figure with a raised arm; later it was separate again and the arm lowered. The page explains this as a remembered evening briefly meeting the present. Its [September 29 creator post](https://x.com/aditecco/status/2104744903309770864) explicitly credits Opus 5.5. This is an observed interaction with a stated interpretation, not a code-verified reconstruction. See [the inspection record](updates/2026-09-30-playable-metaphor.md).

Extend the visual-metaphor principle with this original design method:

1. **Name the relationship before choosing effects.** Write a sentence with two states and a verb: an echo approaches its source; a concealed structure becomes legible; a growing load deforms its support. Decide what the viewer should understand after acting. A palette and camera orbit alone do not communicate that relationship.
2. **Give the input a semantic job.** Choose an action that changes that relationship. Alignment might use a press or drag; revealing might use separation; balance might use placing weight. Keep navigation distinguishable from the meaningful action, especially when orbit and tap share a canvas. Display a short verb-led invitation and provide an equivalent focusable control.
3. **Stage baseline, response, consequence and return.** Show enough of the baseline to establish the difference, make the input response obvious, hold the meaningful state long enough to read, then preserve or release it according to the subject. A fleeting reunion may separate again; an irreversible assembly should not silently undo itself. Decide this deliberately.
4. **Expose the few parameters that carry meaning.** For a new alignment study, tune baseline displacement relative to subject width, ghost opacity, alignment duration, hold duration and release duration. Start with one geometry source and a second transform so identity stays legible. Keep the ghost distinguishable when superimposed and when viewed from another angle. These are implementation suggestions, not measurements or inspected source code.
5. **Test the idea without the explanation.** Ask what changed and what caused it before showing the interpretation. If the action reads as a generic flash or camera move, strengthen the spatial relationship. Then check rapid repeated input, input during return, orbit-versus-tap disambiguation, a narrow viewport and a reduced-motion state comparison. Never require sound to identify the action's consequence.

**Adapted prompt:** Translate [theme] into one visible relationship the audience can change. Describe the baseline, meaningful input, consequence and return before building. Choose a small set of controllable parameters and a visual identity that survives the transition. Provide an accessible action and reduced-motion comparison. Inspect the actual states; label interpretation separately from implementation evidence.
