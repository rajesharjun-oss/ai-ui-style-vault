# Guidelines

### Do
- Use pill-shaped buttons (800px radius) for every interactive element - never square or slightly-rounded buttons
- Let project cards own color: pick one vivid hex from the accent set per card, keep the rest of the page in warm neutrals
- Set body copy at 18px in area-normal 400 - the system reads at editorial size, not product-UI size
- Anchor all headlines in Ink Black (#1d1e19) and let the canvas (#f8f9f3) carry the warmth - never introduce white
- Reserve 40px radius exclusively for hero and feature surfaces; cards stay at 8px to maintain the gallery hierarchy
- Apply the heavy 0 28px 80px shadow only to hero blocks and project cards - the depth comes from a small number of well-placed shadows, not constant elevation
- Use OC Highway at 10px with +0.10em tracking for micro-labels and timestamps - the tracked uppercase is a signature detail

### Don't
- Don't use the chromatic accent palette for buttons, nav, or text - they belong only to project card backgrounds
- Don't mix multiple vivid colors on the same card or section - one color field per surface
- Don't introduce pure black (#000000) as a fill - Ink Black (#1d1e19) is the system black, the tiny warm shift is the difference
- Don't use more than one shadow tier per page level - the heavy shadow is for cards/hero, the faint one for inputs, nothing else
- Don't set body text below 18px - the system is editorial, not data-dense
- Don't use Cobalt Violet (#204ce5) for anything other than a single filled primary action - it's the system's only chromatic action and overuse flattens its meaning
- Don't round inputs at 8px - the 3px input radius creates a deliberate contrast with the pill buttons and is part of the system language

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
