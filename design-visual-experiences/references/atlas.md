# Mechanism atlas and guide routes

Pattern cards below are the canonical mechanism guidance; task-specific links add deeper implementation and worked studies. These are original engineering adaptations of retrieved creator descriptions and prompts, not independently reproduced projects. Each card states a mechanism, construction steps, tuning choices, a failure check, an adapted prompt and primary source links.

## Find a mechanism

Run from the skill directory:

```bash
python3 scripts/search.py "walking character feet slide on ground"
python3 scripts/search.py "ink dries and re wets" --kind sources --prompt-only
python3 scripts/search.py "ink brush" --kind resources
```

Search is local and needs only Python's standard library. Default build results point to current pattern cards, guide sections and compositions. Narrow with `--kind patterns`, `guides` or `compositions`; use `--family camera`, `--limit 10`, or `--json` as needed. With `--kind sources`, `--prompt-only` requires inspected prompt content without certifying completeness; `--prompt-leads` also includes marker-only leads. If nothing useful appears, try the underlying physical relationship or browse a family below. When the library has no useful match, build from the brief; do not force an example into the project.

Read the relevant cards, then choose a primary mechanism and at most a few supporting ones. Use [composition recipes](compositions.md) to combine them and [diagnosis](diagnosis.md) to fix a visible failure. [Source cards](source-cards.md) provide the reverse source-to-pattern lookup. [Inspected implementations](inspected-sources.md) show what was actually read in code. [Coverage](research-coverage.md) states the limits.

## Motion

**Feature launches and product demos:** [Film direction](feature-launch-films.md) connects story, hooks, readable holds, object continuity and generated/controlled production layers.

