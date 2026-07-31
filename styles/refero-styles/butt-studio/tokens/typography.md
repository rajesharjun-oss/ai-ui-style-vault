# Typography

### helvetica - Every utility, body, list, button, and link on the site. Stays at one weight - no bold, no medium. The decision to use weight 400 Helvetica at 20px for body (not 16px) is deliberate: text is meant to feel like printed matter, not a UI. Tighter letter-spacing on larger sizes (-0.03em) prevents the 40px from feeling airy. - `--font-helvetica`
- **Substitute:** Helvetica Neue, Inter, or Arial as system fallback
- **Weights:** 400
- **Sizes:** 20px body, 40px subhead
- **Line height:** 1.20
- **Letter spacing:** -0.03em at 20px, -0.02em at 40px
- **Role:** Every utility, body, list, button, and link on the site. Stays at one weight - no bold, no medium. The decision to use weight 400 Helvetica at 20px for body (not 16px) is deliberate: text is meant to feel like printed matter, not a UI. Tighter letter-spacing on larger sizes (-0.03em) prevents the 40px from feeling airy.

### Caslon - The hero wordmark and any serif accent. A single weight of a custom display serif - chosen because its high contrast strokes and ball terminals read as editorial print, not web type. This font IS the brand; everything else is scaffolding. - `--font-caslon`
- **Substitute:** Playfair Display, Cormorant Garamond, or any high-contrast didone/transitional serif
- **Weights:** 400
- **Sizes:** 42px display, scales up to fill the viewport at the wordmark level
- **Line height:** 1.00
- **Letter spacing:** -0.02em at display sizes, tightening to nearly none at body
- **Role:** The hero wordmark and any serif accent. A single weight of a custom display serif - chosen because its high contrast strokes and ball terminals read as editorial print, not web type. This font IS the brand; everything else is scaffolding.

### Sometimes Times - Sometimes Times - detected in extracted data but not described by AI - `--font-sometimes-times`
- **Weights:** 400
- **Sizes:** 20px
- **Line height:** 1.2
- **Letter spacing:** -0.02
- **Role:** Sometimes Times - detected in extracted data but not described by AI

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| body | 20px | 1.2 | -0.6px | `--text-body` |
| heading | 42px | 1 | -0.84px | `--text-heading` |
| display | 200px | 1 | -4px | `--text-display` |
