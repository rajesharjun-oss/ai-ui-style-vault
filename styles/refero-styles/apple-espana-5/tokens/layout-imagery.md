# Layout & Imagery

## Layout

The page is a vertical stack of full-bleed product sections, each one viewport-height or taller. Max content width for text is ~980px, always centered. Nav is a fixed 44px bar at the top with a frosted glass effect. Each product section follows the same vertical rhythm: centered headline (56px) centered subhead (21px) centered button pair large product render filling the lower 60% of the section. Sections alternate between #f5f5f7 canvas and soft gradient washes to create visual separation. The Apple TV+ entertainment carousel is the only section that breaks the centered-text pattern - it is a full-bleed edge-to-edge horizontal scroll with large card tiles. Footer is a dense 4-column link grid in a #f5f5f7 band at the very bottom. No sidebar navigation, no mega-menus in the visible viewport.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#f5f5f7` | Page background and the majority of section fills |
| 1 | Pure White | `#ffffff` | Nav bar surface, white-on-blue button text, card elevation |
| 2 | Section Wash - Ice | `#aad0f6` | Soft blue gradient band behind certain product hero sections |
| 3 | Dark Band | `#000000` | Apple TV+ / entertainment carousel section - full-bleed dark surface |

## Elevation

- **Global Nav:** `No shadow - uses backdrop-filter: saturate(1.8) blur(20px) for a frosted glass effect against any background`

## Imagery

Product photography is the dominant visual content - large, center-anchored renders of MacBooks, iPhones, and iPads float directly on the section background with no card framing. Photography style is studio-catalog: pure white or pale blue seamless backgrounds, soft natural shadows under the product, no lifestyle context or human models in the product sections. The Apple TV+ carousel uses cinematic dark photography with strong color grading. Iconography is minimal - SF Symbols-style glyphs in the nav at 1.5-2px stroke weight, monochrome. The page contains zero illustrations, zero abstract graphics, and zero decorative backgrounds beyond the per-section tint washes. Imagery occupies roughly 50% of the page's visual area, with the remaining 50% being typography and the off-white canvas.
