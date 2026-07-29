# Typography

## Type System

Use Geist for almost all interface text. Use Geist Mono for labels, metrics, status tags, code-like
surfaces, column headers, and terminal/instrument voices.

## Fonts

| Font | Token | Substitutes | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| Geist | `--font-geist` | Inter, system-ui | 400, 500 | 12, 14, 16, 36, 44, 72 | 1.0 to 1.5 | Tight negative tracking at large sizes | Body, headings, buttons, nav, hero, and most UI text. |
| Geist Mono | `--font-geist-mono` | JetBrains Mono, IBM Plex Mono, ui-monospace | 400 | 12, 14, 16 | 1.0 to 1.2 | `-0.0200em` | Uppercase labels, captions, status tags, metric units, and technical headers. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `12px` | `1` | `-0.24px` | `--text-caption` |
| body-sm | `14px` | `1.43` | normal | `--text-body-sm` |
| body | `16px` | `1.5` | normal | `--text-body` |
| heading | `36px` | `1.1` | `-1.12px` | `--text-heading` |
| heading-lg | `44px` | `1.12` | `-1.1px` | `--text-heading-lg` |
| display | `72px` | `1` | `-2.88px` | `--text-display` |

## Rules

- Use weight `400` by default.
- Use weight `500` sparingly for dense labels, footer headings, or key CTAs.
- Do not use weight `600+` for headings.
- Apply tighter negative tracking as type gets larger.
- Keep line-height at or below `1.5`.
- Do not introduce serif fonts or separate display families.
- Mono text should usually be uppercase and compact.

