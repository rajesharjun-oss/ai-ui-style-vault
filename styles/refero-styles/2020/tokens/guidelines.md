# Guidelines

### Do
- Set display headlines at 137px / line-height 0.79 / letter-spacing -0.05em in Helvetica LT Pro 400 - never bump the weight, the book weight is the signature
- Use Olive Ink (#4f503e) for all text and borders regardless of canvas color - the text must always be the same dark warm tone so the changing background feels like a single identity expressing different moods
- Let the page canvas fill 100% of the viewport edge-to-edge with no container, no max-width, no margin - full-bleed is non-negotiable
- Use 20px as the only spacing unit - vertical rhythm between the headline, subtitle, and grid is always 20px
- Keep all radii at 0px - album tiles, buttons, and tags are sharp-cornered; the colored field provides all the softness the page needs
- Treat the canvas color as the primary navigation: the user changes the page by changing the background, not by clicking links
- Set every text element in a single weight (400) - do not introduce bold, medium, or light variants

### Don't
- Do not use filled buttons - a solid fill would compete with the canvas color; all actions are outlined borders or pure icons
- Do not add card frames, drop shadows, or elevation to album tiles - they sit directly on the canvas with no chrome
- Do not introduce a second typeface - the entire site is set in one family at one weight
- Do not center body text - copy aligns left, full-bleed, and wraps naturally
- Do not use a max-width container - the layout is always edge-to-edge
- Do not pair Olive Ink (#4f503e) text with a colored background outside the established palette (oxblood, sienna, near-black, sage, pearl) - the six surface colors are the only valid canvases
- Do not add line-height above 1.0 for any size above 21px - the tight leading (0.79-0.80) on display text is what makes the headlines feel like solid shapes

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