**Use deeper guidance when:** Refresh-rate differences → [time-based following](time-based-follow.md). Analytic spring/release code → [Elastic Matter](worked-study.md) and [worked spring notes](build-patterns.md#1-a-persistent-object-with-elastic-transformations). Origin-aware UI reveals or selection highlights → [interface vocabulary](motion-recipes.md#morphs-and-interface-motion).

- [A particle form that contracts, bursts and returns](patterns/motion.md#contract-burst-return)
- [Fit articulated product motion to measured reference poses](patterns/motion.md#measured-joint-motion)

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

**Use deeper guidance when:** Words carry structural meaning → [structural typography study](structural-type-study.md). Weight travels across text → [font metrics and footprint](build-patterns.md#traveling-font-weight).

- [Words that become the structure of a scene](patterns/type.md#structural-type)
- [Per-glyph entrances with phrase-level hierarchy](patterns/type.md#glyph-choreography)
- [A letter counter becomes the next scene](patterns/type.md#glyph-aperture)
- [Variable font weight as a physical event](patterns/type.md#weight-as-action)
- [Captions built from speech timing](patterns/type.md#spoken-captions)
- [An image formed from meaningful characters](patterns/type.md#source-code-image)
- [Let the visual system evolve with the story](patterns/type.md#contextual-color-history)
- [Explain a design decision through construction](patterns/type.md#blueprint-rationale)

## Camera

**Use deeper guidance when:** Inspection presets must preserve configuration → [product cameras](interactive-3d.md#product-inspection-through-camera-presets). Pinch/orbit must not become a tap → [spatial input](spatial-input.md).

- [Nested worlds with constant perceived zoom](patterns/camera.md#portal-zoom)
- [A continuous journey across orders of magnitude](patterns/camera.md#scale-ladder)
- [Camera height that makes a small character feel small](patterns/camera.md#subject-scale)
- [Handheld motion with a plausible camera operator](patterns/camera.md#motivated-handheld)
- [A fixed foreground with layered traveling scenery](patterns/camera.md#train-window)
- [Reset a loop while the viewer cannot see the change](patterns/camera.md#occlusion-reset)
- [A directed tour that allows local curiosity](patterns/camera.md#guided-free-exploration)
- [A final pullback that reinterprets the whole scene](patterns/camera.md#reveal-world-in-object)

## Materials

**Use deeper guidance when:** A grab leaves a local residue → [material memory](local-material-memory.md). Glass moves over a moving scene → [registration](build-patterns.md#glass-under-camera-motion). A vessel casts moving light → [refracted footprints](refracted-light-footprints.md). Drawing competes with washing → [brush ownership](build-patterns.md#brush-gestures-and-an-animated-wash). Print dots must stay pinned → [printmaking notes](build-patterns.md#6-printmaking-as-a-rendering-system).

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

**Use deeper guidance when:** Water needs flow and retained wetness → [terrain-water study](terrain-water.md). Match a captured room or compare scan/model → [source-view reconstruction](source-view-reconstruction.md). Physical objects become a projected stage → [spatial registration and staging](interactive-3d.md#make-physical-objects-part-of-the-animation).

- [One weather field for every moving material](patterns/worlds.md#shared-wind)
- [Time of day changes the whole environment](patterns/worlds.md#whole-world-daylight)
- [A world drawn from points and motion ribbons](patterns/worlds.md#particle-illustration)
- [Small creatures that react to proximity and care](patterns/worlds.md#habitat-reactions)
- [An environment with a distinctive structural language](patterns/worlds.md#architectural-grammar)
- [Reconstruct a place from evidence with visible uncertainty](patterns/worlds.md#source-grounded-reconstruction)
- [A flowering tree with an intentional silhouette](patterns/worlds.md#sakura-canopy)
- [An environment event that coordinates multiple actors](patterns/worlds.md#crossing-state-machine)

## Characters

**Use deeper guidance when:** Generated facial features need independent control → [facial preparation](facial-preparation.md). A guide points at changing content → [embodied narrator](embodied-narrator.md). Sitting, holding and expression must coexist → [compatible actions](interactive-3d.md#preserve-compatible-actions-inside-a-spatial-scene).

- [Recognizable dance moves driven by musical phase](patterns/characters.md#beat-locked-move-library)

- [A character bible translated into a controllable rig](patterns/characters.md#identity-rig)
- [Walk cycles that keep feet attached to the ground](patterns/characters.md#planted-foot-ik)
- [Hands and tools constrained through an action](patterns/characters.md#grip-and-tool)
- [Secondary parts that express the character state](patterns/characters.md#emotional-secondary)
- [Pixel animation with deliberate pose timing](patterns/characters.md#pixel-performance)
- [Turn a still into a rig without inventing hidden art](patterns/characters.md#layered-portrait)
- [Retarget a motion clip to a simplified character](patterns/characters.md#motion-retarget)
- [Graphics anchored to a real performer](patterns/characters.md#tracked-body-type)

## Physics

**Use deeper guidance when:** Explain a success, failure or constraint → [simulation verdicts](simulation-verdicts.md). Catch an event between displayed frames → [event stops](simulation-event-stops.md). Direct a fixed mechanical film → [contact-event scheduling](production.md#author-a-chain-reaction-around-contact-events).

- [A chain reaction caused by contacts](patterns/physics.md#rigid-body-chain)
- [A soft object that remains physical after cutting](patterns/physics.md#cuttable-soft-body)
- [An expanding force field with persistent aftermath](patterns/physics.md#pressure-front)
- [Distinct materials in a grid simulation](patterns/physics.md#falling-materials)
- [A fluid field with a coherent solver order](patterns/physics.md#fluid-pipeline)
- [Combustion-inspired fields that evolve together](patterns/physics.md#fire-to-smoke)
- [Water effects driven by depth and disturbance](patterns/physics.md#causal-water)
- [Keep dense simulation data on the GPU](patterns/physics.md#gpu-resident-motion)

## Explainers

**Use deeper guidance when:** Views must share experiment inputs → [multiple explanatory views](interactive-3d.md#build-an-experiment-with-several-explanatory-views). Unfamiliar controls need practice → [action-gated lessons](action-gated-lessons.md).

- [A mechanical explainer whose contacts compute the answer](patterns/explainers.md#contact-driven-computation)

- [Compare mechanisms under the same input](patterns/explainers.md#shared-control-comparison)
- [An optical explainer whose image comes from its model](patterns/explainers.md#computed-optical-image)
- [A cutaway that follows a moving substance](patterns/explainers.md#flow-cutaway)
- [Explain a process across several scales](patterns/explainers.md#causal-scale-story)
- [An explanatory animation driven by real outputs](patterns/explainers.md#data-backed-image)
- [Link a spatial selection to a time series](patterns/explainers.md#linked-space-time)
- [A layout tool that shows the consequences of placement](patterns/explainers.md#constraint-aware-layout)
- [Make a resource rule visible through conserved quantities](patterns/explainers.md#token-conservation)

## Sound

**Use deeper guidance when:** A changed voice take must retime motion → [narration cues](narration-cues.md). Music pickups or displayed frames use different clocks → [timing and presentation](timing-and-presentation.md). Choose a sound palette → [auditioning](production.md#audition-sound-identities-before-making-a-pack); compare recurring scores → [sound identity](production.md#review-sound-identity-across-projects).

- [One event score for both audio and visual motion](patterns/sound.md#shared-score-clock)
- [Map frequency bands to different physical parts](patterns/sound.md#band-to-part)
- [A physical event that produces a musical note](patterns/sound.md#collision-instrument)
- [A drawing gesture that makes a musical phrase](patterns/sound.md#gesture-instrument)
- [Align an effect by its perceptual attack](patterns/sound.md#peak-alignment)
- [Sound synthesis tied to a visible material](patterns/sound.md#physical-timbre)
- [Change visual grammar with the musical section](patterns/sound.md#section-arrangement)
- [One seed creates a coherent visual and musical world](patterns/sound.md#seeded-universe)

## Interaction

**Use deeper guidance when:** Start with interaction, state and renderer choices → [interactive/3D primer](interactive-3d.md). Camera hands drive a material → [hand/depth input](hand-depth-input.md). Objects change only when hidden → [observation-gated motion](observation-gated-motion.md). One pull releases one payload → [tangible release](interactive-3d.md#turn-a-gesture-into-one-tangible-release). Flat and folded views agree → [crease state](interactive-3d.md#fold-a-structure-through-shared-crease-state).

- [A working mechanism that keeps its phase while taken apart](patterns/interaction.md#phase-coherent-explode)

- [An assembly that can be understood in either direction](patterns/interaction.md#exploded-assembly)
- [A visual model constrained by a real parts inventory](patterns/interaction.md#buildable-bricks)
- [A movable inspection lens over aligned layers](patterns/interaction.md#reveal-under-surface)
- [An irreversible-looking surface action with reversible state](patterns/interaction.md#cleaning-mask)
- [A simple control with several meaningful consequences](patterns/interaction.md#one-input-meaning)
- [Emergent pursuit with deliberately imperfect opponents](patterns/interaction.md#readable-chase)
- [A spatial metaphor backed by real system state](patterns/interaction.md#operational-world)
- [A sketchbook with real pages and drawing interaction](patterns/interaction.md#page-as-surface)

## Story

**Use deeper guidance when:** A theme needs a meaningful action → [playable metaphor](principles.md#turn-an-abstract-theme-into-an-action). Particles resolve into readable content → [content handoff](particle-content-handoff.md).

- [One motif changes meaning across scenes](patterns/story.md#motif-handoff)
- [Make the benefit visible as a change in structure](patterns/story.md#chaos-to-organization)
- [Stillness that makes an action or revelation register](patterns/story.md#quiet-payoff)
- [Connect a historical artifact to a present-day idea](patterns/story.md#archival-bridge)
- [Tell the story through decisions and reactions](patterns/story.md#silent-acting)
- [A structure assembles as its story unfolds](patterns/story.md#historical-construction)
- [Use a simple 3D blockout to control a later visual treatment](patterns/story.md#camera-from-previs)
- [Combine generated footage and editable graphics deliberately](patterns/story.md#coherent-mixed-media)

## Production

**Use deeper guidance when:** Frames look good but transitions fail → [transition QA](transition-qa.md). Motion must survive later edits → [editable handoff](editable-motion-handoff.md). Expensive rendering repeats static work → [render reuse](production.md#spend-render-time-on-what-visibly-changes).

- [Responsive scrubbing that cannot be overwritten by stale frames](patterns/production.md#latest-frame-presentation)

- [Render any frame without playing earlier frames](patterns/production.md#pure-time-render)
- [A loop whose motion continues across the seam](patterns/production.md#loop-position-velocity)
- [Motion blur that preserves the information layer](patterns/production.md#selective-motion-blur)
- [A product film grounded in actual UI and actions](patterns/production.md#real-product-demo)
- [Translate a reference into specific change requests](patterns/production.md#reference-to-director-notes)
- [Reduce the expensive effect rather than arbitrary detail](patterns/production.md#quality-tier-by-bottleneck)
- [Recompose for each aspect ratio](patterns/production.md#aspect-aware-staging)
- [Review moments where the system changes state](patterns/production.md#event-based-review)

## Design, review and runnable studies

Use [principles](principles.md) for art direction, [composition guidance](compositions.md) for combining mechanisms, [diagnosis](diagnosis.md) for failures, and [brief/review templates](briefs-and-review.md) when useful. [Fieldwork](mechanism-studies.md) demonstrates shared wind, planted feet and aperture travel. [Benchmark experiences](benchmark-lab.md) provide complete small briefs and revision evidence. [Visual comparisons](visual-comparisons.md) explains how to extract decisions from observed references.

For discovery only, the [historical example shortlist](examples.md) and [toolkit links](toolkits.md) retain earlier browsing material. Their example numbers are unrelated to pattern identities. For implementation, return to the relevant card or focused guide above.

For UI entrances/exits across footage, see [Composition choreography](composition-choreography.md): layered timing, localized activation, readable holds, persistent anchors and consequence-driven departure.
