# Typography

### Inter - Primary body and UI text. The 18px body size with 1.78 line-height creates a generous, editorial reading rhythm that contrasts the compact, tight display type. The 0.89 line-height variant handles single-line labels and metadata where vertical density matters. - `--font-inter`
- **Substitute:** Inter (Google Fonts) or Sohne at 400
- **Weights:** 400
- **Sizes:** 18px
- **Line height:** 1.78 (body) 0.89 (tight label)
- **Letter spacing:** normal
- **OpenType features:** `"dlig" 0, "hlig" 0, "liga" 0, "rlig" 0, "smcp" 0`
- **Role:** Primary body and UI text. The 18px body size with 1.78 line-height creates a generous, editorial reading rhythm that contrasts the compact, tight display type. The 0.89 line-height variant handles single-line labels and metadata where vertical density matters.

### wtqc - Signature display and heading face. The massive 197px/72px/28px scale at weight 300 with tight tracking (-0.033em -0.014em) creates the poster-art identity. At 300 weight, headlines whisper rather than shout - authority through scale and restraint, not boldness. The lighter weight prevents the enormous letterforms from feeling heavy or aggressive. - `--font-wtqc`
- **Substitute:** Inter Tight at weight 300, or Sohne Breit at 300 as a free alternative
- **Weights:** 300, 400
- **Sizes:** 12px, 28px, 72px, 197px
- **Line height:** 1.00 (display) 1.33 (caption)
- **Letter spacing:** -0.033em at 197px, -0.021em at 72px, -0.014em at 28px, -0.003em at 12px
- **OpenType features:** `default ligatures only`
- **Role:** Signature display and heading face. The massive 197px/72px/28px scale at weight 300 with tight tracking (-0.033em -0.014em) creates the poster-art identity. At 300 weight, headlines whisper rather than shout - authority through scale and restraint, not boldness. The lighter weight prevents the enormous letterforms from feeling heavy or aggressive.

### System UI (-apple-system) - Tertiary fallback for cards, metadata blocks, and system-level UI that doesn't carry brand typographic weight - `--font-system-ui-apple-system`
- **Weights:** 400
- **Sizes:** 16px
- **Line height:** 1.00
- **Role:** Tertiary fallback for cards, metadata blocks, and system-level UI that doesn't carry brand typographic weight

### -apple-system - -apple-system - detected in extracted data but not described by AI - `--font-apple-system`
- **Weights:** 400
- **Sizes:** 16px
- **Line height:** 1
- **OpenType features:** `"dlig" 0, "hlig" 0, "liga" 0, "rlig" 0, "smcp" 0`
- **Role:** -apple-system - detected in extracted data but not described by AI

### Roboto - Roboto - detected in extracted data but not described by AI - `--font-roboto`
- **Weights:** 400
- **Sizes:** 12px
- **Line height:** 1.33
- **OpenType features:** `"dlig" 0, "hlig" 0, "liga" 0, "rlig" 0, "smcp" 0`
- **Role:** Roboto - detected in extracted data but not described by AI

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.33 | -0.04px | `--text-caption` |
| body-sm | 16px | 1.5 | - | `--text-body-sm` |
| body | 18px | 1.78 | - | `--text-body` |
| subheading | 28px | 1.29 | -0.39px | `--text-subheading` |
| heading | 72px | 1.04 | -1.51px | `--text-heading` |
| display | 197px | 1 | -6.5px | `--text-display` |
