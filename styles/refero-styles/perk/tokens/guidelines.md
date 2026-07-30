# Guidelines

### Do
- Use #beff50 as the ONLY filled button color - never introduce a second chromatic action color
- Set border-radius to 28px on all cards and primary buttons, 9999px on pills and tags
- Use OTSono weight 500 for all headings, labels, and CTAs; weight 400 for body and supporting text
- Apply letter-spacing -0.03em to any text at 28px and above; let body text use default tracking
- Build the surface stack as white parchment (#f5f5eb) lime (#beff50) - never use shadows to separate layers
- Use 0.1em tracking with uppercase for category eyebrows at 10-12px
- Let the off-black #14140f carry all text - never use pure #000000 except in input fields
- Keep section gaps between 80-120px to maintain the editorial breathing rhythm

### Don't
- Do not add box-shadows to cards - the system relies on tonal contrast, not elevation
- Do not use #000000 for body text - #14140f is warmer and more on-brand
- Do not introduce blue, red, or any secondary accent color - the lime is the only chromatic voice
- Do not mix border-radius values within the same component type (all buttons are 28px, all pills are 9999px)
- Do not use system fonts as fallback for display sizes - OTSono at 60px+ with -0.03em tracking is signature
- Do not place lime buttons on white surfaces without sufficient padding - the contrast is loud, give it room
- Do not use 600 or 700 weights - the system operates on 400 and 500 only
- Do not add gradients - the lime is already saturated; gradients would muddy it

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
