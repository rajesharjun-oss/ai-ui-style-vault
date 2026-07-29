# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-twk-lausanne` | TWK Lausanne | Inter, IBM Plex Sans, Sohne | Body, nav, labels, buttons, cards, most headings |
| `--font-moderat-serif` | Moderat Serif | GT Sectra, Tiempos Headline, Canela | Single largest display h1 |
| `--font-sf-mono` | SF Mono | JetBrains Mono, IBM Plex Mono | API references, code snippets, technical annotations |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 11px | 400 or 500 | 1.45 | -0.022px | `--text-caption` |
| Body | 14px | 400 | 1.57 | normal | `--text-body` |
| Body large | 16px | 400 | 1.63 | normal | `--text-body-lg` |
| Subheading | 18px | 400 or 500 | 1.56 | normal | `--text-subheading` |
| Heading small | 24px | 300 to 500 | 1.33 | -0.048px | `--text-heading-sm` |
| Heading | 40px | 300 | 1 | -1px | `--text-heading` |
| Display | 46px | 300 | 1 | -1.15px | `--text-display` |

## Rules

- Use TWK Lausanne for all interface text.
- Use lighter heading weights at 24px and above.
- Use Moderat Serif only for the largest h1.
- Do not use Moderat Serif below 40px.
- Use SF Mono only for machine-readable or code-adjacent content.
- Keep body text at 14px or above for normal copy.
