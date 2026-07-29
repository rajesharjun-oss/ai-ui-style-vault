# Typography

## Euclid Circular A

- Token: `--font-euclid-circular-a`
- Fallback: Inter, DM Sans, Space Grotesk
- Weights: 300, 400, 500, 700
- Sizes: 12px, 14px, 15px, 16px, 18px, 20px, 22px, 28px, 36px, 48px, 68px, 72px
- Role: sole UI typeface for headlines, navigation, body, buttons, cards, and labels.

Large text compresses with negative tracking. Small labels breathe with slight positive tracking.

## Onsite SemiMono

- Token: `--font-onsite-semimono`
- Fallback: JetBrains Mono, IBM Plex Mono, Geist Mono
- Weight: 400
- Sizes: 12px and 16px
- Line height: 1.48 and 1.60
- Letter spacing: 0.01em
- Role: counts, metrics, IDs, code-like labels, and technical micro-copy.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.48 | 0.12px | `--text-caption` |
| Body SM | 14px | 1.42 | 0.14px | `--text-body-sm` |
| Body | 16px | 1.50 | -0.16px | `--text-body` |
| Subheading | 20px | 1.34 | -0.40px | `--text-subheading` |
| Heading SM | 28px | 1.20 | -0.56px | `--text-heading-sm` |
| Heading | 36px | 1.16 | -1.08px | `--text-heading` |
| Heading LG | 48px | 1.10 | -1.92px | `--text-heading-lg` |
| Display | 68px | 1.04 | -4.08px | `--text-display` |

## Rules

- Use 300 weight for display headlines.
- Do not use 600 or 700 for display headlines.
- Use 500 for nav, tabs, buttons, and compact labels.
- Use 400 for body text.
- Use SemiMono only for data and technical details.
