# Guidelines

### Do
- Keep every element at weight 400 - F-Grotesk and Maison-Neue-Mono both run single-weight. Build hierarchy through size and space, never through bold.
- Let photography fill the viewport edge to edge. No internal gutters in image grids, no rounded corners, no borders around photos.
- Overlay white F-Grotesk category titles directly on imagery. Use 30px for category names, 13px monospace for 'mehr anzeigen' sub-links.
- Separate sections with warm sand (#ebe6dc) bands or 1px #000000 hairlines - never with shadows or card elevation.
- Use Maison-Neue-Mono for all functional labels: nav items, buttons, tags, footer meta. The mono face is the system's 'utility voice'.
- Let the display type breathe: 111px F-Grotesk at line-height 1.0 with generous surrounding whitespace. No letter-spacing tightening - the natural mono-influenced rhythm of F-Grotesk carries it.
- Use the 2px/6px micro-padding for all interactive elements. Buttons are stamp-sized by design, not 'small by accident'.

### Don't
- Don't introduce any chromatic color. The system is 0% colorful - adding even one accent breaks the entire monochrome contract.
- Don't use bold, semibold, or light weights. The font files are loaded at 400 only; attempting 500/600/700 will fall back or look wrong.
- Don't add shadows, glows, or blur effects. The surface model is flat - elevation is communicated by warm-band transitions, not z-axis depth.
- Don't round corners. Every radius in the system is 0px. Adding border-radius introduces a 'card' or 'button' feel that contradicts the editorial-paper aesthetic.
- Don't use sans-serif for functional labels. Monospace is reserved for nav, buttons, and meta - mixing it with F-Grotesk here dilutes the atelier voice.
- Don't crowd the 111px display with surrounding UI. Display type needs air - no buttons, links, or images in its immediate margin zone.
- Don't use colored hover states on links. Underline-on-hover in the same color is the only state change the system supports.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
