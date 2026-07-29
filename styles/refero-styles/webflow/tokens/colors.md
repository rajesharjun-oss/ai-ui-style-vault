# Colors

## Palette

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Webflow Blue | `#146ef5` | `--color-webflow-blue` | Primary buttons, active nav, links, emphasis |
| Indigo Ink | `#1366e2` | `--color-indigo-ink` | Secondary blue and dark-surface emphasis |
| Canvas White | `#ffffff` | `--color-canvas-white` | Page background and card surface |
| Ink Black | `#080808` | `--color-ink-black` | Primary text and inverted surfaces |
| Border Gray | `#d8d8d8` | `--color-border-gray` | 1px borders and structural rules |
| Muted Text | `#5a5a5a` | `--color-muted-text` | Supporting text and monochrome logos |
| Mercury Tint | `#f0f0f0` | `--color-mercury-tint` | Alternating bands and subtle backgrounds |
| Soft Blue | `#6ca7ff` | `--color-soft-blue` | Inline illustration detail only |
| Mint Pulse | `#60ed76` | `--color-mint-pulse` | Inline illustration detail only |
| Orange Marker | `#ffa666` | `--color-orange-marker` | Inline illustration detail only |

## Color Behavior

Webflow is not a rainbow SaaS palette. It is a black, white, gray, and blue product system.

Use `#146ef5` for:

- Filled primary actions.
- Active nav states.
- Text links.
- New or selected badges.
- The most important product emphasis.

Use `#d8d8d8` for:

- Card borders.
- Input borders.
- Section structure.
- Browser frame lines.

Use green and orange only inside small inline illustrations. They should not become status colors, button colors, or navigation states.

## Surface Stack

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas | `#ffffff` | Primary page background |
| 1 | Tinted | `#f0f0f0` | Alternating bands and subtle differentiation |
| 2 | Card | `#ffffff` | Cards on tinted or canvas backgrounds |
| 3 | Inverted | `#080808` | Footer, dark callout, or dark product section |

## Forbidden Color Moves

- No extra UI accent colors.
- No colored customer logos.
- No blue-on-dark hover state unless contrast is handled with white or `#146ef2`.
- No pastel gradient hero.
- No green or orange primary buttons.

