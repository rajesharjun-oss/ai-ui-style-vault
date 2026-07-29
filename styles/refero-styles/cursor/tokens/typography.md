# Typography

## Families

| Family | Token | Fallback | Role |
|---|---|---|---|
| CursorGothic | `--font-cursorgothic` | Inter, system-ui, Helvetica Neue | Primary UI, headings, nav, body, product surfaces. |
| EB Garamond | `--font-eb-garamond` | Iowan Old Style, Palatino Linotype, ui-serif, Georgia | Editorial subheads, prose, and selected table content. |
| berkeleyMono | `--font-berkeleymono` | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas | Code, file paths, CLI snippets, tabs, metadata. |
| system-ui | `--font-system-ui` | system-ui, -apple-system, Helvetica Neue | Small labels only when a custom font is too heavy. |

## Rules

- Headings use CursorGothic at weight 400.
- Do not use weight 600 or 700 for display headings.
- Tighten tracking as heading size increases.
- EB Garamond should be rare and editorial.
- berkeleyMono should make technical content feel native.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Eyebrow | 12px | 1.63 | 0 | `--text-eyebrow` |
| Body SM | 14px | 1.50 | 0.14px | `--text-body-sm` |
| Body | 16px | 1.35 | 0 | `--text-body` |
| Editorial | 17px | 1.35 | 0 | `--text-editorial` |
| Editorial LG | 19px | 1.50 | 0 | `--text-editorial-lg` |
| Heading SM | 22px | 1.30 | -0.11px | `--text-heading-sm` |
| Heading | 26px | 1.25 | -0.312px | `--text-heading` |
| Heading LG | 36px | 1.20 | -0.72px | `--text-heading-lg` |
| Display | 72px | 1.10 | -2.16px | `--text-display` |
