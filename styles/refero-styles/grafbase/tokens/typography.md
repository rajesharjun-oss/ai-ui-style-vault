# Typography

### Inter - Sole typeface. Display uses weight 600 at 90px with -0.05em tracking (about -4.5px) - headline authority through geometric compression rather than heaviness. Headings at 40px use weight 500 with -0.025em tracking for a slightly looser, more editorial register. Body at 16px stays at weight 400 with normal tracking. The 13/14px sizes handle UI chrome and captions. No system fonts, no second family - Inter is the brand. - `--font-inter`
- **Substitute:** Inter (self-hosted or Google Fonts) - no substitute should change identity
- **Weights:** 400, 500, 600, 700
- **Sizes:** 13, 14, 16, 20, 24, 40, 90
- **Line height:** 1.00, 1.10, 1.43, 1.50, 2.00
- **Letter spacing:** -0.0500em, -0.0250em
- **Role:** Sole typeface. Display uses weight 600 at 90px with -0.05em tracking (about -4.5px) - headline authority through geometric compression rather than heaviness. Headings at 40px use weight 500 with -0.025em tracking for a slightly looser, more editorial register. Body at 16px stays at weight 400 with normal tracking. The 13/14px sizes handle UI chrome and captions. No system fonts, no second family - Inter is the brand.

### sans (custom utility) - Rare fallback utility class. Treat as Inter - likely a Tailwind 'sans' alias that resolved to a custom stack. Do not introduce as a distinct type family in output. - `--font-sans-custom-utility`
- **Weights:** 400, 500
- **Sizes:** 14, 16
- **Line height:** 1.43, 1.50
- **Role:** Rare fallback utility class. Treat as Inter - likely a Tailwind 'sans' alias that resolved to a custom stack. Do not introduce as a distinct type family in output.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 13px | 1.5 | - | `--text-caption` |
| body | 16px | 1.5 | - | `--text-body` |
| subheading | 20px | 1.5 | - | `--text-subheading` |
| heading-sm | 24px | 1.43 | - | `--text-heading-sm` |
| heading | 40px | 1.1 | -1px | `--text-heading` |
| display | 90px | 1 | -4.5px | `--text-display` |
