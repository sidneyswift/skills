---
name: social-slides
description: Generate carousel/slide images for social media (LinkedIn, X, Instagram). Produces HTML slides and renders them to PNG via Playwright. Use when asked to create carousel posts, slide decks for social, LinkedIn carousels, swipe posts, or social slide content. Supports multiple visual templates — currently includes "elegant-founder" for editorial thought leadership. Each template lives in references/ with full design specs.
---

# Social Slides

Generate social media carousel/slide images from content. HTML → Playwright screenshot → PNG.

**Personal context:** If `{baseDir}/context.md` exists, read it first. It contains brand-specific overrides (footer name, logo, handle, default template, audience context) that should be applied throughout the workflow.

## Workflow

1. **Check for context** — Read `{baseDir}/context.md` if it exists for brand/template overrides.
2. **Choose template** — Match the content type to a template. Use the default from context.md, or fall back to `elegant-founder`.
3. **Read the template reference** — Load `references/<template-name>.md` for full design specs (colors, typography, layout, slide types).
4. **Structure the content into slides** — One idea per slide. Typical flow:
   - Slide 1: Hook (bold statement or question)
   - Slides 2–3: Evidence (data, stats, quotes)
   - Slide 4: Insight (the "so what")
   - Slide 5: Close (takeaway + handle)
5. **Generate HTML** per slide using the template's shell and slide type specs. Apply any brand overrides from context.md (footer name, logo, handle).
6. **Render to PNG** via Playwright: `npx playwright screenshot --viewport-size="WIDTH,HEIGHT" "file:///path/to/slide.html" "/path/to/slide.png"`
7. **Review each rendered slide** visually. Check against the template's quality checklist.
8. **Iterate** — If a slide feels cluttered, split it. If text is hard to read, increase contrast or reduce content.

## Available Templates

| Template | Style | Best For | Reference |
|----------|-------|----------|-----------|
| `elegant-founder` | Light sky bg, Instrument Serif italic, black/white, editorial | Thought leadership, data breakdowns, industry analysis | [references/elegant-founder.md](references/elegant-founder.md) |

To add a new template: create `references/<template-name>.md` with the same structure (visual identity, typography, layout rules, slide types, HTML shell, quality checklist). Add assets to `assets/templates/<template-name>/`.

## Slide Count Guidelines

- **LinkedIn carousel:** 5–10 slides. 5 is the minimum for meaningful narrative. 8–10 for deep dives.
- **X thread companion:** 3–5 slides. Punchier, less context needed since the thread carries the text.
- **Instagram:** 5–7 slides. Similar to LinkedIn but consider 1080×1080 square format.

## Content Principles

- Every slide earns its place. If it doesn't add a new idea, cut it.
- Data is more compelling than opinions. Lead with numbers when available.
- The hook slide determines whether anyone swipes. Spend disproportionate effort on it.
- Supporting text should be noticeably quieter than headlines — smaller size, lighter color.
- White space is a feature. At least 40% of each slide should be empty.

## Output

Slides are saved as `slide-0.png` through `slide-N.png` in the output directory. HTML source files are saved alongside for iteration.
