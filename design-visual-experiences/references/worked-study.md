# Worked study: Elastic Matter

This original Canvas study makes one research-derived mechanism executable: a recognizable form changes state with staggered spring responses and can be pulled and released. It is a small reusable mechanics example, not a reproduction of a creator's film or a finished client campaign.

## Run and inspect

From this skill directory:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory assets
```

Open `http://127.0.0.1:8765/motion-study.html`. Local HTTP serves the ES module; opening the HTML as a file may block that import. Change the port if it is in use. The study uses no network assets or third-party dependencies.

- Choose Orbit, Wave, or Fold; change again before the transition ends.
- Drag the sculpture, release slowly, then release with a fast flick.
- Focus the canvas and use arrow keys; Escape releases it.
- Play the 12-second sequence; pause/resume, scrub, and reset.
- For reproducible stills use `motion-study.html?frame=5.4`. The sequence has target changes at 1, 4.5, and 8 seconds. It finishes at 12 seconds; it is not certified as a seamless loop.

## How to adapt it

Read [the HTML](../assets/motion-study.html) with [the kernel](../assets/motion-kernel.mjs). `shape(u,state)` defines the visual vocabulary. Each rib retains its identity `u` while its center, angle, and length interpolate among targets. Unwrapped angles avoid taking the long rotation accidentally. `property(t,delay)` evaluates a time-addressable spring track; the per-rib delay makes a traveling response. `currentPull(t)` separates direct drag from analytic release. The small offset ink layer and stable grain are the study's own art direction, independent of the motion mechanism.

For a new project, change the subject and silhouette first. Then adjust total response spread, damping, and frequency. Do not immediately add particles, lens effects, or a camera move. Preserve a clear relationship between the user's action and the result. If the geometry changes substantially, inspect intermediate states again: correct endpoints do not guarantee a good morph.

The helper assumes finite numeric input, positive natural frequency, nonnegative damping, and time-ordered events. Retargeting preserves velocity when the spring parameters remain constant. Do not switch its parameters mid-track and assume continuity; carry position/velocity into a new regime instead. Long-lived applications should compact settled event history rather than accumulating events forever.

## Kernel reference

| Function | Purpose | Important constraint |
|---|---|---|
| `springState(t,x,v,omega,damping)` | Exact displacement and velocity around equilibrium | Seconds; velocity per second; `omega` is angular frequency |
| `targetTrack(t,initial,events,omega,damping)` | Seekable response to successive target changes | Ordered events, same spring parameters |
| `release(t,from,velocity,target,omega,damping)` | Release from a held position with momentum | Match coordinates and clock with input sampling |
| `hermite(t,t0,t1,p0,p1,v0,v1)` | Match endpoint position and velocity inside an interval | Outside interval it clamps; surrounding motion must match endpoints |
| `hash(seed)` | Stable identity variation | Same ID yields same value; do not use render-frame seeds |
| `loopWave(t,period,seed)` | Periodic smooth variation | Positive period; apply to appropriate geometry |
| `paintTick(t,rate)` | Separate stepped texture time | Keep camera/pose on continuous time |
| `cameraPoint(point,focus,zoom,anchor)` | Shared orthographic world-to-screen mapping | Use the inverse mapping for pointer input |

## Mechanical validation

```sh
node scripts/test-motion.mjs
```

The tests check oscillator initial conditions and velocity, settling, position/velocity continuity after rapid retargets, seek-order independence, release momentum, Hermite endpoint velocities, periodic value/velocity, and paint-clock stepping. These invariants catch implementation failures that a screenshot cannot. They do not score aesthetic quality.

Reduced-motion mode makes state-button changes immediate and removes release oscillation; explicit sequence playback remains user-initiated. Verify the target project's own accessibility and performance requirements before reuse. This small study has no audio or video exporter.
