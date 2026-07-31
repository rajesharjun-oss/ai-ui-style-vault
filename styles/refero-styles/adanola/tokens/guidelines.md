# Guidelines

### Do
- Use Favorit at all UI touchpoints - navigation, buttons, product names, headings - with 0.025em letter-spacing as the brand's defining typographic fingerprint
- Set primary actions as ghost/outlined buttons (1px #000000 border, transparent fill) - filled black is reserved for compact secondary actions like Quick Add
- Keep all border-radius values at 0px for product cards, images, and tags; use 4px only for buttons and inputs - the crisp rectangular geometry is core to the editorial lookbook feel
- Let product photography provide all color on listing and editorial pages - the UI chrome should stay near-monochrome (white surfaces, black text, #e5e7eb alternation) so garment hues read as the only chromatic accents
- Use compact 4px-based spacing (4/8/16/24px) for UI elements, then break to generous 64px+ section gaps to create the calm editorial rhythm between product grids
- Anchor the product card layout to a 4-column desktop grid with images that fill card width edge-to-edge - no card containers, no shadows, no borders around product images
- Apply the black announcement bar (#000000 bg, white 9px Favorit text) as a persistent strip above the nav for promotions and shipping messages

### Don't
- Do not introduce drop shadows or box-shadow elevation on any component - the design system is deliberately flat and relies on whitespace and hairlines for separation
- Do not use saturated brand colors for buttons, links, or interactive states - keep the action palette strictly black/white/outline
- Do not round product card images or product card containers - the sharp rectangular edges are signature to the lookbook treatment
- Do not use display serifs, script fonts, or decorative typefaces for headings - the whisper-weight regular Favorit at 30px is the hero voice
- Do not add gradient backgrounds, colored section bands, or decorative patterns to page sections - alternation should be subtle (#e5e7eb, #f0efe7, #f5ebd5) at most
- Do not add icon containers, badges, or pill shapes around UI elements - tags and labels should be plain text with optional hairline underlines
- Do not use large border-radius values (8px+) on any element - the entire system is anchored to 0px and 4px radii only

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
