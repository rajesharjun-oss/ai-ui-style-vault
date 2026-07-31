# Typography

### nhm - Primary type system spanning body (16-21px) to extreme display (173-185px). Weight 400 carries both the whisper-quiet metadata and the 185px display headlines - the system trusts the scale to create hierarchy rather than reaching for bold weights. Letter-spacing tightens aggressively to -0.05em at display sizes to prevent the large counters from feeling airy. - `--font-nhm`
- **Substitute:** Neue Haas Grotesk, Inter, Helvetica Neue
- **Weights:** 400, 700
- **Sizes:** 16, 21, 173, 185
- **Line height:** 0.78, 1.00, 1.10, 1.20
- **Letter spacing:** -0.8px at 16px, -1.05px at 21px, -8.65px at 173px, -9.25px at 185px
- **Role:** Primary type system spanning body (16-21px) to extreme display (173-185px). Weight 400 carries both the whisper-quiet metadata and the 185px display headlines - the system trusts the scale to create hierarchy rather than reaching for bold weights. Letter-spacing tightens aggressively to -0.05em at display sizes to prevent the large counters from feeling airy.

### psl - Mid-scale display for subheadings and section titles. Sits between body text and the extreme display tier, carrying -0.015em tracking for controlled density at smaller display sizes. - `--font-psl`
- **Substitute:** Inter, Sohne
- **Weights:** 400
- **Sizes:** 34, 69
- **Line height:** 1.00, 1.20
- **Letter spacing:** -0.51px at 34px, -1.035px at 69px
- **Role:** Mid-scale display for subheadings and section titles. Sits between body text and the extreme display tier, carrying -0.015em tracking for controlled density at smaller display sizes.

### psr - Body text alternative at 21px with normal tracking - used for longer-form passages where the tighter nhm spacing would feel constrained. - `--font-psr`
- **Substitute:** Inter, system-ui
- **Weights:** 400
- **Sizes:** 21
- **Line height:** 1.00
- **Letter spacing:** normal
- **Role:** Body text alternative at 21px with normal tracking - used for longer-form passages where the tighter nhm spacing would feel constrained.

### Kumbh Sans - Alternate display family at extreme sizes, sharing the same -0.05em tracking and tight 0.78-0.80 line-height as nhm. Provides a geometric counterpoint to nhm's neo-grotesque character for typographic variation within display lockups. - `--font-kumbh-sans`
- **Substitute:** Kumbh Sans (Google Fonts)
- **Weights:** 400
- **Sizes:** 173, 185
- **Line height:** 0.78, 0.80
- **Letter spacing:** -8.65px at 173px, -9.25px at 185px
- **Role:** Alternate display family at extreme sizes, sharing the same -0.05em tracking and tight 0.78-0.80 line-height as nhm. Provides a geometric counterpoint to nhm's neo-grotesque character for typographic variation within display lockups.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 16px | 1.2 | -0.8px | `--text-caption` |
| body | 21px | 1 | -1.05px | `--text-body` |
| subheading | 34px | 1 | -0.51px | `--text-subheading` |
| heading | 69px | 1 | -1.035px | `--text-heading` |
| display | 173px | 0.78 | -8.65px | `--text-display` |
| display-lg | 185px | 0.8 | -9.25px | `--text-display-lg` |
