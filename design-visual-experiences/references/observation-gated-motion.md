# Change the world only while it is hidden

Use for gaze-driven encounters, spatial reveals or an installation that rearranges objects when the audience looks away. This recipe needs camera visibility, not eye tracking. Make the rule understandable before introducing darkness, mirrors or forced blinks.

## Evidence

[Blendi's September 17 announcement](https://x.com/BlendiByl/status/2100442177159729336) explicitly credits GPT-6 Astra and fal. Its [creator follow-up](https://x.com/BlendiByl/status/2100442181983195500) links [Don't Look Away](https://github.com/blendi-remade/weeping-angels). This is a last-30-days reference, outside the primary seven-day window.

At revision `164a9049c00c79663e02a51f21c333a6bb9ee462`, read `src/visibility.ts`, `src/illumination.ts`, `src/angels.ts` and selected visibility/rule tests. The implementation uses posed bounds, opaque blockers, approximate illumination and floor-reflection checks. Before committing movement it examines a volume enclosing the old and proposed poses. Test cases cover wing slivers, gaps between blockers and visible paths between hidden endpoints. These tests were read, not executed.

The live demo loaded: the entrance view showed an aisle, statues, candles, light shafts, damp-floor highlights and an objective HUD. This confirms the initial rendered scene only. Gaze rules, blinking, reflections, timing, sound, completion and performance were not exercised. No repository-wide license file appeared in the retrieved tree/API metadata; bundled fonts have separate license files. Link to the source; no implementation or assets are bundled here.

## Original build recipe

1. **Choose the perceptual promise.** If the object must never visibly change, classify uncertain visibility as observed. A false positive may delay the surprise; a false negative breaks the illusion. Keep this policy separate from ordinary render culling, which serves a different purpose.
2. **Use geometry that matches the question.** Build an enclosing volume for the current pose and orientation. A center-point test misses wings, handles and other protrusions. For wide objects, a few conservative sections can reduce false freezes caused by empty space in one large box. Navigation colliders are not automatically opaque blockers: railings and open furniture may stop walking while preserving sight.
3. **Treat hidden as a proof, not a collection of missing samples.** Testing several rays can miss a slit. In this source, one convex solid must cover the rays to all box corners before the box is classified as fully hidden. That is conservative and may decline to recognize combined cover from several objects. Choose finer geometry or another visibility method only when those false freezes matter; do not silently trade away the promise.
4. **Prepare, inspect, then commit.** Compute proposed position, facing and pose without changing the rendered object. Check the current view, candidate view and the region traversed. Commit all visual state together only if the transition remains hidden. Two concealed endpoints do not establish a concealed path. For continuous rotation, an endpoint box union may miss an intermediate protrusion: use a rotational envelope or validated intermediate bounds. Instant pose swaps and interpolated morphs also require different bounds.
5. **Include alternate ways of seeing.** If reflections are visible, decide whether they hold the object still. If lights can switch, account for silhouettes against lit backgrounds and for the frame in which the light first reveals the object. Approximate light volumes are gameplay rules, not pixel-accurate visibility. Rendering-quality modes that remove a reflection should update its observation rule consistently.
6. **Separate perception, movement and consequences.** Being watched may stop motion without undoing contact already reached. Emit reveal feedback when observation changes and the object has meaningfully changed, rather than firing a surprise every frame. Keep pause and tab suspension on the same gameplay clock so hidden-tab time cannot advance an encounter unexpectedly.

Tune the screen-edge margin, bound tightness, movement distance per update, pose progression, light reveal range and reveal-feedback cooldown. Inspect false freezes as well as forbidden visible motion: a mathematically cautious rule can still make an experience feel unresponsive.

**Failure checks:** a protrusion at each screen edge; two pillars hiding corners but leaving a central slit; two hidden endpoints with a visible crossing; a pose extending beyond its rest bounds; a reflection-only view; a flashlight turned on during a proposed step; pause/resume. For smooth turns, include an intermediate orientation wider than either endpoint. Record the rule and rendered state at the failing frame.

**Adapted prompt:** Build an interactive [scene] where [object] changes only when certainly hidden. Give it current and proposed state, pose-aware bounds and an explicit uncertainty policy. Demonstrate the slit, crossing-path and intermediate-rotation cases before adding atmosphere. Label what was code-inspected and what was actually observed in play.
