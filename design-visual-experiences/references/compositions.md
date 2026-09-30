# Compose mechanisms into experiences

These are original briefs assembled from the atlas, not extra source projects or claims of tested complete productions. The linked cards retain the primary citations. Choose a composition because its mechanism serves the user's subject; replace the example art direction.

## A tactile product transformation

**Combine:** [One object, many functional states](patterns/motion.md#persistent-shape) + [Elastic indicator with independently timed edges](patterns/motion.md#unequal-edge-springs) + [Change style while preserving object identity](patterns/materials.md#material-swap)

**Direction:** One recognizable object stretches into the next useful state. Establish its contour and mass before changing the surface.

**Construction:** Keep a stable object ID and corner order; retarget edges with retained velocities. Blend roughness or color only after the silhouette reads. Let text settle after the shape.

**Iteration order:** Tune geometry first, spring lag second, shading last. A chrome material cannot rescue a broken silhouette.

**Proof:** Scrub backward and interrupt midway. The object must remain continuous and the final label readable.

## An ink instrument

**Combine:** [A brush that stays consistent at different event rates](patterns/materials.md#distance-spaced-brush) + [Ink that dries, settles and can be re-wetted](patterns/materials.md#wet-dry-ink) + [A drawing gesture that makes a musical phrase](patterns/sound.md#gesture-instrument)

**Direction:** Drawing should feel like acting on a medium with memory.

**Construction:** Resample gesture distance into stamps; deposit pigment and water into separate fields. Derive optional sound from contact speed and pressure, with a smoothed envelope. Capture input events if replay matters.

**Iteration order:** Fix stroke coverage before fibers, diffusion before sound. Provide clear/reset and separate brush size from water load.

**Proof:** Repeat the same path at different event rates; re-wet a dried mark; mute without changing the drawing.

## A living miniature world

**Combine:** [One weather field for every moving material](patterns/worlds.md#shared-wind) + [Time of day changes the whole environment](patterns/worlds.md#whole-world-daylight) + [Small creatures that react to proximity and care](patterns/worlds.md#habitat-reactions)

**Direction:** A small place feels alive because its parts share weather and react to events.

**Construction:** Define world time, weather and event state once. Feed sun angle into sky, exposure, light and shadows. Drive plants with a spatial wind field and let creatures react with bounded delays.

**Iteration order:** Choose one environmental rhythm. Use local variation as response differences rather than independent random wiggles.

**Proof:** Freeze world time, then change weather. All affected systems should agree. Interaction must do more than trigger a decorative particle burst.

## A journey across scale

**Combine:** [Nested worlds with constant perceived zoom](patterns/camera.md#portal-zoom) + [A continuous journey across orders of magnitude](patterns/camera.md#scale-ladder) + [Camera height that makes a small character feel small](patterns/camera.md#subject-scale)

**Direction:** Move from a familiar object into a hidden system while preserving orientation.

**Construction:** Choose overlapping scale bands and one anchor visible during each handoff. Interpolate scale in log space; switch detail tiers behind an aperture or matched shape. Keep a recognizable subject size when teaching a new concept.

**Iteration order:** Plot projected sizes, not only camera coordinates. Reserve the fastest travel for low-information regions.

**Proof:** Inspect immediately before and after each handoff. Shape, color and apparent velocity should agree; labels need holds at readable scale.

## A music-responsive sculpture

**Combine:** [One event score for both audio and visual motion](patterns/sound.md#shared-score-clock) + [Map frequency bands to different physical parts](patterns/sound.md#band-to-part) + [Align an effect by its perceptual attack](patterns/sound.md#peak-alignment)

**Direction:** Distinct parts of the sculpture answer different musical roles.

**Construction:** Analyze or author cues against one audio clock. Map low, mid and high energy to separate degrees of freedom. Use attack/release envelopes; schedule a movement early enough that its visible impact meets the accent.

**Iteration order:** Limit each part to a small movement vocabulary. Change arrangement at musical sections instead of making every frame louder.

**Proof:** Listen to the actual export. Test silence, a single impulse and dense passages; the sculpture should settle rather than jitter.

## A character with weight and intent

**Combine:** [A character bible translated into a controllable rig](patterns/characters.md#identity-rig) + [Walk cycles that keep feet attached to the ground](patterns/characters.md#planted-foot-ik) + [Secondary parts that express the character state](patterns/characters.md#emotional-secondary)

**Direction:** The figure acts, pauses and reacts while maintaining its construction.

**Construction:** Define a stable rig and contact schedule. Move the root over fixed stance targets, solve knees, then add delayed head/hand motion tied to the intended emotion. Keep expression assets distinct from placeholders.

**Iteration order:** Block silhouettes and contacts before surface style. Secondary movement should reveal a choice or force.

**Proof:** Check planted-foot drift, reach limits, grip continuity and a silent-viewing pass. Emotion should survive without a caption.

## A causal scientific explainer

**Combine:** [Compare mechanisms under the same input](patterns/explainers.md#shared-control-comparison) + [An optical explainer whose image comes from its model](patterns/explainers.md#computed-optical-image) + [Explain a process across several scales](patterns/explainers.md#causal-scale-story)

**Direction:** The viewer changes one variable and sees why the result changes.

**Construction:** Create a shared model, derive both diagrams and measurements from it, then expose the parameter. Use a guided camera sequence to connect scales. Label illustrative approximations.

**Iteration order:** Keep decoration separate from computed outputs. Add units, useful ranges and reset before extra camera freedom.

**Proof:** Try known limiting cases and compare both views. The image cannot contradict the displayed measurement.

## A satisfying assembly tool

**Combine:** [An assembly that can be understood in either direction](patterns/interaction.md#exploded-assembly) + [A visual model constrained by a real parts inventory](patterns/interaction.md#buildable-bricks) + [A layout tool that shows the consequences of placement](patterns/explainers.md#constraint-aware-layout)

**Direction:** An object separates into understandable pieces and comes together under the viewer’s control.

**Construction:** Store assembled transforms, part identities and exploded destinations. Validate connectivity or fit against the same data used for drawing. Use constraints to separate labels without changing the assembly.

**Iteration order:** Support direct manipulation first; animate settling on release. Use physical validation appropriate to the actual artifact.

**Proof:** Interrupt assembly and reverse it. No part changes identity. A simple geometric support test is not proof that a real construction is stable.

## A film that demonstrates organization

**Combine:** [Make the benefit visible as a change in structure](patterns/story.md#chaos-to-organization) + [One motif changes meaning across scenes](patterns/story.md#motif-handoff) + [Stillness that makes an action or revelation register](patterns/story.md#quiet-payoff)

**Direction:** The benefit is visible in the changed structure of the same objects.

**Construction:** Introduce a few trackable items, show the organizing rule, and carry a motif through transitions. End on a calm useful state with enough hold to understand it.

**Iteration order:** Give the first action a clear setup. Escalate once, then reduce activity for the payoff.

**Proof:** Track three items through the entire film. Avoid unexplained disappearance, duplication or a title card that tells the benefit without showing it.

## A painterly performance

**Combine:** [Retarget a motion clip to a simplified character](patterns/characters.md#motion-retarget) + [Slow paint marks on smoothly moving geometry](patterns/materials.md#paint-clock) + [Motion blur that preserves the information layer](patterns/production.md#selective-motion-blur)

**Direction:** A coherent performance carries a handmade surface rhythm.

**Construction:** Solve the pose and contacts at a continuous time. Regenerate stable form-aligned marks on a slower texture clock. Blur only the moving channels that need it, preserving the intentionally stepped surface.

**Iteration order:** Separate identity, performance, paint and compositing passes so each can be judged alone.

**Proof:** Freeze the rig with the paint still advancing, then freeze paint while moving the rig. Both should retain recognizable form.

## An operational world

**Combine:** [A spatial metaphor backed by real system state](patterns/interaction.md#operational-world) + [An animated object that communicates system state](patterns/motion.md#semantic-orb) + [Anticipation, release and readable reward](patterns/motion.md#earned-reward)

**Direction:** System state becomes an explorable place with meaningful visual responses.

**Construction:** Map real entities to persistent objects and real events to state transitions. Give loading, waiting, failure and success distinct rhythms. Trigger rewards only after the represented action completes.

**Iteration order:** Use a restrained ambient layer. Keep status legible when animation is paused or reduced.

**Proof:** Replay duplicate and out-of-order events, disconnect the source, and fail an operation. The visual state must remain truthful.

## A reliable rendered film

**Combine:** [Render any frame without playing earlier frames](patterns/production.md#pure-time-render) + [Use a simple 3D blockout to control a later visual treatment](patterns/story.md#camera-from-previs) + [Review moments where the system changes state](patterns/production.md#event-based-review)

**Direction:** The exported sequence matches the designed timeline and can be reproduced.

**Construction:** Build a coarse animatic, establish global/local shot time, and record simulation inputs or bake state where random access is impossible. Inspect frames around semantic events and listen to the encoded result.

**Iteration order:** Choose final resolution and aspect before polishing fine details. Reduce costly effects based on measured bottlenecks.

**Proof:** Render the same frame twice and seek backward. Stateful trails or fluids require replay/checkpoints, not a time-uniform shortcut.

