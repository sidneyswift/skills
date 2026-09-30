# Interaction patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [An assembly that can be understood in either direction](#exploded-assembly)
- [A visual model constrained by a real parts inventory](#buildable-bricks)
- [A movable inspection lens over aligned layers](#reveal-under-surface)
- [An irreversible-looking surface action with reversible state](#cleaning-mask)
- [A simple control with several meaningful consequences](#one-input-meaning)
- [Emergent pursuit with deliberately imperfect opponents](#readable-chase)
- [A spatial metaphor backed by real system state](#operational-world)
- [A sketchbook with real pages and drawing interaction](#page-as-surface)

- [A working mechanism that keeps its phase while taken apart](#phase-coherent-explode)

<a id="exploded-assembly"></a>

## An assembly that can be understood in either direction

**Mechanism:** Parts retain their assembly relationships while construction, separation and camera exploration follow distinct phases.

**Build:**

1. Store stable part IDs, local pivots, exact rest transforms and assembly order. Introduce a few representative components at readable scale before unveiling a dense whole when the audience needs its shape vocabulary.
2. Assign collision-aware separation paths driven by one reversible rest-to-exploded parameter. Schedule camera travel independently so the view can explore a held separated field. Highlight a selected part/connection without hiding its surrounding context.
3. Give initial construction its own arrival phase and stagger; group/height ordering can clarify a stylized build but does not prove structural validity. A return can contract directly to rest transforms instead of replaying initial construction.
4. Preserve a wide landmark at departure and return, with an orientation pause before contraction. Derive transforms from stored poses rather than accumulating offsets, so reverse scrubbing lands exactly on the same assembly.

**Tune:** Expose component-introduction count/hold, arrival stagger, separation distance, camera clearance and final hold. Separate enough for understanding, not maximum distance. Provide step/free-scrub controls for an interactive explanation; let readable hero geometry, not sheer part count, carry close passes.

**Failure check:** Scrub backward and select every part; labels and transforms must stay attached to the correct piece. Review intermediate camera positions for clipping, foreground occlusion and crop seams. Derive any precise inventory claim from actual instances; a static parts list is not a progress meter. Return-to-whole is not a seamless loop: if repeating, compare opening/closing object transforms, camera and velocity.

**Adapted prompt:** Explain [assembly] through a few readable components, an ordered first build, independent exploration of its separated parts and a precise return to the whole. Keep part identity stable and make the structure understandable in either direction.

**Evidence:** [@deedydas](https://x.com/deedydas/status/2103174501345493197), [@CurieuxExplorer](https://x.com/CurieuxExplorer/status/2103038628071133588): creator descriptions/prompts. [Higgsfield Notre-Dame study](../research/higgsfield-motion.md#notre-dame--component-introduction-and-independent-camera-travel): all435 source frames at640px, with seven native1600×1200 checks. Three introductory parts, height-progressive construction, an exploded close passage and a contracting return are visible; the final whole differs from the empty opening. Separate phase/state rules above are original synthesis. Exact block count, physical buildability, model workflow, source code, audio and temporal playback were not verified.


<a id="buildable-bricks"></a>

## A visual model constrained by a real parts inventory

**Mechanism:** The same discrete part list drives the model, instructions and bill of materials.

**Build:**

1. Quantize the source into supported colors and dimensions.
2. Tile the volume with available parts and create an assembly order.
3. Check connectivity, intersections and support, then derive all exports from the final inventory.

**Tune:** Prefer robust structural connections over a perfect front-view color match. Separate computer checks from physical build testing.

**Failure check:** Rebuild using a reduced inventory. Parts counts, rendered steps and shopping list must agree exactly.

**Adapted prompt:** Convert [image/form] into a buildable discrete assembly with consistent geometry, instructions and inventory.

**Evidence:** [@johnkarp](https://x.com/johnkarp/status/2103802201739256312), [@johnkarp](https://x.com/johnkarp/status/2103802213655294212). Creator description/prompt; verify the visual when fidelity matters.


<a id="reveal-under-surface"></a>

## A movable inspection lens over aligned layers

**Mechanism:** The reveal works only when exterior and interior imagery share registration.

**Build:**

1. Align both layers in the same image coordinate system.
2. Transform pointer or touch position into that local space and mask the interior with a feathered aperture.
3. Provide a keyboard or slider alternative that can reveal the same information.

**Tune:** Keep lens lag minimal for inspection; feather enough to avoid a pasted-on circle.

**Failure check:** Resize and change crop. The interior must stay aligned with the exterior, including near image edges.

**Adapted prompt:** Let viewers inspect [object] through a movable reveal lens, keeping both layers registered and usable without hover.

**Evidence:** [@iamtanzil_](https://x.com/iamtanzil_/status/2103459848793084047). Creator description/prompt; verify the visual when fidelity matters.


<a id="cleaning-mask"></a>

## An irreversible-looking surface action with reversible state

**Mechanism:** Cleaning feels satisfying when the tool changes a persistent surface field.

**Build:**

1. Store dirt or coverage in a texture or grid.
2. Project the tool footprint onto the surface and reduce coverage with pressure and dwell time.
3. Derive wetness, debris and progress from the changed area rather than pointer distance.

**Tune:** Control edge softness and flow; let reset restore a known initial field.

**Failure check:** Sweep the same area twice. Progress must count newly cleaned area only, and off-object input must not count.

**Adapted prompt:** Build [surface treatment] with a persistent coverage map so the visible result and completion measure reflect actual work.

**Evidence:** [@chongdashu](https://x.com/chongdashu/status/2102674509593796808). Creator description/prompt; verify the visual when fidelity matters.


<a id="one-input-meaning"></a>

## A simple control with several meaningful consequences

**Mechanism:** Depth comes from context and timing rather than a large control vocabulary.

**Build:**

1. Choose one primary action and define its effect in each meaningful state.
2. Make the state visible through pose, environment or a concise cue.
3. Add variation in timing, obstacles or resources before adding more buttons.

**Tune:** Keep the first successful interaction easy to discover; make failure explain the rule.

**Failure check:** Test with no instructions. A new user should understand the action and predict one next consequence.

**Adapted prompt:** Build [small experience] around one clear input whose timing and context produce interesting choices.

**Evidence:** [@blitast_studio](https://x.com/blitast_studio/status/2104003920251257328), [@DannyLimanseta](https://x.com/DannyLimanseta/status/2104215873120764032). Creator description/prompt; verify the visual when fidelity matters.


<a id="readable-chase"></a>

## Emergent pursuit with deliberately imperfect opponents

**Mechanism:** Pursuers become part of the player strategy because they predict, overshoot and collide.

**Build:**

1. Steer toward playerPosition plus playerVelocity times a prediction horizon.
2. Give opponents limited turn ability and imperfect avoidance.
3. Make collisions, damage and recovery visible through coordinated feedback.

**Tune:** Tune one opponent in an empty arena before adding density; preserve a clear player silhouette.

**Failure check:** The player should be able to intentionally cause an opponent mistake. If outcomes feel random, reduce speed or improve telegraphing.

**Adapted prompt:** Create [chase mechanic] where readable opponent prediction creates opportunities for skillful escapes and chain reactions.

**Evidence:** [@froessell](https://x.com/froessell/status/2103789415323562325). Creator description/prompt; verify the visual when fidelity matters.


<a id="operational-world"></a>

## A spatial metaphor backed by real system state

**Mechanism:** A world becomes useful when its inhabitants and objects represent current operations.

**Build:**

1. Map each entity to a stable system ID and a small state vocabulary.
2. Animate transitions from real events, distinguishing queued, active, failed and complete.
3. Offer a direct route from the visual entity to its underlying details.

**Tune:** Use spatial organization to aid recognition; do not make essential information depend on watching an animation.

**Failure check:** Feed out-of-order and repeated events. The world must not show completion early or duplicate an entity.

**Adapted prompt:** Represent [workflow] as [spatial metaphor], with every visible state grounded in actual events and accessible details.

**Evidence:** [@kum1ta](https://x.com/kum1ta/status/2103998389058740521), [@sanjay_khadka07](https://x.com/sanjay_khadka07/status/2104102479927620029). Creator description/prompt; verify the visual when fidelity matters.


<a id="page-as-surface"></a>

## A sketchbook with real pages and drawing interaction

**Mechanism:** The book has a spatial page model while each page owns its own drawing state.

**Build:**

1. Render page art to textures or 2D surfaces.
2. Deform page geometry around a turn axis, retaining front/back mapping.
3. Store drawing strokes in page-local coordinates and transform input through the current page view.

**Tune:** Keep curl readable before adding paper texture; distinguish page-turn gestures from drawing gestures.

**Failure check:** Turn forward and backward, draw near an edge, and resize. Marks must remain on the intended page.

**Adapted prompt:** Make [book/journal] a tactile interactive object with coherent page turns and persistent page-local artwork.

**Evidence:** [@kloss_xyz](https://x.com/kloss_xyz/status/2104021884350439465). Creator description/prompt; verify the visual when fidelity matters.

<a id="phase-coherent-explode"></a>

## A working mechanism that keeps its phase while taken apart

**Mechanism:** One clock controls operation while a separate inspection parameter controls where the parts are displayed.

**Build:**

1. Represent part identity, assembled transforms and inspection offsets separately from gear or linkage phase.
2. Derive connected rotations from one master phase and explicit ratios; compose local operation with inspection placement rather than overwriting either transform.
3. Let scroll or chapter selection change only inspection progress. Readouts, pause and speed controls use the operating clock.

**Tune:** Prove the assembled relationships before spreading the parts. Use rests for labels; keep pause independent from interface navigation.

**Failure check:** Scrub inspection backward while operation continues, then pause and inspect another part. Relative phases and computed readouts must remain consistent. Visual separation does not prove the assembled mechanism is physically correct.

**Adapted prompt:** Build an inspectable [mechanism] whose operation continues as its parts separate. Use independent operation time and inspection progress, preserve part identity, and verify the relationships shown by the readouts.

**Evidence:** Creator prompt retrieved in full; selected frames from the comparison video inspected. Live controls, source code, mechanical correctness and claimed production times were not independently verified. [source 1](https://x.com/theparuchh/status/2105009377002299711) [source 2](https://x.com/theparuchh/status/2105009470292013286)
