# Reference: Dimensions, Aspect Ratios & Safe Zones

The complete sizing reference for social graphics across every major platform and format. Use this to render the same design at the correct dimensions for any placement — feed posts, stories, banners, profile pictures, thumbnails, pins, link previews, and more.

**Specs drift.** Platforms change layouts without notice. These are verified against 2026 platform docs and the major guides (Sprout Social, Hootsuite, Buffer, Metricool). For mission-critical brand assets (logos, ad creative), spot-check the platform's current help center before publishing.

---

## Start here: the 6 canvases that cover ~90% of everything

If you build at these six sizes, you can serve almost any placement. All are 1080px wide except where noted.

| # | Canvas | Ratio | Covers |
|---|--------|-------|--------|
| 1 | **1080 × 1080** | 1:1 | Square feed posts, carousels, profile-adjacent, FB/IG/LinkedIn/X square, YouTube community |
| 2 | **1080 × 1350** | 4:5 | Portrait feed posts — the **highest-engagement** feed format on IG, FB, LinkedIn, Threads |
| 3 | **1080 × 1920** | 9:16 | Stories, Reels, Shorts, TikTok, Snapchat, Pinterest Idea Pins, Spotify Canvas |
| 4 | **1920 × 1080** (or 1600×900) | 16:9 | Landscape video, YouTube thumbnails, X single image, presentation-style |
| 5 | **1200 × 630** | 1.91:1 | Link previews / Open Graph cards (FB, LinkedIn, Slack, Discord), blog featured |
| 6 | **1000 × 1500** | 2:3 | Pinterest standard pin |

**The single most versatile size:** `1080 × 1350` (4:5 portrait). It outperforms square in every feed and downscales cleanly.

---

## Aspect ratio primer

**Aspect ratio ≠ resolution.** Ratio is the *shape* (4:5). Resolution is the *pixel count* (1080×1350). Two images can share a ratio (4:5) at different resolutions (1080×1350 vs 1440×1800). Match the **ratio** so nothing crops; push the **resolution** up for retina/ads.

| Ratio | Shape | Primary uses |
|-------|-------|--------------|
| 1:1 | Square | Universal feed, carousels, profile pics, album/podcast art |
| 4:5 | Tall portrait | Best-performing feed post (IG/FB/LinkedIn/Threads) |
| 3:4 | Portrait | IG grid thumbnails (forced), newer IG feed option |
| 9:16 | Full vertical | All stories/reels/shorts/TikTok/Snapchat |
| 2:3 | Tall | Pinterest pins |
| 16:9 | Landscape | Video, thumbnails, presentations, article covers |
| 1.91:1 | Wide | Link/OG cards, landscape feed |
| 3:1 | Wide strip | X / Bluesky / Mastodon headers |
| 4:1 | Wide strip | LinkedIn personal banner |
| 5:1–6:1 | Ultra-wide strip | LinkedIn company cover, Reddit banner |

**Rule of thumb:** taller wins in feeds (more screen real estate → longer dwell → more reach). Wider is for banners, video, and link cards.

---

## Universal rules (apply everywhere)

1. **1080px is the universal width.** Build feed/story assets at 1080px wide. Exceptions: YouTube banner (2560px), Pinterest (1000px), podcast/album art (3000px).
2. **Design at the largest size, then scale down.** Downscaling stays sharp; upscaling adds blur. For ads, start at 1440px+ wide (platforms re-compress on delivery).
3. **Portrait (4:5) beats square (1:1)** on every feed-based platform. Square beats landscape. Landscape (1.91:1) is deprioritized organically — reserve it for link previews.
4. **9:16 for all vertical video/stories.** Create once, distribute to Reels + Shorts + TikTok + Snapchat.
5. **File format:** JPG for photos, PNG for graphics/text/transparency, WebP for modern web (smallest). Video = MP4 (H.264). Most platforms convert uploaded PNGs → JPG (transparency lost) except Discord/Reddit profile pics.
6. **Color space:** export sRGB / RGB. CMYK uploads shift color badly.
7. **Respect safe zones** on stories, banners, and anything with a circular crop (see safe-zone sections below). This is the #1 most common mistake.

