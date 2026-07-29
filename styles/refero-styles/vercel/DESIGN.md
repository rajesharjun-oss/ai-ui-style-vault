# Vercel Style Reference

Vercel is a monochrome developer-product system. It feels like a precise terminal typeset on warm white paper: tight geometric headings, tiny monospace stamps, hairline border rings, minimal cards, and one black triangle brand mark.

## Theme

Light, developer platform, monochrome, terminal, paper, infrastructure, precise, compact, typography-led.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Carbon | `#000000` | `--color-carbon` | SVG icon fills, triangle logo mark, and pure graphic silhouettes only. |
| Obsidian | `#171717` | `--color-obsidian` | Primary headings, filled buttons, dark card fills, nav borders, and list markers. |
| Charcoal | `#4d4d4d` | `--color-charcoal` | Body paragraphs, card descriptions, and secondary button labels. |
| Stone | `#666666` | `--color-stone` | Muted captions, helper text, and de-emphasized UI labels. |
| Slate | `#7d7d7d` | `--color-slate` | Customer brand names and quiet heading variants. |
| Graphite | `#8f8f8f` | `--color-graphite` | Footer micro-copy and secondary metadata. |
| Smoke | `#a8a8a8` | `--color-smoke` | Tertiary text, placeholder copy, and subtle icon fills. |
| Ash | `#c9c9c9` | `--color-ash` | Disabled text, muted labels, and logo watermarks. |
| Hairline | `#ebebeb` | `--color-hairline` | 1px borders on buttons, links, cards, and input edges. |
| Paper White | `#fafafa` | `--color-paper-white` | Page canvas, card surroundings, and light button fills. |
| Pure White | `#ffffff` | `--color-pure-white` | Elevated cards, inset highlights, and input fields. |
| Terminal Green | `#297a3a` | `--color-terminal-green` | Confirmation text, command success marks, links, tags, and tiny emphasized phrases. |
| Spectrum Gradient | `linear-gradient(90deg, rgb(0, 255, 149) 0%, rgb(255, 208, 0) 25%, rgb(255, 23, 68) 50%, rgb(149, 0, 255) 75%, rgb(0, 229, 255) 100%)` | `--gradient-spectrum` | Decorative marketing sweep only. |
| Solar Edge | `linear-gradient(90deg, rgb(255, 220, 48) 0%, rgb(56, 162, 255) 100%)` | `--gradient-solar-edge` | Decorative two-stop feature callout only. |

## Typography

### Geist Sans

Use for display, body, navigation, buttons, links, cards, and product copy.

- Token: `--font-geist-sans`
- Fallback: Inter, system-ui
- Weights: 400, 450, 500
- Sizes: 14px, 16px, 30px, 56px, 64px
- Line height: 1.00, 1.10, 1.43, 1.50
- Letter spacing: -3.84px at 64px, -3.36px at 56px, -1.5px at 30px, normal at body sizes
- OpenType: disable contextual alternatives when matching the source, keep standard ligatures and stylistic set 11 when available
- Role: precise geometric reading and display voice.

### Geist Mono

Use for labels, metadata, code, CLI output, uppercase eyebrows, and tiny product stamps.

- Token: `--font-geist-mono`
- Fallback: JetBrains Mono, ui-monospace
- Weights: 400, 500, 600
- Sizes: 8px, 11px, 12px, 13px, 14px
- Line height: 1.00 to 1.67
- Letter spacing: 0.071em at 11px to 12px
- Role: mechanical labeling and terminal-native product proof.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Eyebrow | 11px | 1.50 | 0.071em | `--text-eyebrow` |
| Caption | 13px | 1.54 | 0 | `--text-caption` |
| Body | 16px | 1.50 | 0 | `--text-body` |
| Body SM | 14px | 1.43 | 0 | `--text-body-sm` |
| Heading | 30px | 1.10 | -1.5px | `--text-heading` |
| Heading LG | 56px | 1.00 | -3.36px | `--text-heading-lg` |
| Display | 64px | 1.00 | -3.84px | `--text-display` |

## Spacing And Shape

