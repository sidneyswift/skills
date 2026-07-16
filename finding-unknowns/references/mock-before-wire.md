# Mock before you wire

Build a clickable throwaway mock of a UI change before touching the real app, so layout calls get made on a disposable artifact instead of in a refactor. Use when a feature has unresolved placement, layout, or scope questions and the real implementation would be expensive to move around.

Example trigger prompt:

> Before wiring anything up, make a single HTML file mocking the new frame-annotation toolbar with fake data. I want to react to the layout before you touch the real app.

## Output shape

One self-contained HTML file containing:

1. **The mock itself**, with plausible fake data, interactive enough to convey feel (toggles, hover states, an open/close drawer).
2. **Variant toggles** when placement is the question: render each candidate (e.g. floating pill, docked rail, under the seekbar) behind a toggle, each with a one-line characterization including a real-world anchor ("closest to what Loom/Frame.io ship").
3. **A wiring note**: one line stating that everything is fake and where the real implementation would live ("real wiring would live in `apps/player/src/annotate/Toolbar.tsx` behind the `frame_annotations` flag").
4. **Open questions**: 3 to 5 layout calls you would otherwise have to guess. Each question states the trade-off concretely ("inline is one click faster; popover shrinks the pill by ~140px, which matters on 13-inch laptops") and offers A/B/C chips.
5. **A self-filling reply template**: chip taps compose the user's answer for copy-paste.

## Quality bar

- Zero real code touched. The mock must not import from or modify the app.
- Ask only questions whose answer changes what gets built. If every option leads to the same code, decide it yourself.
- State costs in concrete units: pixels stolen, clicks added, seconds of render time, screen sizes affected.
- Cap the questions at five. A mock that asks twenty questions is a spec, and a worse one.
