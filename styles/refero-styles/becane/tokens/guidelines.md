# Guidelines

### Do
- Use Eurostile Becane at 8px with 0.04em tracking as the universal label size for nav, buttons, counts, and footer links
- Keep all borders at 0.5px solid #e6e6e6 - never use box-shadow, never use 1px+ strokes
- Set border-radius to 0px on every interactive element; the only rounding token is the site's own --inner-border-radius for inner cutouts, not visible UI
- Reserve #ff0000 for a single accent surface per viewport; let the rest of the page stay achromatic
- Let product photography carry layout rhythm - space tiles evenly across the full viewport rather than constraining to a fixed grid column
- Set line-height to 1.0 for the 30px wordmark and 1.1-1.2 for 8px labels - tight tracking amplifies the gallery-placard feel
- Anchor a meta-strip (count + secondary affordance) to the bottom of the viewport on category pages

### Don't
- Never add background fills, gradients, or hover-color shifts to buttons - buttons remain ghost
- Never introduce a chromatic CTA button; #ff0000 is a surface accent, not an action
- Never round corners on cards, images, or buttons - sharp 0px edges define the aesthetic
- Never use body copy below 12px or above 30px; the scale is intentionally narrow
- Never add elevation (box-shadow, drop-shadow) - the system is flat and depends on hairline borders for structure
- Never use color to indicate state on links; rely on position, weight, or the Muted Grey #b2b2b2 for de-emphasis
- Never constrain the product row to a centered max-width container - let images breathe edge-to-edge

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
