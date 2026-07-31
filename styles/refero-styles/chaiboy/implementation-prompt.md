# AI Implementation Prompt

Build a CHAIBOY-inspired interface using this source-derived style bundle.

Reference site: https://wearechaiboy.com
Theme: dark
Category: E-commerce
North star: black gallery wall with a single illuminated photograph.

Use these palette anchors:

- Void `#000000` for Page canvas, hero background, footer background - the absolute ground everything else sits on or within
- Carbon `#131313` for Subtle surface variation from the page canvas - used as a near-identical lifted surface where one is needed without breaking the monochrome spell
- Ash `#afafaf` for Secondary text, muted labels, inactive input borders - a half-step between white and black for elements that must recede
- Bone `#ffffff` for Primary text, hairline rules, link and button borders, image borders - the only forward-facing tone, used with restraint as both type and geometry

Use these typography anchors:

- Neue Haas Grotesk TP 55 Roman `--font-neue-haas-grotesk-tp-55-roman` for Sole typeface for all interface text - navigation, body, headlines, buttons, footer. The exclusive use of weight 400 is a deliberate anti-hierarchy choice; scale and spacing do the work that weight normally would. The OpenType 'case' feature is enabled site-wide, giving all-caps small text properly designed uppercase parentheses, hyphens, and numerals instead of lowercase glyphs scaled up.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 60px.
- Card padding: 16px.
- Element gap: 5px.

Build these component patterns where relevant:

- Announcement Ticker Bar: Scrolling promotional strip across the top of every page
- Primary Navigation Row: Main site navigation
- Text Link: All clickable navigation, footer, and inline references
- Bordered Chip Button: Promotional micro-CTA inside the announcement ticker
- Hero Photograph Frame: Full-bleed editorial image that defines the page
- Footer Link Bar: Bottom-of-page legal and contact links
- Cart Link: Shopping bag entry point in the nav
- Brand Wordmark: Logo lockup in the top-left of the nav

Do:

- Use #000000 as the page background everywhere; let #131313 appear only when a true surface lift is needed without breaking the monochrome language.
- Set all interface text in Neue Haas Grotesk 55 Roman at weight 400 only, with font-feature-settings: 'case' on to keep all-caps forms typographically correct.
- Use only the four documented sizes - 11, 14, 18, 54 - to build hierarchy. No weights beyond 400.
- Use #ffffff for primary text, hairline rules, and the 1px borders that separate regions; use #afafaf only when a label must visibly step back.
- Keep all border-radius at 4px across buttons, cards, chips, and inputs - the system has one radius and it should not be overridden.
- Let product or editorial photography carry the visual weight; the chrome should be invisible. Frame hero imagery with a 1px white border on black.
- Separate major regions (announcement, nav, footer) with a 1px solid #ffffff hairline rule rather than background-color changes or padding alone.

Avoid:

- Do not introduce any chromatic color - no brand accent, no semantic red/green/blue, no hover tint. The system is monochromatic by conviction.
- Do not use font-weight above 400, and do not add italic. Weight contrast is not available as a hierarchy tool.
- Do not use box-shadow, gradients, or glow effects. Surfaces are flat black; depth comes from hairline borders and photography only.
- Do not use border-radius larger than 4px. Pills, fully rounded shapes, and large curves are outside this system.
- Do not use backgrounds or fills on nav links, buttons in the main flow, or cart. The bordered chip is the only filled/bordered interactive shape, and it belongs only in the announcement bar.
- Do not underline links or change their color on hover. Text links are distinguished by position, context, and cursor only.
- Do not set type below 11px or use centered body copy. Small text is always uppercase, tight-leading, left-aligned in rows.

Source prompt cues:

Quick Color Reference:
- text: #ffffff
- background: #000000
- border: #ffffff (1px hairlines)
- muted text: #afafaf
- accent: none - the system is monochromatic
- primary action: no distinct CTA color

Example Component Prompts:
1. Create the primary nav row: black #000000 background, 1px solid #ffffff top and bottom rules. Left: 'CHAIBOY' wordmark in 14px Neue Haas Grotesk weight 400 uppercase #ffffff. Center: nav links BLENDS, COCKTAILS, VALUES, STUDIO at 14px weight 400 uppercase #ffffff, 15px gaps. Right: 'CART' link at 14px weight 400 uppercase #ffffff. No fills, no borders on the links themselves.
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
3. Create the hero photograph frame: centered on the #000000 page canvas, constrained to roughly 60% of the page width, 1px solid #ffffff border on all sides. The image is a black-and-white high-contrast portrait. No caption, no overlay, no gradient - just the framed photograph on void.
4. Create the footer link bar: #000000 background, 1px solid #ffffff top border. Left row at 11-14px weight 400 uppercase #ffffff: TERMS & CONDITIONS, PRIVACY POLICY, CONTACT, INSTAGRAM with 4-6px gaps. Right row: NEWSLETTER link and a time string (e.g. '22:50') in the same treatment.
5. Create a bordered chip button: #000000 background, 4px border-radius, 1px solid #ffffff border, 7px padding top/bottom and 10px padding left/right. 11px Neue Haas Grotesk weight 400 uppercase #ffffff text. Used only inside the announcement ticker.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
