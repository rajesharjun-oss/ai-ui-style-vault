# AI Implementation Prompt

Build a Clase bcn-inspired interface using this source-derived style bundle.

Reference site: https://clasebcn.com
Theme: light
Category: Agency
North star: editorial gallery on white wall

Use these palette anchors:

- Paper White `#ffffff` for Page canvas, card surface base, text on dark cards
- Ink Black `#000000` for Primary text, hairline borders, nav labels - the structural anchor of every element
- Carbon `#0a0a0a` for Secondary text and deep surfaces where pure black reads too harsh
- Concrete `#939393` for Muted navigation labels, secondary link text, inactive nav state
- Ash `#aaaaaa` for Tertiary link borders and subdued annotation text
- Plaster `#e8e8e8` for Subtle surface division, alternating card backgrounds
- Sumi `#0a0000` for Near-black project card background - reads as deepest neutral
- Slate Night `#262a36` for Project card background - slightly cool dark, content-driven not UI
- Terracotta Blush `#efccbe` for Project card background - warm content fill, not a UI accent
- Verdant `#43d491` for Project card background - vivid content fill, not a UI accent

Use these typography anchors:

- SuisseIntl-Regular `--font-suisseintl-regular` for SuisseIntl-Regular - detected in extracted data but not described by AI
- Suisse Int'l `--font-suisse-intl` for Single typeface at a single weight carries the entire interface - navigation, body, and display. The refusal to use a bold or italic weight forces hierarchy through size, line-height, and whitespace alone. The variable line-heights (1.11 for tight display stacks, 1.79-2.44 for body) show that this one weight is stretched across very different densities.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 100px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal text-only site header
- Statement Headline: Opening page declaration
- Full-Bleed Project Card: Portfolio case study entry
- Photographic Project Card: Image-led portfolio entry
- Text Link with Arrow: The only interactive element in the system
- Footer: Minimal page closer

Do:

- Use Suisse Int'l (or a neo-grotesque substitute like Inter) at weight 400 for every element - no bold, no italic, no second family
- Let project imagery and project color fills carry all visual variety; keep all UI chrome in #000000 and #ffffff
- Use 20px padding consistently for all text-block insets (navigation, card text, footer)
- Separate projects with 100px vertical breathing room - let each card exist in its own visual silence
- Mark every interaction as a plain text link with a arrow, never as a filled or outlined button
- Scale hierarchy through font size and line-height only - 24px for body, 28px for subtitles, 45px for display
- Keep border-radius at 0 across all elements - corners are sharp, the page is a grid

Avoid:

- Don't introduce buttons, pills, chips, or any filled interactive component - this system has no buttons
- Don't add shadows, gradients, or border effects to cards or images - surface depth comes from color contrast alone
- Don't use bold or semibold weights - weight 400 is the only voice; hierarchy is size-only
- Don't use #43d491, #efccbe, or #262a36 as UI accents - they belong only inside project card backgrounds
- Don't add a logo mark, wordmark treatment, or branded icon - the word 'Cl' in the nav is the entire identity mark
- Don't constrain the layout to a max-width container - project cards must be full-bleed
- Don't add hover animations, transitions, or micro-interactions - the site reads as static, like a printed catalogue

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
