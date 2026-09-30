# Sound patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [One event score for both audio and visual motion](#shared-score-clock)
- [Map frequency bands to different physical parts](#band-to-part)
- [A physical event that produces a musical note](#collision-instrument)
- [A drawing gesture that makes a musical phrase](#gesture-instrument)
- [Align an effect by its perceptual attack](#peak-alignment)
- [Sound synthesis tied to a visible material](#physical-timbre)
- [Change visual grammar with the musical section](#section-arrangement)
- [One seed creates a coherent visual and musical world](#seeded-universe)

<a id="shared-score-clock"></a>

## One event score for both audio and visual motion

**Mechanism:** Sound and picture use the same event times rather than two approximately synchronized timers.

**Build:**

1. Create a cue list in seconds or beats with one tempo conversion.
2. Schedule audio against its clock and derive visual time from the same playback origin.
3. For export, evaluate both from absolute timeline time.

**Tune:** Support pause and seek explicitly; recreate or cancel scheduled audio on transport changes.

**Failure check:** Play, pause, resume and seek repeatedly. Check a sharp visible impact against its audible onset.

**Adapted prompt:** Compose [piece] from one shared cue score that drives both visible events and sound.

**Evidence:** [@aiehon_aya](https://x.com/aiehon_aya/status/2103403361022419005), [@GroundControl](https://x.com/GroundControl/status/2103679486629659063). Creator description/prompt; verify the visual when fidelity matters.


<a id="band-to-part"></a>

## Map frequency bands to different physical parts

**Mechanism:** A deliberate mapping turns music into a coordinated mechanical performance.

**Build:**

1. Extract band envelopes and onset events from the actual track.
2. Assign low, mid and high activity to distinct parts with different response characteristics.
3. Use the song section to change the arrangement instead of scaling every effect together.

**Tune:** Normalize per band and add attack/release smoothing. Keep an inactive baseline so silence has a visible form.

**Failure check:** Mute one band or inspect it alone. Its assigned part should have a clear specific response.

**Adapted prompt:** Make [mechanical object] perform the music through separate bass, transient and high-frequency behaviors.

**Evidence:** [@Acoramaa](https://x.com/Acoramaa/status/2104145227573248467), [@aratamadao](https://x.com/aratamadao/status/2103706285204255186). Creator description/prompt; verify the visual when fidelity matters.


<a id="collision-instrument"></a>

## A physical event that produces a musical note

**Mechanism:** Visible contact and audible onset are one event, making the piece understandable by ear and eye.

**Build:**

1. Emit a contact event from the collision model.
2. Map body identity or location to a pitch set and impact energy to a bounded intensity.
3. Debounce resting contacts so one collision does not create a machine-gun trill.

**Tune:** Limit polyphony and shape note decay; use an intentional scale if harmony is desired.

**Failure check:** Slow playback and inspect first contact. The note must not precede the collision or repeat while objects rest together.

**Adapted prompt:** Turn [physical system] into an instrument where every note is caused by a visible event.

**Evidence:** [@KamStudioLabs](https://x.com/KamStudioLabs/status/2102899866762440893), [@kantamk](https://x.com/kantamk/status/2103148907228176511). Creator description/prompt; verify the visual when fidelity matters.


<a id="gesture-instrument"></a>

## A drawing gesture that makes a musical phrase

**Mechanism:** Gesture position, speed and pauses control an instrument rather than adding background music.

**Build:**

1. Choose a mapping from position to pitch or scale degree.
2. Use speed or pressure for articulation and brightness.
3. Trigger notes at distance or time thresholds, then add a brief release to avoid clicks.

**Tune:** Keep note density bounded; preserve silence when the gesture stops.

**Failure check:** Draw slowly, quickly and in place. Sound must respond predictably without becoming a continuous harsh tone.

**Adapted prompt:** Make [creative gesture] playable as [instrument], with a clear relation between movement, pitch and articulation.

**Evidence:** [@AxtonLiu](https://x.com/AxtonLiu/status/2103288413969621231), [@DemitiyaGeekzen](https://x.com/DemitiyaGeekzen/status/2103517910274818523). Creator description/prompt; verify the visual when fidelity matters.


<a id="peak-alignment"></a>

## Align an effect by its perceptual attack

**Mechanism:** The significant transient may occur after the beginning of the sound file.

**Build:**

1. Measure or listen for the attack offset within each effect.
2. Place the clip start at visualEventTime minus attackOffset.
3. Check the final mixed and encoded output, not only the source timeline.

**Tune:** Use the perceptually relevant attack rather than blindly choosing the largest later peak.

**Failure check:** Inspect a sharp event at slow playback and listen at normal speed. Trimmed leading silence must not shift the intended hit.

**Adapted prompt:** Synchronize [sound effect] to [visible action] using its actual attack rather than its file start.

**Evidence:** [@twoclipping](https://x.com/twoclipping/status/2102554209166000267). Creator description/prompt; verify the visual when fidelity matters.


<a id="physical-timbre"></a>

## Sound synthesis tied to a visible material

**Mechanism:** The sound suggests how the visible object vibrates or is struck.

**Build:**

1. Choose an excitation and resonator model appropriate to the material.
2. Drive the excitation from the visible action and vary resonance with a meaningful parameter.
3. Keep a separate ambience layer so every movement does not require a loud accent.

**Tune:** Tune attack and decay before reverb. Prefer a small coherent sound vocabulary.

**Failure check:** Compare repeated actions at different strengths. Timbre and intensity should remain related to the object.

**Adapted prompt:** Give [material/object] a sound model whose attack, resonance and decay follow the action seen on screen.

**Evidence:** [@Rakhsh_Tech](https://x.com/Rakhsh_Tech/status/2104144532644544921), [@iniyanai](https://x.com/iniyanai/status/2103814603100856596). Creator description/prompt; verify the visual when fidelity matters.


<a id="section-arrangement"></a>

## Change visual grammar with the musical section

**Mechanism:** Sections change the composition and behavior vocabulary, not only effect intensity.

**Build:**

1. Mark phrase boundaries, quiet passages, builds and releases in the real track.
2. Assign a visual grammar to each section and maintain one connecting motif.
3. Reserve the most complex arrangement for the intended peak.

**Tune:** Use contrast in density, scale and stillness; avoid identical cuts on every beat.

**Failure check:** Watch the full piece without sound, then listen without picture. The large-scale energy arcs should still correspond.

**Adapted prompt:** Design [music piece] around its actual sections, with changing composition and a recognizable motif across them.

**Evidence:** [@aratamadao](https://x.com/aratamadao/status/2103706285204255186), [@pound75423](https://x.com/pound75423/status/2103722560462475314). Creator description/prompt; verify the visual when fidelity matters.


<a id="seeded-universe"></a>

## One seed creates a coherent visual and musical world

**Mechanism:** A shared seed coordinates choices while separate streams prevent accidental coupling. Use for repeatable, personalized visual and musical worlds generated from text input such as a visitor name.

**Build:**

1. Hash the user input into a stable seed.
2. Derive named sub-seeds for palette, geometry, rhythm and melody.
3. Constrain each generator to a designed vocabulary so random output still feels authored.

**Tune:** Changing particle count must not unexpectedly change the melody; use independent streams.

**Failure check:** The same input should reproduce the same world. Small implementation changes in one subsystem should not scramble the others.

**Adapted prompt:** Turn [user input] into a repeatable visual and musical world using constrained generators with independent named random streams.

**Evidence:** [@MiaAI_lab](https://x.com/MiaAI_lab/status/2103837521645867073). Creator description/prompt; verify the visual when fidelity matters.
