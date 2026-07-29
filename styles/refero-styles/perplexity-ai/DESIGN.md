# Perplexity AI - Style Reference

> Scholar's parchment behind clean glass

**Theme:** light

Perplexity AI reads as a warm-paper research desk: off-white parchment, quiet ink text, hairline warm-gray dividers, and one restrained teal for selected states. The layout is app-like rather than landing-page-like: a fixed left sidebar, centered category nav, large search artifact, and compact suggestion cards.

The design is deliberately flat. Suggestion cards get only a barely visible 1px shadow, while most hierarchy comes from background tone, hairline borders, and spacing. Typography stays calm: pplxSans-style type at weights 400 and 500 only, with no bold display system.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Parchment | `#faf8f5` | `--color-parchment` | Page canvas, card surfaces, and nav backgrounds. |
| Soft Paper | `#fdfbfa` | `--color-soft-paper` | Slightly elevated suggestion card surface. |
| Warm Mist | `#d1d1cd` | `--color-warm-mist` | Hairline card, input, and button borders. |
| Ash | `#92918b` | `--color-ash` | Muted helper text and secondary labels. |
| Graphite | `#72706b` | `--color-graphite` | Nav icons, secondary buttons, and inactive labels. |
| Ink | `#27251e` | `--color-ink` | Primary text, icon fills, and dark button backgrounds. |
| Pure Black | `#000000` | `--color-pure-black` | Rare maximum-contrast text and icon accents. |
| Deep Teal | `#016a71` | `--color-deep-teal` | Active nav item background, selected chip fill, badge fill, and search-input glow. |

## Tokens - Typography

### pplxSans

- **Token:** `--font-pplxsans`
- **Substitute:** Inter, system-ui, -apple-system, sans-serif
- **Weights:** 400, 500
- **Sizes:** 11px, 12px, 14px, 16px
- **Line height:** 1.00, 1.25, 1.33, 1.43, 1.50, 2.00
- **Letter spacing:** 0 across sizes
- **Role:** Custom geometric sans for all UI. Body text at 16px/1.5, UI labels at 14px/1.43, micro text at 11-12px.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 11px | 1.43 | 500 | 0 | `--text-caption` |
| body-sm | 12px | 1.43 | 400 | 0 | `--text-body-sm` |
| body | 14px | 1.43 | 400 | 0 | `--text-body` |
| body-lg | 16px | 1.43 | 400 | 0 | `--text-body-lg` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** compact

| Purpose | Value |
|---------|-------|
| Page max width | 900px |
| Sidebar width | 260px |
| Search width | 640px |
| Section gap | 32px |
| Card padding | 16px |
| Element gap | 8px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 32 | 32px | `--spacing-32` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| buttons | 6px | `--radius-buttons` |
| inputs | 12px | `--radius-inputs` |
| cards | 16px | `--radius-cards` |
| chips | 9999px | `--radius-chips` |

### Shadows

| Name | Value | Token |
|------|-------|-------|
| subtle | `rgba(0, 0, 0, 0.08) 0px 1px 2px 0px` | `--shadow-subtle` |

## Components

### Sidebar Nav Item

Transparent background, Graphite icon and label, no border, 12px by 12px padding, 16px pplxSans weight 400. Active state uses Deep Teal fill, white text, and 12px radius.

### Ghost Button

Transparent background, Graphite text, 1px Warm Mist border, 6px radius, 8px vertical and 12px horizontal padding, 14px pplxSans weight 400.

### Pill Chip

Transparent or near-transparent fill, Ink text, 9999px radius, 8px vertical and 12px horizontal padding, 14px weight 400. Active chips fill with Deep Teal and use white text.

### Filled Action Button

Ink fill, Parchment text, no border, 12px radius, 8px by 12px padding. Use for high-emphasis search or record controls.

### Suggestion Card

Soft Paper surface, 16px radius, 12px vertical padding, subtle shadow, no border. Contains Ink icon and title, plus Graphite 14px description. Arrange as a two-column grid.

### Search Input

Parchment background, 12px radius, 16px vertical padding, 1px Warm Mist border, optional Deep Teal glow at low opacity, Graphite placeholder at 16px. Width around 640px and centered.

### Badge Tag

Deep Teal fill, white text, 9999px radius, 11px pplxSans weight 500, 2px vertical and 8px horizontal padding.

### Top Nav Link

Transparent background, Graphite text, no border, no padding, 16px pplxSans weight 400. Hover shifts to Ink.

### Sidebar Brand Mark

Ink filled icon, no background, 16px box. Use as left-rail visual anchor.

### Sidebar Section Label

Graphite text, 12px weight 400, no background or border. Use to group Connectors, Skills, or Workflows.

## Do's And Don'ts

### Do

- Use Parchment as the base canvas.
- Use Ink for primary text and Pure Black only for maximum contrast.
- Reserve Deep Teal for active nav, selected chips, NEW badges, and search glow.
- Use 16px radius for cards, 12px for inputs, 6px for ghost buttons, and full pills for chips.
- Keep type weights between 400 and 500.
- Use 1px Warm Mist borders for hairline structure.
- Keep the main content column capped at 900px.

### Don't

- Do not introduce new accent colors.
- Do not use 600+ type weights.
- Do not add drop shadows beyond the single subtle suggestion-card shadow.
- Do not use Pure White as a surface color.
- Do not apply teal to body text or content icons.
- Do not exceed the narrow 900px main content rhythm.
- Do not add gradients, blurs, decorative imagery, photography, or screenshots.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#faf8f5` | Full-viewport warm off-white background. |
| 1 | Card Surface | `#fdfbfa` | Suggestion cards and elevated content blocks. |
| 2 | Active Nav | `#016a71` | Selected navigation item background. |
| 3 | Button Fill | `#27251e` | Solid button background against parchment. |

## Elevation

The design is nearly shadowless. Only suggestion cards use the subtle 1px shadow. All other layering comes from background tone and hairline borders.

## Imagery

No photography, illustration, or product screenshots. Identity comes from UI, typography, spacing, and the single teal accent. Icons are monochrome glyphs in Ink or Graphite.

## Layout

Use a two-pane app layout. The left sidebar is about 260px wide. The main content column is centered and capped around 900px. Top category nav sits above the search area. The central wordmark/search input is followed by a two-column suggestion card grid. Section gaps are compact at about 32px.

## Agent Prompt Guide

### Quick Color Reference

- Primary text: `#27251e`
- Secondary text: `#72706b`
- Background: `#faf8f5`
- Card surface: `#fdfbfa`
- Border: `#d1d1cd`
- Accent: `#016a71`
- Primary action: warm Ink button, not a separate CTA color

### Example Component Prompts

1. Suggestion card: Soft Paper background, 16px radius, 12px vertical padding, subtle 0 1px 2px shadow, Ink title and icon, Graphite description.
2. Search mode chip: full pill, 8px by 12px padding, Ink text; active state fills Deep Teal with white text.
3. Hero search input: Parchment background, 12px radius, 16px padding, Warm Mist border, Graphite 16px placeholder, width around 640px.
4. Sidebar nav item: Graphite icon and label, 12px padding, active Deep Teal background, white text, 12px radius.
5. NEW badge: Deep Teal fill, white 11px text, 9999px radius, 2px by 8px padding.

## Similar Reference Families

- Notion AI style off-white flat assistant UI.
- Phind style centered AI search with minimal decoration.
- ChatGPT style sidebar plus centered-content layout.
- You.com style answer-engine search above suggestions.

