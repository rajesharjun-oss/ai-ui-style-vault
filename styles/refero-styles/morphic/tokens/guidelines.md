# Guidelines

### Do
- Use #0075ff exclusively for primary actions and the 'New' badge - never as a decorative accent, background tint, or text color outside of a clickable element
- Apply the two-tone headline pattern (white line 1, #999999 line 2) for all section headers and the hero - this is the site's signature typographic device
- Use the surface stack #000000 #212121 #292929 #333333 for hierarchy; never introduce a new shade between steps
- Apply -0.0620em letter-spacing at 52px and -0.0480em at 40px for display text - the tight tracking is what makes the headlines feel cinematic
- Use 10px radius for image/showcase cards and 7px radius for buttons - these are the only two radii that should appear in the main content flow
- Keep all borders at 1px #e5e7eb at very low opacity (10-20%) - borders should be felt, not seen
- Use Inter at weight 500 for all buttons, 700 for display, 400 for body - never mix more than two weights on a single screen

### Don't
- Never use a second chromatic color - the system is deliberately monochromatic with one blue accent; adding any other hue breaks the cinema-canvas concept
- Never apply drop shadows to UI components - shadows are reserved for image cards in the showcase grid only
- Never use #ffffff text for body copy - body text should be #999999 or lower contrast; white is reserved for headings, buttons, and high-emphasis labels
- Never center-align body paragraphs - only headlines, CTAs, and the hero text block are centered; body copy is left-aligned
- Never use border-radius values outside the defined scale (7px, 10px, 16px, 24px, 32px, 100px) - ad-hoc radii will break the system's geometric consistency
- Never place a colored background behind text blocks - the canvas must remain pure black; cards float on the void, they don't fill it
- Never use gradient backgrounds - the system is strictly flat; depth comes from the surface stack, not color transitions

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
