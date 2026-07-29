# Guidelines

### Do
- Use Unbounded exclusively - never substitute a secondary typeface, the single-family discipline is the identity
- Apply positive letter-spacing to all text; never collapse tracking below 0.067em even at display sizes
- Keep all UI elements at 0px border-radius - sharp corners are non-negotiable and echo the 3D geometry
- Let the 3D scene be the sole source of color and light; UI stays pure grayscale (#ffffff, #f5f5f7, #cfcfcf, #111111, #000000)
- Use 1px hairline borders for all structural elements - buttons, dividers, card frames
- Center-align hero content and maintain generous vertical breathing room (80-120px between sections)
- Pair weight 600-700 for headlines with weight 100-400 for body to create a weight-contrast hierarchy that replaces color contrast

### Don't
- Never introduce accent colors, gradients, or chromatic buttons - the system is deliberately achromatic
- Never use border-radius on buttons, cards, inputs, or images - the sharp geometry is load-bearing
- Never apply shadows, glows, or blur effects to UI elements - depth belongs to the 3D scene only
- Never use negative letter-spacing or tight tracking - the wide-open spacing is the typographic signature
- Never fill buttons with solid color - always use the transparent ghost-button treatment with a 1px stroke frame
- Never use more than one typeface or mix serif/sans - Unbounded is the sole voice
- Never crowd the central viewport with UI - the 3D object needs negative space to breathe

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
