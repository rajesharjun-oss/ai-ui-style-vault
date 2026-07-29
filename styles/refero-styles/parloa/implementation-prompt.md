# Implementation Prompt

Build a warm editorial SaaS interface in the Parloa style.

Use Canvas Cream (`#ebe9e1`) as the page background, Paper White (`#ffffff`) for cards, and Ink Black (`#1f1c1b`) for primary text, dark navigation, and filled buttons. Use Espresso (`#2d2724`) for the announcement bar or dark secondary surfaces. Use Stone (`#a69b92`) for muted copy, Hairline (`#d9d6ce`) for borders, and Cobblestone (`#c7c1b7`) for stronger dividers. Highlighter Orange (`#ff7714`) is only for links, outlines, icon strokes, small dots, and decorative accents. Never use orange as a filled button or large background.

Typography should feel like a magazine. Use Exposure30 or a close Fraunces/Playfair/DM Serif Display fallback for headings only. Display headings at 42px and above should use weight 350 to 400, never bold. Use Geist or Inter/Manrope/system-ui for every UI and body element. Body text is 16px, weight 400, line-height 1.5, with subtle positive tracking. Buttons use Geist 14px, weight 500.

Shape is near-print-flat. Cards have 0px radius. Buttons, inputs, and tags use 2px radius. Never go above 4px. Use 4px as the base unit, 16px element gaps, 24px card padding, 80px section gaps, and a 1200px content width. Do not use shadows; separate elements with surface contrast and 1px Hairline borders.

Expected components:

- Top announcement bar: Espresso background, compact height, white copy, orange headline/link accents.
- Dark primary navigation: Ink Black or Espresso background, white Geist nav links, logo left, search/language/demo controls right.
- Hero: full-height warm-lit portrait photography with diagonal cream gradient overlay, Exposure30 82px to 96px headline in bottom-left.
- Logo trust bar: grayscale partner logos on cream, no cards.
- Feature split: left serif heading and body, right flat white preview card with Hairline border.
- Industry solution cards: white, 0px radius, Hairline border, outlined icon, serif 24px title, Geist 14px muted body, optional single orange dot on the featured card.
- Primary CTA: Ink Black fill, white text, Geist 14px/500, 2px radius, no hover lift.
- Ghost text button: transparent, Ink Black text, orange arrow or underline.

The page should feel human, premium, editorial, and warm. Avoid abstract hero illustrations, 3D renders, shadows, rounded SaaS cards, cool color fields, orange fills, and generic dashboard styling.
