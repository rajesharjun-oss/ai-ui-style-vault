# Guidelines

### Do
- Use only the three neutral values plus the single dusty-rose card color - never introduce a new hue, the system is intentionally monochrome
- Set display name text at 238px with line-height 0.80 and -0.04em letter-spacing to reproduce the editorial masthead effect
- Use 9999px radius exclusively for nav pill chips - all other elements stay at 0px radius
- Keep all image tiles edge-to-edge with no padding, no rounded corners, and no shadows - the grid is the layout, not a container
- Anchor the central name card with #e8c4c0 background and 38px padding on all sides as the single non-monochrome surface
- Use custom serif at weight 300-400 for all display text - never substitute a sans-serif headline, the serif is the brand
- Maintain 6px gap between nav chips and 2px between image grid cells to keep spacing tight and structural

### Don't
- Do not add any new color - no blues, greens, or warm tones beyond the single blush card background
- Do not use border-radius on cards, images, or content containers - only pill nav chips get radius
- Do not apply shadows or elevation effects to any component - the system is flat, relying on color contrast and grid structure for depth
- Do not add gradients of any kind - the palette is solid only
- Do not use sans-serif for headlines or display text - the custom serif at extreme sizes is the signature element
- Do not constrain the image grid with a max-width container - the grid must be full-bleed edge-to-edge
- Do not add header navigation, footers, or sidebar chrome - the floating name card and bottom pill row are the entire navigation system

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
