# Layout & Imagery

## Layout

Full-bleed, edge-to-edge layout with no max-width container. The page reads as a vertical sequence of full-viewport-height screens: (1) a full-bleed photographic or video hero with a minimal top nav overlaid and a small wordmark bottom-left, (2) subsequent full-bleed media sections stacking vertically with generous 96px breathing gaps, (3) a terminal section that is pure black with a two-column text layout - tiny region labels (US, UK) left-aligned and a flowing block of talent names right-aligned. Navigation is a single thin horizontal row of four evenly-spaced text links with no background and no logo block. Content alignment is asymmetric: nav is spread across the full width, wordmark anchors bottom-left, text blocks pull left with a slight indent. The grid is implicit - there is no visible column structure, only full-width media and text that reads as a credit roll. Density is sparse between sections but tight within text blocks.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void Canvas | `#000000` | Base page background - every section, every gap, every margin is this color |
| 1 | Media Surface | `#000000` | Photographic and video content replaces the void - no surface transition, the canvas IS the background behind media |

## Elevation

Zero elevation. The system treats depth as a sin: no shadows, no z-axis layering, no floating panels, no card lift. Media bleeds directly on the black canvas and type floats on the same plane. The single visual hierarchy device is the jump from #000000 to full-color photography, which is an absolute contrast rather than a soft elevation.

## Imagery

Photography and video are the entire visual system. Imagery is full-bleed, edge-to-edge, unmasked, with zero rounding and no frame. Treatment is cinematic and high-production: warm tungsten key lights, deep shadows, saturated color pockets against darker backgrounds - the aesthetic is music-video or indie film still, not corporate lifestyle. No illustration, no abstract graphics, no product shots. The people in the imagery are the roster - the work is self-portraiture of the talent. Imagery occupies 100% of the viewport in hero and section positions; there is no image-on-canvas composition, only image-as-canvas. A small blue focal dot is sometimes the only UI element overlaid on the photography.
