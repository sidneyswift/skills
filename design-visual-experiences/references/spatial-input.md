# Spatial input that preserves user intent

Useful for explorable scenes, object viewers and simulations with selectable objects. [Mola's creator, September 27](https://x.com/xenit_v0/status/2104118647274787111), attributes the game to GPT 6 Astra. This study inspected selected code at [`d2b3123e`](https://github.com/xenitV1/mola/tree/d2b3123e2dcbdc2163a5d14f96e16b51c36c8c2e); it did not assess the game's visual quality.

## Make a gesture own its consequence

A finger lifting after a camera pinch must not select the object underneath it. Keep gesture history until all participating contacts finish. A tiny final movement does not turn a drag back into a tap.

Original adaptation of the inspected mechanisms:

1. Track contacts by pointer identity. Begin with a tap candidate; crossing a movement threshold permanently consumes that candidate for this gesture.
2. When a second contact joins, snapshot camera zoom, rotation, contact separation and contact angle. Consume the tap candidate. Compute subsequent changes relative to that baseline, not by repeatedly multiplying the last camera value.
3. Apply scale from the separation ratio. Wrap angular difference with `atan2(sin(delta), cos(delta))` to avoid an unintended full revolution across the signed-angle boundary. Reject near-zero baseline separation before division.
4. Retain the consumed-tap state after one finger lifts. A new independent gesture can become a tap again once all contacts end. Explicitly define third-contact behavior and baseline changes; do not let incidental pointer order define it.
5. On cancellation or lost capture, clear owned state before releasing remaining captures, because capture-release callbacks can re-enter cleanup. Ignore stale releases. Disabling the world for a modal must prevent actions and clear active interaction.

The source also maps parallel two-finger travel into rotation. That is one control scheme, not a universal gesture standard. Choose pan/orbit/twist mappings for the task and explain unfamiliar ones. Its fixed movement and separation thresholds are examples to tune at the intended device scale.

## Preserve the point the user is manipulating

The inspected handler passes the finger midpoint to `zoomAt`; that verifies intent, not the renderer's world-anchor implementation. For a new renderer, independently check that the world point under the chosen anchor remains under it while zooming. Perspective scenes need an explicit anchor surface or depth; a screen-space midpoint alone does not prove anchored zoom.

Offer keyboard and named controls alongside direct manipulation. Keep page scrolling usable outside the interactive region. These are engineering recommendations, not features verified in Mola.

## Tests that reveal the failures

| Scenario | Expected consequence |
|---|---|
| Double separation, then return to the starting separation | Starting zoom restored without accumulated drift |
| Pinch, release either finger, then release the other | No object tap; a subsequent independent tap works |
| Cross 179° to −179° | Small angular change, not a revolution |
| Cancel or lose capture, then deliver old moves/releases | No camera movement or selection from stale contacts |
| Disable interaction during a gesture | Active input clears; no world action |

Five independent scenarios covering these cases passed against the pinned camera source in a local event harness. The creator's camera tests were read, not run through their full test runner. Browser event ordering, mobile feel, three-contact transitions and the complete game remain unverified. This is a source-backed behavior study, not a visual benchmark.

## Related character finding: travel is not contact

The inspected pose code advances its walk phase from distance traveled, blends into sitting/standing poses, and adjusts body height using the lowest shoe corner. Those mechanisms can reduce speed mismatch and ground penetration. They do not establish a world-space planted foot: source root smoothing and pose motion can still produce sliding. Use a marked-floor inspection before claiming contact fidelity; use [planted-foot guidance](patterns/characters.md#planted-foot-ik) when the brief requires it.

## Attribution and reuse

Source code is GPL-3.0; README lists separate third-party asset licenses and reserves the Mola name/logo. This skill bundles no Mola code or assets. The steps above are original engineering guidance. For source adaptation, inspect the actual license and asset provenance instead of assuming the repository's headline license covers everything.

Original adaptation prompt:

> Build direct exploration of [scene]. Make camera gestures and object actions mutually exclusive. Preserve gesture ownership through finger release and cancellation, define the zoom anchor, and test reversals and interrupted input. Keep the visual affordance simple and verify the actual target device before judging how it feels.
