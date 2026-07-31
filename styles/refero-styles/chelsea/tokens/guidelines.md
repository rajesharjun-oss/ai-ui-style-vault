# Guidelines

### Do
- Use #4490ff as the only chromatic color in the system - every link, every accent, every focal dot uses it
- Set all interactive elements to 9999px border-radius for the pill shape that defines the brand
- Keep the canvas pure #000000; never introduce a card surface, a gray panel, or a light section mid-page
- Let media bleed edge-to-edge with zero margin, zero radius, and zero frame
- Use Neue Haas Unica Pro weight 400 for body and weight 700 only for the wordmark and button labels
- Set headlines and body at tight line-heights (1.0-1.15) to maintain the credit-roll density
- Use 8px for element gaps and 16px for component padding; jump to 96px between major sections

### Don't
- Do not introduce drop shadows, elevation layers, or card containers - the system is flat by design
- Do not add a second accent color or any warm tone; the palette is black + white + one blue
- Do not round images or media frames - they must be sharp rectangles bleeding to the viewport edge
- Do not use #0000ee or browser-default link blue; links must be #4490ff
- Do not add a visible logo block, nav background, or header bar - the nav is text floating on black
- Do not set body type above 1.5 line-height; the credit-roll feel depends on tight leading
- Do not introduce semantic colors (green/yellow/red) for status - the system has no UI states to encode

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
