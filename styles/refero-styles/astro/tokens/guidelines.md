# Guidelines

### Do
- Use 9999px radius for all interactive elements (buttons, tabs, badges, chips)
- Set the primary CTA to white background (#ffffff) with dark text (#1f232e) - inversion is the system's signature action pattern
- Use the nebula gradient (linear-gradient(83.21deg, #3245ff, #b845ed)) only for hero atmospheric backdrops and stat bars - never for buttons or cards
- Set section eyebrows (14px weight 600) in chromatic accent colors (#4bf3c8, #acafff, #54b9ff) to create the only color punctuation in each section
- Use Obviously at weight 300-400 for headlines to keep the voice whisper-confident rather than shouty
- Maintain 4px base unit for all spacing - element gaps at 8px or 16px, section gaps at 80px
- Place colored borders (1px) on circular icon containers in feature columns using Aurora Mint, Plasma Blue, or Amber

### Don't
- Don't use drop shadows for elevation - the system relies on 1px borders in slightly lighter dark shades
- Don't apply the nebula gradient to text - it destroys legibility against the dark canvas
- Don't use chromatic colors for large background fills - they break the cosmic void atmosphere
- Don't use radius values between 12px and 16px on cards - the system snaps to 8px, 12px, or 16px
- Don't set body text below 14px or above 18px - the type scale is tight to maintain the instrument-panel density
- Don't use obviously > 700 for headlines - the weight 300-400 range is the signature restraint
- Don't add decorative icons inside buttons - pills should be text-only or text + chevron

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
