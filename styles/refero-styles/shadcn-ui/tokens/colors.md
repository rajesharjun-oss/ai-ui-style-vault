# Color Tokens

## Core

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ink | `#09090b` | `--color-ink` | Primary text, primary button fill, highest contrast UI. |
| Canvas | `#ffffff` | `--color-canvas` | Page background, cards, input surfaces. |
| Panel | `#fafafa` | `--color-panel` | Subtle raised panel and control hover surface. |
| Muted Surface | `#f4f4f5` | `--color-muted-surface` | Recessed areas, disabled controls, code and preview backgrounds. |
| Border | `#e4e4e7` | `--color-border` | Card, input, table, and divider hairlines. |

## Text

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Foreground | `#09090b` | `--color-foreground` | Main text and active icons. |
| Muted Foreground | `#71717b` | `--color-muted-foreground` | Secondary text, descriptions, placeholder copy. |
| Subtle Foreground | `#a1a1aa` | `--color-subtle-foreground` | Disabled copy, quiet labels, helper details. |
| Inverse | `#ffffff` | `--color-inverse` | Text on dark buttons and dark surfaces. |

## State

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Destructive | `#e7000b` | `--color-destructive` | Error states, destructive buttons, danger icons. |
| Destructive Soft | `#ffe2e2` | `--color-destructive-soft` | Error background and destructive hover state. |

## Rules

- Use grayscale for normal interface hierarchy.
- Use `#e7000b` only for destructive and error moments.
- Do not add decorative accent colors.
- Use alpha black only for shadows and subtle overlays.
