# September 29, 2026 — an experiment that survives view changes

Added [worked guidance](../interactive-3d.md#build-an-experiment-with-several-explanatory-views) for shared experiment state, view-specific explanations, stable response plots, illustrative layers and reset checks. These are original engineering recommendations informed by observed behavior, not claims about the site's source architecture.

[Creator post](https://x.com/kobez_01/status/2104951103896838350): September 29, 15:07:05 UTC; explicitly credits GPT-6 Astra. Voice/music is separately credited to ElevenLabs. [Live demo](https://wind-tunnel.kobez.dev/) was exercised in a desktop browser:

| Action / state | Observed response |
|---|---|
| Initial 90 KTAS, 6° angle, flaps retracted | Aircraft, airflow and force vectors; lift 16.4 kN, drag 1.1 kN, coefficient 0.77 |
| Set 18° and select Section | Section view retains 18°; coefficient 1.10 and “Past the stall peak”; lift 23.4 kN, drag 3.3 kN |
| Enable pressure and propwash | Colored wing and additional illustrative flow; propwash switches from Section to Aircraft. Inputs and response readings remain unchanged |
| Disable those layers and set 15° | Coefficient 1.54, lift 32.7 kN and drag 3.4 kN; these are app readings, not validated measurements |
| Switch to Wing, then Pause | Wing view retains inputs/readings; Pause label becomes Resume. Actual cessation of every animation was not established |
| Reset | Aircraft and default 6° state restored; coefficient 0.77, lift 16.4 kN, drag 1.1 kN, pressure/propwash off, button returns to Pause. Response plot and current marker visible |

The UI calls propwash illustrative and says readings are unchanged. No aerodynamic model, pressure field, aircraft asset provenance, audio, mobile behavior or performance was validated. No creator code was retrieved, and no external assets are bundled.

Reused archived post retrieval. New paid spend $0. Catalog now 1,282 records and resources 120; atlas remains 104 patterns with 128 supporting posts. Skillry counts unchanged.
