# Typography

## Fonts

- gigaSansText Body text, buttons, navigation, links the workhorse. Weight 400 for paragraphs, 500 for button labels and emphasis. 16px at 1.5 line-height is the readable default; 14px at 1.43 handles dense UI chrome. `--font-gigasanstext`
- emilioDisplay Display headlines the signature voice. Ultra-light weight at 48-66px with tight -0.02em to -0.03em tracking creates a film-title-card feel. Most enterprise brands shout with 700-weight headlines; Giga whispers with 300, which is the entire personality in one choice. `--font-emiliodisplay`
- gigaSansDisplay Section subheadings, feature card titles, prominent UI labels bridges the gap between whisper-thin display and body text. Weight 500 at 22px carries mid-importance statements. `--font-gigasansdisplay`
- interText Large numerical and functional headings 44px with -0.03em tracking for stat callouts and mid-level headings. Acts as a contrast voice to the emilioDisplay serif displays. `--font-intertext`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 2 |  | `--text-caption` |
| body-sm | 14px | 1.43 |  | `--text-body-sm` |
| body | 16px | 1.5 |  | `--text-body` |
| subheading | 22px | 1.5 |  | `--text-subheading` |
| heading-sm | 30px | 1.33 |  | `--text-heading-sm` |
| heading | 48px | 1.3 | -0.96px | `--text-heading` |
| heading-lg | 60px | 1.2 | -1.8px | `--text-heading-lg` |
| display | 66px | 1.2 | -1.98px | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
