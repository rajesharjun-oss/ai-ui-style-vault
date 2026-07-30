# Layout & Imagery

## Layout

Full-bleed dark canvas with max-width 1200px content containers. The hero is centered text-only: announcement strip 110px headline 3-line subhead twin CTA row (filled + ghost). Below the hero, a full-bleed 5-column customer site tile grid bleeds edge-to-edge, breaking the container. Subsequent sections use a max-width 1200px left-aligned model: 62px section heading followed by single-column testimonial cards that are 2-column (quote-left / product-render-right). Navigation is a sticky top bar with centered nav links. Vertical rhythm is consistent: 60-80px section gaps, 10px within-card gaps. The page breathes - large blocks of negative space between editorial-type sections create a gallery-walk feeling.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void | `#000000` | Page background - the base canvas everything sits on |
| 1 | Carbon | `#080808` | Card surfaces, nested containers, secondary background |
| 2 | Obsidian | `#111111` | Elevated cards, modal backgrounds |
| 3 | Graphite | `#171717` | Top-level elevation, popovers, deeply nested panels |
| 4 | Slate | `#242424` | Hover states, interactive fills, subtle overlays |

## Elevation

- **Card:** `rgba(0, 0, 0, 0.25) 0px 1px 2px 0px`
- **Elevated Panel:** `rgba(0, 0, 0, 0.25) 0px 10px 30px 0px, rgba(255, 255, 255, 0.1) 0px 0.5px 0px 0.5px`
- **Modal:** `rgba(0, 0, 0, 0.6) -10px 10px 20px 10px`

## Imagery

Photography and product renders do the heavy lifting in a nearly text-free design. Customer site showcases appear as contained screenshots in a 5-column tile grid, each at 8-12px radius, floating on pure black. Section visuals pair a large product render or editorial photograph (e.g. a creative professional portrait) with a dark overlay card containing UI chrome. Photography is high-contrast, editorial in quality, and always set against dark or neutral environments - no lifestyle clutter, no bright studio setups. Decorative gradients are nearly invisible (6% black overlay). Icons are minimal and outlined at 1px stroke weight in white or Electric Cyan. There are no illustrated characters, no 3D mascots, and no abstract geometric decorations - the visual restraint is total.
