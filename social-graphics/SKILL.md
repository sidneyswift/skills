---
name: social-graphics
description: Generate on-brand social media graphics for any platform and format — feed posts, carousels, stories/reels covers, banners and headers, profile pictures, YouTube thumbnails, Pinterest pins, Open Graph link cards, and ad creative. Renders HTML to PNG via Playwright at correct platform dimensions with safe zones. Use when asked to create a social post, carousel, slide deck for social, story/reel, cover/banner, profile picture, thumbnail, pin, OG image, or to resize/adapt one design across multiple platforms and aspect ratios (1:1, 4:5, 9:16, 16:9, 1.91:1, 2:3, banners, pfps). Visual styles live as templates in references/; dimensions and safe zones live in references/dimensions.md.
---

# Social Graphics

Generate on-brand social media graphics from content, at the right dimensions for any platform and placement. HTML → Playwright screenshot → PNG.

Two independent choices drive every graphic:
- **Format** = the dimensions/aspect ratio (square, 4:5, story, banner, pfp, thumbnail, pin…). See `references/dimensions.md`.
- **Template** = the visual style (colors, type, layout). See `references/<template>.md`.

You can render the *same* template at *many* formats — that's how you create one design for every platform and size.

## Setup

**Step 0: Check configuration**

1. Read `~/.config/sid/identity.md` (or `~/.config/<owner>/identity.md`). This has the brand name, logo, handle, voice, and audience. If it doesn't exist, ask the user for their name, brand, handle, and audience — then create it. Shared across all skills.
2. Read `~/.config/social-slides/.env`. If it doesn't exist or lacks `SETUP_COMPLETE=true`, this is a first run:
   - Ask: "Which template should I default to?" (currently: `elegant-founder`)
   - Ask: "What platform/format are graphics primarily for?" (e.g. linkedin / x / instagram, feed / story / carousel)
   - Write answers to `~/.config/social-slides/.env` with `SETUP_COMPLETE=true`

If both exist and setup is complete, proceed to the workflow.

## Workflow

1. **Identify the format(s).** What is being made and for where? Look up the exact dimensions, aspect ratio, file specs, and safe zone in `references/dimensions.md`. If the user names a platform but not a placement, default to the highest-engagement feed format: **1080×1350 (4:5)**.
2. **Choose the template** (visual style). Use `DEFAULT_TEMPLATE` from `.env` or `elegant-founder`. Read `references/<template>.md` for full specs. User can override per request.
3. **Apply brand from identity.** Use the brand name, logo SVG, and handle for footers/close slides/profile marks.
4. **Compose for the format.** Match the layout to the canvas — a 4:5 feed post, a 9:16 story, a 4:1 banner, and a circular pfp are different compositions, not the same art stretched. Respect the safe zone for the format (see dimensions.md). For multi-slide carousels, one idea per slide.
5. **Generate HTML** sized to the target canvas. Set `body { width: Wpx; height: Hpx; }`. Replace `BRAND_NAME` with the brand from identity; use the identity logo SVG.
6. **Render to PNG** via Playwright at the matching viewport:

   ```bash
   npx playwright screenshot --viewport-size="WIDTH,HEIGHT" "file:///abs/path/graphic.html" "/abs/path/graphic.png"
   ```

7. **Review each render visually** against the safe zone and the template's quality checklist. If cluttered, split or simplify. If text is hard to read at phone scale, increase size/contrast.
8. **Iterate** until clean.

## Create once, adapt everywhere

To ship the same design across platforms and sizes:

- **Within the vertical/square family** (1:1, 4:5, 3:4, 9:16 — all 1080px wide), one HTML can serve all sizes if type and spacing use **width-relative units** (`vw`) instead of fixed `px`. Then only the canvas height changes between sizes and the composition holds. Re-render the same file at each viewport:

  ```bash
  HTML="file:///abs/path/graphic.html"
  for size in 1080,1080 1080,1350 1080,1920; do
    npx playwright screenshot --viewport-size="$size" "$HTML" "out/graphic-${size/,/x}.png"
  done
  ```

- **Landscape, banners, profile pictures, thumbnails** (16:9, 1.91:1, 3:1, 4:1, circle) have very different proportions — give them a **bespoke composition** rather than cramming the portrait layout in. Keep the same colors, type family, and logo so the set stays cohesive.
- **Keep critical content centered.** For 9:16, the *center-square method* (all key elements inside a centered 1080×1080) lets one asset survive Feed/Story/Reel crops. See dimensions.md.

## Available templates

| Template | Style | Best for | Reference |
|----------|-------|----------|-----------|
| `elegant-founder` | Light sky bg, Instrument Serif italic, black/white, editorial | Thought leadership, data breakdowns, industry analysis | [references/elegant-founder.md](references/elegant-founder.md) |

To add a template: create `references/<name>.md` with the same structure (visual identity, typography, layout rules, content-block types, HTML shell, quality checklist) and put assets in `assets/templates/<name>/`. Templates describe *style*; `dimensions.md` describes *size*. A good template notes how its type scale adapts across formats.

## Dimensions & safe zones

All platform sizes, aspect ratios, file specs, profile/banner safe zones, 9:16 story safe zones, and design best practices live in **[references/dimensions.md](references/dimensions.md)**. Read it whenever choosing or adapting a format. The six canvases that cover ~90% of placements: `1080×1080` (1:1), `1080×1350` (4:5), `1080×1920` (9:16), `1920×1080` (16:9), `1200×630` (1.91:1), `1000×1500` (2:3).

## Slide/format count guidelines

- **LinkedIn carousel:** 5–10 slides (5 min for narrative, 8–10 for deep dives). Export to PDF for upload.
- **Instagram carousel:** 5–7 slides; up to 20 supported. Square or 4:5; first slide sets the ratio.
- **X thread companion:** 3–5 punchy slides.
- **Single graphics** (hero post, quote card, announcement): one strong composition beats a thin carousel.

## Content principles

- Every graphic/slide earns its place — if it adds no new idea, cut it.
- Lead with data over opinion when numbers are available; the number is the design.
- The hook (slide 1 / the headline) decides whether anyone engages — spend disproportionate effort there.
- Supporting text is noticeably quieter than headlines (smaller, lighter).
- Whitespace is a feature: ≥40% of a feed graphic should be empty.
- Mobile-first: if it doesn't read at phone-thumbnail scale, it fails.

## Output

Save PNGs to the output directory (e.g. `slide-0.png … slide-N.png`, or `graphic-1080x1350.png` for single/multi-size). Keep HTML source alongside for iteration.
