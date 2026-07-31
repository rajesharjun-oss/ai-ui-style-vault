# Guidelines

### Do
- Use only #000000 and #ffffff as the foundation - every section must resolve to one of these two surfaces, creating hard editorial breaks
- Apply 0.1em letter-spacing to every piece of text set in the custom brand face, at every size, without exception
- Render all photography edge-to-edge with zero border-radius, zero padding, zero shadow - let images bleed to the viewport edges
- Use the 100px border-radius exclusively for ghost outline buttons - every interactive element should be a transparent pill with a 1px border
- Set the hero headline at maximum display scale (the 50-54px token, scaled to fill the viewport width) to make typography function as the visual hero instead of imagery
- Maintain 120px vertical padding above and below major sections to create the breathing room of a gallery wall
- Use uppercase for all headings, button labels, and navigation items - sentence case appears nowhere in the system

### Don't
- Never introduce a chromatic color, gradient, or accent - the system is 0% colorful by design, and any hue would break the gallery aesthetic
- Never use a filled or solid-background button - ghost outlines are the only button pattern permitted
- Never apply box-shadow, drop-shadow, or blur to any element - depth comes from black/white alternation, not elevation
- Never use border-radius on images or cards - the only rounded element is the pill button at 100px
- Never use bold or semibold weights - the custom font exists at weight 400 only, and introducing weight contrast would destroy the system
- Never set body text tighter than 1.4 line-height - the generous leading is what keeps small white-on-black text legible
- Never add decorative UI elements (badges, tags, pills, chips, tooltips) - the system is intentionally stripped to typography, photography, and hairline borders

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
