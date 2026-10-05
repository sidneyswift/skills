# Creative direction and reusable motion production

Use this guide for generated imagery combined with authored graphics, product films, or a motion treatment that must survive new content. Start from [film direction](feature-launch-films.md) for the story and [production](production.md) for export and sound. These mechanisms are optional building blocks, not a mandatory look or a replacement for the existing renderer.

## Direct a shot instead of decorating a prompt

Resolve the shot's job, attention target, world, visible event, viewpoint and editorial use before translating them into a model prompt. A specific world comes from mutually reinforcing geometry, silhouette, materials, light and action. More adjectives, noise, expensive-looking surfaces or camera numbers do not establish taste. Choose details that survive the intended crop and display size.

Describe an opening state, a consequential change and a useful landing. Set direction, amplitude and supporting physical response where meaningful. Quiet shots can be precise; aggression, fisheye, fashion styling and neon are not general quality requirements. For stills choose the decisive state rather than forcing a temporal sequence. Examples of different intentions:

- A game scene can communicate speed with near-ground parallax, a readable vehicle silhouette and a brief foreground occlusion that clears to reveal the destination.
- An object shot can reveal construction through a hinge opening and one traveling reflection across its material.
- A quiet room can establish anticipation through morning light and one chair entering an otherwise settled composition.

These are original ungenerated examples, not validated recipes. Select returned takes against the shot's purpose and its actual composition. Preserve deviations and rejection reasons. When prompt, duration, take and edit change together, a human preference is evidence for the revision, not proof of which prompt phrase caused it.

## Decide the edit before generating its ingredients

Use a continuous take when spatial understanding, a performance or a transformation is the point. Use multiple shots when another view, detail, reaction, time change or example contributes new information. Each cut needs a job; neither shot count nor speed is a quality score.

Plan useful source handles, incoming/outgoing action phases, focal position, screen direction and continuity before generation. Generate clean scene content and author exact text, logos, controls and product claims separately. A still with a pan is not equivalent to requested subject motion. Judge both the source take and its final small-card crop.

Treat the inner edit as a media source with its own recipe: source hashes, trims, order, source PTS, intended rate changes, audio policy and duration. The outer composition controls its presentation and framing. Shrinking into UI must not restart the inner edit. A rendered intermediate is acceptable when its editable recipe and provenance remain available. Deliberate replay and resampling need explicit policies. A source review does not approve the assembled edit or UI composition.

## Simple elements, deliberate attention and timing

Give each beat one dominant subject. State what moves and what remains still. Distinguish camera transforms, object movement, deformation, lighting and texture; each visible effect needs an owner. Shared gestures should use shared progress rather than unrelated timers.

Compose the meaningful arrival frame first. Derive the camera and incoming movement from visible subject/text bounds, not only the media rectangle. Use a cut, continuous move or overlap according to the relationship being explained. At an attention handoff, check the actual focal feature in screen coordinates; equal object centers can still put a face or important control elsewhere. Preserve intentional changes in framing.

For an energy pass, first remove unnecessary anticipation/settling, overlap compatible actions and strengthen travel direction. Preserve recognition and completed-text holds. Do not accelerate all footage or add bounce everywhere. Keep nonzero transit velocity through flowing waypoints; use stops where the subject should actually rest. A source action can determine the reveal's landing time more meaningfully than an arbitrary UI duration.

Protect the image from unnecessary chrome. Branding requires correct identity when shown, not a persistent corner logo. Project brand sources override reference palettes. Keep conceptual UI, verified product behavior and factual outcome claims distinct. A visually working button or an exported local file is not proof that a product performs the depicted operation.

## Scene contract and engine helpers

The original [scene kernel](../assets/scene-kernel.mjs) supplies deterministic numeric tracks, named cue dependencies, channel ownership checks, source-PTS edit mapping, uniform-camera focal placement and review-receipt freshness checks. It complements the [motion kernel](../assets/motion-kernel.mjs); it does not generate assets, fit layout, render pixels or judge creativity. Copy both modules together when using them outside this skill.

Separate content inputs, layout, choreography and renderer. Keep project brand/copy/assets out of reusable mechanics. Expose useful semantic controls with units. An existing stack may implement these contracts without using this helper.

