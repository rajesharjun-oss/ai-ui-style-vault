# Guidelines

### Do
- Use 9999px radius for all interactive pills, tags, and the video play button - full rounding is the default for anything that triggers an action
- Set display headlines at 112px in Exposure Variable weight 300 with line-height 0.85 - the vertical compression is the signature, never loosen it
- Use 0.1em letter-spacing on all uppercase eyebrows and step numbers in ABC Favorit Mono at 13px - the tracking creates the editorial chapter-marker rhythm
- Apply 1px solid borders (28 uses) rather than shadows to define card edges - borders are the primary depth cue, shadows are reserved for floating elements only
- Place buttons as floating elements with 20px radius (not full pill) for primary CTAs, reserving 9999px for secondary pill controls
- Use the --student-marquee spectrum gradient sparingly - once per page maximum, as a section divider or hero accent, never as a fill
- Maintain 80px section gaps and 2.19 line-height on body text - generous spacing is non-negotiable for the editorial feel

### Don't
- Do not use bright saturated colors as background fills - the system is 96% achromatic; the only permitted color washes are lime (#f2fcb3) and saffron (#ffdc5c) in small editorial zones
- Do not set headlines at weight 600-700 - Dia speaks at weight 300 for display and 650 for subheadings; bold weights break the whisper-tone voice
- Do not use border-radius values outside the defined set (12, 16, 20, 24, 9999px) - improvised radii destroy the visual coherence
- Do not use multi-layer drop-shadow stacks on cards - the 3-layer filter is reserved for product screenshot windows only; regular cards use 1px borders
- Do not place colored buttons on colored backgrounds - the system uses black text on white/linen or white text on black, never chromatic fills
- Do not use line-height below 1.25 for any text - even the compressed 112px display keeps 0.85 only because the font is custom-designed for tight vertical fit; do not replicate this with system fonts
- Do not add hover transforms (scale, translate) to buttons - the system transitions only color, border, and opacity at 0.2s ease

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
