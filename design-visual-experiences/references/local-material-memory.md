# Local deformation with material memory

Use for tactile toys and playful product objects where a local press or pull should feel attached to the material. Read alongside [interactive 3D](interactive-3d.md). This approximation does not provide cutting, self-collision or calibrated physical behavior.

## Evidence

[EverettFish's September 23 post](https://x.com/everettfish0408/status/2102685254167462028) credits GPT-6 Astra and Blender. The [repository](https://github.com/EverettFish/squishy-skill) was inspected at `004ed4d06ee349f99060f7c26b41248510f5a8e5`: interaction notes, deformation module, selected import/raycast/input/render code, README and license notes.

The source preserves rest vertices, maps deformed hits back with triangle barycentric coordinates, caches compact contact weights and sums local displacement fields. A fast oscillator and slow memory govern recovery. The template includes release handlers for cancellation, lost capture, blur and hiding. These were read, not stress-tested.

In the [live demo](https://everettfish.github.io/squishy-skill/), pulling the left facial area distorted that area and the nearby eye. It subsequently approached its earlier shape. Recovery was changed from5 to12 seconds; post-release readback showed a shrinking displacement with the contact still retained. This verifies selected interaction behavior, not an exact settling duration. Template/deployment equivalence, keyboard, touch, repeated grabs and frame-rate robustness were not established.

Code/documentation are MIT licensed; example character and asset rights are separately reserved. No third-party implementation or character assets are bundled here.

## Original design adaptation

**Choose a material story.** Decide whether a grab should feel gummy, springy or compressible. Tune immediate compliance, release oscillation and slow recovery independently. Avoid using one long easing curve for every phase: it often makes the initial response feel delayed when only the residue should be slow.

**Keep a stable material address.** After importing the model, put geometry and raycast hits in a common coordinate system. Resolve a contact to the undeformed surface and retain that address while the visible surface moves. Recompute each frame from the rest shape plus current contributions, rather than repeatedly adding offsets to already-deformed vertices. This makes recovery and repeated grabs easier to reason about.

**Localize the field.** Make the effect fade smoothly to zero inside a chosen support radius. Preview the support region as a debug overlay; a cheek gesture should not unintentionally move the feet. Apply the same displacement field to attached facial and clothing parts so they remain part of the object. Nearby disconnected parts may need an explicit group mask rather than proximity alone.

**Separate object manipulation from camera manipulation.** Show an understandable mode or modifier for rotation. While a contact is held, give that gesture to the object. On release or cancellation, retire the input ownership immediately while allowing visible material recovery to continue. A recovering dent need not remain an active pointer contact.

**Make imperfections deliberate.** A physically loose toy can stretch dramatically, but define the limit before faces invert or surfaces intersect distractingly. Tune with an exaggerated pull, not only a pleasing idle pose. Keep the silhouette recognizable at rest and check attached details during the largest intended deformation. Choose a different solver when true volume conservation, collision or tearing is central to the brief.

## Parameters and checks

Expose support radius relative to object size, maximum pull distance, press depth, held-response stiffness, release damping and slow-memory fraction/recovery. First vary one control at a time using the same gesture and view. Then test short and long holds, repeated nearby contacts, off-object drags and interruption while held. Record visible geometry and input state separately; a changed status label alone is insufficient.

Inspect the rest state, maximum deformation, early release and late residue. Check remote vertices, attached eyes/text, normal updates and raycast bounds. A correct-looking first grab can hide stale bounds that break the second grab. For reduced motion, retain direct manipulation but reduce decorative rebound according to the user's needs.

**Adapted prompt:** Build a tactile [original object] with local pressing and pulling. Keep contacts anchored to the material, preserve attached details, and give release a fast elastic response plus a separately tunable slow residue. Provide a clear camera-control mode. Demonstrate extreme intended deformation, a repeated grab during recovery and cancellation before polishing the scene.
