# Layout & Imagery

## Layout

Full-bleed dark canvas with centered max-width ~1440px content container. Hero is a single-screen viewport with oversized headline left-aligned at ~20% from left edge, product image centered-right with dramatic negative space, and a floating glass price/buy bar anchored bottom-right. Section rhythm alternates between full-bleed black bands and full-bleed white bands (section openers like 'Lo principal.', 'Mas de cerca.', 'Bateria', 'macOS Tahoe'), separated by 80px vertical padding. Feature grids use 3-column card layouts at 28px radius. Content arrangement is consistently text-first: left-aligned headline, optional right-aligned video link, then media grid below. Navigation is a sticky 44px top bar + optional 52px promo strip, both fully opaque. No sidebar, no mega-menu - navigation is horizontal text links only with extreme minimalism.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#000000` | Full-page background, hero, nav backdrop |
| 1 | Elevated Surface | `#1d1d1f` | Card surfaces on dark mode, promo banner, section dividers |
| 2 | Glass Surface | `#424245` | Floating UI over photography, frosted price/buy bar |
| 3 | Light Card | `#ffffff` | Alternating light sections, feature card backgrounds |

## Elevation

The system rejects shadow-based elevation entirely. Depth is communicated through three mechanisms only: (1) tonal contrast - charcoal #1d1d1f cards on black #000000 canvas, (2) frosted glass via rgba(66,66,69,0.72) + backdrop-filter blur(20px) saturate(1) for elements that float over photography, and (3) the 28px border-radius which optically lifts card edges from the background. Adding box-shadow would violate the flat, cinematic aesthetic.

## Imagery

Photography is the primary visual content and dominates the page surface. Treatment: product hero shot on pure black background with dramatic side-lighting revealing the laptop's metallic edge - no environmental context, no lifestyle staging, the object exists in a void. Secondary product imagery follows the same isolation principle: devices on pure black or against gradient washes. Chip badges use prismatic iridescent gradients (blue purple pink orange) as decorative texture on otherwise minimal cards. Iconography is monochrome white outlined glyphs (play button, plus, arrow) at the SF Symbols stroke weight. No illustration, no 3D rendering, no abstract graphics - photography and typographic scale carry the entire visual weight.
