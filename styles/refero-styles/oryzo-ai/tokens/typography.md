# Typography

### halyard-display-variable - The only typeface. Weight 500 at 51px drives display headlines with extreme uppercase confidence; the same family at weight 400 / 29px becomes the system's sole mixed-case body voice. Letter-spacing stays normal - the geometric forms do the work without tightening. Substitute: 'Inter', 'Sohne', or 'Neue Haas Grotesk' for close structural match. - `--font-halyard-display-variable`
- **Substitute:** Inter or Sohne
- **Weights:** 400, 500
- **Sizes:** 8, 10, 12, 14, 15, 18, 24, 29, 41, 51px
- **Line height:** 0.90-1.26
- **Letter spacing:** normal across all sizes - no negative tracking even at display scale, the font's geometry handles visual weight without compression
- **OpenType features:** `"ss01" on`
- **Role:** The only typeface. Weight 500 at 51px drives display headlines with extreme uppercase confidence; the same family at weight 400 / 29px becomes the system's sole mixed-case body voice. Letter-spacing stays normal - the geometric forms do the work without tightening. Substitute: 'Inter', 'Sohne', or 'Neue Haas Grotesk' for close structural match.

### Arial - System fallback for micro-legal labels (8px uppercase credits like "* ADOBE ILLUSTRATOR"). Not a design choice - a necessity for system-rendered disclaimers. - `--font-arial`
- **Substitute:** system-ui
- **Weights:** 400, 500
- **Sizes:** 8px
- **Line height:** 1.20
- **Role:** System fallback for micro-legal labels (8px uppercase credits like "* ADOBE ILLUSTRATOR"). Not a design choice - a necessity for system-rendered disclaimers.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| subheading | 18px | 1 | - | `--text-subheading` |
| heading-sm | 24px | 1.09 | - | `--text-heading-sm` |
| body | 29px | 1.26 | - | `--text-body` |
| heading | 41px | 0.9 | - | `--text-heading` |
| display | 51px | 0.9 | - | `--text-display` |
