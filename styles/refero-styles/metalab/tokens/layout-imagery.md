# Layout & Imagery

## Layout

The page is full-bleed with no container constraint - text and elements flow edge-to-edge across a wide viewport (1440px+ target). The hero pattern is a three-column asymmetric split: display headline flush-left, a dark elevated panel centered, and a secondary headline word ('Make') flush-right with metadata annotations floating in the margins. Section rhythm uses generous vertical gaps (96px+) with no visible dividers - separation is spatial, not structural. Navigation is a minimal text row at the top, not a bar with background fill. The overall density is low: large amounts of black space, few elements per screen, and each element given room to breathe. The grid is loose - columns are implied by alignment, not by visible lines.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void | `#000000` | Base page canvas - the entire site lives on black |
| 1 | Charcoal | `#252525` | Elevated panel, the single step of depth above the canvas |
| 2 | Bone | `#ffffff` | Inverse surface for high-contrast zones and typographic inversion |

## Elevation

Depth is achieved through a single value step: #252525 panels sit on the #000000 canvas with no shadow, no border, no blur. The system deliberately avoids box-shadows entirely - a 1.4:1 contrast between #000000 and #252525 is sufficient to distinguish elevation, and adding shadows would introduce warmth and softness that contradicts the flat, editorial aesthetic. There is exactly one tier of depth above the canvas, and it is always the same color.

## Imagery

Imagery is minimal and treated with the same restraint as the type system. A single dark, softly gradient panel appears in the hero - its surface is nearly featureless, suggesting a product or device rendering rather than a photograph. No lifestyle photography, no illustration, no decorative graphics. The visual weight of the page comes entirely from typography and negative space. If images appear on inner pages, they would be high-contrast, tightly cropped, and sit on the same #000000 canvas without frames or borders.
