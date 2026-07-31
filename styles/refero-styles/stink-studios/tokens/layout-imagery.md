# Layout & Imagery

## Layout

Full-bleed single-column composition with editorial vertical rhythm. The page opens with a 100vh cinema-set hero image with a giant wordmark overlaid. Navigation is not a top bar - it is a bottom-right anchored link cluster, giving the hero maximum negative space. Below the fold, the layout shifts to a wide single column of typographic manifesto blocks (60px Times New Roman) separated by 60-180px vertical gaps. The work showcase is a 2-column grid of full-bleed project stills, no gutters or card padding. No sidebar, no mega-menu, no sticky header. Every section bleeds to both viewport edges. The overall density is spacious: a handful of large elements per screen, each given room to breathe against the black canvas.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void | `#000000` | Universal page canvas - every section sits on absolute black |
| 1 | Soot | `#050505` | Nested containers and form fields needing barely-visible separation from canvas |

## Elevation

No shadows, no elevation tokens, no z-axis depth. The design is intentionally flat - the only layering is visual (image overlapping type, or text overlaying a dark photographic region for legibility). Components do not lift on hover; they swap, dim, or reveal a border. Depth is created by content scale and contrast, not by surface separation.

## Imagery

Full-bleed cinema-set photography and behind-the-scenes production stills dominate the hero - moody blue-lit studio environments with director's chairs, ladders, and lighting rigs. Work grid tiles are large-format project stills: outdoor advertising photography (the pink/magenta HR & Payroll transit poster), urban street scenes with branded signage (Canva storefront), and lifestyle editorial crops. Imagery is always unframed, 0px radius, edge-to-edge. No illustrations, no 3D renders, no abstract graphics. Icons are minimal: a single small circular toggle glyph in the nav cluster. Photography treatment is high-contrast and color-saturated - the projects are where the chroma lives, never the UI.
