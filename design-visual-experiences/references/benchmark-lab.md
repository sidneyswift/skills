# Benchmark lab: studies in feeling

Three original, editable experiences turn selected mechanisms into complete small briefs. They are practice artifacts, not proof of superior model performance or a guarantee of exceptional taste. No third-party implementation, font, media or prompt is bundled here.

## Run and adapt

From the skill directory, run `python3 -m http.server 8766 --bind 127.0.0.1 --directory assets`, then open `http://127.0.0.1:8766/benchmark-lab/`. The [studio](../assets/benchmark-lab/index.html) imports ES modules, so serve it over HTTP. Its [application](../assets/benchmark-lab/app.mjs), [models](../assets/benchmark-lab/models.mjs) and [stylesheet](../assets/benchmark-lab/style.css) are editable. Run `node scripts/test-benchmarks.mjs` for numerical checks.

| Brief | Defining moment | Parameters worth changing | Failure to look for |
|---|---|---|---|
| Resonance: an inviting seven-string instrument | Held tension becomes a released vibration | Damping, natural frequency, release velocity, pluck location, partial gains | A jump on release; scrolling cancels touch; visually active but inaudible interaction |
| Make room: a 12-second motion identity | Scattered marks gather, arrange, then become the words MAKE ROOM | Gather/stack/morph intervals, stagger, motif scale, text hold | Marks vanish before the idea arrives; intermediate copy competes with the action; unreadable payoff |
| A distant pull: an explainer about relative influences | Moving the Moon changes both a profile and its measured range | Angle, solar contribution, illustrative exaggeration | Readout disagrees with geometry; controls have no visible consequence; approximation appears factual |

## Art direction as decisions

Resonance uses fine copper lines, pin highlights and restrained soundboard contours to make displacement the main event. The film gives the small mark a large job: its identity survives from disorder to lettering. The explainer keeps a quiet orbital diagram and uses two named extremes to turn exploration into a testable comparison. The shared editorial shell is convenient for comparison, not a template to impose on projects.

For a new brief, choose one visual rule and one behavioral invariant. Examples: “every mark survives the transformation,” “the dragged point has the same position immediately after release,” or “one angle controls both diagram and readout.” Define what may vary and what must remain recognizable. A deliberate cut can be better than a morph; continuity is useful here because the film's subject is arrangement.

## September 29 review and revision

| First version or code finding | Revision | Evidence |
|---|---|---|
| Film marks faded out while an unrelated text layer faded in; rhythm copy crossed the grid | Persistent mark identities travel to original bitmap glyph targets; copy moves below the grid | Browser frames at arrangement and payoff, scrub, replay and completion |
| Pointer release reset velocity and used a different endpoint mapping; cancellation discarded the held state | Track pointer identity and sampled velocity; use one geometry mapping; cancel quietly from held displacement | Code inspection, finite-difference continuity tests, browser pluck; cancellation itself not device-tested |
| First tide outline could intersect the solid Earth; values were only drawn into Canvas | Increase illustrative shell offset; expose range in live DOM text; add both reference extremes | Browser alignment, right-angle, drag and Sun-toggle checks; independent dense-extrema calculation |
| Final film divider crossed the bottom row of lettering | Move divider and closing line below glyphs | Revised payoff screenshot |

Do not turn these into universal rules. The useful lesson is how a visible weakness leads to a specific edit and a repeatable check.

## Evidence and limits

- Browser exercised: string dragging, keyboard note 4, reset, study switching, film seeking/replay to 12-second stop, Moon dragging, aligned/right-angle presets and removing the Sun. No captured browser warnings/errors in the inspected log.
- Composition inspected in sampled desktop states and with a narrow viewport override. The browser reported a 433 CSS-pixel document width under the nominal 390-pixel override; this is responsive desktop evidence, not a real phone test.
- 44 model checks cover deterministic seeking, release initial displacement/velocity, endpoint geometry and analytic tide range against independently sampled extrema.
- Playback was run and sampled. No frame-time profile, continuous captured video assessment, real touch-device check, auditory listening, screen-reader session or exported-film verification was performed. Reduced-motion behavior was inspected in code, not tested through an OS preference change. Optional audio remains unverified by listening.
- The instrument is a visual oscillator with synthesized partials, not a physical string solver. Its release handoff is tested; catching an already vibrating string is not modeled as a complete physical contact event.
- The tide model is an original angular harmonic illustration: `cos(2*(theta-moon)) + 0.46*cos(2*theta)`. Solar contribution is optional. The readout is the maximum minus minimum of this normalized profile. This is not a coastal prediction or full equilibrium simulation. [NOAA explains alignment and spring/neap variation](https://oceanservice.noaa.gov/facts/springtide.html); it does not validate this implementation's exaggeration or units.

## Use benchmarks to improve the skill

1. Freeze a short brief, references, constraints and delivery target before building. Hold these constant when comparing skill versions.
2. Save the first playable attempt and its exact source. Choose inspection moments before polishing: initial view, defining action, interrupted action, result, reset, narrow layout.
3. Write the largest weakness as an observation at a specific state or time. Label code-only findings separately. Fix it and revisit the same state.
4. Record the change that helped, the parameters that mattered and an unsuccessful approach if informative. Promote reusable guidance; do not add a pattern for every cosmetic variation.
5. Let a person compare results without telling them which is newer where practical. Ask which better communicates the idea, which behavior feels convincing, and what remains generic. Do not substitute self-assigned aesthetic scores for that judgment.
6. Keep some briefs unseen during skill editing. Only repeated improvement on new briefs supports a claim of better generalization. This first three-build pass is formative, not a controlled evaluation.

Original adaptation prompt:

> Build [experience] around [one visible idea]. Preserve [identity or causal invariant]. Establish a distinctive still frame, then make the hardest action work. Save a first playable version. Inspect [named states] and identify the largest concrete weakness. Revise that weakness, show the same states again, and explain which principle transfers to other work. Separate visual observation, numerical testing and unresolved taste judgments. Use existing project branding and tools.
