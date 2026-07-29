# Kobu - Style Reference

## Positioning

Kobu feels like a travel gazette or gallery catalogue. The interface should stay quiet enough that hotels, villas, landscapes, interiors, and architecture become the color and atmosphere. It should not feel like a booking funnel, a colorful travel marketplace, or a generic card grid.

## Theme

- Theme: light
- Mood: monochrome travel gazette on warm parchment
- Best fit: boutique travel, hotels, villas, retreats, architecture journals, hospitality portfolios, destination editorials

## Visual Principles

1. Use Parchment as the page paper.
2. Keep UI color monochrome.
3. Let photography be the only expressive color.
4. Make the wordmark the hero element.
5. Use Fira Mono labels as museum-tag details.
6. Separate with whitespace and 1px hairlines.
7. Avoid CTAs, gradients, fills, and shadows.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Ink Black | `#000000` | Maximum contrast headings and nav borders |
| Charcoal Deep | `#070707` | Densest display text when extra weight is needed |
| Obsidian | `#242429` | Primary text, icon strokes, and hairline borders |
| Graphite | `#3e3e3e` | Body copy, metadata, and softer list text |
| Ash Gray | `#919191` | Muted locations, tertiary labels, quiet accents |
| Parchment | `#f9f5f2` | Page canvas, hero, footer, and breathing space |
| Gallery White | `#ffffff` | Card surfaces, image borders, badge backgrounds |

## Typography

Use Gill Sans or a close humanist substitute for headings, body, wordmark, and editorial copy. Use Fira Mono for labels, badges, navigation, category tags, prices, and metadata.

Gill Sans creates the literary travel-magazine tone. Fira Mono creates the museum label tone. The pairing is the whole typographic personality.

Recommended fallbacks:

- Primary: `Gill Sans`, `Gill Sans MT Pro`, `Avenir`, `Proxima Nova`, `Museo Sans`, `ui-sans-serif`, `system-ui`
- Label mono: `Fira Mono`, `JetBrains Mono`, `IBM Plex Mono`, `ui-monospace`, `monospace`

OpenType for mono labels:

```css
font-feature-settings: "tnum" 1, "ss01" 1;
```

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Label | 10px | 1.5 | 500 | 0.183em |
| Caption | 12px | 1.43 | 400 | 0.167em |
| Body Small | 15px | 1.43 | 400 | 0 |
| Body | 16px | 1.25 | 400 | 0 |
| Subheading | 21px | 1.25 | 500 | 0 |
| Heading Small | 24px | 1.25 | 500 | 0 |
| Heading Large | 33px | 1.2 | 400 | 0 |
| Display Wordmark | 64px | 1 | 500 | 0 |

## Spacing And Shape

- Density: comfortable
- Page max width: 1440px
- Section gap: 60px to 80px
- Card padding: 0px
- Element gap: 10px to 15px
- Cards: 0px radius
- Images: 0px radius
- Buttons: 0px radius
- Badges: 5px radius

## Layout

Use a full-width parchment canvas with a large wordmark near the top, a minimal navigation bar, and property image cards that sit directly on the page. Property grids should feel like editorial plates arranged on paper rather than e-commerce cards.

Use 60px to 80px between sections. Keep card internals tight with 10px to 15px gaps. Prices and View All links should align right to create tension against left-aligned names and sections.

## Imagery

Photography is the expressive language. Use large, natural, editorial images of architecture, interiors, landscapes, resort exteriors, gardens, courtyards, modernist concrete, and warm interior lighting. Do not add overlays, duotone treatments, vignettes, or decorative image masks.

## Components

### Navigation Bar

Full-width bar on the Parchment canvas. Left group uses uppercase Fira Mono category links. Center uses a small KOBU wordmark. Right side uses a simple search icon. A single 1px Obsidian hairline runs along the bottom edge.

### Display Wordmark

Large KOBU text in Gill Sans, around 64px, line-height 1, weight 500 or 400, Obsidian color. It should stretch wide enough to become the main visual statement.

### Section Heading

Gill Sans 33px, line-height 1.2, weight 400, Obsidian. Optional paragraph below in Graphite, around 16px, constrained for readability.

### Property Card

Image-first layout. Full-bleed photo with no radius. Below: property name, location label, and right-aligned price. No card fill, no shadow, no border.

### Featured Badge

Fira Mono 10px uppercase label, weight 500, wide tracking, Gallery White fill, Obsidian text and border, 5px radius. Position top-left over the photograph.

### New Badge

Same as Featured Badge, but with a different label. Do not create a new color treatment.

### Price Tag

Fira Mono 12px uppercase label, Obsidian, tracked, right-aligned. No background and no border.

### Back-To-Top Button

Small fixed round utility button with Gallery White fill, 1px Obsidian border, and a simple upward chevron. This is a utility exception; do not use roundness elsewhere.

### View All Link

Gill Sans 21px weight 400, Obsidian, right-aligned, with a small outbound or directional glyph. No underline by default.

### Body Paragraph

Gill Sans 16px, line-height 1.25, weight 400, Graphite, max-width around 480px.

### Search Icon

Simple 16px line magnifying glass in Obsidian. No fill, no button background.

### Footer

Parchment band with a 1px Obsidian top border. Minimal uppercase Fira Mono text. No newsletter form and no CTA block.

## Rules

- Make photography the only expressive color.
- Use no colored CTA buttons, gradients, or accent fills.
- Use 1px Obsidian hairlines for structure.
- Use no shadows or elevation.
- Keep all UI surfaces in Parchment and Gallery White.
- Use Gill Sans for headings, body, and wordmark.
- Use Fira Mono for labels, badges, nav, prices, and metadata.
- Use 5px radius only for badges.
- Use 0px radius for cards, images, buttons, and nav.
- Do not introduce illustrations, icon fills, or decorative graphics.
