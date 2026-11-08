---
name: apple-hig
description: >-
  Design, implement, or review Apple-platform interfaces using Apple's Human
  Interface Guidelines. Use for iOS, iPadOS, macOS, watchOS, tvOS, and visionOS
  UX decisions, native navigation and controls, accessibility, adaptive layout,
  or Liquid Glass adoption. Also use when explicitly asked for an Apple HIG
  audit or Apple-inspired interface; do not automatically impose native Apple
  conventions on unrelated websites or replace a project's brand.
metadata:
  author: Sidney Swift
  version: "0.1.0"
  source: "https://developer.apple.com/design/human-interface-guidelines"
  source_checked: "2026-11-08"
---

# Apple Human Interface Guidelines

Translate the HIG into decisions about the actual product, not a generic
Apple-looking skin. This is an independent, selective synthesis with links to
Apple's authoritative guidance; it is not Apple's documentation or certification.

## Contract

- Fit the task, target platform, supported OS versions, and existing design system.
- Connect recommendations to an observed problem or a concrete design decision.
- Distinguish Apple guidance, project constraints, and this skill's adaptations.
- Deliver the requested design, implementation, or review with honest verification.

## Workflow

### 1. Establish the context

Inspect the brief, screens, relevant code, and project instructions. Establish:

- **Person and task:** What are they trying to accomplish? What matters most?
- **Surface:** Platform, device/window sizes, input methods, minimum OS, framework.
- **Constraints:** Brand, existing navigation, accessibility, localization, state/data.
- **Mode:** Design/specification, implementation, or review. Infer it from the request.

Infer routine details from the project. Ask only when a missing fact would change
the result. Do not turn a component fix into a redesign or require a spec approval
before carrying out an already authorized implementation.

For an Apple-inspired website, preserve browser semantics, responsive behavior,
and the project's web accessibility requirements. Treat HIG patterns as inspiration,
not native API instructions or a reason to recreate desktop/iPhone chrome.

### 2. Load guidance for the decision

Read only the references that serve the task:

| Decision | Reference |
|---|---|
| Hierarchy, type, color, materials, symbols, motion | [Foundations](references/foundations.md) |
| Navigation, controls, sheets, forms, onboarding, permissions, state | [Patterns](references/patterns.md) |
| Platform ergonomics and input differences | [Platforms](references/platforms.md) — read the target section |
| Acceptance checks and evidence-based findings | [Review](references/review.md) |
| Current source lookup, exact values, unbundled topics | [Sources](references/sources.md) |

For consequential recommendations, open the relevant Apple page and its platform
section. Recheck exact metrics, new materials, component behavior, and API availability
against the target OS/SDK; a current HIG page is not a deployment-target guarantee.
If browsing is unavailable, use the bundled synthesis, identify version-sensitive
assumptions, and do not claim they were verified. A scoped task does not require
crawling the whole HIG.

### 3. Decide the structure before styling

Use Apple's current [design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)
as competing decision criteria, not a compliance score:

| Principle | Question to resolve |
|---|---|
| Purpose | Does this help accomplish the product's central task? |
| Agency | Can people control the flow and recover from mistakes? |
| Responsibility | Are consequences and data use understandable? |
| Familiarity | Can people reuse what they already know? |
| Flexibility | Does the experience accommodate different contexts and abilities? |
| Simplicity | Is the structure clear without hiding necessary capability? |
| Craft | Have details and failure states been considered and tested? |
| Delight | Does the personality support the experience rather than delay it? |

Choose the navigation model, main action, information hierarchy, and recovery path.
Separate destinations from commands; distinguish persistent navigation from a
temporary task. Prefer native components for native behavior, then customize where
the product benefits. Preserve brand through content, imagery, voice, and purposeful
styling without sacrificing recognizable interaction.

### 4. Produce the requested work

**Design:** Specify the flow, component choices, content hierarchy, key states,
adaptive behavior, and accessibility acceptance criteria. Show a mockup or prototype
when useful. Explain significant departures from platform convention.

**Implement:** Use the project's framework and design tokens. Verify availability
before introducing an API. Include state, semantics, input behavior, and appropriate
fallbacks, not just the default screenshot. Inspect the rendered result and exercise
the affected interaction when the environment permits.

**Review:** Inspect actual artifacts. Use the [review format](references/review.md)
to report actionable findings, ordered by user impact. A screenshot supports visual
observations; it does not prove focus order, VoiceOver behavior, tap regions, latency,
or runtime adaptation. Keep those as checks to perform, not confirmed defects.

### 5. Verify the affected experience

Exercise the primary flow and relevant empty, loading, error, cancellation, and
recovery states. Check the target's input methods, larger text, appearance settings,
and window/device adaptations. Scale this to the change; a wording adjustment does
not require a full platform audit. Record unavailable device or assistive-technology
testing rather than silently treating it as passed.

## Output

Deliver the artifact or changes first, followed by the key decisions, supporting
Apple links where material, and what was actually verified. For a review, lead with
findings or state that no actionable findings were found within the inspected scope.
Do not claim universal HIG compliance, App Store approval, or measured usability
from a checklist.

## Anti-patterns

- Treating HIG recommendations as identical requirements across every Apple platform.
- Quoting memorized pixel sizes, tab counts, or API availability as timeless rules.
- Confusing visual size with hit area, or points with physical pixels or CSS pixels.
- Using blur, rounded rectangles, and animation as a substitute for clear behavior.
- Flattening the product's identity into an Apple clone or ignoring its supported OS.
- Inventing audit defects, source claims, measurements, or testing that did not occur.

## Tools

Use available browsing, code inspection, preview, simulator/device, and accessibility
tools as needed. No particular vendor tool, installed companion skill, paid service,
or production access is required. This skill grants no additional publishing authority.
