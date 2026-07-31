# Guidelines

### Do
- Use #008fff as the full-viewport canvas for every top-level section - never place the headline on a white card with a blue background behind it; the blue IS the surface.
- Flip one or two words inside a 52px Honk Header headline to #ffe400 to create emphasis. Never underline, italicize, or bold the highlighted word - color is the only differentiator.
- Set all body copy in Honk Sans at 16-19px with the negative tracking values from the type scale (-0.018em at 16px, -0.006em at 19px) - the tightened grotesque is part of the voice.
- Use the 16px-radius token for any white panel embedded in the blue field (notification banners, content cards, image containers) and the 6px-radius token for small pills or chips.
- Place the phone mockup on the right side of the hero at 45-55% column width, surrounded by 2-3 floating white speech-bubble decorations - never center it, never add a drop shadow.
- Use #3fcc6b green exclusively inside the phone screen for product-internal UI; keep the marketing surface to the blue/yellow/white trio only.
- Keep icon strokes at 2px in Honk Sans weight, white on blue - icons are line-style, never filled, never chromatic.

### Don't
- Don't use white or light-gray page backgrounds for marketing screens - the design system assumes the blue field is always present, so a white page reads as broken.
- Don't use #ffe400 for body text, button backgrounds, or large fill areas - Signal Yellow is a word-level highlight only, not a surface color.
- Don't introduce a third saturated color to the marketing surface (purple, red, orange) - only the blue field, yellow accents, white text, and the green inside device mockups are permitted.
- Don't use heavy drop shadows on cards, buttons, or the phone mockup - elevation comes from color contrast against the blue, not from shadow stacks.
- Don't split the headline across more than 3 lines or highlight more than 2 words with yellow - the system relies on a single punctuation moment, not scattered emphasis.
- Don't use a different font family for sub-headings, buttons, or links - Honk Sans at varied weights covers the entire UI; Honk Header is display-only.
- Don't use the 6px-radius token on cards or large panels, and don't use the 16px-radius token on buttons - keep small-radius on small elements, large-radius on large surfaces.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
