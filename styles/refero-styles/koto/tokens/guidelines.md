# Guidelines

### Do
- Set page background to #060606 (Void Black); never use pure #000000
- Use gtKotoheimCondensed weight 300 at 38-48px only for display headlines; pair with -0.48px letter-spacing at 48px
- Use gtKotoheim at 12-16px for all UI, body, and navigation text with the 'salt' font-feature enabled
- Reserve #ffe800 (Signal Yellow) exclusively for the logo mark; it must not appear in any UI component, button, or text
- Communicate elevation through lightness shifts (canvas #141414 cards), not through shadows or borders
- Keep element gaps at 8px and section gaps at 48px; the rhythm comes from these fixed multiples of the 4px base unit
- Left-align all text and let negative space carry the layout - never center body copy or add decorative dividers

### Don't
- Don't introduce any color outside the neutral scale and Signal Yellow; the system is 0% colorful by design
- Don't use filled buttons or colored CTAs; interactive elements are ghost/outlined with #ffffff borders on transparent fills
- Don't apply shadows, gradients, or blur effects to any element - the flat void treatment is non-negotiable
- Don't use radius values other than 2px, 6px, or 10px; mixing radii breaks the geometric discipline
- Don't set body copy in gtKotoheimCondensed or display in gtKotoheim regular; the two families are strictly separated by size and role
- Don't use pure #ffffff for body text - reserve it for headings, borders, and the UTC indicator; body copy uses #b4b4b4
- Don't add icons, illustrations, or imagery to the base layout; the page is typographic-first and visual assets should only appear inside Dark Surface Cards

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
