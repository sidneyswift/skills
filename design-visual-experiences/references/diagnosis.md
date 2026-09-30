# Diagnose the visible failure

Change the mechanism responsible for the symptom before adding polish. These are original debugging heuristics, not universal style rules. Tune against the actual subject, device and output.

| Visible symptom | Likely cause | Small diagnostic | First repair |
|---|---|---|---|
| Everything moves but nothing matters | No temporal hierarchy | Freeze all supporting layers | Give the defining action a setup and hold; reintroduce supporting motion only when it directs attention |
| Morph turns into an unrecognizable blob | Unstable correspondence | Draw point IDs and object anchors | Preserve point order/identity; use a cover or cut when a meaningful intermediate shape is impossible |
| Drag release feels dead | Velocity discarded | Release after fast and slow drags | Estimate pointer velocity over a short stable window and initialize the settling motion with it |
| Spring becomes more frantic after retargeting | New spring starts from stale state | Retarget repeatedly before settling | Evaluate current position and velocity at the retarget time before changing the destination |
| All edges move like a rigid sticker | Identical response everywhere | Show corner paths | Vary response by edge or attachment while keeping direct manipulation responsive |
| Feet skate | Contact computed in body space | Draw a mark at each stance target | Hold that target in world space; solve the body-to-foot chain |
| Knees flip | Ambiguous bend direction | Draw joint plane/pole | Keep a stable pole and clamp unreachable targets; avoid crossing the singular fully extended pose |
| Held object floats away from the hand | Two separately animated transforms | Draw hand and grip anchors | Solve the hand to the prop anchor or parent the prop consistently; switch constraints deliberately |
| Painterly character melts | Surface noise changes anatomy | Freeze the pose, advance only paint | Anchor marks to form; separate continuous rig time from surface refresh time |
| Ink looks like particles floating above paper | No deposited state | Pause motion after a stroke | Maintain settled pigment separately from wet transport and let paper modify absorption |
| Brush dots appear during fast input | Spacing follows event count | Replay at different sample rates | Stamp by arc length and preserve remainder distance between events |
| Whole forest feels like unrelated wiggles | Independent clocks | View only silhouettes | Share a spatial wind field, vary material response and add sparse local events |
| Day/night feels like a color filter | Lighting systems disagree | Compare sky, shadow, windows, exposure | Derive them from one sun/time state; stage discrete lights with transitions |
| Zoom accelerates strangely | Linear world distance crosses huge scales | Plot projected size over time | Use logarithmic scale and explicit handoff anchors; judge image-space speed |
| Camera reveals empty space | Path optimized without subject framing | Draw subject bounds per frame | Solve framing and a destination before smoothing the camera path |
| Loop pops despite matched endpoints | Velocity or hidden state differs | Inspect samples on both sides of seam | Match position and derivative; include particles, trails, noise phase and sound tails |
| Audio feels late | Motion starts on the beat but peaks later | Compare impact time to audio transient | Schedule anticipation before the accent, or shift the cue so visible peak meets audible peak |
| Audio-reactive motion jitters | Raw samples drive transforms | Feed a steady tone and silence | Analyze bands/envelopes; add attack/release and a quiet resting state |
| Type is energetic but unreadable | Glyph timing ignores phrase hold | Watch at final delivery size | Finish the entrance before the reading hold; animate graphemes, preserve shaping |
| A physics slider changes labels only | Render and model use different state | Compare known limiting values | Route simulation, geometry and labels through shared parameters |
| Particles stutter despite low polygon count | CPU allocations, draw calls or readback | Profile update, upload and draw separately | Reuse buffers, batch geometry, reduce readback; lower particle count only when it is the bottleneck |
| Export differs from preview | Wall clock or unrecorded state | Seek frames in a different order | Use pure-time state or fixed-step replay/checkpoints; record input and stable random seeds |
| Mobile composition loses the point | Desktop crop treated as layout | Inspect the narrow composition | Re-stage camera, labels and negative space for the aspect; do not only shrink everything |
| Details disappear after encoding | Excessively fine texture or contrast | View the compressed file at delivery size | Increase meaningful feature size, reduce noisy texture and test the real encoder |
| Reward plays before success | Animation disconnected from application state | Force a failed or delayed operation | Trigger it from confirmed completion; preserve distinct pending and failure states |

## A focused revision prompt

“Keep [identity, composition and working behavior]. At [time/state], [specific visible symptom] breaks [intended meaning]. Change [responsible mechanism], using [constraint or measured parameter]. Verify [one repeatable test].”

Example: “Keep the character proportions and camera. During left-foot stance the sole drifts backward against the floor mark. Hold the stance target in world coordinates and solve the knee from the moving hip. Check the contact across five samples within that stance.”

Do not repeatedly ask for ‘more cinematic’ or ‘more premium’ without naming the visible difference to create.
