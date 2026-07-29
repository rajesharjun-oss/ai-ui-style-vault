# Typography Tokens

## Fonts

| Font | Token | Role | Substitute |
| --- | --- | --- | --- |
| Sohne / Custom Grotesk | `--font-grotesk` | Primary interface and display type. | Inter, Geist, Space Grotesk |
| Sohne Mono / JetBrains Mono | `--font-mono` | SDK names, code snippets, technical labels. | IBM Plex Mono, Geist Mono |

## Type Scale

| Role | Size | Line Height | Weight | Token |
| --- | --- | --- | --- | --- |
| caption | `12px` | `1.5` | `400` | `--text-caption` |
| body-sm | `14px` | `1.5` | `400` | `--text-body-sm` |
| body | `16px` | `1.5` | `400` | `--text-body` |
| body-lg | `18px` | `1.6` | `400` | `--text-body-lg` |
| subheading | `20px` | `1.4` | `500` | `--text-subheading` |
| heading-sm | `24px` | `1.3` | `500` | `--text-heading-sm` |
| heading | `36px` | `1.2` | `500` | `--text-heading` |
| heading-lg | `66px` | `1.09` | `500` | `--text-heading-lg` |
| display | `100px` | `1.0` | `500` | `--text-display` |
| mega | `125px` | `1.0` | `500` | `--text-mega` |

## Font Rules

- Use weight 500 for headings and large display.
- Use body at 16px to 18px for dark readability.
- Use small uppercase labels with wide tracking around `0.129em` to `0.167em`.
- Use mono font only for SDKs, code, language tabs, and identifiers.
- Keep display line-height between 1.0 and 1.09.
