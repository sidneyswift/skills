# Time-based following instead of a fixed per-frame fraction

A [September 28 Opus 5.5 motion prompt](https://x.com/notdwd/status/2104719555394232743) proposes a remaining-distance fraction each frame. The creator's workflow is attributed in their own retrieved post. No resulting video was inspected. The correction below is original mathematical synthesis, not a claim that the creator's actual renderer is defective.

## Why the units matter

With a constant target, the remaining error after n frames is `error0 * (1-a)^n`. At twice the refresh rate, the same per-frame fraction consumes that error twice as quickly in wall-clock time. A fixed offline frame rate can make this recipe valid, but it needs to be specified.

Use `alpha = 1 - exp(-ln(2) * dt / halfLife)` and `value += (target-value)*alpha`. The original [motion kernel](../assets/motion-kernel.mjs) exposes `followHalfLife(value, target, dt, halfLife)`; both time arguments are seconds. `expm1` keeps the calculation accurate for small intervals.

For example, 80 ms half-life removes half the remaining error every 80 ms and about 95% after 346 ms. Adapt taste in time units. To translate an existing fraction `a` at reference rate `f`, use `halfLife = -ln(2)/(f*ln(1-a))`. Assuming 60 Hz, the source's 12–19% range becomes about 90–55 ms. The source did not specify 60 Hz. A two-to-four-frame stagger would likewise mean about 33–67 ms only under that assumption.

## Choose the right mechanism

- **Held target:** updates compose exactly over elapsed time regardless of how time is partitioned.
- **Moving target:** each update assumes the sampled target was held during its interval. Input sample rate still affects the path; this is not perfect equivalence for arbitrary input.
- **Reversal:** position is continuous, velocity can jump. Use the spring/release machinery for a dragged object that should retain momentum.
- **Film scrubbing:** evaluate the closed form from a segment's start value and elapsed time; do not depend on previous rendered frames. Preserve event times if targets change.
- **Background pause:** decide whether the art should catch up or pause. Clamping dt deliberately changes elapsed-time behavior; document that choice.
- **Completion:** exponential following approaches its target asymptotically. Use an explicit duration for an exact timed arrival, or a perceptual error threshold and final snap for interactive idle detection.

Verification: [tests](../scripts/test-follow.mjs) compare 30/60/120 Hz, irregular intervals, conversions, half-life, zero-time retarget and invalid inputs. These numerical tests establish the held-target calculation, not subjective motion quality.
