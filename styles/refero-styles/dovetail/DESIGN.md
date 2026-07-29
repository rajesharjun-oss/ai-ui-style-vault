# Dovetail Style Reference

## North Star

Dovetail feels like a research command center after hours. The interface is dark, dense, and evidence-led. It should feel like a place where interview clips, insights, tags, transcripts, and decisions are organized with care.

The design is not dramatic cyberpunk. It is quiet product darkness: graphite canvas, charcoal cards, thin borders, pale text, and a single soft indigo action color.

## Color

The palette is dark neutral with one cool accent:

- `Graphite` `#0a0a0a`: page canvas and deepest application background.
- `Obsidian` `#111111`: main cards, elevated surfaces, input backgrounds.
- `Charcoal` `#1e1e1e`: nested panels, hover states, secondary dark fills.
- `Slate` `#2d2d2d`: active rows, separators, toolbar surfaces.
- `Iron` `#3a3a3a`: stronger borders and disabled controls.
- `Silver` `#a3a3a3`: secondary text, metadata, muted descriptions.
- `Pearl` `#fafafa`: primary text and high-contrast icon strokes.
- `White` `#ffffff`: strongest foreground, logos, and selected icon details.
- `Soft Indigo` `#8b7cf6`: primary CTA, selected states, and active markers.
- `Indigo Glow` `#a78bfa`: hover/active accent and subtle glow detail.
- `Muted Purple` `#6d5dd3`: secondary accent for tags, charts, and inactive accent states.

Use indigo sparingly. The system loses its seriousness if every card or chart becomes purple.

## Typography

Use Inter for most product text and JetBrains Mono for metadata. If Inter is unavailable, use system-ui. If JetBrains Mono is unavailable, use ui-monospace.

Recommended roles:

- Metadata: 12px, JetBrains Mono, 500, line-height 1.33.
- Caption: 13px, Inter, 500, line-height 1.38.
- UI: 14px, Inter, 500, line-height 1.43.
- Body: 15px to 16px, Inter, 400, line-height 1.5 to 1.6.
- Card title: 18px to 20px, Inter, 600, line-height 1.3.
- Section heading: 32px, Inter, 600, line-height 1.15, letter-spacing -0.02em.
- Hero: 48px to 56px, Inter, 700, line-height 1.05, letter-spacing -0.03em.

Keep text compact. This is an insight workspace, not an editorial hero site.

## Layout

The layout should feel like a research tool:

- Dark full-page canvas.
- Top navigation or app shell with thin border.
- Left sidebar or filter column for projects, tags, sources, or teams.
- Main content area with grids of research cards.
- Evidence detail panel with transcript, tags, quotes, and video preview.
- Dashboard sections with stats, charts, and insight lists.

Use a max width around 1280px for marketing/product pages, but allow full-width app layouts for dashboard surfaces. Keep 64px to 96px section gaps on marketing pages and tighter 12px to 20px gaps in app surfaces.

## Shape And Elevation

Dovetail uses small functional radii:

- Buttons: 8px.
- Cards: 8px.
- Inputs: 8px.
- Tags: 9999px.
- Video/media tiles: 10px to 12px.

Elevation is mostly absent. The system relies on 1px borders, surface steps, and hover fills:

- Card border: 1px solid Charcoal or Slate.
- Hover surface: Charcoal.
- Active row: Slate.
- Shadow: avoid, except very subtle overlay shadows for modals.

## Components

### Primary Indigo Button

Soft Indigo fill, White text, 8px radius, Inter 14px/600, compact padding. Use for key actions like create, analyze, import, or start research.

### Secondary Dark Button

Obsidian or Charcoal fill, Slate/Iron border, Pearl text, 8px radius. Use for lower-pressure actions and toolbar controls.

### Research Card

Obsidian surface, 1px Charcoal border, 8px radius, 16px to 20px padding, title, metadata row, tags, and optional preview snippet.

### Evidence Video Card

Obsidian or Charcoal frame, 10px to 12px radius, dark video thumbnail, timestamp metadata, transcript snippet, and tag pills.

### Tag Pill

Charcoal fill with Slate border, Silver or Pearl text, 9999px radius, 12px to 13px type. Selected tags can use Soft Indigo fill or border.

### Sidebar Navigation Item

Transparent default, 8px radius, 14px Inter 500, Silver text. Hover uses Charcoal, active uses Slate with Pearl text and optional Soft Indigo left marker.

### Search Or Filter Input

Obsidian fill, 1px Charcoal border, 8px radius, Silver placeholder, Pearl text, compact 12px vertical padding.

### Metric Tile

Obsidian card, 1px Charcoal border, 8px radius, metadata label in JetBrains Mono, large Pearl value, and small Silver context.

### Transcript Panel

Charcoal or Obsidian surface, compact rows, mono timestamps, Pearl speaker text, Silver body copy, and indigo highlight for selected quote.

### Table Or List Row

Graphite/Obsidian base, 1px divider, hover Charcoal, active Slate, compact cell padding. Use for projects, clips, insights, and participant lists.

## Imagery

Use product-real content: video thumbnails, transcript panels, insight cards, chart snippets, dashboard grids, customer quotes, and research media. Avoid abstract purple blobs, generic stock photos, and decorative hero art.

## Do

- Use Graphite as the dominant background.
- Build hierarchy with stepped dark surfaces.
- Use Soft Indigo for primary action and active state only.
- Use Inter for product text and JetBrains Mono for metadata.
- Use 8px radii for most functional UI.
- Use borders and surface fills instead of shadows.
- Show product-real research artifacts.

## Do Not

- Do not use colorful gradients.
- Do not use large purple backgrounds.
- Do not use big rounded marketing cards.
- Do not use heavy shadows for elevation.
- Do not make the interface sparse and airy when it should be dense.
- Do not use decorative stock imagery as the hero.
- Do not introduce extra accent colors.
