# Typography

## Fonts

- ES Allianz Primary typeface for all UI text a high-contrast didone-influenced serif used at dramatic display sizes (74152px) for headlines, and at body sizes (1619px) for running text. The tight letter-spacing (-0.045em at display, -0.02em at body) tightens the serifs into a modern editorial stance. Weight 400 carries most copy; 700 for hero impact; 500 for navigation and subheadings. This serif does the heavy lifting that a sans-serif system would spread across three families. `--font-es-allianz`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 14px | 1.2 | -0.28px | `--text-caption` |
| body-sm | 16px | 1.4 | -0.32px | `--text-body-sm` |
| subheading | 19px | 1.2 | -0.38px | `--text-subheading` |
| heading-sm | 28px | 1.2 | -0.56px | `--text-heading-sm` |
| heading | 46px | 1.1 | -1.84px | `--text-heading` |
| heading-lg | 64px | 1.1 | -2.56px | `--text-heading-lg` |
| display | 74px | 1 | -3.33px | `--text-display` |
| display-xl | 152px | 0.85 | -6.84px | `--text-display-xl` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
