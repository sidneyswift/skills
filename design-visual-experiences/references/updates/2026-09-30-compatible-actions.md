# September 30 — compatible spatial actions

Extended [interactive 3D guidance](../interactive-3d.md#preserve-compatible-actions-inside-a-spatial-scene) with original implementation steps, parameters, an adapted prompt and combination checks for posture, props and expressive motion.

**Attribution:** [Louise de Sadeleer's original post](https://x.com/LouiseDSadeleer/status/2102679047918555146), September 23 08:38:45 UTC, explicitly names GPT-6 Astra. The full [linked tutorial](https://louisedesadeleer.substack.com/p/i-turned-my-apartment-into-a-video) was read. It specifies retaining couch position while taking a toy and retaining a toy during petting. These are creator requirements, not proof of every resulting behavior.

**Code inspected:** public template revision `355d0edc1886b44a5cf08c5ee311252e7f22f5d5`; full affection module, selected seating geometry, support, jump validation and gesture-strength sections. The probe uses articulated geometry and attached toy bounds, expands prop bounds for sway, checks clearance and support separately, samples transitions and tries decreasing gesture strengths. Source files and hashes are archived. No source was executed locally and no full test suite was run. Sampled pose checks do not establish continuous collision safety.

**Live observations:** in [the apartment](https://loulous-apartment.vercel.app/), a rope selection produced an insufficient-room message. Jumping onto the couch temporarily disabled toy/arrangement controls; after landing, the action changed to Jump down. Selecting Ball then produced a checked Ball control and a possession message; a screenshot shows the character on the couch with the blue ball. The earlier failure message remained visible alongside this success. Petting with a held toy, prop replacement, keyboard/mobile, reduced motion, performance and the full collision suite were not tested. Music was paused; audio was not evaluated. No deployed-template hash match was established.

**Rights:** inspected MIT code license and asset notices. The code license excludes third-party artwork, product labels, covers, trademarks and music; the template's generated geometry and original animation have separate starter-use permission. No source code, assets or full creator prompts are bundled in the skill.

**Novelty:** preserve compatible state across actions; size collision/support checks for animated poses and attachments; reduce optional expression amplitude before disrupting location or possession; test feedback recovery after rejection. These extend existing state guidance without inflating atlas pattern counts.

Totals: 1,299 catalog records, 135 resources, 104 patterns, 26 repository investigations. New paid API spend: $0. All remaining 76 archived candidate previews were screened in this pass; preview screening is not full-post or visual verification.
