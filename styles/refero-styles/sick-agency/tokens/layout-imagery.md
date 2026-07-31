# Layout & Imagery

## Layout

Layout is full-bleed, not containerized. There is no max-width wrapper - the page fills the viewport horizontally. Sections are hard-cut color bands stacked with zero vertical gap, each band filling 100vw. Within a band, content sits in a loose editorial grid: display type often runs edge-to-edge (letterforms bleeding off the sides), body text is constrained to a narrow measure (max ~480px) and left-aligned. The hero is a single color band with display type set at 229px or 122px, sometimes split by a vertical type column on the left edge (rotated 90 ). Navigation is minimal - a single pill button or text link, not a traditional nav bar. The rhythm is poster-like: one big typographic statement per section, surrounded by color silence.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Cobalt Field | `#0029ff` | Darkest full-bleed band; used for primary action surface and dramatic section backgrounds |
| 1 | Orange Field | `#ff4e27` | Mid-warmth full-bleed band; provides transition between the cobalt and yellow extremes |
| 2 | Yellow Field | `#ffc700` | Lightest full-bleed band; the dominant canvas color, carries display headings in black |

## Elevation

There is no elevation system. Depth is communicated through color contrast between full-bleed sections, never through shadows or blur. A button on a section inherits contrast from the section's background, not from a shadow ring. Any use of box-shadow would break the broadside aesthetic - if a component feels like it needs elevation, it is the wrong component for this system.

## Imagery

The site is almost entirely type-driven, with no photography. Visual content consists of hand-drawn illustration stickers (UFO, basketball, abstract orbital shapes) that function as zine-style decorations rather than product imagery. The illustration style is flat with hard outlines or single-color fills, rendered in system colors (#0029ff on yellow/orange fields, #ffc700 on cobalt fields). There are no product screenshots, no stock photography, no lifestyle imagery, no gradients or textures. The page IS the visual - color fields and display typography carry the entire atmosphere.
