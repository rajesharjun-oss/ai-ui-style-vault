# Guidelines

### Do
- Use only #000000 and #ffffff - every surface, every border, every character is one of these two values.
- Reserve RomieLigatures for display moments only: site wordmark, section titles, marquee bands, and track names at 65px+. Never use it for UI labels or metadata.
- Use LifeLTStd 18px as the single body/nav/label size across the entire site - do not introduce a type scale beyond the four documented roles.
- Separate every content block with a 1px solid white hairline that spans 100% viewport width with no padding gap.
- Set display type at 167px with line-height 0.73 so stacked lines nearly touch - this density is the editorial signature.
- Enable discretionary ligatures ("dlig" on) on all RomieLigatures usage - the fused letterforms are the brand's most recognizable visual element.
- Use 15px padding for all internal spacing within bands and 40px between major content sections.

### Don't
- Never introduce color - not for hover states, not for active nav, not for error messages, not for decorative accents.
- Never use border-radius - all corners are square (0px). This includes buttons, images, and tags.
- Never apply box-shadow or drop-shadow - elevation is expressed through white hairlines and negative space, not depth.
- Never use bold or semibold weights - both typefaces operate at 400 only. Emphasis comes from size contrast, not weight.
- Never use RomieLigatures for body copy, labels, timestamps, or anything below 65px - the decorative ligatures become illegible at small sizes.
- Never add background fills, gradients, or colored overlays to poster images - keep them raw grayscale with only a white border.
- Never center-align body text or metadata - left-align for content, right-align only for timestamps and durations.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
