# Motion recipes

This optional vocabulary guide helps name a visual move, especially an origin-aware reveal, selection highlight or shape grammar. For construction steps and authoritative mechanism detail, use the [atlas and pattern cards](atlas.md); for combinations, use [compositions](compositions.md). The numbered suggestions below retain earlier study links and are original adaptations. They are not claims about undocumented creator code. Use the recipe that serves the brief, then adapt it to the project's visual language.

## Morphs and interface motion

### 1. One object, several functions
Keep a persistent container or contour. Interpolate its position, size, radius, and local features; sequence content changes so old and new information do not fight. Keep an anchor fixed while the rest transforms. Inspect halfway states as carefully as endpoints. **Study:** example 2; [Onetake](https://github.com/feitangyuan/onetake). **Failure:** unrelated scenes hidden by a scale-and-fade transition.

### 2. Origin-aware reveal
Expand a menu, tooltip, or panel from the trigger's spatial origin. Make the return direction consistent. Preserve keyboard focus and interruption behavior independently of the visual transition. **Study:** [Emil's animation details](https://emilkowal.ski/ui/good-vs-great-animations). **Failure:** the panel looks attached to a different point than its trigger.

### 3. Shared selection highlight
Move one highlight between options rather than creating unrelated flashes. Synchronize text contrast with the actual highlighted area; a clipping mask can help. Keep selection immediate even if the indicator settles afterward. **Study:** the same Emil article. **Failure:** unreadable text during travel or delayed functional selection.

### 4. Anticipation, action, settlement
Use a small preparation to make a larger action intelligible, then give secondary parts time to settle. Preparation must not delay ordinary functional feedback. **Study:** follow-through, example 5; reward sequences 7–8. **Failure:** everything bounces at once or users wait for feedback.

## Typography and graphic rhythm

### 5. Kinetic type with a reading hierarchy
Choose the phrase that must be read and the words that may function as texture. Animate phrase groups or meaningful words, preserve baselines when useful, and provide a clean reading hold. **Study:** examples 4, 9, 54. **Failure:** character-by-character spectacle obscures the message.

### 6. Shape grammar
Reuse a small family of contours, line weights, and spacing relationships across scenes. Change composition and scale to create variety. **Study:** geometric/minimal reels 1 and 3. **Failure:** every shot introduces a new unrelated style.

### 7. A reveal with an actual payoff
Build tension through concealment, compression, or accumulation, then reveal one legible result. Put the largest visual contrast at the payoff and hold it. **Study:** chest/card examples 7–8. **Failure:** bloom, particles, and camera shake hide the object being celebrated.

### 8. A seamless loop
Plan periodic positions and compatible velocities at the seam. Check secondary motion, particle ages, lighting, camera, and sound tails too. For discrete animation sample frames from 0 through N−1, not an extra duplicate endpoint. **Study:** water cycle, example 89; [Claude Animation balloon example](https://github.com/buildwithhanif/claude-animation-skill). **Failure:** matching first/last images while the motion still visibly jolts.

## Characters, illustration, and material

### 9. Rig first, performance second
Create a small pose sheet with consistent proportions, pivots, and expressions. Test a reach, turn, walk, and extreme pose before animating a whole story. Overlap body parts in a deliberate draw order. **Study:** [Claude Animation](https://github.com/buildwithhanif/claude-animation-skill), [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase). **Failure:** drifting anatomy and limbs that slide through contacts.

### 10. Drawing as a meaningful process
Reveal construction in the order the material is made: geometry before shading, large washes before details, or separate print layers. The final image should still be strong without the reveal. **Study:** [Anidoodle](https://github.com/alexgreensh/anidoodle), architectural example 37. **Failure:** a generic opacity wipe over a finished image.

### 11. Tactile motion without visual noise
Use stable seeded texture in object or material space. If line boil or animated grain is intentional, control its rate and amplitude separately from object movement. **Study:** Window Seat, example 30; [p5.brush cartoon](https://github.com/az9713/opus-5.5-musical-cartoon). **Failure:** unseeded redraw noise that reads as shimmer rather than texture.

### 12. A material-specific transformation
Paper folds, cloth bends, soft matter deforms, and rigid parts hinge or separate. Pick one physical logic and preserve it through the change. **Study:** paper story 25, clay 40, cake 63, vehicle transformation 68. **Failure:** every material behaves like the same elastic rectangle.

## Space, camera, and fields

### 13. Exploded assembly
Choose a viewing axis and separate parts enough to reveal their relationships. Label stable anchors; keep leaders away from occluding geometry. Let users reassemble or isolate components. **Study:** lens 13, rocket engine 16, building 37. **Failure:** impressive separation that loses the spatial relationship being explained.

### 14. A journey through scale
Use identifiable intermediate landmarks and a scale indicator when scale is educational. Adjust coordinate strategy and clipping for extreme ranges. Choose where conceptual simplification is needed rather than pretending literal physical continuity. **Study:** data-center-to-atom 66; its post is a third-party account, not a verified first-person case.

### 15. A camera that hands attention forward
Compose the next event before moving toward it. Use foreground occlusion, a carried object, or an anticipated landing point when useful. Keep a rest after a fast move. **Study:** continuous-camera example 53; [Onetake case breakdowns](https://github.com/feitangyuan/onetake). **Failure:** camera movement motivated only by available effects.

### 16. Particles with local meaning
Specify what a particle represents, its initial distribution, the force or mapping that moves it, and the settled form. Use instancing or batched drawing when appropriate. **Study:** word-vector galaxies 46, orbital art 55. **Failure:** random particle clouds used to decorate unrelated concepts.

### 17. Fluid as an instrument
Map pointer velocity to impulse and a separate control to dye or force radius. Keep simulation and display settings distinguishable. Tune persistence so gestures remain readable. **Study:** [theailoser's indexed prompt](https://www.tripo3d.ai/3d-prompts/claude-opus-5-5-2102565611473661963), example 94. **Failure:** attractive prerecorded turbulence that ignores input.

### 18. Environmental layers
Separate structural movement from small atmospheric detail: boat travel, then waves, then reflections and spray. Use distance, occlusion, and contrast to establish depth. **Study:** Clearwater 18, Tidewater 20, garden 21. **Failure:** every layer moves at the same speed and scale.

### 19. A causal chain reaction
Make contact readable before the next event begins. If the brief asks for simulation, derive reactions from the solver; for an authored film, a designed timeline is valid. Do not describe keyframes as physical validation. **Study:** sketch 19, Rube Goldberg 99. **Failure:** later events fire on timers despite failed earlier contact.

### 20. Sound-driven form
Choose what the sound drives: onset, energy in a frequency band, phrase structure, or explicit score events. Smooth noisy measurements while preserving important attacks. Design a meaningful silent state. **Study:** robot visualizer 24, piano 27, [JavaScript animation pack](https://github.com/iart-ai/javascript-animation-skills). **Failure:** unrelated pulses labeled audio-reactive.

## When a move feels wrong

Use [diagnosis](diagnosis.md) for symptoms, small tests and repairs. If the subject feels floaty, inspect contact and settlement before adding more bounce. If it feels generic, reconsider the material behavior or visual relationship, not only the palette.

## Translate timing advice between frame rates

A fixed remaining-distance fraction per rendered frame changes speed with refresh rate. Use [time-based following](time-based-follow.md) when adapting that recipe, and record the reference rate for frame-count staggers. A spring is still preferable when retargeting must preserve velocity.
