# September30 — catch an exact simulation event

Added [simulation event stops](../simulation-event-stops.md), routed from interactive/3D and inspected-source references. The distinct mechanism is detecting a short-lived event inside batched simulation steps and holding its exact state for inspection, while keeping targeted jumps as a separate operation.

**Source:** [Edwin Hayward's post](https://x.com/edwinhayward/status/2105022417005334692), September29 19:50:28UTC, explicitly names Opus5.5 and links the [gallery](https://www.experimentswithai.com/ants-on-a-grid.html). The full retrieved body includes a model-style research narrative, a correction to an earlier truncated-output reading, and the creator's link to the finished tool. Attribution is creator-reported; survey results, theorems, numerical claims and C/JavaScript agreement were not independently reproduced.

**Inspected implementation:** selected inline `isPaired`, `createEngine`, reset/run/predicate, jump/load, readout, frame-loop and control-handler sections. The engine updates a mismatch count for a fixed reflection after each cell change, detects nonempty symmetric states inside each simulation step and returns early when event-stop is enabled. The frame loop uses bounded chunks and an elapsed-time check. Skip mode bypasses the event stop, computes toward the target, and then resumes ordinary playback. Earlier target requests reset/replay rather than assigning the step label. A fixed finite map stops on boundary exit. No whole-program correctness or sustained performance claim follows from these reads.

**Live observations:** LLRR with mirror-stop enabled paused at3,928; Play paused again at3,932, with the event count increasing from218 to219. A pink mirror line and corresponding colored pattern were visible. The LLRL250,000 preset advanced and resumed, first observed at251,710; pausing later at304,234 showed a long narrow ribbon extending from the dense pattern. Reset returned step and colored-cell counts to zero. Two screenshots are archived. No arbitrary-rule survey, huge-step benchmark, mobile/keyboard audit or full boundary test was performed.

HTML was archived on September30 with SHA256 `7b553a19ff71e96a26e874c479dac6b6dda777c4f5ab2e48aab106cfeda25514`. No explicit reuse license was observed in the inspected page; third-party implementation stays in the research archive and is not bundled. New build guidance and prompt are original synthesis. This is an inline-code study, so the repository-investigation count remains27.

Research: the last69 novel previews were screened, completing419 of419 for Apify run `NKYsGJgC6rHZCYe4l`. The search hit its result cap and remains non-exhaustive. Selected resource/media leads are retained for future inspection rather than marked visually verified. No new paid retrieval; the reused run's previously reported actual cost is$0.64.

Totals:1,303 catalog records,137 resources,104 patterns,27 repository investigations.
