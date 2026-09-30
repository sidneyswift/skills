# September30, 2026 — preserve trail continuity without stale history

Strengthened [particle-illustration](../patterns/worlds.md#particle-illustration), with no new pattern or source. [Original September24 post](https://x.com/ishuagra02/status/2102920408743678129) explicitly credits Opus5.5. [Skillry comparison](https://skillry.dev/ai-videos/opus-5-5/ishuagra02-678129) was played muted and sampled independently: ocean around10/11s, under-pier structure around20s, a daylight pier around33s and sunset wide views around47s. Both show luminous marks with different framing; no complete-film ranking, synchronization, sound or gameplay verification.

The gallery lacks a partial-prompt badge, yet its displayed text explicitly says additional prompts were used. The supplied text is a starting point. The 110 gallery badge count is unchanged; the completeness evidence is now more precise.

## Inspected code and original guidance

Reused archived [ribbons.js at revision92db822](https://github.com/ishuagrawal/particle-beach/blob/92db82255b962acf2930f19bf6e5e7790174a790/js/ribbons.js). Its active offscreen branch retains distance-triggered samples and trims them by lifetime/count while hiding geometry. Missing owners or near-zero fade clear history. This is code inspection, not executed edge-case validation; the existing repository MIT note remains applicable, and no implementation is bundled.

- Treat visibility, ownership and history as separate states. An active offscreen object may need continuity on return; a removed object should not leave history available for an unrelated replacement.
- Choose discontinuity policy explicitly. Clear on teleport/respawn/time jump, or start a separate trail segment when a visible break is intentional. A long connection is not evidence of rapid continuous travel.
- A minimum-distance insertion test suppresses redundant samples; it does not fill intermediate samples. If fast sparse updates make corners or wide gaps, resample the known path by distance. Do not interpolate across a true discontinuity.
- Test near/far views and camera re-entry, then compare lifecycle behavior under different update rates. Keep lifetime and sample-cap effects distinct: a cap can shorten the visible trail at high speeds.

The visual samples establish environmental appearance only. They do not prove ribbon continuity, correct resets, deterministic seeking or performance. New paid spend $0; catalog, resource and atlas counts unchanged.
