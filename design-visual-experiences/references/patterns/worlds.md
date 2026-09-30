# Worlds patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [One weather field for every moving material](#shared-wind)
- [Time of day changes the whole environment](#whole-world-daylight)
- [A world drawn from points and motion ribbons](#particle-illustration)
- [Small creatures that react to proximity and care](#habitat-reactions)
- [An environment with a distinctive structural language](#architectural-grammar)
- [Reconstruct a place from evidence with visible uncertainty](#source-grounded-reconstruction)
- [A flowering tree with an intentional silhouette](#sakura-canopy)
- [An environment event that coordinates multiple actors](#crossing-state-machine)

<a id="shared-wind"></a>

## One weather field for every moving material

**Mechanism:** A shared wind signal creates environmental coherence while different materials respond differently.

**Build:**

1. Evaluate wind direction and gust strength in world space.
2. Feed it into foliage, cloth, smoke, water detail and loose particles.
3. Give each material a different inertia and frequency response instead of an unrelated sine wave.

**Tune:** Use a broad gust plus local variation. Keep trunks and heavy objects much stiffer than leaves.

**Failure check:** Follow a gust across the scene. Flags, smoke and foliage must agree about its broad direction.

**Adapted prompt:** Make [environment] breathe under one shared wind system, with material-specific stiffness and lag.

**Evidence:** [@MengTo](https://x.com/MengTo/status/2103155074705019158), [@vib3coded](https://x.com/vib3coded/status/2102534606121746589). Creator description/prompt; verify the visual when fidelity matters.


<a id="whole-world-daylight"></a>

## Time of day changes the whole environment

**Mechanism:** The hour coordinates light, atmosphere, activity and sound rather than changing only the sky color.

**Build:**

1. Use one time-of-day parameter for sun direction and environment state.
2. Derive sky, fog, exposure, artificial lights and habitat activity from it.
3. Keep transitions continuous and reserve discrete events for meaningful thresholds.

**Tune:** Protect readable night values. Use hysteresis around light-on thresholds to avoid flicker while scrubbing.

**Failure check:** Scrub dawn, noon, dusk and night in both directions. Reflections and emissive objects must match the current state.

**Adapted prompt:** Let [place] change coherently across a full day, including light, reflections, sound and the behavior of its inhabitants.

**Evidence:** [@dotey](https://x.com/dotey/status/2102565403109085669), [@ishuagra02](https://x.com/ishuagra02/status/2102920888261742726). Creator description/prompt; verify the visual when fidelity matters.


<a id="particle-illustration"></a>

## A world drawn from points and motion ribbons

**Mechanism:** Point placement describes form while ribbons reveal recent motion.

**Build:**

1. Sample surfaces by stable seeded positions, with denser accents around important silhouettes.
2. Animate skeletal or scene transforms underneath those points.
3. Build ribbons from a short history of meaningful anchors, with width and alpha fading along the trail.
4. Separate render culling from trail history: while an owner remains active offscreen, retain only a bounded, expiring history if continuity on re-entry matters.
5. Clear history deliberately when the owner despawns, respawns, teleports or time jumps; do not join unrelated positions into a long ribbon.
6. Give sampling distance, maximum history length and lifetime separate controls. A distance threshold alone does not resample a fast sparse input into uniform segments.

See the [trail lifecycle study](../updates/2026-09-30-particle-trails.md) for code evidence and visual inspection limits.

**Tune:** Tune point size against target pixel density. Keep enough dark gaps that the image does not become a solid glow.

**Failure check:** Compare steady motion, a stationary anchor, fast motion, camera exit/re-entry, owner despawn/respawn and teleport. Check bounded history, expired samples and unwanted long segments; inspect silhouettes at near and far views without merging all marks into glow.

**Adapted prompt:** Draw [world] as luminous marks and selective gesture trails, preserving structure and a clear focal hierarchy.

**Evidence:** [@ishuagra02](https://x.com/ishuagra02/status/2102920408743678129), [@ishuagra02](https://x.com/ishuagra02/status/2102920888261742726). Selected original/remake environments sampled; pinned trail code read. Lifecycle edge cases, audio and performance remain unverified.


<a id="habitat-reactions"></a>

## Small creatures that react to proximity and care

**Mechanism:** A few purposeful state changes make a world feel inhabited.

**Build:**

1. Give each creature idle, approach, flee or feed states with explicit triggers.
2. Use local steering within its habitat and keep contact with the correct surface.
3. Add cooldowns and individual seeded thresholds to avoid synchronized crowds.

**Tune:** Start with one believable reaction; tune awareness radius, turn speed and recovery time.

**Failure check:** Approach slowly, quickly and repeatedly. Creatures must recover rather than oscillate forever between two states.

**Adapted prompt:** Make [habitat] respond to [simple visitor action] through a small set of readable creature behaviors.

**Evidence:** [@SouranyPhomhome](https://x.com/SouranyPhomhome/status/2103539410302038359), [@dangreenheck](https://x.com/dangreenheck/status/2102878170089169235). Creator description/prompt; verify the visual when fidelity matters.


<a id="architectural-grammar"></a>

## An environment with a distinctive structural language

**Mechanism:** Repeated architectural rules create identity while landmarks create orientation.

**Build:**

1. Choose a structural vocabulary, proportions and material hierarchy.
2. Generate secondary buildings from that grammar and author a few hero landmarks.
3. Validate that stairs, doors, bridges and paths actually connect.

**Tune:** Spend detail where the camera can approach; vary modules within the same grammar rather than scattering random primitives.

**Failure check:** Walk the intended route and inspect key sightlines. Nothing floats, routes connect, and landmarks remain distinguishable.

**Adapted prompt:** Build [place] around a coherent architectural vocabulary and a few memorable landmarks that support exploration.

**Evidence:** [@vib3coded](https://x.com/vib3coded/status/2103257873203462412), [@techartist_](https://x.com/techartist_/status/2103933640392786274). Creator description/prompt; verify the visual when fidelity matters.


<a id="source-grounded-reconstruction"></a>

## Reconstruct a place from evidence with visible uncertainty

For captured spaces, use the [matched-view study](../source-view-reconstruction.md) for silhouette/depth comparison and scene-relative contact.

**Mechanism:** Geometry traces back to measurements and sources rather than plausible invention.

**Build:**

1. Build a source table of footprint, height, material and confidence.
2. Generate repeated architectural elements from those records.
3. Flag contradictory measurements and leave uncertain details labeled or simplified.

**Tune:** Match major proportions before ornament. Use a known-size reference to keep the whole scene in scale.

**Failure check:** Trace several visible objects back to their source rows. A beautiful render must not conceal guessed dimensions.

**Adapted prompt:** Reconstruct [place] from [drawings/photos] with sourced proportions and explicit handling of conflicting or missing details.

**Evidence:** [@alexalbert__](https://x.com/alexalbert__/status/2102466524934271381), [@aayush4soni](https://x.com/aayush4soni/status/2104181266459644283). Creator description/prompt; verify the visual when fidelity matters.


<a id="sakura-canopy"></a>

## A flowering tree with an intentional silhouette

**Mechanism:** Branch architecture gives a canopy volume; flower cards supply detail.

**Build:**

1. Build the trunk and primary branches to define a readable umbrella or weeping silhouette.
2. Distribute clustered cards around branch volumes with some inner fill.
3. Apply lighter outer and darker inner values before adding small wind deformation.

**Tune:** Use alpha testing or an appropriate transparency strategy; budget overdraw and vary card orientation.

**Failure check:** View from below, side and distance. Avoid a hollow shell of flowers or an opaque pink sphere.

**Adapted prompt:** Construct [flowering tree] from a purposeful branch structure, layered blossom density and restrained shared-wind motion.

**Evidence:** [@pound75423](https://x.com/pound75423/status/2103480085319942353). Creator description/prompt; verify the visual when fidelity matters.


<a id="crossing-state-machine"></a>

## An environment event that coordinates multiple actors

**Mechanism:** A train crossing feels real because signals, gates, vehicles and pedestrians share one event state.

**Build:**

1. Define approach, warning, closed, passing and reopening states.
2. Make agents wait based on the crossing state rather than a fixed independent timer.
3. Drive light, bell and gate motion from the same transition events.

**Tune:** Leave enough warning time to avoid a gate intersecting traffic; test delayed arrivals and paused simulation.

**Failure check:** Restart in each state. No actor should cross while the gate is closed or continue waiting after reopening.

**Adapted prompt:** Build [coordinated environmental event] with one shared state machine controlling movement, signals and sound.

**Evidence:** [@pound75423](https://x.com/pound75423/status/2103480085319942353). Creator description/prompt; verify the visual when fidelity matters.
