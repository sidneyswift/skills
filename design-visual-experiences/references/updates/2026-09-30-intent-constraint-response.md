# September 30, 2026 — make the physical limit explain the motion

Added [intention, constraint and response](../simulation-verdicts.md#show-intention-constraint-and-response-separately) to the existing simulation guide. Original synthesis covers three distinct state values, visible accumulation, historical constraint flags, replay that preserves tuned settings, and honest comparison assumptions. No new pattern count.

**Attribution:** [Lukasz Samson's September 28 post](https://x.com/lukaszsamson/status/2104680852366262458) explicitly credits Opus 5.5 and claims one-shot creation. Its [creator reply](https://x.com/lukaszsamson/status/2104680919198056903) links [PID Flight Lab](https://pid-flight-lab.netlify.app/). Dates and bodies read from archived retrieval and live X. The generation process was not independently verified; no full prompt retrieved.

**Observed live:** opened integral-windup lesson, then paused around simulation time 9.9s. The displayed altitude was 7.58m against a 3m target; the chart showed the thrust cap, accumulated integral term and red path segment. Changed anti-windup from off to clamping, then selected Fly this setup: time reset to0, altitude to3m, accumulated term to9.8, and clamping remained selected. Pause state also persisted until Play was selected. This is a selected-state inspection, not an exhaustive or quantitative comparison of policies.

**Inspected code:** archived public HTML on September30; controllerTick computes requested output and a bounded command, physics advances actual thrust with motor lag, and historical trail records contain saturation flags consumed by rendering. Replay preserves a listed set of controller gains/policy/filter/noise/delay/rate settings while restoring scenario defaults and scripted events. Mass and wind are not in that preserved list. Gaussian noise uses Math.random without a seed, so equal-input replay was not established. Relevant code sections were read, not copied into the skill or independently executed as a test suite.

**Limits:** not all12lessons, scientific fidelity, numerical convergence, accessibility, audio, mobile behavior or performance verified. The displayed linear stability estimate omits thrust limits and ground constraints by its own description. No source repository or explicit code license established for this page; retain links and original guidance only.

The same pass read the full [notdwd motion tutorial](https://x.com/notdwd/article/2104684539142648062). Reference analysis, scoped critique, rendering and sound principles substantially overlap installed guidance. Its per-frame easing advice is not imported as a universal rule; the existing time-based-follow guide covers frame-rate-independent adaptation. No tutorial media was inspected this pass and no duplicate source was promoted.

Totals: 1,292 catalog records, 127 resources, 104 patterns. No additional paid API spend.
