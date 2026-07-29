# Lightdash - Style Reference

> Lavender console on paper: warm surfaces, slate text, one violet action color, soft dashboard cards, and quiet technical credibility.

## Theme

Light. The page should feel like a clean analytics workspace printed on a warm off-white canvas. Avoid cold white-on-blue SaaS styling.

## Design Story

Lightdash sits between developer tooling and friendly product marketing. Use warm paper backgrounds and barely tinted lavender panels to keep the product approachable. Let actual dashboard screenshots, query panels, and connector logos do the technical work.

The main color discipline is important: violet is the action and focus color. Use one clear violet moment per viewport, then rely on neutrals and pale lavender for structure.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Electric Violet | `#6e56cf` | `--color-electric-violet` | Primary action, active tabs, focus, selected navigation |
| Periwinkle | `#b8b8ff` | `--color-periwinkle` | Secondary accent, soft illustration fills, hover washes |
| Mist Violet | `#f5f4ff` | `--color-mist-violet` | Hero gradient and pale highlight sections |
| Slate Ink | `#121217` | `--color-slate-ink` | Primary text and strongest UI strokes |
| Graphite | `#2d2b35` | `--color-graphite` | Secondary headings and technical copy |
| Pebble | `#6d6875` | `--color-pebble` | Body text, muted nav, captions |
| Ash | `#8c8796` | `--color-ash` | Placeholder text, disabled states, helper copy |
| Line Gray | `#e5e1eb` | `--color-line-gray` | Borders, dividers, input outlines |
| Cloud | `#f7f5fb` | `--color-cloud` | Card and panel background |
| Paper | `#fffdf8` | `--color-paper` | Page canvas and warm light sections |
| Pure White | `#ffffff` | `--color-pure-white` | Cards, buttons, screenshot frames |
| Code Navy | `#1f2937` | `--color-code-navy` | Dark code blocks and terminal surfaces |

## Typography

Display font: Britti Sans.

- Use for hero and large section headings.
- Keep it at 44px to 72px.
- Use weight 700.
- Tracking should be tight but not squeezed.
- Do not use Britti Sans for paragraphs, forms, nav, tables, or code.

UI and body font: Inter.

- Use Inter for everything functional.
- Body text is 16px to 18px at 1.5 to 1.6 line-height.
- Labels and buttons use 14px to 15px medium.
- Use JetBrains Mono or a similar mono only inside SQL snippets, schema labels, or technical examples.

## Type Scale

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.4 | 0 |
| Label | 14px | 500 or 600 | 1.4 | 0 |
| Body | 16px | 400 | 1.55 | 0 |
| Body Large | 18px | 400 | 1.6 | 0 |
| Card Heading | 20px | 600 | 1.3 | 0 |
| Section Heading | 44px | 700 | 1.05 | -0.02em |
| Hero Display | 72px | 700 | 0.98 | -0.03em |
| Code | 13px | 400 | 1.55 | 0 |

## Spacing And Shape

- Base unit: 4px.
- Density: comfortable.
- Page max width: 1180px.
- Section gap: 72px to 96px.
- Card padding: 24px to 32px.
- Element gap: 12px to 20px.
- Buttons: 8px radius.
- Inputs: 8px radius.
- Cards: 12px radius.
- Large panels: 16px radius.
- Pills and badges: 999px radius.

## Elevation

Use soft slate-tinted shadows only:

- Card shadow: `0 18px 50px rgba(31, 41, 55, 0.10)`
- Panel shadow: `0 8px 24px rgba(31, 41, 55, 0.08)`
- Focus ring: `0 0 0 3px rgba(110, 86, 207, 0.22)`

Avoid dramatic drop shadows and glow effects.

## Components

### Primary CTA Button

Electric Violet fill, Pure White text, Inter 600 at 15px, 8px radius, 12px 18px padding. Use one primary action at a time.

### Secondary Button

Pure White fill, Line Gray border, Slate Ink or Graphite text, Inter 600 at 15px, 8px radius. Use for docs, demo, or secondary conversion actions.

### Top Navigation

White or warm translucent header with Lightdash wordmark left, product links center, and action cluster right. Keep nav labels 14px Inter medium. Use violet only for selected or primary action states.

### Hero Product Frame

Centered hero copy with Britti Sans display heading, muted product explanation, button row, and a large dashboard screenshot frame below. The screenshot frame uses a white card, 12px radius, Line Gray border, and soft panel shadow.

### Dashboard Screenshot Card

Use real dashboard or analytics mockups with tables, charts, SQL, metrics, and sidebars. Frame in white with 12px radius and light border. Avoid abstract art where a product screenshot would explain more.

### Feature Card

Cloud or Pure White surface, 12px radius, 1px Line Gray border, 24px padding, small violet icon or badge, Inter heading and body copy.

### Tabbed Comparison Panel

Segmented tabs at top using pill or 8px controls. Active tab uses Electric Violet fill or violet text on Mist Violet. Panel body can show code snippets, charts, or workflow diagrams.

### Code Block

Code Navy surface, 12px radius, JetBrains Mono 13px, soft syntax colors, and a small header label. Use code blocks sparingly as technical proof.

### Connector Logo Grid

Grid of data-source, warehouse, or BI logos inside white or Cloud tiles. Keep tiles quiet and evenly spaced. Use neutral borders and no heavy shadow.

## Layout

Use a centered 1180px content frame. Hero is a centered stack with a large product preview below. Supporting sections alternate Paper, Cloud, Mist Violet, and Pure White panels. Use 2-column feature explanations, 3-column feature cards, and full-width screenshot bands. Keep section rhythm spacious but not airy.

## Imagery

Use product screenshots, dashboard panels, SQL snippets, connector logos, and simple geometric illustrations. Avoid lifestyle photography, stock office scenes, and decorative blob backgrounds. If illustrations are used, keep them schematic and product-adjacent.

## Rules

Do:

- Use Electric Violet for primary action, active state, and focus.
- Keep violet sparse, usually one prominent violet element per viewport.
- Use Britti Sans only for display headings.
- Use Inter for all functional UI.
- Frame screenshots in white cards with light borders.
- Use Mist Violet and Cloud for soft structure.
- Use 8px controls and 12px cards.

Do not:

- Do not turn the page into a purple gradient system.
- Do not use violet as body text.
- Do not use Britti Sans for paragraphs or nav.
- Do not use dark mode as the default.
- Do not add cartoon mascots or lifestyle photography.
- Do not make card corners overly round.
