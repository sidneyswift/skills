# Pattern atlas

104 implementation patterns across 12 families. These are original engineering adaptations of retrieved creator descriptions and prompts, not 104 independently reproduced projects. Each card states a mechanism, construction steps, tuning choices, a failure check, an adapted prompt and primary source links.

## Find a mechanism

Run from the skill directory:

```bash
python3 scripts/search.py "walking character feet slide on ground"
python3 scripts/search.py "ink dries and re wets" --kind sources --prompt-only
python3 scripts/search.py "ink brush" --kind resources
```

Search is local and needs only Python's standard library. The default result points to the exact family and anchor. Use `--family camera`, `--limit 10`, or `--json` as needed. `--prompt-only` on sources means a prompt marker appeared in retrieved text; it does not guarantee a complete prompt. If nothing useful appears, search a physical mechanism or browse a family below.

Read the relevant cards, then choose a primary mechanism and at most a few supporting ones. Use [composition recipes](compositions.md) to combine them and [diagnosis](diagnosis.md) to fix a visible failure. [Source cards](source-cards.md) explain the 128 sources behind the atlas. [Inspected implementations](inspected-sources.md) show what was actually read in code. [Coverage](research-coverage.md) states the limits.

## Motion

- [Consistent follow speed across refresh rates](patterns/motion.md#time-based-follow)

- [One object, many functional states](patterns/motion.md#persistent-shape)
- [Elastic indicator with independently timed edges](patterns/motion.md#unequal-edge-springs)
- [Direct drag followed by a momentum-preserving snap](patterns/motion.md#release-momentum)
- [Soft resistance outside an interaction limit](patterns/motion.md#rubber-boundary)
- [An animated object that communicates system state](patterns/motion.md#semantic-orb)
- [Badge tilt with a bounded celebration](patterns/motion.md#constrained-badge)
- [Anticipation, release and readable reward](patterns/motion.md#earned-reward)
- [Particles that arrive at the value they change](patterns/motion.md#collect-to-destination)

## Type

- [Words that become the structure of a scene](patterns/type.md#structural-type)
- [Per-glyph entrances with phrase-level hierarchy](patterns/type.md#glyph-choreography)
- [A letter counter becomes the next scene](patterns/type.md#glyph-aperture)
- [Variable font weight as a physical event](patterns/type.md#weight-as-action)
- [Captions built from speech timing](patterns/type.md#spoken-captions)
- [An image formed from meaningful characters](patterns/type.md#source-code-image)
- [Let the visual system evolve with the story](patterns/type.md#contextual-color-history)
- [Explain a design decision through construction](patterns/type.md#blueprint-rationale)

## Camera

- [Nested worlds with constant perceived zoom](patterns/camera.md#portal-zoom)
- [A continuous journey across orders of magnitude](patterns/camera.md#scale-ladder)
- [Camera height that makes a small character feel small](patterns/camera.md#subject-scale)
- [Handheld motion with a plausible camera operator](patterns/camera.md#motivated-handheld)
- [A fixed foreground with layered traveling scenery](patterns/camera.md#train-window)
- [Reset a loop while the viewer cannot see the change](patterns/camera.md#occlusion-reset)
- [A directed tour that allows local curiosity](patterns/camera.md#guided-free-exploration)
- [A final pullback that reinterprets the whole scene](patterns/camera.md#reveal-world-in-object)

## Materials

- [A glossy spike field reaches toward an attractor](patterns/materials.md#attractor-spike-field)
- [Slow paint marks on smoothly moving geometry](patterns/materials.md#paint-clock)
- [Ink that dries, settles and can be re-wetted](patterns/materials.md#wet-dry-ink)
- [A brush that stays consistent at different event rates](patterns/materials.md#distance-spaced-brush)
- [A mosaic whose pieces become moving figures](patterns/materials.md#tile-flock)
- [Glass whose shape is readable through distortion](patterns/materials.md#glass-volume)
- [Change style while preserving object identity](patterns/materials.md#material-swap)
- [Rain and wet surfaces that belong to the scene](patterns/materials.md#lit-rain)
- [Stable toon outlines from geometry buffers](patterns/materials.md#outline-normal-depth)

## Worlds

- [One weather field for every moving material](patterns/worlds.md#shared-wind)
- [Time of day changes the whole environment](patterns/worlds.md#whole-world-daylight)
- [A world drawn from points and motion ribbons](patterns/worlds.md#particle-illustration)
- [Small creatures that react to proximity and care](patterns/worlds.md#habitat-reactions)
- [An environment with a distinctive structural language](patterns/worlds.md#architectural-grammar)
- [Reconstruct a place from evidence with visible uncertainty](patterns/worlds.md#source-grounded-reconstruction)
- [A flowering tree with an intentional silhouette](patterns/worlds.md#sakura-canopy)
- [An environment event that coordinates multiple actors](patterns/worlds.md#crossing-state-machine)

## Characters

- [A character bible translated into a controllable rig](patterns/characters.md#identity-rig)
- [Walk cycles that keep feet attached to the ground](patterns/characters.md#planted-foot-ik)
- [Hands and tools constrained through an action](patterns/characters.md#grip-and-tool)
- [Secondary parts that express the character state](patterns/characters.md#emotional-secondary)
- [Pixel animation with deliberate pose timing](patterns/characters.md#pixel-performance)
- [Turn a still into a rig without inventing hidden art](patterns/characters.md#layered-portrait)
- [Retarget a motion clip to a simplified character](patterns/characters.md#motion-retarget)
- [Graphics anchored to a real performer](patterns/characters.md#tracked-body-type)

## Physics

- [A chain reaction caused by contacts](patterns/physics.md#rigid-body-chain)
- [A soft object that remains physical after cutting](patterns/physics.md#cuttable-soft-body)
- [An expanding force field with persistent aftermath](patterns/physics.md#pressure-front)
- [Distinct materials in a grid simulation](patterns/physics.md#falling-materials)
- [A fluid field with a coherent solver order](patterns/physics.md#fluid-pipeline)
- [Combustion-inspired fields that evolve together](patterns/physics.md#fire-to-smoke)
- [Water effects driven by depth and disturbance](patterns/physics.md#causal-water)
- [Keep dense simulation data on the GPU](patterns/physics.md#gpu-resident-motion)

## Explainers

- [Compare mechanisms under the same input](patterns/explainers.md#shared-control-comparison)
- [An optical explainer whose image comes from its model](patterns/explainers.md#computed-optical-image)
- [A cutaway that follows a moving substance](patterns/explainers.md#flow-cutaway)
- [Explain a process across several scales](patterns/explainers.md#causal-scale-story)
- [An explanatory animation driven by real outputs](patterns/explainers.md#data-backed-image)
- [Link a spatial selection to a time series](patterns/explainers.md#linked-space-time)
- [A layout tool that shows the consequences of placement](patterns/explainers.md#constraint-aware-layout)
- [Make a resource rule visible through conserved quantities](patterns/explainers.md#token-conservation)

## Sound

- [One event score for both audio and visual motion](patterns/sound.md#shared-score-clock)
- [Map frequency bands to different physical parts](patterns/sound.md#band-to-part)
- [A physical event that produces a musical note](patterns/sound.md#collision-instrument)
- [A drawing gesture that makes a musical phrase](patterns/sound.md#gesture-instrument)
- [Align an effect by its perceptual attack](patterns/sound.md#peak-alignment)
- [Sound synthesis tied to a visible material](patterns/sound.md#physical-timbre)
- [Change visual grammar with the musical section](patterns/sound.md#section-arrangement)
- [One seed creates a coherent visual and musical world](patterns/sound.md#seeded-universe)

## Interaction

- [An assembly that can be understood in either direction](patterns/interaction.md#exploded-assembly)
- [A visual model constrained by a real parts inventory](patterns/interaction.md#buildable-bricks)
- [A movable inspection lens over aligned layers](patterns/interaction.md#reveal-under-surface)
- [An irreversible-looking surface action with reversible state](patterns/interaction.md#cleaning-mask)
- [A simple control with several meaningful consequences](patterns/interaction.md#one-input-meaning)
- [Emergent pursuit with deliberately imperfect opponents](patterns/interaction.md#readable-chase)
- [A spatial metaphor backed by real system state](patterns/interaction.md#operational-world)
- [A sketchbook with real pages and drawing interaction](patterns/interaction.md#page-as-surface)

## Story

- [One motif changes meaning across scenes](patterns/story.md#motif-handoff)
- [Make the benefit visible as a change in structure](patterns/story.md#chaos-to-organization)
- [Stillness that makes an action or revelation register](patterns/story.md#quiet-payoff)
- [Connect a historical artifact to a present-day idea](patterns/story.md#archival-bridge)
- [Tell the story through decisions and reactions](patterns/story.md#silent-acting)
- [A structure assembles as its story unfolds](patterns/story.md#historical-construction)
- [Use a simple 3D blockout to control a later visual treatment](patterns/story.md#camera-from-previs)
- [Combine generated footage and editable graphics deliberately](patterns/story.md#coherent-mixed-media)

## Production

- [Render any frame without playing earlier frames](patterns/production.md#pure-time-render)
- [A loop whose motion continues across the seam](patterns/production.md#loop-position-velocity)
- [Motion blur that preserves the information layer](patterns/production.md#selective-motion-blur)
- [A product film grounded in actual UI and actions](patterns/production.md#real-product-demo)
- [Translate a reference into specific change requests](patterns/production.md#reference-to-director-notes)
- [Reduce the expensive effect rather than arbitrary detail](patterns/production.md#quality-tier-by-bottleneck)
- [Recompose for each aspect ratio](patterns/production.md#aspect-aware-staging)
- [Review moments where the system changes state](patterns/production.md#event-based-review)


## Recent additions

- [A working mechanism that keeps its phase while taken apart](patterns/interaction.md#phase-coherent-explode)
- [A particle form that contracts, bursts and returns](patterns/motion.md#contract-burst-return)

[September 29 evidence and lessons](updates/2026-09-29-evening.md).

- [A mechanical explainer whose contacts compute the answer](patterns/explainers.md#contact-driven-computation)
- [Fit articulated product motion to measured reference poses](patterns/motion.md#measured-joint-motion)

[Causal motion update](updates/2026-09-29-causal-motion.md).

- [Recognizable dance moves driven by musical phase](patterns/characters.md#beat-locked-move-library)
- [Responsive scrubbing that cannot be overwritten by stale frames](patterns/production.md#latest-frame-presentation)

[Timing and asynchronous presentation update](updates/2026-09-29-timing.md).
