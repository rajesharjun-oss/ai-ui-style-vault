# AI Implementation Prompt

Build a Netflix-inspired streaming UI. Use it as a style reference, not as a clone of the source site.

## Required Feel

The interface must feel like a dark cinema lobby with an endless content shelf. Use pure black as the base, white type for clarity, and Netflix Red as the only saturated action color. The content imagery should carry the visual density while controls remain simple and flat.

## Core Rules

- Use `#000000` for the main canvas.
- Use `#e50914` only for brand, primary CTAs, and active states.
- Use `#ffffff` for primary headings and body text.
- Use `#b3b3b3` for secondary text and footer links.
- Use Netflix Sans or a practical substitute like Roboto or Inter.
- Use a single type family throughout.
- Use 4px radius for buttons and inputs.
- Use 16px radius for large feature cards.
- Do not use box shadows.
- Use poster imagery, carousels, and dark gradients for depth.

## Suggested Page Structure

1. Minimal header with red logo on the left and language/sign-in actions on the right.
2. Full-bleed hero with dimmed poster collage backdrop.
3. Centered headline, subcopy, email input, and red CTA.
4. Trending shelf with vertical posters and oversized ranking numerals.
5. Feature grid using deep blue-purple gradient cards.
6. FAQ or expandable rows on graphite/black surfaces.
7. Footer with silver links.

## Component Recipes

Hero CTA:

- Background: `#e50914`.
- Text: `#ffffff`.
- Font: Netflix Sans, 700, 24px.
- Radius: 4px.
- Padding: 16px 24px.

Header sign-in button:

- Background: `#e50914`.
- Text: `#ffffff`.
- Font: Netflix Sans, 500, 14px.
- Radius: 4px.
- Padding: 4px 16px.

Language or secondary header button:

- Background: `rgba(0, 0, 0, 0.4)`.
- Border: `1px solid #808080`.
- Text: `#ffffff`.
- Radius: 4px.
- Padding: 6px 16px.

Email input:

- Background: `rgba(22, 22, 22, 0.7)`.
- Border: `1px solid #5a5a5a`.
- Text: `#ffffff`.
- Placeholder: `#808080`.
- Font size: 16px.
- Radius: 4px.
- Padding: 20px 16px.

Feature card:

- Background: `linear-gradient(149deg, #192247, #210e17)`.
- Radius: 16px.
- Padding: 24px.
- Heading: 24px, weight 900, white.
- Body: 16px, weight 400, white.

Trending poster card:

- Vertical poster aspect ratio.
- Poster art fills the card.
- Large ranking number at lower-left, 100px, weight 900.
- No decorative frame beyond what is needed for focus states.

## Do Not

- Do not use any saturated accent besides Netflix Red.
- Do not use light or gray page backgrounds.
- Do not add card shadows.
- Do not outline primary buttons.
- Do not crowd the header with navigation.
- Do not use multiple type families.
- Do not make the cards soft, bubbly, or SaaS-like.

