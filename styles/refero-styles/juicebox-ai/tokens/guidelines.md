# Guidelines

### Do
- Use #6a2f8d Royal Plum exclusively as a brand accent - hero washes, active states, product frames, the submit button on the search bar, and the announcement banner. Never use it for body text or for more than one element on a single screen.
- Set all display headlines (40-72px) in Roobert 400 with letter-spacing between -0.03em and -0.04em. The aggressive negative tracking is the signature - do not relax it.
- Use DM Mono with 0.077em tracking for every section eyebrow label, tab label, and technical tag. The mono face signals 'this is metadata, not prose'.
- Default to 2px border-radius on every interactive element - buttons, inputs, cards, tags, and product frames. Square edges are part of the system's engineering posture.
- Build the page surface stack in three tiers only: Parchment #f8f6f8 (page) Paper #ffffff (cards) Plum Mist #eee8fd (accented sections). Use surface lightness, not shadows, to imply elevation.
- Pair Filled Dark CTA (#2a232a) and Outlined Ghost Button (1px #1d161d border) at identical dimensions and padding so they read as a matched set side-by-side in every feature section.
- Set body copy at 14-18px in Haas Grot 400 with line-height 1.43-1.56 and tracking -0.01em. Never go below 14px or above 1.56 line-height for paragraph text.

### Don't
- Don't use #000000 for text - use #1d161d Obsidian. Pure black fights the warm Parchment canvas and breaks the system's subtle violet undertone.
- Don't round corners above 2px. The system is intentionally rectangular; pills, 8px, or 12px radii immediately read as a different product.
- Don't introduce drop shadows on cards or sections. Elevation comes from the two-tier Parchment-to-Paper surface, not from box-shadow. The single inset shadow rgba(0,0,0,0.5) 0 0 12px inset is reserved for active/pressed button states only.
- Don't use Royal Plum #6a2f8d as a text color on white backgrounds. It fails contrast for body copy; reserve it for headings on Plum Mist, for buttons, and for decorative elements.
- Don't combine Roobert with a different display face, and don't set headlines at weight 700. The single 400 weight is the whole signature - bolding a headline breaks the editorial tone.
- Don't add new saturated colors. The palette is intentionally near-monochrome with one brand purple, one green emphasis, and one lilac outline. Introducing teal, red, or amber immediately dilutes the system.
- Don't use color for body text emphasis. Use Obsidian #1d161d bold for inline emphasis and the green #2f8d6 only for individual highlighted words, never for full sentences.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
