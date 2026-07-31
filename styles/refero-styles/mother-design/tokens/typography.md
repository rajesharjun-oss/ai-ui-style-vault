# Typography

### Basis - Primary typeface across all UI. Weight 400 for body, links, and most running text; weight 600 used sparingly for the small uppercase-ish labels and the navigation tabs. The 226px size at 1.0 line-height is the signature - display type behaves like a poster headline, not a web heading. Negative tracking tightens as size grows: -0.04em at display, -0.02em at mid, -0.01em at body. - `--font-basis`
- **Substitute:** Inter, Suisse Int'l, or Neue Haas Grotesk
- **Weights:** 400, 600
- **Sizes:** 10, 14, 16, 48, 60, 110, 226
- **Line height:** 1.00-1.50 (context-dependent: 1.0 for display, 1.5 for body)
- **Letter spacing:** -0.04em at 226px, -0.04em at 110px, -0.02em at 60px, -0.02em at 48px, -0.01em at 16px, 0 at 14px and below
- **Role:** Primary typeface across all UI. Weight 400 for body, links, and most running text; weight 600 used sparingly for the small uppercase-ish labels and the navigation tabs. The 226px size at 1.0 line-height is the signature - display type behaves like a poster headline, not a web heading. Negative tracking tightens as size grows: -0.04em at display, -0.02em at mid, -0.01em at body.

### Basis Mono - Used for technical labels, metadata, timestamps, and small annotations. The +0.06em letter-spacing gives it the feel of a printed caption set in a typewriter face - a deliberate counterpoint to Basis's tight grotesque. - `--font-basis-mono`
- **Substitute:** JetBrains Mono, IBM Plex Mono, or Berkeley Mono
- **Weights:** 400
- **Sizes:** 14
- **Line height:** 1.20
- **Letter spacing:** 0.06em (8.4px at 14px)
- **Role:** Used for technical labels, metadata, timestamps, and small annotations. The +0.06em letter-spacing gives it the feel of a printed caption set in a typewriter face - a deliberate counterpoint to Basis's tight grotesque.

### Times - System serif used as a rare editorial accent - appears in icon and small body contexts where a note of 'newspaper' or 'footnotes' is wanted. Its presence is felt more than seen; the choice signals print lineage rather than decoration. - `--font-times`
- **Substitute:** Times New Roman, EB Garamond, or Source Serif
- **Weights:** 400
- **Sizes:** 14
- **Line height:** 1.20
- **Letter spacing:** 0.06em
- **Role:** System serif used as a rare editorial accent - appears in icon and small body contexts where a note of 'newspaper' or 'footnotes' is wanted. Its presence is felt more than seen; the choice signals print lineage rather than decoration.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 10px | 1.2 | - | `--text-caption` |
| body-sm | 14px | 1.2 | - | `--text-body-sm` |
| body | 16px | 1.5 | -0.16px | `--text-body` |
| heading-sm | 48px | 1.1 | -0.96px | `--text-heading-sm` |
| heading | 60px | 1 | -1.2px | `--text-heading` |
| heading-lg | 110px | 1 | -4.4px | `--text-heading-lg` |
| display | 226px | 1 | -9.04px | `--text-display` |
