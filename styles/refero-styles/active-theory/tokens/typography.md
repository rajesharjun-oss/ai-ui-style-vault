# Typography Tokens

## Fonts

| Font | Token | Role | Substitute |
| --- | --- | --- | --- |
| nbarchitekt | `--font-nbarchitekt` | Navigation, buttons, micro-labels, link text, technical chrome. | Space Grotesk, Inter |
| Times | `--font-times` | Body copy, prose, card descriptions, editorial content. | Times New Roman, Georgia |
| Arial | `--font-arial` | Cookie consent and compliance micro-copy. | system sans |

## Type Scale

| Role | Size | Line Height | Weight | Token |
| --- | --- | --- | --- | --- |
| caption | `10px` | `3` | `400` | `--text-caption` |
| body-sm | `12px` | `1.5` | `400` | `--text-body-sm` |
| micro-ui | `13px` | `1.2` | `400` | `--text-micro-ui` |
| body | `14px` | `1.2` | `700` | `--text-body` |
| prose | `16px` | `1.88` | `400` | `--text-prose` |

## Font Rules

- Use nbarchitekt for chrome only.
- Use 10px to 12px nbarchitekt for nav and metadata.
- Use 14px nbarchitekt weight 700 for button labels.
- Use Times for body copy and descriptions.
- Do not set prose in the geometric UI sans.
- Keep letter spacing normal.
