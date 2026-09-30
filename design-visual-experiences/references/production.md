# Production: time, sound, performance, and delivery

Use this guide to choose the delivery time model and inspect the audience’s actual output. Read individual sound, contact, accessibility or render-reuse sections only when that work is in scope. [Pattern cards](atlas.md#production) own the reusable mechanisms.

**In this guide:** [Choose the correct time model](#choose-the-correct-time-model) · [Author a chain reaction around contact events](#author-a-chain-reaction-around-contact-events) · [Timing and easing](#timing-and-easing) · [Sound that belongs to the picture](#sound-that-belongs-to-the-picture) · [Audition sound identities before making a pack](#audition-sound-identities-before-making-a-pack) · [Review passes with distinct jobs](#review-passes-with-distinct-jobs) · [Keep live motion responsive](#keep-live-motion-responsive) · [Accessibility without losing the idea](#accessibility-without-losing-the-idea) · [Deliver to the actual destination](#deliver-to-the-actual-destination) · [When two clocks disagree](#when-two-clocks-disagree) · [Review sound identity across projects](#review-sound-identity-across-projects) · [Spend render time on what visibly changes](#spend-render-time-on-what-visibly-changes)

For feature launches and product demonstrations, use [film direction](feature-launch-films.md) before assigning shot timing or selecting production layers.

## Choose the correct time model

**Live UI:** Respond to current state and input. Make transitions interruptible; do not queue decorative animations behind rapidly changing user intent. A spring can preserve velocity when retargeted if the chosen implementation supports it. A fixed easing curve may be simpler for a known transition. See [spring physics](https://www.joshwcomeau.com/animation/a-friendly-introduction-to-spring-physics/).

**Authored film:** Prefer explicit timeline data and a render function evaluated at a requested timestamp. Seed randomness and keep frame evaluation independent of previous calls. Render frame i at i/fps; test repeated timestamps in different orders. [Opus JS Animations](https://github.com/klsoen/opus-js-animations) documents this approach and frame inspection tools.

**Stateful simulation:** Integrate at an appropriate fixed step; render from the current or interpolated state. Export with deterministic replay or cached trajectories. Do not retrofit a pure time function by ignoring the solver's history.

## Author a chain reaction around contact events

Use this for a directed mechanical film whose sequence must land on known frames. [Kwazikot's September 29 Opus 5.5 explanation](https://x.com/Kwazikot/status/2104965124872142993) describes procedural Blender geometry and calculated motion baked into keyframes: gear ratios, rolling distance, gravity and geometric domino triggers. The creator explicitly says it does not use Blender's rigid-body solver. Selected recording frames show staged ramps/gears and a ball at different ramp positions, with upright and toppled domino states. The recording also revisits earlier timeline states, so its playback time is not a continuous machine-time measurement. No code was retrieved and contact correctness was not independently established.

The following method is **original engineering synthesis**:

1. Define an event graph: release, ramp exit, impact, lever release, next impact. Store each event's time, incoming/outgoing object, contact point and local orientation. Derive downstream starts from upstream contacts plus intentional delays; avoid unrelated hand-tuned timestamps. A cyclic mechanism needs a declared period or stateful solver, not a cyclic dependency graph.
2. Fit trajectories to the shared contact conditions. For a simple vertical drop from rest through height `h`, `duration = sqrt(2h/g)`; a zero-height drop needs no division by duration. Use scene-consistent units. If the chosen dramatic duration disagrees with this, adjust the staging or explicitly use authored easing instead of labeling it gravity. Include nonzero initial velocity when present.
3. Couple visible motion to traveled distance. For a ball rolling without slip along a straight ramp, `angle = distance/radius` in radians. Choose the rotation axis from the surface normal and travel direction; curved paths require accumulated orientation. For external gears, the signed angular speeds have inverse tooth-count ratio; choose initial phase so teeth meet. These kinematic relationships do not establish collision or energy accuracy.
4. Bake or evaluate all affected objects from the same event data. At a handoff, the incoming trajectory endpoint and outgoing start must agree spatially. Match velocity for continuous transport; use an intentional velocity change for impact. Avoid automatic smooth interpolation that visibly slows a falling object just before contact or overshoots a stop. Inspect actual interpolated frames, not only key poses.
5. Review just before, at and after every contact, then play at normal speed. Check early domino falls, hovering gaps, penetrations, gear phase and sliding balls. Move a ramp or delay one upstream event and confirm dependent stages update. Scrub backward and request frames out of order to catch hidden state. A predictable film is useful, but it is not evidence that a freely interactive machine will work.

Expose event delays, ramp dimensions, ball radius, tooth counts and camera holds. Use wide framing long enough to establish the causal chain, then reserve close-ups for contacts that are otherwise unreadable. Preserve a contact-review camera while developing the beauty shot. If the viewer can change geometry or add forces, use an appropriate solver or recompute trajectories; a baked sequence must not silently pretend to respond physically.

**Adapted prompt:** Direct a short mechanical chain reaction around a small set of legible contacts. Build a shared event schedule and expose its key dimensions and delays. Derive rolling and gear motion consistently, inspect every handoff, and label authored motion separately from simulated behavior. Make the cause visible before revealing the consequence.

## Timing and easing

Define a small motion vocabulary appropriate to the brand and medium. Distinguish quick feedback, ordinary state changes, larger spatial changes, and expressive moments. Tune durations by distance, content, frequency, and device. [Carbon's motion guidance](https://carbondesignsystem.com/elements/motion/overview/) is a useful concrete system, but its token values and no-bounce style are not universal.

For films, translate tempo into useful event times when music drives the structure: beat duration is 60/BPM seconds. Sync selected important actions; not everything must hit every beat. Reading time, acting, and explanation can override the grid. [JavaScript Animation Skills](https://github.com/iart-ai/javascript-animation-skills) provides an example of shared shot and sound event timing.

## Sound that belongs to the picture

Keep one event schedule for major visible actions and their audio cues. Separate ambience, music, speech, and transient effects so levels can be adjusted independently. Preserve supplied audio according to the brief; do not silently change it. Check headroom, intelligibility, start/end cuts, and tails. Sound should reinforce physical or narrative events rather than cover every movement.

Compare the actual mixed export with the visual at both normal playback and key contacts. Nominally matching durations do not prove synchronization. If sample rate divided by frame rate is not integral, use timestamps or rational arithmetic rather than accumulating rounded samples per frame. Keep captions or a visual explanation when speech carries essential meaning.

For narrated explainers and kinetic type, use [word-anchored cues and retiming checks](narration-cues.md) when changing voice takes must move the related action, camera and sound together.

## Audition sound identities before making a pack

[Amir Mushich's September 27 prompt](https://x.com/AmirMushich/status/2104257004474671129) starts from a muted edit and asks for a small set of dry sound prototypes, an audition reel and a cue sheet before variations. The creator jointly credits “GPT-6 Astra/Sol” without identifying each model's contribution. Opus 5.5 is mentioned as capable, not credited as the production model. The actual prompt was retrieved; its audio was not heard or its export specifications verified in this research pass.

Use this original adaptation when motion needs a distinctive sonic identity:

1. **Choose a few representative events.** Select a small cut, a firm attachment or arrival, and a larger transition from the real edit. Note what each action should feel like and when the visible change becomes perceptible. Start with a few contrasting sound directions; do not generate dozens of near-duplicates before establishing the character.
2. **Compare like with like.** Put each candidate on the same short visual segment with the same cue placement and the same lead-in/tail. Keep unrelated music out of the first comparison. Use comparable audition levels without clipping; identical peak normalization alone does not establish equal perceived loudness. Retain the original files and document audition gain so an apparently better candidate is not merely louder.
3. **Separate character from synchronization.** First choose whether the sound feels soft, granular, rigid, hollow or tactile enough for the object. Then adjust its attack relative to the visual event and review the whole action at normal speed. Use the [perceptual attack alignment pattern](patterns/sound.md#peak-alignment); a waveform peak, sound onset and perceived impact need not coincide. Preserve enough tail to hear whether the material feels right.
4. **Record the reason for the choice.** Keep a compact cue sheet with event ID, film time, sound file/version, gain, offset and a short purpose. Make variations along one meaningful axis at a time, such as shorter decay or denser texture. Limit differences within a family so repeated events share an identity while important events retain emphasis. The creator's dry mechanical style is one direction, not a rule for every project.
5. **Verify the delivered context.** After choosing the palette, audition it with dialogue and music, then check the encoded film. Inspect clipping, abrupt cuts, tails and channel cancellation; listen in mono as well as stereo where relevant. A numeric check can reveal a problem but cannot establish that a sound feels good. If playback cannot be heard, report technical checks only and leave aesthetic preference pending instead of inventing a listening verdict.

**Adapted prompt:** Propose a small, contrasting sound palette for these visual events. Place each candidate against the same excerpt and keep audition gain documented. Provide individual assets and a cue sheet. Explain the intended material and motion relationship, then refine timing and make variations only after a direction has been selected. Distinguish measured audio properties from what was actually heard.

## Review passes with distinct jobs

| Pass | What it catches | What it cannot prove |
|---|---|---|
| Opening / key stills | Hierarchy, composition, material, type | Rhythm or smoothness |
| Contact sheet | Visual consistency and scene progression | Fast-action continuity or audio sync |
| Consecutive-frame strip around a transition | Clipping, pose discontinuities, occlusion | Overall pacing |
| Normal-speed playback with sound | Rhythm, synchronization, readability | Interactive correctness |
| Live controls and repeated use | State, input, interruption, recovery | Export correctness |
| Final-file inspection and playback | Format, dimensions, timing, actual delivery | Quality in every untested environment |

Use a quick preview to solve the visual problem before an expensive full-resolution render. After the final encode, inspect the final file again. Keep a known-good output until the replacement has finished successfully. The [Claude Animation harness](https://github.com/buildwithhanif/claude-animation-skill) illustrates frame strips, deterministic verification, and staged export.

For one-frame flashes, shared-object seams or subframe blur crossing a cut, use [transition QA](transition-qa.md).

## Keep live motion responsive

Prefer transform and opacity for ordinary DOM movement when they fit. Profile the rendering pipeline before selecting costlier effects, and avoid adding `will-change` everywhere. [web.dev](https://web.dev/articles/animations-guide) explains compositing, layout/paint costs, and profiling.

Reduce render resolution or expensive scene work based on measured need. Stop or reduce unnecessary work when the experience is hidden, and clean up observers, animation loops, listeners, and GPU resources on teardown. For libraries with breakpoint helpers, check their cleanup semantics; [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/) supports responsive and reduced-motion animation contexts.

## Accessibility without losing the idea

Honor reduced-motion preferences for nonessential movement. Replace large parallax, zooms, and repeated motion with stable compositions, direct state changes, or restrained alternatives that preserve the information. Keep controls operable by the relevant input methods and expose meaningful labels or explanations outside an inaccessible canvas when needed.

Provide pause/stop/hide for qualifying automatically moving content presented alongside other content. [WCAG 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) is Level A and includes specific conditions and exceptions. [Animation from Interactions, 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) is Level AAA; do not misstate it as a blanket Level AA requirement. Reduced motion is a design behavior, not proof of complete accessibility conformance.

## Deliver to the actual destination

Verify requested dimensions/aspect ratio, duration, frame rate, file type, sound, and loop behavior. Check safe areas and readable type in the final crop. Do not blindly crop a horizontal composition into vertical; recompose when it changes the focal hierarchy.

For websites or apps, show the running result and summarize tested paths. For a film, deliver the playable export with editable source and relevant credits. State constraints plainly: “repository reviewed,” “frames inspected,” “controls tested,” and “export played” describe different evidence.

## When two clocks disagree

Use [timing and presentation contracts](timing-and-presentation.md) for retained musical pickups, downbeat alignment, frame scrubbing and labels that must match the image actually on screen.

## Review sound identity across projects

[Mort1d's September 28 release post](https://x.com/Mortid_X/status/2104644829846397171) explicitly teaches a workflow for Opus 5.5. Its [pinned sound-comparison code](https://github.com/Mort1d/motion-graphics-skills/blob/63930a9fa7093601f64eed7c282b242ae1d1486a/skills/motion-graphics/assets/template/tools/sound-print.mjs) measures rhythmic, spectral and tempo similarity against earlier scores. Selected analysis/comparison/cache code was read; no audio was auditioned and the tool was not executed. See [evidence and limits](updates/2026-09-30-sound-identity.md).

Use this original adaptation when several films keep feeling like the same template:

1. **Decide what should repeat.** A campaign may intentionally retain a musical motif or sound material. Record that invariant and the dimension that should change for this story: pulse, texture, density, register or the distribution of silence. Difference alone is not the goal.
2. **Compare a small, explicitly chosen set.** Include the template score and a few relevant prior outputs the user has authorized for this project. Compare music separately from voice and effects where stems exist; a shared narrator should not automatically imply a reused score. Do not scan unrelated folders as a side effect of a design review.
3. **Treat metrics as questions.** Similar pulse positions invite a rhythm review; a similar spectrum invites a timbre review. Prefer known timeline tempo, label estimates, and check half/double-time ambiguity. Separate music sections before comparing when an averaged measure hides a quiet opening and dense ending. Low similarity does not prove novelty, licensing, emotional fit or good synchronization.
4. **Change a meaningful dimension, then listen.** Make two short alternatives over the same scene, preserving the narrative cue and using documented audition levels. Compare in context and with picture hidden. An analyzer can shortlist passages, but do not claim heard quality from spectra or waveforms. If audio inspection is unavailable, keep the result explicitly provisional.
5. **Make analysis reproducible.** For an original analyzer, record the selected files, content hashes, analysis version, tempo source and settings. Recompute when content changes; path, size and modification time alone can miss a replaced file. Use similarity thresholds as locally calibrated review triggers, never universal pass/fail taste rules.

**Checks:** a volume change should not masquerade as a new sound identity; silence and very short clips need an insufficient-evidence result; tempo estimates deserve confidence labels; intentionally recurring motifs must remain possible. Listen to encoded deliverables after mixing changes. A score can pass a difference check and still be wrong for the film.

**Adapted prompt:** Give this [motion piece] a sound identity that supports [story/emotion]. Preserve [intentional series motif], vary [chosen dimension], and compare against [approved references]. Offer two short alternatives aligned to the same scene. Report measured similarity separately from what was heard; choose for fit, not maximum numerical difference.

For films that will be revised in an editor, use [editable motion handoff](editable-motion-handoff.md): native items versus rendered layers, source-time mapping, retained placement and explicit conversion losses.

## Spend render time on what visibly changes

[A September 28 Opus 5.5 production article](https://x.com/0xInsiderf5/article/2104648908370792673) describes measuring scene preparation and effect costs, rendering backgrounds once, separating moving props, and using depth to reproject camera moves. The creator also distinguishes the raw film from an earlier cut with three GPT Image replacements. These are creator-reported workflow details; source code and render timings were not inspected. Only selected raw-clip frames were seen. See [evidence and limits](updates/2026-09-30-render-reuse.md).

Original adaptation for short films with expensive scenes:

1. **Measure a representative shot before committing the whole film.** Time scene preparation, rendering and compositing separately. Compare a small preview with and without the suspected expensive effect while holding the camera and scene fixed. Lower sample count may barely help when scene setup dominates. Record the actual preview configuration and visible compromise; do not copy another machine's timings as a budget.
2. **Partition by change and dependency.** Separate stable background, moving subject/props, foreground occluders, text and sound when their interactions allow it. Retain depth and masks where useful. A moving hand may change shadows, reflections and occlusion on the background, so independence must be demonstrated. Render a coupled group together if separating it creates an obvious mismatch.
3. **Set a limited camera range for reused plates.** A depth-backed image can support restrained camera movement, but it contains no view of surfaces hidden in the original render. Test the furthest intended camera positions early. Look for revealed holes, stretched edges, doubled silhouettes, wrong parallax, stale highlights and foreground overlap errors. Reduce the move, add a separate layer or render another view when the plate cannot supply the missing information. Do not promise arbitrary orbit from one frame.
4. **Treat render passes as deliverables.** Confirm that depth, color, alpha and masks were actually written, have matching dimensions and camera metadata, and are interpreted in the expected spaces. Inspect a simple diagnostic composite before producing all frames. File existence alone does not prove a usable pass. Changes to geometry, lighting, camera or pass settings must invalidate the affected cached layers.
5. **Make progress recoverable.** Save the shot specification and completed outputs after each meaningful unit of work. Establish the actual environment's process lifetime rather than assuming every sandbox restarts between turns. Retain completed shots if a render stops; validate them before resuming missing work. A failed background process should not force rebuilding the art direction.

**Tune and check:** preview scale, sample count, costly effect toggles, camera displacement, overscan, layer grouping and invalidation keys. Compare the reconstructed frame at the start, largest camera move, prop contact and ending against an appropriate full-scene reference. Review normal-speed playback for drifting shadows, edge shimmer and layer timing. Render reuse is successful when it preserves the intended visible result, not merely when it lowers elapsed time.

**Adapted prompt:** Build [film] around an early representative preview. Measure where rendering time goes, identify which scene elements can be reused, and retain the passes needed to composite them. Limit camera movement to what the available geometry and plates support. Prove the hardest occlusion/contact and camera extreme before rendering every shot, and preserve validated outputs for recovery.
