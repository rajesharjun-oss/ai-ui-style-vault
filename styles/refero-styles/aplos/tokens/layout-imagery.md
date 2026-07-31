# Layout & Imagery

## Layout

Max-width 1200px centered content with full-bleed dark hero and alternating section bands. The hero is a full-viewport dark slab with large product photography and left-aligned serif headline. Below, the page shifts to a Bone (#f2f1ed) canvas hosting a centered 'Benefits' section: serif heading, body paragraph, then a 3-column card grid mixing one Cocoa card and two Paper White cards. The grid is symmetric and equal-width. Subsequent sections follow the pattern: centered serif heading 1-2 column product showcases with overlapping image+text panels. Navigation is a simple top bar (not sticky, not mega-menu) with logo left and 4-5 text links right. Footer follows in dark Ink. Vertical rhythm is very slow - 96-120px between sections - creating a gallery-like scroll rather than a dense commerce page.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Bone | `#f2f1ed` | Page-level canvas, most section backgrounds |
| 1 | Paper White | `#ffffff` | Card surfaces, product panels, light benefit cards |
| 2 | Cocoa | `#3b3429` | Inverted accent cards, dark feature blocks |
| 3 | Ink | `#000000` | Hero backdrop, footer, maximum contrast slabs |

## Elevation

The system deliberately avoids drop shadows and blur effects. Elevation is communicated entirely through tonal layering: Bone canvas Paper White cards Cocoa accent cards Ink hero slabs. The only shadow token (#b4aeac) is a barely-perceptible link hover state, never used for component lift.

## Imagery

Product photography is the dominant visual element - tightly cropped cans, bottles, and styled cocktail glassware on pure black. No lifestyle, no people, no contextual environments: the object IS the hero. Photography is high-contrast, studio-lit, and occupies 60-80% of hero and product card real estate. No illustrations, no icons beyond minimal UI chrome, no decorative graphics. Color treatment is natural (sage green can, pale yellow cocktail liquid) but always grounded against black backgrounds so the warmth feels intentional rather than incidental.
