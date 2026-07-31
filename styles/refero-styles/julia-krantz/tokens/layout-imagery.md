# Layout & Imagery

## Layout

Full-bleed, no max-width container. Header bar spans full width: name logotype pinned left, email and nav pinned right, both at 16px horizontal padding. Bio section below header uses a multi-column horizontal layout - approximately 4-5 text columns (About, Press, Speaking, Podcasts, Links) filling full width with 20-32px column gaps. Grid section below bio: 10-column mosaic of variable-width tiles in rows, each tile filled with photography. Tiles vary in width - some span one column, some two - creating a journalistic contact-sheet rhythm. No gutters visible between tiles except the 1px Ghost Line border. Navigation is a minimal top-right inline set of 3 links. No sidebar, no sticky header. The entire page scrolls vertically with no section anchoring or visual dividers beyond the Ghost Line horizontal rule.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Void Canvas | `#000000` | Base page background, section backgrounds, nav bar |
| 2 | Image Tile | `#111111` | Grid project tiles - filled with photography, bordered by Ghost Line 1px |

## Elevation

Zero shadows across the entire system. Depth is created purely by the contrast between the black canvas and photographic tile content. No box-shadow values appear anywhere; the 1px rgba(248,248,248,0.12) border is the only surface separator. Hover states use filter: brightness(0.82) - darkening the image rather than lifting the element.

## Imagery

Photography-dominant - every project grid tile is a full-bleed photographic crop: fashion portraiture, macro textile/material studies, AI-generated imagery, event photography. Photographs are raw-edged, sharp-cornered, zero border-radius. Images are not contained or padded - they fill their tile completely, edge to edge. No lifestyle staging context visible; images are treated as abstract color fields at tile scale, only readable as subjects when enlarged. Color in the UI exists exclusively within these photographs - from vivid AI-generated chromatics to desaturated fashion editorial. The photographic density IS the design: at the grid scale, the tiles form a chromatic mosaic against black. Icons: minimal use of directional glyphs (' ', ' ') inline with text, no standalone icon components. No illustrations, no 3D renders in the UI chrome.
