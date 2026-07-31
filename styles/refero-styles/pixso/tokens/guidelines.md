# Guidelines

### Do
- Use Figtree for everything - no secondary font family, no system fallbacks in production output
- Let the page background be #faf8fd, never pure #ffffff, so cards visibly lift
- Pair a Filled Primary Button (Carbon #121212) with an Outlined Secondary Button (Mist border) in the same action row
- Reserve 8px radius for cards and nav, 12px for buttons, 18px only for prominent product frames
- Keep shadows to the signature two-layer stack: 1px hairline dark + 2-4px soft blur
- Use the Iris Sweep gradient only on the wordmark and brand-identity surfaces - never on buttons or functional UI
- Let product mockups and design kit thumbnails carry all the color; keep chrome grayscale

### Don't
- Don't introduce a chromatic CTA color - the primary action is always Carbon #121212
- Don't use heavy drop shadows or colored shadows; elevation must stay hairline
- Don't set body type below 13px or use Figtree below weight 400
- Don't add gradient backgrounds to UI surfaces; gradients belong to the logo and decorative imagery
- Don't center-align body paragraphs - the system uses left-aligned running text below the hero
- Don't use #0000ee or browser-default link blue for any interactive element
- Don't round buttons to pill (9999px); the system uses 8/12/18px radii only

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
