# Typography

### Inter - Entire UI - body, nav, headings, buttons, cards. Only two weights used (regular 400, medium 500) which is the core typographic discipline: no bold display weight, no light italic, just calm and confident Inter. The 13px/17px pair forms the dense product text; 40-60px carries the marketing voice. Headlines use -0.03em tracking to pull letters tight against the dark canvas. - `--font-inter`
- **Substitute:** system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif
- **Weights:** 400, 500
- **Sizes:** 13, 17, 27, 40, 53, 60
- **Line height:** 1.0, 1.2, 1.5
- **Letter spacing:** -0.0300em, -0.0100em
- **Role:** Entire UI - body, nav, headings, buttons, cards. Only two weights used (regular 400, medium 500) which is the core typographic discipline: no bold display weight, no light italic, just calm and confident Inter. The 13px/17px pair forms the dense product text; 40-60px carries the marketing voice. Headlines use -0.03em tracking to pull letters tight against the dark canvas.

### Inconsolata (custom-mapped eyebrow face) - Eyebrow labels, status pills, and small ALL CAPS markers like 'ASSEMBLY 15 NOW ORDINAL', 'SCHEDULING', 'WATCH A DEMO 4:15'. The monospace character at 13-17px is a deliberate break from Inter's proportions - signals 'metadata / system status / not body content'. 0.01em positive tracking on the eyebrow adds the ALL CAPS breath small caps need. - `--font-inconsolata-custom-mapped-eyebrow-face`
- **Substitute:** 'JetBrains Mono', 'IBM Plex Mono', 'Roboto Mono', monospace
- **Weights:** 400, 500
- **Sizes:** 13, 17
- **Line height:** 1.0, 1.5
- **Letter spacing:** 0.01em at eyebrow size; -0.01em at 17px body-mono
- **Role:** Eyebrow labels, status pills, and small ALL CAPS markers like 'ASSEMBLY 15 NOW ORDINAL', 'SCHEDULING', 'WATCH A DEMO 4:15'. The monospace character at 13-17px is a deliberate break from Inter's proportions - signals 'metadata / system status / not body content'. 0.01em positive tracking on the eyebrow adds the ALL CAPS breath small caps need.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 13px | 1.5 | -0.01px | `--text-caption` |
| body | 17px | 1.5 | -0.01px | `--text-body` |
| subheading | 27px | 1.2 | -0.27px | `--text-subheading` |
| heading | 40px | 1.2 | -0.4px | `--text-heading` |
| heading-lg | 53px | 1.2 | -1.59px | `--text-heading-lg` |
| display | 60px | 1 | -1.8px | `--text-display` |
