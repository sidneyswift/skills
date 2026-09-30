# Materials patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [Slow paint marks on smoothly moving geometry](#paint-clock)
- [Ink that dries, settles and can be re-wetted](#wet-dry-ink)
- [A brush that stays consistent at different event rates](#distance-spaced-brush)
- [A mosaic whose pieces become moving figures](#tile-flock)
- [Glass whose shape is readable through distortion](#glass-volume)
- [Change style while preserving object identity](#material-swap)
- [Rain and wet surfaces that belong to the scene](#lit-rain)
- [Stable toon outlines from geometry buffers](#outline-normal-depth)

- [A glossy spike field reaches toward an attractor](#attractor-spike-field)

<a id="paint-clock"></a>

## Slow paint marks on smoothly moving geometry

**Mechanism:** The subject remains coherent while the surface redraws at a lower cadence.

**Build:**

1. Animate the underlying pose and camera continuously.
2. Quantize a separate texture clock and seed brush variation by stroke ID and texture tick.
3. Orient strokes to local form, then composite them under consistent lighting.

**Tune:** Begin around 10–15 surface updates per second as a stylistic trial, not a universal rule. Keep large shape changes independent.

**Failure check:** Freeze the pose while time advances. It should look redrawn, not like the anatomy is melting.

**Adapted prompt:** Paint [subject] with stable form and a slower handmade surface rhythm. Preserve silhouette and lighting through motion.

**Evidence:** [@yumaeriel](https://x.com/yumaeriel/status/2103053172235264150), [@GroundControl](https://x.com/GroundControl/status/2103679486629659063). Creator description/prompt; verify the visual when fidelity matters.


<a id="wet-dry-ink"></a>

## Ink that dries, settles and can be re-wetted

**Mechanism:** Wet pigment and settled pigment behave differently, giving the medium memory.

**Build:**

1. Maintain separate fields for mobile pigment, water and deposited pigment.
2. Transport the wet fields, evaporate water, and transfer pigment into a settled layer.
3. Re-wetting should mobilize only a controlled fraction of deposited pigment.

**Tune:** Tune drying time, diffusion and paper anisotropy separately. Start at low simulation resolution before adding fibers.

**Failure check:** Paint slowly, quickly, then add water to a dry stroke. Each action should have a distinct repeatable effect.

**Adapted prompt:** Make [ink medium] respond to speed, drying and re-wetting. The marks should retain a history of how they were made.

**Evidence:** [@AxtonLiu](https://x.com/AxtonLiu/status/2103288413969621231). Selected code and live brush/water behavior inspected; see [observations and limits](../updates/2026-09-29-ink.md).


<a id="distance-spaced-brush"></a>

## A brush that stays consistent at different event rates

**Mechanism:** Stamp spacing follows traveled distance, so a slow device does not create dotted strokes.

**Build:**

1. Accumulate path distance between pointer samples.
2. Insert stamps at fixed spacing relative to brush radius.
3. Normalize deposited pigment by spacing and reduce ink load with travel distance.
4. If lifting reloads the brush, reset its load at the start of each stroke, not on every move event. Clear the gesture on release, cancellation and lost capture.

**Tune:** Use speed to shape width, with smoothing that preserves sharp turns. Keep bristle texture anchored across the stroke normal.

**Failure check:** Draw the same path at different input rates. Coverage should remain comparable and corners should not leave gaps.

**Adapted prompt:** Build a [brush] whose width and ink respond to gesture speed while coverage remains stable across pointer sampling rates.

**Evidence:** [@AxtonLiu](https://x.com/AxtonLiu/status/2103288413969621231). Selected code and live brush/water behavior inspected; see [observations and limits](../updates/2026-09-29-ink.md).


<a id="tile-flock"></a>

## A mosaic whose pieces become moving figures

**Mechanism:** Persistent tile identities connect a flat image to articulated movement and back.

**Build:**

1. Give every tile a home transform and a figure-local transform.
2. Blend groups into the moving figure while preserving its silhouette.
3. Return each tile to its own home location with a spatially ordered settling wave.

**Tune:** Control flock noise below the silhouette scale. Separate highlight intensity from base-color contrast.

**Failure check:** Inspect the figure in flight and edge-on tiles during flips. Avoid a moment where the entire composition disappears.

**Adapted prompt:** Let parts of [mosaic] lift into [creature/action] and settle back into their original positions without losing the figure shape.

**Evidence:** [@LCSlates](https://x.com/LCSlates/status/2102503028859211905), [@LCSlates](https://x.com/LCSlates/status/2102503030469833168), [@dfeinition](https://x.com/dfeinition/status/2102436001473786054). Creator description/prompt; verify the visual when fidelity matters.


<a id="glass-volume"></a>

## Glass whose shape is readable through distortion

For moving cameras and overlays, see [sampling alignment and layer order](../build-patterns.md#glass-under-camera-motion).

**Mechanism:** Refraction, edge response and thickness must agree with the same surface.

**Build:**

1. Start with a signed distance or mesh normal field.
2. Use the normal to offset a background sample and use thickness to modulate absorption.
3. Add a restrained edge highlight and verify the center remains transmissive.

**Tune:** Increase distortion only until volume reads; do not let chromatic separation become an unrelated rainbow outline.

**Failure check:** Move the object over stripes and text. Distortion should follow surface orientation and stay continuous at joins.

**Adapted prompt:** Create [glass form] whose refraction and highlights explain its volume against a deliberately structured background.

**Evidence:** [@twoclipping](https://x.com/twoclipping/status/2103835273813496100). Creator description/prompt; verify the visual when fidelity matters.


<a id="material-swap"></a>

## Change style while preserving object identity

**Mechanism:** A shared rig or geometry survives changes in shading, line work and texture.

**Build:**

1. Define identity invariants: silhouette, proportions and key marks.
2. Make material style a separate renderer layer or skin.
3. Transition the environment and subject treatment with a clear order while holding pose continuity.

**Tune:** Change only a few style dimensions per world; keep a recognizable color or accessory across all states.

**Failure check:** Compare a lineup at the same pose. If the character appears redesigned rather than restyled, restore the invariants.

**Adapted prompt:** Take [character/object] through [styles] using one consistent design and motion rig. Let rendering change while identity stays fixed.

**Evidence:** [@pradeepXkapoor](https://x.com/pradeepXkapoor/status/2103176289482154373), [@pradeepXkapoor](https://x.com/pradeepXkapoor/status/2103099194693271874). Creator description/prompt; verify the visual when fidelity matters.


<a id="lit-rain"></a>

## Rain and wet surfaces that belong to the scene

**Mechanism:** Drops, splashes and reflections respond to existing lights and surfaces.

**Build:**

1. Place rain at several depths with shared wind direction.
2. Tint or brighten drops as they enter local light volumes.
3. Spawn splashes at receiving surfaces and reflect only plausible nearby light sources.

**Tune:** Use density, shutter length and exposure together. Keep the subject visible beneath the weather.

**Failure check:** Turn a light off and inspect its rain and reflection. Both should change with it; rain must not pass through solid awnings.

**Adapted prompt:** Add rain to [scene] using its own lights, depth layers and shelter geometry so the weather feels physically present.

**Evidence:** [@yangfei33113](https://x.com/yangfei33113/status/2102611841122017632), [@minosdevs](https://x.com/minosdevs/status/2103112948478570675). Creator description/prompt; verify the visual when fidelity matters.


<a id="outline-normal-depth"></a>

## Stable toon outlines from geometry buffers

**Mechanism:** Contours and creases need different detection rules to avoid noisy diagonal edges.

**Build:**

1. Render depth and normals to intermediate targets.
2. Detect silhouettes from depth discontinuity and internal creases from normal change.
3. Scale line width in screen space and composite before text and interface layers.

**Tune:** Tune thresholds at grazing angles; high depth sensitivity often invents stripes on smooth faces.

**Failure check:** Rotate the object slowly, including oblique views. Edges should remain coherent without internal crawling or hidden-object outlines.

**Adapted prompt:** Give [3D object] a clean illustrative outline with stable exterior weight and quieter internal seams.

**Evidence:** [@op7418](https://x.com/op7418/status/2104085539419021491). Creator description/prompt; verify the visual when fidelity matters.


<a id="attractor-spike-field"></a>

## A glossy spike field reaches toward an attractor

**Mechanism:** Ferrofluid-inspired surface: stable peak centers share one continuous height field; a bounded attractor envelope changes local height while reflections reveal connected valleys.

**Build:**

1. Place fixed peak centers on a hexagonal grid inside a dish; use one tessellated surface and a smooth edge mask.
2. Blend smooth radial peak kernels into that surface, varying their amplitudes with a bounded distance-to-attractor envelope. Treat this as authored geometry, not magnetic fluid physics.
3. Compute normals from the same height field; stage broad white reflections and one warm rim before increasing surface detail.
4. Separate field motion from camera motion; use deterministic time or a stable input filter, then inspect flat rest, tall peaks, reversals and edge contact.

**Tune:** Peak spacing and radius, tip sharpness, rest height, attraction gain and width, rim margin, roughness, light-card size; start with a fixed camera.

**Failure check:** Zero gain preserves the regular field; zero height produces a flat surface with upward normals; attractor at a peak stays finite. Check mesh resolution at maximum height and prevent rim/sphere intersections. No physical accuracy or seamless-loop claim.

**Adapted prompt:** Create a responsive sculpture of glossy dark peaks in a shallow ceramic dish. A restrained moving attractor lifts a local cluster while the base stays continuous. Establish one clear silhouette and broad readable reflections. Expose attraction width, peak height and sharpness; include a static state. Use an authored approximation and label it accordingly.

**Evidence:** [@gogu_name](https://x.com/gogu_name/status/2104736947822645622). September 29 creator explicitly credits GPT-6 Astra + Three.js + Remotion. Original recording played and selected frames inspected, including 4.89s rounded/pointed field, 9.33s red sphere with tall local peak, and end field. No creator code or prompt available; height-field method is original synthesis, not inspected implementation. Audio, physics, performance, live input and loop seam unverified.

### A concrete authored approximation

Use coordinates `(x,z)` on the dish and fixed peak centers `c_i`. One starting shape is `K_i = exp(-(|q-c_i|/r)^p)`, with `p > 1` so the tip has a defined zero gradient. Values near 1 sharpen the rounded apex but require finer tessellation; values near 2 produce softer mounds. Modulate each amplitude with `a_i = h_rest + gain * exp(-|c_i-attractorXZ|² / width²)`, keeping width positive and gain bounded. Form `H(q) = edge(q) * sum(a_i*K_i(q))`. The sum can exceed a single peak amplitude when kernels overlap: check its actual maximum against the sphere and dish clearance instead of assuming the gain is the maximum surface height. This is a design construction, not a recovered creator formula.

Use a smooth radial edge mask that reaches zero with zero slope before the rim. For a mesh parameterized as `(x,H,z)`, derive the normal as `normalize(-dH/dx, 1, -dH/dz)`; central differences are a simple starting point. Reduce the difference step and increase tessellation together until highlights stop changing materially. A coarse mesh with a sharp kernel produces crawling specular facets. Keep peak spacing stable and animate amplitude, width or the attractor path before adding positional wobble.

Block out three readable phases: regular field, locally softened mounds, then a concentrated reaching peak. Those states were visible in the source; this proposed staging and its equations are synthesis. Design independent envelopes for base height, sharpness and attraction strength. If exporting by frame, evaluate time directly rather than accumulating per-frame displacements. For pointer input, map into the dish plane and use a time-based response; do not imply the source was interactive.

Use a broad white reflection to show each peak and one warm edge reflection to join the valleys. Tune the geometry in a neutral material before reflective polish. Avoid adding noise to hide silhouette defects. This single-valued height surface cannot represent overhangs, pinch-off droplets or a real magnetic-fluid volume; choose a different representation if those are the defining behavior.
