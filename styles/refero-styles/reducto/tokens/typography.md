# Typography

### reductoSerif - Display and headline serif - the brand's signature voice. Set at 64-136px for hero/display, drops to 24-32px for section headings. Weight 470 is the workhorse (editorial body weight for a display face), weight 650 is reserved for stat numbers. The tight -0.01em tracking at every size is critical: it tightens the serif's natural rhythm into a modern, condensed look. Substituted with Playfair Display, Lora, or Source Serif Pro when unavailable. - `--font-reductoserif`
- **Substitute:** Playfair Display, Lora, or Source Serif 4
- **Weights:** 400, 470, 650
- **Sizes:** 16px, 24px, 32px, 64px, 80px, 136px
- **Line height:** 0.74, 1.13, 1.25, 1.33, 1.50
- **Letter spacing:** -0.01em at all sizes
- **Role:** Display and headline serif - the brand's signature voice. Set at 64-136px for hero/display, drops to 24-32px for section headings. Weight 470 is the workhorse (editorial body weight for a display face), weight 650 is reserved for stat numbers. The tight -0.01em tracking at every size is critical: it tightens the serif's natural rhythm into a modern, condensed look. Substituted with Playfair Display, Lora, or Source Serif Pro when unavailable.

### Inter - Body and UI sans - the workhorse for nav links, buttons, descriptions, paragraphs, and form fields. Weight 400 for body, 500 for button labels and emphasized nav. Activates stylistic alternates 'salt' (single-storey 'a') and 'ss02' (open 'g') - these are essential to matching the brand; without them, Inter reads as generic. - `--font-inter`
- **Substitute:** DM Sans or General Sans
- **Weights:** 400, 500
- **Sizes:** 14px, 15px, 16px, 17px, 18px, 20px, 24px
- **Line height:** 1.33, 1.43, 1.50, 1.56, 1.60
- **OpenType features:** `"salt" on, "ss02" on`
- **Role:** Body and UI sans - the workhorse for nav links, buttons, descriptions, paragraphs, and form fields. Weight 400 for body, 500 for button labels and emphasized nav. Activates stylistic alternates 'salt' (single-storey 'a') and 'ss02' (open 'g') - these are essential to matching the brand; without them, Inter reads as generic.

### reductosans - Compact UI sans for small labels, tag chips, micro-copy, and dense interface text where Inter feels too tall. Functionally overlaps with Inter but provides a tighter, more 'captured' rhythm for chrome. - `--font-reductosans`
- **Substitute:** Inter at the same weight and size
- **Weights:** 400, 500
- **Sizes:** 14px, 15px, 16px
- **Line height:** 1.43, 1.50, 1.60
- **Role:** Compact UI sans for small labels, tag chips, micro-copy, and dense interface text where Inter feels too tall. Functionally overlaps with Inter but provides a tighter, more 'captured' rhythm for chrome.

### Reddit Mono - Single-purpose display monospace for oversized stat numbers - the '2,000,000,000' counter. The -0.03em tracking pulls the mono's natural width inward so the number doesn't look like code, but a label. Substituted with JetBrains Mono or IBM Plex Mono. - `--font-reddit-mono`
- **Substitute:** JetBrains Mono or IBM Plex Mono
- **Weights:** 400
- **Sizes:** 80px
- **Line height:** 1.13
- **Letter spacing:** -0.03em at 80px
- **Role:** Single-purpose display monospace for oversized stat numbers - the '2,000,000,000' counter. The -0.03em tracking pulls the mono's natural width inward so the number doesn't look like code, but a label. Substituted with JetBrains Mono or IBM Plex Mono.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 14px | 1.5 | - | `--text-caption` |
| body-sm | 16px | 1.5 | - | `--text-body-sm` |
| body-lg | 18px | 1.5 | - | `--text-body-lg` |
| subheading | 20px | 1.5 | - | `--text-subheading` |
| heading-sm | 24px | 1.33 | -0.01px | `--text-heading-sm` |
| heading | 32px | 1.25 | -0.01px | `--text-heading` |
| heading-lg | 64px | 1.13 | -0.01px | `--text-heading-lg` |
| display-sm | 80px | 1.13 | -0.01px | `--text-display-sm` |
| display | 136px | 1.13 | -0.01px | `--text-display` |
