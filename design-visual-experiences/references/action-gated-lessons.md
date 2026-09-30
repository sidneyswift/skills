# Teach an interaction through measurable actions

Use this for a playable exhibit, unfamiliar creative tool or simulation whose controls need practice. Start with a small scene where one cause and its visible result can be understood. Keep that scene available as a regression fixture when the art becomes more elaborate.

## Build the lesson

1. **Separate input, effect and outcome.** Track movement distance or deliberate input, successful contact/change in the scene, and completed objectives independently. A pressed button does not establish that the user aimed successfully. An overall win does not establish that every intermediate technique was practiced.
2. **Remove competing demands initially.** Teach navigation and one manipulation in a small space before adding a second tool, timing pressure or penalties. Preserve visible consequences without making the initial mistake expensive. Expose difficulty as lesson data rather than duplicating the whole experience.
3. **Teach tool choice through contrast.** Let the user try a weak tool on a resistant target, then reveal a better tool and require its specific effect. Finish with a contrasting target that benefits from switching back. Keep the mismatch short enough to explain a difference without feeling broken.
4. **Advance from state evidence.** Define each step with an instruction, completion predicate, optional progress and optional target marker. Present one current step, retaining completed context and subdued future steps. Project markers from scene coordinates so they remain attached to the target as the camera moves.
5. **Decide what early actions mean.** Accumulated progress may legitimately satisfy a later step immediately; a lesson requiring fresh practice needs a baseline when that step activates. Store completion reason separately: demonstrated, skipped, or bypassed by the final outcome. A celebration may end the lesson without claiming that every action was demonstrated.

**Controls:** movement threshold, valid-contact duration, target resistance, tool unlock point, objective count, optional timer and penalty limits. Treat reference thresholds as scene-specific examples, not recommended universal values. Couple keyboard and touch instructions to the active input mode while preserving equivalent goals.

**Failure checks:** input without contact; repeated tiny taps; completion before a later step activates; switching tools before unlocking; a final objective reached out of sequence; reset halfway through; pause/resume; touch and keyboard paths; markers after camera/viewport changes. Verify whether progress is intentionally cumulative or step-local. Test the actual outcome and the recorded completion reason separately from decorative checkmarks.

**Adapted prompt:** Build a three-stage introduction to [interaction]: a small safe practice scene, a contrast that teaches tool choice, then the real constraint. Derive progress from actual effects, expose one current goal, and distinguish demonstrated actions from skipped or outcome-bypassed steps. Retain the practice scene for regression checks as visuals improve.

## Evidence and limits

This is original engineering synthesis from [the Pressure Wash Panic walkthrough and selected shipped code](updates/2026-09-30-action-gated-lessons.md). It generalizes beyond the game and its model/stack. Selected live introductory states were inspected; lesson completion, later lessons and all input paths were not verified. The reference's end-of-job checklist completion is presentation behavior, not proof of every prerequisite. No third-party implementation or complete prompt is bundled.
