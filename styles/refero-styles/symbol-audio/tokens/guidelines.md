# Guidelines

### Do
- Use #1c3c27 as the page canvas for every section band - the entire site lives inside this single color, section transitions are invisible.
- Pair the Chalet serif for all body, nav, prices, and badges with SupremeLL-Bold for every heading - never mix roles.
- Set product card backgrounds to #fffffd (Frost White) with 0px radius and a hairline #dfe2e5 border - the card is a placard, not a tile.
- Use 9999px border-radius for every badge, tag, and pill button - sharp corners everywhere else.
- Anchor display headlines to the left edge and let them run large (52-80px) with -0.02em tracking in SupremeLL-Bold.
- Place the announcement marquee fixed to the bottom viewport edge with the evergreen fill - it never scrolls away.
- Use #000000 text on frost-white cards and #dfe2e5 text on evergreen - maintain the 16:1+ contrast ratio at all times.

### Don't
- Do not introduce a filled solid-color button - this system only uses outlined/ghost actions on transparent fills.
- Do not use the blue (#447cf0) or red (#c72a00) as functional UI colors - they are decorative photography accents only.
- Do not apply border-radius to product cards or hero images - the system is sharp-edged everywhere except pills and badges.
- Do not set body text in SupremeLL-Bold - the sans is exclusively for display and headings.
- Do not add box-shadow or drop-shadow to cards or images - surfaces are flat, the contrast comes from color, not elevation.
- Do not use pure #ffffff for surfaces or text - the system runs #fffffd (frost) and #dfe2e5 (pewter) for its lightest tones.
- Do not break the marquee pattern - the announcement ticker is always present, always fixed, always evergreen-on-pewter.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
