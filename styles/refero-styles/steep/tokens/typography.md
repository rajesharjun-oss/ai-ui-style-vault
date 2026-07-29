# Typography

## Type System

Use a restrained editorial serif for large display headings and a precise sans for everything else.
The signature is regular-weight serif headlines paired with fine-grained sans weights.

## Fonts

| Font | Token | Substitutes | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| Signifier | `--font-signifier` | GT Sectra, Tiempos Headline, Source Serif 4, Georgia | 400 | 44px, 64px, 90px | 1.30 | Tight negative tracking | Display and H1/H2 headline serif. |
| Sohne | `--font-sohne` | Inter, ui-sans-serif, system-ui | 400, 430, 450, 480, 500 | 14px to 26px | 1.00 to 1.50 | Subtle negative tracking at larger sizes | Body, UI, navigation, buttons, cards, metadata. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `15px` | `1.5` | normal | `--text-caption` |
| body | `17px` | `1.35` | normal | `--text-body` |
| body-lg | `20px` | `1.35` | normal | `--text-body-lg` |
| subheading | `22px` | `1.5` | normal | `--text-subheading` |
| heading-sm | `26px` | `1.18` | `-0.23px` | `--text-heading-sm` |
| heading | `44px` | `1.3` | `-0.66px` | `--text-heading` |
| heading-lg | `64px` | `1.3` | `-0.96px` | `--text-heading-lg` |
| display | `90px` | `1.3` | `-2.25px` | `--text-display` |

## Rules

- Use Signifier weight `400` for all display and headline copy.
- Do not use Signifier bold or semibold.
- Use Sohne-style half-step weights (`430`, `450`, `480`) before jumping to `500`.
- Use tighter tracking as type gets larger.
- Keep display type editorial and calm, not loud or heavy.
- Use sans for all product UI, metadata, nav, buttons, and card text.

