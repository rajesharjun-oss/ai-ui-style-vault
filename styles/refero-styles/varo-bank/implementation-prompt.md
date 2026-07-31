# AI Implementation Prompt

Build a Varo Bank-inspired interface using this source-derived style bundle.

Reference site: https://www.varomoney.com
Theme: light
Category: Fintech
North star: neon bank statement on a sticky note - bold compressed type punched onto bright colored cardstock, held together by hairline black outlines

Use these palette anchors:

- Varo Violet `#8c58d0` for Primary action buttons, active nav, brand logo - the single saturated mid-violet that powers all interactive states
- Deep Plum `#42185f` for Dark accent surfaces, bold text on light cards, full-bleed dark band backgrounds - almost-black with violet undertone
- Lilac Mist `#cdb0fa` for Soft violet fill for selected/secondary surface states, tag backgrounds
- Coral Ember `#ed6c52` for Decorative section fills, icon highlights, dotted ticker text - warm chromatic punctuation that breaks up the violet dominance
- Salmon Wash `#f2a295` for Soft warm section background, muted coral - large-area color band that reads warm without screaming
- Butter Cream `#faefdc` for Pale cream surface band - the gentlest warm neutral, used as an alternate section background to white
- Lemon Zest `#fdf0af` for High-saturation yellow accent for card borders, feature callouts, ticker text - never a fill, always an outline or text
- Lime Pulse `#d4e84b` for Vivid lime used in feature card backgrounds and outlined graphic elements - the most attention-grabbing decorative color
- Forest Ink `#183428` for Deep green for dark feature card backgrounds and high-contrast text - rare but anchors green-themed cards
- Mustard Shadow `#4a4216` for Muted olive text and border accent on yellow/cream surfaces - never used as a fill
- Carbon `#000000` for Primary text, hairline borders, icon strokes - the dominant structural color
- Paper White `#ffffff` for Page canvas, card surfaces, button text on colored fills, inverted text on dark bands
- Soft Ash `#1c1c1c` for Near-black secondary text and borders - barely distinguishable from Carbon but used for slightly softer contrast
- Concrete `#939393` for Muted helper text, disabled states, secondary metadata
- Fog `#eff2f5` for Cool light-gray surface, pressed-button background, input field fill on dark sections

Use these typography anchors:

- Neue Haas Grotesk Display `--font-neue-haas-grotesk-display` for Body, subheads, small labels, button text, nav, form copy - the workhorse neo-grot at 12-72px. Weight 450 is the signature mid-weight for body copy; 500 for nav and labels; 400 for de-emphasized body. Letter-spacing tightens from 0.0200em at 12px to -0.0200em at 72px. Substitute: Inter, Sohne, or Neue Haas Grotesk Text Pro.
- National 2 Compressed `--font-national-2-compressed` for Display headlines only - used at 56-147px with line-height 0.80-0.95, the ultra-condensed proportions make type behave as a graphic block; weight 450 for default, 700 for maximum-impact stat callouts. Substitute: Oswald (700/600) or Antonio Bold. Letter-spacing: -0.0100em across the scale.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- Times `--font-times` for Times - detected in extracted data but not described by AI
- Metropolis `--font-metropolis` for Metropolis - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48-64px.
- Card padding: 24px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Primary CTA Button (Filled Violet): Only filled button variant - every meaningful action in the product
- Text-Only Action Button (Ghost): Secondary actions rendered as clickable text, often with an arrow
- Email Input Field: Hero and form lead-capture
- Top Navigation Bar: Persistent global header
- Hero Split Section: First screen above the fold
- Ticker Marquee Band: Scrolling trust statement / feature highlight
- Feature Card (Colored Fill): Product feature highlight in the 'Start banking better today' grid
- Split Feature Section: Product capability pages (Cash Advance, Line of Credit)
- Dark CTA Banner: Conversion closer, e.g. 'Quails apply' sections
- Footer: Legal, links, app store badges
- Stat Callout (Oversized Number): In-page emphasis on dollar amounts or key facts

Do:

- Use National 2 Compressed at 76-147px with line-height 0.80-0.95 for every display headline; never set line-height above 1.0 on display sizes.
- Apply the single violet #8c58d0 for every filled primary action - Log in link, Get started button, and Learn more all share this exact fill.
- Combine two type families only: National 2 Compressed for display, Neue Haas Grotesk Display for everything from 72px down. Never mix a third face.
- Set all radii to 4px - buttons, inputs, cards, images, and tags share the same corner radius for a uniform, sticker-like quality.
- Use 1px solid #000000 borders on every card, input, and graphic element. Color lives in fills, not strokes.
- Anchor every section with a kicker label (14-16px weight 500) above the display headline; the kicker names the product or concept.
- Tighten letter-spacing on large sizes: -0.0100em on National 2 Compressed, -0.0200em on Neue Haas Grotesk Display at 52px and above.

Avoid:

- Never use #8c58d0 as decorative fill or section background - it is reserved exclusively for interactive elements. Colored section bands use cream, salmon, plum, or lime instead.
- Never introduce drop shadows, blur effects, or multi-layer elevation. The system is intentionally flat - if a surface needs separation, add a 1px black border or a color change.
- Never mix line-heights above 1.0 with National 2 Compressed - the compressed letterforms need tight leading to read as a graphic block; open leading destroys the block effect.
- Never place a chromatic button on a chromatic section background of the same hue family - violet buttons only sit on white, cream, or dark plum.
- Never use a serif, monospace, or handwriting face - the two-family system (compressed display + neutral grotesk) is the entire typographic identity.
- Never round corners above 4px or use pill-shaped buttons; 4px is a hard rule across the system.
- Never use #0000ee or any browser-default link color; all link text and underlines are #000000 or section-matched.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
