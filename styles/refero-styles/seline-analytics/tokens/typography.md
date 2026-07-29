# Typography

## Roobert

- **Role:** Display and heading typeface.
- **Fallback:** Inter Tight or Satoshi
- **Weights:** 400, 500
- **Sizes:** 18px, 20px, 32px, 52px
- **Line height:** 1.12, 1.22, 1.25, 1.69
- **Letter spacing:** -0.025em at 32px, -0.021em at 52px, -0.017em at 18px
- **Rule:** Use weight 400 for all display and headings.

## Inter

- **Role:** Body, nav, UI, captions, and dashboard labels.
- **Weights:** 400, 500, 600
- **Sizes:** 10px, 12px, 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.33, 1.53, 1.64, 1.69, 2.3
- **Letter spacing:** 0.003em, 0.004em, 0.025em

## Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 10px | 2.3 | 400 | 0 | `--text-caption` |
| body-sm | 14px | 1.64 | 400 | 0.056px | `--text-body-sm` |
| body-lg | 16px | 1.69 | 400 | 0.048px | `--text-body-lg` |
| subheading | 20px | 1.2 | 400 | -0.1px | `--text-subheading` |
| heading-sm | 32px | 1.25 | 400 | -0.8px | `--text-heading-sm` |
| display | 52px | 1.12 | 400 | -1.092px | `--text-display` |

## Rules

- Do not set headings in Inter.
- Do not use 600 or 700 weights for heading emphasis.
- Use cyan highlight spans instead of bold weight jumps.
- Keep body copy mostly 14px Inter with 1.64 line-height.

