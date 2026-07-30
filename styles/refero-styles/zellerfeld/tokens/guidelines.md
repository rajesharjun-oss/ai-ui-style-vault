# Guidelines

### Do
- Use Roobert at -0.04em tracking for all UI text; never let letter-spacing drift to 0 or positive values
- Reserve #000aff exclusively for New In badges, the active Shop pill, and current-state indicators - no more than 3% of any screen should carry this color
- Apply 10px border-radius to all cards, buttons, inputs, and images; 30px only for pill-shaped badges
- Use Space Mono for prices, rank numerals, and 'By {brand}' credit lines - never for headlines or body
- Set product card surfaces to #ecedee (Plaster), not #ffffff, to create a gentle tier above the white canvas
- Anchor product card metadata (brand mark, name, price) to a 16-20px padding from the card edge with a consistent 40x40 brand thumbnail
- Keep the hero image full-bleed and let overlays sit on the bottom third - the shoe should be the visual subject, the UI floats on top

### Don't
- Don't introduce new chromatic colors beyond the single cobalt (#000aff) and its pale variant (#e5e7ff)
- Don't use drop shadows on product cards - the system relies on surface color stepping and 10px radius for separation
- Don't set type larger than 128px (display) or smaller than 12px (Space Mono micro labels)
- Don't use rounded radii other than 10px and 30px - no fully square corners, no fully circular elements
- Don't center body text or metadata; left-align all product information including the 'By {brand}' credit
- Don't apply color to icons - keep all line icons monochrome Ink (#111) at 1.5px stroke
- Don't separate badge variants by shape - all status badges share the 30px pill; differentiate by fill color only

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
