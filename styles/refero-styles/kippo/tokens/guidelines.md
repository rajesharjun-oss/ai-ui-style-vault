# Guidelines

### Do
- Use Source Code Pro for every text element - body, headings, buttons, nav, labels. No secondary font.
- Set all UI text to uppercase with letter-spacing 0.1em minimum; display headlines should reach 0.3-0.5em tracking.
- Define cards with a 1px #ffffff border on a #000000 or #29292a fill - never with shadow, never with a colored fill.
- Reserve #ee1f66 for the primary CTA background, the accent word in two-tone display headlines, and active/border-current-page states. Use it no more than once per viewport section.
- Use 10px radius for buttons and tags, 15px for cards and images, 50px for icon buttons. Never exceed 15px on rectangular surfaces.
- Maintain generous vertical breathing room: 100-150px between major sections, 30px inside cards, 15px between inline elements.
- Enable the 'zero' font-feature on Source Code Pro so the numeral 0 is slashed - it reinforces the terminal identity.

### Don't
- Don't introduce a second typeface (no Inter, no Helvetica, no sans-serif fallback for body). Monospace-only is the identity.
- Don't fill cards with color, gradient, or image. Cards are transparent panels - the border is the card.
- Don't use drop shadows for elevation. Depth comes from overlapping layers and outline contrast, never from blur.
- Don't dilute #ee1f66 by using it for body text, borders on non-action elements, or large background areas. It must remain rare.
- Don't use border-radius larger than 15px on rectangular surfaces, and never use fully-rounded pill shapes on buttons (10px max).
- Don't mix light and dark themes - this is a dark-only system. No white-background sections, no theme toggle.
- Don't use red, green, or yellow for semantic states (success/error/warning) - those colors are decorative only in this system, and the dark canvas + white text + single pink accent is the entire signal vocabulary.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
