# September 30 — keep information readable through an exposure

Strengthened [selective motion blur](../patterns/production.md#selective-motion-blur) and [transition QA](../transition-qa.md#a-forward-shutter-still-needs-cut-alignment). New guidance separates freezing a changing value from preserving sharp geometry, and tests cut alignment after retiming. No new pattern or copied implementation.

**Attribution:** [wzarok's September 29 post](https://x.com/wzarok/status/2105022439289921947), 19:50:33 UTC, explicitly says the showcase used ft-motion with Claude Code Opus 5.5. The [creator reply](https://x.com/wzarok/status/2105022442725159139), one second later, links [the repository](https://github.com/imserhatdemir/ft-motion). This attributes the film, not necessarily authorship of every repository file.

**Inspected:** revision `6abcf2e648bc8a7578d8d6bc32b346b846bec9bb`; MIT license (Serhat Demir), README and technique documentation, selected runtime `engine/core.js` lines 265–312. The runtime samples scene time forward within a configurable shutter, exposes one frame time, averages canvas samples and invokes a final post pass. Documentation explains counters and labels using the fixed time or final pass. Selected code was read, not executed; deterministic behavior, linear-light correctness and performance were not validated. No film or audio was inspected, so visual quality remains unverified.

**Independent probe:** exact rational arithmetic recreated only the sample schedule at 60 fps, six samples and half-frame shutter. At speed 1, a cut at 1 second stayed separate across frames 59 and 60. At speed 1.01 with a cut at 0.997 seconds, frame 59 straddled the cut with three samples in each shot. This demonstrates an alignment condition, not a source-runtime test. Original guidance adds retiming and information-layer checks without treating source defaults as universal.

**Research receipt:** Apify run `i1IGCqNdS7La8BkSN` succeeded with five rows, actual cost $0.002. Both creator conversation bodies were read. The fire/smoke creator's [reply](https://x.com/Machinedelusion/status/2105122474031808960) says packaging is forthcoming; no public code/demo link was supplied in these results, so it remains pending and is not promoted. No unchanged thread refetch is planned without a new availability signal.

Third-party implementation and full prompts are not bundled. Repository MIT terms do not establish rights to all dependencies or media. Totals: 1,305 catalog records, 138 resources, 104 patterns, 28 repository investigations.
