# Visitors - Style Reference

Visitors is a bright white analytics system with an engineered, restrained product feel. It combines a white canvas, carbon text, lavender primary action, pill controls, hairline dashboard cards, and small functional category colors. The style should feel flat and fast, not decorative or heavy.

## Theme

- Theme mode: light.
- Visual temperature: white, cool, engineered, and precise.
- Surface logic: white canvas, linen bands, mist fills, fog borders, soft dashboard panels.
- Energy: analytics-first, privacy-product, flat, geometric, quick.

## Core Principles

1. Use Lavender only for primary action and selected states.
2. Use Iris only for the register/nav button.
3. Use OpenRunde across the whole UI.
4. Keep buttons, chips, and tags fully pill-shaped.
5. Use 1px Fog borders on cards, tables, and dashboard panels.
6. Use minimal elevation and avoid dramatic shadows.
7. Keep feature category colors scoped to one category each.
8. Center the hero text stack; keep dashboard content structured and aligned.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Carbon | `#181925` | Primary text, headings, nav links |
| Paper White | `#ffffff` | Base canvas, card surfaces, button fills |
| Linen | `#fafafa` | Subtle background sections and table rows |
| Mist | `#f5f5f5` | Ghost fills, inputs, disabled states |
| Fog | `#e8e8e8` | Hairline borders, table gridlines, card edges |
| Ash | `#999999` | Muted body text, placeholders, inactive nav |
| Graphite | `#666666` | Secondary text, captions, light-button text |
| Lavender | `#918df6` | Primary action, selected nav state, conversion moment |
| Iris | `#9580ff` | Register nav button and deeper lavender emphasis |
| Mint | `#33c758` | Positive metric text when paired with Mint Wash |
| Mint Wash | `#def6e4` | Positive metric callout background |
| Amber | `#ffa600` | Performance feature category accent |
| Sky | `#2c78fc` | Realtime feature category accent, announcement chip, links |
| Magenta | `#d6409f` | Visitor profiles category and icon accent |
| Ember | `#ff3e00` | Chart fill and illustration accent only |

Gradient roles:

- Sky to Lavender: hero band behind dashboard mockup.
- Shimmer gray: skeleton loading state.
- Pale sky progression: chart fills.
- Pale sky to lavender: decorative or chart-adjacent accent.

## Typography

Primary type is OpenRunde. Fallbacks: Inter, DM Sans, Geist Sans, system-ui, sans-serif.

Rules:

- Use OpenRunde everywhere.
- Use weight 500 for headings and buttons.
- Use weight 600 for display and special emphasis.
- Use weight 400 for body and captions.
- Keep tracking negative across the scale.
- Display headline: 60px, weight 600, line-height 1.13, tracking -3px.
- Body: 16px, weight 400, line-height 1.5, tracking -0.32px.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 12px | 400 | 1.33 | -0.32px |
| Body | 16px | 400 | 1.5 | -0.32px |
| Subheading | 18px | 500 | 1.33 | -0.32px |
| Heading Small | 24px | 500 | 1.17 | -0.31px |
| Heading | 36px | 500 | 1.22 | -0.61px |
| Heading Large | 48px | 500 | 1.0 | -0.34px |
| Display | 60px | 600 | 1.13 | -3px |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max content width: 1200px.
- Section gap: 64px.
- Card padding: 32px.
- Element gap: 16px.
- Spacing values: 4, 8, 12, 16, 20, 24, 32, 48, 64.

Radius:

- Images: 8px.
- Inputs: 8px.
- Cards: 16px.
- Tables: 24px.
- Buttons, tags, and chips: 9999px.

## Elevation

Visitors is mostly flat.

- Use `1px solid #e8e8e8` for cards and tables.
- Primary CTA can have a small two-layer shadow.
- Dashboard panel can have a subtle three-layer stack.
- Do not use dramatic shadows or heavy lifts.

## Layout

- Full-width vertical sections with centered 1200px content.
- Hero is centered: announcement chip, display headline, subtext, dual CTA, partner logos.
- Follow hero with a full-width sky-to-lavender atmospheric band containing a floating dashboard mockup.
- Feature sections can use centered 3-column icon grids.
- Product sections can use alternating 2-column text and product layouts.
- Navigation is a centered floating pill bar.
- Footer is a minimal multi-column link grid.

## Imagery

Preferred imagery:

- Dashboard screenshots.
- Analytics cards, charts, tables, profile panels, and realtime lists.
- Grayscale partner logos.
- Flat single-color icons in 40px lavender circles.

Avoid:

- Lifestyle photography.
- People-focused imagery.
- Decorative images that do not show product or data.
- Heavy illustration systems.
- Colorful chrome without feature purpose.

## Motion

Motion should feel precise and lightweight.

- Use subtle hover and focus transitions.
- Avoid large-scale parallax or heavy easing.
- Dashboard cards should stay readable.
- Gradients are atmospheric bands, not animated button fills.

