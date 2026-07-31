# Typography

### Aeonik - Primary typeface for all display, heading, and body text. Weight 300 at 75-90px with line-heights near 0.90-1.00 creates the system's signature sculptural headlines - letterforms lock together through aggressive negative tracking (-0.053em) rather than spacing. Mid-weight 400-500 handles body and UI at 19-20px with 1.45-1.70 line-height for generous readability. - `--font-aeonik`
- **Substitute:** Inter, Neue Haas Grotesk, or Suisse Int'l
- **Weights:** 300, 400, 500
- **Sizes:** 13, 14, 19, 20, 27, 30, 35, 75, 90
- **Line height:** 0.90, 1.00, 1.11, 1.16, 1.45, 1.48, 1.70, 2.23
- **Letter spacing:** -0.0530em at 75-90px, -0.0200em at 35px, -0.0100em at 27-30px, 0.0100em at 19-20px, 0.0200em at 13px, normal at 14px
- **Role:** Primary typeface for all display, heading, and body text. Weight 300 at 75-90px with line-heights near 0.90-1.00 creates the system's signature sculptural headlines - letterforms lock together through aggressive negative tracking (-0.053em) rather than spacing. Mid-weight 400-500 handles body and UI at 19-20px with 1.45-1.70 line-height for generous readability.

### -apple-system - System fallback for nav items, footer micro-copy, and supporting UI text where the custom Aeonik isn't loaded. Carries no distinctive role - purely a graceful degradation layer. - `--font-apple-system`
- **Substitute:** system-ui, BlinkMacSystemFont, 'Segoe UI'
- **Weights:** 400
- **Sizes:** 14, 28, 30
- **Line height:** 1.50, 1.70
- **Role:** System fallback for nav items, footer micro-copy, and supporting UI text where the custom Aeonik isn't loaded. Carries no distinctive role - purely a graceful degradation layer.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 13px | 1.7 | 0.26px | `--text-caption` |
| subheading | 20px | 1.45 | 0.2px | `--text-subheading` |
| heading-sm | 27px | 1.16 | -0.27px | `--text-heading-sm` |
| heading | 30px | 1.11 | -0.3px | `--text-heading` |
| heading-lg | 35px | 1.11 | -0.7px | `--text-heading-lg` |
| display | 75px | 1 | -3.98px | `--text-display` |
| display-xl | 90px | 0.9 | -4.77px | `--text-display-xl` |