---

## Per-platform specs

Dimensions are **recommended upload size**. "Display" = how the platform shows it. Profile pics are cropped to a **circle** on nearly every platform — keep the subject centered.

### Instagram

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 320 × 320 (min 110×110) | 1:1 | Circle crop |
| Feed — square | 1080 × 1080 | 1:1 | |
| Feed — portrait | 1080 × 1350 | 4:5 | **Best engagement** |
| Feed — landscape | 1080 × 566 | 1.91:1 | |
| Feed — tall (newer) | 1080 × 1440 | 3:4 | Matches grid crop |
| Carousel | 1080 × 1080 or 1080 × 1350 | 1:1 / 4:5 | Up to **20 slides**; first slide sets ratio for all |
| Stories | 1080 × 1920 | 9:16 | Safe area 1080×1610 |
| Reels (video) | 1080 × 1920 | 9:16 | Cover/grid crops to 3:4 (1080×1440) |
| Reel cover (grid) | 1080 × 1440 | 3:4 | Can't be edited after publish |
| Ad — feed | 1440 × 1800 (4:5) / 1440×1440 (1:1) | 4:5 / 1:1 | Upload hi-res |
| Ad — story | 1440 × 2560 | 9:16 | |

File: ≤30 MB image. Grid thumbnails now display at **3:4** — keep key visuals centered.

### Facebook

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 320 × 320 (use up to 2048²) | 1:1 | Displays 170/176 desktop, 196 mobile; circle |
| Cover photo | 851 × 315 | ~2.7:1 | Displays 820×312 desktop, 640×360 mobile — keep content centered |
| Feed post | 1080 × 1350 (4:5) | 4:5 | Also 1:1 / 1.91:1 |
| Link share | 1200 × 630 | 1.91:1 | Pulled from `og:image` |
| Stories / Reels | 1080 × 1920 | 9:16 | All FB video is now Reels |
| Event cover | 1920 × 1005 | 1.91:1 | |
| Group cover | 1640 × 856 | 1.91:1 | |
| Ad — feed | 1080 × 1080 / 1080 × 1350 | 1:1 / 4:5 | |

File: ≤30 MB. Profile pic overlaps the **lower-left** of the cover.

### LinkedIn

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 400 × 400 (min 268²) | 1:1 | Circle; ≤3 MB |
| Personal banner | 1584 × 396 | 4:1 | Keep text out of lower-left (pfp overlap) |
| Company logo | 400 × 400 (min 268²) | 1:1 | |
| Company cover | 1128 × 191 | ~5.9:1 | Very wide/short — bold graphics, not fine text |
| Feed — portrait | 1080 × 1350 | 4:5 | Best engagement |
| Feed — square | 1080 × 1080 | 1:1 | |
| Feed — landscape / link | 1200 × 627 | 1.91:1 | |
| Carousel (document) | 1080 × 1080 or 1080 × 1350 per page | 1:1 / 4:5 | Uploaded as **PDF**; cover + CTA slide recommended |
| Article cover | 1920 × 1080 | 16:9 | |
| Life tab hero | 1128 × 376 | 3:1 | Mobile app only |

File: ≤10 MB image. LinkedIn carousels = a multi-page PDF; export your slides to PDF.

### X (Twitter)

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 400 × 400 | 1:1 | Circle |
| Header | 1500 × 500 | 3:1 | Left side overlapped by pfp on mobile |
| Single image — landscape | 1600 × 900 | 16:9 | Largest timeline preview |
| Single image — portrait | 1080 × 1350 | 4:5 | Well-supported |
| Single image — square | 1080 × 1080 | 1:1 | |
| Link / summary card | 1200 × 628 | 1.91:1 | Use `twitter:image`; 1200×600 (2:1) avoids edge crop |