```js
import {compileScene} from './scene-kernel.mjs';
const scene = compileScene({
  duration: 4,
  cues: {submit: 1, reveal: {cue: 'submit', offset: 0.25}},
  objects: {
    image: {values: {progress: 0}},
    label: {stationary: true, values: {opacity: 1}},
  },
  tracks: [{target: 'image', property: 'progress',
    at: {cue: 'reveal'}, end: 2, from: 0, to: 1, ease: 'smoother'}],
});
const state = scene.sample(1.5); // Renderer maps progress to geometry.
```

Cues are seconds or `{cue, offset}` references. Tracks have explicit start/end, from/to and easing (`linear`, `smooth`, `smoother`, `out4`, or `hermite` with `v0`/`v1` in units per second). Values hold before/between/after tracks; `cut:true` permits an intentional starting-value discontinuity. Missing cues, cycles, overlapping writers, nonfinite values, unknown fields and out-of-lifetime spans fail compilation. `stationary:true` forbids tracks on that object; it does not forbid an external camera from moving its projection. Spatial parenting and bounds remain the renderer's responsibility. Numeric tracks do not enforce property-specific limits; clamp or validate opacity, scale and counters appropriately in the adapter.

`compileSequence({sources, clips})` accepts sources with `duration` and increasing normalized `pts`, and clips with `source`, `in`, `out`, optional positive `rate`. `sample(sequenceTime)` returns source identity, frame index and source PTS, or null outside the half-open edit. It supports hard cuts only. It holds the latest source frame at the requested time, explicitly allowing repeated/skipped frames when delivery cadence differs; it performs no interpolation. Preserve the normalization offset if the original stream does not begin at zero. Dissolves, audio mixing, decode and rendering require a separately tested adapter.

`focalPlacement({viewport:[w,h], camera:{x,y,scale}, focus:[x,y], size:[w,h]})` converts a desired screen rectangle center and size into world geometry under a uniform camera. Use a measured focal-feature offset when the attention point is not the rectangle center; rotation, perspective and arbitrary transforms need a different adapter.

## Prove reuse and preserve review state

Test routine changes during animation, not only in a settled still: a longer phrase, alternate media dimensions/subject bounds, one timing change and a second aspect ratio when requested. Measure text and fit components deliberately; automatic shrinking is not a universal repair. Keep related cue timing consistent, and do not retime source footage during a camera-only edit. A new aspect ratio may need restaging rather than a crop.

Keep two comparisons: current output against the reference mechanism, and current output against the approved baseline. The first checks creative intent; the second finds unintended changes. Inspect source PTS, consecutive boundary frames, intermediate motion, native details and actual playback/audio when available. Record frame review, playback observation and listening separately. A control test cannot certify perceived rhythm.

Bind review receipts to actual hashes of output, source assets, code, recipe and brand inputs. Relevant changes make dependent approval stale. `reviewState(receipt, currentHashes, {playback, audio})` requires lowercase SHA-256 values for `export`, `assets`, `code`, `recipe` and `brand` (hash a canonical manifest for each grouped dependency), then checks these identities plus explicitly recorded technical, visual, playback/audio and human states. It does not compute hashes, verify honesty or grant approval; the caller must supply actual current evidence. Drafts remain usable while review is pending. Never infer human acceptance from a passed validator, and never upgrade unavailable playback/listening into a pass.

Open the [scene transfer study](../assets/scene-study.html) through a local HTTP server for a synthetic long-copy/alternate-aspect fixture with an inner cut at two seconds. It demonstrates mechanics, not an approved creative treatment.

Run `node scripts/test-scene.mjs` for the bundled mechanics and failure cases. With Playwright already available, run `node scripts/test-scene-browser.cjs http://localhost:PORT/assets/scene-study.html` against the served fixture; `PLAYWRIGHT_MODULE` may point to an existing installation. Also test the chosen renderer with actual changed content. A mechanically successful transfer is not a taste benchmark. Human review should evaluate unaided understanding, intentional visual choices, attention, brand fit and the usefulness of the result for the stated funnel/job. Generalize the reason for a preference, not a performer's wardrobe or one scene's coordinates.

## Sources and scope

Original synthesis from local mixed-media iterations and inspection of Higgsfield's published `fnf-after-effects-mcp` 0.1.3 skill modules (design, motion, transitions, editable rigs, collage and review) and installed `motion-craft` guidance. [Package source](https://www.npmjs.com/package/fnf-after-effects-mcp). Their skills informed contracts and comparison questions; no third-party skill text, code, footage or fixed recipes are bundled here. This does not establish how their marketing films were made, model training, compatibility with their runtime or aesthetic parity. The helper implementation is original and backend independent.
