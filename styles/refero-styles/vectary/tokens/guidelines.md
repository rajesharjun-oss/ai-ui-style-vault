# Guidelines

### Do
- Use Inter exclusively across the entire interface; never substitute a second typeface family
- Set border-radius to 8px on every rounded element - buttons, cards, nav containers, tags all share the same radius for a unified geometric language
- Reserve the violet gradient (linear-gradient(129deg, #6100ff, #9d50ff)) for the single primary CTA per screen; never duplicate it
- Use weight 900 only at the display size (83px); weights 400 and 700 cover everything else
- Apply negative letter-spacing at every size: -0.17px at 14px scaling to -3.24px at 83px
- Build vertical rhythm from the 6px base unit: 30px for card padding, 60px for section gaps, 20px between inline elements
- Keep the page background pure #ffffff; the system has no tinted canvas variants

### Don't
- Do not introduce a second chromatic accent - the system is monochromatic plus one violet, and adding red/green/blue/yellow breaks the drafting-tool identity
- Do not use weight 900 for body, labels, or section headings; it is loud and will flatten the hierarchy
- Do not add drop shadows, glows, or blur effects - the design language is flat; elevation comes from background tone, not shadow
- Do not use #6100ff on decorative icons, tags, illustrations, or non-action UI - the violet earns its place by being scarce
- Do not use #313131 as a page or card background; it is a nav-level surface only
- Do not set letter-spacing to 0 or positive values - the system always tightens, even at 14px body size
- Do not place violet text on a violet gradient background; the gradient already carries the brand and needs white text for contrast

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
