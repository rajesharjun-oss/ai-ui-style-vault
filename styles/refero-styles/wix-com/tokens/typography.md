# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-madefor-display` | madefor-display | Inter, DM Sans, Space Grotesk | Large headlines and display text |
| `--font-madefor-text` | madefor-text | Inter, IBM Plex Sans, Noto Sans | Body, nav, list items, descriptions, inputs |
| `--font-arial` | Arial | system-ui, Arial | Tiny utility and icon labels |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 13px | 400 | 1.2 | -0.13px | `--text-caption` |
| Body | 16px | 400 | 1.5 | -0.16px | `--text-body` |
| Subheading | 21px | 400 | 1.3 | -0.21px | `--text-subheading` |
| Heading small | 31px | 400 | 1.2 | -0.62px | `--text-heading-sm` |
| Heading | 48px | 400 | 1.1 | -0.96px | `--text-heading` |
| Heading large | 82px | 400 | 1 | -2.46px | `--text-heading-lg` |
| Display | 104px | 400 | 0.95 | -3.12px | `--text-display` |
| Hero super display | 184px | 400 | 0.85 to 1.3 | -0.03em | `--text-super-display` |

## Rules

- Use Madefor Display at 48px to 104px for major headlines.
- Tighten display tracking as size increases.
- Keep headline line-height tight at 48px and above.
- Use Madefor Text for reading copy and product UI.
- Use Arial only for very small utility contexts.
- Do not add serif or mono voices.
