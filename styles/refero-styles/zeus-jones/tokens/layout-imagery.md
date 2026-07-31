# Layout & Imagery

## Layout

The page model is full-bleed with generous side padding (~40px at desktop). The hero is a full-viewport display headline over a colorful aurora background - no navigation chrome competes with the statement. Below the hero, a thin 1px-bordered announcement bar spans edge-to-edge. Content sections follow a single-column or wide-grid structure with a 1200px max-width reading area; project cards appear in a 4-column horizontal row with overflow scrolling (the row is intentionally wider than the viewport, showing partial cards at the edges as a 'more work' affordance). Section headings are left-aligned with a 24px gap below a small eyebrow label. Spacing is generous: 40px between major sections, 16px between elements within a section. The overall rhythm is editorial - long quiet sections separated by typographic anchors, no dense information blocks, no sidebar navigation, no mega-menu.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Warm Parchment | `#fcfaf3` | Page canvas and default body surface |
| 2 | Soft Linen | `#ebe9e4` | Elevated card or panel - one tonal step up from the canvas |
| 3 | Midnight Ink | `#1a1c2c` | Dark surface for filled buttons and inverted sections |

## Elevation

The system deliberately avoids box-shadows. Hierarchy is established through type weight contrast (weight 100 display against weight 500 labels), hairline 1px borders in Midnight Ink, and surface tonal steps. A 1px solid border in #1a1c2c is the system's only structural separator - no soft drop shadows, no glow effects, no layered cards. This flatness is part of the editorial identity: the page should feel like ink on paper, not like a glass-morphism dashboard.

## Imagery

The visual system is dominated by two image modes: a single full-bleed psychedelic aurora on the hero (pink, violet, yellow, and green diffused color fields - clearly a photographic or AI-generated abstract, not a gradient token), and rectangular project card thumbnails with 20px radius showing editorial photography, product renders, and campaign artwork. Below the hero, imagery is contained, never full-bleed except for the card images themselves. Icon style is minimal - line-based menu icon in Obsidian #000000, and small 8px filled dots in Blush Coral #fd9494 as bullet markers. The site carries no illustration, no 3D, no product screenshots, and no icon system beyond utility marks. Photography treatment varies per project card and is not normalized - the design system treats images as content, not as styled components.
