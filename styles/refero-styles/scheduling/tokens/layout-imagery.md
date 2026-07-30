# Layout & Imagery

## Layout

Max-width 1200px centered content frame, with full-bleed sections (photo hero, dark cards, gradient washes) breaking out to viewport edges. The page model is a vertical stack of sections that alternate between white and mint-tint backgrounds, creating the cadence of a printed spread. The hero is a full-bleed dark photograph with left-aligned white headline overlay (not centered) and a single yellow CTA + ghost button stack positioned in the lower-left. Feature sections use a two-column pattern: large left-aligned heading with a 3-column card grid or single product mockup on the right. The stats band is a 3-column horizontal grid on a mint background with oversized numbers dominating. Navigation is a minimal top bar - text links left, three-button cluster right (ghost login, ghost demo, dark pill start trial) - with no sticky behavior on the hero. Section gaps are 80-120px, generous enough to feel editorial rather than dense.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Primary page background for header, content sections, and footer interior |
| 1 | Tint | `#f0f7f6` | Alternating section bands, card surfaces, badge fills - creates the second visual register |
| 2 | Ink | `#17150` | Dark cards, footer, announcement bar, primary buttons - highest-contrast surface for elevation |
| 3 | Highlight | `#cccc25` | Accent surface for CTAs, metric chips, gradient washes - functional, never decorative chrome |

## Elevation

- **Card:** `none - flat surfaces only, separation achieved through tint alternation and 1.5px hairlines`
- **Chat Widget:** `0 4px 12px rgba(23, 21, 14, 0.15) - the only consistently elevated element, used to mark it as out-of-flow UI`

## Imagery

Imagery alternates between two modes: editorial photography and product screenshot capture. The hero is a full-bleed documentary-style photograph of people working at a salon (warm, slightly desaturated, natural lighting, no staged poses) overlaid with white headline type - the photo sets lifestyle context without dominating. Product visuals are tight screen captures of the actual interface (calendar, analytics dashboard, payment flow) presented inside mint-tinted cards with no device frames or mockup chrome. Decorative gradient washes (yellow, periwinkle, green-fade) appear as full-bleed section backgrounds to break the rhythm between content blocks. Icons are minimal - mostly line-weight UI icons in product screenshots rather than illustrative iconography. No 3D renders, no abstract geometric art, no stock photography in feature sections.
