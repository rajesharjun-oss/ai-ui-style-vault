# AI Implementation Prompt

Build a Flecto-inspired interface using this source-derived style bundle.

Reference site: https://flecto.io
Theme: mixed
Category: SaaS
North star: Botanical greenhouse glasshouse. A warm cream-walled conservatory where deep teal planters hold bright mint seedlings - flat, rounded, alive with green, zero shadows.

Use these palette anchors:

- Forest Ink `#004737` for Dominant brand surface - hero panels, section backgrounds, thick structural borders, nav header, footer blocks. Deep teal absorbs the page and makes cream text glow
- Mint Pulse `#56f09f` for Green outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Mint Mist `#d4ffe8` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Cream Canvas `#fffbec` for Page background - warm off-white replaces pure white. Border-color on teal sections, card fills on light areas, heading text on dark surfaces
- Deep Loam `#032019` for Text color on cream surfaces, subtle dark borders. Near-black with a green undertone that harmonizes with the Forest Ink brand color
- Sage Whisper `#99b5af` for Muted body text and secondary borders - desaturated green-gray that recedes on cream while staying tonally consistent with the brand palette
- Stone Mist `#ccdad7` for Hairline dividers, icon borders, subtle background tints on cards within light sections
- Bone `#faf2d5` for Soft warm card background - slightly warmer and more saturated than cream canvas, used to lift specific content blocks without breaking the tonal family
- Charcoal `#222222` for Body text and standard button borders in neutral contexts. Used when chromatic text is not appropriate
- Iris Spark `#8f37ff` for Violet outline accent for tags, dividers, and focused UI edges.

Use these typography anchors:

- Aeonik `--font-aeonik` for Universal typeface - headings, body, UI labels, buttons. Single weight 400 across the entire system; contrast is achieved through size and negative letter-spacing, not weight. This is the signature choice: a monoweight geometric sans where display headlines at 56-74px tighten to -0.043em while body text at 14-16px sits at normal or slightly positive tracking. Tabular numerals ('tnum') are enabled for all instances.
- roobert `--font-roobert` for Secondary body face - used for longer descriptive copy, list items, and hero subtext. Warmer and more humanist than Aeonik, providing tonal variety in long-form text while staying in the same single-weight, geometric family.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 40-80px.
- Card padding: 12-20px.
- Element gap: 10-12px.

Build these component patterns where relevant:

- Filled Mint Button: Primary call-to-action (Login, Start)
- Outlined Dark Button: Secondary action (Book a Demo)
- Ghost Pill Button: Tertiary action or filter
- Hero Panel: Full-bleed dark section
- Light Card: Content card on cream canvas
- Tinted Feature Card: Highlighted content block
- Language Selector: Compact utility dropdown
- Navigation Bar: Top-level site nav
- Decorative Shape Module: Brand illustration element
- Footer Section Block: Dark footer column
- Icon Glyph: UI icon system
- Circular Action Button: Floating utility (download, scroll)

Do:

- Use Aeonik at weight 400 for all text - never introduce bold or light weights; let size and negative tracking create hierarchy
- Apply -0.043em letter-spacing at 56px and above; tighten to -0.030em at 32-36px; open up to +0.020em at caption sizes 8-12px
- Use Forest Ink (#004737) for hero backgrounds and primary structural borders; never use it as a small accent - it is a surface color
- Reach for Mint Pulse (#56f09f) only on filled buttons, active icons, and decorative shapes; its rarity is the system
- Set borders at 1-2px using Forest Ink on dark sections and Stone Mist (#ccdad7) on light sections instead of adding shadows
- Set page background to Cream Canvas (#fffbec) - never pure #ffffff for the base canvas
- Use border-radius 40px on all buttons, 19px on cards, and 9999px on pill tags

Avoid:

- Don't introduce additional font weights - the monoweight system is the signature
- Don't use Mint Pulse (#56f09f) as a large surface area - it loses punch; keep it to button-sized and icon-sized moments
- Don't add drop shadows beyond rgba(0,0,0,0.04) 0px 3px 2px 0px - the flatness is intentional
- Don't use pure #ffffff as the page background - the cream warmth is load-bearing for the botanical feel
- Don't apply gradients - the system is strictly flat color blocks
- Don't use #8f37ff (Iris Spark) as a functional color - it is decorative only and should appear rarely
- Don't center-align body copy or lists - only headlines; body text stays left-aligned for reading rhythm

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
