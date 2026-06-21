# Template: Elegant Founder

Editorial-style carousel slides for thought leadership, data breakdowns, and industry analysis. Designed for LinkedIn and adaptable to X/Instagram.

**Configurable values:** The HTML template shell below uses `BRAND_NAME` as a placeholder. Replace it with the brand name from `context.md`. If no context.md exists, omit the brand name text (keep the logo if one is provided, or remove the footer brand section entirely). Similarly, the logo SVG below is a default — replace it with the logo from `context.md` if specified.

## Visual Identity

- **Background:** Light sky gradient — `linear-gradient(175deg, #e4edf6 0%, #edf2f8 20%, #f5f7fa 45%, #fafbfc 70%, #ffffff 100%)`
- **Optional cloud texture overlay:** Two subtle radial gradients for organic depth
- **Text color:** `#0a0a0a` (near-black) for headlines, `#888888` for supporting text, `#aaaaaa` for labels/metadata
- **No colored accents.** Contrast comes from typography scale, not color.

## Typography

| Role | Font | Weight | Usage |
|------|------|--------|-------|
| Headlines (H1/H2) | Instrument Serif italic | 400 | Hook slides, insight slides, closers |
| Data numbers | Instrument Serif regular | 400 | Giant stat displays ($1.44B, +51%) |
| Labels | Plus Jakarta Sans | 600 | Uppercase category labels above data |
| Body/supporting | Plus Jakarta Sans | 500 | Context lines, subtitles |

Load via Google Fonts:
```
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
```

## Dimensions & formats

This template works at any canvas. For the full size/aspect-ratio/safe-zone reference, see [dimensions.md](dimensions.md). Common targets:

| Use | Size | Ratio |
|-----|------|-------|
| LinkedIn / feed (default) | 1080 × 1350 | 4:5 |
| Square / carousel | 1080 × 1080 | 1:1 |
| Story / reel cover | 1080 × 1920 | 9:16 |
| Link / OG card | 1200 × 630 | 1.91:1 |

**Default: 1080×1350 (4:5).**

**Adapting the type scale across formats.** The pixel sizes below are tuned for the 1080-wide canvas, so they hold across the vertical/square family (1:1, 4:5, 3:4, 9:16) unchanged. When the canvas width changes, scale type proportionally: `size = base × (canvas_width / 1080)`. For wide formats (16:9, banners, OG cards) the height is the constraint — anchor type to height instead and shorten copy. Keep the 80px margin as `~7.4%` of canvas width so it scales too.

## Layout Rules

- **Margins:** 80px left/right, content never touches edges
- **Safe zones:** for 9:16 (stories/reels), keep headlines, footer, and the page count inside the center band — clear the top ~250px and bottom ~340px (UI overlays). For banners/headers, keep content centered. See [dimensions.md](dimensions.md).
- **Content position:** Upper third to center. Do NOT center vertically — editorial layouts anchor content high with generous space below
- **Alignment:** Left-aligned throughout. Exception: the final/CTA slide may center for a deliberate shift
- **Footer:** Logo mark + brand name (17px, 600 weight) left, page count right. Positioned at bottom: 52px. Always present. Use the brand name from `context.md` if available, otherwise use no brand name (logo only).
- **One idea per slide.** If a slide has more than one concept, split it.

## Logo

The logo SVG path (from `assets/templates/elegant-founder/logo-dark.svg`) with viewBox `48 41 127 141`.

For light backgrounds, set `fill="#0a0a0a"`.
For dark backgrounds, set `fill="white"`.

Inline SVG at 26×29px in the footer:
```html
<svg width="26" height="29" viewBox="48 41 127 141" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#0a0a0a"/>
</svg>
```

## Slide Types

### Hook
Big Instrument Serif italic headline. One sentence, broken across 2–3 lines. Optional muted subtitle below.
- Headline: 82–86px, line-height 1.06, letter-spacing -2px
- Subtitle: 24px Plus Jakarta Sans 500, color `#888888`, margin-top 44px
- Position: top ~280px from top edge

