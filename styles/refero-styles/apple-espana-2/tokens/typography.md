# Typography

## Fonts

- SF Pro Display Hero headlines, section headings, and the page-level brand statement. Set in semibold at very large sizes (6496px) with aggressive negative tracking (-0.019em to -0.005em) that tightens the headline into a single confident block. Smaller sizes (2128px) carry section headings and card titles. The signature choice: weight 600 is the heaviest weight on the entire site Apple trusts display weight 600 over 700+ to command the page `--font-sf-pro-display`
- SF Pro Text Body copy, nav labels, button text, spec text, and large display numerals (44px). Weight 400 is the paragraph default; weight 600 marks links, button labels, and emphasis within body text. The 44px instance is a display-numeral role used for prices or large data it borrows SF Pro Text rather than Display because the data needs to feel tabular, not editorial `--font-sf-pro-text`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 1.33 | -0.036px | `--text-caption` |
| body-sm | 14px | 1.43 | -0.14px | `--text-body-sm` |
| body | 17px | 1.47 | -0.272px | `--text-body` |
| subheading | 21px | 1.33 | 0.231px | `--text-subheading` |
| heading-sm | 28px | 1.14 | -0.252px | `--text-heading-sm` |
| heading | 39px | 1.07 | -0.351px | `--text-heading` |
| heading-lg | 64px | 1.06 | -0.96px | `--text-heading-lg` |
| display | 96px | 1.04 | -1.824px | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
