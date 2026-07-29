# Guidelines

### Do
- Use Cocoa Ink (#200e0e) for all body text, icons, and borders - never use pure #000000 or charcoal grays; the warm undertone is the brand
- Apply 2.23px radius to every surface - cards, buttons, badges, inputs, images; sharp corners are non-negotiable
- Use Signal Red (#ed212d) only in three places: the brand bar, the guarantee bar, and product status badges - never on CTAs, links, or body text
- Compress display headlines to letter-spacing -0.02em (e.g. -0.84px at 42px) for editorial tightness; body and below stays at normal tracking
- Alternate white (#ffffff) and Blush Cream (#f8f0ec) section backgrounds to create rhythm without using shadows
- Center-align the category navigation row and the 'Help Me Choose' button - left-aligned navigation would break the print-catalogue feel
- Use full-bleed lifestyle photography (portrait crops, natural light, shallow DOF) for heroes and editorial sections; product-only shots on solid color backgrounds for the grid

### Don't
- Do not add box-shadows to any component - elevation comes from background-color shifts, never from blur or offset
- Do not round corners beyond 2.23px - no pill buttons, no large radii; the near-sharp aesthetic defines the system
- Do not use Signal Red (#ed212d) for buttons, links, or hover states - it is brand-identity color, not an action color
- Do not introduce drop shadows, gradients, or glassmorphism - the design is deliberately flat and print-like
- Do not use the product color swatches (Sage Mist #9ac9b5, Dusty Rose #dbb0b3) as system-wide accent tokens - they are product variant colors only
- Do not center-align body paragraphs or use fonts other than Antarctica (or its substitute); the single-typeface discipline is what makes the system feel like one publication
- Do not use pure black (#000000) for text or icons - always use Cocoa Ink (#200e0e) to maintain the warm tonal harmony

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
