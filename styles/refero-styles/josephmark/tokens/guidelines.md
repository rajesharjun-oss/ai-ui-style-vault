# Guidelines

### Do
- Use Scto Grotesk A at weight 300 for all display and heading sizes - the light weight is the signature, not a fallback
- Apply negative letter-spacing consistently: -0.035em at display (70px), scaling proportionally to -0.019em at caption (12px)
- Build with full-bleed sections, not contained max-width layouts - let the dark canvas extend to the viewport edges
- Use #000000 and #f4f5ef as the two primary canvas colors, alternating between them for section rhythm
- Define interactive elements with 1px borders and 9999px radius - the pill shape is the only button form
- Set body text at 16px/1.38 with #ffffff on dark and #4e5449 on light surfaces
- Separate content blocks with 1px #e5e7eb hairlines, never with shadows or background fills

### Don't
- Do not introduce color beyond the single warm taupe (#a9a498) - the system's power comes from its 1% colorfulness
- Do not add shadows, glows, or any drop effects - this system is rigorously flat
- Do not use rounded corners on cards, images, or containers - only buttons are rounded (to 9999px)
- Do not center text - everything is left-aligned, following editorial column logic
- Do not use bold weights (600+) for emphasis - the scale goes 300 400 500, and contrast comes from size and color, not weight
- Do not add icon systems or decorative graphics - typography and photography are the only visual elements
- Do not use #ffffff as a section background - it appears only as surface within forms and as text color on dark

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
