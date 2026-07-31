# Guidelines

### Do
- Use #0c0c0d filled pills with 999px radius for the single primary action per screen; the rest must be ghost or text
- Keep all UI surfaces achromatic - only the artwork or the Blush-to-Violet gradient carries color
- Use 4px radius on artwork images and thumbnails at every size, 8px on text cards, 999px on any interactive element
- Set headlines in Gamma Sans Display weight 300 at 48-72px so the type reads as a watermark, not a wall
- Separate cards with 1px #e9e9ec hairlines or whitespace alone; never use box-shadow for elevation
- Use 14px #808080 weight 400 for all metadata (mint counts, prices, dates) and inline numerics in #0c0c0d weight 600 to lift them
- Maintain ~88px vertical gap between major sections and 40px between sub-blocks to let the artworks breathe

### Don't
- Do not introduce a chromatic accent color, brand fill, or saturated button - the UI must stay colorless so the artwork remains the only loud element
- Do not round artwork thumbnails beyond 4px; the sharp corner is what makes the image feel like a print pinned to a wall
- Do not use box-shadow, glow, or blur on any component - depth is communicated only by hairline borders and a single dark surface
- Do not place UI text inside a scrim or colored box over artwork; the display type must sit directly on the image
- Do not use the Blush-to-Violet gradient on buttons, navs, or borders - it is reserved for the Prints section backdrop only
- Do not mix more than two type weights on a single screen; the 300/400/600 scale is for hierarchy, not decoration
- Do not center-align body text or metadata; keep descriptions and counts left-aligned with consistent left margin to the thumbnail edge

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
