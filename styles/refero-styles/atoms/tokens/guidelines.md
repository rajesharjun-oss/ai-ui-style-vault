# Guidelines

### Do
- Use #fff7dd for all primary text and hairline borders on black surfaces
- Reserve #c8ad86 exclusively for category tags, accent headings, and decorative borders - never as a full-surface fill
- Apply Switzer with tight negative letter-spacing on all display sizes: -1.85px at 44px, -0.13px at 16px
- Set border-radius to 4px on cards and buttons, 100px on tags and pills only
- Separate cards and sections with 1px hairline borders, never with shadows or background fills
- Keep vertical rhythm tight: 8-16px between related elements, 80px between major sections
- Render all icons and arrows in #fff7dd or #c8ad86 - never introduce additional colors

### Don't
- Do not use shadows, glows, or blur effects for elevation - define surfaces with borders only
- Do not introduce saturated colors beyond the champagne accent - no blues, greens, or reds
- Do not use pure white (#ffffff) for text - #fff7dd is warmer and on-brand
- Do not add background fills to cards or sections - they sit directly on the black canvas
- Do not use large border-radius values on cards (no 12px, 16px, 24px) - stay at 4px max for rectangles
- Do not apply letter-spacing to body text - keep tracking tight only on 16px+ sizes
- Do not animate color, position, or scale on load - the system is static and placed, not kinetic

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
