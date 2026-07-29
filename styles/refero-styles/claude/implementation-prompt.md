# Implementation Prompt

Build a warm parchment editorial AI-product interface in the Claude style.

Use Bone Parchment (`#f8f8f6`) as the page canvas, Paper White (`#ffffff`) for elevated cards, and Soft Stone (`#efeeeb`) for nested cards or alternate bands. Use Carbon Ink (`#121212`) for primary text, headings, icons, and dark buttons. Use Graphite (`#373734`), Ashen (`#7b7974`), and Pebble (`#9c9a92`) for text hierarchy. Use Mist (`#b7b7b5`) and Chalk (`#e7e6e1`) for hairline rules and borders. Obsidian (`#000000`) is only for the footer. Clay (`#d97757`) is only for small decorative marks, icon details, dots, or illustration accents. Never use Clay as a CTA fill or link color.

Typography is the signature. Use Anthropic Serif or a Source Serif 4/Charter/Georgia fallback only for editorial headings, at 24px or 30px, weight 400, line-height 1.2 to 1.33. Use Anthropic Sans or an Inter/IBM Plex Sans/system fallback for all other UI and copy. Keep most sans text between weight 400 and 580. Do not use 700+ weights. Body text is usually 14px/1.5 or 16px/1.63.

Use an 8px base unit. Keep the content rail around 1200px. Use 64px to 80px between sections, 32px card padding, and 8px to 12px internal element gaps. Buttons, inputs, and nav controls use 8px radius. Regular cards use 16px radius. Pricing/elevated cards use 24px radius. Shadows are optional and very soft, only on hover or featured cards.

Expected components:

- Minimal top nav on the parchment canvas with transparent nav links.
- Filled dark CTA: Carbon Ink fill, Bone Parchment or white text, 8px radius, Anthropic Sans 15px/500.
- Pricing tier card: white surface, 24px radius, 32px padding, serif plan heading, sans price/body, optional soft warm hover shadow.
- Feature benefit card: Soft Stone or Paper White, 16px radius, 24px to 32px padding, monochrome icon.
- Editorial section header: Anthropic Serif 30px/400 with short sans supporting copy.
- FAQ accordion: hairline dividers, sans text only, 24px vertical padding.
- Footer band: full-width Obsidian with muted Pebble links in compact columns.
- Clay accent mark: non-interactive decorative dot, icon detail, or illustration mark.

The page should feel printed, warm, restrained, readable, and thoughtful. Avoid cool SaaS blues, bright status colors, heavy shadows, gradients, multicolor icons, 3D renders, glossy dashboard styling, and bold display typography.
