# Typography

## Monument

- Token: `--font-monument`
- Fallback: Montserrat
- Weight: 400
- Sizes: 10px, 16px, 24px, 64px, 96px
- Line height: 1.00, 1.06, 1.24, 1.46, 1.50
- Letter spacing: negative at display sizes, especially around `-0.03em`
- Role: display headlines, navigation, and prominent textual elements.

## Mono

- Token: `--font-mono`
- Fallback: Space Mono
- Weight: 400
- Sizes: 10px, 12px, 14px
- Line height: 0.80, 1.00, 1.50
- Letter spacing: about `0.06em` for body/data and `0.16em` for tiny captions
- Role: body copy, descriptive labels, technical text, and code-like elements.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 10px | 0.80 | 0.16px | `--text-caption` |
| Body | 14px | 1.50 | 0.06px | `--text-body` |
| Heading | 24px | 1.24 | -0.01px | `--text-heading` |
| Heading LG | 64px | 1.46 | -0.03em | `--text-heading-lg` |
| Display | 96px | 1.50 | -0.03em | `--text-display` |

## Rules

- Keep type weight at 400.
- Use Monument for display/nav.
- Use Mono for body and labels.
- Preserve tracking; it is the character of the system.
