# Layout & Imagery

## Layout

Full-bleed page model with no outer container. Each section is a viewport-width color block. Internal layout is split-composition: text occupies the left ~55%, decorative geometry or code occupies the right ~45%. Text is left-aligned within its column; body prose sometimes right-aligns in a narrow sub-column. The nav is a floating centered pill, not a full-width bar - it detaches from the layout grid. Hero section uses a Sage background with a 120px headline left and a curved striped panel right. Subsequent sections alternate Warm Stone, Soft Sand, and Powder Blue backgrounds. Section gaps are generous (90-150px vertical padding). No card grids, no pricing tables, no feature matrices - content is prose-led, not grid-led. The page reads top-to-bottom as a sequence of colored editorial spreads.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Bone Canvas | `#f9f9f0` | Default page background between colored sections |
| 1 | Sage Field | `#d5fad3` | Hero section background - carries the largest display type |
| 2 | Warm Stone Field | `#9d937c` | Body-copy sections, editorial prose blocks |
| 3 | Soft Sand Field | `#ccc5a3` | Tonal break sections, striped-pattern panels |
| 4 | Powder Blue Field | `#badbee` | Code display panels, technical data surfaces |
| 5 | Charcoal Stamp | `#21201c` | Filled button surface, inverted modal background |

## Elevation

- **Nav Pill Border:** `inset 0 0 0 1px #0f0e0b`
- **Section Hairline (Warm):** `inset 0 0 0 1px #ccc5a3`
- **Section Hairline (Cool):** `inset 0 0 0 1px #badbee`

## Imagery

No photography. The visual language is entirely abstract: (1) Full-bleed muted color fields that act as atmosphere, not content. (2) Hard-edge striped geometric patterns on the right side of sections, distorted by wave/curve masks to create flowing vertical bands. (3) Monospace code blocks inside Powder Blue panels, showing actual Move/Rust syntax. (4) 1px hairline lines as printed-matter dividers. The aesthetic is editorial-graphic, not product-screenshot. Everything is flat, geometric, and color-blocked. No 3D renders, no illustrations, no product mockups, no lifestyle photography - the palette and typography ARE the imagery.
