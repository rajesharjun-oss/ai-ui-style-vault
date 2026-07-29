# Typography

## Type System

Use a single Cosmica-like geometric sans for every typographic role. Display text becomes authoritative
through weight and scale; body and UI text stay compact and efficient.

## Font

| Font | Token | Substitute | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| Cosmica | `--font-cosmica` | DM Sans | 300, 400, 500, 600, 700 | 10, 12, 13, 14, 15, 16, 18, 20, 32, 40, 56, 64 | 1.0 to 1.8 | normal | Single-family system for display, body, nav, buttons, badges, metadata, and all UI text. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `12px` | `1.64` | normal | `--text-caption` |
| body | `15px` | `1.45` | normal | `--text-body` |
| body-lg | `18px` | `1.45` | normal | `--text-body-lg` |
| subheading | `20px` | `1.5` | normal | `--text-subheading` |
| heading-sm | `32px` | `1.5` | normal | `--text-heading-sm` |
| heading | `40px` | `1.28` | normal | `--text-heading` |
| heading-lg | `56px` | `1.28` | normal | `--text-heading-lg` |
| display | `64px` | `1.12` | normal | `--text-display` |

## Rules

- Use weight `600` for display headings.
- Do not set display headings below weight `600`.
- Use weight `600` to `700` for section headings.
- Use weight `400` for body and UI text.
- Keep body text compact around `14px` to `15px`.
- Do not introduce a second type family.
- Keep letter spacing normal.

