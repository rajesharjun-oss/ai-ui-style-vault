# Typography Tokens

## Fonts

| Font | Token | Role | Substitute |
| --- | --- | --- | --- |
| NotionInter | `--font-notioninter` | Primary sans for UI, body, nav, cards, and display headings. | Inter |
| Lyon Text | `--font-lyon-text` | Editorial serif for select intros and literary body moments. | Source Serif Pro |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Weight | Token |
| --- | --- | --- | --- | --- | --- |
| caption | `12px` | `1.33` | `0.12px` | `400` | `--text-caption` |
| body-sm | `14px` | `1.43` | `0` | `400` | `--text-body-sm` |
| body | `16px` | `1.5` | `0` | `400` | `--text-body` |
| subheading | `20px` | `1` | `0` | `400` | `--text-subheading` |
| heading-sm | `22px` | `1.27` | `-0.242px` | `700` | `--text-heading-sm` |
| heading | `40px` | `1.5` | `0` | `400` | `--text-heading` |
| heading-lg | `48px` | `1.5` | `0` | `400` | `--text-heading-lg` |
| display-sm | `54px` | `1.04` | `-1.89px` | `700` | `--text-display-sm` |
| display | `72px` | `1.21` | `-2.016px` | `500` | `--text-display` |
| display-lg | `96px` | `1.04` | `-4.608px` | `600` | `--text-display-lg` |

## Font Rules

- Use NotionInter or Inter for most of the system.
- Use 500 for nav and compact UI text.
- Use 600 to 700 for high-impact headlines.
- Tighten tracking on display sizes only.
- Keep body text at normal tracking.
- Use Lyon Text sparingly at `18px` or `32px`; do not use it for nav, buttons, or labels.