### Data
Small uppercase label → giant number → short context. The number IS the design.
- Label: 16px Plus Jakarta Sans 600, color `#aaaaaa`, letter-spacing 0.1em, uppercase
- Number: 140–172px Instrument Serif 400, line-height 0.9, letter-spacing -5px
- Context: 24px Plus Jakarta Sans 500, two lines max. First line `#888888`, second line `#aaaaaa`
- Position: top ~320px from top edge

### Insight
Instrument Serif italic statement + supporting context. For the "so what" moment.
- Headline: 58–64px italic, line-height 1.12
- Body: 24px Plus Jakarta Sans 500, color `#888888`, max-width 700px, margin-top 44px
- Position: top ~260px from top edge

### Close
Centered Instrument Serif italic statement. The takeaway. Handle below.
- Headline: 56–64px italic, centered, max-width 800px
- Handle: 19px Plus Jakarta Sans 600, color `#aaaaaa`, margin-top 48px
- Position: true vertical center (translateY -50%)

## HTML Template Shell

```html
<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1350px;
    position: relative; overflow: hidden;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    background: linear-gradient(175deg, #e4edf6 0%, #edf2f8 20%, #f5f7fa 45%, #fafbfc 70%, #ffffff 100%);
  }
  body::before {
    content: '';
    position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 100% 70% at 65% 10%, rgba(195, 215, 235, 0.25) 0%, transparent 55%),
      radial-gradient(ellipse 70% 50% at 15% 60%, rgba(200, 218, 235, 0.1) 0%, transparent 45%);
    pointer-events: none;
  }
</style>
</head>
<body>
  <!-- SLIDE CONTENT HERE -->

  <!-- FOOTER (every slide) -->
  <div style="position:absolute; bottom:52px; left:80px; right:80px; display:flex; justify-content:space-between; align-items:center;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="26" height="29" viewBox="48 41 127 141" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M118.106 41C112.845 41 108.581 45.2558 108.581 50.5056V88.3242C108.581 93.9241 106.846 99.3868 103.613 103.964C98.5169 111.179 90.2239 115.471 81.3785 115.471H57.525C52.2645 115.471 48 119.727 48 124.977V172.304C48 177.554 52.2645 181.81 57.525 181.81H104.894C110.155 181.81 114.419 177.554 114.419 172.304V139.968C114.419 133.432 116.445 127.056 120.218 121.714L120.885 120.77C126.833 112.348 136.512 107.339 146.836 107.339H165.475C170.736 107.339 175 103.083 175 97.833V50.5056C175 45.2558 170.736 41 165.475 41H118.106Z" fill="#0a0a0a"/></svg>
      <span style="font-size:17px; font-weight:600; color:#0a0a0a; letter-spacing:-0.02em;">BRAND_NAME</span>
    </div>
    <span style="font-size:15px; font-weight:500; color:#aaaaaa; letter-spacing:0.04em;">N / T</span>
  </div>
</body></html>
```

Replace `N / T` with slide number / total.

## Rendering

Generate HTML per slide, then screenshot with Playwright at the target canvas:
```bash
npx playwright screenshot --viewport-size="1080,1350" "file:///path/to/slide.html" "/path/to/slide.png"
```

To output the same design at several sizes, change `body` width/height (and scale type per the rule above) or re-render a width-relative layout at each viewport. See the "Create once, adapt everywhere" section in SKILL.md.

## Quality Checklist

Before finalizing slides, verify:
- [ ] Every slide conveys exactly one idea
- [ ] Headlines use Instrument Serif italic (not regular, not sans-serif)
- [ ] Data numbers are the largest element on their slide
- [ ] Supporting text is noticeably smaller and lighter than headlines
- [ ] Left margin is consistent (80px) across all slides
- [ ] Footer logo + page number present on every slide
- [ ] No decorative elements that don't serve the content (accent lines, ghost numbers, colored dots)
- [ ] Generous white space — at least 40% of the slide is empty
- [ ] Text never runs wider than ~920px (80px margins) on a 1080-wide canvas
- [ ] Content respects the format's safe zone (no headline/footer under platform UI on 9:16)
- [ ] Renders cleanly at the target canvas size and reads at phone-thumbnail scale
