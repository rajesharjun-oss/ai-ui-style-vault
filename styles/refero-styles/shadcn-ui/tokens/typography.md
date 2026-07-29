# Typography Tokens

## Fonts

| Font | Token | Role | Substitute |
| --- | --- | --- | --- |
| Geist Sans | `--font-geist-sans` | UI, body, nav, labels, headings, buttons. | Inter |
| Geist Mono | `--font-geist-mono` | Code, keyboard shortcuts, token labels, CLI snippets. | JetBrains Mono |

## Type Scale

| Role | Size | Line Height | Weight | Token |
| --- | --- | --- | --- | --- |
| caption | `12px` | `16px` / `1.33` | `400` | `--text-caption` |
| body-sm | `14px` | `20px` / `1.43` | `400` | `--text-body-sm` |
| body | `16px` | `24px` / `1.5` | `400` | `--text-body` |
| subheading | `18px` | `28px` / `1.56` | `500` | `--text-subheading` |
| heading-sm | `24px` | `32px` / `1.33` | `600` | `--text-heading-sm` |
| heading | `30px` | `36px` / `1.2` | `600` | `--text-heading` |
| heading-lg | `36px` | `40px` / `1.11` | `600` | `--text-heading-lg` |
| display | `48px` | `48px` / `1.0` | `700` | `--text-display` |

## Font Rules

- Use Geist Sans as the default font.
- Use Geist Mono only where text is technical or code-like.
- Keep UI text compact.
- Use medium weight for actions and nav.
- Use semibold or bold only for headings and primary hierarchy.
- Keep letter spacing normal.
