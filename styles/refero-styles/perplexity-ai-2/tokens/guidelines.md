# Guidelines

### Do
- Use 9999px border-radius for all interactive controls (buttons, nav items, toggle chips, tags)
- Maintain the narrow type scale: 12px caption, 14px body-sm, 16px body - do not introduce sizes outside this set
- Set all card and input backgrounds to #ffffff on the #faf8f5 canvas to create the paper-on-paper layering effect
- Use 1px #d1d1cd borders for all container separation - avoid shadows except the single whisper-soft card shadow
- Use #016a71 teal only for active/selected state indicators - it should appear on fewer than 5% of elements
- Keep the main content column at 640px max-width centered - the search bar is the focal point, not a wide canvas
- Use pplxSans weight 500 exclusively for emphasis and active states; weight 400 for all default and body text

### Don't
- Do not introduce new colors - the palette is deliberately minimal: cream, black, warm grays, and one teal
- Do not use bold weights (600+) - the system maxes at weight 500
- Do not use 0px or 4px border-radius on interactive elements - always pill (9999px) or 12px minimum
- Do not apply heavy shadows or multiple shadow layers - the design is intentionally flat
- Do not use pure white (#ffffff) as a page background - the warm #faf8f5 canvas is a signature choice
- Do not center-align body text - left-align all labels, descriptions, and input text
- Do not use the teal accent decoratively - it signals a functional state (active, selected, live)

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
