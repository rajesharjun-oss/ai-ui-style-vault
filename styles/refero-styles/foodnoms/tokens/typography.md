# Typography

## Fonts

- Aquawax Pro Medium Aquawax Pro Medium detected in extracted data but not described by AI `--font-aquawax-pro-medium`
- Aquawax Pro Primary brand typeface used across all display, heading, and body contexts. The custom face has a wide x-height, rounded geometric forms, and friendly proportions. Bold (700) is used for the 60px display and 30px section headlines these are the system's typographic anchors. DemiBold (600) handles subheadings and button labels at 1416px. Medium (500) carries body copy at 1720px with generous 1.61.8 line-height for comfortable reading. `--font-aquawax-pro`
- System sans-serif Fallback for very small UI text and icon labels. Aquawax Pro is not used at micro sizes; system font handles them to keep render weight low. `--font-system-sans-serif`
- Aquawax Pro DemiBold Aquawax Pro DemiBold detected in extracted data but not described by AI `--font-aquawax-pro-demibold`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| tiny | 12px | 1.2 |  | `--text-tiny` |
| caption | 14px | 1.2 |  | `--text-caption` |
| body-sm | 16px | 1.4 |  | `--text-body-sm` |
| subheading | 20px | 1.8 |  | `--text-subheading` |
| heading-sm | 22px | 1.2 |  | `--text-heading-sm` |
| heading | 30px | 1.2 |  | `--text-heading` |
| display | 60px | 1.2 |  | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
