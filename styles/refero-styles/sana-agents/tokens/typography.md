# Typography

## Fonts

- Sana Serif Hero display headline only. A weight-400 serif at 72px is the system's signature move: most AI brands shout with bold sans, Sana whispers with editorial type and lets the scale carry authority. The serif counterforms and bracket serifs give the wordmark a literary, humanist quality absent from typical product UI. `--font-sana-serif`
- Sana Sans All UI, body, navigation, buttons, and subheadings. The 450 weight is a distinctive mid-step between regular and medium used for button labels and nav links instead of jumping to 500, producing quieter emphasis. Tabular numerals (tnum) and lining figures (lnum) are always on, giving all numeric data a consistent grid. `--font-sana-sans`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 13px | 1.5 |  | `--text-caption` |
| body | 16px | 1.43 |  | `--text-body` |
| heading | 20px | 1.2 |  | `--text-heading` |
| display | 72px | 1.1 |  | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
