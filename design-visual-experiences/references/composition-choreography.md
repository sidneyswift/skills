# Composition choreography for mixed-media films

Use with [creative production](creative-production.md) for generated footage, controlled UI and editorial motion. These are transferable decisions, not a fixed sequence, palette, genre or duration. A quiet product film may need fewer moves. Reference timing is evidence about one passage, not a universal preset.

## Direct the composition before animating components

For each meaningful UI entrance or exit, name the dominant subject before, during and after; the persistent object or spatial anchor; how the existing footage makes room; the information that must become readable; the cause of the change; and the result revealed by departure. A container's center is not always the subject's focal point. Review masks, depth, crop and occlusion in output coordinates.

Treat entrance as coordinated channels: preparation/visibility → framing and geometry → content resolution → readable interval → action response → departure and consequence. Overlap compatible phases rather than requiring them all to wait. Text may begin during expansion, but enough space must exist before it needs to be read. Activation follows the completed information when the story requires comprehension. Other stories may deliberately show the result first; label editorial illustration separately from a literal workflow capture.

Make the surrounding scene participate: translate or crop footage to clear a writing area, reduce its contrast or focus, or reveal a wider workspace around it. Preserve media playback through a camera-only move. Do not shrink compelling footage merely to accommodate unnecessary chrome. A full-screen-to-card move can expose controls already below the picture instead of making each control fly in independently.

## Separate geometry, lettering, effects and camera timing

Give each channel its own job and timing, with shared semantic cues where related. Use a stable button, object or headline as an anchor while another part changes. A capsule can expand around a bottom control row; a headline can remain anchored while partner badges reflow beneath it. The viewer should not need to follow every element simultaneously.

Select text behavior by meaning. Input typing communicates authoring; phrase entrances establish hierarchy; letter scale/offset/mask reveals introduce identity. These are different operations. Measure actual glyph bounds, including descenders and accents, at intermediate sizes; text masks must not clip settled copy. Preserve stable reading time after the last essential character resolves. Choose it for copy length, feed size and context, not a universal word-rate formula.

Choose travel, arrival, continuous passage, press and departure independently. Preserve nonzero velocity through a waypoint when the move should flow. Allow a stop for a deliberate read. Do not add spring overshoot to all properties: opacity cannot overshoot like position, and bounce may contradict a precise interface. Infer only visible displacement/blur from reference frames; exact spring or Bezier parameters require fitting or source code.

## Localized activation and consequence-driven exits

Give feedback a meaningful origin: a pressed control, contact point or changed object. Define the effect's boundary, propagation direction, intensity peak and decay. A brief textured light sweep inside a panel conveys operation more clearly than an unrelated full-frame flash. A world transformation may intentionally spread beyond the control; keep that different effect's ownership explicit.

Let entrance establish identity and exit clear attention. They need not be temporal reversals or equal lengths. Concentrate directional smear in fast travel and return to sharpness for reading. After comprehension, the outgoing panel can leave rapidly while the result arrives. Avoid an empty reset between them unless the pause serves the story.

Retire explanatory UI when visual proof takes over: notice → visible result → small identifying label. Overlap departing notices with the beginning of the result without leaving both at full emphasis. The next element can begin before the previous one is fully gone, provided one remains dominant. Sometimes the right exit is demotion: keep a previous asset as a small contextual thumbnail while the next becomes the main subject. Persistent controls can stay still while content changes.

## Materials, hierarchy and restrained complexity

Use simple geometry with intentional detail: thin edge light, a soft offset surface, a controlled gradient, subtle depth separation. Brand accents can peak during arrival or activation and recede for the hold. Adapt this to the actual brand; neither lime nor glass is a quality requirement. Correct brand identity does not require a permanent corner logo.

One dominant event may have several supporting movements. That differs from several independent focal events. Reduce simultaneous reading tasks, remove duplicated labels, and let framing carry explanation. Vary visual density between immersive footage, a focused operation and a quiet brand read. Energetic direction includes contrast and release; uniformly short cuts and permanently animated captions become tiring.

## Build and inspect a handoff

1. Compose the arrival and result frames with real copy, brand assets and subject bounds.
2. Define semantic cues for container readiness, content completion, action, departure and consequence as applicable. State which intervals overlap and why.
3. Assign transform/mask/blur ownership: camera, media, container, glyphs or effect. Keep one writer per property; source footage has its own clock.
4. Bind layout to measured content. Keep an intended anchor stable when resizing or restaging. New aspect ratios can require a new composition.
5. Implement the smallest meaningful passage with the existing renderer. Include footage before the UI and the result after it, not only the UI animation.
6. Inspect consecutive decoded frames with source PTS across anticipation, travel, settling, reading and departure, with context on both sides. Six 640px-wide frames per sheet is a useful inspection scale, not proof that every detail is readable; check native crops too. A one-second overview does not complete motion review.
7. Compare the same passage against both reference and prior output: displacement, scale, crop, occlusion, opacity, text resolution, effect origin and focal handoff. Record exactly reviewed frame ranges and hashes. Review normal/slowed playback and audio only when actually perceivable; generated players and successful playback controls are not perceptual evidence.

## Executable holds, cue relations and motion roles

[Choreography helpers](../assets/choreography-kernel.mjs) wrap the existing scene kernel. `compileChoreography({scene, relations, holds})` resolves named cues or seconds and checks minimum gaps without prescribing creative timing. A relation is `{id, before, after, minGap}`. A hold is `{id, at, end, channels:[{target, property, min, max}]}`. All timings use seconds; hold intervals are half-open. `sample(t)` rejects values outside declared channel bounds during a hold. Render every output frame through it; sampling a few times cannot prove unsampled intervals. Include camera/parent channels when their movement affects the read. Bounds check selected numeric channels, not actual text legibility or perceived focus.

`pressScale(t,{at,duration,depth})` makes a transient compression and returns exactly to rest. `visibilityEnvelope(t,{enter,ready,exit,gone})` gives separate entrance, hold and exit intervals. Both are stateless, permit deterministic seeking and require explicit timing. Their analytic curves are original options, not recovered Higgsfield curves. Use raw scene tracks for other motion characters. Copy the choreography, scene and motion modules together.

`assertSelectedAssets(selectedHashes, rejectedHashes)` rejects previously excluded source bytes even after renaming; the adapter must hash the actual files and provide the project rejection list. It is not an aesthetic classifier.

Run `node scripts/test-choreography.mjs`. With an existing Playwright installation, serve the skill and run `node scripts/test-choreography-browser.cjs http://localhost:PORT/assets/choreography-study.html`; `PLAYWRIGHT_MODULE` can name that installation. The [transfer fixture](../assets/choreography-study.html) uses the wrapper in a renderer with two unrelated product stories, long copy, different palettes, viewports and an inner cut independent of the outer UI. Its checks exercise cue shifts, read intervals, asymmetric exits and rejected holds. It is a synthetic mechanics demonstration, not generated-media quality validation or a claim of aesthetic parity.

## Evidence and limits

Original synthesis from mixed-media production iterations and consecutive-frame inspection of the [Higgsfield Games demonstration](https://x.com/higgsfield/status/2065177172571214270): prompt staging roughly 7.37–9.67s; notification-to-result handoff 9.67–11.17s; circle/capsule/badge reflow and title departure 12.47–15.57s; persistent asset controls 29.17–32.57s; game-to-card/remix/world transformation 36.73–39.97s. These are selected reviewed passages, not a claim of full-film review, audio assessment, inspected source code or a known generation pipeline. The displayed model badges do not establish the film's production software. Keep third-party frames and private review receipts outside the distributable skill.
