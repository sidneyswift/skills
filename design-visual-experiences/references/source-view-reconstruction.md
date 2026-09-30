# Match source views before polishing a reconstructed scene

Use for video-derived spaces, spatial exhibits and scene-aware character motion. Extend [source-grounded reconstruction](patterns/worlds.md#source-grounded-reconstruction) when the source appearance matters; fictional scenes need not imitate a captured room.

## Evidence

[AHa-3D](https://kevinxu02.github.io/real2sim-indoor-site/) by Congrong Xu, Siyuan Bian and Jun Gao explicitly uses GPT-6 Astra with specialist tools. The [September 27 creator post](https://x.com/siyuan_bian/status/2104359501394485262) and September 2026 article were inspected September 29. The article describes estimated cameras, segmentation, fused geometry, measurements, outline comparisons, support checks and scene-aware motion refinement. Its final stylized-video stage uses MiniMax H3; those videos must not be labeled Astra-only renders.

**Observed live:** loaded the open-concept room, used its tabletop camera preset, changed the island surface from pale stone to walnut, and reset it to the original surface. These interactions worked in this browser. No frame-rate, reconstruction-accuracy or contact-physics claim was tested. Several article video elements were unavailable; neither every example nor the full motion sequence was inspected.

**Inspected code:** [overlay compositor](https://github.com/KevinXu02/aha-3d/blob/82f4b1110cfe4b55fff19df3b3790852ce07b171/tools/layout_inspection/overlay.py), its three tests, and [contact-refinement documentation](https://github.com/KevinXu02/aha-3d/blob/82f4b1110cfe4b55fff19df3b3790852ce07b171/docs/CONTACT_REFINEMENT.md). All three selected compositing tests passed. The overlay combines matching RGBA passes without depth; its report distinguishes that view from an occlusion-aware depth view. This is not a full Blender or reconstruction test. Apache 2.0 license inspected; dependencies and assets have separate terms. No third-party implementation or prompts bundled.

## Original adaptation: a useful reconstruction loop

1. **Choose anchor views.** Keep the source timestamp, camera, image dimensions and crop attached to each comparison. Start with the room envelope and two or three dominant forms. Confirm scale against an independent known dimension when metric accuracy matters; estimated metric output remains an estimate.
2. **Expose one disagreement.** Render one object's silhouette over the corresponding source view. Use a restrained contrasting color and a stable object ID. Hide internal trim until the outer proportion is correct. Classify the mismatch as camera, position, orientation, size or shape before editing it.
3. **Use two diagnostic views.** An X-ray outline reveals model edges even behind reference geometry; a depth-aware view shows occlusion. Check a second camera before accepting an ambiguous fix. Matching one silhouette alone cannot settle hidden geometry or depth.
4. **Keep edits addressable.** Store dimensions, pivots, material slots and interaction state by object ID. Changing a finish should not destroy a cabinet's opening behavior. Preserve an initial scene snapshot so reset restores both appearance and state. Introduce one convincing interaction before adding a room full of controls.
5. **Make contact targets follow objects.** For a character touching a moving table, define the target in the table's local frame and transform it into the shared scene frame over the intended contact interval. Review approach, contact onset, sustained contact and release. A hand that is close at one frame can still slide or snap across the interval.
6. **Separate capture repair from animation invention.** When preserving captured motion, start with rigid placement and explicit contact constraints. Do not silently resize a person or alter local joint poses to conceal a room-scale error. If the brief permits new choreography or IK, treat it as a deliberate authored variant. The source repository's restricted contact route is not a universal ban on IK.

**Tune:** overlay opacity, diagnostic camera selection, geometric tolerances, hinge pivots, contact intervals, and the balance between contact residuals and temporal continuity. Keep guessed surfaces and occluded details distinguishable from measured ones.

**Failure checks:** same camera/crop for each before/after; a second view still agrees; objects retain support after edits; reset restores materials and articulation; contact does not improve at the cost of a visible jump, planted-foot slide or implausible body scale. Label unresolved residuals rather than hiding them through framing.

**Adapted prompt — original:** Turn [reference footage] into an editable [spatial experience]. Match its main proportions from corresponding source views before adding surface detail. Give objects stable identities and demonstrate [one interaction]. Compare silhouettes and depth separately. For [character action], define contact against the actual moving object and inspect approach, hold and release. Preserve uncertainty where the source is missing; distinguish scene renders from any generative video treatment.

## Inspect scan and model through one camera

The [kitchen twin demo](https://frank-zy-dou.github.io/kitchen-twin/) offers another diagnostic route: a movable wipe between scan and model. [Frank Dou's September 11 post](https://x.com/frankzydou/status/2098460193319186578) explicitly credits GPT-6 Astra. Selected inline viewer code and live comparison controls were inspected; the upstream reconstruction pipeline, metric accuracy, acceptance scores and robot simulation were not verified. See [dated evidence and limits](updates/2026-09-30-shared-camera-comparison.md).

**Original adaptation:** use this when a spatial experience should let people examine what was captured, inferred or changed.

- Keep one camera transform, projection and full-stage aspect ratio for both layers. Render each through a complementary scissor region of that full viewport. Moving the divider changes the reveal, not the camera or object scale. A separately fitted camera in each half can disguise positional error.
- Put both layers into a documented shared coordinate frame before rendering. Check an asymmetric landmark, known dimension and floor direction. A convincing wipe does not establish metric accuracy; conversion or alignment errors can survive a single view.
- Preserve inspection context: camera, selected object ID, cutaway height and display settings. Save the ordinary layer toggles before entering comparison, disable conflicting toggles while it owns visibility, and restore them on exit. Restore temporary renderer state after both passes, including on an early return or error.
- Route picking to the layer exposed under the pointer. Compute the pointer in full-canvas coordinates, determine which side of the divider it occupies, and intersect only that side's selectable geometry. Apply the visible cutaway test to hit points too. Test near the divider and on overlapping objects so hidden geometry cannot steal clicks.
- Separate geometry review from surface review. Use neutral silhouette or depth passes for shape decisions; then inspect materials. Captured color may contain baked lighting while the model receives new lighting, so a color difference alone is not proof of a wrong material.
- Keep draft, measured and inferred states visible. Treat acceptance scores as metadata until their definition and validation are available. Sparse observations and shiny or thin surfaces deserve explicit uncertainty rather than a polished appearance being mistaken for evidence.

**Tune and check:** divider position, clipping height, lighting and selected camera. Exercise both divider extremes, resized and high-density displays, orbit/top-down changes, clipped objects, selection on either side, and entry/exit with unusual toggle combinations. Verify the same landmark remains stationary as the divider moves. Do not claim these checks passed merely because the reference exposes the controls.

**Adapted prompt:** Build a scan/model inspection view for [scene]. Share one full-view camera across both layers and reveal them with a movable divider. Preserve selection and cutaway state, make picking respect the visible layer, restore normal visibility on exit, and label uncertain geometry. Show alignment from two views before using the display to judge model quality.
