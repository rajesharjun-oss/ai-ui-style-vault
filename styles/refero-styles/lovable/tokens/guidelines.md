# Guidelines

### Do
- Use 9999px border-radius for all buttons, badges, and pill-shaped controls - the full-pill shape is the signature interactive affordance
- Keep the palette almost entirely achromatic; reserve chromatic color exclusively for the hero gradient and semantic states - never for buttons, links, or UI accents
- Apply -0.025em letter-spacing globally across all text sizes; this tight tracking is a defining characteristic of the type system
- Use #f7f4ed (Warm Sand) for card surfaces and #fcfbf8 (Parchment) for the page canvas - the two warm whites create the surface hierarchy
- Use weight 480 for headings and weight 400 for body text - this subtle weight contrast (not bold vs regular) defines the typographic hierarchy
- Set 'liga' 0 in font-feature-settings on all text to disable ligatures, matching the original type rendering
- Use 1px solid #eceae4 for all borders - dividers, card outlines, input strokes, nav separators - one warm beige border color everywhere

### Don't
- Never use cool grays (#e5e7eb, #6b7280) - all neutrals skew warm with a yellow undertone; cool grays would break the parchment atmosphere
- Never apply colored backgrounds to buttons; the primary action is near-black (rgba(0,0,0,0.88)) and secondary is transparent - there is no colored CTA
- Never use drop shadows for elevation except on the chat input card; most cards and surfaces are flat with no shadow at all
- Never use more than one font family - Camera Plain Variable (or its substitute) handles everything from 14px captions to 60px display headlines
- Never use sharp corners (0px radius) on interactive elements; even image thumbnails get 12px radius
- Never use the hero gradient colors on individual UI components like buttons, badges, or icons - the gradient exists only as a full-bleed atmospheric background
- Never add visual weight to feature sections with icons, colored badges, or decorative elements - this system communicates through type weight and scale alone

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
