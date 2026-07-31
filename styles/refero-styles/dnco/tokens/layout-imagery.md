# Layout & Imagery

## Layout

The page model is a wide single-column or 2-column grid with a generous max-width (~1400px) and flush-left alignment. The hero is a full-bleed black band dominated by the DNCO wordmark at extreme scale - no headline copy competes. Below the hero, the layout shifts to white with an editorial two-line headline flush-left at the page edge. Project work is presented as a multi-column image grid (2-3 columns) with no card chrome, separated by whitespace alone. Filter controls sit as a plain text list above the grid, not as a toolbar. Section rhythm is defined by hairline #e5e7eb dividers and 64px vertical gaps rather than by alternating background bands. Navigation is a minimal top bar with pill-radius text links and a tiny dot indicator for the active route.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Canvas White | `#ffffff` | Page background, primary content surface |
| 2 | Image Placeholder Mist | `#e5e7eb` | Solid fill behind loading or empty project tiles |
| 3 | Obsidian Invert | `#000000` | Hero/wordmark inversion - full-bleed black with white type |

## Elevation

Philosophy

The system has zero elevation. No component uses box-shadow, drop-shadow, or blur. Depth is created exclusively through: (1) whitespace between elements, (2) 1px #e5e7eb hairline dividers, and (3) the single full-bleed black inversion that breaks the otherwise all-white canvas. Never add shadows to cards, buttons, modals, or popovers - if a component appears to need depth, it should be flattened against the surface instead.

## Imagery

Photography is the only source of color in the system. Project images are shot on location - outdoor environments, people in public spaces, architecture, transit, signage, urban textures. Treatment is natural-light, documentary-style, full-bleed, and uncropped: no duotone, no overlay, no border, no radius. Images are presented at large landscape aspect ratios (roughly 4:3 or 3:2) and arranged in generous grids where whitespace does the work of gutters. The first-viewport brand wordmark is set in pure white on black, creating a dramatic tonal pivot before the white gallery layout begins. No illustrations, no icons, no abstract graphics - the visual identity is carried entirely by the wordmark and the project photography.
