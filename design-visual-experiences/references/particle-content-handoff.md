# Particle forms that resolve into readable content

Use for transformations between a list, diagram, product structure or interface where the viewer should recognize the same information across different forms. Pair with [motif handoff](patterns/story.md#motif-handoff); a particle burst should advance the story, not conceal an unrelated scene cut.

## Evidence and limits

[Marcell Havlik's September 25 original](https://x.com/cviklihamar/status/2103487512979398698) explicitly credits Opus 5.5 and multiple prompts. A [September 28 creator follow-up](https://x.com/cviklihamar/status/2104662955879281020) describes rasterizing HTML, sampling a lattice, spatially sorting points with Morton order, adding per-point delays and fading live HTML over settled shapes. These are creator-reported techniques; no implementation was retrieved.

Selected playback and sought frames of the 38.49-second original show an unchanged list layout with three items ticked, a dispersed particle phase, a gold sphere, a three-column task board, a particle browser outline and a gold checkmark. This supports the visual progression, not exact algorithm, DOM interactivity, particle correspondence, audio quality or performance. No Skillry comparison matched this source during this pass.

## Original build adaptation

1. **Author the destination first.** Lay out readable text and controls at the intended delivery size. Wait for fonts and assets before sampling. Convert the target's visible coverage into candidate particle positions using one coordinate system for the overlay and particles. Decide which fine detail should stay as ordinary content rather than forcing every glyph into sparse points.
2. **Make sample density a visual control.** A regular cell grid gives a predictable upper bound on density. Select at most one point in each occupied cell and keep deterministic positions for a given state. Compare text at final size: narrow stems and counters disappear before large silhouettes do. Adjust cell size and point radius together; brightness alone cannot restore missing geometry.
3. **Preserve meaningful identity first.** A list gaining checkmarks should retain its existing row samples. Add the changed marks without rebuilding the whole cloud. For unrelated silhouettes, map equal-sized point sets with a reproducible correspondence. Morton order can be a cheap spatial heuristic: sort normalized coordinates by interleaved coordinate bits, then pair by rank. It does not guarantee shortest paths or semantic identity. Keep task or glyph groups separate when unrestricted pairing would scramble meaning.
4. **Separate trajectory from arrival order.** Give points stable delays, then evaluate each point's progress from scene time and that delay. Keep a shared arrival deadline so the last few points do not obstruct reading. Tune a directional wave or clustered stagger before adding independent randomness. For exports, seeking to the same time must produce the same positions.
5. **Hand off at alignment.** Once the particle silhouette settles, fade in the crisp content using the exact same layout transform. Compare baseline, scale and bounds at the crossover. Fade the particles down as content becomes opaque to avoid doubled edges. A subtle particle residue can remain decorative, but readable content owns the settled state.
6. **Use one interaction owner.** In an interactive version, the real content should own focus, selection and hit testing. Decorative particle surfaces should not intercept input. Avoid duplicate accessible text from rasterization helpers; keep one semantic representation. If a transition hides a focused control, preserve its identity or deliberately restore focus to its replacement.

## Tune and diagnose

Expose sampling cell size, point radius, correspondence strategy, stagger spread, settle duration and overlay crossover separately. Inspect a single transition in slow motion and at delivery speed. Begin without bloom, camera movement or flashes so misalignment is visible.

Check the last thin glyph to arrive, the busiest midpoint, a resize during motion, a late font load, reverse seeking, repeated state toggles and a reduced-motion route. A reduced-motion route can show the final content with a short fade; it need not simulate the travel. For responsive layouts, regenerate target samples after layout settles and transition from the current positions rather than snapping back to the old source.

## Adapted prompt

Carry [information] through [two or three meaningful forms] using a stable particle field. Build the final readable content first, sample its shapes reproducibly, preserve unchanged items across state edits, and choreograph staggered travel with a clear arrival deadline. Resolve particles into aligned crisp content before the reading beat. Expose sampling, mapping and crossover controls, and show the midpoint and handoff without decorative effects so defects can be found.

This is original engineering synthesis informed by the creator description and selected video observations. It is not the creator's full prompt or a tested implementation.
