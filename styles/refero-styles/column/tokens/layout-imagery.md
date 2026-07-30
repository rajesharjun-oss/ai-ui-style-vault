# Layout & Imagery

## Layout

Full-page structure is max-width 1200px centered with generous side margins (64-80px on desktop). Hero is a split layout - headline and CTAs left-aligned at 40% width, with a floating transaction widget positioned right at 55-70% width over the halftone map background. Below the hero, sections alternate between white (#ffffff) and the light canvas (#f6f6f8) with 72px vertical gaps. Content arrangement follows a consistent 6-column grid: text blocks span 4 columns (66%), image/product cards span 5-6 columns with deliberate off-grid positioning. Feature sections use a 2-column text-left/product-right pattern. The trust stats section breaks to a full-width 4-column equal grid. Customer logos sit in a single centered row with 48px gaps. The footer is compact, 2-column layout. Navigation is a fixed top bar, 62px tall, transparent over the hero with backdrop blur, transitioning to white on scroll. No sidebar, no mega-menu - dropdowns are simple chevron menus.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#f6f6f8` | Base page background - the near-white cool-tinted surface that fills the viewport. |
| 1 | Card Surface | `#ffffff` | Top of the surface stack - content cards, transaction widgets, code blocks all sit here. |
| 2 | Frosted Overlay | `#ffffff80` | Translucent layer for nav pills, badges, and overlays that need to hint at background content beneath. |
| 3 | Sky Wash | `#88deeb` | Decorative background wash - used as soft accent behind data sections and chart areas. |
| 4 | Signal Orange Surface | `#f2936b` | Featured accent card background - the highest-signal warm surface, used at most once per page for the Brex highlight. |
| 5 | Deep Surface | `#011821` | Dark mode inversion - appears when a section needs to flip to dark navy for contrast. |

## Elevation

- **Product Card:** `rgba(0,0,0,0.02) 0px 40px 32px 0px, rgba(0,0,0,0.03) 0px 22px 18px 0px, rgba(0,0,0,0.03) 0px 12px 10px 0px, rgba(0,0,0,0.04) 0px 7px 5px 0px, rgba(0,0,0,0.07) 0px 3px 2px 0px`
- **Transaction Widget:** `rgba(30,30,44,0.15) 24px 48px 64px 0px, rgb(255,255,255) 0px 0px 0px 1px inset`
- **Bordered Card:** `rgba(18,22,30,0.024) 0px 1px 4px 0px, rgba(18,22,30,0.05) 0px 1px 0px 0px, rgba(18,22,30,0.024) 0px 0px 0px 1px`
- **Primary Button:** `rgba(17,26,74,0.1) 0px 1px 3px 0px, rgba(17,26,74,0.05) 0px 1px 0px 0px, rgba(255,255,255,0.5) 0px 1px 0px 0px inset, rgba(255,255,255,0.5) 0px 1px 4px 0px inset`

## Imagery

Imagery is minimal and functional - Column avoids stock photography entirely. The visual language is built from three sources: (1) SVG data illustrations, specifically a dotted halftone world map rendered in indigo-to-orange-to-seafoam gradient dots that creates a global-scale atmosphere behind the hero; (2) product mockup cards - floating widgets showing account balances, transfer details, and JSON code snippets in white cards with dramatic shadows; (3) chart visualizations - candlestick or bar charts in seafoam green with thin connecting lines, used in the trust/stats section. The halftone map is the signature visual element - its gradient transitions from #d65620 (orange) through violet, blue, sky cyan, seafoam, to yellow, creating a spectrum that ties together the entire brand palette in a single decorative surface. Icons are uniformly outlined at 1.5-2px stroke weight in #232730 or #a9acb6, with filled variants for active states. No lifestyle photography, no abstract 3D renders - the restraint is deliberate, keeping focus on product and data.
