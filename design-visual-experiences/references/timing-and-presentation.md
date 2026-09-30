# Make the visible result obey the intended time

Use this for music-driven performances and frame-based inspection. Both can look almost correct while their clocks disagree. The contracts and worked numbers below are original synthesis; the linked tutorials supply the research evidence, not tested output from this skill.

## Music: distinguish source time, film time and musical phase

The [song-map tutorial](https://github.com/am-will/music-video-reimagined/blob/7d6b7b22caf08c6e330e1abb869953d8e4f2cc1a/skills/music-video-reimagined/references/song-map.md) discusses downbeats, pickups, local drift and verification after trimming. Its [audio preparation script](https://github.com/am-will/music-video-reimagined/blob/7d6b7b22caf08c6e330e1abb869953d8e4f2cc1a/skills/music-video-reimagined/scripts/trim_audio.sh) was read but not executed here.

Keep an explicit mapping. If source timestamp `s0` must land at film timestamp `f0`, then `filmTime(s) = f0 + s - s0`. Do not overwrite the musical downbeat with the start of the retained audio. A pickup can legitimately have a negative beat index while still appearing after film time zero.

**Original worked example:** a downbeat occurs at source 3.2 s, but the wanted pickup begins at 2.7 s. Place that pickup at film 1.0 s. The downbeat must then land at film 1.5 s. At 120 BPM, define phase from `(filmTime - 1.5) / 0.5`; using 1.0 as the downbeat offset would put every accent one beat early. Preserve the chosen mapping in the storyboard and test it on the actual delivered audio.

A constant offset error and progressive drift need different repairs. Check a clear transient near the start and another near the end. Similar errors suggest an offset; increasing error suggests a tempo, resampling or clock mismatch. Tempo changes need local anchors, not a global cosmetic delay. Do not automatically snap expressive movement or rubato to a fixed beat.

For gesture design, consult [beat-locked move libraries](patterns/characters.md#beat-locked-move-library). Distinguish the anticipation, strongest readable pose, contact and recovery: the largest displacement is not necessarily the perceptual accent. Test a short loop against the final audio before directing a whole scene.

## Frame inspection: distinguish requested state from presented state

The [frame-sequence tutorial](https://github.com/nikunjkothiya/gpt-6-astra-skills/blob/d18496cc2c0bdddc1e60abec6450c2872d9df6c4/skills/interactive-motion/references/scroll-image-sequences.md) specifies a bounded loader, stale-result rejection, cleanup and presentation-aware labels. Its mapping helpers were inspected; no full loader was run.

For N constant-rate frames, `round(clamp(progress, 0, 1) * (N - 1))` includes both endpoints. Variable-rate footage requires timestamp lookup. This mapping chooses a target; it says nothing about whether the image has decoded.

**Original failure sequence:** request frame 12, then frame 80. Frame 80 finishes first and is shown. Frame 12 finishes later. It may remain useful in a cache, but must not replace frame 80. Replace the source during the same sequence and even an index-80 result from the old source must be rejected. Therefore identity is at least `(source generation, frame index)`, not just an integer index.

Keep explanatory overlays tied to the actual presented frame when they identify visible anatomy or parts. A progress handle may show requested position, but its meaning must be clear while the picture catches up. Preserve a valid visible image while waiting instead of flashing an empty canvas.

Inspect after reversing input, resizing, changing source and tearing down. Count pending decodes until they settle, including cancellation requests that have not completed. Estimate decoded pixel memory separately from download size and verify real resource behavior in the target environment. See [latest-frame presentation](patterns/production.md#latest-frame-presentation).

## Evidence limits

The music repository credits Opus 5.5 and Sonnet 5.5 and contains MIT-licensed work, including separately attributed upstream material. The Astra toolkit is explicitly linked by its creator's Astra 6 post; this is author attribution, not a controlled model benchmark. No license file was found in the inspected Astra tree. No third-party code, complete prompts or media are bundled in these additions. Neither workflow's rendered output was inspected during this pass.
