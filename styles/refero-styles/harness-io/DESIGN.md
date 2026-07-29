# Harness.io Style Reference

Harness.io is a nocturnal developer-infrastructure system. The interface reads as a mission-control deck: dark surfaces stack upward in small luminance steps, light borders define edges, and the few accent colors behave like instrument signals.

## Theme

Dark, DevOps, Git hosting, infrastructure, mission control, phosphor accent, pill controls, 3D product visual, command deck.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Void Canvas | `#070707` | `--color-void-canvas` | Page background and deepest surface. |
| Carbon Plate | `#0d0e12` | `--color-carbon-plate` | Primary card surface and main elevated panel. |
| Obsidian | `#141418` | `--color-obsidian` | Secondary card surface, code blocks, and nested panels. |
| Steel Border | `#22222a` | `--color-steel-border` | Structural borders, button outlines on dark, and nav separators. |
| Iron Edge | `#2e3038` | `--color-iron-edge` | Mid-tier surface, dividers, and hover overlays. |
| Cinder | `#60606c` | `--color-cinder` | Deep muted text, low-priority links, and idle icons. |
| Slate Mute | `#a2a4a9` | `--color-slate-mute` | Nav borders, inactive nav text, and chrome dividers. |
| Graphite | `#aeaeb7` | `--color-graphite` | Tertiary body text, subdued labels, and disabled-ish states. |
| Ash | `#c8cad0` | `--color-ash` | Secondary body text, muted descriptions, and helper text. |
| Fog | `#d9dae5` | `--color-fog` | Light card hairline borders on dark surfaces. |
| Cloud Mist | `#f0f0f0` | `--color-cloud-mist` | Secondary light text, soft fills, and muted highlights. |
| Pure White | `#ffffff` | `--color-pure-white` | Primary text, primary pill fill, and icon strokes. |
| Phosphor Mint | `#70dcd3` | `--color-phosphor-mint` | Accent card fill and highlight surfaces; one per viewport. |
| Signal Blue | `#0092e4` | `--color-signal-blue` | Link borders, active links, and focus accents. |
| Current Blue | `#00ade4` | `--color-current-blue` | Active nav state, selected menu item, and current-page indicator. |
| Deep Signal | `#0677d4` | `--color-deep-signal` | Input focus border, form active state, and info stroke. |
| Ice Blue | `#a6e5f2` | `--color-ice-blue` | Decorative soft borders and light accent strokes on cards. |
| Verdant Edge | `#75ae4c` | `--color-verdant-edge` | Outlined action borders, linked labels, and lightweight green emphasis. |
| Steel Iris | `#929dbd` | `--color-steel-iris` | Cool blue-gray card borders and secondary outlines. |

## Typography

### Calsans

Use for display and headings.

- Token: `--font-calsans`
- Fallback: Space Grotesk, wide-tracked geometric sans
- Weights: 300, 600
- Sizes: 18px, 24px, 32px, 34px, 56px, 64px, 72px, 88px
- Line height: 0.96 to 1.37
- Letter spacing: 0.056em at all sizes
- Role: engineered, instrument-panel headlines. Use positive tracking; never tighten it.

### Geist

Use for body, navigation, controls, forms, activity rows, badges, and metadata.

- Token: `--font-geist`
- Fallback: Inter, system-ui
- Weights: 300, 400, 500, 600
- Sizes: 8px, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 40px
- Line height: 0.88 to 1.57
- Letter spacing: negative at display-adjacent sizes, slightly positive at body sizes, strongly positive for micro labels
- Role: functional command-deck UI and readable product copy.

### Helvetica

Use only if a legacy embedded asset requires it.

- Token: `--font-helvetica`
- Fallback: Arial, system-ui
- Weight: 400, 600
- Size: 13px
- Role: incidental legacy content; not part of the primary style.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.22 | 0.5px | `--text-caption` |
| Body SM | 14px | 1.44 | 0.25px | `--text-body-sm` |
| Body | 16px | 1.50 | 0.27px | `--text-body` |
| Subheading | 20px | 1.50 | -0.34px | `--text-subheading` |
| Heading SM | 32px | 1.10 | 1.8px | `--text-heading-sm` |
| Heading | 56px | 1.10 | 3.1px | `--text-heading` |
| Heading LG | 72px | 1.00 | 4px | `--text-heading-lg` |
| Display | 88px | 0.96 | 4.9px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 8px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

### Spacing Scale

`8, 16, 24, 32, 40, 56, 80`

### Radius Scale

