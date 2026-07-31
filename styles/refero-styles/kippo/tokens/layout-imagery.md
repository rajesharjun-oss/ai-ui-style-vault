# Layout & Imagery

## Layout

Single-column, max-width ~1200px centered layout on a pure black canvas. The hero is a two-column split: left side holds the two-tone display headline, subtitle, download badges, and QR code; right side holds the phone mockup on a gradient backdrop. Below the hero, a full-width press logo strip repeats logos in two stacked rows. Further down, sections alternate between two-column text+visual blocks (text-left/image-right) and centered single-column feature stacks. Cards are arranged in single rows, not multi-column grids. Navigation is a single horizontal bar pinned at the top: logo left, three uppercase links right, all within a thin white-bordered pill or rectangle. The overall rhythm is spacious - 100-150px between major sections, with the dark canvas absorbing visual weight and making the few colored elements feel deliberate.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void Canvas | `#000000` | Page-level background - the infinite black everything else floats on |
| 1 | Carbon Panel | `#29292a` | Elevated card surface, barely stepping forward from the void |
| 2 | Neon Border | `#ffffff` | 1px white outlines that define transparent cards without filling them |

## Elevation

Philosophy

Kippo has no shadows. Depth is created entirely through layering (overlapping profile cards, the phone mockup on a gradient plane) and through outline contrast (a 1px white border on a black fill is louder than any shadow). This is an intentional anti-convention: most dark-mode UIs rely on subtle elevation shadows to separate surfaces, but Kippo's arcade-wireframe language treats the border as the structural element and shadows as unnecessary noise. When stacking elements, overlap them with a small offset rather than adding drop-shadow or blur.

## Imagery

Imagery is almost entirely product-internal: phone mockups showing the app UI, and stacked profile-card illustrations that function as feature explainers. The only 'real' photography is inside the phone mockup screens (user profile photos of people, shown as small rounded thumbnails). No full-bleed lifestyle photography, no decorative illustrations outside the product, no abstract graphics. The phone mockup sits on a gradient backdrop (gold magenta) that is the single moment of color richness in the system. Press logos in the social-proof band are the one place external brand colors appear, tolerated as content rather than decoration.
