# Layout & Imagery

## Layout

Page model is max-width 1200px centered with generous outer padding (40-60px). The hero is a centered single-column type stack on the canvas - no split image+text, no full-bleed background. Sections below transition to a two-column asymmetric layout: left column is narrow (~40%) for heading + kicker, right column is wider for body copy, with 40-60px gap. The feedback widget card breaks the pattern - it appears as a floating centered card overlapping the decorative illustration band, creating a layered focal point. Navigation is a minimal top bar with three zones (brand left, logo center, actions right), no sticky behavior visible. The page breathes: 80-120px between sections, no dense grids, no card grids. The rhythm is editorial - one idea per section, each given room to exist. The faint background grid pattern behind the hero adds technical texture without competing with content.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#fafafa` | The base warm-white background of all pages |
| 1 | Card Surface | `#fafafa` | Floating content panels and cards - same color as canvas, distinguished only by shadow and radius |
| 2 | Secondary Surface | `#f4f4f5` | Nested or secondary buttons, subtle hover states, elevated sub-panels |
| 3 | Dark Surface | `#292929` | Primary action button fill, dark UI elements requiring maximum contrast against the light canvas |

## Elevation

- **Content Card:** `rgba(19, 19, 22, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 2px 3px 0px, rgba(34, 42, 53, 0.04) 0px 4px 6px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px`
- **Elevated Modal/Popover:** `rgba(19, 19, 22, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 2px 3px 0px, rgba(47, 48, 55, 0.05) 0px 24px 68px 0px, rgba(34, 42, 53, 0.04) 0px 4px 6px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px`
- **Image Frame:** `rgba(16, 24, 40, 0.08) 0px 17px 23px -6px, rgba(16, 24, 40, 0.03) 0px 6px 9px -3px`
- **Subtle Card Hairline:** `rgba(0, 0, 0, 0.2) 0px 0px 0.5px 0.5px, rgba(0, 0, 0, 0.08) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px`

## Imagery

Imagery is bimodal: product/UI screenshots sit in 16px-radius frames with soft directional shadows, while decorative editorial illustration appears as a full-bleed crowd of hand-drawn doodle characters in rainbow colors. The illustration is organic, uncontained, and runs edge-to-edge at the base of sections - it bleeds without a frame or mask. Photography (if any) would be high-key and desaturated to match the neutral palette. Icons are 24px outlined strokes in #292929, thin weight, monoline. The system treats illustration as atmosphere, not content - it's the only place color is permitted, and it stays in a contained decorative band rather than leaking into UI controls.
