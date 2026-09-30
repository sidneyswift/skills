# Worked implementation notes

Sections preserve concrete mappings, code snippets and source-specific observations. Keep the applicable pattern’s contract while adapting these examples.

**In this guide:** [1. A persistent object with elastic transformations](#1-a-persistent-object-with-elastic-transformations) · [2. Kinetic typography with designed hierarchy](#2-kinetic-typography-with-designed-hierarchy) · [3. Painterly motion: two clocks, one coherent subject](#3-painterly-motion-two-clocks-one-coherent-subject) · [4. Water: make optical layers agree](#4-water-make-optical-layers-agree) · [5. Improve simulations through causal criticism](#5-improve-simulations-through-causal-criticism) · [6. Printmaking as a rendering system](#6-printmaking-as-a-rendering-system) · [7. Shared state makes spectacle believable](#7-shared-state-makes-spectacle-believable) · [8. Continuous transitions need resource and timing discipline](#8-continuous-transitions-need-resource-and-timing-discipline) · [9. Storyboards and assets as production inputs](#9-storyboards-and-assets-as-production-inputs) · [A reusable implementation prompt](#a-reusable-implementation-prompt) · [Glass under camera motion](#glass-under-camera-motion) · [Brush gestures and an animated wash](#brush-gestures-and-an-animated-wash) · [Traveling font weight](#traveling-font-weight)

Read a selected section only when the [canonical pattern card](atlas.md) needs more implementation detail; this workbook is not a second mechanism catalog. Source statements below came from retrieved creator text or inspected source; they do not certify every video. **Build, tuning, and checks are this skill's original synthesis.** Numeric suggestions are starting points, not universal rules or claimed creator settings. Select one main mechanism, build it, observe it, then tune.

## 1. A persistent object with elastic transformations

**Evidence.** [Twoclipping's morph post](https://x.com/twoclipping/status/2103273003555402193) describes a continuous object, different springs for its edges, direct manipulation during drag, release dynamics, independent text masks, and seekable timing. The full post was retrieved; its video was not reproduced.

**Build.** Keep identity, anchor, and semantic state while changing geometry. Represent each target change as an event. Superpose the response to each target delta, so a new command does not restart velocity at zero. For a rectangle, calculate left and right edges with different damping or frequency; reconstruct center and width afterward. Preserve minimum width if overshoot crosses the edges. While held, the control should follow the pointer; on release, initialize the spring with measured velocity. Smooth noisy pointer velocity and cap extreme impulses.

```js
import {targetTrack, release} from '../assets/motion-kernel.mjs';
const changes = [{time: .4, value: 180}, {time: .65, value: 40}];
const leading = targetTrack(t, 0, changes, 13, .78);
const trailing = targetTrack(t, 0, changes, 10, .86);
// After release, in the same coordinate system:
const x = release(timeSinceRelease, grabbedX, releaseVelocity, targetX, 12, .8);
```

**Tune.** Start with damping .75–.9; increase frequency for quicker settling. Keep edge lag small before increasing bounce. Separate exiting and entering labels instead of distorting glyphs with the container. For many ribs or points, spread a small total delay across the form rather than delaying each point by a large constant.

**Check.** Retarget three times during movement: no position jump, no sudden stop, no inverted geometry. Release after a fast and slow drag: their first motion must differ. Test at the middle of each morph, where endpoints alone hide tangles. The [worked study](worked-study.md) exercises this mechanism with an original visual treatment.

## 2. Kinetic typography with designed hierarchy

**Evidence.** [TechHalla's prompt reply](https://x.com/techhalla/status/2103411247618146715) specifies type roles, per-glyph timing, restrained print offsets at impacts, masks between phrases, camera accents, and beat stills. These are design decisions beyond “animate the text.”

**Build.** Assign roles before fonts: primary statement, interruption, annotation. Lay out each phrase as a readable composition first. Animate a phrase's mass, then add internal glyph delay where it reinforces speech or rhythm. Use the outgoing word's contour as the next reveal mask to give the transition a reason. Tie camera emphasis and registration error to one impact envelope; leave quiet holds genuinely still.

**Tune.** Original starting plan: a 6-second phrase uses .4s preparation, .7s entry, 1.8s hold, .5s transition, and remaining time for the next phrase. Adjust to reading length and audio. Try total glyph spread .15–.4s; do not let long text accumulate seconds of delay. Keep accent offsets tiny relative to cap height.

**Check.** Mute it: can the message be read? Freeze impact: is hierarchy intact? Remove the camera accent: if the sequence becomes incomprehensible, fix blocking. Test the longest actual phrase, not placeholder text. Do not copy a reference's colors or font count as universal rules.

## 3. Painterly motion: two clocks, one coherent subject

**Evidence.** [Yuma's full prompt](https://x.com/yumaeriel/status/2103053172235264150) separates a stable underlying character from repainting marks and asks for slower paint updates than camera motion. It is a prompt specification, not proof of the renderer's implementation.

**Build.** Use continuous time for pose and camera; quantize only the paint variation. Seed marks by object ID, stroke ID, and paint tick. Put marks in the object's local coordinates, so the texture follows the turning face or limb. Vary existing strokes gently rather than replacing the silhouette with random noise. Direct brush orientation along form: cheek plane, sleeve fold, hair flow.

```js
import {paintTick, hash} from '../assets/motion-kernel.mjs';
const tick = paintTick(t, 12);
const strokeJitter = (hash(strokeId * 8191 + tick) - .5) * 1.4;
// Apply jitter to local stroke geometry after constructing coherent anatomy.
// Pose and camera still use continuous t.
```

**Tune.** Begin with 10–15 paint updates per second and sub-pixel to 2px variation at delivery resolution. Start with an unmoving camera and one readable gesture. Let light/shadow colors define the planes before adding surface noise.

**Check.** Pause on neighboring frames: can the same face, joints, and clothing folds be tracked? Scrub backward: same time yields the same marks. If a stationary subject crawls aggressively, reduce jitter or preserve more marks between ticks. Avoid full-screen noise as a substitute for painted form.

## 4. Water: make optical layers agree

**Evidence.** [Clearwater source at the inspected revision](https://github.com/Aureliengmz/clearwater/blob/4bc826134321043a25df3c2b6fed16fb7b9241e8/index.html) contains wave normals, refraction, Fresnel reflection, sun highlights, depth absorption, caustics, and local ripples. Its live demo was opened and a tap produced visible rings; frame rate and mobile behavior were not measured.

**Build.** Establish bottom geometry and depth first. A shared surface height/normal field must drive reflected direction, refracted lookup, and local ripple response. Layer bottom lighting, depth attenuation, transmitted light, reflection, and highlights deliberately. Debug with switches for normals, depth, refraction, caustics, reflection, and particles. Use a correctly transformed input hit point in water coordinates.

For light transferred through a moving vessel, see [refracted-light footprints](refracted-light-footprints.md): shared optical state, concentration and replacement of intercepted direct light.

**Tune.** Begin with mild wave slope, then adjust absorption and highlight roughness independently. Increase ripple amplitude until visible without destabilizing refraction. Add foam or particles only when the water already reads. Keep an explicit quality scale for simulation and output resolution.

**Check.** Tap near the edge and center; resize and repeat. Ripples must begin at the touched location. Turn off caustics: depth and material should remain legible. Turn off reflection: the floor should not slide arbitrarily. Inspect dark areas and grazing angles as well as the attractive center.

## 5. Improve simulations through causal criticism

**Evidence.** [Dan Greenheck's prompt chain](https://x.com/dangreenheck/status/2102911556296052788) records multiple fixes to water, foam, terrain, artifacts, and performance. The useful lesson is iterative diagnosis; it is not a one-prompt recipe. [The fluid prompt](https://x.com/theailoser/status/2102565612874596411) describes separate velocity, pressure, and dye fields with projection.

**Build.** Decide what drives what. For an incompressible fluid sketch: advect velocity → apply input forces → compute divergence → solve pressure → subtract its gradient → advect dye. Keep read/write buffers separate. For water foam, generate where the chosen model predicts breaking or contact, then age and dissipate it. Do not paint unrelated white noise over the entire surface.

**Tune.** First tune input radius and force, then velocity dissipation, then dye dissipation. Change one group at a time. Solver iteration count is a quality/cost variable; measure it on the actual target rather than inheriting a large number from a showcase.

**Check.** With input off, energy should decay or remain bounded according to the model. Resize without stale buffer dimensions. Repeated reset must return to a clean state. When an effect looks wrong, write a causal note: “foam appears before impact,” “dye teleports on resize,” or “pressure artifacts persist at borders.” A label like “more realistic” does not locate the repair.

## 6. Printmaking as a rendering system

**Evidence.** Riso Windowseat's [live-plate implementation notes](https://github.com/sevenevesai/riso-windowseat/blob/1275fdaf81eb1817b729ee69cbf7b6b6fe535a4e/docs/live-plates.md) describe coverage masks screened into ink dots and composited on paper. Its [motion notes](https://github.com/sevenevesai/riso-windowseat/blob/1275fdaf81eb1817b729ee69cbf7b6b6fe535a4e/docs/motion.md) distinguish stable randomness from continuous motion. Source documents were inspected; the complete film was not rendered here.

**Build.** Draw each ink's continuous coverage mask. Blur coverage for soft light, then threshold against a stable page-space dot pattern. Composite the resulting ink layers on paper, often with multiply. Keep the screen anchored to the page while content moves through it. For luminous objects at night, first open a light region in the dark ink, then add colored glow coverage; adding bright multiply ink alone cannot lighten darkness.

**Tune.** Choose a small ink palette and dot spacing at final resolution. Test registration offset at zero before adding imperfection. Cache stable backgrounds and bound expensive mask work to the active area. Do not assume multi-plate high-resolution blur runs in real time.

**Check.** Scrub slowly: dots stay pinned; silhouettes move. Blur should not smear the dot screen. Inspect overlap and dark scenes. For moving characters, solve positional and velocity continuity separately from random stability. A deterministic animation can still pop at every scene boundary.

## 7. Shared state makes spectacle believable

**Evidence.** [AGIOyaZ's cathedral brief](https://x.com/AGIOyaZ/status/2103145567945986461) calls for coordinated stained-glass imagery, light beams, and projected floor light during a staged reveal. [The cake-cutting prompt](https://x.com/ImaStudio_ai/status/2104517586092458039) describes deformation and new physical pieces after cuts.

**Build.** For projected light, maintain one image, mask, and reveal-progress state; sample or transform it into window, beam, and floor layers. For deformable cutting, distinguish visual slicing from actual topology/state changes. Start with one deformable body and one cut. New pieces inherit appropriate position, deformation, and velocity. Make cutting, grabbing, and camera orbit mutually exclusive input modes.

**Tune.** Cathedral: stage a readable silhouette before releasing light; adjust exposure before adding bloom. Physics: tune stiffness and damping on one body before increasing piece count. Select a solver appropriate to the desired illusion and performance; a creator's named solver is not mandatory.

**Check.** Change the source mask: all projected manifestations must change coherently. Make a second cut on an already cut piece: it should act on current state. Reset after several operations and confirm no orphan bodies or forces. If stats are shown, derive them from the simulation rather than decoration.

## 8. Continuous transitions need resource and timing discipline

**Evidence.** [Twoclipping's launch-film post](https://x.com/twoclipping/status/2103835273813496100) combines persistent shapes, masks, glass distortion, iris geometry, and imported media. The description includes assets; do not interpret “code-made” as asset-free.

**Build.** Give each transition a carried element: the same contour, color mass, or image region. Maintain a transition state that both scenes read. For glass, build a displacement field matched to the lens geometry; use a reference clone when that renderer needs one, then verify alignment. For an iris, animate blade geometry and overlap. When sampling video at exact times, wait until the decoder has sought before capturing.

**Tune.** Separate motion geometry from material strength. First run glass with zero displacement and verify the image lines up; then increase distortion. First run the iris without motion blur and check coverage. If using subframes, accumulate samples from a deterministic time function.

**Check.** Scrub both directions. Test first/last frames and corners for uncovered pixels. A loop needs matching value and velocity, not simply a duplicate final frame. Test the actual renderer: claims about browser filter limitations are context-specific, not universal facts.

## 9. Storyboards and assets as production inputs

**Evidence.** [Rexan's workflow](https://x.com/rexan_wong/status/2103707054108299437), [Leo's account](https://x.com/leodev/status/2102781872107659270), and [Donald's production post](https://x.com/donaldjewkes/status/2102801274173587569) describe references, brand inputs, iterations, component reuse, or generated assets. Attribution is creator-reported and these workflows use different tools.

**Build.** Give the agent actual product components and approved assets. Specify a scene's purpose, focal object, entry state, action, exit state, and transition. Reserve negative space for captions before generating footage. Make character/set sheets for repeated generated scenes, track asset provenance, and choose an export path early. For a short film, inspect representative stills before costly full rendering, then inspect motion and audio after rendering.

**Tune.** Ask for distinct treatments when the direction is unresolved; once selected, issue local director notes. Example: “The product arrives at 1.8s but its label stays obscured until 2.5s; move the covering shape earlier and hold the label before the cut.”

**Check.** Verify the real product UI, not an attractive approximation. Review continuity, captions, music edits, and final encoding. One-frame approval cannot certify the film. A reference's permission to spend freely or call a media provider does not authorize this project.

## A reusable implementation prompt

Use the [compact visual brief](briefs-and-review.md#a-compact-visual-brief), then name the selected mechanism and its failure check. For multi-mechanism work, use the [composition method](compositions.md#combine-mechanisms-beyond-these-examples). Prompts there are original adaptations.

## Glass under camera motion

Use with [glass volume](patterns/materials.md#glass-volume) when a moving lens or translucent type crosses a moving scene. [Twoclipping's prompt](https://x.com/twoclipping/status/2103835273813496100) describes a separate background copy and shape-derived displacement. Selected original/remake playback was inspected; [evidence and limits](updates/2026-09-29-glass.md) distinguish visible treatment from unverified renderer claims.

The following mapping and tests are original engineering synthesis:

- **Share time and coordinate space.** Evaluate the background, camera and lens from the same time value. For a 2D affine camera, let `L(t)` map lens-local points into scene coordinates, and `C(t)` map scene coordinates into the background render target's pixels. A lens point `q` samples `p = C(t) L(t) q`. Normalize `p` by the target dimensions only at the texture lookup; do not apply the camera transform again to that already-rendered background.
- **Name displacement units.** Add a screen-pixel displacement after the mapping above, or transform a scene-space displacement through the camera's linear part. These give different behavior under zoom. Choose deliberately; a fixed pixel rim stays screen-sized while a scene-space rim grows with its object.
- **Start with a zero-distortion test.** Disable offsets, tint, blur and rim. Move the lens and zoom/pan the camera over a checkerboard. The interior should match the background exactly. A sliding image means the sampling transform or crop is wrong; stronger refraction will only conceal the error.
- **Declare the layers.** Render the scene behind the glass first, sample it into the glass, then draw crisp labels and foreground objects. Keep the glass out of its own source buffer. For overlapping panes, decide whether the upper pane samples the lower one; a shared pre-glass snapshot and sequential compositing produce different results.
- **Keep shape cues coherent.** Derive the visible mask, displacement falloff and rim from the same changing contour. Inspect thin letter strokes and rounded corners while morphing. Excessive offsets can turn a readable letter into a bright outline with no legible interior.

**Failure checks:** camera-only motion, lens-only motion, simultaneous movement, two overlapping lenses, resize/device-pixel-ratio change, and arbitrary-time seeking. Inspect zero-distortion registration before comparing the final material. Test sampled source pixels outside the render target; choose padding or clamping deliberately to avoid stretched edge streaks.


## Brush gestures and an animated wash

For [distance-spaced brushes](patterns/materials.md#distance-spaced-brush), the stroke boundary can be a material event. In [Moyun's inspected pointer code](https://github.com/axtonliu/moyun/blob/eb488acf811122bb9a574d87fb148ffa42ed4c23/index.html), pointer-down initializes ink load; travel consumes it. Water injects wetness and motion separately from black pigment. Selected live observations are recorded in the [ink update](updates/2026-09-29-ink.md).

**Original adaptation:** keep a stroke record with pointer ID, last position/time, smoothed speed, remaining ink and a stable bristle seed. Refill on a new stroke if that suits the medium. Use travel distance to consume ink; a pause should not drain the reservoir unless soaking is deliberately modeled. Process coalesced samples in order, and make cancellation end the stroke cleanly.

Treat washing as an operation with an explicit owner. The inspected implementation runs a swirl and clears pigment after roughly 1.9 seconds, while its pointer handlers can still enqueue marks. When adapting that mechanism, choose whether drawing interrupts the wash or stays disabled until it finishes. Do not let an old completion callback clear a newly started drawing: invalidate the wash generation when a new operation supersedes it. An automatic painter should similarly release control when the user takes over, unless simultaneous painting is intentional.

**Check:** one continuous long stroke versus two shorter strokes with a lift; cancellation followed by a new stroke; drawing during wash; repeated wash/start actions; and water over a previously retained mark. Observe both what moves and what remains. A frame-rate label on a demo is not a measured performance result.


## Traveling font weight

Use with [weight as action](patterns/type.md#weight-as-action). The [original/remake study](updates/2026-09-29-weight-wave.md) shows mixed thin/heavy letters and a later wider word. A screenshot does not establish a real variable-font implementation. The following recipe is original engineering synthesis:

- **Separate three controls.** Use one finite action envelope, delayed by glyph index, for local weight. Keep overall word expansion and tracking on their own curves. This lets a pressure wave travel across a word without every letter following an unrelated animation. Reverse the phase order to reverse the wave; change the delay to change its travel rate.
- **Choose the footprint intentionally.** For a fixed editorial composition, reserve space for the maximum extent across the axis range and mixed-weight states. Anchor the word to a baseline plus a chosen left, center or right reference. For an expanding word, animate the footprint deliberately and give neighboring content space. Avoid recomputing a fit-to-width scale every frame: that can cancel the intended weight change and make the whole word pump.
- **Use actual font metrics.** Confirm the font and supported axis, then measure advances, kerning and visible ink bounds at representative weights. Weight, width and tracking are different variables. Keep tight pairs from colliding as their outlines thicken. Isolated glyph spans can lose shaping and kerning; for connected scripts or ligatures, preserve shaped runs or choose another treatment instead of blindly splitting characters.
- **Keep annotations honest.** If the art direction includes a bounding box, rulers or axis readout, derive them from the same evaluated state as the glyphs. Decide whether the box depicts layout advances or visible ink bounds. Label it accordingly; a decorative rectangle should not masquerade as a measurement. Draw fine annotations after broad glow so the diagnostic layer stays legible.
- **Check the transition, not only endpoints.** Review the narrow state, mixed-weight peak, widest state and exit into the next scene. A word that fits at its light and heavy endpoints can still collide during a staggered transition. Compare with glow disabled, at final crop and delivery size. Keep a deliberate reading hold before replacing the word with another focal event.

**Adapted prompt:** Make a controlled wave of weight travel across [word], then let the whole word expand for emphasis. Keep weight, tracking and footprint as separate controls. Choose one anchor, preserve readable shaping, and measure the worst mixed state. If you show bounds or axis values, derive them from what is actually rendered.
