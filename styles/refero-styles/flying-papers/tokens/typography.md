# Typography

## Font Roles

| Font | Role | Weights | Sizes |
| --- | --- | --- | --- |
| ObviouslyVariable | Display and giant headings | 800, 900 | 18px to 341px |
| DegularVariable | Tiny neutral UI copy | 400 | 10px |
| bergen_monoregular | Mono micro-copy, labels, tags | 400, 600 | 12px, 14px |
| DegularDisplay-Bold | CTA labels and emphasized micro-copy | 700 | 16px |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 10px | 400 | 1 | normal | `--text-caption` |
| Body | 16px | 700 | 1 | 0.8px | `--text-body` |
| Body Large | 18px | 800 | 0.9 | 0.36px | `--text-body-lg` |
| Subheading | 30px | 800 | 0.9 | 0.6px | `--text-subheading` |
| Heading Small | 100px | 900 | 0.9 | 2px | `--text-heading-sm` |
| Heading | 149px | 900 | 0.85 | 2.98px | `--text-heading` |
| Heading Large | 184px | 900 | 0.85 | 3.68px | `--text-heading-lg` |
| Display | 341px | 900 | 0.8 | 6.82px | `--text-display` |

## Typography Rules

- Use display type at poster scale.
- Keep display leading extremely tight.
- Use 0.02em tracking for large headline settings.
- Disable contextual alternates with `font-feature-settings: "calt" 0;`.
- Use Bergen Mono for small labels and disclaimers.
- Use DegularDisplay-Bold for compact action labels.
- Do not use ObviouslyVariable below 18px or above 341px.
