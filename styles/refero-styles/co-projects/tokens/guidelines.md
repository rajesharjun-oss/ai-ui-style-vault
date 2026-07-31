# Guidelines

### Do
- Use only the three palette colors: #ffffff for canvas, #000000 for ink and geometric fills, #e5e7eb exclusively for 1px hairline dividers
- Set all type to weight 400 - never bold, never medium, never light. The system has exactly one weight and that constraint is the brand
- Apply 139-208px vertical margins between major sections to maintain gallery-scale breathing room
- Let geometric ring/circle forms occupy 50-70% of the viewport to create the architectural scale contrast with 16px nav text
- Use Alpha at 60px / lineHeight 1.00 for display headlines and Takt at 36px / lineHeight 1.11 for subhead blocks
- Position navigation as three sparse text labels at the top corners - no bar, no background, no border
- Set border-radius to 0 on all rectangular elements; reserve all rounding for intentional circular geometry

### Don't
- Never add a shadow, blur, or elevation effect - the system is completely flat and any depth cue breaks the figure/ground purity
- Never introduce a color outside the three achromatic tokens - no accent hues, no tinted grays, no hover-state colors beyond opacity shifts
- Never use a font weight other than 400 - no 500, 600, 700, or 800 under any circumstance
- Never apply border-radius to buttons, cards, tags, or inputs - rectangular means sharp corners, always
- Never constrain the hero composition to a max-width container - let the geometric forms run full-bleed and crop at viewport edges
- Never add icons, illustrations, photography, or decorative graphics - the circle/ring IS the imagery
- Never use letter-spacing adjustment - all type sits at default tracking, the custom typefaces are already tuned

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
