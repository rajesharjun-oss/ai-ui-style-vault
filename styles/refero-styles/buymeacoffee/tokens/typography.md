# Typography

## Fonts

- ui-sans-serif ui-sans-serif detected in extracted data but not described by AI `--font-ui-sans-serif`
- Circular Bold Display and hero headlines Circular Bold at 96px with -0.042em letter-spacing carries the 'Fund your creative work' headline; the extreme size and tight tracking make the wordmark feel monumental. Also used for button labels and emphasized short-form copy. `--font-circular-bold`
- Circular Medium Subheadings, card titles, and emphasis within body copy the bridge weight between Bold displays and Regular body, used where hierarchy needs weight without volume `--font-circular-medium`
- Circular Regular Body copy, descriptions, conversational text the workhorse weight for everything from supporter messages to card body descriptions, with a 16px baseline for body text `--font-circular-regular`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 10px | 1.2 |  | `--text-caption` |
| body | 14px | 1.5 |  | `--text-body` |
| body-lg | 16px | 1.5 | -0.34px | `--text-body-lg` |
| subheading | 20px | 1.2 | -0.6px | `--text-subheading` |
| heading-sm | 24px | 1.17 | -0.5px | `--text-heading-sm` |
| heading | 30px | 1.25 | -0.63px | `--text-heading` |
| heading-lg | 40px | 1.2 | -1.24px | `--text-heading-lg` |
| display | 64px | 1 | -2.7px | `--text-display` |
| hero | 96px | 0.99 | -4px | `--text-hero` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
