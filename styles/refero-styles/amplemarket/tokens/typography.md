# Typography

## Family

| Role | Preferred Font | Fallbacks | Notes |
|---|---|---|---|
| Whole system | Labil Grotesk Variable | Inter, DM Sans, General Sans Variable, Arial | Geometric grotesque for nav, body, buttons, cards, and headings |

## Scale

| Token | Size | Line Height | Weight | Tracking | Transform |
|---|---:|---:|---:|---:|---|
| `--text-eyebrow` | 10px | 1.0 | 500 | 0.3px | none |
| `--text-caption` | 12px | 1.0 | 400 | 0 | none |
| `--text-body-sm` | 14px | 1.3 | 400 | 0 | none |
| `--text-body` | 16px | 1.0 | 400 | 0 | none |
| `--text-body-lg` | 20px | 1.3 | 400 | -0.4px | none |
| `--text-subheading` | 28px | 1.1 | 400 | -0.476px | none |
| `--text-heading-sm` | 36px | 1.1 | 400 | -1.08px | none |
| `--text-heading` | 44px | 1.1 | 400 | -1.76px | none |
| `--text-heading-lg` | 56px | 1.0 | 400 | -2.8px | none |
| `--text-display` | 84px | 0.8 | 900 | -2.52px | uppercase |

## Rules

- Keep most headings at weight 400.
- Use weight 900 only for poster-scale uppercase display text.
- Let letter spacing become more negative as size increases.
- Keep body and normal UI text at zero tracking.
- Enable stylistic alternates `ss02` and `ss01` when available.
