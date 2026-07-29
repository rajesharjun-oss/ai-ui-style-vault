# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-instrument-serif` | Instrument Serif | Playfair Display, EB Garamond, Cormorant Garamond | Italic headings, display text, ghost wordmark |
| `--font-dm-mono` | DM Mono | JetBrains Mono, IBM Plex Mono, Space Mono | Labels, tags, metadata, buttons, stamps |
| `--font-geist` | Geist | Inter, system-ui | Paragraphs and descriptions |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 10px | 400 | 1.4 | 0.21px | `--text-caption` |
| Mono label | 12px | 400 | 1.2 | 0.021em | `--text-mono-label` |
| Body | 17px | 400 | 1.4 | normal | `--text-body` |
| Subheading | 20px | 400 | 1.2 | -0.2px | `--text-subheading` |
| Heading small | 32px | 400 | 1.1 | 0.26px | `--text-heading-sm` |
| Heading | 48px | 400 | 1.1 | -1.44px | `--text-heading` |
| Heading large | 72px | 400 | 1 | -2.16px | `--text-heading-lg` |
| Display | 96px | 400 | 0.9 | -3.84px | `--text-display` |
| Wordmark | 393px to 403px | 400 | 1.1 to 1.4 | tight | `--text-wordmark` |

## Rules

- Use Instrument Serif italic for all major headings.
- Use Instrument Serif only when the text has enough scale to breathe.
- Use DM Mono for all system chrome and product labels.
- Use Geist for paragraph copy so the page remains readable.
- Tighten letter spacing at 48px and above.
- Keep wordmark text enormous and partially outside the viewport.
