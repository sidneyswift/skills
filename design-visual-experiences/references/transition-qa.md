# Inspect transitions between the good frames

Use when a rendered film looks good in key stills but has flashes, handoff jumps or ghosted cuts. Start with the existing [review passes](production.md#review-passes-with-distinct-jobs).

## Evidence and limits

[On September 29, hkbonur](https://x.com/hkbonur/status/2104968600352088332) explicitly recommended Opus 5.5 for the intro workflow and linked [Howseen's motion repository](https://github.com/howseen-ai/claude-motion-design). At revision `ae1499434b01326bc7f3b8b11797a2f727a70ab2`, the [render template](https://github.com/howseen-ai/claude-motion-design/blob/ae1499434b01326bc7f3b8b11797a2f727a70ab2/skill/motion-design/scripts/render_template.py) samples subframes and averages them; its pop scan compares each frame-change magnitude with its immediate neighbors. The [remake QA script](https://github.com/howseen-ai/claude-motion-design/blob/ae1499434b01326bc7f3b8b11797a2f727a70ab2/skill/motion-design/scripts/remake/remake_qa.py) makes consecutive-frame sheets at selected seams. Selected source was read; no film was rendered or visually assessed. MIT code license inspected; external media retains separate licenses. No implementation bundled.

The isolated-peak rule has a static limitation: a one-frame flash produces two adjacent large differences, so each can hide the other from that rule. A synthetic scalar probe confirms this logic case; it does not measure real-video detector accuracy. The source's fixed seam frame numbers and palette thresholds belong to its example, not every project.

## Original engineering synthesis

1. **Declare intentional boundaries.** Keep a timeline list of cuts, flashes, layer handoffs and scene changes. Store frame numbers against the actual export rate. For each boundary inspect at least the last two frames before it and first two after it; expand the window for a long overlap. Include loop end/start when the output loops.
2. **Look for paired edges as well as isolated spikes.** Compute adjacent-frame change as a candidate signal, then group nearby peaks. A flash can look like normal A → outlier B → normal A: compare the outer frames too. A real cut tends to persist into the following frames. Fast movement and deliberate strobing can resemble errors, so consult the event list and inspect flagged strips rather than auto-removing frames.
3. **Keep detail visible.** A small grayscale scan is cheap but can hide a tiny glyph jump or equal-luminance color flash. Inspect full-resolution crops around important text and handoff objects, plus a color-aware overview. Tune sensitivity to the shot; a global mean can dilute a local defect. Scores locate candidates, not aesthetic quality.
4. **Check the exposure window at cuts.** Subframe blur can sample both scenes around a hard cut and mix them into one output frame. If that blend is unwanted, partition samples by shot or limit the shutter interval at the boundary. Compare sharp and blurred strips. Preserve intentional dissolves; avoid forcing every transition into a cut.
5. **Test seek order and the delivered file.** Request the same seam frames forward, backward and directly to reveal stale transforms or cached layers. Then inspect the encoded result at the same events: a correct preview does not establish a correct export. Play each repaired section at normal speed before judging rhythm.

Controls: export frame rate, event frame, inspection radius, candidate threshold, region of interest, subframe count and shutter interval. Start with a short representative section before rendering the whole film.

**Adapted prompt:** Build a transition review sheet from the actual edit events. Include consecutive frames, relevant text/object crops and sharp-versus-blurred comparisons. Flag isolated and paired changes for review, explain intentional cuts, and verify repeated seeking plus the final export. Report observed defects separately from numerical candidates.

## A forward shutter still needs cut alignment

[ft-motion's pinned runtime inspection](updates/2026-09-30-crisp-frame-clock.md) adds a concrete case to the exposure-window check. Its default samples lie forward of the output-frame time, within half a frame. With positive constant playback speed and a cut on the output-frame grid, the frame before the cut samples only the old shot and the cut frame only the new shot. This does not guarantee sharp cuts at arbitrary times or shutter lengths.

**Original check:** map scene cut time through the actual playback speed into output-frame coordinates. After retiming or changing export rate, verify that mapping again; a cut on a musical beat is not necessarily on an output frame. Either snap intentional cuts to the export grid or explicitly restrict each frame's samples to its intended shot. Reweight remaining samples if clipping the exposure. Handle speed changes through the time mapping rather than assuming a constant multiplier. Test the frame before, at and after each cut with blur enabled. Keep deliberate dissolves intact.

An independent arithmetic probe of the inspected schedule produced six old-shot samples before an aligned cut and six new-shot samples at it. A selected off-grid case produced three of each. This is a timing counterexample, not execution of the source renderer or visual-quality verification.
