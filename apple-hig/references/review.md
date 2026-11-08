# Review and verification

This is the skill's review procedure, not an Apple scoring system. Use only the
checks relevant to the requested work. Read [Sources](sources.md) to verify a rule.

## Establish evidence

State what was inspected: screenshots, design file, source code, rendered build,
simulator, device, or assistive-technology run. Record target platform and OS when
known. Distinguish an observed defect from a probable issue and an untested question.

| Evidence | Can support | Cannot establish by itself |
|---|---|---|
| Screenshot | Visible hierarchy, copy, crowding, apparent state | Actual hit regions, screen-reader labels, focus, motion, adaptability |
| Source inspection | Declared semantics, layout rules, availability checks | What renders on every device or how comfortable it is |
| Interactive preview | Exercised controls and rendered states | Native behavior absent from that preview |
| Device/accessibility test | Specific behavior in the tested configuration | All platforms, OS versions, or user needs |

## Follow the person's task

1. Locate the primary action and navigation context.
2. Complete the flow using the relevant input method.
3. Exercise applicable interruption, error, cancellation, and recovery paths.
4. Change the meaningful conditions: window size, text size, appearance, locale,
   reduced motion/transparency, keyboard/pointer, or accessibility interaction.
5. Recheck the affected behavior after a fix. Report untested conditions explicitly.

Use Accessibility Inspector, VoiceOver, simulator/device settings, contrast tooling,
or framework tests where available. A static review should leave a targeted test list,
not pretend these tools ran. For web adaptations, use browser/accessibility-tree and
keyboard checks appropriate to the web rather than claiming native coverage.

## Findings format

```text
[Impact] Screen/component — finding
Evidence: artifact, state, and observation; distinguish inference if necessary.
User consequence: what becomes harder, inaccessible, misleading, or unsafe.
Basis: specific Apple page + platform section, or clearly labeled project rationale.
Change: smallest concrete repair that addresses the consequence.
Verify: observable condition that would demonstrate the repair.
```

Order by consequence: blocked task or data loss; substantial access/usability
problem; then clarity and polish. These are local prioritization labels, not official
HIG severity levels. Do not invent numeric scores or pad the report to a fixed count.

## Example: bounded inference

Given only an iPhone screenshot with an icon-only trailing control:

- Reasonable: the symbol's meaning is ambiguous in this context; propose a clearer
  symbol or visible label and cite Buttons guidance.
- Needs verification: measure the control's interactive region and inspect its
  accessibility label in the running app.
- Unsupported: declaring that VoiceOver is broken or that the tap target is exactly
  the icon's visible dimensions.

## Finish

Provide the highest-impact findings or say none were found within the inspected
scope. List only material open checks and confirmed deviations. A successful build,
visual polish, or use of native components alone does not demonstrate accessibility,
HIG compliance, or App Store acceptance.
