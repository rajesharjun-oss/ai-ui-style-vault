# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-recoleta` | Recoleta | GT Super, Canela, Tiempos Headline | Display and heading text 36px and above |
| `--font-oldschool-grotesk` | Oldschool Grotesk | Sohne, Inter, Neue Haas Grotesk | UI, body, nav, cards, buttons |
| `--font-times-system-fallback` | Times system fallback | Times New Roman, Georgia | Rare annotations |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Body small | 15px | 300 or 400 | 1.6 | 0.15px | `--text-body-sm` |
| Body | 16px | 300 or 400 | 1.4 to 1.6 | -0.16px | `--text-body` |
| Body large | 21px | 300 | 1.3 | -0.42px | `--text-body-lg` |
| Subheading | 36px | 400 | 1.1 | -0.36px | `--text-subheading` |
| Heading small | 47px | 400 | 1.1 | -0.94px | `--text-heading-sm` |
| Heading | 61px | 400 | 1.1 | -1.22px | `--text-heading` |
| Heading large | 80px | 400 | 1 | -2.4px | `--text-heading-lg` |
| Display | 125px | 400 | 1 | -3.75px | `--text-display` |

## OpenType

Use common ligature settings on both display and primary text when available:

```css
font-feature-settings: "clig" 1, "liga" 1;
```

## Rules

- Serif display type starts at 36px.
- Do not use the serif display family for body copy.
- Tighten tracking more as heading size increases.
- Use Oldschool Grotesk weight 300 for descriptive copy.
- Use Oldschool Grotesk weight 400 for buttons, nav, and primary UI.
