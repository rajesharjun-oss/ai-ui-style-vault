# Typography

## Davinci

- **Role:** Display serif for wordmarks, section titles, and editorial moments.
- **Fallback:** Canela, Tiempos Headline, GT Super, Playfair Display
- **Weights:** 400, 500
- **Sizes:** 16, 24, 34, 52, 94, 374px
- **Line height:** 0.84, 1.00, 1.10, 1.33, 1.50
- **Letter spacing:** -0.0090em, -0.0050em, -0.0010em
- **Rule:** Use at 52px and above for primary display moments; avoid normal body use.

## Helvetica Now

- **Role:** Utility grotesk for nav, labels, stats, body, buttons, and captions.
- **Fallback:** Inter, Neue Haas Grotesk, Sohne, Helvetica Neue
- **Weights:** 400, 500
- **Sizes:** 9, 12, 15, 16, 22, 24, 26, 43px
- **Line height:** 1.25, 1.50
- **Rule:** Keep it functional and small; never let it take display duty.

## Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| micro | 9px | 1.25 | 400 | 0 | `--text-micro` |
| body-sm | 15px | 1.5 | 400 | 0 | `--text-body-sm` |
| body | 16px | 1.5 | 400 | 0 | `--text-body` |
| subheading | 22px | 1.33 | 400 | -0.11px | `--text-subheading` |
| heading-sm | 26px | 1.33 | 400 | -0.13px | `--text-heading-sm` |
| heading | 43px | 1.1 | 400 | -0.215px | `--text-heading` |
| heading-lg | 52px | 1 | 500 | -0.47px | `--text-heading-lg` |
| section-display | 94px | 0.84 | 500 | -0.85px | `--text-section-display` |
| display | 374px | 0.84 | 500 | -3.37px | `--text-display` |

## Rules

- Use size and tracking for drama.
- Let the 374px wordmark crop at viewport edges.
- Keep display line-height tight at 0.84.
- Keep utility text between 9px and 26px most of the time.

