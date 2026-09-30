# Prepare a generated face for controllable motion

Use when a generated character looks convincing in a still but its eyes, lids or brows cannot be animated cleanly. Route performance timing through [embodied narration](embodied-narrator.md) only when a character actually guides an explanation.

## Source and observed workflow

[Catriel Mamani's September 28 post](https://x.com/Catriel_Mamani/status/2104535340979740993) credits GPT-6 Astra and Tripo. A creator reply says separate face meshes are needed for this workflow. Selected muted tutorial frames show Tripo UV preparation (~0:29), a caption describing rebuilding iris/lash/brow features and cleaning textures (~0:42), texture cleanup (~0:57), lashes and eye shading (~1:08), a facial-controller panel (~1:28) and a final profile pose (~1:54). The ~1:17 caption attributes facial rig/controller creation to Astra. The ~1:40 caption separately identifies ActorCore for a body rig and expresses dissatisfaction with it. Do not credit Astra with every asset or treat this as validated full-body rigging.

These are sampled visual evidence and creator descriptions. No Blender file, scripts, weights, topology or export was inspected; audio, controller response and deformation correctness remain unverified. No character assets or full prompts are bundled.

## Original implementation guidance

1. **Audit what makes the face visible.** In a preserved copy, identify which irises, lashes, brows and shadows are geometry, texture, material effects or combinations. Hide one component at a time. A duplicate painted iris behind a moving eye can produce a ghost feature; removing geometry alone will not fix the texture. Record what should stay static and what must move.
2. **Choose a representation per feature.** Separate objects can suit stylized eyes or brows; connected deforming surfaces and shape keys can suit other faces. Separate meshes are a technique in this tutorial, not a universal requirement. Preserve identity, UVs and material assignments while replacing only the features that prevent control. Keep an untouched source for comparison.
3. **Repair in an inspectable order.** Establish clean base color, then movable features, then shading. Compare a neutral unlit view and the intended lighting so a painted shadow is not mistaken for a geometry defect. Resolve a small texture artifact directly when that is clearer than repeatedly regenerating the entire character.
4. **Expose understandable controls.** Provide neutral/reset, gaze, left/right blink, brows and mouth/jaw controls as appropriate. Give each a documented range and avoid changing unrelated features from one control. Preserve manual editing access alongside scripted animation. This is an interface requirement, not proof that the underlying rig is correct.
5. **Test combinations before acting.** Inspect half and full blinks, side gaze plus blink, smile plus jaw opening and return to neutral from front and profile. Look for lid gaps, eye penetration, floating lashes, doubled brows and mouth discontinuities. Isolated extremes can pass while combined poses fail; constrain or correct the combination instead of simply adding stronger expressions.
6. **Verify the destination separately.** For browser delivery, test the exported asset's actual supported animation channels and materials. For a film, inspect representative rendered poses. A Blender controller panel does not prove that a web export carries those controllers or that the result deforms correctly.

Tune gaze limits, lid closure, brow travel, jaw range, feature offsets and expression intensity. Keep proportions and neutral appearance stable while tuning; changing the base face and the motion simultaneously makes regressions difficult to locate.

**Adapted prompt:** Audit this generated character's facial features before rigging. Propose which parts remain painted and which need independent deformation. Preserve the original, expose a small editable control set, demonstrate combined poses and neutral reset, then verify the actual delivery format. Identify unsupported claims and unresolved deformation defects.
