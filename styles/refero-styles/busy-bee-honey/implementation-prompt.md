# AI Implementation Prompt

Build a Busy Bee Honey-inspired interface using this source-derived style bundle.

Reference site: https://www.busybeehoney.com
Theme: mixed
Category: E-commerce
North star: painted barn-side honey label - dark cocoa, gold, and blue stacked like a vintage billboard. Two sentence grounding: massive condensed serif display type bleeds edge-to-edge against solid color bands, and the bear-bottle product sits centered and unframed like the hero of a roadside sign.

Use these palette anchors:

- Dark Cocoa `#3b2722` for Primary canvas for hero/header, body text on light surfaces, structural borders, dark CTA fills - the most-used chromatic color in the system, carrying 80%+ of text and border weight
- Cream Parchment `#f2ebd0` for Light canvas for alternate sections, text on dark canvases, hairline borders, card surfaces - the warm off-white that makes the dark cocoa feel like printed kraft paper
- Charcoal `#000000` for Hard-edge text and fine borders where absolute contrast is required
- Honeycomb Gold `#ffca50` for Filled CTA buttons on dark sections, full-bleed section canvas, nav fill - the most chromatic and warmest surface, used as functional punctuation against the brown
- Barn Red `#a0342a` for Red outline accent for tags, dividers, and focused UI edges.
- Cornflower Blue `#6aacc2` for Marquee band background, secondary nav fill - the sky/honey-sky blue used as a thin chromatic strip between full-bleed color blocks
- Sage Green `#6fa162` for Subtle accent strip alongside the blue in marquee/decorative bands - an herb-garden green that keeps the blue from feeling isolated

Use these typography anchors:

- TayMakawao `--font-taymakawao` for Mega-display headlines - 'KNOW YOUR HONEY'-scale type that bleeds edge to edge, set tight (0.80 lh) with -0.01em tracking so letterforms lock together like wooden cutout letters
- Barkman Honey `--font-barkman-honey` for Secondary display and large numerals - the 'honey drip' serif used for sub-headlines and hero subtext (e.g. 65px section titles), its warmer curves pair against TayMakawao's mechanical weight
- TayBirdie `--font-taybirdie` for UI and small-body workhorse - nav links, footer text, micro-labels, and small caps. Normal tracking keeps it legible at small sizes; the tightest 1.00 lh is reserved for nav rows
- Times New Roman `--font-times-new-roman` for Fallback body text inside the system, also pulls double duty for italic-as-brand-voice moments where a system serif feels more honest than a designed face
- Anonymous Pro `--font-anonymous-pro` for Monospaced flavor for traceability codes, lot numbers, and any 'data' moment that should feel like a printed receipt - positive 0.031em tracking gives the text a stamped/inked feel
- Arial `--font-arial` for Button and micro-copy fallback - the utilitarian text inside pill buttons where neutrality beats the warmer display faces

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Navigation Bar: Top-level site navigation
- Scrolling Marquee Band: Section divider and emphasis strip
- Mega Display Headline: Hero and feature section titles
- Section Subhead: Supporting headline below mega display
- Pill CTA Button (Dark on Light): Primary action on gold/light sections
- Pill CTA Button (Yellow on Dark): Primary action on dark sections
- Product Hero Bottle: Centered product showcase within a hero section
- Circular Badge / Trace Seal: Decorative stamp element
- Bee Glyph: Decorative motif
- Full-Bleed Color Section: Page-level section container
- Footer: Site-level footer

Do:

- Set mega display at 90px or larger with line-height 0.80-0.82 and letter-spacing -0.01em - anything taller than body, anything less tight, and the headline stops sounding like billboard lettering
- Let every primary action be a 1000px-radius pill; never round the corners partially
- Use full-bleed color sections (Dark Cocoa, Honeycomb Gold, Cornflower Blue) with no inter-section gap - the seam between colors is the layout
- Place the product photo centered and unframed; never wrap it in a card, never add a shadow, never constrain it to a column
- Invert CTA fill against the section it's on: dark pill on gold, gold pill on dark - never a dark pill on dark
- Use the blue (#6aacc2) only as a marquee band or thin strip - it is a divider color, not a surface
- Reserve the barkmanhoney 65px subhead for the second-most-important line on a section; don't promote it above the TayMakawao display

Avoid:

- Don't introduce drop shadows, glows, or any z-axis elevation - the system is deliberately flat
- Don't set display type with line-height 1.0; tight leading is the signature, not an accident
- Don't put a card, border, or container around the hero product - the bottle sits on the canvas
- Don't use white (#ffffff) for canvas; the cream (#f2ebd0) is warmer and intentional
- Don't use a sans-serif display face - the system only works with the condensed serif 'painted sign' attitude
- Don't use Sage Green (#6fa162) for text or buttons - it is a marquee-strip accent only
- Don't break the full-bleed section into a max-width container with side gutters - bleed to the edge or it loses the billboard quality

Source prompt cues:

**Quick Color Reference**
- text: #3b2722 (on light) / #f2ebd0 (on dark)
- background: #3b2722 (dark canvas) / #ffca50 (gold section) / #6aacc2 (marquee strip)
- border: #3b2722
- accent: #a0342a (barn red - subhead emphasis)
- primary action: #ffca50 (filled action)

**Example Component Prompts**
1. *Hero section*: Full-bleed Dark Cocoa (#3b2722) canvas. Centered TayMakawao 209px / line-height 0.80 / letter-spacing -2.09px headline in Cream Parchment (#f2ebd0) that bleeds past the viewport. Centered product photo of the bear bottle at 50% viewport height, no border, no shadow, sitting on the cocoa canvas.
2. *Gold feature section*: Full-bleed Honeycomb Gold (#ffca50) canvas, 40px internal top/bottom padding. Left-aligned Barkman Honey 65px / line-height 1.0 subhead in Barn Red (#a0342a), a small Cornflower Blue circular trace badge above it. Dark Cocoa pill CTA (1000px radius, 16px x 24px padding, Arial 13px caps in #f2ebd0) with a right-arrow icon.
3. *Marquee band*: Full-bleed Cornflower Blue (#6aacc2) strip, 56px tall. Inline TayMakawao 28px / line-height 1.0 caps text in Dark Cocoa repeating 'MADE IN THE USA' separated by a 14px Dark Cocoa bee glyph, animated left-to-right infinite scroll.
4. *Mega display headline*: TayMakawao 135px / line-height 0.82 / letter-spacing -1.35px, color Cream Parchment (#f2ebd0), set on a Dark Cocoa (#3b2722) full-bleed section. Text overflows its container horizontally - do not constrain.
5. *Navigation bar*: Dark Cocoa (#3b2722) background, full-width, 20px vertical padding. TayBirdie 12px all-caps links in Cream Parchment (#f2ebd0), separated by 36px horizontal padding, distributed across a single row.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
