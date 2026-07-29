# Typography

## Type System

Use an editorial serif for headings and a monospace for every functional string. This pairing is the
core identity: the serif announces; the mono instructs.

## Fonts

| Font | Token | Substitutes | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| ABC Diatype Mono | `--font-abc-diatype-mono` | JetBrains Mono, IBM Plex Mono, Space Mono | 400, 500 | 12px, 14px, 16px, 18px, 20px, 28px | 1.0 to 1.35 | Tight negative tracking | Body copy, navigation, buttons, badges, tags, and all UI strings. |
| Untitled Serif | `--font-untitled-serif` | Times New Roman, Georgia, editorial serif | 400 | 24px, 32px, 40px, 48px, 80px | 1.2 | `-0.02em` at all sizes | Display headings, section titles, feature card titles, and FAQ questions. |
| Untitled Sans | `--font-untitled-sans` | system-ui | 400 | 16px | 1.35 | `-0.02em` | Rare fallback/supporting sans detected in source. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `12px` | `1.2` | `-0.4px` | `--text-caption` |
| body-sm | `14px` | `1.35` | `-0.28px` | `--text-body-sm` |
| body | `16px` | `1.35` | `-0.4px` | `--text-body` |
| label | `18px` | `1.2` | `-0.4px` | `--text-label` |
| body-lg | `20px` | `1.35` | `-0.4px` | `--text-body-lg` |
| subheading | `24px` | `1.2` | `-0.48px` | `--text-subheading` |
| heading-sm | `32px` | `1.2` | `-0.64px` | `--text-heading-sm` |
| heading | `40px` | `1.2` | `-0.8px` | `--text-heading` |
| heading-lg | `48px` | `1.2` | `-0.96px` | `--text-heading-lg` |
| display | `80px` | `1.2` | `-1.6px` | `--text-display` |

## Rules

- Use Untitled Serif weight `400` for all headings.
- Never use bold or `600+` heading weights.
- Use ABC Diatype Mono for body, buttons, nav, tags, badges, and UI text.
- Use uppercase plus tight tracking for nav labels, buttons, and tags.
- Use mono weight `500` only for emphasized UI labels.
- Do not substitute a normal sans for body copy; the mono body is the brand voice.

