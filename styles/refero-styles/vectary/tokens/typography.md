# Typography

### Inter - Single-family system: weight 400 for body and UI labels, weight 700 for section headings and button text, weight 900 reserved for display headlines (83px). The dramatic jump from 26px to 83px creates a two-tier hierarchy - page-heading-class copy lives at 22-26px, and only true hero moments reach 83px. Negative letter-spacing tightens with size: -0.012em at 14px scaling linearly to -0.039em at 83px, so display text optically squares up while small text stays crisp. - `--font-inter`
- **Substitute:** system-ui, -apple-system, 'Segoe UI', sans-serif
- **Weights:** 400, 700, 900
- **Sizes:** 14, 16, 18, 22, 26, 83px
- **Line height:** 1.00-1.69
- **Letter spacing:** -0.17px at 14px, -0.30px at 16px, -0.45px at 18px, -0.66px at 22px, -0.88px at 26px, -3.24px at 83px
- **OpenType features:** `"ss01" on, "cv11" on`
- **Role:** Single-family system: weight 400 for body and UI labels, weight 700 for section headings and button text, weight 900 reserved for display headlines (83px). The dramatic jump from 26px to 83px creates a two-tier hierarchy - page-heading-class copy lives at 22-26px, and only true hero moments reach 83px. Negative letter-spacing tightens with size: -0.012em at 14px scaling linearly to -0.039em at 83px, so display text optically squares up while small text stays crisp.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 14px | 1.69 | -0.17px | `--text-caption` |
| body-sm | 16px | 1.5 | -0.3px | `--text-body-sm` |
| body | 18px | 1.4 | -0.45px | `--text-body` |
| subheading | 22px | 1.3 | -0.66px | `--text-subheading` |
| heading | 26px | 1.09 | -0.88px | `--text-heading` |
| display | 83px | 1 | -3.24px | `--text-display` |
