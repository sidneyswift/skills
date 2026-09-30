# Terrain water: simulation state versus visual treatment

Use with [causal water](patterns/physics.md#causal-water) when rain and springs should form understandable streams and pools. This is a worked study of [Stephan Ferraro's September 24 Opus 5.5 post](https://x.com/StephanFerraro/status/2103020274107224281), with [original/remake comparison](https://skillry.dev/ai-videos/opus-5-5/stephanferraro-224281). The gallery text is a partial description, not a complete build prompt.

## Evidence inspected

At revision `680f87e6d54984199525dd12005bd95711bb47bb`, read the [solver](https://github.com/AiondaDotCom/ai-sim-benchmark/blob/680f87e6d54984199525dd12005bd95711bb47bb/runs/claude-code-opus-5-5/src/sim/water.ts), [water renderer](https://github.com/AiondaDotCom/ai-sim-benchmark/blob/680f87e6d54984199525dd12005bd95711bb47bb/runs/claude-code-opus-5-5/src/render/waterMesh.ts) and [water tests](https://github.com/AiondaDotCom/ai-sim-benchmark/blob/680f87e6d54984199525dd12005bd95711bb47bb/runs/claude-code-opus-5-5/tests/water.test.ts). The repository labels the run Opus 5.5 and shows an MIT license. No implementation is bundled here.

**Code observed:** the heightfield solver moves water between neighbors according to surface-height differences, limits outflow to available volume, and records rain, springs, evaporation and drainage. The renderer uses depth and speed to change visibility, color and foam, with additional animated ripples. It deliberately increases the visibility of fast thin flows without modifying stored depth.

**Video observed:** both comparison videos played. Selected views show a central rocky massif, radial pale channels, small blue pools and an orbiting viewpoint. At a later sample near 26 seconds, the map boundary is conspicuous, especially in the remake. These observations do not establish the solver, performance or accuracy of the remake.

**Tests executed:** three independent probes against the inspected solver passed: conserved initial volume under closed boundaries, moved water downhill on an incline, and reconciled an open-boundary source/sink budget. These were not a rerun of the creator's claimed 23-test suite. They do not validate a physical model or the integrated renderer.

## Original build adaptation

Keep two layers explicit. The simulation stores quantities with units and a volume budget. Presentation converts those quantities into readable marks. Let a stream's visibility be tuned without adding hidden water to make it look thicker. Conversely, do not use an animated highlight as evidence that water is being transported.

Build three small diagnostic scenes before an attractive landscape: a tilted plane to reveal direction, a bowl to reveal pooling, and a bounded patch to expose the source/sink balance. Check `final volume = initial + added - removed`. Choose what happens at the edges as part of the scene design: water can exit, accumulate against a wall, or enter a larger modeled region. A closed domain with persistent inflow needs a deliberate long-run outcome.

After the state works, tune depth color, minimum visible depth, speed-dependent accents, ripple scale and wet/dry blending separately. Check shallow flow against the underlying terrain for flicker. Keep decorative normal perturbations separate from geometric water height when the surface must convey levels.

Use camera framing to explain the catchment: show a source, a descending channel and its destination together before moving closer. If an edge is visible, make it an intentional cutaway or modeled outlet. Concealing an incorrect boundary with fog does not repair the flow.

**Adapted prompt:** Build a small terrain-water study where rain and springs feed visible channels and pools. Define the surface state, units, water budget and boundary behavior first. Demonstrate downhill flow and pooling on simple geometry, then add a landscape. Derive appearance from depth and speed while keeping styling separate from simulation quantities. Show the source-to-destination relationship, test long-run behavior and report which numerical and visual checks passed.

## Let a shoreline remember contact

The [coastline prompt linked in this September 28 Opus 5.5 follow-up](https://x.com/hajimetwi3/status/2104641083733053881) requests shared terrain/depth coordinates, foam with a lifecycle, and sand wetness based on prior wave reach. It also asks for continuous camera passage through the water surface. These are requested behaviors, not verified results. The [Japanese prompt](https://github.com/hajimetwi3/hajimetwi3-prompt-okiba/blob/main/contents/demo/realtime_kaigan_subagent.txt) was read; no generated implementation or motion was inspected for this addition.

**Original implementation sketch:** keep current water coverage, residual wetness and foam density as different fields. In a world-aligned wetness texture, refresh cells actually contacted by water; decay exposed cells with a controllable drying time. For a simple art-directed approximation, use `wet = contact ? 1 : wet * exp(-dt / dryTime)`, with positive `dryTime` in seconds. This is a material-memory model, not a hydraulic solver. Blend sand roughness and albedo from wetness; use current coverage for the water film. Store foam separately so its motion does not drag the wet footprint across the beach.

**Tune:** compare fast, medium and slow drying while holding wave motion and camera fixed. Change roughness before increasing reflectance; keep the dry sand's grain and hue recognizable. Use a debug view for contact, residual wetness and foam before judging the composite.

**Checks for an original build:** pause the camera while water recedes: the wet footprint should remain and fade. Move only the camera: the footprint must stay in world space. Pause simulation time: drying should pause with it. Resize or switch quality without relocating the footprint; explicitly resample the field if its resolution changes. Reset clears both current and remembered state. Check multiple frame rates for comparable decay. Limit the world's accumulation region so distant unused texels cannot create permanent wetness.

**Adapted prompt:** Give [surface] a visible memory of [contact event]. Separate present contact from its residue, expose the residue's decay time, and keep the memory anchored to the surface as the camera moves. Show a diagnostic view and a fixed-camera before/during/after comparison. Use this for water, footprints or pigment only when the material story calls for it; choose the appropriate transfer and decay law for each.
