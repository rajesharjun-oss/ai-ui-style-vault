# Layout & Imagery

## Layout

Page model: full-bleed sections that alternate between atmospheric image backgrounds and cream/white editorial blocks, all max-width ~1440px centered for content. Hero pattern: full-viewport atmospheric image with massive overlaid serif headline in light cream, no nav, no CTAs - just title and a thin scroll indicator. Section rhythm: alternating bands of #ffffff and #fbf9f3, each separated by 100px of vertical breathing room, no visible dividers or rules. Content arrangement: consistently asymmetric - text occupies a narrow left column (35-40%) while photography takes the dominant right column (60-65%), creating a gallery-catalog reading rhythm. Grid usage: 2-column image grids for visual proof, 2-column text+image splits for editorial content, no 3+ column grids. Navigation: minimal sticky header with stacked wordmark and single hamburger, no mega-menu, no visible nav links until interaction. The overall feel is a printed monograph digitized - each screen is a spread.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Paper White | `#ffffff` | Primary page canvas |
| 1 | Warm Cream | `#fbf9f3` | Alternate section surface, card backgrounds, editorial warmth |
| 2 | Ink Black | `#1e1e1` | Dark mode sections, button fills, footer |

## Elevation

The system uses zero shadows. All depth and separation comes from the contrast between #ffffff, #fbf9f3, and #1e1e1 surfaces, plus generous whitespace. The cream-on-white tonal shift IS the elevation system - there is no z-axis, only surface levels. This is a deliberate editorial choice: shadows would cheapen the gallery aesthetic.

## Imagery

Imagery is the content, not decoration. The site uses large-format, uncropped architectural and interior photography - retail spaces, living rooms, and art installations where custom wallpaper is the protagonist. The hero is an abstract painted wallpaper texture (warm peach, pink, and blue atmospheric wash) that functions as a mood board rather than a product shot. All images have zero border-radius and fill their containers edge-to-edge. No image overlays, no darkened scrims, no duotone treatments. The color is allowed to live in the photography because the UI itself is strictly monochrome - this is a deliberate handoff: the interface is the frame, the imagery is the art. Density is image-heavy in content sections but text-dominant in the hero, where the 180px serif headline occupies the full viewport.
