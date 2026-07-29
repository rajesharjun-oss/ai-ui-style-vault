# Spacing And Shape

## Spacing

| Purpose | Value |
|---|---:|
| Density | compact |
| Base unit | `4px` |
| Max width | `1280px` |
| Section gap | `80px` to `120px` |
| Card padding | `24px` to `32px` |
| Element gap | `8px` |

## Spacing Scale

| Name | Value | Token |
|---|---:|---|
| 4 | `4px` | `--spacing-4` |
| 8 | `8px` | `--spacing-8` |
| 12 | `12px` | `--spacing-12` |
| 16 | `16px` | `--spacing-16` |
| 24 | `24px` | `--spacing-24` |
| 32 | `32px` | `--spacing-32` |
| 76 | `76px` | `--spacing-76` |
| 100 | `100px` | `--spacing-100` |

## Border Radius

| Element | Value | Token |
|---|---:|---|
| nav | `0px` | `--radius-nav` |
| cards | `24px` | `--radius-cards` |
| links | `0px` | `--radius-links` |
| badges | `0px` | `--radius-badges` |
| filled buttons | `8px bottom-only` | `--radius-button-filled-bottom` |
| outlined buttons | `12px` | `--radius-button-outlined` |

## Elevation

- **Cards:** no shadow; use surface tone shift.
- **Buttons:** no shadow; identity comes from fill color and bottom-corner treatment.
- **Navigation:** no shadow; flat on the parchment surface.

## Shape Rules

- Card surfaces use `24px` radius.
- Text links and badges have no container radius.
- Filled ivory buttons use sharp top corners and rounded bottom corners.
- Outlined dark buttons use `12px` radius.
- Avoid generic pills unless adapting for accessibility or platform constraints.

