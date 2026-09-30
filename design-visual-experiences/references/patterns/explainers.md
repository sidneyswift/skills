# Explainers patterns

Read only the mechanisms relevant to the brief. Build steps, tuning and prompts below are original adaptations, not verbatim creator prompts. Source links establish the described idea; they do not prove every requested effect was achieved. Numeric suggestions are starting points to test.

## Contents

- [Compare mechanisms under the same input](#shared-control-comparison)
- [An optical explainer whose image comes from its model](#computed-optical-image)
- [A cutaway that follows a moving substance](#flow-cutaway)
- [Explain a process across several scales](#causal-scale-story)
- [An explanatory animation driven by real outputs](#data-backed-image)
- [Link a spatial selection to a time series](#linked-space-time)
- [A layout tool that shows the consequences of placement](#constraint-aware-layout)
- [Make a resource rule visible through conserved quantities](#token-conservation)

- [A mechanical explainer whose contacts compute the answer](#contact-driven-computation)

<a id="shared-control-comparison"></a>

## Compare mechanisms under the same input

**Mechanism:** A common control makes different responses directly comparable.

**Build:**

1. Define one input variable with units and a valid range.
2. Feed it into each model and align camera, time scale and labels.
3. Add a synchronized slow-motion control without changing the underlying input relationship.

**Tune:** Keep the comparison frame and colors stable; highlight the differing mechanism only.

**Failure check:** Set equal inputs and pause at the same phase. Labels, speeds and outputs must agree with the models.

**Adapted prompt:** Compare [two mechanisms] under one shared [input], using synchronized time and matched views to expose the difference.

**Evidence:** [@StefanoStraus](https://x.com/StefanoStraus/status/2104236916316971191). Creator description/prompt; verify the visual when fidelity matters.


<a id="computed-optical-image"></a>

## An optical explainer whose image comes from its model

**Mechanism:** The visible result changes because the simulated rays or mapping change.

**Build:**

1. Choose and state the approximation: ray tracing, geometric projection or a stylized mapping.
2. Compute the image or ray paths from editable parameters.
3. Display controls and labels that expose the relationship between cause and output.

**Tune:** Limit adjustable parameters to a few understandable ones. Separate aesthetic lens distortion from the instructional model.

**Failure check:** Change one parameter and verify the expected direction of change against a known simple case.

**Adapted prompt:** Explain [optical phenomenon] with imagery computed from the model, including a clear statement of the approximation.

**Evidence:** [@cagrimbakirci](https://x.com/cagrimbakirci/status/2104011756397842869), [@The_MrAI](https://x.com/The_MrAI/status/2104068960035713523). Creator description/prompt; verify the visual when fidelity matters.


<a id="flow-cutaway"></a>

## A cutaway that follows a moving substance

**Mechanism:** The viewer follows a coherent route through components instead of seeing a disconnected exploded diagram.

**Build:**

1. Model the physical path as connected segments with named components.
2. Animate tracers along path distance and show flow direction consistently.
3. Reveal cutaway geometry as the tracer reaches a component, then connect its behavior to a control.

**Tune:** Keep path topology readable before adding dense particles; use distinct channels for separate fluids.

**Failure check:** Trace the whole route manually. No tracer should jump between unconnected channels or move against its arrow.

**Adapted prompt:** Explain [system] by following [substance] through its actual connected path and exposing each component at the useful moment.

**Evidence:** [@konstantinsaifo](https://x.com/konstantinsaifo/status/2104094723887501736). Creator description/prompt; verify the visual when fidelity matters.


<a id="causal-scale-story"></a>

## Explain a process across several scales

**Mechanism:** Each new scale explains the consequence of the previous stage.

**Build:**

1. List the entities and transformations in order before designing transitions.
2. Preserve a recognizable substructure at each handoff.
3. Distinguish literal scale, schematic spacing and time compression in the explanation.

**Tune:** Use fewer stages with clear causality rather than a spectacular unlabelled zoom.

**Failure check:** Ask whether each transition answers what changed and why. Independently verify scientific claims and quantities.

**Adapted prompt:** Connect [small process] to [large outcome] through a sequence of causal transformations with explicit scale and time assumptions.

**Evidence:** [@mrmagan_](https://x.com/mrmagan_/status/2103470233080254891). Creator description/prompt; verify the visual when fidelity matters.


<a id="data-backed-image"></a>

## An explanatory animation driven by real outputs

**Mechanism:** The picture uses actual data or model results instead of a convincing-looking substitute.

**Build:**

1. Load or generate the real dataset with a recorded source and processing step.
2. Bind visible marks, counts and labels to that output.
3. Keep a clear distinction between sample data, measured results and illustrative geometry.

**Tune:** Reduce data volume for clarity without changing its meaning; expose the aggregation rule.

**Failure check:** Recompute a few displayed values independently. A changed input must update the corresponding visual output.

**Adapted prompt:** Make [concept] visible using real [data/model outputs], with every displayed number traceable to the underlying computation.

**Evidence:** [@ng169onX](https://x.com/ng169onX/status/2103183904563998809), [@arambarnett](https://x.com/arambarnett/status/2104011150471917838). Creator description/prompt; verify the visual when fidelity matters.


<a id="linked-space-time"></a>

## Link a spatial selection to a time series

**Mechanism:** Selecting a point in the scene reveals its behavior over time.

**Build:**

1. Use stable IDs for spatial samples and their time-indexed values.
2. Bind the selected point, chart highlight and current-time marker to one state.
3. Explain units, sampling interval and the source of the values.

**Tune:** Choose meaningful defaults and avoid implying fine precision from coarse samples.

**Failure check:** Select several locations and scrub time. The chart and scene must identify the same sample and timestamp.

**Adapted prompt:** Let viewers select [spatial feature] and inspect its [time-varying quantity] through synchronized scene and chart views.

**Evidence:** [@mizugame_22](https://x.com/mizugame_22/status/2104045418141368438). Creator description/prompt; verify the visual when fidelity matters.


<a id="constraint-aware-layout"></a>

## A layout tool that shows the consequences of placement

**Mechanism:** Moving objects changes computed clearances and feasibility, not just the picture.

**Build:**

1. Represent footprints, doors and required clearance zones separately.
2. Recompute collisions and passage widths from object transforms.
3. Display the active conflict beside the affected geometry and offer a reversible adjustment.

**Tune:** Prioritize major passage conflicts before small decorative overlaps; document assumed dimensions.

**Failure check:** Rotate, resize and move objects through boundaries. Reported clearance must match the visible geometry.

**Adapted prompt:** Make [planning scene] editable with real geometric constraints and immediate explanations of what a placement changes.

**Evidence:** [@goofyninjaaa](https://x.com/goofyninjaaa/status/2103540288136315331). Creator description/prompt; verify the visual when fidelity matters.


<a id="token-conservation"></a>

## Make a resource rule visible through conserved quantities

**Mechanism:** A resource animation becomes explanatory when its counters obey the same rule as its marks.

**Build:**

1. Implement the resource update independently of rendering.
2. Represent each admission, refill and rejection as an event from that model.
3. Derive labels and moving tokens from the event log so they cannot disagree.

**Tune:** Choose a slowed demonstration time without changing the ratios; expose capacity and rate in units.

**Failure check:** Test empty, full, burst and steady input. Counts must never become negative or exceed capacity.

**Adapted prompt:** Explain [rate or queue rule] with a working model, synchronized counters and visible admissions or rejections.

**Evidence:** [@ParkerRex](https://x.com/ParkerRex/status/2103206747846701462). Creator description/prompt; verify the visual when fidelity matters.

<a id="contact-driven-computation"></a>

## A mechanical explainer whose contacts compute the answer

**Mechanism:** Arrival events change discrete state; the displayed answer is decoded from that state after the visible process settles.

**Build:**

1. Define a transition table for each gate and route an arriving token according to its previous state.
2. Use one arrival handler to mutate state, trigger the visible gate response and choose the outgoing path. Keep joins continuous.
3. Derive output from final gate states. Test against an independent oracle and verify that every state change occurred at its visible contact.

**Tune:** Use fixed simulation steps and arc-length paths for stable timing. Slow important contacts enough to explain the change; separate render quality from simulation state.

**Failure check:** Verify limiting inputs, carry chains, reset and interruption. A correct final value alone is insufficient: every transition must have an on-screen cause. Scripted paths are not rigid-body physics.

**Adapted prompt:** Build [process] so its visible interactions actually drive the state being explained. Derive the readout from the resulting state and test both the final answer and the causal events.

**Evidence:** Creator prompt retrieved. Astra mechanism and test code inspected at revision 1f3dddb74ab2180ec139413706632e0f4ff17c5a. All four supplied tests passed locally, including 256 input pairs. Browser visuals, sound and frame rate were not assessed. [Creator post](https://x.com/GodsBoy7777/status/2103117450854150194).
