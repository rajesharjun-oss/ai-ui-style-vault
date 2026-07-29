# Typography

## SuisseIntlCond

- Token: `--font-suisseintlcond`
- Fallback: Anton, Bebas Neue, Barlow Condensed Bold
- Weight: 700
- Sizes: 48px, 64px, 80px, 130px
- Line height: 0.90
- Letter spacing: -0.03em
- Role: massive uppercase condensed display headings.

## SuisseIntl

- Token: `--font-suisseintl`
- Fallback: Inter, Sohne, Neue Haas Grotesk
- Weights: 400, 450, 500
- Sizes: 14px, 16px, 18px, 20px, 28px, 40px
- Role: body, nav, subheads, buttons, cards, and secondary headings.

## SuisseIntlMono

- Token: `--font-suisseintlmono`
- Fallback: JetBrains Mono, IBM Plex Mono, Geist Mono
- Weight: 400
- Size: 12px
- Role: labels, tags, technical metadata, and numbered annotations.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.60 | -0.36px | `--text-caption` |
| Body SM | 14px | 1.30 | -0.154px | `--text-body-sm` |
| Body | 16px | 1.25 | 0 | `--text-body` |
| Subheading | 18px | 1.33 | 0 | `--text-subheading` |
| Subheading LG | 20px | 1.20 | 0 | `--text-subheading-lg` |
| Heading SM | 28px | 1.30 | -0.84px | `--text-heading-sm` |
| Heading | 40px | 1.10 | -0.8px | `--text-heading` |
| Heading LG | 48px | 0.90 | -1.44px | `--text-heading-lg` |
| Display | 80px | 0.90 | -2.4px | `--text-display` |
| Display XL | 130px | 0.90 | -3.9px | `--text-display-xl` |

## Rules

- All display headings are uppercase.
- Never set display heading line-height above 0.95.
- Do not use SuisseIntlCond below 48px.
- Use 16px/500 SuisseIntl for body and buttons.
