# Motion patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [One object, many functional states](#persistent-shape)
- [Elastic indicator with independently timed edges](#unequal-edge-springs)
- [Direct drag followed by a momentum-preserving snap](#release-momentum)
- [Soft resistance outside an interaction limit](#rubber-boundary)
- [An animated object that communicates system state](#semantic-orb)
- [Badge tilt with a bounded celebration](#constrained-badge)
- [Anticipation, release and readable reward](#earned-reward)
- [Particles that arrive at the value they change](#collect-to-destination)

- [A particle form that contracts, bursts and returns](#contract-burst-return)

- [Fit articulated product motion to measured reference poses](#measured-joint-motion)

<a id="persistent-shape"></a>

## One object, many functional states

**Mechanism:** Preserve one enclosing silhouette while its function changes; continuity comes from geometry and position, not a crossfade.

**Build:**

1. Represent each state as center, width, height, radius and color targets.
2. Use one continuous track per property; replace content inside a separate clipped layer.
3. Exit the old text before the container reaches its most compressed shape; reveal new content after usable space exists.

**Tune:** Start with three states and one accent. Keep the shortest dimension above the content minimum; camera framing is a separate track.

**Failure check:** Scrub backward and interrupt a transition. No duplicated shells, title overlap, abrupt width resets, or clipped focus target.

**Adapted prompt:** Transform [object] through [three meaningful states]. Keep its visual identity legible and make each transformation explain a user action.

**Evidence:** [@twoclipping](https://x.com/twoclipping/status/2103273003555402193), [@verbove](https://x.com/verbove/status/2103483957266268381). Creator description/prompt; verify the visual when fidelity matters.


<a id="unequal-edge-springs"></a>

## Elastic indicator with independently timed edges

**Mechanism:** A pill stretches because its leading and trailing boundaries respond differently.

**Build:**

1. Animate left and right bounds independently toward the selected item.
2. Choose the leading edge from travel direction, so rightward and leftward motion both stretch correctly.
3. Enforce a positive minimum width without changing the final target bounds.

**Tune:** Use a faster leading response and slightly delayed trailing response; keep overshoot small for precise controls.

**Failure check:** Rapidly alternate adjacent and distant targets. Width must stay positive and the last selection must settle exactly.

**Adapted prompt:** Make the selection marker feel tensile. Use separate edge dynamics and preserve continuity when selection changes before settling.

**Evidence:** [@twoclipping](https://x.com/twoclipping/status/2103273003555402193). Creator description/prompt; verify the visual when fidelity matters.


<a id="release-momentum"></a>

## Direct drag followed by a momentum-preserving snap

**Mechanism:** Held objects follow the pointer; released objects inherit the actual release velocity.

**Build:**

1. Track pointer displacement directly while captured.
2. Estimate velocity from recent timestamped samples, rejecting stale events.
3. On release, initialize a spring with the current position and velocity toward the snap target.

**Tune:** Tune snap spacing, velocity clamp and damping independently. Slow dragging must still feel exact.

**Failure check:** Release in both directions, at a bound, and after pausing while held. Check pointercancel and keyboard equivalents.

**Adapted prompt:** Build a tactile [slider/deck]. It should track exactly under the finger and carry its momentum into a bounded settle.

**Evidence:** [@listudio](https://x.com/listudio/status/2104162483888062945). Creator description/prompt; verify the visual when fidelity matters.


<a id="rubber-boundary"></a>

## Soft resistance outside an interaction limit

**Mechanism:** Compress overscroll into a finite visible distance, then return from that visible state.

**Build:**

1. Separate the raw pointer coordinate from its displayed coordinate.
2. Beyond a bound, display sign(over) × R × (1-exp(-abs(over)/R)).
3. Release from the displayed position and its derivative, rather than the unbounded raw input.

**Tune:** R controls maximum visible stretch, not allowable data value. Keep the semantic value clamped.

**Failure check:** Very large drags must not escape the screen. Releasing must not jump from the resisted coordinate to the raw coordinate.

**Adapted prompt:** Give [control] a soft end stop. Show resistance without letting the underlying value exceed its valid range.

**Evidence:** [@listudio](https://x.com/listudio/status/2104162483888062945). Creator description/prompt; verify the visual when fidelity matters.


<a id="semantic-orb"></a>

## An animated object that communicates system state

**Mechanism:** One object changes its behavior vocabulary across listening, thinking and completion.

**Build:**

1. Define named states with independent amplitude, deformation speed and color targets.
2. Map listening to a measured or scripted syllable envelope; reserve a distinct completion gesture.
3. Keep its trajectory and silhouette continuous when it becomes a smaller avatar.

**Tune:** Give idle the least activity. Do not use faster random noise as the only distinction between states.

**Failure check:** Compare muted stills and short loops for each state. The behavior must distinguish states without implying progress that is not real.

**Adapted prompt:** Create a [material] companion for [task]. Make listening, processing and completion unmistakable through different behaviors.

**Evidence:** [@listudio](https://x.com/listudio/status/2104162483888062945). Creator description/prompt; verify the visual when fidelity matters.


<a id="constrained-badge"></a>

## Badge tilt with a bounded celebration

**Mechanism:** A familiar graphic gains depth without losing the original composition.

**Build:**

1. Separate the badge face, relief and shadow.
2. Convert normalized pointer position into a small tilt and move the highlight consistently.
3. Run a brief completion accent, then return to a quiet resting state.

**Tune:** Start with low tilt; limit particle area to the badge perimeter and keep the central mark unobscured.

**Failure check:** Inspect front view, extreme tilt and reduced motion. The artwork must remain readable and recognizable.

**Adapted prompt:** Preserve [badge] exactly while adding restrained depth, cursor response and one short earned celebration.

**Evidence:** [@BThreeAgency](https://x.com/BThreeAgency/status/2103739079745827092). Creator description/prompt; verify the visual when fidelity matters.


<a id="earned-reward"></a>

## Anticipation, release and readable reward

**Mechanism:** Intensity has a clear arc; the reveal clears space so the reward becomes readable.

**Build:**

1. Model anticipation, charge, burst, reveal and collect as explicit states.
2. Put moving parts on real pivots and route VFX from the physical release point.
3. On reveal, remove competing layers; cancel prior oscillations before starting the next state.

**Tune:** Scale light, timing and debris by reward tier; keep the peak brief and offer a calmer motion variant.

**Failure check:** Spam activation, mute audio and replay. Reward balance changes only once; the hero is not hidden behind bloom.

**Adapted prompt:** Stage [achievement] as a short payoff. Build tension, release it, then give the actual reward a clean readable hold.

**Evidence:** [@op7418](https://x.com/op7418/status/2104085539419021491). Creator description/prompt; verify the visual when fidelity matters.


<a id="collect-to-destination"></a>

## Particles that arrive at the value they change

**Mechanism:** A collection effect explains where a reward goes, rather than spraying decoration.

**Build:**

1. Give each item a deterministic curved path from the reward to its destination.
2. Schedule arrivals and update the displayed total from those arrivals.
3. Separate the animation count from the authoritative award so interruptions cannot duplicate rewards.

**Tune:** Use a few representative tokens for large amounts; preserve the exact final total.

**Failure check:** Skip animation, resize during travel, and replay. The final balance and destination position must remain correct.

**Adapted prompt:** Make [earned items] travel into [counter]. The movement should explain the transfer and finish at the exact earned total.

**Evidence:** [@op7418](https://x.com/op7418/status/2104085539419021491). Creator description/prompt; verify the visual when fidelity matters.

<a id="contract-burst-return"></a>

## A particle form that contracts, bursts and returns

**Mechanism:** A recognizable particle form passes through concentrated anticipation, rapid expansion and a legible return using persistent particle identities.

**Build:**

1. Give particles stable home coordinates and seeded variation; define an inward target and outward displacement for each identity.
2. Author separate envelopes for contraction, expansion, brightness and return. Reach a compact focal point before the expansive gesture.
3. Blend particles back to their own home coordinates; let trails and bloom decay instead of resetting the entire image.

**Tune:** Separate scale from exposure so brightness is not the only sign of anticipation. Keep some spatial structure visible in the burst. Use different durations for compression and release.

**Failure check:** Inspect pre-burst, peak expansion and reassembly. No random reseeding, teleportation or frame-filling white flash should hide broken continuity. Treat this as choreographed motion unless a physical model is actually implemented.

**Adapted prompt:** Create a [particle form] that gathers tension, releases into an expansive event, and reforms recognizably. Keep particle identities stable and make timing, extent, brightness and camera independently editable.

**Evidence:** Creator attributes the work to GPT-6 Astra. Frames around 3, 5, 7, 11 and 15 seconds were inspected through the creator-linked video. Source code, audio and continuous playback quality were not assessed. [source 1](https://x.com/Acoramaa/status/2104962747125412335)

<a id="measured-joint-motion"></a>

## Fit articulated product motion to measured reference poses

**Mechanism:** A measured pose trajectory preserves the characteristic acceleration, dwell and contact of a real articulated object.

**Build:**

1. Choose reference frames with clear geometry; record time, joint pose and uncertainty. Calibrate viewpoint before inferring rotation from projected width.
2. Fit a shape-preserving curve through the pose keys and explicitly set endpoint behavior. Separate camera travel from joint movement.
3. Compare rendered poses and per-frame angular changes to the reference. Preserve display content and lighting cues through articulation instead of matching only the silhouette.

**Tune:** Retain measured pauses and contact behavior. A monotone interpolant is useful on a one-direction segment; split direction changes into separate segments. Treat source-specific camera, lighting and blur numbers as examples.

**Failure check:** Inspect angular velocity for unintended extra peaks and inspect contact for artificial rebound. If pose and camera cannot be disentangled, obtain a clearer reference or label the estimate instead of calling it measured truth.

**Adapted prompt:** Animate [articulated object] from a small set of measured reference poses. Preserve its characteristic acceleration and contact, state uncertain measurements, and compare pose and velocity before adding surface polish.

**Evidence:** Creator prompt and linked product-hero-realism tutorial read at revision 255562b04b1e5ecaa4ba98e5c9aa191d5ba7f6fa. The tutorial’s measured values and visual result were not independently reproduced; guidance here is an original adaptation. [Creator post](https://x.com/everestchris6/status/2104965415164399895).

<a id="time-based-follow"></a>

## Consistent follow speed across refresh rates

**Mechanism:** Convert per-frame remaining-distance easing into a time-based exponential response, so the same held target settles at the same speed across refresh rates.

**Build:**

1. Choose a half-life in seconds: the time in which the remaining distance should halve. For a constant target, update with alpha = 1 - exp(-ln(2) * dt / halfLife).
2. If adapting a per-frame fraction a, record its reference frame rate f. Use halfLife = -ln(2)/(f*ln(1-a)); do not assume the original prompt specified f.
3. For a scrubbed film with a fixed target segment, evaluate directly from its initial position and elapsed time. For live moving targets, update from measured dt and understand the target is assumed constant within each sample.

**Tune:** Use half-life or settling duration instead of a frame fraction. A 12–19% fraction at an assumed 60 Hz corresponds to roughly 90–55 ms half-life; these are conversion examples, not universal taste settings.

**Failure check:** Compare equal elapsed time at 30, 60 and 120 Hz and irregular partitions with a held target. Test target reversals separately: first-order following preserves position but changes velocity abruptly; use a spring when momentum continuity matters.

**Adapted prompt:** Make [follower] respond consistently across refresh rates. Specify its response in time units, verify equal-time positions with a held target, and choose a spring instead if a reversal must retain momentum.

**Evidence:** September 28 creator prompt explicitly says it is used for Opus 5.5 motion. Text retrieved through the completed Apify run. The frame-rate correction, half-life conversion and implementation are original engineering synthesis; no associated visual output inspected. [Creator source](https://x.com/notdwd/status/2104719555394232743). See the [worked conversion](../time-based-follow.md).