File: ≤5 MB image, ≤15 MB GIF. Multi-image posts crop to a grid — center content.

### TikTok

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 200 × 200 (use 400²) | 1:1 | Circle |
| Video | 1080 × 1920 | 9:16 | Center 65% is the safe zone |
| Photo Mode (carousel) | 1080 × 1920 or 1080 × 1350 | 9:16 / 4:5 | 4–35 images |

Right sidebar (~120px) + bottom caption area overlap content — keep text centered.

### YouTube

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 800 × 800 | 1:1 | Circle; ≤4 MB |
| **Channel banner** | 2560 × 1440 | 16:9 | **Safe area 1546 × 423** (see below) |
| Thumbnail | 1280 × 720 | 16:9 | ≤2 MB; single most important CTR asset |
| Video | 1920 × 1080 | 16:9 | 4:3 gets pillarboxed |
| Shorts | 1080 × 1920 | 9:16 | Bottom ~340px reserved for title |
| Community post | 1080 × 1080 | 1:1 | |

**Banner safe area:** the full 2560×1440 is only seen on TVs. Put logo/text/handles inside the centered **1546 × 423** so they survive phone, tablet, desktop, and TV crops.

### Pinterest

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 165 × 165 (use 400²) | 1:1 | Circle |
| Business cover | 800 × 450 | 16:9 | |
| **Standard pin** | 1000 × 1500 | 2:3 | **Required ratio** — deviating truncates the pin |
| Square pin | 1000 × 1000 | 1:1 | Less feed presence |
| Long pin (max) | 1000 × 2100 | ~1:2.1 | |
| Idea Pin / video | 1080 × 1920 | 9:16 | |

File: ≤20 MB. Title ≤100 chars, description ≤250.

### Threads

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 320 × 320 | 1:1 | Synced from Instagram; circle |
| Post — portrait | 1080 × 1350 | 4:5 | Best impact |
| Post — square / landscape | 1080 × 1080 / 1080 × 566 | 1:1 / 1.91:1 | Max width 1440px |
| Video | 1080 × 1920 | 9:16 | |

### Snapchat

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 320 × 320 | 1:1 | Circle |
| Snap / Story / Spotlight | 1080 × 1920 | 9:16 | Safe area center 1080×1420 |
| Filter / Lens overlay | 1080 × 2340 | 9:19.5 | Transparent PNG |

Keep critical content ~400px from the bottom (Send/Chat UI).

### Bluesky

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Avatar | 400 × 400 | 1:1 | Circle |
| Banner | 1500 × 500 | 3:1 | |
| Post image | 1200 × 675 | 16:9 | |

### Mastodon

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Avatar | 400 × 400 | 1:1 | Rounded square |
| Header | 1500 × 500 | 3:1 | Supports WebP/AVIF for better compression |

### Discord

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Avatar | 128 × 128 (use 512²) | 1:1 | Circle; ≤8 MB; PNG keeps transparency |
| Profile banner | 600 × 240 | 5:2 | Nitro |
| Server icon | 512 × 512 | 1:1 | |
| Server banner | 960 × 540 | 16:9 | Boosted server |
| Invite splash | 1920 × 1080 | 16:9 | Level 3 boost |
| Custom emoji | 128 × 128 | 1:1 | ≤256 KB |

### Reddit

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Avatar / community icon | 256 × 256 | 1:1 | Circle |
| Profile / subreddit banner | 1920 × 384 | 5:1 | Edges cropped — center everything |
| Mobile banner | 1600 × 480 | 10:3 | |

PNG transparency preserved for avatars.

### WhatsApp / Telegram

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| WhatsApp profile | 640 × 640 | 1:1 | Circle |
| WhatsApp status | 1080 × 1920 | 9:16 | |
| Telegram profile | 512 × 512 | 1:1 | Circle |

