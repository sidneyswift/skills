# Evidence ownership and inspection limits

Use [source-catalog.jsonl](source-catalog.jsonl) for source identity, attribution and current retrieval/prompt status; [inspected sources](inspected-sources.md) for revision-specific code inspection; and a linked dated record for the precise observed states and limits. A pattern's local evidence paragraph must identify the source that supports that particular claim. An observation from one creator is not evidence for another creator's result.

## Current implementation and lookup ownership

- `patterns/*.md` owns mechanism instructions, build steps, tuning, checks and adapted prompts. `patterns.json` owns stable IDs, families and source membership; its repeated implementation fields are generated compatibility summaries. Search reads the current cards directly.
- Focused guides own substantial implementation detail. Compositions own relationships among mechanisms. Older browsing/workbook pages link to these owners rather than override them. Search derives guide and composition destinations from their Markdown; no second prose index is maintained.
- `source-catalog.jsonl` keeps original evidence notes and normalized prompt fields. `prompt_availability` is `content-inspected`, `lead-only`, or `not-established`. `content-inspected` means prompt text or images were read; it does **not** certify completeness. `lead-only` means a marker was found without established prompt-content inspection. A tutorial or code inspection alone is not prompt inspection.
- `prompt_format` records `text`, `image`, `linked-text`, or `unknown`; `prompt_completeness` records `not-certified` or `creator-claims-complete`. Keep detailed `prompt_signal` notes without using their free-form wording as program logic. New content must not inherit an inspected status merely from a creator's claim.

`search.py --kind sources --prompt-only` returns inspected prompt content. `--prompt-leads` also permits marker-only leads. Pattern prompts are original adaptations, so these filters apply only to sources.

For maintenance, run `python3 scripts/sync-index.py` after changing canonical cards/data, then `python3 scripts/sync-index.py --check` and `python3 scripts/test-library.py`. Preserve source IDs and scoped evidence relationships when updating cards. The checks establish local integrity and retrieval behavior, not visual quality or external URL availability.

## Historical first pass

Historical first-pass evidence. The full backlog retrieval and current counts are in [research coverage](research-coverage.md). Individual observations below remain scoped to what was inspected.


Snapshot: September 29, 2026. The broad index remains a discovery backlog. This pass retrieves actual creator text and converts a selected subset into [build patterns](build-patterns.md); it does not claim to have watched every linked video or found every relevant X post.

## Access and provenance

Apify retrieved all 24 selected direct posts. Five creator-thread searches returned 81 rows; the combined data deduplicates to 100 post IDs, including short replies. Those counts describe retrieval, not 100 useful design lessons. The initial general actor rejected direct-post URLs and produced zero results; the lightweight actor succeeded. Total recorded usage was $1.2612 (about $1.26).

The scraper's `text` field contained complete long-form bodies where `fullText` could be a legacy truncated preview. Evidence extraction used the complete returned body. Raw datasets and run receipts are saved separately in the research workspace, not copied into the skill. Creator prompts are summarized, not republished wholesale.

**Evidence levels:** retrieved text establishes what a creator wrote; source inspection establishes the inspected implementation; live inspection establishes only the interaction actually observed. A prompt's ambitious requested behavior is not proof of achieved output. Model names and workflow claims remain creator attributions.

## Direct posts retrieved

