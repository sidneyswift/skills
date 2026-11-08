# Foundations

Use this guide for visual-system decisions. These are implementation-oriented
summaries, not a replacement for the linked platform sections. Checked 2026-11-08.

## Layout: organize, then adapt

Make the important content easy to find in the locale's reading order. Use alignment,
grouping, and spacing to communicate relationships before adding decoration. Disclose
secondary detail without hiding the main task.

Respond to the available space and supported size classes rather than hard-coded
device names. Preserve the selected item, task, and recognizable structure when a
window resizes. Respect safe areas for essential information and controls; backgrounds
may extend beyond them. Plan for the keyboard, longer translations, and large text.

**Check:** Resize a populated screen and an editing state. Verify that primary controls
remain reachable and content does not disappear behind system UI. Read the relevant
platform section before choosing fixed margins or component placement.

Source: [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

## Typography: preserve meaning at every size

Start with semantic text styles. Use a limited, intentional hierarchy; maintain its
relative importance when type grows. Custom type is valid when it remains legible
and supports the platform's scaling and accessibility behavior.

Let containers grow, wrap useful content, and switch crowded horizontal arrangements
to vertical ones. Avoid solving large-text overflow by shrinking text back down.
Meaningful symbols should scale with the associated text. Use Apple's live tables
for exact platform-specific specifications, not a universal font-size recipe.

**Check:** Compare the default and largest supported accessibility text settings with
realistic long content. Inspect important labels, amounts, errors, and action names.

Source: [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).

## Color and appearance: encode roles, not sampled values

Prefer semantic system colors for native roles; do not freeze a system color into a
sampled hex value. Custom brand colors still need deliberate light, dark, and increased
contrast treatments. Keep meanings consistent, and pair color-coded status with words,
symbols, or shapes. Evaluate contrast against the background actually rendered,
including imagery and translucency.

Honor the system appearance where appropriate. Dark Mode is not a simple inversion:
check image edges, text fields, backgrounds, elevation, and disabled states independently.

**Check:** Compare the same state in light/dark appearance and increased contrast.
Measure important foreground/background pairs; a visual impression is not a measurement.

Sources: [Color](https://developer.apple.com/design/human-interface-guidelines/color),
[Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode).

## Materials: distinguish controls from content

Current HIG guidance uses Liquid Glass for the functional layer, such as navigation
and controls, above content. It is not a treatment for every content card. Standard
materials support separation within the content layer. Let standard components obtain
their system appearance where supported; add custom glass selectively.

Choose materials for their role, not a blur amount copied from a screenshot. For custom
Liquid Glass, regular is the general legibility-oriented choice; clear is intended for
visually rich backgrounds such as media and needs contrast evaluation. Check reduced
transparency and increased contrast behavior. Verify API and OS support before coding;
older targets need suitable native fallbacks, not an assertion that a CSS blur is equivalent.

**Check:** Scroll busy content beneath the control and test relevant appearance settings.
The control must remain identifiable and legible throughout.

Source: [Materials](https://developer.apple.com/design/human-interface-guidelines/materials).

## Symbols and app icons: different jobs

Use familiar symbols for familiar actions, with a rendering mode and weight that fit
their context. Provide accessible text for meaningful custom symbols. Symbol animation
should communicate a state change, not run as decoration. Confirm each symbol and
effect exists in the supported OS version.

An app icon is an identity asset, not an enlarged toolbar glyph. Keep its recognizable
features across platform shapes and appearances. Follow the current Icon Composer,
layer, masking, and export guidance for the target; do not bake system effects or
platform masks into source artwork indiscriminately. Check asset licensing separately
before redistributing fonts, symbols, or Apple artwork.

Sources: [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols),
[App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons).

## Motion: explain a change without blocking work

Use motion to make transitions and consequences understandable. Favor responsive,
interruptible feedback over sequences people must wait through. Reduce or replace
nonessential motion when requested, preserving the information conveyed. Spatial
experiences need extra attention to peripheral motion, camera movement, and a stable
reference frame.

**Check:** Repeat the interaction quickly, interrupt it, and use Reduce Motion.
A still image cannot establish timing, continuity, or comfort.

Source: [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

## Accessibility: inspect the experience, not just the image

Expose meaningful labels, roles, values, and state to assistive technologies. Ensure
core actions have alternatives to difficult gestures and color-only or audio-only cues.
Check focus order, text enlargement, contrast, media alternatives, and reachable controls
using the relevant platform tools.

**Metric caution:** Apple's currently published table distinguishes default from minimum
control sizes: for iOS/iPadOS it lists 44×44 pt as default and 28×28 pt as minimum.
That does not make 28 pt a good blanket design target. Consider input, spacing, context,
and the specific component guidance. Do not label 44 pt a universal cross-platform
minimum, convert it directly to physical pixels, or conflate a small glyph with its
larger interactive region. Reopen the source before citing numbers.

Source: [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
