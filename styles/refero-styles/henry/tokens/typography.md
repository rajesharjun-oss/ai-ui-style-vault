# Typography

## Font Families

| Role | Font | Token | Fallback |
| --- | --- | --- | --- |
| UI and body | Neue Montreal | `--font-neue-montreal` | Inter, Sohne, General Sans, system-ui, sans-serif |
| Display serif | Louize Display | `--font-louize-display` | Fraunces, GT Sectra, Lyon Display, Georgia, serif |
| Short serif | Louize | `--font-louize` | Fraunces, GT Sectra, Georgia, serif |
| Masthead display | Manuka | `--font-manuka` | Druk, Condor, Antonio, Impact, sans-serif |

## Type Scale

| Role | Size | Weight | Line Height | Tracking | Token |
| --- | --- | --- | --- | --- | --- |
| caption | 12px | 400 or 700 | 1.5 | -0.12px | `--text-caption` |
| body | 16px | 400 | 1.5 | -0.16px | `--text-body` |
| subheading | 20px | 400 or 700 | 1.3 | -0.2px | `--text-subheading` |
| heading-sm | 24px | 400 | 1.2 | -0.24px | `--text-heading-sm` |
| heading | 32px | 400 | 1.1 | -0.32px | `--text-heading` |
| heading-lg | 77px | 400 | 0.9 | 0 | `--text-heading-lg` |
| display | 132px | 400 | 0.8 | 0 | `--text-display` |
| display-xl | 371px | 400 | 0.75 | 0 | `--text-display-xl` |

## Typography Rules

- Louize Display should define sections at 77px and above.
- Manuka is reserved for 226-371px masthead stamps.
- Neue Montreal carries nav, labels, metadata, and body.
- Keep UI/body tracking tight around -0.01em.
- Do not use display serif sizes for long body text.
- Do not center-align Neue Montreal body copy.

