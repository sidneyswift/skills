# Forward test — v0.1.0

Date: 2026-11-08

An independent agent loaded the skill and relevant references, then completed the
three requests below. It received no intended answers or suspected defects. The
author reviewed the resulting responses. These are design/review evaluations, not
runtime tests of an application. The repository packager excludes this directory.

## Description-only iPhone review

Request:

> Review this iPhone UI from this description only: the screen has five icon-only
> tabs including a central + that creates a new record, a blurred glass card for
> every record, and a small gear icon at top right. Tell me what is wrong and what
> you can verify.

Observed response:

- Identified the creation command as different from a tab destination and proposed
  moving it to a suitable action control without inventing another destination.
- Recommended useful visible tab labels, with verification of the running controls
  left as a separate task.
- Treated the card criticism conditionally: ordinary blur does not establish use
  of Liquid Glass, and standard content materials are not categorically forbidden.
- Did not claim five tabs are intrinsically wrong, a small glyph proves a small hit
  region, or an unseen accessibility implementation is broken.
- Distinguished current documentation checks from unperformed UI testing.

## SwiftUI app retaining iOS 17 support

Request:

> Our shipping SwiftUI app supports iOS 17 and newer. Add the new Apple glass look
> and support iPad resizing. Give a concrete implementation direction, not code;
> preserve our existing brand and main workflow.

Observed response:

- Kept the deployment target, brand, and workflow; started with standard navigation
  and selective custom treatment instead of a wholesale redesign.
- Consulted official API metadata: custom glass APIs require iOS/iPadOS 26;
  optional sidebar-adaptable tabs require 18; suitable split navigation predates 17.
- Specified compatible older-OS behavior and state preservation across resizing.
- Proposed touch, keyboard/pointer, window-size, accessibility, and appearance
  checks without claiming any device tests had run.

## Apple-inspired React dashboard

Request:

> Make our desktop React analytics dashboard feel Apple-inspired. Keep our brand
> and framework. Propose a focused design approach and acceptance checks.

Observed response:

- Scoped the proposal to an overview screen and retained React, routes, brand,
  metric definitions, and browser semantics.
- Used hierarchy, restrained surfaces, explicit controls, and useful state design
  instead of simulated Mac/iPhone chrome or a native-framework migration.
- Labeled translucency as a web adaptation, not native Liquid Glass.
- Proposed browser zoom, keyboard, focus, accessibility-tree, measured contrast,
  chart alternatives, and responsive checks; did not claim these had passed.

## Outcome and limits

No instruction defect was demonstrated by these three responses, so the trial did
not justify a skill rewrite. The Apple Markdown fallback worked after direct browser
fetches were unavailable. A guessed additional article returned 404 and was not used
as evidence; a retrieved official source supplied the needed guidance.

Not exercised: production implementation, rendered output, actual assistive technology,
physical devices, other Apple platforms, or operation with all source access unavailable.
Passing these scenarios does not establish universal HIG compliance.

## Structural checks

- Bundled skill-creator frontmatter validator: passed.
- UI metadata, skill name, version, and invocation consistency: passed.
- Seven relative Markdown links resolve.
- Forty-four distinct Apple links checked against retrieved root/topic content.
- Versioned ZIP built with this repository's `package.sh` in isolated staging;
  seven shipped files match their source bytes and archive integrity passes.
- Staged diff whitespace check: passed.
