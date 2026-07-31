# Guidelines

### Do
- Use only the nine achromatic tokens - any chromatic color in the interface breaks the system. Color belongs inside project thumbnails, not on chrome.
- Set the tightest tracking (-0.02em) on any text 27px or larger; use -0.01em below that. Tracking is the primary hierarchy tool.
- Build cards as borderless blocks with sharp corners (no radius) when the thumbnail is a solid color swatch; reserve 8px radius for cards that contain photography or compound layouts.
- Alternate between Paper White and True Black bands at 96px vertical breaks - the rhythm of light/dark is the page's structural skeleton.
- Use weight 400 for everything by default; reach 500 only for project names in cards and nav links. Never use weight 600 or above.
- Set display headings at line-height 1.00-1.05 so lines stack into a compressed slab. Body copy opens to 1.88 for breathing room - the contrast between tight display and airy body is deliberate.
- Let the 4-column project grid do the visual work: large solid-color blocks fill 1:1 tiles, with a 24px gap below for two lines of Plain 400/500 metadata in 16/13px.

### Don't
- Don't add any color to navigation, buttons, or backgrounds. The interface is 100% achromatic - color only appears inside project thumbnails.
- Don't use border-radius above 8px on cards or 4px on buttons. Sharp corners read as editorial plates; rounding undermines the gallery-catalog feel.
- Don't introduce filled buttons, outlined buttons, or ghost buttons. There is no button component - every affordance is a text link, an image, or a dot.
- Don't use weight 600+ or italic. The typeface's weight range stops at 500; anything heavier breaks the compressed-restraint language.
- Don't add icons inside body content. The only icon on the entire site is the search affordance in the nav.
- Don't use background colors on text or dividers for emphasis. Emphasis comes from size, tracking, and the Paper White / Ink contrast pair - never from color fill or tint.
- Don't use shadows, gradients, or glow effects. Elevation is communicated purely through band alternation (white black white), not through drop shadows.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