### Twitch

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Profile photo | 256 × 256 | 1:1 | Circle |
| Channel banner | 1200 × 480 | 5:2 | ~100px margin top/bottom |
| Offline banner | 1920 × 1080 | 16:9 | Edge-to-edge OK (fills player) |
| Panel image | 320 × wide | — | 320px wide, height flexible |

### Spotify & podcasts

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| **Podcast cover** | 3000 × 3000 | 1:1 | Min 1400²; **≤512 KB** (Apple) → export JPG 80–90% |
| Album cover | 3000 × 3000 | 1:1 | |
| Playlist cover | 640 × 640 (min 300²) | 1:1 | |
| Artist profile | 750 × 750 | 1:1 | Circle |
| Artist header | 2660 × 1140 | ~7:3 | |
| Spotify Canvas | 1080 × 1920 | 9:16 | 3–8s looping MP4 |

Podcast cover is viewed as small as 40px — use bold type and high contrast.

### Web / Open Graph / Email

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| Open Graph (universal) | 1200 × 630 | 1.91:1 | FB, LinkedIn, WhatsApp, Slack, Discord; keep content in central 80% |
| OG for X | 1200 × 600 | 2:1 | Avoids edge crop |
| Blog featured | 1200 × 630 | 1.91:1 | Doubles as OG image |
| Email header | 600 × 200 | 3:1 | 600px = email standard; ≤200 KB |
| Favicon | 512 × 512 (also 32, 180) | 1:1 | Export multiple sizes |

### E-commerce (quick)

| Placement | Size (px) | Ratio |
|-----------|-----------|-------|
| Shopify product | 2048 × 2048 | 1:1 |
| Shopify hero | 1920 × 1080 | 16:9 |
| Etsy listing | 2000 × 2000 | 1:1 |
| Etsy shop banner | 3360 × 840 | 4:1 |
| Google Business | 720 × 720 (min 250²) | 1:1 |

---

## Profile pictures: upload vs. display (cross-platform)

Almost all are **circle-cropped**. Upload square, center the subject, leave breathing room at the edges, and never put text near the corners.

| Platform | Upload | Shape |
|----------|--------|-------|
| Instagram / Threads / Snapchat | 320 × 320 | Circle |
| Facebook | 320 × 320 (up to 2048²) | Circle |
| X / LinkedIn / Bluesky | 400 × 400 | Circle |
| YouTube | 800 × 800 | Circle |
| TikTok | 200–400 | Circle |
| Pinterest | 165–400 | Circle |
| Discord | 128–512 | Circle |
| Reddit / Twitch | 256 × 256 | Circle |
| WhatsApp | 640 × 640 | Circle |
| Telegram | 512 × 512 | Circle |
| Spotify artist | 750 × 750 | Circle |

---

## Banner / cover safe zones (cross-platform)

Banners get cropped differently on desktop vs. mobile, and profile pics overlap them. Keep logos and text **centered** and treat edges as bleed.

| Platform | Upload | Safe / watch-out |
|----------|--------|------------------|
| YouTube | 2560 × 1440 | Center **1546 × 423** only |
| Facebook | 851 × 315 | Mobile crops to 640×360; pfp covers lower-left |
| X | 1500 × 500 | Center; bottom-left under pfp on mobile |
| LinkedIn personal | 1584 × 396 | Keep text right-of-center; lower-left under pfp |
| LinkedIn company | 1128 × 191 | Ultra-wide — bold shapes only |
| Reddit | 1920 × 384 | Left/right cropped per screen width |
| Bluesky / Mastodon | 1500 × 500 | Center |
| Twitch | 1200 × 480 | ~100px top/bottom margin |

---

## 9:16 vertical safe zones (Stories / Reels / Shorts / TikTok / Snapchat)

This is where most designs fail. On a **1080 × 1920** canvas, platform UI overlays the top and bottom. Keep all text, logos, and CTAs inside the **center ~70%**.

