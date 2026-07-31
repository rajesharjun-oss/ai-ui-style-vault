# Typography

### Haffer Variable - Primary display serif for headlines at 30-53px. Weight 450 is anti-convention - most product sites push display to 600-700, but Haffer at 450 keeps headlines warm and editorial rather than commanding. Activating liga and ss04 unlocks the alternative g and stylised letterforms that give the wordmark its personality. - `--font-haffer-variable`
- **Substitute:** Source Serif 4, Newsreader, or DM Serif Display
- **Weights:** 450
- **Sizes:** 24px, 30px, 45px, 53px
- **Line height:** 1.10
- **Letter spacing:** -0.02em
- **OpenType features:** `"liga" on, "ss04" on`
- **Role:** Primary display serif for headlines at 30-53px. Weight 450 is anti-convention - most product sites push display to 600-700, but Haffer at 450 keeps headlines warm and editorial rather than commanding. Activating liga and ss04 unlocks the alternative g and stylised letterforms that give the wordmark its personality.

### Bogue - Companion serif at regular weight, used for badge labels and secondary serif moments where Haffer 450 would feel too heavy. Tighter tracking at -0.03em distinguishes it from Haffer. - `--font-bogue`
- **Substitute:** Source Serif 4, Cormorant Garamond
- **Weights:** 400
- **Sizes:** 24px, 30px, 45px, 53px
- **Line height:** 1.10
- **Letter spacing:** -0.03em
- **Role:** Companion serif at regular weight, used for badge labels and secondary serif moments where Haffer 450 would feel too heavy. Tighter tracking at -0.03em distinguishes it from Haffer.

### Haffer - Static fallback for small serif text - 15px badges, 24px sub-serial moments - `--font-haffer`
- **Substitute:** Source Serif 4
- **Weights:** 400
- **Sizes:** 15px, 24px
- **Line height:** 1.20
- **Letter spacing:** -0.02em
- **OpenType features:** `"liga" on, "ss04" on`
- **Role:** Static fallback for small serif text - 15px badges, 24px sub-serial moments

### Inter - All UI, body, nav, button labels, helper text. Inter at 400 handles body, 600 carries subheadings and button text. The -0.02em tracking matches the serif family, keeping the type system visually unified. - `--font-inter`
- **Weights:** 400, 600
- **Sizes:** 12px, 15px, 24px, 30px, 45px
- **Line height:** 1.10, 1.20, 1.50
- **Letter spacing:** -0.02em
- **Role:** All UI, body, nav, button labels, helper text. Inter at 400 handles body, 600 carries subheadings and button text. The -0.02em tracking matches the serif family, keeping the type system visually unified.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.5 | -0.24px | `--text-caption` |
| body-sm | 15px | 1.5 | -0.3px | `--text-body-sm` |
| subheading | 24px | 1.2 | -0.48px | `--text-subheading` |
| heading-sm | 30px | 1.1 | -0.6px | `--text-heading-sm` |
| heading-lg | 45px | 1.1 | -0.9px | `--text-heading-lg` |
| display | 53px | 1.1 | -1.06px | `--text-display` |
