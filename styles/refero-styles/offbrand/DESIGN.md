# OFF+BRAND. - Style Reference

OFF+BRAND. is a warm-parchment editorial system built around typography, hairlines, strict geometry, and one iridescent sphere. The page should feel like a printed studio portfolio: big custom type, quiet monochrome surfaces, sharp project tiles, museum-label microcopy, and a single chromatic object in the hero.

## Theme

- Theme mode: light.
- Visual temperature: warm paper, ink, and one iridescent light source.
- Surface logic: parchment canvas, white paper cards, stone secondary panels, ash hairlines.
- Energy: editorial, restrained, architectural, agency-grade, typographic.

## Core Principles

1. Use Parchment as the exclusive page canvas.
2. Use one typeface family across the entire system.
3. Treat the iridescent sphere as a singleton hero object.
4. Keep buttons and links ghost-like.
5. Use 0px radius for cards and images.
6. Use 10px radius only for interactive hit areas.
7. Use Ash hairlines for structure, never colored lines.
8. Avoid color beyond the hero sphere.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Parchment | `#e5e4e0` | Page canvas and section backgrounds |
| Ink | `#1d1d1d` | Primary text, headings, link borders, dark UI marks |
| Paper | `#ffffff` | Elevated card surfaces, logo cells, project tile canvases |
| Ash | `#bfbebe` | Hairline borders, subtle dividers, structural outlines |
| Stone | `#cdcdc9` | Secondary panel background and quiet surface separation |
| Iridescent Sphere | `linear-gradient(255deg, rgb(250, 203, 14), rgb(240, 107, 168) 30%, rgb(120, 186, 230) 65%, rgb(255, 255, 255))` | One hero gradient object only |

## Typography

Primary type is Ataero Retina OB Edition. Use it everywhere: display, headings, body, labels, links, nav, and buttons. Fallbacks for prototypes only: Neue Haas Grotesk Display, Inter with tight tracking, Suisse Intl, system-ui, sans-serif.

Rules:

- Use one type family only.
- Use weight 400 for display, headings, and body.
- Use weight 700 sparingly for small labels or navigation.
- Use all caps for display headlines and section labels.
- Use positive tracking across the scale.
- Do not set body text below 15px or above 18px.
- Display line-height should be 0.80 so stacked lines form one typographic block.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 400 | 1.4 | 0.55px |
| Body Small | 15px | 400 | 1.4 | 0.15px |
| Body | 18px | 400 | 1.4 | 0.23px |
| Subheading | 34px | 400 | 1.0 | 0.44px |
| Heading Small | 46px | 400 | 1.0 | 0.6px |
| Heading | 70px | 400 | 0.8 | 0.91px |
| Heading Large | 76px | 400 | 0.8 | 0.99px |
| Display | 103px | 400 | 0.8 | 1.34px |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max content width: 1400px.
- Section gap: 76px to 119px.
- Card padding: 30px.
- Element gap: 19px.
- Spacing values: 5, 6, 8, 15, 19, 30, 32, 46, 76, 119.

Radius:

- Cards: 0px.
- Images: 0px.
- Links: 10px.
- Inputs: 10px.
- Buttons: 10px.
- Do not round card or image containers.

## Elevation

This system is intentionally flat.

- No box shadows.
- No drop shadows.
- No elevation effects.
- No glow.
- Depth comes from Parchment, Paper, Stone, hairlines, and layered background ornaments.

## Layout

- Full-viewport hero with display type overlapping a large gradient sphere.
- The sphere is slightly right-of-center and behind the text.
- Content blocks are left aligned with asymmetric text and body columns.
- Client logos use a strict 2 by 5 grid with hairline dividers.
- Project cards are large sharp rectangles with subtle grid-paper backgrounds.
- Section labels are small all-caps museum labels above content.
- Concentric circle ornaments appear as page-level geometry.
- No sidebar, no heavy footer structure, no busy navigation.

## Imagery

Preferred imagery:

- One CSS gradient sphere in the hero.
- Product renders and screenshots on white project cards.
- Flat client logos inside strict cells.
- Thin concentric circle ornaments.
- Grid-paper overlays for project tiles.

Avoid:

- Lifestyle photography.
- Stock imagery.
- Abstract illustrations beyond the sphere.
- Gradients repeated as small accents.
- Colored button fills or card fills.

## Motion

Motion should be minimal and editorial.

- Hover can underline a ghost text link or invert the all-work filter button.
- The hero sphere is static.
- Concentric circles are static.
- Avoid animated gradients, parallax, hover lift, and dramatic transitions.

