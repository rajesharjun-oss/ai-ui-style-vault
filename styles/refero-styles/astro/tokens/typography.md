# Typography

### ui-sans-serif - Body and UI text - system stack fallback. Weight 400 for body copy, 500/600 for button labels and nav, 700 for subheadings. Line-height 1.65 at 14px keeps dense UI readable without feeling airy. - `--font-ui-sans-serif`
- **Substitute:** Inter, system-ui
- **Weights:** 300, 400, 500, 600, 700
- **Sizes:** 14px, 16px, 20px
- **Line height:** 1.40, 1.50, 1.65, 1.81
- **Letter spacing:** normal
- **OpenType features:** `"calt", "zero"`
- **Role:** Body and UI text - system stack fallback. Weight 400 for body copy, 500/600 for button labels and nav, 700 for subheadings. Line-height 1.65 at 14px keeps dense UI readable without feeling airy.

### Obviously - Display and headline face - the custom workhorse. Weight 300/400 used for the largest headlines, 700 for the hero. The cv09 and salt alternates give it a distinctive wide, slightly retro character; ss06 and ss11 add quirky details. No web-safe substitute captures the feel - Inter Black or Space Grotesk Bold approximate it. - `--font-obviously`
- **Substitute:** Space Grotesk, Inter
- **Weights:** 300, 400, 700
- **Sizes:** 20px, 30px, 36px, 48px
- **Line height:** 1.10, 1.11, 1.20, 1.40
- **Letter spacing:** normal
- **OpenType features:** `"calt", "cv09", "liga", "salt", "ss06", "ss11"`
- **Role:** Display and headline face - the custom workhorse. Weight 300/400 used for the largest headlines, 700 for the hero. The cv09 and salt alternates give it a distinctive wide, slightly retro character; ss06 and ss11 add quirky details. No web-safe substitute captures the feel - Inter Black or Space Grotesk Bold approximate it.

### ui-monospace - Code blocks, terminal commands, and inline code. Fixed 14px with generous 1.65 line-height for readability of multi-line snippets. - `--font-ui-monospace`
- **Substitute:** JetBrains Mono, Fira Code
- **Weights:** 300, 400
- **Sizes:** 14px
- **Line height:** 1.65
- **OpenType features:** `"calt", "zero"`
- **Role:** Code blocks, terminal commands, and inline code. Fixed 14px with generous 1.65 line-height for readability of multi-line snippets.

### MDIO - Icon and badge face - used at 12-16px with widened tracking (0.0250em) for small labels and version chips. The slight letter-spacing and geometric forms give badges a technical, instrument-panel feel. - `--font-mdio`
- **Substitute:** Space Mono, IBM Plex Mono
- **Weights:** 300, 400
- **Sizes:** 12px, 16px
- **Line height:** 1.00, 1.33, 1.50
- **Letter spacing:** 0.0250em
- **OpenType features:** `"calt", "zero"`
- **Role:** Icon and badge face - used at 12-16px with widened tracking (0.0250em) for small labels and version chips. The slight letter-spacing and geometric forms give badges a technical, instrument-panel feel.

### Inter - Inter - detected in extracted data but not described by AI - `--font-inter`
- **Weights:** 200, 400
- **Sizes:** 16px, 18px
- **Line height:** 1.5
- **Role:** Inter - detected in extracted data but not described by AI

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.5 | 0.3px | `--text-caption` |
| body-sm | 14px | 1.65 | - | `--text-body-sm` |
| body | 16px | 1.5 | - | `--text-body` |
| subheading | 20px | 1.4 | - | `--text-subheading` |
| heading-sm | 30px | 1.2 | - | `--text-heading-sm` |
| heading | 36px | 1.11 | - | `--text-heading` |
| display | 48px | 1.1 | - | `--text-display` |
