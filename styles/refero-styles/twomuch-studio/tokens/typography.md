# Typography

## Fonts

- ABCMonumentGrotesk Sole typeface across all UI body, labels, nav, headings, buttons, icons, links. The single medium weight with uniformly negative tracking (~-0.48px) gives every label a compressed, display-poster feel regardless of size. Avoid pairing with a secondary face; the constraint IS the identity. `--font-abcmonumentgrotesk`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 0.9 | -0.48px | `--text-caption` |
| body-sm | 14px | 1 | -0.476px | `--text-body-sm` |
| body | 16px | 1.05 | -0.48px | `--text-body` |
| subheading | 18px | 1.33 | -0.486px | `--text-subheading` |
| heading-sm | 20px | 1.33 | -0.48px | `--text-heading-sm` |
| heading | 22px | 1.43 | -0.528px | `--text-heading` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
