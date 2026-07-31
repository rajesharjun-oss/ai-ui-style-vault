# AI Implementation Prompt

Build a Acceptandproceed-inspired interface using this source-derived style bundle.

Reference site: https://www.acceptandproceed.com
Theme: light
Category: Agency
North star: editorial broadsheet on warm paper

Use these palette anchors:

- Ink `#000000` for Primary text, hairline borders, icon strokes, badge outlines, card outlines - the only structural line color in the system
- Paper Warm `#f9f7f3` for Page canvas, card surfaces, body backgrounds - the warm cream base layer for all content
- Bone `#ecebe7` for Raised surfaces, pill button fills, input fills, link backgrounds - one step warmer/darker than the canvas for tactile depth without shadows
- White `#ffffff` for Headline color on dark hero overlays, card highlight wash, inverted surface accents
- Graphite `#8c8c8c` for Secondary borders, muted metadata text, badge secondary text and borders - the warm mid-gray step in the neutral scale
- Ash `#a2a1a1` for Tertiary badge borders and subtle dividers - the lightest structural gray for the quietest separators
- Charcoal `#333333` for Input text and form field copy - softer than pure black for longer reading inside form contexts

Use these typography anchors:

- Messina Sans `--font-messina-sans` for The only workhorse typeface - used for everything from micro-labels (8px) to display headlines (72px). Weight 400 is the sole weight; hierarchy is created entirely by size and line-height, never by weight contrast. This produces a quiet, editorial voice where the type whispers at every level rather than shouting with bold.
- Letterformvariations 04 Dmgx `--font-letterformvariations-04-dmgx` for Decorative display face used very sparingly for typographic moments - an experimental or contrast voice to break the Messina Sans monotony, reserved for editorial flourishes only

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 64px.
- Card padding: 12px.
- Element gap: 8px.

Build these component patterns where relevant:

- Pill Button (Primary): Primary action button for CTAs like 'See More' and 'Listen'
- Medium Radius Button: Secondary action button
- Project Card: Featured project tile in a 2-column grid
- Outlined Tag Badge: Category label for projects (Technology, Design, Digital, Climate, Space)
- Audio List Row: Tabular row in the Endless Vital Activity podcast/audio catalogue
- Text Input: Form field for user input
- Full-Bleed Hero: Above-the-fold section image
- Top Navigation: Global site navigation
- Section Header: Label for content sections like 'Featured Projects'
- Project Description Block: Long-form description under a project title

Do:

- Use weight 400 of Messina Sans for every piece of type - from 8px captions to 72px headlines. Never introduce a bold or medium weight; hierarchy comes from size alone.
- Use only the warm cream palette: #f9f7f3 for canvas, #ecebe7 for raised interactive surfaces, #000000 for text and hairlines. No chromatic colors of any kind.
- Use 100px border-radius for all primary action buttons and input fields. Pills are the dominant button shape.
- Use 8px border-radius on project images and card containers. This subtle rounding keeps the print-like crispness while avoiding sharp corners.
- Separate content sections with 1px #000000 hairline borders, not colored bands or background changes. The page reads as connected paper, not segmented panels.
- Let photography fill the full viewport width in hero and feature sections. The image is the page; type and chrome step back.
- Use the 3.4px border-radius on all badges and tag chips. This is a signature micro-radius - not fully rounded, not sharp - that reads as editorial label.

Avoid:

- Don't introduce bold, semibold, or any non-400 weight. The single-weight system is the entire typographic voice; a bold headline would break the editorial whisper.
- Don't add any color - no blue links, no red errors, no green success states. Every state change uses #000000 #8c8c8c opacity shifts, or #f9f7f3 #ecebe7 surface steps.
- Don't apply drop shadows or box-shadows to any element. Depth is communicated by surface color and hairlines only.
- Don't use a border-radius outside the four-tier system: 3.4px (badges), 8px (cards/images), 20px (secondary buttons), 100px (pills/inputs). No 4px, no 12px, no 16px.
- Don't use uppercase tracking or letter-spacing increases for labels. The -0.01em tightening is consistent across the type scale - never widen it.
- Don't add icons, illustrations, or decorative graphics. Photography is the only imagery; everything else is type and hairline structure.
- Don't use colored hover states. Hover changes on links and buttons should toggle between #000000 and #8c8c8c text/border, or swap #ecebe7 #f9f7f3 surface inversion.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
