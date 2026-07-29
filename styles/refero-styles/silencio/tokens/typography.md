# Typography

## Fonts

- HaasR Workhorse grotesque for body, subheadings, and mid-size headings. Weight 100 is used for restraint in body contexts; 700 sparingly for emphasis. The single most-used face carries the page. `--font-haasr`
- HaasT Display-only face at 141px with tightened leading (0.90). Used for hero statements and singular set-pieces the only moment typography shouts, and it shouts at full volume against pure white. `--font-haast`
- PT Mono Metadata, spec labels, catalog tags the typographic equivalent of a printed museum label. Appears at 11px only; functions as a quiet signature rather than informational copy. `--font-pt-mono`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| body | 16px | 1.4 |  | `--text-body` |
| subheading | 22px | 1.1 |  | `--text-subheading` |
| heading-sm | 39px | 1 |  | `--text-heading-sm` |
| heading | 58px | 0.9 |  | `--text-heading` |
| display | 141px | 0.9 |  | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
