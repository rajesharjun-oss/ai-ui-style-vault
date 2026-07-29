# Typography

## Fonts

- ABCDiatypeExpanded-Bold Display, brand logo, section headings, project titles, and nav labels. The extremely wide expanded letterforms (letter-spacing -0.02em at 7882px) are the signature element uppercase, never set small under 10px, and reserved for moments that demand visual weight. The 7882px sizes fill the full width of the hero canvas. Weight stays at 400 because the expansion provides all the weight needed; going bolder would distort the geometric proportions. `--font-abcdiatypeexpanded-bold`
- Grit-Regular All body copy, paragraph text, descriptions, and mid-weight headings. A contemporary serif with subtle texture provides editorial gravitas against the expanded display sans. Weight 400 for running text, 500 for emphasized phrases and sub-headings. The 56px size with 1.25 line-height creates dramatic editorial pull-quotes. Pairs with ABCDiatypeExpanded by contrasting serif warmth against geometric coldness. `--font-grit-regular`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 10px | 1.2 |  | `--text-caption` |
| body-sm | 14px | 1.43 |  | `--text-body-sm` |
| body | 16px | 1.5 |  | `--text-body` |
| subheading | 20px | 1.25 |  | `--text-subheading` |
| heading | 30px | 1.2 |  | `--text-heading` |
| heading-lg | 40px | 1.15 | -0.4px | `--text-heading-lg` |
| display | 56px | 1.25 | -0.56px | `--text-display` |
| hero | 80px | 1.1 | -1.6px | `--text-hero` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
