# September 30, 2026 — one gesture, one tangible release

Added [tangible-release guidance](../interactive-3d.md#turn-a-gesture-into-one-tangible-release) for mechanical toys and product interactions. Original synthesis covers preparation, a one-event latch, payload ownership, secondary action, refill/history semantics and edge-case checks. No new pattern count or third-party implementation bundled.

**Attribution:** [Mengxue Bi's September 28 post](https://x.com/MengxueBi/status/2104619977454362948),17:11:19UTC, explicitly credits Opus5.5 and Blender. The short-prompt and production claims are creator descriptions; no full prompt or Blender source was retrieved.

**Observed live:** [Pull-Arm Candy Dispenser](https://m-ms-dispenser.vercel.app/). A downward hand drag released a yellow candy: stock30→29 and yellow tally0→1. It settled on the table. Tapping it changed Eaten0→1 while the historical tally remained1. A small pull left those counts unchanged. Tapping the top cap replenished stock to30 while preserving the tally and Eaten1. Customize exposed scene/color/sound choices; those alternatives were not exercised. A final screenshot and accessibility snapshot were archived.

**Inspected public inline code:** pointer hit testing/capture, pull tracking, fire/rearm conditions, dynamic payload creation, removal/consumption guards and refill. A ready flag is cleared at firing and only reset below a separate lower pull threshold. A consumed object's hit target and physics body are removed before its visual disappearance completes. The table-count limit removes an older payload without increasing Eaten, so visible stock/consumption alone is not a conservation ledger.

**Implementation cautions:** source pointer velocity uses a fixed event-rate factor, and pointer cancellation shares the pointer-up handler. The guide recommends measured input time and an explicit cancel path for original builds; these are not source features verified as correct. Full held-input, cancellation, exhaustion and concurrent-input tests were not performed.

**Limits:** sound was not auditioned. No physics-fidelity, complete keyboard-accessibility, mobile, performance or asset-provenance audit. Public page code license was not established; linked branded artwork remains a reference, not a bundled asset or project-independent branding requirement.

Totals:1,294 catalog records,129 resources,104 patterns. No additional paid API spend.
