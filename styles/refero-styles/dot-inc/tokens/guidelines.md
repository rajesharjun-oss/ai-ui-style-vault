# Guidelines

### Do
- Use #ff5a2f exclusively for primary action buttons and active state accents - it should appear on no more than 3-5 elements per viewport.
- Set border-radius to 20px for cards and images, 30px for buttons and badges, and 12-20px for inline images.
- Use Plus Jakarta Sans weight 300 or 400 for headlines 40px and above to maintain the light, spacious typographic feel.
- Apply 1px #e5e7eb borders for all card and section dividers - never use heavier borders or decorative lines.
- Space sections with 80px vertical gaps and use 24px for inter-element gaps within cards and lists.
- Keep backgrounds white (#ffffff) as the default canvas; use #f5f5f5 only for alternating content bands or subtle card elevation.
- Reserve the shadow token rgba(0,0,0,0.25) 0px 4px 10px 0px for the single primary CTA button per view.

### Don't
- Do not introduce additional chromatic colors - the system's identity depends on the 2% colorfulness ceiling.
- Do not use border-radius below 8px for any interactive element; the soft, rounded geometry is a core brand trait.
- Do not apply shadows to cards, images, or navigation - only the primary CTA may have elevation.
- Do not use #000000 for body text at sizes above 20px; switch to #1f1f1f for large headings to avoid harshness.
- Do not use bold (weight 700-800) for body or heading text - reserve weights 700-800 for short labels or tags only.
- Do not create flat hard-edged rectangular blocks; every container needs 20-30px radius.
- Do not use gradients - the system is entirely flat with single solid color fills.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
