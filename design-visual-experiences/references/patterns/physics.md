# Physics patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [A chain reaction caused by contacts](#rigid-body-chain)
- [A soft object that remains physical after cutting](#cuttable-soft-body)
- [An expanding force field with persistent aftermath](#pressure-front)
- [Distinct materials in a grid simulation](#falling-materials)
- [A fluid field with a coherent solver order](#fluid-pipeline)
- [Combustion-inspired fields that evolve together](#fire-to-smoke)
- [Water effects driven by depth and disturbance](#causal-water)
- [Keep dense simulation data on the GPU](#gpu-resident-motion)

<a id="rigid-body-chain"></a>

## A chain reaction caused by contacts

For interactive experiments, use [simulation verdicts](../simulation-verdicts.md) to distinguish arrival, sustained stability and completion.

**Mechanism:** The outcome emerges from constraints and collisions, allowing meaningful perturbations.

**Build:**

1. Use a fixed simulation step independent of display rate.
2. Define contact shapes, friction and joints separately from decorative meshes.
3. Record inputs and seed randomness so a reset can reproduce the same setup.

**Tune:** Tune mass ratios, substeps and solver iterations on a small scene first.

**Failure check:** Change the initial impulse and compare results. The reaction must change causally rather than playing the same keyed sequence.

**Adapted prompt:** Build [chain reaction] from actual contacts and constraints, with reset and adjustable initial conditions.

**Evidence:** [@leogao25](https://x.com/leogao25/status/2102544081863717153), [@nybobs](https://x.com/nybobs/status/2103385835328680050). The latter's September 25 original explicitly credits Opus 5.5. Selected muted [original/remake phases](https://skillry.dev/ai-videos/opus-5-5/nybobs-680050) were inspected September 30: wall penetration, a weld-labeled wall and a friction-labeled row. The original overlay names AVBD and 110,000 bricks; the remake names a lightweight position-based solver and 49,724 bricks. These are displayed claims, not measured counts or independently verified implementations. See [inspection limits and test design](../updates/2026-09-30-rigid-body-comparison.md).

**Original comparison checks:** separate visual resemblance from solver equivalence. First compare the same semantic phase: intact wall, first contact, local failure, debris settling. Normalize camera, object dimensions and impact direction before assessing fragmentation. Then test one property per small scene: an impact against an unjoined wall, a jointed wall with an adjustable break threshold, and equally launched blocks with different friction settings on the same plane. Record timestep, substeps, iterations, mass ratio and initial impulse; hold the others fixed while changing one parameter. Inspect rest jitter, persistent penetration, break timing and sensitivity to reset/input changes. A cinematic wall smash or coefficient label alone does not establish contact, joint or friction correctness; benchmark body count and frame time separately on the actual device.


<a id="cuttable-soft-body"></a>

## A soft object that remains physical after cutting

**Mechanism:** A cut changes connectivity while retaining the material state at the cut instant.

**Build:**

1. Represent shape with a volumetric or surface constraint system suited to the desired effect.
2. Split connectivity along the cut and construct valid new boundary surfaces.
3. Transfer position, velocity and material properties to the resulting pieces.

**Tune:** Prove one clean cut before arbitrary slicing. Tune compliance independently from damping.

**Failure check:** Cut during motion, cut twice and reset. Pieces must not explode from stale constraints or lose all momentum.

**Adapted prompt:** Make [soft material] deform and separate under a controlled cut, preserving the state and motion of each resulting piece.

**Evidence:** [@ImaStudio_ai](https://x.com/ImaStudio_ai/status/2104517586092458039). Creator description/prompt; verify the visual when fidelity matters.


<a id="pressure-front"></a>

## An expanding force field with persistent aftermath

**Mechanism:** An event changes objects as its front reaches them, leaving an interpretable spatial trace.

**Build:**

1. Compute arrival time from distance and propagation speed.
2. Apply a distance-dependent impulse or damage value when the front crosses each object.
3. Persist displacement or damage after the luminous front disappears.

**Tune:** Separate visual brightness from physical effect; label stylized models rather than implying accurate blast prediction.

**Failure check:** Pause at several radii. Effects should not occur before arrival, and replay should clear prior damage.

**Adapted prompt:** Visualize [expanding event] through propagation, local response and lasting aftermath, with inspectable timing.

**Evidence:** [@FornYapayZeka](https://x.com/FornYapayZeka/status/2102971287224135914), [@FornYapayZeka](https://x.com/FornYapayZeka/status/2102971287891009707). Creator description/prompt; verify the visual when fidelity matters.


<a id="falling-materials"></a>

## Distinct materials in a grid simulation

**Mechanism:** Materials differ by movement and interaction rules, not color alone.

**Build:**

1. Store material and auxiliary state per cell.
2. Update with double buffering or conflict-resolved moves so each cell is processed predictably.
3. Define density, displacement and transformation rules for a small initial material set.

**Tune:** Vary update traversal or use deterministic parity to avoid permanent directional bias.

**Failure check:** Drop each material in isolation and in pairs. Check mass accounting, boundaries and reset before adding more types.

**Adapted prompt:** Build a sandbox where [materials] behave differently under the same forces and interact through explicit local rules.

**Evidence:** [@cyrilXBT](https://x.com/cyrilXBT/status/2103532793406149036). Creator description/prompt; verify the visual when fidelity matters.


<a id="fluid-pipeline"></a>

## A fluid field with a coherent solver order

**Mechanism:** Velocity transport, pressure projection and dye advection serve different jobs.

**Build:**

1. Keep velocity and dye in separate ping-pong targets.
2. Advect velocity, apply forces, solve pressure and subtract its gradient, then transport dye using the projected flow.
3. Set explicit boundary behavior and expose a velocity or divergence debug view.

**Tune:** Resolution, pressure iterations and vorticity strength trade cost against appearance; avoid presenting artistic vorticity as physical validation.

**Failure check:** A closed field should not accumulate obvious divergence. Compare still water, one impulse and boundary contact.

**Adapted prompt:** Create [fluid interaction] with clear velocity, pressure and pigment stages, then tune the artistic response without hiding instability.

**Evidence:** [@theailoser](https://x.com/theailoser/status/2102565612874596411), [@AxtonLiu](https://x.com/AxtonLiu/status/2103288413969621231). Creator description/prompt; verify the visual when fidelity matters.


<a id="fire-to-smoke"></a>

## Combustion-inspired fields that evolve together

**Mechanism:** Flame, heat and smoke share an evolving field rather than unrelated particle emitters.

**Build:**

1. Track fuel, temperature and smoke or soot as separate quantities.
2. Couple buoyancy and visible emission to temperature, then let cooling produce a different visual state.
3. Sample lighting and sound intensity from the same event or field summary.

**Tune:** Start with a stylized model; keep resolution and buoyancy stable before adding turbulent detail.

**Failure check:** Extinguish the source. Flame should decay while existing smoke continues; light should not remain at full intensity.

**Adapted prompt:** Make [fire effect] evolve from heat into smoke with connected motion, lighting and decay.

**Evidence:** [@NathanWilbanks_](https://x.com/NathanWilbanks_/status/2103881538592981110), September 26, explicitly credits Opus 5.5. Selected [original/remake phases](https://skillry.dev/ai-videos/opus-5-5/nathanwilbanks-981110) were inspected September 30: the original shows a bright flame, broad ground illumination and a rising smoke plume; the remake has taller foreground logs and a narrower exposed flame. Later sampled shots show a smaller campfire in a wider dark composition. These observations do not verify a fluid solver, physical blackbody model, sound coupling or the claimed frame rate. See [the dated comparison record](../updates/2026-09-30-fire-comparison.md).

**Original visual checks:** review the flame opening between fuel geometry, the smoke silhouette above it, and the illumination on nearby surfaces separately. Keep the main flame legible through the intended camera path; moving tall logs can hide emission without any change in heat. Inspect a neutral smoke pass against a contrasting background so bright bloom cannot conceal a missing or clipped plume. Check the light pool on surrounding objects as well as the emitter. To evaluate cooling or extinction, hold camera and exposure fixed and deliberately turn down the source; a pullback, fade or darker grade is not evidence that the simulated field decayed. The source's solver and physical claims remain creator-described until code or controlled behavior can be inspected.


<a id="causal-water"></a>

## Water effects driven by depth and disturbance

**Mechanism:** Shore foam, wakes and refraction arise from specific spatial conditions.

**Build:**

1. Use depth to separate shallow and deep appearance.
2. Generate wakes from moving hulls and foam from breaking or obstructed flow regions.
3. Share the same water normal field across reflection, refraction and specular response.
4. For terrain runoff, track water depth and neighbor flux separately from shading. Limit total outgoing volume to available water and account explicitly for sources, evaporation and drainage.

**Tune:** Tune the near-shore transition before adding more distant wave detail. Keep visual stream visibility thresholds separate from physical depth; inspect map boundaries and shallow wet/dry transitions.

**Failure check:** Move the obstacle or boat. The wake must follow it and disappear appropriately; foam must not slide with the camera. For runoff, reconcile the water budget and test an incline and a basin before judging the finished landscape.

**Adapted prompt:** Build [water scene] around depth, obstacles and moving sources so each visible effect has a clear cause.

**Evidence:** [Source 1](https://x.com/dangreenheck/status/2102911556296052788), [Source 2](https://x.com/MengTo/status/2103155074705019158), [Source 3](https://x.com/StephanFerraro/status/2103020274107224281). Creator text or prompt retrieved; mechanism is an original engineering adaptation. Visual result not implied verified. Additional terrain-runoff evidence: Opus 5.5 post dated September 24 retrieved. Solver, water shader and water tests read at 680f87e6d54984199525dd12005bd95711bb47bb. Three independent local numerical probes passed. Selected original/remake video frames inspected; full benchmark suite, live controls, accuracy and performance not validated.

Read the [terrain-water worked study](../terrain-water.md) for state, rendering and diagnostic choices.


<a id="gpu-resident-motion"></a>

## Keep dense simulation data on the GPU

**Mechanism:** Rendering from simulation buffers avoids copying every body back to the CPU each frame.

**Build:**

1. Choose a data layout usable by both compute and rendering.
2. Run simulation passes on the device and draw instances from the updated state.
3. Read back only selected bodies or events needed by interaction and diagnostics.

**Tune:** Benchmark a representative small scene before scaling; adapt count or quality to measured device capacity.

**Failure check:** Measure compute, render and readback separately. A large advertised body count on another machine is not a performance guarantee.

**Adapted prompt:** Build [dense simulation] with minimal data transfer and a measured quality tier suited to the target device.

**Evidence:** [@nybobs](https://x.com/nybobs/status/2103385835328680050). Creator description/prompt; verify the visual when fidelity matters.
