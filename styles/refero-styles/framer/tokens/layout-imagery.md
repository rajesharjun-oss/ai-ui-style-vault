# Layout & Imagery

## Layout

Full-width sections that bleed edge-to-edge on the black canvas, with content constrained to ~1200px max-width centered within. Hero is a left-aligned headline + single CTA pill, with the right side left intentionally empty - asymmetric, not centered. Sections alternate between type-only layouts (large headline + sub-text) and product-screenshot showcases. The 'Shipped with Framer' section uses a logo wall in a 4-column grid. The community section frames a product screenshot in a centered max-width container with rounded window chrome. Navigation is minimal - a thin top bar with left logo and right-aligned links, no sticky behavior visible. Section rhythm: generous 80px vertical gaps between sections, creating distinct islands of content floating in the void.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void | `#000000` | Page canvas - the infinite black background |
| 1 | Graphite | `#111111` | Large feature cards and elevated panels one step above void |
| 2 | Obsidian | `#171717` | Mid-tier surfaces - content cards, button fills, window chrome |
| 3 | Iron | `#1e1e1` | Subtle intermediate surface for hover and pressed states |
| 4 | Slate | `#242424` | Input fields, elevated panels, highest standard surface |
| 5 | Midnight Tide | `#002238` | Atmospheric blue-tinted wash for accent sections and shadow tints |

## Elevation

- **Standard button:** `rgba(0, 0, 0, 0.2) 0px 2px 6px 0px`
- **Elevated card:** `rgba(0, 0, 0, 0.1) 0px 1px 2px 0px`
- **Floating element:** `rgba(0, 0, 0, 0.25) 0px 4px 8px 0px`
- **Blue accent glow:** `rgba(0, 153, 255, 0.2) 0px 5px 5px 0px`

## Imagery

Product UI screenshots dominate - framed in simulated window chrome with traffic-light dots, the embedded app screenshots become the hero imagery. Logo wall for social proof uses white wordmarks on black with generous spacing. No photography, no illustration, no abstract graphics - the visual language is the product itself, displayed as live interface. Icon style: minimal, outlined, mono-white at small sizes. Density: text-dominant with occasional large product screenshot breaks. The visual space ratio heavily favors typography over imagery.
