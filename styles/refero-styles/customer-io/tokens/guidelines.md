# Guidelines

### Do
- Use 2px border-radius on all cards, inputs, images, and containers - pill shapes (9999px) are reserved exclusively for buttons
- Use weight 475 for all text including 96px display headlines - never bold above 600 except for 20px subheadings
- Use 1px solid #ebebeb hairline borders for card edges and dividers - never thicker
- Color individual words in display headlines using #863d1c (orange), #123a88 (blue), #41a251 (green), #b52473 (pink) - words stay inline, never separate blocks
- Use #abffae exclusively for primary CTA fills and focus glow rings - never as body text or background tint
- Use 24px for element gaps, 32px for card padding, 96px for section vertical gaps - the 4px base unit scales through these three tiers
- Use #fffcf6 as the default light surface; alternate to #032125 for dark sections; tint with #e2f4ff, #fdf0e9, or #eafde8 for semantic accent bands
- Use 4px colored focus glow rings (0px 0px 0px 4px) for interactive focus states instead of outline or shadow changes

### Don't
- Never use drop shadows for elevation - depth comes from colored 4px glow rings only
- Never use bold weights above 600 for display or heading text - the signature is the calm 475 voice
- Never use corner radius above 2px on non-button elements - sharp-cornered cards define this system
- Never use #0000ee or default browser blue for links - links use #032125 or #a1c2c6
- Never place #abffae on white or light backgrounds without sufficient contrast - it is a glow color, not a fill
- Never use more than 4 columns in content grids - the system favors generous spacing over density
- Never use the heading accent colors (#863d1c, #123a88, etc.) for UI chrome - they exist only for inline keyword coloring in display text

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
