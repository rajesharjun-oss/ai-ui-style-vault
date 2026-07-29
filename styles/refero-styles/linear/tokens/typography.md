# Typography Tokens

## Fonts

| Font | Token | Role | Substitute |
| --- | --- | --- | --- |
| Inter Variable | `--font-inter-variable` | UI, body, nav, buttons, labels, headings. | Inter |
| Berkeley Mono | `--font-berkeley-mono` | Issue IDs, keyboard shortcuts, technical metadata, code-like labels. | SFMono-Regular |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Weight | Token |
| --- | --- | --- | --- | --- | --- |
| caption | `13px` | `1.2` | `0` | `400` | `--text-caption` |
| body-sm | `15px` | `1.6` | `-0.165px` | `400` | `--text-body-sm` |
| body-lg | `20px` | `1.33` | `-0.24px` | `400` | `--text-body-lg` |
| subheading | `24px` | `1.33` | `-0.288px` | `510` | `--text-subheading` |
| heading-sm | `32px` | `1.13` | `-0.704px` | `510` | `--text-heading-sm` |
| heading | `48px` | `1.0` | `-1.056px` | `510` | `--text-heading` |
| heading-lg | `64px` | `1.0` | `-1.408px` | `510` | `--text-heading-lg` |
| display | `72px` | `1.0` | `-1.584px` | `510` | `--text-display` |

## Font Rules

- Use Inter Variable for all ordinary UI and marketing text.
- Use Berkeley Mono only for technical metadata.
- Keep weights in the 400 to 510 range.
- Use tight tracking at large sizes.
- Do not use Berkeley Mono for headings or marketing copy.
