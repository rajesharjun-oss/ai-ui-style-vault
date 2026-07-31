# Guidelines

### Do
- Use Terracotta (#a9553c) and Lilac Veil (#ddbdea) only as full-bleed panel fills - never as button backgrounds, never as text colors, never as borders.
- Let letter-spacing grow with size: 0.01em at 15px, 0.024em at 35px. Never set negative tracking on headlines.
- Keep all type at weight 400 except the rare 700 micro-label. Weight contrast is a resource - spend it sparingly.
- Build the page as a strict grid of edge-to-edge tiles. White canvas between tiles is the gutter - no margins, no shadows, no hairlines.
- Use 0px border-radius on all panels and cards. Reserve 5px for buttons and 9999px only for pill tags.
- Pad panel interiors with 25px on all sides. Headlines sit 25px from the panel edge - flush, never floating.
- Pair every colored panel with a single short text element (headline + optional inline arrow link). Never stack multiple components inside a panel.

### Don't
- Don't soften black to near-black or add a tint - #000000 is absolute and the system depends on that contrast.
- Don't introduce a third chromatic color, a gradient, or a neutral mid-gray. The two-color discipline is the brand.
- Don't add shadows, glows, or elevation to cards. The grid is flat - surfaces sit on the page, not above it.
- Don't use negative letter-spacing on any size. The positive tracking is a signature, not a mistake to correct.
- Don't round card or panel corners beyond 0px. The sharp 90 edges are what make it feel like editorial print.
- Don't mix multiple typefaces or weight the headlines at 600-700. Theinhardt 400 everywhere, plus rare 700 for micro-tags.
- Don't create centered, max-width containers. The grid is full-bleed; content fills its tile completely.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
