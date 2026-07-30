# Guidelines

### Do
- Use 2px solid #292929 borders as the primary separator and container system instead of shadows or background fills
- Set all border-radius to 0px - no rounded corners anywhere
- Use NH weight 100-300 at 32-43px for headlines with -0.02em letter-spacing
- Set S-Condensed labels at 12-14px uppercase with +0.1em to +0.2em letter-spacing for all nav, tags, and metadata
- Let the grid go edge-to-edge (no max-width container) - sections butt directly against each other via shared borders
- Use 8px as the base spacing unit, stepping in multiples (8, 12, 20, 43, 45)
- Pair white (#ffffff) surfaces with #292929 ink for all text and borders - never introduce accent color

### Don't
- Don't add box-shadow, drop-shadow, or any elevation - the system is intentionally flat
- Don't round any corner - cards, buttons, inputs, images all stay 0px
- Don't use bold weights (600+) - the system's voice comes from weight 100/300/400/500
- Don't introduce a brand accent color - the palette is strictly black/white/ink
- Don't use gradients - fills are always flat solids
- Don't use lowercase body text in S-Condensed - that face is always uppercase
- Don't center-align body paragraphs - copy flows left-aligned in editorial register

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
