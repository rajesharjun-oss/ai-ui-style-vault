# Guidelines

### Do
- Set all interface text in NaN Holo Mono with 0.075em tracking - the monospace + tracking combo is what reads as 'NaN UI' versus generic mono
- Use #262626 for text and borders, never #000000 for UI chrome - pure black is reserved for the heaviest display specimens
- Let display specimens bleed to viewport edges without a max-width clamp; the type defines the lateral scale
- Use the aurora gradient button (29.4px radius) exactly once per page - the gradient is rationed because it's the only warm element
- Mark every new section with a hollow circle bullet ( ) in 14px NaN Holo Mono, followed by 60-80px vertical space
- Make specimen cards self-documenting: render the card's font name IN that font, not as a label
- Keep all elevation to 1-2px hairline borders in #262626 - never introduce drop shadows

### Don't
- Don't use #ffffff as a page surface - it kills the mint canvas identity
- Don't use #000000 for body text or UI borders - it fights the pastel canvas
- Don't set the Holo Mono tracking below 0.05em - the letter-spacing is what makes the mono read as deliberate UI
- Don't introduce additional accent colors - the palette is mint, lime, carbon, and the aurora gradient, nothing else
- Don't add drop shadows to cards or buttons - the site defines depth through borders and whitespace only
- Don't use a 4px or 8px radius on cards - the 18px card radius is the signature soft-corner language
- Don't wrap display specimens in centered containers; full-bleed is what makes the type feel architectural

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
