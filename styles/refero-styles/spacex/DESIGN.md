# SpaceX Style Reference

> Mission-control typography over a cinematic black viewport, with spacecraft photography acting as the entire visual system.

## Theme

Dark.

SpaceX uses a severe monochrome interface. The page is black, the typography is cool off-white, and everything else is supplied by full-bleed photography of rockets, planets, launches, and space. The system has no decorative accent color and no card layer. It feels like an aerospace control panel laid directly over a cinematic image feed.

## Core Principles

1. Use black as every page surface.
2. Use cool off-white as the only primary foreground color.
3. Let photography carry the visual spectacle.
4. Use uppercase industrial sans typography with strong tracking.
5. Use outlined ghost buttons only.
6. Place text directly on imagery or black, never inside cards.
7. Keep section flow single-column and full-bleed.
8. Avoid shadows, glows, gradients, and elevated surfaces.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Black | `#000000` | `--color-void-black` | Page canvas and every section background |
| Star White | `#f0f0fa` | `--color-star-white` | Headings, body text, icons, nav, button text, button borders |
| Dim Steel | `#545457` | `--color-dim-steel` | Secondary outlines, dividers, muted labels |
| Dark Gunmetal | `#404040` | `--color-dark-gunmetal` | Barely visible separators and structural hairlines |

## Typography

Use D-DIN when available. Use Barlow as the practical free fallback. The overall effect should feel engineered, geometric, and industrial rather than editorial or warm.

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Primary | D-DIN | Barlow, DIN Next Condensed | Navigation, body, labels, buttons |
| Headline | D-DIN-Bold | Barlow Bold, DIN Next LT Pro Bold | 48px all-caps section headlines |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 10px | 400 | 0.94 to 1.5 | 0.09em |
| Body small | 12px | 400 | 1 to 1.5 | 0.10em |
| Body | 13px | 400 or 700 | 0.94 to 1.7 | 0.10em |
| Body large | 16px | 400 | 1.5 | 0.10em |
| Section headline | 48px | 700 | 1 to 1.25 | 0.02em |

Small text is widely tracked. Headlines are still uppercase but less tracked so they read as solid mass.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Section gap | 60px |
| Card padding | 20px |
| Element gap | 18px |
| Nav radius | 4px |
| Card radius | 4px |
| Button radius | 4px |
| Pill radius | 32px |

Structural elements should stay at 4px radius. Use 32px only for compact pill selectors or toggle-like controls.

## Layout

Use a single-column, full-bleed flow. Each section is dominated by one large image or a black field. Text blocks are left-aligned and constrained to about 400px to 500px. Place the text in the left third of the viewport, vertically centered when used over imagery.

Recommended flow:

1. Transparent top navigation over black or imagery.
2. Full-bleed hero photograph.
3. Left-third text block with all-caps headline, body copy, and ghost button.
4. More full-bleed image sections stacked vertically.
5. Minimal utility selector or launch information in the nav.
6. No card grids, no alternating light sections, no tinted panels.

## Components

### Ghost Outline Button

Primary action style. Transparent fill, 1px Star White border, 4px radius, Star White uppercase text, 12px to 13px, 700 weight, 0.10em tracking. Padding should be around 10px 20px. Optional arrow icon stays Star White.

### Secondary Outline Button

Transparent fill, 1px Dim Steel border, Dim Steel uppercase text, same dimensions as the primary ghost button. Use for de-emphasized or utility actions.

### Pill Selector

32px radius with the same outline and tracked uppercase text treatment. Reserve for compact selectors, launch dropdowns, or toggle-like controls.

### Top Navigation Bar

Transparent background with no shadow, blur, or filled strip. Put the white wordmark on the left, uppercase tracked links across the nav, and a compact outlined selector at the far right. Use 10px to 12px D-DIN-style text with 700 weight and 0.09em to 0.10em tracking.

### Full-Bleed Hero Section

Use a viewport-width aerospace image with no border, no radius, and no overlay panel. The text block floats directly on the dark region of the image. Headline is 48px, uppercase, Star White, tight line height. Body is 13px, tracked out, and max 500px wide.

### Text-Over-Image Block

Same pattern as the hero but can be used for subsequent sections. Keep text left-aligned, no card, no tinted backing, and no framed image container.

### Section Headline

D-DIN-Bold-style, 48px, uppercase, Star White, 0.02em tracking, line-height 1 to 1.25. It should be the loudest typographic element.

### Body Paragraph

D-DIN-style, 13px, weight 400, Star White, 0.10em tracking, line-height about 1.7, max-width around 450px. It should read more like mission-control labeling than relaxed prose.

### Launch Selector Widget

Outlined top-nav utility. Use a 1px Star White border, 4px radius, uppercase tracked label, and a small caret. Keep it transparent.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Void | `#000000` | Base canvas for all sections |
| 1 | Image Bleed | `#000000` | Full-bleed photography fades back into black |

There is no elevated surface layer. There are no cards, panels, or tinted content containers.

## Elevation

No elevation system. Do not use shadows, drop shadows, glows, blurs, glass effects, or depth layers. Depth comes from photography only. Hover states can adjust outline opacity or add a very subtle transparent fill.

## Imagery

Full-bleed cinematic photography is the design system. Use rockets, launchpads, Earth from orbit, Mars, spacecraft interiors, boosters, plumes, and space-black compositions. Images should be large enough to own the viewport.

Use raw image edges. Do not round, crop into cards, frame, blur, or overlay decorative gradients. The ideal image has dark regions where off-white text can sit without a backing panel.

## Do

- Use `#000000` as the page background everywhere.
- Use `#f0f0fa` for almost all UI foregrounds.
- Set headings in all caps at 48px with 0.02em tracking.
- Use uppercase D-DIN-style text with 0.09em to 0.10em tracking for nav, labels, body, and buttons.
- Build all actions as 1px outline ghost buttons.
- Anchor text blocks in the left third of the viewport.
- Use full-bleed aerospace photography as the main visual layer.

## Don't

- Do not introduce a chromatic accent color.
- Do not use filled buttons.
- Do not place text inside cards, panels, or tinted containers.
- Do not use structural radius above 4px, except 32px pill selectors.
- Do not use warm, humanist, or editorial fonts.
- Do not add shadows, gradients, glows, or glass blur.
- Do not fragment imagery into grids.

## AI Builder Notes

If the page feels empty, the answer is stronger imagery or more precise type placement, not more UI. The brand voice is black, off-white, tracked uppercase, hairline outlines, and a single cinematic image per section.
