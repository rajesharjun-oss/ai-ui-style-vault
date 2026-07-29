# Guidelines

## Do

- Use #fbff2b fill with 1px #1a1a1a border exclusively for the single primary action per screen never use the yellow as a background for large surfaces or decorative blocks.
- Set all text at -0.03em letter-spacing using the Neue Haas Grotesk Text scale (14/16/17/20/24/42px) do not introduce a second typeface or loosen tracking at display sizes.
- Apply 10px border-radius to buttons, nav elements, and inputs; reserve 16px for larger card surfaces and info banners.
- Build vertical rhythm on the 6px base unit: 8px between list items, 12px for element gaps, 16px for card padding, 48-96px for section separation.
- Use #f4f4f4 as the only mid-surface between white and the yellow accent never introduce additional gray tints or gradient washes.
- Keep page layout centered with a 1200px max-width and 111px left margin for content blocks; let white space carry the visual weight.
- Communicate hierarchy through weight (400 vs 500), not color or size variation the system has exactly two weights and a tight type scale.

## Do Not

- Don't introduce drop shadows, glow effects, or blur elevation is flat and border-defined.
- Don't use #fbff2b on more than one element per viewport its power comes from scarcity.
- Don't add a second accent color; the palette is monochrome + one yellow-green signal.
- Don't use Ash Gray (#a3a3a3) for body copy it's a 2.5:1 contrast fail on white; reserve it for placeholders and inactive metadata only.
- Don't increase border-radius above 16px the slightly squared geometry is part of the identity.
- Don't break the 6px spacing grid with arbitrary pixel values; every gap should be a multiple of 6.
- Don't add a subtitle or eyebrow text above page headings the 42px heading stands alone.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
