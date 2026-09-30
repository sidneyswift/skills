# Watchable references: compare, extract, build

Use this route when the brief needs a visible reference, particularly when X playback fails. Search the [comparison index](visual-comparisons.json) without loading it all:

```bash
python3 scripts/search.py "optical camera focus" --kind visuals --limit 4
python3 scripts/search.py "elastic shape" --kind visuals --limit 4
```

The [Skillry gallery](https://skillry.dev/ai-videos/opus-5-5) was inventoried September 29, 2026: 389 original/remake entries (223 motion, 47 explainers, 51 3D, 68 interactive), of which 374 match the source catalog. The other 15 are discovery leads. This is a metadata inventory, not 389 watched or approved examples. 110 entries carry a partial-prompt flag; lack of that flag does not certify the other 279 prompts as complete. A recorded remake does not prove a live interaction works. Verify dates and attribution on the original source before promoting a lead.

## Turn a comparison into useful design decisions

This inspection method and the prompts below are original engineering synthesis, not instructions supplied by the gallery.

1. Choose a pair for the mechanism the brief needs. Name the decision it should inform: timing, spatial explanation, continuity, materials, interaction feedback, or composition.
2. Watch the original and remake separately first. Record setup, action and resolution timestamps. Match equivalent events, not merely equal timestamps: playback and edit timing may differ.
3. Describe each independently. At a key event, identify the focal object, state change, camera motion, motion hierarchy, and what remains legible. A remake can preserve the subject but alter all five.
4. Extract one invariant: for example, the same object survives a transformation, or one parameter drives both geometry and its explanatory overlay. Distinguish visible correlation from a verified causal implementation.
5. Write a minimal build contract: input → state → geometry/render → visible consequence. Expose two or three meaningful controls. Identify the smallest sequence that could disprove the mechanism.
6. Build an original study, then inspect the same event phases. Keep what serves the brief. Do not average two incompatible art directions or infer performance from compressed video.

Use a compact record:

| Field | Record |
|---|---|
| Provenance | Original URL, comparison URL, source date and exact model attribution |
| Evidence | Creator statement / sampled video / live interaction / code inspected / original synthesis |
| Event | Timestamp or phase, what visibly changes, what stays recognizable |
| Mechanism | State variables and the relationship they must preserve |
| Tuning | Parameter, expected visible effect, useful range to test |
| Check | An input or frame comparison that exposes a failure |
| Unknown | Missing assets, partial prompt, untested controls, numerical or performance assumptions |

## Worked reference: an optical camera lab

[Original post](https://x.com/chudry223/status/2103044654187081860) · [paired videos](https://skillry.dev/ai-videos/opus-5-5/chudry223-081860)

**Observed:** selected playback frames show separated lens elements, ray lines and an image plane in both versions. The remake includes a close view of the image plane. Both videos played; they were not perfectly synchronized. **Creator description:** adjustable optics. **Not verified:** live controls, accurate optical calculation, performance, complete prompt. Skillry labels this prompt partial.

**Original build adaptation:** make one optical setting govern the explanation, not just a decorative slider. Keep three representations consistent: a spatial lens arrangement, a ray diagram and a resulting image. Use a clearly labeled simplified model if physical correctness is out of scope. Separate inspection spacing from optical distances: exploding a lens for viewing should not accidentally alter its computational configuration. Keep focus distance, aperture and inspection spacing independently adjustable so the viewer can learn their distinct effects.

**Adapted prompt:** Build an interactive optical study with one focal scene, visible lens elements and an image plane. Define the optical state before the animation. Couple the ray diagram and image response to the same state; label approximations. Add a separate inspection control that spreads parts without changing the simulated settings. Prove the relationship using two contrasting focus distances and two apertures, then polish the materials and camera framing. Keep labels legible during every transition.

**Checks:** compare image and diagram at both parameter extremes; retarget while parts are moving; restore the assembled state without parameter drift; show the current approximation. A video match alone does not pass these checks. Start from the [computed optical image pattern](patterns/explainers.md#computed-optical-image) when the brief needs causal explanation.

## Attribution and prompt cautions

[Codrops' gallery entry](https://skillry.dev/ai-videos/opus-5-5/codrops-340299) describes an arcade containing independent developers' games and mentions Opus as context. Its gallery placement is insufficient evidence that Opus generated those games. Keep it a design lead until the original authorship is checked.

[The persistent UI-shape entry](https://skillry.dev/ai-videos/opus-5-5/twoclipping-402193) includes a more detailed prompt than the camera and water descriptions. Read its constraints as choices for that particular piece. A single shape, single file, fixed beat, or uninterrupted shot is not a universal design principle. Do not bundle the full prompt or assume a remake reused exactly the same inputs.

## Additional sampled reference

The [terrain-water study](terrain-water.md) connects a second sampled original/remake pair to inspected source code and three numerical probes. This does not upgrade the other unviewed entries.

The [structural typography study](structural-type-study.md) records a third sampled pair: words become loads and supports. It includes event-specific observations and a build contract without treating every prompt instruction as achieved.

## Glass follow-up

[September 29 glass study](updates/2026-09-29-glass.md): original and remake sampled separately. Original slider, lens and translucent digits observed; matching time values did not reliably indicate matching events. Background-copy rendering remains creator-described, not implementation-verified.

## Traveling type weight follow-up

[September 29 typography study](updates/2026-09-29-weight-wave.md): mixed letter weights and word expansion observed in both recordings. [Build guidance](build-patterns.md#traveling-font-weight) separates glyph weight, tracking, footprint and measurement overlays.

## Train window follow-up

[September 30 tunnel study](updates/2026-09-30-train-window.md) strengthens the existing train-window pattern with sampled occlusion/reveal evidence and original landscape-state and interior-lighting checks.

## Particle beach follow-up

[September30 trail lifecycle study](updates/2026-09-30-particle-trails.md) pairs selected environmental samples with existing pinned ribbon code. The unbadged gallery prompt explicitly describes additional prompts; do not treat it as complete.

## Keep copy fidelity separate from motion resemblance

The [TechHalla comparison](https://skillry.dev/ai-videos/opus-5-5/techhalla-498547) has similar poster colors and animated-letter structure but substitutes its own call to action and brand. See [the paired-state record](updates/2026-09-30-type-comparison.md). Record content, typography and motion fidelity separately. A polished remake with different copy is a useful adaptation reference, not evidence that the original prompt was followed. For per-letter entrances, inspect the first fully readable phrase and the beginning of its exit independently; equal clip timestamps need not represent equal event phases.

## Portal zoom follow-up

[The September30 paired-state study](updates/2026-09-30-portal-comparison.md) strengthens an existing portal-zoom reference. Both sampled versions place the next landscape inside a camera lens and later a mirror, with different framing and phase timing. The original creator explicitly names Opus5.5 and separately confirms external media generation. The initial prompt is available, but the full production history, exact zoom law, handoff continuity and loop closure are not verified.

## Fire and smoke follow-up

[The campfire comparison](updates/2026-09-30-fire-comparison.md) strengthens the existing fire-to-smoke pattern. Selected original/remake campfire and late wide-shot phases show different flame visibility, fuel silhouettes and light pools. Keep camera/framing changes separate from heat decay, and retain the creator-only status of solver, sound and performance claims. Gallery prompt remains explicitly partial.

## Rigid-body comparison follow-up

[Wall, weld and friction phases](updates/2026-09-30-rigid-body-comparison.md) strengthen the existing contact-chain pattern. The remake labels a different solver approach and body count; compare presentation without treating it as validation of the original AVBD implementation. Use isolated contact, break-threshold and friction tests before making physics or performance claims.
