# Guidelines

### Do
- Use Neue Haas Unica Pro (or Inter / Neue Haas Grotesk) at weight 400 exclusively - never introduce bold, medium, or light weights
- Set all type with letter-spacing -0.025em; tight tracking is non-negotiable for the editorial feel
- Use only #ffffff, #e5e7eb, #000000, and #a3a3a3 - no chromatic accents anywhere in the UI
- Build hierarchy through size jumps (16 18 22 72), not through weight or color shifts
- Separate sections with 1px #e5e7eb hairlines or generous whitespace, never with fills or shadows
- Make every interactive element a pill (9999px) or a text-only label - no filled buttons, no rounded cards, no bordered inputs
- Let photography carry all color; images bleed into the layout without frames, radii, or overlays

### Don't
- Do not add a second typeface family - the system is monotypographic by design
- Do not introduce any color other than the four neutrals - no brand red, blue, or accent green
- Do not use box-shadows or elevation on any component - depth comes from whitespace, not blur
- Do not add border-radius to cards or images - only navigation and chips use 9999px
- Do not bold or italicize text to create emphasis - increase size instead
- Do not place content inside bordered containers or filled panels - use whitespace to group
- Do not use background colors for buttons, tags, or interactive states - use text color and the dot indicator

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
