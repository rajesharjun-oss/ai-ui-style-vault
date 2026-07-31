# Typography

### -apple-system - System-font fallback for body text and rendering across platforms. Used wherever native OS fonts provide a reliable, performance-optimized default at body size. - `--font-apple-system`
- **Substitute:** BlinkMacSystemFont, Segoe UI, Roboto, sans-serif
- **Weights:** 400
- **Sizes:** 16px
- **Line height:** 1.00
- **OpenType features:** `"dlig" 0, "hlig" 0, "liga" 0, "rlig" 0, "smcp" 0`
- **Role:** System-font fallback for body text and rendering across platforms. Used wherever native OS fonts provide a reliable, performance-optimized default at body size.

### Geist - Primary display and UI typeface. The 300 weight at micro sizes (8-10px) creates whisper-quiet labels; the negative letter-spacing (-0.056em at 8px, -0.037em at 10px) tightens small type into dense, confident blocks. 400 at 16-18px serves body and subheadings with -0.025em to -0.011em tracking. - `--font-geist`
- **Substitute:** Inter, Satoshi, General Sans
- **Weights:** 300, 400, 500
- **Sizes:** 8px, 10px, 16px, 18px
- **Line height:** 1.00, 1.17, 1.38, 2.67
- **Letter spacing:** -0.056em at 8px, -0.037em at 10px, -0.025em at 16px, -0.011em at 18px
- **OpenType features:** `"ss02", "lnum"`
- **Role:** Primary display and UI typeface. The 300 weight at micro sizes (8-10px) creates whisper-quiet labels; the negative letter-spacing (-0.056em at 8px, -0.037em at 10px) tightens small type into dense, confident blocks. 400 at 16-18px serves body and subheadings with -0.025em to -0.011em tracking.

### wtqc (custom display) - Reserved for prominent display headings (30px, 1.07 line-height, -0.033em tracking) and compact labels (12px, 1.33 line-height). The tight 1.07 line-height on the 30px size gives headings a condensed, editorial feel. - `--font-wtqc-custom-display`
- **Substitute:** Geist, Inter
- **Weights:** 500
- **Sizes:** 12px, 30px
- **Line height:** 1.07, 1.33
- **Letter spacing:** -0.033em at both sizes
- **OpenType features:** `"lnum"`
- **Role:** Reserved for prominent display headings (30px, 1.07 line-height, -0.033em tracking) and compact labels (12px, 1.33 line-height). The tight 1.07 line-height on the 30px size gives headings a condensed, editorial feel.

### custom_166638 - custom_166638 - detected in extracted data but not described by AI - `--font-custom166638`
- **Weights:** 300
- **Sizes:** 8px
- **Line height:** 1.5
- **OpenType features:** `"dlig" 0, "hlig" 0, "liga" 0, "rlig" 0, "smcp" 0`
- **Role:** custom_166638 - detected in extracted data but not described by AI

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption-sm | 10px | 1.17 | -0.37px | `--text-caption-sm` |
| body | 16px | 1.38 | -0.4px | `--text-body` |
| subheading | 18px | 2.67 | -0.2px | `--text-subheading` |
| heading | 30px | 1.07 | -0.99px | `--text-heading` |
