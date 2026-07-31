# Layout & Imagery

## Layout

The page is an asymmetric, masonry-flavored grid of themed cards on an Obsidian canvas. The hero is a single full-width Cream Paper panel (one card spanning the grid) containing the Portrait wordmark and a two-column meta block beneath. Below the hero, the layout breaks into a responsive 3-column card grid that itself becomes the navigation: each card is a destination, and the chromatic fills form a color-coded index. Cards are not uniform in height - a tall Cream Panel sits next to a shorter Charcoal card next to a full-bleed Solar Yellow thesis block. Column gaps are ~20px, row gaps are ~25-40px, and the outer page is centered within a 1280px max-width container. Section breaks are achieved with 80px of empty Obsidian space, never with a divider line.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Obsidian Canvas | `#000000` | The void between every grid cell and the outer page background. |
| 1 | Charcoal Card | `#2b2b2b` | Default monochrome card surface for text-forward content. |
| 2 | Cream Panel | `#f0e7e4` | Inverted hero/about card - the only light surface in the system, acts as a full-bleed opener. |
| 3 | Themed Chromatic Field | `#113619` | Category cards that substitute the neutral surface for a saturated chapter color (also #322b66, #2e2909, #fde440). |

## Elevation

The system is entirely flat. No box-shadows, no glows, no blurs. Depth is communicated exclusively through chromatic contrast - a Solar Yellow card sitting next to a Forest Floor card next to an Obsidian void creates the sense of layered paper without any rendered shadow. The single visual exception is the occasional radial-gradient wash in empty hero states, which simulates spotlight on a gallery wall rather than a UI drop shadow.

## Imagery

Imagery is used as documentary evidence, not decoration. Article cards carry full-color editorial photography (copper mines, oil rigs, glacial fields, aerial urban shots) clipped to 12px-radius tiles. Some cards use flat geometric illustrations (a constellation diagram for the Berlin card, a wind-turbine sketch for the Sakana AI card) - these are monochrome line art in Coffee Bean on a chromatic fill. Icons are line-only, ~1.5px stroke, and sit inside Location cards. There are no full-bleed hero photographs, no overlapping layers, no masked edges - every image lives inside a 12px-radius rectangle inside a 20px-radius card. The visual language is closer to a printed annual report than a SaaS landing page.
