# Typography

## Fonts

- Teodor Display and editorial headlines, brand statements, section titles. Custom serif with sharp contrast between thick and thin strokes; at 90px with 0.75 leading it creates a magazine-cover authority that is the signature typographic gesture of the site. Subheading scale at 24px carries the same character into smaller contexts. `--font-teodor`
- Inter Body copy, UI labels, navigation, buttons, captions. The weight 300 default across most sizes keeps the interface quiet against the display serif the contrast between Teodor's editorial presence and Inter's whisper-light functional text is a defining rhythm of the system. `--font-inter`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 1.5 |  | `--text-caption` |
| body-sm | 16px | 1.5 |  | `--text-body-sm` |
| body | 20px | 1.3 |  | `--text-body` |
| subheading | 24px | 1.5 |  | `--text-subheading` |
| heading-sm | 28px | 1.3 |  | `--text-heading-sm` |
| heading | 35px | 1 |  | `--text-heading` |
| heading-lg | 55px | 1 |  | `--text-heading-lg` |
| display | 90px | 0.75 |  | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
