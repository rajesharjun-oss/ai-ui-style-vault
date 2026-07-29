# Typography

## Type System

Use a PPNeueMontreal-like geometric sans for all text. The signature move is huge weight-400 display
type paired with very light 18px body copy. Hierarchy comes from scale and tracking rather than boldness.

## Font

| Font | Token | Substitute | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| PPNeueMontreal | `--font-ppneuemontreal` | Inter | 200, 400, 600, 700 | 12, 14, 15, 18, 24, 27, 36, 42, 48, 78, 113 | 0.81 to 1.50 | tight display tracking, positive nav tracking | All UI text, headlines, body, nav, labels, and buttons. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `12px` | `1.5` | normal | `--text-caption` |
| nav-label | `14px` | `1.2` | `0.35px` | `--text-nav-label` |
| body | `18px` | `1.5` | normal | `--text-body` |
| heading-2xs | `24px` | `1.25` | `-0.48px` | `--text-heading-2xs` |
| heading-xs | `27px` | `1` | normal | `--text-heading-xs` |
| subheading | `36px` | `1.2` | normal | `--text-subheading` |
| heading-sm | `42px` | `1.2` | `-1.68px` | `--text-heading-sm` |
| heading | `48px` | `1.1` | `-1.68px` | `--text-heading` |
| heading-lg | `78px` | `1.1` | `-3.12px` | `--text-heading-lg` |
| display | `113px` | `1.1` | `-4.52px` | `--text-display` |

## Rules

- Use weight `400` for all major headings.
- Use weight `200` for 18px body copy.
- Use weight `600` for uppercase nav labels and small action labels.
- Avoid bold headings; the style relies on scale.
- Apply tight negative tracking on display sizes, especially 42px and above.
- Use OpenType feature `"ss01"` where available.
- If PPNeueMontreal is unavailable, use Inter but preserve the weight and tracking logic.

