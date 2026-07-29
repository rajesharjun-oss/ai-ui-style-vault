# Typography

## Fonts

- Pragmatica Cond Primary display and UI typeface narrow condensed uppercase at 14px for body, 20px for section labels, 32px for hero wordmark. The extreme narrowness and all-caps setting at 14px body size is the system's most signature choice: body text reads as a whisper of architectural type, not conventional prose. Substitute with Oswald or Barlow Condensed if Pragmatica Cond is unavailable. `--font-pragmatica-cond`
- Pragmatica Secondary body typeface used for longer-form prose passages (e.g. the 'AI Operating System' card description at 24px, paragraph text at 15px). Slightly wider than Pragmatica Cond for reading comfort in extended blocks, but still 400 weight no bold ever. Substitute with Inter or Shne. `--font-pragmatica`
- Roboto Mono Monospace micro-type for the top news bar ticker ('NEWS JUN 15, 2026 CRUCIBLE EARLY ACCESS IS NOW OPEN'). The only place monospace appears, creating a clear functional distinction: this is system data, not brand voice. `--font-roboto-mono`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 11px | 1.1 | -0.22px | `--text-caption` |
| body-sm | 14px | 1.43 | -0.28px | `--text-body-sm` |
| heading-sm | 20px | 1 | -0.4px | `--text-heading-sm` |
| heading | 24px | 1.2 | -0.48px | `--text-heading` |
| heading-lg | 32px | 1.05 | -0.64px | `--text-heading-lg` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
