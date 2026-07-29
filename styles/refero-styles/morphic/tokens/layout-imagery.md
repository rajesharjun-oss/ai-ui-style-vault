# Layout & Imagery

## Layout

Full-bleed dark canvas with a centered max-width content area of ~1280px. The hero is a two-column layout: left side has the announcement bar + two-tone headline, right side has body text + dual CTAs (primary blue + secondary dark). Below the hero, the showcase grid is a two-row, seven-column grid of borderless image cards spanning the full content width. Subsequent sections use a single-column layout with a left-aligned two-tone section header and a horizontally-scrolling card carousel (6+ cards visible, with left/right arrow controls and a 'See more' button). Section gaps are generous (96px) to let the dark space breathe. Navigation is a minimal top bar with no background fill, floating on the black canvas. The product UI mockup section uses a centered single-column layout with the mockup panel occupying ~80% of the content width.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#000000` | Full-bleed page background, hero sections, and between-section gutters - pure black absorbs all light so generated imagery and accent blue are the only luminous elements |
| 1 | Card | `#212121` | Primary elevated surface for workflow cards, product UI mockups, and content containers |
| 2 | Raised | `#292929` | Secondary buttons (ghost/outlined), nested cards, and interactive surfaces one step above Card |
| 3 | Floating | `#333333` | Tertiary buttons, highest elevation elements, and active/pressed state backgrounds |

## Elevation

- **Image card:** `rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`

## Imagery

Imagery is the star of the system. The entire visual strategy revolves around AI-generated photographs and renders displayed in tightly-cropped rectangular cards within a grid. Images are full-color, high-contrast, and span the entire spectrum - portraits, landscapes, cinematic scenes, product shots, surreal compositions. They are presented without frames, borders, or labels in the showcase grid (two rows of borderless images on pure black), and with a subtle caption overlay (white title + gray description) in the workflow carousel. There is no lifestyle photography, no stock imagery of people using software, no office shots - every image is generated content demonstrating the product's output. The imagery-to-text ratio is extremely high: images occupy roughly 70% of vertical space below the fold, while text serves only as thin captions and section headers.
