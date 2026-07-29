# Layout & Imagery

## Layout

Page model is full-bleed for all hero and feature imagery, with max-width 1200px contained for text and component grids. The hero is a 100vh full-bleed dark photograph with text overlaid in the bottom-left quadrant - no centered headline, no split layout. The first scroll section drops to a #ffffff band with a single centered statement (max-width ~720px), creating a moment of silence. The third section is a #031e25 dark band with a 3-column card grid of image-top / text-below cards. Section rhythm alternates: dark photo white statement dark feature grid light detail blocks. Navigation is a minimal top bar with logo-left, links-center, hamburger-right, transparent background over the hero. Spacing is generous - 36-64px between sections, 18-20px between elements, 20px inside cards. No sidebar, no mega-menu, no sticky behavior visible in static frames.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#e5e7eb` | Default page background for light sections - a slightly warm light gray that feels industrial rather than clinical |
| 1 | Paper | `#ffffff` | Section backgrounds, card surfaces, button fills, image frames - the bright neutral that creates breathing room |
| 2 | Deep Section | `#1d1d1` | Dark band background for feature sections and image-forward blocks |
| 3 | Ocean Floor | `#031e25` | Deepest dark surface - the bottom of the elevation stack, used for hero overlays and full-bleed photographic sections |

## Elevation

Arc avoids shadow almost entirely. The single detected shadow (rgba(0,0,0,0.05) 0 10px 15px -3px) is an isolated instance on the hero - likely a subtle text-lift on the headline. Depth comes from tonal jumps between #e5e7eb, #ffffff, #1d1d1, and #031e25, not from cast shadows. This reinforces the flat, engineering-precise aesthetic: surfaces sit on top of each other through color contrast, not blur.

## Imagery

Photography is the primary visual medium and it is always marine and always aerial or high-angle. Shots are full-bleed or 32px-radius framed, never square, never with decoration. Color treatment is naturalistic - the deep teal-green of open water carries the only chromatic energy in the system. No illustration, no iconography beyond the smallest utility glyphs (hamburger, flag), no 3D renders, no abstract graphics. The product itself (boats) is always shown in motion from above, creating wake and speed lines. Screenshots of software interfaces appear as flat product evidence inside feature cards. Density is image-dominant in the hero and feature sections, text-dominant in transition and detail sections.
