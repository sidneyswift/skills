# Interactive and 3D design

Use the opening sections for interaction/state/renderer choices, or jump directly to a focused recipe. These optional recipes extend the [canonical pattern cards](atlas.md); they are not prerequisites for every spatial experience.

**In this guide:** [Design an interaction people can discover](#design-an-interaction-people-can-discover) · [Separate authored spectacle from a simulation](#separate-authored-spectacle-from-a-simulation) · [Build an experiment with several explanatory views](#build-an-experiment-with-several-explanatory-views) · [Make spatial scenes read well](#make-spatial-scenes-read-well) · [Product inspection through camera presets](#product-inspection-through-camera-presets) · [Rendering choices with practical consequences](#rendering-choices-with-practical-consequences) · [Reference routes](#reference-routes) · [Fold a structure through shared crease state](#fold-a-structure-through-shared-crease-state) · [Turn a gesture into one tangible release](#turn-a-gesture-into-one-tangible-release) · [Preserve compatible actions inside a spatial scene](#preserve-compatible-actions-inside-a-spatial-scene) · [Make physical objects part of the animation](#make-physical-objects-part-of-the-animation)

## Design an interaction people can discover

Name the user's verb: drag, rotate, cut, tune, assemble, explore, compare, or play. Make the first action apparent through composition, a short cue, or a restrained demonstration. A long instruction panel usually cannot rescue an unclear affordance.

Map input to a meaningful parameter. Then show both the immediate action and its consequence. In a lens explainer, changing focus should affect the optical explanation and displayed result; in a physical toy, a press should deform the touched region. Example 13 is a useful explainer reference, and 63 is a soft-body prompt reference.

Give each input one clear owner. Dragging the object should not also orbit the camera. Preserve normal page scrolling outside an immersive canvas; supply a way to leave pointer lock or immersive navigation. For touch, avoid interactions that depend solely on hover. Provide named controls and a usable keyboard path where the task permits it.

For concrete pinch/drag/tap arbitration and recovery checks, use the [spatial input study](spatial-input.md), based on pinned code from a recent Astra 6 game.

For camera-driven hands, use [hand/depth alignment and worker timing](hand-depth-input.md) before coupling tracking to a material or simulation.

## Separate authored spectacle from a simulation

An animation can be excellent without simulating its subject. Choose honestly:

| Need | Suitable structure | Evidence to check |
|---|---|---|
| Explain a fixed sequence | Authored timeline with visible cause/effect | Correct order and understandable transitions |
| Let a user change parameters | State model driving the view | Different inputs produce the intended different outcome |
| Explore physical behavior | Solver with stated assumptions | Stable integration, contacts/constraints, recovery and meaningful limits |
| Present actual scientific claims | Validated model/data plus visualization | Units, sources, ranges and consistency |

Use a shared state object or equivalent authoritative model. Derive geometry, labels, plots, and readouts from it. Test reset after multiple interactions, not only on first load. Avoid hardcoded branches that appear general but only support the demo's first two states.

For fixed-step simulation, separate simulation time from display time. Bound catch-up work after a stalled frame; use interpolation when appropriate. For reproducible replays, keep the seed, inputs, and integration schedule deterministic. Arbitrary seeking in a stateful solver needs replay/checkpoints or a precomputed trajectory; merely setting a timestamp does not reconstruct physics. The [Horizon animation project](https://github.com/misbahsy/claude-horizon-animation) is a useful reference for physics-driven scenes and linked mathematical explanations.

## Build an experiment with several explanatory views

[Flight Lab](https://wind-tunnel.kobez.dev/), linked by a [September 29 Astra creator post](https://x.com/kobez_01/status/2104951103896838350), is a useful live interaction reference. Aircraft, wing and section views reveal different levels of detail; angle controls, force labels, a plot marker and numeric readings describe the current setup. Selected controls were exercised; this establishes interface behavior, not aerodynamic accuracy. See [the observation record](updates/2026-09-29-experiment-views.md).

The following is original implementation guidance:

1. **Separate experiment inputs from presentation.** Keep quantities such as speed and angle in the experiment state; keep view, layer visibility and camera in presentation state. Derive a response record from the inputs, then use that record for the object, vectors, plot marker and readouts. A visibility toggle should not quietly recompute a different experiment. State dependencies explicitly when a layer requires a particular view.
2. **Make view changes answer a question.** Start with the recognizable whole object, use a component view to locate the mechanism, then a section to expose the hidden relationship. Preserve inputs while changing representations. Match landmarks and orientation where practical; choose a legible section camera instead of carrying an unusable orbit into the cutaway. If a view-specific layer switches views, show the new selection clearly and avoid resetting inputs.
3. **Pair movement with a stable comparison.** Show the input value, relevant threshold and response plot together. A marker on a fixed-domain plot explains where the current state sits relative to alternatives. Avoid continuously rescaling the plot around its current point; that can conceal the size of a change. Use units and consistent vector/legend meanings. Any nonlinear vector scaling or illustrative field should be identifiable as such.
4. **Design a short experiment loop.** Make one parameter's visible consequence easy to discover before adding more controls. Invite comparison of two nearby states around an interesting threshold. Let the user remove visual layers to see the underlying geometry and restore them without losing the setup. Keep pause, reset and a useful default view accessible.
5. **Test separation and recovery.** Capture response values, toggle layers and switch views, then verify the values stay stable unless the experiment inputs changed. Move one input through a meaningful range and check the geometry, marker and labels agree. Reset after several changes and compare with the initial state. Test pause separately from reset: a changed button label alone does not prove all animation stopped. Establish a deliberate policy for changing inputs while paused.

Expose view choice, one or two meaningful experiment inputs, field visibility and a reset. For a stylized explainer, label approximations and keep illustrative effects out of quantitative readouts. For scientific use, validate the model and data independently; polished airflow curves are not evidence of a solved flow field.

**Adapted prompt:** Build an interactive [system] with whole-object, component and section views sharing one experiment state. Couple the visible mechanism, response plot and readouts. Let presentation layers explain the result without silently changing it. Demonstrate a threshold comparison and a reset, and distinguish observed interface behavior from model accuracy.

## Make spatial scenes read well

- Block out camera, scale, major masses, and lighting before detailed materials.
- Use overlap, value separation, grounded contact, and atmospheric depth to make space legible.
- Ensure controls and labels remain readable against the moving scene. Attach explanatory labels to meaningful parts; resolve occlusion deliberately.
- Make exploration worth doing: reveal a cross-section, viewpoint, state, or relationship that a flat image cannot show.
- Keep camera speed and turn behavior appropriate to the scale. Offer a stable or guided view for people who do not want free navigation.

For water, translucency, or metallic surfaces, first decide which visual cues do the work. Reflections, refraction, absorption, caustics, and surface normals have distinct roles. A stylized solution can omit some while remaining coherent. [Clearwater](https://github.com/Aureliengmz/clearwater) and [Tidewater](https://github.com/dgreenheck/tidewater) expose implementation examples; do not infer that their settings are portable across all devices.

## Product inspection through camera presets

The [Artura configurator](https://3d-car-configurator-lac.vercel.app/) is a broader-window September 22 reference. Its [creator](https://x.com/xingor_dev/status/2102316320012607591) credits GPT-6 Astra with Blender model optimization, then describes building the configurator themselves. Do not attribute the entire implementation to Astra. Selected live paint, studio, headlight, airflow and camera controls were exercised; no code, WebGPU backend, optimization ratio or physical airflow accuracy was verified. See the [inspection record](updates/2026-09-30-product-inspection.md).

The following is original implementation guidance inspired by those interactions:

1. **Author a purpose for each camera stop.** Overview establishes silhouette; a close wheel view reveals construction; a cockpit view explains the interior. Store a target, position or orbit parameters, framing margin and appropriate zoom limits per stop. Check occlusion and cropping at the destination aspect ratio. A named preset should consistently reveal its named feature.
2. **Preserve the configuration during inspection.** Keep selected finish and optional equipment separate from camera and studio state. Make camera reset return to a useful overview without resetting finish, lights or effect toggles. Offer a separate full reset if needed. The inspected demo preserved blue paint, daylight studio and headlights after camera reset.
3. **Let users see the object without spectacle.** Provide a direct toggle for trails, airflow or other explanatory overlays. In the observed scene, disabling airflow removed luminous lines while leaving the car and configuration intact. Treat these lines as illustrative unless an actual solver has been validated. Avoid placing the strongest luminous effects across the feature being inspected.
4. **Judge materials under a controlled comparison.** Keep camera and finish fixed while switching lighting; then keep lighting fixed while changing finish. Include both dark and bright finishes in the review. Inspect shadow detail, highlight shape, transparency and surface continuity. Daylight samples of this demo had broad washed-out highlights even with headlights off; this is an observed appearance, not a diagnosis of its renderer. In a new build, inspect lighting, exposure, tone mapping and post-processing separately before changing the base color to compensate.
5. **Make camera handoff predictable.** For a new build, interrupt a preset transition from its current visible pose rather than restarting from the previous preset. Give dragging and preset motion a deliberate ownership policy. Test repeated preset selections, resize, drag interruption and return to overview. These interruption behaviors were not tested in the source demo.

Tune feature framing, transition duration, orbit limits, environment intensity and effect brightness independently. A shorter transition can improve comparison, while a longer one can explain spatial relationships; judge whether the feature remains legible throughout the move. Respect reduced motion with an immediate or restrained view change.

**Adapted prompt:** Build a [product] inspection experience with meaningful overview and detail cameras. Preserve the chosen finish and options while changing views. Include a plain inspection mode without decorative overlays. Review dark and bright finishes under two controlled lighting setups, test interrupted camera movement and camera-only reset, and report the actual device and rendering limits verified.

## Rendering choices with practical consequences

**Color:** Track input, working, and output color spaces. Three.js lighting uses a linear working space; color textures and numeric data maps need different treatment. Avoid fixing a conversion error with arbitrary exposure changes. Consult the [current Three.js color guide](https://threejs.org/manual/pages/color-management.html) for the installed version's API.

**Performance:** Set a target device and frame budget, then measure the actual interaction. Reduce internal render resolution, expensive passes, particle count, or shadow cost when the profile calls for it. High device-pixel ratios increase the rendered pixel workload quadratically. Batch repeated geometry where appropriate and release unused GPU resources. The [MDN WebGL guide](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices) covers back-buffer sizing, batching, memory, and portability.

**Fallback:** Detect required rendering capabilities. Offer a simpler renderer, static explanatory view, or clear unsupported message instead of a blank canvas. Do not claim a fallback exists until it has been exercised.

**Verification:** Check a typical input, an extreme input, an interrupted action, repeated reset, resize, and the most demanding scene. Capture key states for visual review, but test controls live. A simulated crowd or fluid demo is not evidence of real-world predictive accuracy.

## Reference routes

- Optical/mechanical explanation: 13, 14, 16, 17.
- Fields, fluids and emergent motion: 18, 23, 46, 51, 55, 94, 103.
- Spatial exploration and environmental art: 15, 20–22, 57, 74–75, 78, 93, 95, 101–104.
- Physical toys and machines: 19, 38–39, 63–64, 68, 77, 84, 99.
- Playable visual worlds: 47–50, 62, 65, 71, 73, 80, 90, 100.

Numbers refer to [examples.md](examples.md). Some entries are comparisons or third-party posts; read the evidence notes before attributing them.

For generated characters that need expressive eyes, lids and brows, read [facial preparation](facial-preparation.md) before committing to a rig.

For gaze-driven reveals or objects that change only while hidden, use [observation-gated motion](observation-gated-motion.md), including partial visibility and transition bounds.

## Fold a structure through shared crease state

A [September 29 origami comparison](https://x.com/vaclav_kozak/status/2104752931710902716) attributes its upper result to Opus 5.5 and lower result to Sonnet 5.5. Its [two-page prompt](https://x.com/vaclav_kozak/status/2104753860682068305) requests crease-axis folding, edge-length preservation, a progress control, a flat crease editor and tactile feedback. Selected video samples show the Opus view's crease panel beside a flat sheet at 0%, then a raised zigzag structure at 100%. These samples do not verify a general origami solver, arbitrary crease editing, physical validity or the requested shader/audio features. See [the evidence record](updates/2026-09-30-crease-state.md).

Use this original engineering adaptation for paper toys, folding diagrams, packaging previews and articulated exhibits:

1. **Separate the flat specification from the posed geometry.** Give each face and crease a stable ID. Store crease endpoints in sheet coordinates, fold direction, target angle and activation interval; derive the 2D map and 3D pose from this shared specification. A line drawn over a texture is not a hinge. Splitting a face must update its geometry and adjacency before that line can participate in folding.
2. **Start with a solvable mechanism.** Build two rigid faces and one hinge first. Rotate the moving face around the crease line rather than interpolating its vertices directly toward a final silhouette. A rigid rotation preserves distances within that face. For a chain or tree of faces, compose child transforms from their parents and transform each hinge consistently. Closed crease loops, intersections, collisions and valid origami constraints require more than this simple hierarchy; label an authored approximation honestly.
3. **Make progress reproducible.** For a designed sequence, map global progress into a local interval for each fold, then ease its angle. Rebuild the pose from the flat rest state whenever progress changes, including backward scrubbing. Do not keep rotating yesterday's vertices by today's angle. Select the active crease in both views and keep its direction identifiable by a symbol or line style as well as color.
4. **Keep tactile animation on a separate layer.** A tap-triggered heartbeat, hop or flap can give the finished object character. Apply that response through explicit articulation or a reversible secondary deformation; do not silently rewrite the crease pattern. Define what happens when folding resumes mid-response. Reset should restore geometry, progress, active crease and transient motion together.
5. **Stage material after structure.** Use simple front/back colors and neutral lighting while checking folds. Then add paper grain, soft shading and translucency appropriate to the brief. Thin-paper glow is a visual treatment unless the light transport was actually modeled. Neither bloom nor double-sided rendering establishes thickness, collision or physical validity.

**Tune:** signed fold angle, order/overlap of activation intervals, progress easing, crease emphasis, camera angle, paper contrast and secondary-motion amplitude/damping. Choose ranges for the particular mechanism rather than promising every drawn pattern can fold.

**Failure checks:** hinge endpoints remain coincident; face edge lengths stay stable; forward and backward scrub reach the same pose; the 2D map and 3D selection agree; a changed pattern rebuilds dependent geometry; unsupported patterns receive clear feedback; repeated taps and preset changes clear stale motion; reset works after mixed editing and folding. Test self-intersections separately if collision-free folding is a requirement.

**Adapted prompt:** Build a [folding object] with one shared crease specification driving a flat diagram and a 3D view. Prove a single hinge first, then a small authored sequence with reversible progress. Keep playful secondary motion separate. Show structural checks before surface polish, and state which fold patterns and physical constraints are supported.

## Turn a gesture into one tangible release

[This September 28 dispenser](https://x.com/MengxueBi/status/2104619977454362948) credits Opus 5.5 and Blender. In the [live demo](https://m-ms-dispenser.vercel.app/), a downward hand drag released one candy, reduced stock from30 to29 and incremented its color tally. Tapping the settled candy increased Eaten to1; a small subsequent pull released nothing. Tapping the cap restored stock to30 while retaining the tally and Eaten count. Selected inline code confirms a release latch with separate fire/rearm thresholds. See [inspection limits](updates/2026-09-30-tangible-release.md).

Original adaptation for mechanical toys, collectible reveals and tactile product demonstrations:

1. **Show preparation before commitment.** Let a normalized gesture value move the handle and visibly prepare the payload. Keep the consequential release as a discrete event. Return an incomplete gesture to rest without inventing a reward. Build the affordance into the object's pose, with a short hint and a keyboard alternative.
2. **Latch once per cycle.** Track ready versus released separately from the handle's position. Crossing the activation threshold while ready consumes one unit and creates one payload. Rearm only after returning below a lower threshold. The gap between thresholds prevents jitter near the trigger from producing repeated events. Apply pointer and keyboard input through the same event rule.
3. **Transfer ownership at release.** Before release, the payload belongs to the mechanism; afterwards, a dynamic object owns its motion and identity. Position it at the outlet before enabling its velocity and collisions. Do not leave both a loaded copy and a moving copy active. Use a stable ID so a rapid double tap cannot consume the same object twice.
4. **Separate the next action from the first.** After release, invite a meaningful follow-up: collect, open, consume or inspect. Update the hint at that state change. Remove the object's hit target as soon as consumption begins, even if a short disappearance animation continues. Keep feedback tied to the particular object the viewer acted on.
5. **Define stock and history explicitly.** Refill can replenish stock while retaining the session's history; reset can clear both. Name them accordingly. If performance cleanup removes old objects, record that separately from consumption. A strict conservation check needs cumulative refills and retired objects, not just a current stock gauge.

**Tune:** pull travel, activation/rearm gap, return damping, payload launch speed, settling behavior and selection tolerance. Prefer a larger invisible hit region to making a small object visually oversized. Near-object selection should respect occlusion and avoid stealing taps meant for the mechanism or camera.

**Failure checks:** hold beyond the trigger without repeated release; jitter across the fire threshold; release below it; double-tap a consumed object; refill while partly pulled; exhaust stock; cancel the pointer gesture; change focus while a keyboard pull is held; remove old payloads without incrementing Eaten. Treat pointer cancellation as cancellation, not a click. Use measured input time for release velocity rather than assuming a fixed pointer-event rate. These last two are recommendations for a new build, not claims that the inspected demo implements them.

**Adapted prompt:** Create a tactile [object] where [gesture] prepares and then releases one [payload]. Show the causal movement before the release, latch once per completed cycle, and give the payload a second purposeful interaction. Keep stock, consumption, refill and reset coherent. Test partial gestures, held input, cancellation and repeated selection before polishing materials or sound.

For deformable tactile objects, read [local deformation and material memory](local-material-memory.md): stable contact coordinates, bounded influence, independent response/recovery and camera-input ownership.

## Preserve compatible actions inside a spatial scene

[Louise de Sadeleer's September 23 tutorial](https://louisedesadeleer.substack.com/p/i-turned-my-apartment-into-a-video) and [original post](https://x.com/LouiseDSadeleer/status/2102679047918555146) explicitly credit GPT-6 Astra. Its apartment pet is a useful interaction-composition reference: the tutorial asks for taking a toy without leaving the couch and petting without dropping the toy. Selected [template code](https://github.com/louisedesadeleer/build-your-own-apartment) checks animated body/prop bounds and reduces seated gesture strength when space is tight. In the live demo, a rope request was rejected for insufficient room; after jumping onto the couch, taking a ball succeeded. Petting while holding the ball was not tested. See the [dated evidence and limits](updates/2026-09-30-compatible-actions.md).

Use this original adaptation for companions, tabletop scenes, interactive mascots and product assembly:

1. **Represent compatible state separately.** Track location/support, posture, held object and transient expression independently. An event should change only the state it owns: acquiring a prop changes possession; affection temporarily layers a response over the current posture. Define incompatible combinations explicitly, such as walking during a committed jump. Avoid a single animation label whose every change silently discards the previous activity.
2. **Check the next pose with its attachments.** A standing collision shape does not describe a seated body, a swinging tail or an extended prop. Create a probe using the same articulated transforms as the visible object. Test the intended pose plus attached geometry against obstacles and bounds; check support separately. Empty space above a seat does not prove that the feet or belly remain supported on it.
3. **Adapt expression to the available space.** Try a small ordered set of decreasing gesture amplitudes. Select the strongest response whose checked poses remain clear and supported. If none works, keep the existing valid state and give contextual feedback. Do not silently teleport, drop an object or cancel sitting just to make room for an optional flourish. A subtle head response can communicate affection when a full-body wiggle would clip.
4. **Check the transition, not only its destination.** Sample important phases of a jump, sit or lean, including extremes of secondary motion and prop sway. Expand bounds to account for untested motion where defensible. Sampling can miss collisions between poses; use conservative swept bounds or continuous tests when required. Keep the collision approximation and supported animation range explicit.
5. **Keep feedback tied to the attempted action.** Clear an obsolete failure message after a successful action and make temporary lockouts understandable. During a jump, disable or queue conflicting actions according to a documented rule, then restore their affordances. The inspected demo retained an earlier insufficient-room message while also reporting successful ball possession; treat this as a feedback-coherence check, not a desired behavior.

**Tune:** gesture amplitude and phase, secondary-motion range, collision margin, support tolerance, transition sampling and prop bounds. Derive spatial values from the object and room scale rather than copying another scene's constants. Cache expensive pose probes only with all geometry-affecting inputs represented; invalidate when the rig, prop, scale or environment changes. Bound cache growth.

**Combination checks:** seated + acquire prop; seated + affection; seated + prop + affection; prop replacement; transition interrupted by a new request; rejected action followed by a valid action. Assert both the changed and preserved state, then inspect body/prop contact through the motion. Include narrow seats, nearby obstacles and reduced motion. These are proposed checks for a new build, not a claim that the reference passed them all.

**Adapted prompt:** Build an interactive [original character or object] whose location, posture, attachments and expressive responses compose predictably. Preserve compatible state when a new action begins. Use pose-aware clearance and support checks, reducing optional gesture strength when space is tight. Demonstrate combined actions and recovery from a rejected action before polishing materials.

## Make physical objects part of the animation

[A September 30 Opus 5.5 projection-mapping post](https://x.com/antipdoom/status/2105102530049175928) turns three candles and a pot into a small animated stage. Selected recording states show a luminous character near the pot, then near a candle, with colored light on the objects and later shapes across the wall. The creator says a camera and projector enabled automatic calibration; no calibration procedure, code or accuracy measurement was available in the inspected post. See [evidence and limits](updates/2026-09-30-physical-stage.md).

Original adaptation for tabletop exhibits, installations and spatial storytelling:

1. **Give the real geometry a narrative role.** Choose a few recognizable landmarks: a rim as a stage, a top edge as a landing point, a gap as a passage. Author the defining action around those landmarks before adding a full-wall spectacle. Keep the physical silhouettes readable during the quiet setup and the busiest moment. The projection should explain why these particular objects are present.
2. **Separate content coordinates from output alignment.** Store named objects, visible surface regions and action anchors separately from animation time. Map that specification into the projector output through the chosen calibration/warping system. Keep a per-surface mask and explicit background region so an intended glow can be distinguished from unintended spill. Do not assume one flat warp fits objects at different depths or curved surfaces. Begin with a fixed arrangement and a small usable surface region; add geometry-aware mapping only when the scene needs it.
3. **Prove registration before choreography.** Project a restrained diagnostic outline, numbered anchors and a grid onto each target. Check corners, curved silhouettes, gaps and surface boundaries from the intended viewing position. Inspect both the camera image and the physical result: a pleasing camera view does not establish alignment from every audience position. Save calibration with the output resolution, projector/camera pose and object arrangement. Moving an object or changing output geometry invalidates the affected mapping. A manually aligned fallback is useful when automatic calibration is unavailable; name it honestly.
4. **Drive object and background events from one sequence.** Define each transfer as departure, travel, arrival and a short response at the destination. Use the named anchors for launch and landing instead of hand-tuning unrelated screen coordinates. Give each phase enough visual separation that the audience can follow the action. Keep local highlights and any wider wall response on the same timeline. Specify whether glow may cross a mask boundary; avoid feathering every edge until object-specific lighting becomes a generic rectangle.
5. **Test light on the actual material.** Evaluate a small palette on the real objects before final grading. Tune brightness, contrast, mask inset and feathering for ambient light and the chosen surfaces. Check the scene with the animation paused at contact, brightest spread and final hold. If an audience member or object blocks the projector, the content cannot simply draw through the obstruction; design a limited viewing area or a graceful interrupted state as appropriate. Do not infer projector performance from a screen capture.

**Controls and checks:** expose alignment mode, object masks, named anchors, global sequence progress and a brightness control. Test a deliberate object displacement to reveal stale calibration, a projector/output resize, the most demanding edge crossing, a temporary occlusion and a replay after adjustment. Preserve the authored sequence while recalibrating its spatial placement. For installations with camera input, distinguish a static calibration photograph from continuously tracked geometry.

**Adapted prompt:** Turn [physical objects] into a short projected story. Give each object a role and prove one action that transfers between named surface landmarks. Separate calibration, masks and anchors from the animation timeline. Show diagnostic alignment before the finished sequence, test it on the actual materials, and state which placement changes require recalibration. Treat automatic calibration as a capability to demonstrate, not an assumption.

For simulations whose most interesting state passes quickly, use [event-triggered inspection and bounded jumps](simulation-event-stops.md): detect within simulation steps, hold the exact state, and keep jump/arrival behavior explicit.

For unfamiliar controls, use [action-gated lessons](action-gated-lessons.md): teach safe practice, tool contrast and real constraints through measurable effects, with separate demonstrated and bypassed completion.
