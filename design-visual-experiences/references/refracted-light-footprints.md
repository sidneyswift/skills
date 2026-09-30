# Refracted light footprints

Use this for a moving glass object, liquid vessel or focused-light exhibit where illumination on the receiving surface should respond to the same geometry as the visible refraction. The recipe is an original adaptation of [selected Whiskey Caustics code and live checks](updates/2026-09-30-caustic-footprints.md), not a general photon-mapping implementation.

## Build one convincing light transfer

1. **Share the optical state.** Feed object pose, boundaries, medium indices, absorption and surface normals into both the view-facing material and the light-transfer pass. Start with one object, one directional source and a planar receiver. Keep normal transformations explicit as the object tilts.
2. **Compare undeviated and refracted footprints.** Launch a structured grid of light rays around the object. Record where each ray would hit the receiver without the object, then trace its refracted path to the actual hit. Reject paths that do not reach the receiver. Store the result in receiver coordinates, not a decorative texture glued to the object.
3. **Estimate concentration from area change.** Compare the local ray-cell area before and after refraction. Compression should brighten the receiving region; spreading should dilute it. Multiply by transmitted throughput. Protect nearly collapsed cells with an explicit denominator floor and intensity cap. These stabilizers bias the result: inspect their effect instead of calling the output physically exact.
4. **Replace the intercepted direct light.** Maintain the undeviated coverage footprint alongside the deposited radiance. Compose remaining direct light plus transported light, so enabling caustics does not merely brighten an already fully lit receiver. Keep ambient and unrelated lighting separate. If several objects overlap, design a coverage/transmittance composition explicitly; blindly summing masks can subtract too much light.
5. **Update mapping before presentation.** Keep the receiving region large enough for the refracted spread as the object or light moves. Clear stale deposits each update. Debug the coverage, transported radiance and combined result separately before bloom, tone mapping and grain.

**Independent controls:** source ray-grid density, receiver-map resolution, trace limit, concentration cap, absorption, light direction and smoothing. Ray count grows with the square of grid width. A larger receiving texture cannot recover paths that were never traced; a denser source grid cannot repair a clipped receiving region.

**Failure checks:** disable the transfer pass; use a near-neutral refractive setup; move and tilt the object; change liquid slope; test a concentrated focus, grazing light and receiver boundaries. Look for double-counted brightness, stale shadows, missing deposits, negative direct-light factors and unstable spikes. Test coverage overlap deliberately. Compare resolution changes with exposure and post-processing fixed. Measure pass timings under motion after warm-up; a refresh-capped frame rate or one displayed statistic is not a benchmark.

**Adapted prompt:** Build [transparent object] over [receiver] with one shared optical state driving its appearance and its light footprint. Expose undeviated coverage and refracted radiance separately, then replace intercepted direct light. Keep ray density and receiving resolution independent. Demonstrate toggling, movement and boundary checks, and label trace limits and concentration stabilizers as approximations.

This complements [causal water materials](build-patterns.md) and [glass-volume art direction](patterns/materials.md#glass-volume). No third-party source or media is bundled.
