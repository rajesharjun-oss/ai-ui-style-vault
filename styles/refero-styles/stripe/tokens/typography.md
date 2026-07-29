# Typography

## Families

| Family | Token | Fallback | Role |
|---|---|---|---|
| sohne-var | `--font-sohne-var` | Inter, system-ui, Helvetica Neue | Entire interface: headings, body, buttons, nav, and tables. |
| ui-monospace | `--font-mono` | SFMono-Regular, Menlo, Monaco, Consolas | Optional code snippets and terminal panels only. |

## Rules

- Use one main family across the system.
- Large headings use weight 300.
- Body copy uses weight 300 to 400.
- Buttons, nav actions, and table values can use weight 500.
- Do not introduce serif or decorative display fonts.
- Tighten tracking at large sizes and keep captions slightly open.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 13px | 1.54 | 0.2px | `--text-caption` |
| Body SM | 15px | 1.60 | 0 | `--text-body-sm` |
| Body | 16px | 1.56 | 0 | `--text-body` |
| Body LG | 17px | 1.73 | 0 | `--text-body-lg` |
| Heading SM | 24px | 1.25 | -0.24px | `--text-heading-sm` |
| Heading | 31px | 1.23 | -0.31px | `--text-heading` |
| Heading LG | 51px | 1.08 | -1.53px | `--text-heading-lg` |
| Display | 56px | 1.07 | -1.68px | `--text-display` |
| Display XL | 82px | 1.00 | -2.46px | `--text-display-xl` |
