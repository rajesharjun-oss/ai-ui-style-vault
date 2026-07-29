# Typography

## Ivy Presto

- Token: `--font-ivy-presto`
- Fallback: Playfair Display, DM Serif Display, Libre Caslon Display
- Weights: 400, 500
- Sizes: 28px, 44px, 52px, 64px, 88px
- Line height: 1.0 to 1.38
- Letter spacing: 0.01em
- Role: display and heading serif at 28px and above.

## Inter

- Token: `--font-inter`
- Fallback: Inter
- Weights: 300, 400, 500, 600, 700
- Sizes: 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 48px
- Line height: 1.0 to 1.56
- Letter spacing: -0.04em to 0.01em
- Role: UI sans for body, nav, buttons, labels, forms, links, and tables.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Eyebrow | 13px | 1.00 | -0.26px | `--text-eyebrow` |
| Body XS | 16px | 1.50 | 0 | `--text-body-xs` |
| Body SM | 18px | 1.38 | -0.36px | `--text-body-sm` |
| Body | 20px | 1.38 | -0.8px | `--text-body` |
| Subheading | 24px | 1.00 | -0.31px | `--text-subheading` |
| Heading SM | 44px | 1.38 | 0.44px | `--text-heading-sm` |
| Heading | 52px | 1.13 | 0.52px | `--text-heading` |
| Heading LG | 64px | 1.13 | 0.64px | `--text-heading-lg` |
| Display | 88px | 1.00 | 0.88px | `--text-display` |

## Rules

- Use Ivy Presto only at 28px and above.
- Use Inter for all functional UI and body copy.
- Keep body copy at 16px Inter 400 with 1.5 line height in Bone.
- Do not set Inter body text larger than 20px.
