# Typography

## Type System

Use Inter for functional UI text. Use Esbuild only for display moments.

## Fonts

| Font | Token | Substitutes | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| Inter | `--font-inter` | DM Sans, IBM Plex Sans | 300, 400, 500, 600, 700 | 10, 11, 12, 14, 15, 16, 18, 22, 24 | 1.00, 1.13, 1.25, 1.38, 1.50 | Tight at larger sizes, subtle compression for body | Body, nav, buttons, list items, captions, small headings. |
| Esbuild | `--font-esbuild` | Sora, General Sans | 400, 500, 600 | 28, 32, 80, 84 | 0.80, 0.90, 1.00 | `-0.05em` to `-0.02em` | Hero headlines, section openers, major feature titles. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `11px` | `1.38` | `-0.1px` | `--text-caption` |
| body | `14px` | `1.5` | `-0.14px` | `--text-body` |
| body-lg | `16px` | `1.5` | `-0.16px` | `--text-body-lg` |
| subheading | `18px` | `1.5` | `-0.36px` | `--text-subheading` |
| heading-sm | `22px` | `1.25` | normal | `--text-heading-sm` |
| heading | `24px` | `1.25` | `-0.48px` | `--text-heading` |
| display-sm | `32px` | `1` | `-1.6px` | `--text-display-sm` |
| display | `80px` | `0.9` | `-4px` | `--text-display` |

## Rules

- Body copy should usually be `14px`, `1.5` line-height, and `-0.14px` tracking.
- Increase tracking compression as display size increases.
- Reserve Esbuild for `28px` and up.
- Do not use Esbuild for body, nav, dense tables, or small UI controls.
- Keep functional text practical and readable; the editorial personality belongs in display moments.

