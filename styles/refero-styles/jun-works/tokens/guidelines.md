# Guidelines

### Do
- Use 129.6px border-radius on every interactive element - no rectangles, no modest rounding
- Set all display text in Standard at 45-54px with -0.045em to -0.054em letter-spacing
- Render body text in Times serif with ~1.70 line-height for editorial breathing room
- Anchor all content to the left edge - no centering, no max-width containers
- Prefix list items with an em-dash (-) instead of bullets or numbers
- Use #000000 for all borders, text, and outlines - never introduce color
- Maintain #ffffff backgrounds everywhere; let the 1px black border define shape, not fill

### Don't
- Never add color - no accent, no semantic green/red/yellow, no brand color
- Never use box-shadow or elevation - depth comes from border definition, not shadow
- Never use border-radius below 129.6px on any element
- Never bold the display type - Standard ships in one weight (400) and that restraint is the system
- Never use a sans-serif for body text - the serif/sans split is structural, not optional
- Never center-align headings or body paragraphs
- Never add imagery, photography, or illustration - the page is pure typography and label geometry

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
