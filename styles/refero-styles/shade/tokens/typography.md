# Typography

### sans-serif - sans-serif - detected in extracted data but not described by AI - `--font-sans-serif`
- **Weights:** 400
- **Sizes:** 12px
- **Line height:** 1.2
- **Role:** sans-serif - detected in extracted data but not described by AI

### Inter Display - Primary typeface for all UI text, body and headings alike. Single weight 400 carries the entire hierarchy through size and tracking alone - no bold, no light. The custom stylistic sets (ss01, ss07, ss08) reshape the g, a, and l terminals into a more geometric, editorial silhouette that distinguishes it from stock Inter. - `--font-inter-display`
- **Substitute:** Inter
- **Weights:** 400
- **Sizes:** 10px, 14px, 16px, 18px, 20px, 21px, 24px, 28px, 32px, 36px, 40px, 48px, 56px, 72px
- **Line height:** 1.0-1.57 (size-dependent)
- **Letter spacing:** -0.01em to -0.03em (tighter as size increases: -0.01em at body, -0.03em at display)
- **OpenType features:** `"ss01", "ss07", "ss08", "cv03", "cv04", "cv09", "cv11", "blwf"`
- **Role:** Primary typeface for all UI text, body and headings alike. Single weight 400 carries the entire hierarchy through size and tracking alone - no bold, no light. The custom stylistic sets (ss01, ss07, ss08) reshape the g, a, and l terminals into a more geometric, editorial silhouette that distinguishes it from stock Inter.

### Aux Mono - Monospaced label font for section eyebrows (e.g. 'DAY 1', 'LET'S CHAT', nav items, badge text). Sets at 14px with -0.04em tracking gives timestamps and labels a technical, archival feel against the editorial display type. - `--font-aux-mono`
- **Substitute:** JetBrains Mono
- **Weights:** 400
- **Sizes:** 14px
- **Line height:** 1.29
- **Letter spacing:** -0.04em
- **Role:** Monospaced label font for section eyebrows (e.g. 'DAY 1', 'LET'S CHAT', nav items, badge text). Sets at 14px with -0.04em tracking gives timestamps and labels a technical, archival feel against the editorial display type.

### Inter - Secondary fallback / system-level utility text where the custom display features aren't required - `--font-inter`
- **Substitute:** system-ui
- **Weights:** 400, 500
- **Sizes:** 12px, 14px, 16px
- **Line height:** 1.2-1.5
- **Role:** Secondary fallback / system-level utility text where the custom display features aren't required

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.2 | -0.12px | `--text-caption` |
| body-sm | 14px | 1.29 | -0.14px | `--text-body-sm` |
| body | 16px | 1.5 | -0.16px | `--text-body` |
| subheading | 20px | 1.4 | -0.2px | `--text-subheading` |
| heading-sm | 24px | 1.3 | -0.24px | `--text-heading-sm` |
| heading | 32px | 1.22 | -0.96px | `--text-heading` |
| heading-lg | 48px | 1.15 | -1.44px | `--text-heading-lg` |
| display | 72px | 1.1 | -2.16px | `--text-display` |
