# Layout & Imagery

## Layout

Full-bleed layout with no max-width constraint. A fixed left sidebar (~160px) holds the seven numbered section nav cards stacked vertically, each card a different vivid color. The main content area fills the remaining viewport with the warm cream canvas. The hero is a single oversized display headline (200-259px) that bleeds past its container - the type IS the hero, not a background image. A bottom progress bar (Ember Orange) spans the full viewport width. Sections alternate between cream canvas and one of five warm tinted backgrounds (Sage, Blush, Sand, Sky, Celadon) or one of four dark slates, creating a zine-like chapter rhythm. The page model is asymmetric: the sidebar is a permanent anchor while content flows full-width to the right edge.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Bone Cream Canvas | `#f4e9e1` | Primary page background, the warm paper that everything sits on |
| 1 | Paper White | `#ffffff` | Elevated card surfaces, active nav state, input fields |
| 2 | Tinted Washes | `#cee4cd` | Alternating colored section backgrounds - Sage, Blush, Sand, Sky Tint, Celadon - one tint per content block |
| 3 | Saturated Color Blocks | `#ff3d00` | Full-saturation nav cards and content blocks using the seven section colors |
| 4 | Dark Slates | `#444639` | Dark sections with hue-tinted darks - Olive, Forest, Cocoa, Plum |

## Elevation

No shadows. The system is entirely flat - depth comes from color contrast, not blur or offset. Color blocks sit directly on the cream canvas with zero shadow. Rounded corners (16px) and color saturation do all the work that drop-shadows would do in a conventional system.

## Imagery

Primarily typographic and color-block-based - the system treats massive display type itself as the dominant visual. When photography appears (in Work, Talent, Careers sections), it is contained in 16px-radius frames on the cream canvas, never full-bleed, and never given a shadow. No illustrations, no 3D, no decorative graphics - the seven section colors and the display type ARE the visual identity. Iconography is minimal to absent; when present, it is a single-color flat glyph at 16-24px. Image-to-text ratio is low: text dominates, images serve as proof points within color blocks.
