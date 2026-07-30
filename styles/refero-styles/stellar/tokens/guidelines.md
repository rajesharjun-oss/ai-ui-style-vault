# Guidelines

### Do
- Use Sprint Violet (#6a48f2) only for the primary CTA fill, active link state, and focused input border - its scarcity is the design
- Set all display headlines at weight 400, never bold. The 70-104px scale carries authority through size, not stroke weight
- Apply -0.02em letter-spacing at 70px+ display sizes and +0.035-0.040em on small uppercase eyebrows - the contrast between tight display and open labels creates the type system's character
- Use 10px radius on designer cards and 50px pill radius on buttons - these two radii define the geometric language; avoid anything in between
- Layer surfaces at #000000 #171718 #2c2c2 - each step is one shade of difference, creating depth without illumination
- Keep subtext and supporting copy at 18-19px in Ash (#888888) so the display headline remains the loudest element on every screen
- Set page max-width to 1200px and center content - the void extends to the viewport edges but typography stays in a controlled measure

### Don't
- Do not introduce a second chromatic accent - Sprint Violet is the only color, and adding another dilutes the system
- Do not use bold (weight 600+) on any headline - weight 400 at large sizes is the signature; bold would break the hushed tone
- Do not add box-shadows to cards or buttons - depth comes from the #000000 #171718 surface contrast, not elevation shadows
- Do not use light gray (#f3f3f3, #e9e9e9) as a page background - the entire system depends on pure void black as the canvas
- Do not use 8px or 12px border-radius on cards or buttons - the system only uses 6px (inputs/nav), 10px (cards), and 50px (buttons/links)
- Do not set body text below 15px - the type scale starts at 14px for captions only; 15-16px is the readable minimum
- Do not place white or violet text directly on a #6a48f2 background without testing contrast - use white-on-violet for the CTA text only, never decorative

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