- Density: compact.
- Base unit: 4px.
- Max width: 1280px.
- Section gap: 96px to 128px.
- Card padding: 16px.
- Element gap: 12px.

### Spacing Scale

`4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 44, 208`

### Radius Scale

| Element | Radius |
|---|---:|
| Nav | 2px |
| Cards | 6px |
| Buttons | 6px |
| Pills | 9999px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Subtle ring | `--shadow-subtle` | `rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgb(250, 250, 250) 0px 0px 0px 2px` |
| Hairline ring | `--shadow-subtle-2` | `rgb(235, 235, 235) 0px 0px 0px 1px` |

These are border rings, not shadows. Avoid blur and offset depth.

## Components

### Filled Black Button

Obsidian fill, Pure White text, 6px radius, 12px to 20px horizontal padding, Geist Sans 14px/400. Use for the primary action.

### Ghost Outline Button

Transparent fill, Charcoal text, Hairline ring, 6px radius, 20px padding, Geist Sans 14px/400. Use for secondary actions.

### Pill Button

Obsidian or Pure White fill with contrasting text, 9999px radius, compact 12px horizontal padding. Use only in tight nav or header clusters.

### Text Link Button

No background, no border, 0px radius, Obsidian or Charcoal text, Geist Sans 14px to 16px. Use for navigation and inline references.

### Bordered Card

Pure White background, 6px radius, 16px padding, border via stacked rings: `0 0 0 1px rgba(0,0,0,0.08), 0 0 0 2px #fafafa`. Use for feature cards and product mockups.

### Inverted Card

Obsidian fill, Pure White text, 6px radius. Use sparingly to break a grid.

### CLI Output Panel

Pure White panel with Geist Mono 12px to 13px. Use black triangle command prefixes and Terminal Green checkmark confirmations. This is the product demo voice.

### Logo Strip Row

Single horizontal strip of grayscale customer logos, 24px to 32px gaps, softened to Slate or Ash.

### Eyebrow Label

Geist Mono 11px/400, uppercase, 0.071em tracking, Obsidian, with about 12px spacing before the heading.

### Top Nav Bar

64px sticky bar, Paper White background, optional backdrop blur, wordmark left, nav links center-left, action cluster right. No bottom border.

### Hero Composition

Asymmetric three-zone composition: headline on the left, black triangle mark centered or offset, eyebrow stack on the right. No image background.

### Feature Card Grid

Two-up or three-up card grid. Cards use the bordered card treatment, 16px to 24px padding, 30px headings, Charcoal descriptions, and embedded product proof.

## Layout

Use a 1280px centered container with 24px to 48px horizontal padding. Keep the background Paper White across the page, with no section color shifts. The hero is asymmetric, with tight headlines, the triangle mark, and a small right-side metadata stack. Sections separate through 96px to 128px whitespace, not dividers. Feature grids use 2-column or 3-column layouts with compact gaps.

## Imagery

Imagery is functional. Use the triangle mark, CLI output panels, light-mode product screenshots, integration cards, framework logos, and grayscale customer wordmarks. Avoid photography, decorative illustration, 3D renders, large colored gradients, and generic icon packs.

## Do

- Use Obsidian for primary text and filled buttons.
- Use Carbon only for the triangle mark and SVG fills.
- Apply 6px radius to cards, buttons, and bordered containers.
- Use 9999px radius only for tight nav pills.
- Set headings at weight 400 to 450 with tight tracking.
- Use Geist Mono uppercase labels at 11px to 12px with 0.071em tracking.
- Build depth with stacked hairline rings.
- Prefix terminal commands with a triangle mark and confirmations with a checkmark in Terminal Green.
- Keep sections separated by 96px to 128px whitespace.

## Don't

- Do not use drop shadows.
- Do not introduce chromatic UI color outside Terminal Green and optional decorative gradients.
- Do not use pure black for text.
- Do not use pure white for dark surfaces.
- Do not use border radius larger than 6px on cards or rectangular buttons.
- Do not set body or heading type outside the Obsidian, Charcoal, and Stone scale.
- Do not use 300, 600, or 700 weights for headings.
- Do not use Geist Sans for labels, metadata, or code.
