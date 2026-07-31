# AI Implementation Prompt

Build a A24-inspired interface using this source-derived style bundle.

Reference site: https://a24films.com
Theme: mixed
Category: Media
North star: opening title sequence on pure black

Use these palette anchors:

- Obsidian `#000000` for Section backgrounds for dark bands, primary body text on light surfaces, hairline borders and dividers throughout - the structural backbone of every page
- Paper White `#ffffff` for Light section backgrounds, card surfaces, product image containers, modal/overlay panels, primary text on dark backgrounds
- Ash Gray `#eeeeee` for Subtle surface variant for product showcase panels and soft background shifts on light sections
- Smoke `#888888` for Muted secondary text, subdued nav labels, low-emphasis borders - sits just above AA contrast for accessibility
- Bone `#cacaca` for Light hairline borders on white surfaces, minimal separator lines, very low-emphasis UI strokes

Use these typography anchors:

- NB International Web `--font-nb-international-web` for Primary typeface for all UI - navigation, body copy, headings, and display film titles. Weight 400 carries body and most UI; weight 500 for emphasis. The 74px display size with tight tracking (-0.04em) and 0.92 line-height lets film titles stack in dense, almost poster-like blocks. The humanist proportions and slight warmth make it readable at 11px yet commanding at 74px - the same family spans the entire voice.
- NB International Mono Web `--font-nb-international-mono-web` for Monospaced companion for technical labels, year markers beside film titles, and code-like annotations. Used sparingly as a typographic accent that signals data/specification context.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 96px.
- Card padding: 22px.
- Element gap: 9px.

Build these component patterns where relevant:

- Top Navigation Bar: Persistent header across all pages
- Film Title Block: Hero and film-list display
- CTA with Arrow: Section navigation links
- Product Showcase Card: Merchandise display
- Email Signup Modal: Newsletter capture overlay
- Email Input Field: Text capture within modal
- Sign Up Button: Form submission in modal
- Podcast Feature Block: Audio content promotion
- Search Icon Button: Search trigger in nav
- Hamburger Menu Trigger: Primary navigation open
- Scroll Indicator Arrow: Vertical scroll prompt at page bottom

Do:

- Use #000000 and #ffffff as the only meaningful background and text values - alternate full-bleed black and white sections to create visual rhythm
- Set display headlines to 74px with NB International weight 400, line-height 0.92, letter-spacing -2.96px, letting titles stack with zero vertical gap
- Use NB International Mono at 15px for year labels and technical annotations - pair flush-right with display titles
- Apply 0px border-radius to every component - cards, buttons, inputs, modals, images. Sharp edges are non-negotiable
- Use NB International at 10-11px with 0.14em tracking for all uppercase labels (nav items, category tags, form labels)
- Separate form inputs and buttons with shared borders (input has left/top/bottom border, button is solid fill) to create a single connected control
- Let the page be full-bleed with no max-width constraint - let type and image define the grid

Avoid:

- Do not introduce any color, gradient, or chromatic accent - the palette is strictly achromatic
- Do not use border-radius on any element, including images and product cards
- Do not apply box-shadow, drop-shadow, or any elevation effect - depth comes from value contrast alone
- Do not center-align body copy or film titles - everything reads left-aligned
- Do not use font-weight above 500 - NB International's range is restrained on purpose
- Do not add decorative elements, dividers, or ornamental graphics between content blocks
- Do not use a second typeface family beyond NB International Mono - the mono variant is the only permitted departure

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