| Element | Radius |
|---|---:|
| Inputs | 5px |
| Nested cards | 16px |
| Cards | 20px |
| Badges | 800px |
| Buttons | 800px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Dark card | `--shadow-none` | `none` |
| Filled pill | `--shadow-filled-pill` | `rgba(0, 0, 0, 0.05) 2px 2px 0px 0px, rgb(255, 255, 255) 0px -1px 0px 0px inset, rgb(255, 255, 255) 1px 0px 0px 0px inset, rgb(255, 255, 255) -1px 0px 0px 0px inset, rgb(255, 255, 255) 0px 1px 0px 0px inset` |
| Input lift | `--shadow-input` | `rgba(0, 0, 0, 0.05) 2px 2px 0px 0px` |

Cards rely on light borders and surface steps, not drop shadows.

## Components

### Hero Headline

Calsans 88px/300, line-height 0.96, letter-spacing 0.056em, Pure White. Optional first phrase can use Phosphor Mint. The mood is spacious, engineered, and not shouted.

### Filled Pill Button

Pure White fill, Void Canvas text, 800px radius, 12px by 24px padding, Geist 16px/500. This is the only filled button style.

### Ghost Pill Button

Transparent fill, 1px Pure White border, Pure White text, 800px radius, 12px by 24px padding, Geist 16px/400.

### Dark Surface Card

Carbon Plate fill, 1px Fog border, 20px radius, 24px padding, no shadow. The light border on a dark card is the system-defining move.

### Phosphor Accent Card

Phosphor Mint fill, 20px radius, 24px padding, optional Fog border. Use at most one per viewport.

### Code Surface

Obsidian fill, 16px radius, 16px to 20px padding, code-like Geist text at 13px to 14px, Graphite text, subtle syntax accents. Nest inside Carbon Plate cards.

### Navigation Bar

Void Canvas background, about 64px height, logo left, centered links in Geist 14px, inactive labels in Slate Mute, active label in Pure White or Current Blue, right-side contact link and filled pill CTA. Use a light nav border if needed.

### Activity Row

Avatar circle, commit or PR message in Geist 14px/500 Pure White, metadata in 12px Graphite, status dot in Phosphor Mint or Verdant Edge, 10px vertical padding, and Iron Edge row dividers.

### Input Field

Carbon Plate fill, 1px Iron Edge border at rest, Deep Signal focus border, 5px radius, 12px padding, Geist 14px, Pure White text, Cinder placeholder. No glow ring.

### Status Badge

Outlined pill badge, 800px radius, 2px by 8px padding, Geist 11px to 12px with wide tracking. Success uses Verdant Edge border/text; info uses Deep Signal border/text. Never fill.

### Section Header

Uppercase Geist 12px eyebrow with wide tracking in Ice Blue or Steel Iris, followed by Calsans 56px/300 heading with positive tracking.

### 3D Product Visual Block

Rendered product visual with dark gradient ground, glowing edges, curved tracks, ribbons, or geometric objects. It blends into the Void Canvas and is not framed like a screenshot.

### Footer Link Column

Geist 14px/500 Pure White column heading, 13px to 14px Graphite links, 8px to 16px vertical gaps, four-column layout.

## Layout

Use a full dark theme from top to bottom. Hero is split 50/50 with headline and copy left, 3D product visual bleeding right. Later sections alternate between two-column text plus visual layouts, centered section headers, and 2-column or 3-column dark card grids. Keep content centered within 1200px and use 64px to 80px section rhythm.

## Imagery

Use rendered product visuals: curved tracks, flowing light ribbons, abstract geometric objects, and neon edge-lit forms on dark gradient grounds. Use activity feeds with avatars and status dots for flat product content. Avoid photography, flat illustration, light sections, and generic marketing icons.

## Do

- Use Calsans for all headlines at 56px or larger with positive 0.056em tracking.
- Define card edges with 1px Fog light borders.
- Use the filled white pill as the single primary action.
- Apply Phosphor Mint to no more than one card or panel per viewport.
- Use 20px card radius and 800px pill controls.
- Keep body text at Geist 16px/400 with slight positive tracking.
- Stack dark surfaces upward from Void Canvas to Carbon Plate to Obsidian.

## Don't

- Do not use drop shadows on cards or panels.
- Do not fill buttons with color; only the primary white pill is filled.
- Do not use multiple accent colors in one section.
- Do not set body text below 14px or above 18px.
- Do not apply negative letter-spacing to Calsans.
- Do not use dark borders on cards.
- Do not break the dark theme with light sections.
