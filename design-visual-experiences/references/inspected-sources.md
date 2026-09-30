# Inspected source implementations

September 29, 2026. Source reading is not execution or performance validation. These links are pinned to the inspected revision. New implementation recipes are independently written; third-party repositories are not copied into this skill.

## github.com/axtonliu/moyun

**code-excerpt-inspected** · [inspected file](https://github.com/axtonliu/moyun/blob/eb488acf811122bb9a574d87fb148ffa42ed4c23/index.html)

Brush spacing is distance-based; dye channels distinguish mobile ink, water and settled ink. Read the bleed and brushSeg sections. Its live wash uses randomness and accumulated simulation, so do not assume arbitrary seek is deterministic.

September 29 follow-up: read pointer and wash handlers at the same archived revision; MIT license inspected. The live site accepted a manual ink stroke and a water gesture pulled a faint trail while much of the initial mark remained. The first crossing showed little visible change. Auto-paint and wash controls were exercised; no controlled input-speed comparison, audio assessment or GPU performance measurement. Live deployment revision was not independently pinned. See [gesture and wash guidance](build-patterns.md#brush-gestures-and-an-animated-wash).

## github.com/ishuagrawal/particle-beach

**code-inspected** · [inspected file](https://github.com/ishuagrawal/particle-beach/blob/92db82255b962acf2930f19bf6e5e7790174a790/js/ribbons.js)

Ribbon history is bounded by lifetime and distance; strip width and opacity decay along its length. This is stateful history, so export needs replay or baking rather than merely setting a time uniform.

## github.com/sbobyn/three-avbd

**code-excerpt-inspected** · [inspected file](https://github.com/sbobyn/three-avbd/blob/b3675dea83c78aba9644b059975f48285bf02a47/src/avbd3d/painting.ts)

The painting setup derives scale and injection rate from body count and a fixed step. The README describes GPU-resident rendering and selective readback; benchmark claims remain author-reported, not reproduced here.

## github.com/JohnHeibel/ClaudeAnimationBase

**code-inspected** · [inspected file](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/0ac8bf2b31942376cb6b8c4074715595d512acd2/src/timeline.js)

Shots receive global and local time. A covering brush wipe hides the shot switch. This is useful for deterministic shot orchestration; the third-party character and art direction are optional.

## github.com/shinshin86/still2rig-psd

**code-excerpt-inspected** · [inspected file](https://github.com/shinshin86/still2rig-psd/blob/29f2c086fef408483cdd1650b6b7626e27117600/src/motionQa.mjs)

Motion QA compares the expected facial region against changes elsewhere and looks for seams. The README explicitly distinguishes preview expression placeholders from production-ready artwork.

## github.com/hs7j4yk4sz-boop/punk-to-bricks

**code-inspected** · [inspected file](https://github.com/hs7j4yk4sz-boop/punk-to-bricks/blob/7d9fc7afdbe1079084ff24f63d58c5207fb3f540/src/core/check.ts)

Checks use the final part list for connectivity and intersections. Center-of-mass support uses the base bounding rectangle, so it is a simplified check, not proof of real structural stability or physical build testing.

## github.com/JimLiu/taohuayuan

**code-excerpt-inspected** · [inspected file](https://github.com/JimLiu/taohuayuan/blob/61567657a5cffd64461d8e00c5907540b733f8dc/src/story/director.js)

The director rebuilds chapter state, uses narration-derived timing and supports bounded look-around. The prompt is a later reconstruction of an iterative build, not the original one-shot instruction.

## github.com/petergpt/painted-rickroll

**code-inspected** · [inspected file](https://github.com/petergpt/painted-rickroll/blob/ca9a66250a0c4efc15d6c149c8335403badfb64b/src/30-rig.js)

A shared pose feeds a skeletal hierarchy and two-segment inverse kinematics with reach clamping and a pole direction. The project separates rig, dance, surface painting and audio.

## github.com/makevoid/motion-graphics-music-video-skill

**documentation-reviewed** · [inspected file](https://github.com/makevoid/motion-graphics-music-video-skill/blob/93248cc6117d05a2c108339fb5936bfb9c6f313e/README.md)

A mixed-media workflow combines generated assets and programmable compositing. Read dependencies and generation costs in the project before deciding whether to use it; it is not proof that every frame was drawn in code.

## github.com/ferndesk/no-slop-motion

**documentation-reviewed** · [inspected file](https://github.com/ferndesk/no-slop-motion/blob/dc4896d2012760f81af5a24b064a883ba271211f/README.md)

A brand-film workflow with script, voice, visual-world and animatic stages. Its mandatory approval gates are its own process; they are not inherited by this general design skill.

## github.com/moguzbulbul/blueprint-animation

**documentation-reviewed** · [inspected file](https://github.com/moguzbulbul/blueprint-animation/blob/29aa30b83db4632daf586420c52a251e7dac2d92/README.md)

Useful design-rationale reference with a before/after construction sequence. CC BY-NC 4.0: commercial reuse of its code or skill requires permission. No third-party code from it is bundled here.

## github.com/dgreenheck/tidewater

**documentation-reviewed** · [inspected file](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/README.md)

The current repository has evolved into a fishing game with a custom WebGPU engine and externally sourced assets/audio. Do not assume the current main branch is identical to the original X clip.

## Find more

`python3 scripts/search.py "ink brush" --kind resources` searches the creator-linked resource directory. Resource type is based on its URL; a video may be a finished film rather than a tutorial. Uninspected entries are explicitly labeled.

## github.com/GodsBoy/astra-6-bench

**selected-code-inspected-and-tests-run** · [mechanism](https://github.com/GodsBoy/astra-6-bench/blob/1f3dddb74ab2180ec139413706632e0f4ff17c5a/index.html) · [tests](https://github.com/GodsBoy/astra-6-bench/blob/1f3dddb74ab2180ec139413706632e0f4ff17c5a/tests/mechanism.test.cjs)

Read the rail and MarbleComputer code plus the complete test harness. Four tests passed locally, covering 256 input pairs, contact-triggered flips, path joins, reset and demo sequence. Visual quality and performance remain untested. This uses scripted tracks, not rigid-body simulation. No license file was present in the inspected tree; source is a study reference, not bundled reusable code.

## github.com/echris6/motion-video-kit

**documentation-reviewed** · [product-motion tutorial](https://github.com/echris6/motion-video-kit/blob/255562b04b1e5ecaa4ba98e5c9aa191d5ba7f6fa/business-motion-film/references/product-hero-realism.md)

Read README and the linked tutorial. Useful subjects include pose measurement, curve fitting, display continuity and motion-aware lighting. Numeric targets, tool choices and restrictive style rules are source-specific examples. The tutorial's results were not reproduced. README states MIT; no external code or skill was copied or installed.

## github.com/am-will/music-video-reimagined

**selected-documentation-and-code-reviewed; not-executed** · revision `7d6b7b22caf08c6e330e1abb869953d8e4f2cc1a` · [dance tutorial](https://github.com/am-will/music-video-reimagined/blob/7d6b7b22caf08c6e330e1abb869953d8e4f2cc1a/skills/music-video-reimagined/references/dance-videos.md)

Read dance-videos and song-map tutorials, chapter boundary guidance and trim_audio.sh. MIT license inspected; inherited ClaudeAnimationBase attribution retained by the source. README credits both Opus 5.5 and Sonnet 5.5. No external script was run or film inspected. Extracted the pose-library and clock contracts as original adaptations.

## github.com/nikunjkothiya/gpt-6-astra-skills

**selected-documentation-and-code-reviewed; not-executed** · revision `d18496cc2c0bdddc1e60abec6450c2872d9df6c4` · [frame-sequence tutorial](https://github.com/nikunjkothiya/gpt-6-astra-skills/blob/d18496cc2c0bdddc1e60abec6450c2872d9df6c4/skills/interactive-motion/references/scroll-image-sequences.md)

Read frame-sequence guidance and embedded pure mapping/crop helpers, plus canonical-pose guidance. Extracted asynchronous presentation invariants; no full loader or rendered demo was executed. Repository tree contained no license file. No external implementation or skill installed. Creator attribution to Astra 6 is retained as a claim, not independent verification.

## github.com/AiondaDotCom/ai-sim-benchmark — Opus 5.5 water run

**selected-code-inspected; three independent numerical probes passed; selected video frames inspected** · revision `680f87e6d54984199525dd12005bd95711bb47bb` · [worked study and source files](terrain-water.md)

Read water solver, water renderer and water tests. Local probes covered volume conservation, downhill movement and open-boundary budget accounting. These are not the creator's full 23-test suite. Repository declares MIT; no implementation bundled. Selected Skillry original/remake frames were inspected separately; neither frame rate nor physical accuracy was established.

## github.com/xenitV1/mola

**selected-code-inspected; five independent gesture scenarios passed** · revision `d2b3123e2dcbdc2163a5d14f96e16b51c36c8c2e` · [camera source](https://github.com/xenitV1/mola/blob/d2b3123e2dcbdc2163a5d14f96e16b51c36c8c2e/src/view/camera-gestures.ts) · [worked guidance](spatial-input.md)

Read camera gestures, camera tests, pose, street detail construction and city-life tests. Five independent scenarios executed against the camera source: pinch roundtrip with tap suppression, cancellation, capture loss, angle wrap and disabling input. This is not the full game suite or a real-device test. Pose code uses distance-driven phase and foot-bottom height correction, not planted-foot IK. GPL-3.0 license inspected; third-party asset licenses and reserved name/logo noted in README. No implementation or assets bundled. Creator attributes game to GPT 6 Astra; visuals not inspected.

## github.com/KevinXu02/aha-3d

**selected-code-inspected; three compositor tests passed; selected live controls observed** · revision `82f4b1110cfe4b55fff19df3b3790852ce07b171` · [worked guidance](source-view-reconstruction.md)

Read overlay.py, its three tests and CONTACT_REFINEMENT.md. Tested opaque/transparent and antialiased edge compositing and mismatched array rejection. Did not run Blender, reconstruction or motion refinement. The contact documentation distinguishes current translation-based constraints from a historical leg solver; do not infer that a legacy command validates contact. Live browser evidence covers tabletop camera, material change and reset only. Apache 2.0 repository license inspected; assets and dependencies remain separately licensed. No implementation bundled.

## github.com/google-ai-edge/mediapipe-samples-web

**selected-worker-code-read; not-executed** · [inspected worker](https://github.com/google-ai-edge/mediapipe-samples-web/blob/fa5a2eec5a6a3bed339d872dfd8d7895e1db13f7/src/workers/hand-landmarker.worker.ts)

Video detection receives a timestamp; input bitmap is closed; result includes inference duration but no capture ID/timestamp. This is an official supporting example, not the water-orb creator's code. Apache-2.0 header inspected; no third-party implementation bundled. [Original input-pairing guidance](hand-depth-input.md) adds an explicit identity contract.

## github.com/kitcut-hq/kitcut

**selected-pinned-source-read; not-executed** · [engine](https://github.com/kitcut-hq/kitcut/blob/7ba9c98db0b231cd294ed5060ad4a582b2776c9e/sketch/engine.js) · revision `7ba9c98db0b231cd294ed5060ad4a582b2776c9e`

Word/occurrence lookup, line-local to film-time placement and renderer timeline injection read. Example helper sends decimal fallback-like values into occurrence indexing; missing lookups return zero. No render failure was reproduced and no visuals assessed. No license file found in retrieved tree; implementation not bundled. [Original narration cue recipe](narration-cues.md) adds stable line IDs, explicit cue fields, preflight and dependent retiming.

## github.com/howseen-ai/claude-motion-design

**selected-pinned-source-read; synthetic logic probe only** · revision `ae1499434b01326bc7f3b8b11797a2f727a70ab2` · [worked transition QA](transition-qa.md)

Read render template, example renderer and remake QA script. Sample averaging and adjacent-frame difference scan inspected. A synthetic paired-edge flash is missed by the isolated-peak rule; this is not a measured detector benchmark. Full repository and films not executed or visually reviewed. MIT license read; separate media rights retained; no implementation bundled.

## github.com/blendi-remade/weeping-angels

**selected-pinned-code-and-tests-read; not-executed** · revision `164a9049c00c79663e02a51f21c333a6bb9ee462` · [visibility source](https://github.com/blendi-remade/weeping-angels/blob/164a9049c00c79663e02a51f21c333a6bb9ee462/src/visibility.ts) · [original recipe](observation-gated-motion.md)

Read visibility, illumination, angel movement and selected tests. Conservative partial visibility, separate sight blockers and proposed-step bounds supply the mechanism. Original guidance distinguishes instantaneous pose swaps from smooth rotational sweeps. Initial live chapel rendered; no gameplay rule or performance verified. No repository-wide license found in tree/API metadata; separate font licenses present. No implementation or assets bundled.

## github.com/Mort1d/motion-graphics-skills

**Selected pinned comparison code read; not executed or auditioned.** See [sound identity evidence](updates/2026-09-30-sound-identity.md) for revision, inspection scope and measurement limits.

## github.com/EverettFish/squishy-skill

**Selected pinned code and live pull/recovery inspected.** See [local material memory](local-material-memory.md) for rest-space contacts, fast response/slow residue and separate character-asset rights. No full interaction or physical-accuracy verification.

## github.com/louisedesadeleer/build-your-own-apartment

**Tutorial, selected pinned code and selected live actions inspected.** See [compatible actions](updates/2026-09-30-compatible-actions.md) for pose clearance and gesture-strength findings. Combined petting/prop behavior and continuous collision safety remain unverified.

## github.com/veedstudio/open-edit

**Selected pinned export/import code and tests read; not executed.** Revision `7f212e0484a01d976fb3e68d4adc9f6373c19346`. See [editable motion handoff](editable-motion-handoff.md): native items, rendered-layer origins, independent trim/placement and reported conversion losses. Apache-2.0 license inspected; no implementation bundled. No live editor, exported film or audio verification.

## Ant gallery: event stops and targeted jumps

[Simulation event-stop study](simulation-event-stops.md) reads selected inline engine and UI scheduling code from the public [Ants on a grid page](https://www.experimentswithai.com/ants-on-a-grid.html), archived by content hash. Selected live stop/resume/jump/reset paths were exercised. This is an inline implementation study, not an additional repository investigation; mathematical survey claims and full numerical correctness were not reproduced.

## Kitchen twin: shared-camera scan/model comparison

[Shared-camera inspection guidance](source-view-reconstruction.md#inspect-scan-and-model-through-one-camera) is backed by selected inline viewer code and live split, selection, top-down and exit controls. The [dated evidence](updates/2026-09-30-shared-camera-comparison.md) separates this browser study from unverified upstream reconstruction and accuracy claims. No additional repository investigation or third-party implementation is bundled.

## ft-motion: frame clocks and cut alignment

MIT license and selected `engine/core.js` runtime plus technique documentation read at `6abcf2e648bc8a7578d8d6bc32b346b846bec9bb`. [Dated study](updates/2026-09-30-crisp-frame-clock.md) strengthens existing selective-blur and transition guidance. Independent sample-time arithmetic checked; no source execution, export, audio audition or film inspection.

## Pressure Wash Panic: action and effect predicates

Selected shipped JavaScript lesson definitions, coach progression and counter/reset paths read; initial live tutorial sampled. [Evidence and limits](updates/2026-09-30-action-gated-lessons.md) distinguishes code findings from untested later lessons and the coach's end-of-job completion shortcut. No repository or license claim; no implementation bundled.

## Whiskey Caustics: receiver-space light transport

Selected tracing, receiver-map, coverage composition and quality settings read at `09c11c31b5a54d9af265f398cb41f8bef6dcbc7b`; deployed main module matched. Live caustics toggle and glass drag inspected. [Dated evidence](updates/2026-09-30-caustic-footprints.md) separates the structured ray-grid implementation from unverified general photon mapping, energy accuracy and performance claims. No license file found; implementation not bundled.
