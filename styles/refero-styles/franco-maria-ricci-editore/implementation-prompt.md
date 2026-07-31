# AI Implementation Prompt

Build a Franco Maria Ricci Editore-inspired interface using this source-derived style bundle.

Reference site: https://www.francomariaricci.com/en
Theme: light
Category: E-commerce
North star: Art Deco gallery catalogue - burnished gold hairlines on bone-white vellum

Use these palette anchors:

- Vellum White `#f6f6f6` for Page canvas - the warm off-white that grounds every section, never pure #ffffff so type never feels clinical
- Paper `#ffffff` for Card and section surfaces - book spreads, product panels, inset blocks sitting one shade above the vellum canvas
- Gallery Ink `#0a0a0a` for Dark sections (FMR Magazine block, footer band) and deepest typographic emphasis - reads as letterpress black, not screen black
- Letterpress Black `#000000` for Body copy, navigation text, icons, all hairlines and borders, pagination marks - the structural ink of the system
- Silver Wash `#b3b3b3` for Muted surface for secondary hero panels and quiet tonal breaks - used sparingly as a gallery-shadow gray
- Burnished Gold `#bc9c5c` for Section header underlines, link hover rules, decorative title borders - the only chromatic voice in the system, applied as 1px strokes and inline rules, never as fill

Use these typography anchors:

- BodoniSvntytwoITCStd-Book `--font-bodonisvntytwoitcstd-book` for Primary voice - every editorial moment. 42px with line-height 0.95 for the cinematic display headline (the tight leading lets the tall Bodoni capitals lock together as a single typographic object). 22px for section openers. 18px and 16px for body and book metadata. 14px and 12px for navigation, captions, and the monogrammed fine print. Substitute: Bodoni Moda, Bodoni 72, or Playfair Display when the ITC cut is unavailable.
- BodoniSvntytwoITCStd-BookIt `--font-bodonisvntytwoitcstd-bookit` for Editorial italics for the signature flourish - "Editore" wordmark, italic section titles like OUR SELECTION, and the quiet poetic asides. The italic is used as ornament, not emphasis: a single italic line beside a roman headline changes the register of the whole spread. Substitute: Bodoni Moda Italic, Playfair Display Italic.
- Arial `--font-arial` for System utility for pagination counters (2/5), shipping notices, form labels, and the rare inline metadata. Arial sits beside Bodoni as a quiet functional label - the contrast between high-contrast serif and neutral sans is the only typographic tension the system permits. No tracking adjustments; letterspacing inherits from the browser default.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: 1280px.
- Section gap: 48px.
- Card padding: 40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Bar Navigation: Primary site navigation
- Hero Headline Block: Opening editorial statement
- Section Title with Gold Rule: Section divider heading
- Three-Column Book Grid: Product showcase
- Book Cover Plate: Individual product object
- Ghost Link / Editorial CTA: Outlined action
- Magazine Brand Block: Branded section separator
- Pagination Indicator: Scroll progress marker
- Section Header Tab: In-grid category label

Do:

- Use Burnished Gold (#bc9c5c) only as 1px strokes: section header underlines, link hover rules, decorative title borders. Never as a fill.
- Set the display headline at 42px Bodoni 400 with line-height 0.95 - the tight leading locks the tall capitals into a single typographic block.
- Apply italic Bodoni for editorial flourishes: the wordmark subtitle, section openers, and quiet asides. Roman Bodoni carries the weight; italic ornaments it.
- Separate three-column book grids with 1px #000000 vertical rules at full column height. Gaps and padding cannot replace the rule - the dividers are the architecture.
- Keep every radius at 0px. Corners are sharp; softness comes from typography and whitespace, not from curves.
- Use #f6f6f6 as the base canvas, not #ffffff. The warm off-white prevents Bodoni from reading as clinical and keeps the system in the print-catalogue register.
- Express every action as text with a hairline bottom border. Bracketed markers like `{ ORDER NOW }` are an acceptable editorial convention for primary actions.

Avoid:

- Do not introduce drop-shadows, blurs, or glow effects. The system is flat; elevation is tonal.
- Do not use Burnished Gold (#bc9c5c) as a background fill on buttons, badges, or surfaces. It is a stroke color only.
- Do not round any corner. Buttons, cards, inputs, images all keep 0px radius.
- Do not use any secondary accent color. The palette is monochrome + one gold; introducing red, blue, or green would destroy the letterpress discipline.
- Do not use Arial for headlines or editorial copy. Arial is reserved for pagination counters, form labels, and utility metadata.
- Do not set line-height above 0.95 on the 42px display headline - the tight leading is signature, not an oversight.
- Do not add hover animations, transitions, or micro-interactions. The page reads as a printed catalogue; movement would break the metaphor.

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Letterpress Black)
- background: #f6f6f6 (Vellum White)
- card surface: #ffffff (Paper)
- border / hairline: #000000 (Letterpress Black)
- accent stroke: #bc9c5c (Burnished Gold)
- dark band: #0a0a0a (Gallery Ink)
- primary action: #bc9c5c (outlined action border)

**Example Component Prompts**

1. **Hero editorial block** - Left third: headline "Erte. Style is Everything." in Bodoni 42px weight 400, line-height 0.95, #000000. Sub-copy in Bodoni 16px weight 400, #000000, max-width 320px. Action: text link `{ ORDER NOW }` in Bodoni 14px, #000000, with a 1px #000000 bottom border. Right two-thirds: a full-height Art Deco portrait illustration, no frame, no border-radius, sitting on the #f6f6f6 canvas.

2. **Three-column book grid with section header** - Section title centered in italic Bodoni 22px #000000, followed by a 1px #bc9c5c horizontal rule spanning the full grid width. Three equal columns on a #ffffff surface, separated by 1px #000000 vertical rules running the full column height. Each column has 40px internal padding and a centered book cover image with 24px top margin. No card shadow, no radius, no caption.

3. **Magazine dark band** - Full-bleed #0a0a0a band, ~40% viewport height. Left half: a large FMR magazine cover plate, sharp corners, no border. Right half: the wordmark "FMR" in Bodoni 42px weight 400 #ffffff, centered, with "MAGAZINE" in Arial 12px letter-spaced beneath in #ffffff.

4. **Ghost navigation link with gold hover** - Top-bar link in Bodoni 14px weight 400, #000000, 4px below a 1px #000000 bottom border. On hover, both text and border shift to #bc9c5c. No background fill at any state. 40px vertical padding around the link row.

5. **Pagination indicator** - Bottom-right corner, Arial 12px weight 400, #000000, format ` 2 / 5 `. 1px #000000 horizontal rule above, aligned to the page edge with a 20px inset. No background, no border-radius.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
