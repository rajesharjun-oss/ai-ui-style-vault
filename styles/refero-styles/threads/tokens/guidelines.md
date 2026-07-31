# Guidelines

### Do
- Use Ink Black (#000000) for all primary text and structural icon strokes - let the weight of black carry the hierarchy
- Apply Meta Blue (#385898) exclusively to hyperlinks, verification badges, and icon accents - never as a filled surface or large block of color
- Set border-radius to 1000px on every avatar, button, and badge to keep the pill/circle vocabulary consistent
- Separate posts with a 1px Cloud Gray (#d5d5d5) bottom border, not with card backgrounds or spacing alone
- Wrap the feed in a single 640px-max-width container with 18px radius and the 12px 4%-opacity shadow halo
- Type body copy at 15px/400 system-ui with 1.4 line-height; reserve 600 weight for usernames and navigation labels
- Keep all interactive controls borderless - express state through color shifts (Ash Gray Ink Black) rather than fills or borders

### Don't
- Don't introduce a second chromatic color - the system is monochrome plus one blue, and adding another breaks the newspaper discipline
- Don't use colored or gradient fills on buttons, cards, or surfaces - the only filled surface is the Ink Black Log in button
- Don't use shadows on individual post cards - the single elevation halo belongs to the feed container only
- Don't render text larger than 20px - the system operates in a 12-17px window and oversized type breaks the compact rhythm
- Don't use a webfont when system-ui renders natively - replacing it with a custom face shifts the personality away from neutral utility
- Don't put borders or backgrounds on sidebar icon buttons - they must read as a column of marks on a blank rail
- Don't round card corners above 8px for embedded link previews or media - large radii on those elements compete with the feed container's own 18px curve

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
