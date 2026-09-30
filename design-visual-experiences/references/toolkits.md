# Toolkits, tutorials, and primary guidance

This is an optional annotated directory of external references, reviewed as public documentation on September 29, 2026. Use the local [atlas](atlas.md) for mechanism guidance and the searchable [resource directory](resources.json) for source evidence. Tools were not installed or executed in this research. Counts are snapshot claims from their authors, not independently audited inventories. Check current compatibility and licensing before reusing code; links here do not make packages dependencies of this skill.

## Creator code and production workflows

| Resource | Why open it | Useful material / boundary |
|---|---|---|
| [iart-ai / motion-skills](https://github.com/iart-ai/motion-skills) | Browse a broader motion workflow collection | Hub reporting 50 skills across 14 packs; inspect only relevant entries |
| [JavaScript Animation Skills](https://github.com/iart-ai/javascript-animation-skills) | Coordinate coded film and sound | Shared timing, Canvas films, soundtrack workflow; no-assets constraints belong to this pack |
| [Claude Horizon Animation](https://github.com/misbahsy/claude-horizon-animation) | Make physical and mathematical explanations | Physics sketch, lab explainer, and mixed-media reel approaches |
| [Opus JS Animations](https://github.com/klsoen/opus-js-animations) | Go from audio/brief to frame-exact film | Director treatment, pure-time rendering, contact sheets, style references; its approval gates are not inherited |
| [Charlie Hills motion graphics](https://github.com/charlie947/motion-graphics-skills) | Find specific brand and motion workflows | 13 skills, prompt files, animated charts, launch films, effects, exports |
| [Claude Animation](https://github.com/buildwithhanif/claude-animation-skill) | Improve hand-drawn characters and surfaces | Rigs, material detail, film examples, inspection harness; Node and ffmpeg workflow |
| [Musical cartoon project](https://github.com/az9713/opus-5.5-musical-cartoon) | Study an actual iterative build | p5.js/p5.brush, storyboard, development journey, sound and frame timing |
| [Onetake](https://github.com/feitangyuan/onetake) | Study continuity between beats | Ten case films and breakdowns, camera and carry mechanisms; repository says PolyForm Noncommercial, so do not vendor its code for commercial work |
| [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | Find a character/storyboard starting point | p5.brush character animation and rendering scaffold |
| [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) / [gallery](https://lemomo-ai.github.io/lemo-opuscar/) | Expand artistic range beyond default tech reels | Author reports 43 coded film styles; director and technique guides plus individual STYLE.md files |
| [Anidoodle](https://github.com/alexgreensh/anidoodle) | Make illustration, drawing films, and interactive art | 31 material/drawing styles, character consistency, process-based reveals, synthesis |
| [Clearwater](https://github.com/Aureliengmz/clearwater) | Inspect water rendering | Waves, ripples, refraction and caustics; contains generated texture material, not proof of an asset-free workflow |
| [Tidewater](https://github.com/dgreenheck/tidewater) | Inspect an explorable island scene | Browser environment and boat exploration; [creator's prompt reply](https://x.com/dangreenheck/status/2102911556296052788) |
| [Window Seat](https://github.com/sevenevesai/riso-windowseat) | Inspect a complete risograph-style film | Visual design, rendering, and score documentation |

## Prompt and case collections

| Collection | What it adds | Evidence limitation |
|---|---|---|
| [Claude Video](https://claudevideo.org/videos) | 1,048 indexed posts in the research snapshot; categories and prompt flags | Flags include partial briefs; index inclusion does not validate the work |
| [athemeroy's reviewed cases](https://github.com/athemeroy/awesome-opus-5-5-videos) | 168 reviewed case records and technique notes | Overlaps heavily with Claude Video; notes are credited to their author and were not copied wholesale |
| [Tripo Opus prompt catalog](https://github.com/TripoGrowthLab/awesome-opus-5-5-prompts) | 45 cases, including games, simulations, spatial scenes and prompt text | Original posts and replies can have different IDs; prompt provenance varies; some cases are comparisons or third-party accounts |
| [joeseesun prompt collection](https://github.com/joeseesun/opus-video-prompts) | 54 cases and 18 full-prompt entries in the earlier research | Read individual provenance and required inputs; not every case contains a complete prompt |

The bundled [examples](examples.md) provide a manageable shortlist; [discovery.csv](discovery.csv) retains 1,101 unique post IDs. Search rather than reading the entire catalog. These are distinct links, not necessarily distinct projects or first-person creator posts.

## Primary principles and implementation references

| Source | Use it for |
|---|---|
| [Apple: Motion](https://developer.apple.com/design/human-interface-guidelines/motion) | Feedback, purpose, restraint, and alternatives |
| [Carbon: Motion](https://carbondesignsystem.com/elements/motion/overview/) | Productive versus expressive motion, easing roles, duration system |
| [Emil Kowalski: You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations) | Frequency and restraint in real interfaces |
| [Emil Kowalski: Good vs great animations](https://emilkowal.ski/ui/good-vs-great-animations) | Origins, contrast, direction, and small timing details |
| [Josh Comeau: Spring physics](https://www.joshwcomeau.com/animation/a-friendly-introduction-to-spring-physics/) | Mass, tension, friction, and motion character |
| [web.dev: Animation performance](https://web.dev/articles/animations-guide) | Rendering pipeline and profiling |
| [MDN: WebGL best practices](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices) | GPU portability, memory, batching, and resolution |
| [Three.js: Color management](https://threejs.org/manual/pages/color-management.html) | Correct input, working, and output color spaces |
| [GSAP: matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/) | Responsive animation contexts and cleanup |
| [W3C: Animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) | Reduced/optional interaction motion; Level AAA criterion |
| [W3C: Pause, stop, hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) | User control of qualifying automatic movement; Level A criterion |

## Refreshing the library

Search creator names and specific mechanisms, not only “beautiful website.” Try fluid, shader, generative art, cutaway, motion design, kinetic typography, interactive physics, camera, code animation, and soundtrack. Follow replies for prompts, source repositories, reference assets, and later corrections.

Record original post ID, root post versus reply when known, author, subject, evidence URL, prompt status, code/demo links, and date checked. Deduplicate by post ID while retaining project-level overlap. Add a one-sentence study question. Keep claims from the source separate from techniques you infer. Do not call the collection exhaustive or silently upgrade an index flag into a verified original prompt.


The [resource directory](resources.json) contains the maintained creator-linked inventory. Search it with `python3 scripts/search.py "your mechanism" --kind resources`; use [inspected sources](inspected-sources.md) for investigation records and their evidence limits; current totals belong to [research coverage](research-coverage.md).
