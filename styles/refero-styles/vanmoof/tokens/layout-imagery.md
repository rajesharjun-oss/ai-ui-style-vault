# Layout & Imagery

## Layout

Page model is full-bleed with no max-width constraint on hero panels - dark cinematic imagery spans the entire viewport. Content sections after the hero use a centered max-width of ~1200-1440px with generous 24-64px horizontal gutters. The hero pattern is a single full-viewport dark panel per product, stacking vertically as the user scrolls (S6 hero, then A5 hero, then app section). Each hero is a split: oversized left-anchored product name (280px) + right-aligned supporting text with ghost CTA. Navigation is a fixed top bar with centered logo. Section rhythm alternates between dark full-bleed hero bands and white content sections, creating high-contrast vertical pulses. Content arrangement uses 4-column symmetric grids for feature cards (track, configure, share, unlock) with equal gutters. No sidebar, no mega-menu - the hamburger is the only nav trigger. Density is extremely sparse: each section gets 64-80px vertical padding, and the page never exceeds 5-6 content blocks above the fold of any given product.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Hero Panel | `#222222` | Full-bleed dark photographic background for product heroes - the darkest surface in the system |
| 1 | Canvas | `#ffffff` | Primary page background for content sections, feature grids, editorial blocks |
| 2 | Section Band | `#f7f7f7` | Alternating section tint to create visual rhythm between white content blocks |
| 3 | Muted Surface | `#e0e0e0` | Subtle background for inactive states, placeholder fills, or tertiary panels |
| 4 | Structural Line | `#e5e7eb` | Hairline border and divider color - defines edges without surface weight |

## Elevation



## Imagery

Imagery is the sole source of color and atmosphere in this system. Hero panels use full-bleed, high-contrast product photography - tight crops on bicycle frames, handlebars, lights, and wheels against dark studio backgrounds with no lifestyle context. The bike IS the subject; the photography eliminates all background noise, leaving the product to occupy the entire visual field. No people, no environments, no props. Lower sections transition to white-background product shots and UI mockups (app screens, dashboard tiles). The treatment is editorial-commerce: think automotive launch photography, not lifestyle cycling. Images are always rectangular with sharp corners (no rounding), overlapping the navigation boundary, and frequently full-bleed edge-to-edge. The 280px product name sits as a typographic overlay on the left, never centered, creating an asymmetric balance with the product imagery occupying the right and center.
