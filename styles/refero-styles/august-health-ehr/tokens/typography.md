# Typography

## Fonts

- Reckless Neue All headings and display text. A contemporary editorial serif used exclusively at weight 400 (regular) no bold. This is anti-convention: most healthtech brands use sans-serif or bold serifs; the regular-weight serif at large sizes creates a literary, trustworthy quality without shouting. Largest sizes (48-64px) anchor section headlines, while 24-32px serves subheadings. `--font-reckless-neue`
- Saans Body text, UI controls, navigation, buttons, cards, labels, and everything non-headline. Weight 400 for body and descriptions, weight 500 for buttons and nav links where slight emphasis is needed. The geometric humanist sans provides clarity and warmth at small sizes, contrasting the editorial serif headings. `--font-saans`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 1.6 |  | `--text-caption` |
| body-sm | 14px | 1.4 |  | `--text-body-sm` |
| body | 16px | 1.6 |  | `--text-body` |
| subheading | 20px | 1.3 |  | `--text-subheading` |
| heading-sm | 24px | 1.3 |  | `--text-heading-sm` |
| heading | 32px | 1.1 |  | `--text-heading` |
| heading-lg | 48px | 1.1 |  | `--text-heading-lg` |
| display | 64px | 1 |  | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
