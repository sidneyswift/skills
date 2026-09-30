# Characters patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [A character bible translated into a controllable rig](#identity-rig)
- [Walk cycles that keep feet attached to the ground](#planted-foot-ik)
- [Hands and tools constrained through an action](#grip-and-tool)
- [Secondary parts that express the character state](#emotional-secondary)
- [Pixel animation with deliberate pose timing](#pixel-performance)
- [Turn a still into a rig without inventing hidden art](#layered-portrait)
- [Retarget a motion clip to a simplified character](#motion-retarget)
- [Graphics anchored to a real performer](#tracked-body-type)

<a id="identity-rig"></a>

## A character bible translated into a controllable rig

**Mechanism:** The character stays recognizable because proportions and expression vocabulary are explicit.

**Build:**

1. Record silhouette, proportions, distinctive features and palette.
2. Build a hierarchy with pivots at anatomical or mechanical joints.
3. Produce a turnaround and expression lineup before staging a long sequence.

**Tune:** Make eye direction and pose readable at final viewing size; add secondary detail only after the lineup works.

**Failure check:** Compare front, side, back and extreme expressions. Features must not drift or detach under rotation.

**Adapted prompt:** Build [character] as a consistent rig with a small expression vocabulary, then prove identity across views before animating the story.

**Evidence:** [@pradeepXkapoor](https://x.com/pradeepXkapoor/status/2103176289482154373), [@akokoi1](https://x.com/akokoi1/status/2103149539880562718). Creator description/prompt; verify the visual when fidelity matters.


<a id="planted-foot-ik"></a>

## Walk cycles that keep feet attached to the ground

**Mechanism:** The body moves over a temporarily fixed support foot instead of sliding the foot beneath it.

**Build:**

1. Split each leg cycle into stance and swing.
2. Store the stance contact in world space and solve the leg toward it.
3. During swing, advance to the next contact along a raised arc; align foot orientation to terrain.

**Tune:** Tune stride length from travel speed. Clamp unreachable targets and choose a consistent knee bend side.

**Failure check:** Watch only the feet on a marked floor, then on a slope. Stance contacts must not skate or penetrate terrain.

**Adapted prompt:** Make [creature] walk with planted stance feet and purposeful swing arcs, adapting its stride to speed and terrain.

**Evidence:** [@vib3coded](https://x.com/vib3coded/status/2102450842070569099), [@victormustar](https://x.com/victormustar/status/2102707412704919910). Creator description/prompt; verify the visual when fidelity matters.


<a id="grip-and-tool"></a>

## Hands and tools constrained through an action

**Mechanism:** A tool interaction reads as effort when hands, feet and the contact point agree.

**Build:**

1. Define the tool path and its contact point first.
2. Solve hand targets on the tool and support contacts on the floor.
3. Add torso lean and recovery around that constrained action, then secondary cloth.

**Tune:** Keep the tool reachable throughout the cycle. Change grip intentionally rather than letting the hands slide.

**Failure check:** Inspect the action from the side. The tool must not pass through hands, body or supporting geometry.

**Adapted prompt:** Animate [character] using [tool] with fixed grip points, planted support and visible transfer of effort.

**Evidence:** [@MengTo](https://x.com/MengTo/status/2103155074705019158). Creator description/prompt; verify the visual when fidelity matters.


<a id="emotional-secondary"></a>

## Secondary parts that express the character state

**Mechanism:** Antennae, ears or accessories reinforce acting through controlled lag and pose.

**Build:**

1. Assign a resting pose to each emotional state.
2. Blend toward it with inertia and add impulses from meaningful body actions.
3. Keep small idle movement subordinate to intentional gestures.

**Tune:** Vary stiffness by material. Reserve stillness for attention or surprise rather than animating everything continuously.

**Failure check:** Mute the scene and hide dialogue. The emotional change should be legible from pose, eyes and the secondary feature.

**Adapted prompt:** Use [distinctive appendage] to reinforce [character] emotions with deliberate pose changes and material-appropriate follow-through.

**Evidence:** [@pradeepXkapoor](https://x.com/pradeepXkapoor/status/2103176289482154373), [@gmgmgm1545](https://x.com/gmgmgm1545/status/2103794101892374823). Creator description/prompt; verify the visual when fidelity matters.


<a id="pixel-performance"></a>

## Pixel animation with deliberate pose timing

**Mechanism:** A fixed logical grid and held poses produce intentional sprite motion.

**Build:**

1. Render to a low-resolution offscreen surface with a fixed palette.
2. Animate pose parameters, then quantize drawing positions and hold pose updates at an authored cadence.
3. Scale with nearest-neighbor sampling and letterbox when integer scaling does not fill the screen.

**Tune:** Choose logical resolution from silhouette detail; use a few strong poses rather than smooth subpixel wobble.

**Failure check:** Resize repeatedly and inspect diagonals. Pixels must remain crisp and the silhouette must read in each pose.

**Adapted prompt:** Create a pixel-art [character/action] with a controlled palette, strong key poses and deliberate held-frame timing.

**Evidence:** [@majidmanzarpour](https://x.com/majidmanzarpour/status/2102476499387383834), [@akiy_8](https://x.com/akiy_8/status/2102545213218803769). Creator description/prompt; verify the visual when fidelity matters.


<a id="layered-portrait"></a>

## Turn a still into a rig without inventing hidden art

**Mechanism:** Separating depth layers enables motion, but unseen expressions and overlaps require actual artwork.

**Build:**

1. Separate back hair, body, head, facial features and front hair into registered layers.
2. Define motion limits from available coverage behind each layer.
3. Add genuine closed-eye and mouth variants; distinguish temporary preview shapes from finished expression art.

**Tune:** Keep rotations modest until hidden regions are repaired. Check front/back ordering for crossing limbs.

**Failure check:** Blink, open the mouth and turn at limits. Look for holes, duplicate facial features and shoulder edges crossing clothing.

**Adapted prompt:** Prepare [portrait] for controlled motion with explicit layer order and honest limits on missing expression artwork.

**Evidence:** [@shinshin86](https://x.com/shinshin86/status/2103108187272708544), [@shinshin86](https://x.com/shinshin86/status/2103606937443336289). Creator description/prompt; verify the visual when fidelity matters.


<a id="motion-retarget"></a>

## Retarget a motion clip to a simplified character

**Mechanism:** A simple figure can inherit joint motion without inheriting the source mesh or its drift.

**Build:**

1. Map source joints to the target body segments.
2. Normalize forward direction and decide whether locomotion owns root translation.
3. Trim or blend the loop at matching poses and trigger props from specific action frames.

**Tune:** Retain a small joint map; match limb lengths before adding corrective offsets.

**Failure check:** Inspect foot contacts, hand-held tools and the loop seam. Root motion must not be applied twice.

**Adapted prompt:** Adapt [motion clip] onto [simple rig], preserving action timing, consistent facing and clean contact points.

**Evidence:** [@Viggle_PINOC](https://x.com/Viggle_PINOC/status/2102861943094583723). Creator description/prompt; verify the visual when fidelity matters.


<a id="tracked-body-type"></a>

## Graphics anchored to a real performer

**Mechanism:** Type and effects appear to emerge from movement because they share tracked anchors.

**Build:**

1. Extract pose tracks with confidence values and smooth them without erasing fast gestures.
2. Attach words or effects to selected joints and derive accents from motion events.
3. Switch to a fallback or hide the attachment when tracking confidence collapses.

**Tune:** Use normalized coordinates and transform through the same crop as the video. Reserve large type for clean silhouette moments.

**Failure check:** Check occlusions, fast turns and reframing. Graphics must not jump to unrelated body parts or lag visibly.

**Adapted prompt:** Attach [graphic language] to the performer through tracked joints and meaningful motion events, with graceful handling of occlusion.

**Evidence:** [@aicreataro](https://x.com/aicreataro/status/2103757144789221819). Creator description/prompt; verify the visual when fidelity matters.


<a id="beat-locked-move-library"></a>

## Recognizable dance moves driven by musical phase

**Mechanism:** A named pose function carries a recognizable gesture while a shared musical phase controls contact, bounce and routine changes.

**Build:**

1. Identify a short signature move and annotate supporting foot, free limb, arm target and body accent at key musical phases. Separate tempo, downbeat offset and pickup timing.
2. Create a compact pose interface for the target rig. Resolve limb targets from its geometry; test the move on a plain figure and in costume before staging an ensemble.
3. Schedule moves in musical counts. Preserve contacts through transitions and introduce small bounded ensemble variations without moving the principal accents.

**Tune:** Control stance width, gesture extent, bounce amplitude, support-switch phase and transition duration. Choose framing and shot length that let the defining gesture read.

**Failure check:** Inspect contact, anticipation, accent and recovery in sequence, then play with the final soundtrack. A static pose sheet cannot prove rhythm; costumes and camera cuts must not hide the action.

**Adapted prompt:** Create a short original dance for [character] using named, reusable pose functions tied to a measured musical phase. Prove the move on a plain rig, then in costume, then in a formation. Preserve support contacts and check the final soundtrack before expanding the sequence.

**Evidence:** [Creator post](https://x.com/LLMJunky/status/2104659866304516101). Recent Opus 5.5 creator prompt retrieved; linked music-video-reimagined dance and timing tutorials read at 7d6b7b22caf08c6e330e1abb869953d8e4f2cc1a. README credits both Opus 5.5 and Sonnet 5.5. MIT source, not bundled; rendered film not inspected.
