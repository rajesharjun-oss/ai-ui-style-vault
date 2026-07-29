# Typography

## Families

| Family | Token | Role |
|---|---|---|
| FrameGothic | `--font-framegothic` | Primary brand typeface for display, body, nav, buttons, cards, and UI |
| NeueMachinaInktrap | `--font-neuemachinainktrap` | Uppercase stamped eyebrow labels only |
| Arial | `--font-arial` | System fallback and embedded product mockup UI text |
| Times | `--font-times` | Detected by Refero, but not part of the main implementation voice |

## Substitutes

- FrameGothic substitute: Inter, Neue Haas Grotesk, Space Grotesk, or Helvetica Neue.
- NeueMachinaInktrap substitute: Space Mono or IBM Plex Mono.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | `12px` | `1.45` | `0.72px` | `--text-caption` |
| Body Small | `14px` | `1.5` | `0` | `--text-body-sm` |
| Body | `16px` | `1.45` | `0.16px` | `--text-body` |
| Subheading | `18px` | `1.3` | `0` | `--text-subheading` |
| Heading Small | `24px` | `1.25` | `-0.72px` | `--text-heading-sm` |
| Heading | `38px` | `1.04` | `-1.33px` | `--text-heading` |
| Heading Large | `48px` | `1.02` | `-1.92px` | `--text-heading-lg` |
| Display | `80px` | `0.96` | `-3.6px` | `--text-display` |

## Rules

- Display headings should use weight 400, not 600 or 700.
- Letter spacing gets tighter as type gets larger.
- Eyebrow labels use NeueMachinaInktrap at 12px, uppercase, 0.06em tracking, and line-height 0.90.
- Do not use the eyebrow style for badges, buttons, or product labels.

