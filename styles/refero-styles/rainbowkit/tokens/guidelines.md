# Guidelines

### Do
- Use 9999px radius for every button, tag, and pill - the radius is the brand's friendliness signal
- Apply the 1px inset white border (rgba(255,255,255,0.12)) to all elevated interactive elements on Obsidian surfaces
- Use the aurora gradient (linear-gradient(to right, #3898ff, #7a70ff)) only for primary hero CTAs and the wordmark - reserving it makes it feel premium
- Default to #0e76fd for all secondary action buttons and link emphasis
- Set body copy at 16px SFRounded weight 400 with 0.27px letter-spacing; headlines at 40-52px weight 700 with 0.88-1.3px letter-spacing
- Float product cards with rgba(0, 0, 0, 0.4) 0px 8px 24px 0px - the heavy shadow is what makes a modal feel like a window into the product
- Keep the canvas at true #000000 - never warm it with off-black, the void is the point

### Don't
- Don't use the chromatic accent colors (Hyper Pink, Ember Red, Solar Orange, Toxic Green) as semantic UI states - they are demonstration options, not success/error/warning tokens
- Don't apply shadow to text or the canvas itself - shadows belong to floating cards only, the background is shadowless
- Don't use negative letter-spacing - SFRounded is designed for positive tracking; tightening it fights the rounded letterforms
- Don't introduce a second body font - SFRounded handles everything from 11px captions to 52px displays; a serif or system fallback breaks the cohesion
- Don't place white or light-colored cards on the canvas - every surface must stay in the Obsidian/Graphite range to preserve the void
- Don't use #25292 for text - it's a border color, contrast on it is insufficient for readable copy
- Don't round images of phones or product screenshots with small radii - they should be 24px+ or fully inherit the device frame

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
