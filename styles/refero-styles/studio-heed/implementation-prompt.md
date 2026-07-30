# AI Implementation Prompt

Build a Studio HEED-inspired interface using this source-derived style bundle.

Reference site: https://www.studioheed.com
Theme: dark
Category: Agency
North star: midnight gallery wall - black exhibition space with hairline white frames and tiny precise labels

Use these palette anchors:

- Void `#000000` for Page canvas, dominant card surface - the near-black that absorbs the eye and lets project imagery carry all visual weight
- White `#ffffff` for Hairline borders, text, link borders, and the 124 link borders form the white wireframe structure of every tile and section
- Midnight Navy `#00174f` for Accent card surface and decorative panels - the only chromatic hue in the system, used sparingly as a deep tonal interruption against the void
- Cement `#c2c1bf` for Alternate card surface - a warm desaturated gray that breaks the black/navy rhythm when a tile needs to feel physical or grounded

Use these typography anchors:

- Suisse Intl `--font-suisse-intl` for Exclusive display and body font - the studio's signature is deploying a weight 600 grotesque at a whisper-small 12-14px for absolutely everything, from navigation to project labels to body copy. This uniform micro-size is anti-convention; most agencies use a dramatic type scale, but HEED treats 12-14px weight 600 as a single visual register, like a single monospace that carries every function.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 14px.

Build these component patterns where relevant:

- Project Gallery Tile: Primary content unit - the exhibition piece hanging on the gallery wall
- Project Caption Label: The two-line label identifying each gallery tile
- Studio Header Block: Top-of-page identity, navigation, and contact information
- Nav Link: Primary site navigation items
- Language Toggle: Bilingual site switcher
- Contact Info Line: Email, phone, and social handles displayed in the header
- Description Paragraph: Studio self-description below the header identity
- Gallery Row: Horizontal strip of project tiles

Do:

- Use #000000 as the default page canvas for every section - the void IS the brand
- Apply 5px border-radius to every card, image, and interactive surface - never deviate
- Keep all type at 12px or 14px weight 600 Suisse Intl - the micro-type register is the signature
- Maintain 14px gaps between gallery tiles and between stacked metadata lines
- Use #ffffff for all text and hairline borders - the white wireframe IS the UI structure
- Present projects as equal-height tiles in a horizontal row, separated by 14px gaps
- Let the four surface colors (void, white, midnight navy, cement) carry all visual variety - no gradients, no shadows, no decorative elements

Avoid:

- Never add drop shadows, elevation, or glow effects to any surface
- Never use a type size larger than 14px - the micro-type register is non-negotiable
- Never introduce additional colors beyond the four surface tones - the palette is closed
- Never use soft radii (8px+) or pill shapes (9999px) - 5px is the only radius in the system
- Never use font weights below 600 - the uniform semibold weight carries the entire voice
- Never add underlines, backgrounds, or color differentiation to active nav states
- Never use gradients, photographic backgrounds, or illustrated section dividers between content blocks

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
