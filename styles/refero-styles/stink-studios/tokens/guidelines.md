# Guidelines

### Do
- Use 52px Helvetica weight 300 for any logo or hero wordmark, with -2.08px letter-spacing to compress the caps into a cinematic block
- Reserve 60px Times New Roman weight 400 for editorial statements and manifesto copy - never for navigation, labels, or body
- Apply 0.10em positive letter-spacing to all Courier New 14px text (tags, badges, index numbers) to read as slate-marking texture
- Let the page canvas be #000000 universally - do not introduce light section bands; the system is monochrome by intention
- Use 20px gap between navigation links and 60px minimum margin-top between major editorial sections
- Set every image to full-bleed (100vw) with 0px radius when it is the section's primary content
- Signal interactivity through a 1px white bottom border appearing on hover - never through color shifts or background fills

### Don't
- Do not introduce colored buttons, colored backgrounds, or gradient UI elements - the accent palette belongs to the work, not the chrome
- Do not use box-shadow or elevation on cards, buttons, or navigation - this system is deliberately flat; depth comes from imagery, not stacking
- Do not use rounded corners on cards or work tiles - 0px radius is the signature; rounded containers would break the cinematic frame
- Do not combine the serif display (Times New Roman) with the monospace (Courier New) on the same line or within the same component
- Do not add light-mode toggle, theme switcher UI, or alternate color schemes - dark is the only mode
- Do not use font-weight above 700 for Helvetica - the system lives in the 300-700 range; black weight would break the whisper-thin display logic
- Do not pad work cards with internal whitespace - imagery bleeds to the cell edges, and titles overlay the image directly

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