| Platform | Keep clear (top) | Keep clear (bottom) | Safe content area |
|----------|------------------|---------------------|-------------------|
| Instagram Stories | ~155px | ~310px | center 1080 × 1610 |
| Instagram Reels | ~250px (14%) | ~340px (20%) | center column |
| TikTok | ~150px | ~480px (caption) | center 65% width; ~140px off right edge |
| YouTube Shorts | ~150px | ~340px (title) | center column |
| Snapchat | ~130px | ~400px (Send/Chat) | center 1080 × 1420 |
| Facebook Stories/Reels | ~250px | ~400px | center column |

### The center-square method (one asset, every placement)

Place **all critical elements** (headline, logo, CTA) inside a centered **1080 × 1080** square on the 1080 × 1920 canvas. The core message then survives cropping across Feed, Stories, and Reels with no re-layout. The outer top/bottom bands become atmospheric background.

### Meta unified ad safe zone (March 2026)

For Stories/Reels **ads** on a 1440 × 2560 canvas: keep critical elements outside the **top 14%** (~358px), **bottom 20–35%** (~512–896px), and **6% each side** (~87px). Center content within the middle ~80% horizontally to survive Smart Zoom on ultra-tall (20:9) devices.

---

## Design best practices (deeply researched)

**Mobile-first.** The vast majority of impressions happen on a ~390px-wide phone. Preview every asset scaled down to phone size — if the headline isn't readable at thumbnail scale, it fails.

**Win the scroll in <300ms.** A post has a fraction of a second to stop the thumb. Use one of: high contrast, a face, a scale anomaly (one huge element), or a pattern break. Don't bury the hook.

**Type legibility on a 1080px canvas:**
- Body / supporting text: **≥30px** (smaller disappears on mobile).
- Headlines: 60–160px. The hero element should dominate.
- Line length: cap at ~30–40 characters for headlines; keep body under ~700px wide.
- One clear hierarchy per graphic: a primary element, a secondary, and quiet metadata — not three things shouting.

**Contrast.** Aim for WCAG AA (≥4.5:1 for text). Text over photos needs a scrim, gradient, or solid panel. Never rely on color alone to convey meaning (accessibility + small-screen rendering).

**One idea per asset.** If a slide/graphic carries two concepts, split it. Whitespace is a feature — leave ≥40% of feed graphics empty.

**Consistency across a series.** Carousels and campaigns should share a grid, type scale, color, and footer so they read as one set. Vary the content, not the system.

**Safe zones are non-negotiable** for stories, banners, and circular crops. Design with the overlay in mind from the first pixel, not as an afterthought.

**Resolution & quality.** Upload at the recommended pixel size — platforms penalize blurry/low-res content in distribution. Don't upscale. For ads, start at 1440px+ wide because delivery re-compresses.

**File discipline.** JPG for photos, PNG for crisp graphics/transparency, WebP where supported. Watch hard caps (e.g., podcast cover ≤512 KB, email header ≤200 KB, OG ≤300 KB ideal).

---

## Format → canvas quick lookup

| You want to make… | Build at | Ratio |
|-------------------|----------|-------|
| A feed post (any platform) | 1080 × 1350 | 4:5 |
| A square post / carousel slide | 1080 × 1080 | 1:1 |
| A story / reel / short / TikTok / Snap | 1080 × 1920 | 9:16 |
| A YouTube thumbnail / landscape image | 1280 × 720 (or 1920×1080) | 16:9 |
| A link preview / blog hero | 1200 × 630 | 1.91:1 |
| A Pinterest pin | 1000 × 1500 | 2:3 |
| A profile picture | 800 × 800 (downscales everywhere) | 1:1 |
| An X / Bluesky / Mastodon header | 1500 × 500 | 3:1 |
| A LinkedIn personal banner | 1584 × 396 | 4:1 |
| A YouTube channel banner | 2560 × 1440 (safe 1546×423) | 16:9 |
| A podcast / album cover | 3000 × 3000 | 1:1 |
| A Spotify Canvas | 1080 × 1920 | 9:16 |
