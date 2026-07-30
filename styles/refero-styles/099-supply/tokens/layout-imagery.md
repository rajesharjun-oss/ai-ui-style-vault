# Layout & Imagery

## Layout

Full-bleed white canvas with no max-width container - content extends edge to edge. Hero is a centered site title area (the '099' counter in large mono) followed by section grids. Each section begins with a left-aligned uppercase heading ('3D MOCKUPS', 'FRAMER COMPONENTS') in muted gray with wide tracking, then a uniform 5-column tile grid with consistent 12px gaps between tiles. Tiles are identically sized and shaped - a square-ish rectangle containing a centered asset and a metadata strip footer. No alternating bands, no dark sections, no asymmetric compositions. The grid is the page: museum-row after museum-row of black objects on white. Navigation is minimal - likely a top bar with category links in the same tracked-out uppercase treatment.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Page background - the gallery wall. |
| 1 | Card | `#ffffff` | Individual mockup and component tile surfaces, visually identical to canvas but defined by a 1px border. |
| 2 | Elevated Dark | `#222222` | Dark mode toggle, loader ring fills, modal overlays - the only surface that breaks from white. |

## Elevation

Zero shadows. All depth is conveyed through 1px hairline borders (#e0e0e0 default, #999999 on hover, #101010 for strong emphasis). The absence of shadows is deliberate - the museum-plinth aesthetic requires flat, paper-thin surfaces where objects sit on the same plane as their frames.

## Imagery

Pure UI, no decorative photography. The only imagery is the mockup assets themselves - high-fidelity 3D product renders (iPhone, hoodie, Apple Watch, drink carton, cap, Pro Display, MacBook Pro, business card, digital tablet) rendered in pure black or near-black against white. Illustrations are limited to UI component previews (theme toggle, loader ring, kinetic text dot sphere, grid loader plus-pattern, compare slider garment). Icon style: thin 1-2px stroke outlines, monochrome #555 or #101010, no fills. No lifestyle, no atmosphere, no context - each object is isolated like a product shot for a catalog.
