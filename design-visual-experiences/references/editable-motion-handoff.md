# Preserve motion through an editable handoff

Use when a film must survive copy changes, revised timing or a person's later edit. Pair with [production](production.md) and [narration cues](narration-cues.md).

## Evidence and scope

[A September 28 creator post](https://x.com/sab8a/status/2104627757766578399) describes Opus 5.5 videos becoming editable projects. An [earlier creator follow-up](https://x.com/sab8a/status/2103237519127011469) links [Open Edit](https://github.com/veedstudio/open-edit). Selected code at `7f212e0484a01d976fb3e68d4adc9f6373c19346` was read: plan types, timeline import, layer clipping, provenance and selected round-trip tests. Repository license: Apache-2.0. No implementation is bundled.

The code supports native text, footage, images and audio alongside rendered page layers. A rendered layer remains a picture of its source; changing its internal content requires rendering again. The import code explicitly reports unsupported changes, including certain filters, effects, rotations, playback rates and subtitle tracks. This is evidence of the implementation's design, not a verified live round trip. No source tests, browser editor, export or audio were executed or inspected in this pass. Creator videos remain visually unverified here.

## Original implementation recipe

1. **Choose what the next editor must change.** Identify copy, captions, footage cuts, music and bespoke motion separately. Keep the first four as native editable items when the destination supports them. Render a complex animation as its own transparent layer only when needed. Name layers by purpose, such as “price reveal” or “orbit diagram,” so the next person can locate the intended change.
2. **Keep source time separate from placement time.** Record the source asset and source interval, the destination timeline start, duration and layer order. Trimming changes which part of the source plays; moving a clip changes when it plays. Neither should silently rewrite the animation's internal clock. For a rendered page layer, retain its page, stable selector or object ID, source revision and original rendered interval.
3. **Preserve edits when regenerating.** Store the original layer bounds plus the current placement transform. On re-render, apply the person's move/resize to the new bounds. Store source-time trims and timeline shift independently. Keep native copy changes in the plan rather than attempting to recover them from pixels. If the new duration cannot satisfy an existing trim, surface the conflict; do not silently substitute a different moment.
4. **Render bounds across the whole motion.** A crop based on the first frame can amputate a later flourish or shadow. Find the occupied bounds over the rendered interval, including antialiasing, glow and blur. Keep short empty gaps in one semantic clip when useful, but split truly separate appearances intentionally. Preserve alpha and inspect recomposition over the actual background. Blend modes and effects that depend on other layers may need grouped rendering rather than isolation.
5. **Make conversion losses visible.** Maintain a feature map: preserved natively, baked into pixels, approximated, or unsupported. Retain the original project and export a revised copy. Report missing media and unsupported attributes beside the affected item and time. A plan that loads successfully can still have lost rotation, speed changes or audio ducking; do not call it a lossless round trip on that basis.
6. **Review the reconstructed composition.** Export, change one caption and one layer's trim/placement, import, regenerate and compare the affected intervals. Confirm that unchanged layers and audio cues stay put. Compare normal-speed playback with sound as well as key frames; a timeline listing alone cannot verify the output.

### Small timing example

Suppose a layer originally represents page seconds 4–10. The editor trims its first 0.5 seconds and places the resulting clip at film second 8. Re-render page interval 4.5–10 and apply a film-time shift of 3.5 seconds. Its first visible sample remains film second 8. Keep these quantities explicit; assigning the new film start as the page start would change the animation's phase.

### Controls and failure checks

Expose frame rate, source interval, placement, z-order, alpha padding and any gap-bridging threshold. Snap frame boundaries consistently at export; retain the timeline's rational rate when applicable. Test a thin line, faint glow, animated offscreen entrance, overlapping layers, trimmed footage, changed source duration, missing asset and unsupported speed change. A native text layer should remain text after handoff; a rendered procedural layer should retain the source recipe needed to change it.

**Adapted prompt:** Build [motion piece] as a layered edit. Keep requested copy, captions, footage cuts and audio separately editable. Preserve source-time and timeline-time mappings for bespoke animation, plus its generating source and placement. Demonstrate one copy revision and one trimmed/moved layer surviving regeneration. Report baked and unsupported features and inspect the reconstructed output before delivery.
