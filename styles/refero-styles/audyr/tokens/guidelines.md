# Guidelines

### Do
- Use #262626 as the only filled button background - it is the single visual anchor in the monochrome system
- Apply -0.025em letter-spacing to every text element at every size, from 12px captions up to 48px displays
- Use #ededed for all structural dividers, card borders, and input outlines at 1px
- Set card radii to 14px, button radii to 4px, and badge radii to 9999px - these three radii define the visual language
- Limit the chromatic surface tint (#ecfdf5) to success/popular badges only; never apply it to large surfaces
- Keep shadows to the two soft levels: the diffuse card shadow (lab 0.1 25px 50px -12px) and the button micro-shadow (oklab 0.05 1px 2px)
- Maintain 80-160px section padding to preserve the editorial breathing room

### Don't
- Don't introduce a brand color accent - the absence of color IS the brand
- Don't use radii outside the 4 / 8 / 14 / 18 / 9999px scale; no 6px or 12px intermediate values
- Don't add drop shadows heavier than the documented card shadow - anything more theatrical breaks the paper-grain feel
- Don't pair Inter with a second typeface for display use - the single-family commitment is structural
- Don't use #ffffff for text on white surfaces, and don't use #ededed for body text - both will fail contrast
- Don't apply gradients - the system is committed to flat, unshaded fills
- Don't use colored status indicators on the marketing site; restrict color to badges and the pricing 'Popular' highlight

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
