# Altitude Style Reference

Altitude is a dark editorial finance system. It uses a carbon-black canvas, stepped charcoal surfaces, bone-white serif display type, compact Inter UI, and precise Fira Code terminal details. The result feels like a private research journal for a financial AI product.

## Theme

Dark, monochrome, editorial, technical, alpine, finance-oriented.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Carbon Canvas | `#181818` | `--color-carbon-canvas` | Primary page background and dominant dark surface. |
| Obsidian | `#111111` | `--color-obsidian` | Deepest layer for footers, contrast wells, and dark recesses. |
| Graphite Card | `#1f1f1f` | `--color-graphite-card` | Cards, inputs, terminal panes, and contained panels. |
| Slate Elevated | `#262626` | `--color-slate-elevated` | Hover rows, secondary panels, and raised surfaces. |
| Iron Peak | `#323232` | `--color-iron-peak` | Highest dark tier for selected rows, menus, and popovers. |
| Bone | `#eeeeee` | `--color-bone` | Primary text, key labels, and light hairline details. |
| Ash | `#e4e4e4` | `--color-ash` | Secondary borders and light card outlines. |
| Fog | `#a4a19b` | `--color-fog` | Muted helper text, icon strokes, captions, and disabled labels. |
| Smoke | `#5e5d59` | `--color-smoke` | Low-emphasis text, subtle dividers, and quiet badge fills. |
| Pewter | `#4b4b4b` | `--color-pewter` | Deep borders and table separators. |
| Pure White | `#ffffff` | `--color-pure-white` | Maximum contrast details and light contrast cards. |
| Voltage Blue | `#2b7fff` | `--color-voltage-blue` | Sole saturated accent for links, focus rings, active states, and terminal highlights. |
| Mid Navy | `#1a365d` | `--color-mid-navy` | Subtle blue depth for icons, thin decorative marks, and restrained heading tints. |

## Typography

### Libre Baskerville

Use for display headlines only: hero statements, section openers, and editorial identity moments. Keep it at weight 400 or 500. Do not use it for body text, labels, buttons, tables, or navigation.

- Token: `--font-libre-baskerville`
- Fallback: Source Serif Pro, Lora, Crimson Text, serif
- Weights: 400, 500
- Sizes: 36px, 48px, 72px
- Letter spacing: `-0.025em`

### Inter

Use for every functional UI element: body copy, nav, captions, buttons, inputs, tables, labels, and badges.

- Token: `--font-inter`
- Fallback: system-ui, -apple-system, Segoe UI, sans-serif
- Weights: 400, 500, 600, 700
- Small uppercase labels can use positive tracking.

### Fira Code

Use only for terminal, command, code, and data identifier contexts.

- Token: `--font-fira-code`
- Fallback: JetBrains Mono, IBM Plex Mono, monospace
- Weights: 400, 600
- Tracking: `0.1em`

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 10px | 1.5 | 0.5px | `--text-caption` |
| Body | 14px | 1.5 | 0 | `--text-body` |
| Heading SM | 18px | 1.43 | -0.45px | `--text-heading-sm` |
| Heading | 28px | 1.38 | -0.7px | `--text-heading` |
| Heading LG | 36px | 1.15 | -0.9px | `--text-heading-lg` |
| Display | 72px | 1.1 | -1.8px | `--text-display` |

## Spacing And Shape

- Density: comfortable but compact in data areas.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 12px by default, increasing to 24px only for larger editorial panels.
- Element gap: 8px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 48, 64, 80, 96, 128, 136, 224`

### Radius Scale

| Element | Radius |
|---|---:|
| Icons | 4px |
| Badges | 4px |
| Inputs | 4px |
| Buttons | 4px |
| Cards | 8px |
| Large surfaces | 16px |

## Components

### Neutral Button

Use a transparent or dark surface, 1px border, 4px radius, Inter 14px, and Bone text. This system does not want a loud filled CTA as the default. Use Voltage Blue for focus, link text, or active indicators.

### Serif Section Header

Use Libre Baskerville, 36-72px, weight 400, tight tracking, and Bone text on dark backgrounds. Pair it with Inter helper copy in Fog.

### Workflow Tile

Use a light stone/off-white surface for the contrast interruption. Keep the card at 8px radius, 12-24px padding, thin Ash border, centered outline icon, and dark Inter label.

### Terminal Window

Use Graphite Card background, 8px radius, 1px Slate Elevated border, a compact top bar, and Fira Code content. Keep terminal type small and well spaced.

### Data Table Row

Use Inter 13px, Bone text, Slate dividers, and restrained alternating row backgrounds. Header labels should be small uppercase with positive tracking and Fog color.

### Pill Badge

Use 4px radius rather than full pill geometry. Keep badge text small, tracked, and neutral. Reserve Voltage Blue only for active or selected badges.

## Layout

Use a centered 1200px max-width page. Keep the hero as a single centered stack: serif display headline, short subhead, restrained action, and a thin mountain ridge line near the bottom. Product sections should alternate between dark terminal/product visuals and one light workflow-card interruption.

Navigation should be a simple 64px top bar with a wordmark, centered nav links, and a right-side login/action area. Avoid sticky behavior and avoid mobile-heavy hamburger patterns unless the viewport requires it.

## Imagery

Use painterly, atmospheric mountain landscapes in muted blue-gray tones, thin ridge-line artwork, and product terminal screenshots. Images should feel like expedition windows or research backdrops, not generic lifestyle stock.

## Do

- Use Libre Baskerville at 36-72px for display and section headlines.
- Maintain a five-step dark surface stack: Obsidian, Carbon Canvas, Graphite Card, Slate Elevated, Iron Peak.
- Use 4px radii for controls and 8px radii for cards.
- Keep body text in Inter 14px with Fog as the muted text color.
- Build spacing from 8px element gaps and 80px section rhythm.
- Let mountain line art or landscape imagery carry the storytelling.
- Reserve Voltage Blue for links, focus, selected states, and functional highlights.

## Don't

- Do not add extra saturated accents.
- Do not use bold serif headlines.
- Do not use the serif for body or UI text.
- Do not add gradient meshes, glowing orbs, glassmorphism, or 3D decorative art.
- Do not use heavy shadows.
- Do not make every section black; the light workflow interruption is part of the rhythm.
- Do not turn badges into large pills.
