# Typography

### Exposure Variable - Display headlines - the 112px whisper-weight serif that anchors hero and section titles. Its 0.85 line-height vertically compresses letters, making headlines feel carved and monumental rather than airy. Signature choice: anti-convention weight (300, not 700) and negative letter-spacing (-0.03em) create authority through restraint. Substitute: Playfair Display or DM Serif Display at weight 400 with tight tracking. - `--font-exposure-variable`
- **Substitute:** Playfair Display
- **Weights:** 300
- **Sizes:** 112px
- **Line height:** 0.85
- **Letter spacing:** -0.03em
- **Role:** Display headlines - the 112px whisper-weight serif that anchors hero and section titles. Its 0.85 line-height vertically compresses letters, making headlines feel carved and monumental rather than airy. Signature choice: anti-convention weight (300, not 700) and negative letter-spacing (-0.03em) create authority through restraint. Substitute: Playfair Display or DM Serif Display at weight 400 with tight tracking.

### Exposure VAR - Section headings and large nav - the bold companion to Exposure Variable. Used for 'Dia reads between the tabs' and feature titles. Tighter tracking at -0.05em at 48px gives headline density. Substitute: Inter Tight or a condensed grotesque. - `--font-exposure-var`
- **Substitute:** Inter Tight
- **Weights:** 650
- **Sizes:** 24px, 48px
- **Line height:** 1.17-1.25
- **Letter spacing:** -0.05em at 48px, -0.03em at 24px
- **Role:** Section headings and large nav - the bold companion to Exposure Variable. Used for 'Dia reads between the tabs' and feature titles. Tighter tracking at -0.05em at 48px gives headline density. Substitute: Inter Tight or a condensed grotesque.

### ABC Oracle - Body text, UI labels, subheadings, and large feature headlines (54px at weight 300). The workhorse font - its humanist sans quality keeps long-form copy legible at generous line-heights (2.19 for body). Weight 500 used sparingly for emphasis. The 54px weight 300 headline is the secondary display voice, lighter than Exposure VAR but in the same serif-adjacent register. Substitute: Sohne or Inter at matching weights. - `--font-abc-oracle`
- **Substitute:** Inter
- **Weights:** 300, 400, 500
- **Sizes:** 10px, 14px, 16px, 18px, 20px, 22px, 24px, 54px
- **Line height:** 1.11-2.19
- **Letter spacing:** -0.04em at 54px, -0.02em at 18px, normal elsewhere
- **Role:** Body text, UI labels, subheadings, and large feature headlines (54px at weight 300). The workhorse font - its humanist sans quality keeps long-form copy legible at generous line-heights (2.19 for body). Weight 500 used sparingly for emphasis. The 54px weight 300 headline is the secondary display voice, lighter than Exposure VAR but in the same serif-adjacent register. Substitute: Sohne or Inter at matching weights.

### ABC Oracle Triple - Button text, inline labels, UI microcopy - a narrower variant of Oracle designed for button and tag contexts. The wide line-height (2.19) suggests single-line button use with internal padding breathing. Substitute: Inter at 16px weight 400. - `--font-abc-oracle-triple`
- **Substitute:** Inter
- **Weights:** 400
- **Sizes:** 16px
- **Line height:** 2.19
- **Role:** Button text, inline labels, UI microcopy - a narrower variant of Oracle designed for button and tag contexts. The wide line-height (2.19) suggests single-line button use with internal padding breathing. Substitute: Inter at 16px weight 400.

### ABC Favorit Mono - Eyebrow labels, step numbers (01, 02, 03), navigation metadata - all-caps at 13px with 0.1em tracking creates the editorial chapter-marker effect. The mono face contrasts with Oracle's humanist sans, creating typographic tension. - `--font-abc-favorit-mono`
- **Substitute:** JetBrains Mono
- **Weights:** 400
- **Sizes:** 
- **Line height:** 1.23-1.27
- **Letter spacing:** 0.1em uppercase at 13px
- **Role:** Eyebrow labels, step numbers (01, 02, 03), navigation metadata - all-caps at 13px with 0.1em tracking creates the editorial chapter-marker effect. The mono face contrasts with Oracle's humanist sans, creating typographic tension.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 10px | 1.5 | - | `--text-caption` |
| eyebrow | 13px | 1.23 | 1.3px | `--text-eyebrow` |
| body-sm | 16px | 2.19 | - | `--text-body-sm` |
| body | 18px | 1.5 | -0.36px | `--text-body` |
| body-lg | 20px | 1.5 | - | `--text-body-lg` |
| subheading | 22px | 1.36 | - | `--text-subheading` |
| heading-sm | 24px | 1.25 | -0.72px | `--text-heading-sm` |
| heading | 48px | 1.17 | -2.4px | `--text-heading` |
| heading-lg | 54px | 1.11 | -2.16px | `--text-heading-lg` |
| display | 112px | 0.85 | -3.36px | `--text-display` |
