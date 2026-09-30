# Fieldwork: three executable mechanism studies

Open [mechanism-studies.html](../assets/mechanism-studies.html) through a local HTTP server because it imports an ES module. From the skill directory:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory assets
```

Visit `http://127.0.0.1:8765/mechanism-studies.html`. Choose another free port if needed. No install, external assets, network calls, audio, or third-party runtime is required. The examples are original illustrations of selected mechanisms, not reproductions of creator videos or production-ready scenes.

## One wind, many responses

144 plants in three depth layers share a spatial wind function. Height and layer alter visible response; a gust is a timestamped envelope traveling across the field. Stable per-plant random values preserve the composition when seeking.

Adapt the field, plant silhouettes, palette and response scale independently. Store events as time/strength pairs to replay them. Do not replace shared wind with unrelated random displacement per frame. The plant drawing remains deliberately simple; it does not model leaf collisions or full plant dynamics.

## Planted feet

A straight-travel gait fixes each stance foot in world coordinates. The root advances while two-segment inverse kinematics solves each leg. During swing the foot follows a smooth path to the next contact. Ground marks make unwanted slip easy to see.

`footAt` is a procedural straight-walk starting point, not a terrain, turning or locomotion system. For an uneven scene, plan contact positions and normals against the ground; retain the contact constraint while solving the body. `solveLimb` clamps unreachable targets and returns `clamped` so the caller can adjust its pose rather than silently stretching bones.

## Through the aperture

Nested ellipses grow in constant scale ratios with `logZoom`. At each scale handoff the layer index, color and dot phase map to the same visible layer. The transport stops at 20 seconds; this entire study is not presented as a seamless 20-second loop.

Extend the aperture into a scene transition by assigning actual content to each scale band. Keep a visual anchor through the handoff. A mathematically continuous camera does not guarantee legible staging.

## Helpers and checks

[experience-kernel.mjs](../assets/experience-kernel.mjs) supplies named random streams, index-based random samples, positive logarithmic zoom, event envelopes, shared wind, a clamped limb solver and absolute-time foot placement. These functions are small reference implementations, not a required framework.

```bash
node scripts/test-experience.mjs
node scripts/test-motion.mjs
python3 scripts/test-library.py
```

The numerical tests cover repeatability, zoom ratios, envelope onset, limb lengths, reach clamping, bend direction, planted contact and gait continuity. Browser checks covered the three studies, play/pause, seeking, a gust, reset, keyboard seeking, narrow layout and the aperture handoff. Reduced-motion preference handling is implemented and code-reviewed; the preference was not toggled in the browser. No target-device frame-rate benchmark was performed.

For analytic springs and velocity-preserving transitions, use the separate [Elastic Matter study](worked-study.md).
