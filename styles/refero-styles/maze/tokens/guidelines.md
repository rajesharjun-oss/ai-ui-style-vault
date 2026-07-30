# Guidelines

### Do
- Use Phonic at weight 300 for every display and headline; weight 400 for body and UI only
- Default to a 12px radius on cards, 8px on buttons, 4px on badges - the radius scale is narrow and intentional
- Use #f5f4f0 (Bone) as the page canvas; reserve #ffffff for cards and inputs that need to lift off the canvas
- Let Chartreuse (#dbf570) appear as small functional punctuation - one badge, one tag, one globe - never as a wide wash of UI color
- Track headlines aggressively tight: -6.3px at 90px, scaling proportionally so letters almost touch at the largest sizes
- Keep buttons quiet: Ink-filled or Ink-outlined, 8px radius, 12px x 20px padding, no shadow, no gradient
- Use Lavender (#b8a3ff) full-bleed for section breaks to create contrast against the bone canvas

### Don't
- Do not use sans-serif for headlines - Phonic serif at weight 300 IS the brand voice; substituting bold sans-serif destroys the editorial register
- Do not apply heavy box-shadows to cards - the system is intentionally flat, elevation is a hairlines-only discipline
- Do not use Chartreuse as a CTA background - it is a highlight color for tags and motifs, not an action color; Ink stays the action
- Do not set display text at line-height 1.4+ - headlines run tight (1.00-1.10) so the serif rhythm stays architectural
- Do not introduce new chromatic colors beyond the three in the palette (Chartreuse, Olive, Lavender) - every additional hue dilutes the bone-paper system
- Do not use #000000 as body text - Ink (#1c1c1c) is the text color; #000 is reserved for the announcement bar and hairline borders
- Do not center body paragraphs in cards - only section headlines and hero copy may center; study card copy stays left-aligned

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
