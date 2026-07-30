# Guidelines

### Do
- Use pill radius (40px) for every button, tag, and nav link - pill geometry is the system's strongest signature shape.
- Use 16px radius for all images, image cards, and image containers - keep this consistent across the entire site.
- Use 8px radius for inputs only - a deliberate contrast with the pill buttons that signals interactivity without softness.
- Reach for #f6f2eb (Bone Warm) as the section background between two white bands - the warm tint is the only way this achromatic system creates rhythm.
- Set display headlines at 48-92px in DM Sans weight 700 with letter-spacing -0.0110em ( -0.53px at 48px, -1.01px at 92px) - tight tracking is what makes the type feel editorial rather than corporate.
- Use uppercase labels and button text with letter-spacing 0.0560em for breathing room - never use uppercase without expanding the tracking.
- Use hairline 1px borders in #666666 for all dividers and interactive affordances instead of shadows - the system deliberately avoids elevation in favor of line.

### Don't
- Never introduce chromatic color - the system is 0% colorful by design, and any accent hue would break the editorial monochrome logic.
- Never use shadows for elevation - the only shadow pattern in the system is the 1px inset border on links; do not add drop shadows to cards or buttons.
- Never use #000000 as a large filled surface - use #212121 (Obsidian) for dark backgrounds and reserve pure black for text and thin accent strokes only.
- Never use sharp 0px corners on images or cards - everything that contains an image uses 16px radius; flat-cornered images would feel foreign.
- Never use display-weight tracking on body text - the -0.0110em is calibrated for 40px+ sizes; applying it to 16px body copy will over-condense letters and hurt readability.
- Never use uppercase for body copy - uppercase is reserved for eyebrows, badges, and button labels where the 0.0560em tracking provides necessary letter spacing.
- Never use the warm Bone Warm (#f6f2eb) for form fields or interactive surfaces - it is a sectional wash only; form wells should use the cool Ash Mist (#f5f5f5) to signal input.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