| Creator post | Returned body length | How it informs further work |
|---|---:|---|
| [@twoclipping](https://x.com/twoclipping/status/2103273003555402193) | 2,894 characters | Persistent morph, edge dynamics, seeking. |
| [@RyanSael](https://x.com/RyanSael/status/2102591147927654847) | 302 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@Aurelien_Gz](https://x.com/Aurelien_Gz/status/2102786378282987591) | 288 characters | Clearwater showcase; live page and source inspected. |
| [@dangreenheck](https://x.com/dangreenheck/status/2102878170089169235) | 1,153 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@rexan_wong](https://x.com/rexan_wong/status/2103707054108299437) | 2,739 characters | Reference/brand/storyboard workflow. |
| [@twoclipping](https://x.com/twoclipping/status/2103835273813496100) | 5,486 characters | Carry-over transitions, glass/masks, supplied media. |
| [@donaldjewkes](https://x.com/donaldjewkes/status/2102801274173587569) | 165 characters | Generated-media production workflow and continuity. |
| [@yumaeriel](https://x.com/yumaeriel/status/2103053166006657284) | 98 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@ImaStudio_ai](https://x.com/ImaStudio_ai/status/2104517586092458039) | 1,971 characters | Deformation/cutting specification; not a tested solver. |
| [@leodev](https://x.com/leodev/status/2102781872107659270) | 293 characters | Iteration and mixed production tools. |
| [@allforbigfire](https://x.com/allforbigfire/status/2104193522715029657) | 179 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@AGIOyaZ](https://x.com/AGIOyaZ/status/2103145567945986461) | 1,309 characters | Shared imagery and staged light reveal. |
| [@op7418](https://x.com/op7418/status/2103724883301814408) | 126 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@techhalla](https://x.com/techhalla/status/2103411244468498547) | 139 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@jurlycat](https://x.com/jurlycat/status/2102645793828036643) | 300 characters | Riso showcase; repository documents inspected. |
| [@poolio](https://x.com/poolio/status/2102445641205248145) | 58 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@yumaeriel](https://x.com/yumaeriel/status/2103053172235264150) | 17,664 characters | Painterly character prompt; separate motion and paint clocks. |
| [@himanshutwtxs](https://x.com/himanshutwtxs/status/2103495232637882858) | 264 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@theailoser](https://x.com/theailoser/status/2102565612874596411) | 2,507 characters | Fluid simulation specification; not a verified demo. |
| [@kevin_t_ngo](https://x.com/kevin_t_ngo/status/2102437977435893771) | 195 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@donaldjewkes](https://x.com/donaldjewkes/status/2102801469976248500) | 9,554 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@dangreenheck](https://x.com/dangreenheck/status/2102911556296052788) | 12,929 characters | Long iterative simulation correction chain. |
| [@leodev](https://x.com/leodev/status/2102897952587133299) | 1,755 characters | Retrieved context; inspect media/code before deriving visual claims. |
| [@kevin_t_ngo](https://x.com/kevin_t_ngo/status/2103482164193165711) | 106 characters | Retrieved context; inspect media/code before deriving visual claims. |

## Replies that change interpretation

- [TechHalla's full prompt](https://x.com/techhalla/status/2103411247618146715) exposes the type roles, timing, masks, and impact accents behind the brief.
- [Jurlycat's correction](https://x.com/jurlycat/status/2102809455826268361) says the piano samples are baked in, rather than synthesized. Do not describe the soundtrack as entirely procedural.
- [Op7418's process reply](https://x.com/op7418/status/2103867745666474220) describes two or three tuning rounds. Do not convert the chest showcase into a verified one-shot claim.
- [Kevin's implementation reply](https://x.com/kevin_t_ngo/status/2102452698369134984) names Canvas and Web Audio; it does not supply a complete prompt or prove that this stack is necessary for similar work.

## Inspected primary implementation material

- [Clearwater, pinned source](https://github.com/Aureliengmz/clearwater/blob/4bc826134321043a25df3c2b6fed16fb7b9241e8/index.html): read selected wave, refraction, lighting, input, and adaptive-resolution code. Opened [the live demo](https://aureliengmz.github.io/clearwater/) and observed tap-generated rings. No frame-rate benchmark or touch-device test.
- [Riso Windowseat motion notes](https://github.com/sevenevesai/riso-windowseat/blob/1275fdaf81eb1817b729ee69cbf7b6b6fe535a4e/docs/motion.md) and [live plates](https://github.com/sevenevesai/riso-windowseat/blob/1275fdaf81eb1817b729ee69cbf7b6b6fe535a4e/docs/live-plates.md): read continuity, ink-screening, and performance guidance. Did not render the whole film.
- [iart's animation skills](https://github.com/iart-ai/javascript-animation-skills/tree/deb46e0eff8dece768d6cde20b2eed6c22526e5f): inspected technique guidance as additional reference; no third-party code was vendored into the original study.

## What this skill adds

The build patterns and parameter suggestions are original synthesis. The motion kernel and Elastic Matter study are original implementation examples, not copied creator code or reproductions of their films. The broad catalog still contains index-only claims; consult these evidence notes and the patterns before treating an entry as a learned technique.
