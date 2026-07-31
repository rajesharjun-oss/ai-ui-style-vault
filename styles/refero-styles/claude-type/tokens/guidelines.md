# Guidelines

### Do
- Use 100px border-radius for all interactive elements: nav bar, buttons, badges, and tags
- Use 900px border-radius for full-bleed image cards and dark specimen cards to create the signature arched/tombstone shape
- Set all body text in MagicUIPro weight 400 - never use bold weights in UI copy; the system stays visually quiet so display serifs can speak
- Reserve #99ff66 (Acid Lime) exclusively for metadata badges; never apply it to backgrounds, borders, or body text
- Use #2b1b1b (Espresso) for all hairline borders at 1px; this warm brown is the structural line color across the system
- Maintain generous spacing: 64px minimum between major sections, 14-16px within component groups
- Activate "dlig" font-feature-settings on all MagicUIPro text to enable the custom discretionary ligatures

### Don't
- Do not add drop shadows, glows, or blur effects to cards or buttons - the system is shadow-free by design
- Do not introduce additional accent colors beyond #99ff66; the 3% colorfulness is intentional
- Do not use border-radius values below 10px for cards or 100px for interactive elements - the pill/arch vocabulary is binary
- Do not set body text above 18px or use MagicUIPro for display headlines; display serifs are product content, not UI
- Do not use pure white (#ffffff) as a page background - always use #fcfbf7 cream as the canvas
- Do not apply bold (600+) or semibold weights to MagicUIPro; the family exists at 400 only and any synthetic bolding breaks the system
- Do not center-align body paragraphs or create dense text blocks; the layout is gallery-sparse with generous line-height (1.6-2.0)

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
