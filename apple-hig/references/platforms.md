# Platform fit

Read the target section, then the platform considerations in each component's Apple
page. These are starting points, not frozen hardware assumptions. Verify capabilities
and OS support in the actual project. Checked 2026-11-08.

## iOS

Prioritize the task and reachable controls for handheld, often interrupted use.
Preserve standard back navigation and gesture alternatives. Support the relevant
orientations, appearance changes, and Dynamic Type without losing context. Use platform
capabilities to reduce effort only with the appropriate access.

**Acceptance probe:** Complete the main action in a narrow layout, with the keyboard
visible and enlarged text; background and resume during editing.

Source: [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios).

## iPadOS

Use space to show relevant content and reduce unnecessary modal transitions. Adapt
to the window, not just the full physical display. Support touch plus keyboard/pointer,
and Pencil where it genuinely serves the task. Preserve selection and access to actions
as columns collapse. Do not assume a sidebar is always the starting navigation choice;
consult current tab-bar guidance.

**Acceptance probe:** Resize while editing a selected item, then perform the same
task with touch and keyboard/pointer. Inspect the smallest supported window.

Source: [Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados).

## macOS

Design for sustained work, resizable windows, menus, keyboard shortcuts, and precise
selection. Use available space to reduce unnecessary navigation depth. Respect standard
commands and window behavior; let people arrange their workspace. Check current
device/input guidance instead of asserting that all Macs have the same inputs.
For touch-capable targets, preserve desktop density while adapting hit regions and
revealing controls appropriately; touch must not be the only way to reach functionality.

**Acceptance probe:** Complete the primary flow keyboard-only, resize the window,
switch between windows, and verify menu/toolbar command consistency.

Sources: [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos),
[Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures),
[Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices).

## watchOS

Reduce the experience to concise, glanceable information and focused actions. Keep
hierarchy shallow and use Digital Crown behavior appropriately. Consider complications
and notifications when they serve the task, without making the app itself dependent
on another device. Minimize text entry and extended waiting.

**Acceptance probe:** Can the essential task be completed in a brief interaction
without typing a form or watching a long spinner? Check supported small-display and
larger-text configurations.

Source: [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos).

## tvOS

Design for viewing from across a room, remote input, and a prominent focus state.
Make focus movement predictable and readable; do not depend on touch/hover behavior
copied from a phone or website. Minimize typing, support convenient authentication,
and preserve the correct viewer's context in multiuser experiences.

**Acceptance probe:** Navigate every essential control using the supported remote or
controller path. Check where focus lands after a dialog closes or a result disappears.

Source: [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos).

## visionOS

Choose the least immersive presentation that serves the moment. Use windows for
familiar UI tasks, spatial content when depth adds value, and deeper immersion
intentionally. Support comfortable eye-and-hand interaction and indirect gestures
that do not require sustained reaching. Preserve legibility across placement and scale.
Avoid unnecessary movement of the surrounding world and excessive peripheral motion.
Content placement relative to a person is not a blanket instruction to rigidly attach
everything to their head.

**Acceptance probe:** Evaluate selection, spacing, text, and movement in the supported
spatial environment. A desktop screenshot cannot prove physical comfort, eye-target
selection, or in-headset readability; mark those unverified without device testing.

Source: [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos).

## Cross-platform input

Keep standard gestures and shortcuts meaningful. Additional gestures may accelerate
an action but should not become its only accessible route. Use standard pointer and
focus behavior where appropriate, and support keyboard access without repurposing
system shortcuts. Shared product intent does not require identical screen layouts.

Sources: [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures),
[Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices),
[Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards).
