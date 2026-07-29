# Typography

## Family

- **Primary:** Sequel Sans
- **Fallback:** Inter, Manrope, DM Sans, ui-sans-serif, system-ui
- **Weights:** 400, 450, 500
- **Design behavior:** One geometric grotesque handles the whole system. Size, leading, and whitespace do the hierarchy work.

## Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 12px | 1.5 | 400 | 0.36px | `--text-caption` |
| body-sm | 14px | 1.4 | 400 | 0.42px | `--text-body-sm` |
| body | 16px | 1 | 400 | 0 | `--text-body` |
| subheading | 23px | 1.2 | 500 | 0.23px | `--text-subheading` |
| heading-sm | 33px | 1.2 | 500 | 0.33px | `--text-heading-sm` |
| heading | 44px | 1.2 | 500 | 0.44px | `--text-heading` |
| heading-lg | 72px | 1 | 500 | 0.72px | `--text-heading-lg` |
| display | 106px | 1 | 500 | 0 | `--text-display` |
| display-xl | 110px | 1 | 500 | 1.1px | `--text-display-xl` |
| display-hero | 155px | 0.9 | 500 | 1.55px | `--text-display-hero` |

## Rules

- Keep display sizes tight: 0.9-1.0 line-height.
- Keep display and heading tracking slightly positive, around 0.01em.
- Keep labels, nav, and buttons tracked around 0.03em.
- Do not use weights above 500.
- Do not add a serif, mono, or decorative secondary typeface.
- On mobile, step down display size responsively while preserving tight leading and editorial scale.

