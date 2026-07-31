# Typography

### Kinfolk-Serif-Text - Long-form body copy, captions, and article decks at 20px (lead paragraphs) and 15px (body). Normal letter-spacing lets the text breathe at reading size; the elevated line-height (1.5 at 15px) gives prose an airier, more literary rhythm than typical web body text. - `--font-kinfolk-serif-text`
- **Substitute:** Cormorant Garamond, Lora
- **Weights:** 400
- **Sizes:** 15px, 20px
- **Line height:** 1.25-1.50
- **Letter spacing:** normal
- **Role:** Long-form body copy, captions, and article decks at 20px (lead paragraphs) and 15px (body). Normal letter-spacing lets the text breathe at reading size; the elevated line-height (1.5 at 15px) gives prose an airier, more literary rhythm than typical web body text.

### Kinfolk-Serif-Display - Hero and feature headlines (60px, lh 1.0, tracking -0.025em / -1.5px). The tight tracking on a single 400 weight produces compressed, almost carved letterforms - authority through restraint, not volume. Used sparingly for the largest editorial moments. - `--font-kinfolk-serif-display`
- **Substitute:** Playfair Display, Cormorant Garamond
- **Weights:** 400
- **Sizes:** 20px
- **Line height:** 1.00
- **Letter spacing:** -0.025em
- **OpenType features:** `"liga" on, "dlig" on`
- **Role:** Hero and feature headlines (60px, lh 1.0, tracking -0.025em / -1.5px). The tight tracking on a single 400 weight produces compressed, almost carved letterforms - authority through restraint, not volume. Used sparingly for the largest editorial moments.

### Kinfolk-Serif-Deck - Section titles, article headlines, and deck/sub-deck lines at 50/32/25px. Same 400-only discipline as the display face but at intermediate optical sizes. Tracking is still negative at the top end (-0.5px at 50px) for that dense editorial feel. - `--font-kinfolk-serif-deck`
- **Substitute:** Cormorant Garamond, EB Garamond
- **Weights:** 400
- **Sizes:** 25px, 32px, 50px, 60px
- **Line height:** 1.04-1.19
- **Letter spacing:** -0.01em to -0.005em
- **Role:** Section titles, article headlines, and deck/sub-deck lines at 50/32/25px. Same 400-only discipline as the display face but at intermediate optical sizes. Tracking is still negative at the top end (-0.5px at 50px) for that dense editorial feel.

### Kinfolk-Sans - UI chrome, metadata, category labels, navigation, button text, and small functional text. Tracking opens up dramatically at the small end (0.06em / ~0.78px at 13px) - a common editorial convention that makes all-caps metadata read as labels rather than body. One weight only, with scale doing all the differentiation. - `--font-kinfolk-sans`
- **Substitute:** Inter, Sohne, GT America Standard
- **Weights:** 400
- **Sizes:** 13px, 15px, 16px, 20px, 25px
- **Line height:** 1.16-1.50
- **Letter spacing:** 0.01em to 0.06em (widens at smaller sizes)
- **Role:** UI chrome, metadata, category labels, navigation, button text, and small functional text. Tracking opens up dramatically at the small end (0.06em / ~0.78px at 13px) - a common editorial convention that makes all-caps metadata read as labels rather than body. One weight only, with scale doing all the differentiation.

### Arial - Arial - detected in extracted data but not described by AI - `--font-arial`
- **Weights:** 400
- **Sizes:** 13px
- **Line height:** 1.2
- **Role:** Arial - detected in extracted data but not described by AI

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 13px | 1.2 | 0.78px | `--text-caption` |
| body-sm | 15px | 1.5 | - | `--text-body-sm` |
| subheading | 20px | 1.33 | - | `--text-subheading` |
| heading-sm | 25px | 1.19 | 0.25px | `--text-heading-sm` |
| heading | 32px | 1.16 | -0.32px | `--text-heading` |
| heading-lg | 50px | 1.04 | -0.5px | `--text-heading-lg` |
| display | 60px | 1 | -1.5px | `--text-display` |
