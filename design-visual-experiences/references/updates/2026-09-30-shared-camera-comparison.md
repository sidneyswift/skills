# September 30 — inspect two spatial layers through one camera

Extended [source-view reconstruction](../source-view-reconstruction.md#inspect-scan-and-model-through-one-camera) with a comparison wipe, side-aware picking, state restoration, tuning and failure checks. This strengthens an existing mechanism family instead of creating another pattern.

**Primary attribution:** [Frank Dou's post](https://x.com/frankzydou/status/2098460193319186578), September 11, 2026 at 17:14:32 UTC, explicitly names GPT-6 Astra and links the [kitchen demo](https://frank-zy-dou.github.io/kitchen-twin/). This is a broader-30-day source, outside the priority seven days. Full archived body reread. It describes a video-to-scan-to-model workflow with specialist tools and a separate verifier; that pipeline was not executed or independently verified.

**Code read:** selected public inline sections at archived HTML lines 137–265 and 345–470: shared renderer/camera, coordinate conversion, joint transforms, clipping, comparison visibility/scissor passes, UI metadata, selection and pointer-side routing. The two passes use the same camera and full viewport. Split changes scissor regions; exit restores checkbox-defined visibility. Pointer coordinates remain relative to the full canvas while candidate geometry depends on the exposed side. This is a viewer study, not a repository investigation or reconstruction-code audit.

**Observed live:** comparison loaded; split changed from 50% to 70% and back; refrigerator list selection produced a label/highlight and camera movement; top-down retained the comparison; leaving comparison restored enabled layer toggles. Scan surfaces appeared incomplete and irregular beside simplified model geometry. A top-down screenshot is archived. Door motion, exact per-pixel picking, all layer combinations, resize/high-density behavior, accessibility and performance were not tested. Displayed scores, metric dimensions and draft/accepted labels are source metadata, not independently validated results.

HTML SHA256: `63706af3cb1d01f62d82373f3f5a9818ca2c9802266e436615397680fe673468`. No explicit reuse license observed in the inspected page. No third-party code, assets or full prompts bundled; implementation guidance and adapted prompt are original synthesis.

No new paid API work. Reused Apify run `NKYsGJgC6rHZCYe4l`, whose previously reported actual cost was $0.64. All 419 novel previews remain screened; pending inspections continue. Totals: 1,304 catalog records, 138 resources, 104 patterns and 27 repository investigations.
