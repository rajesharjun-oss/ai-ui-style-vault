# AI Implementation Prompt

Build a Leandra-isler-inspired interface using this source-derived style bundle.

Reference site: https://www.leandra-isler.ch
Theme: light
Category: Other
North star: dried botanicals pressed into warm vellum - calm, tactile, editorial, almost reverent.

Use these palette anchors:

- Vellum Sand `#f4e6cd` for Primary page canvas - the base warm-cream that fills every section, never competing with content
- Pressed Linen `#edddc3` for Secondary surface for subtle section breaks, link backgrounds, and content cards resting on Vellum Sand
- Aged Ink `#1e211e` for Dominant text and hairline border color - near-black with a touch of warmth, used for 95% of all rules, headings, and body copy
- Charcoal Black `#000000` for Hard ink for display headings, icon fills, and the strongest contrast moments where absolute black reads better than warm
- Twilight Bronze `#8f774b` for Gradient stop - the deepest tone in the vertical vellum wash, used only inside the hero gradient
- Hayfield `#ba9d6a` for Gradient midtone - the saturated middle of the vertical wash, gives the canvas its sun-warmed depth
- Wheat Sheaf `#d6bd97` for Gradient light tone - the transition stop between the warm mid and the Vellum base

Use these typography anchors:

- PP Neue Montreal `--font-pp-neue-montreal` for The sole typeface across every screen. Body text sits at 16-20px weight 400; subheadings lift to 24-26px weight 500; display headlines scale dramatically from 75px through 122px to 158-173px at weight 500. The signature move is this extreme display scaling - the same family at 14px captions and 173px hero headlines proves the typeface can carry both whispered body copy and shouted editorial moments without switching personality.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 80-120px.
- Card padding: 0px.
- Element gap: 4-8px.

Build these component patterns where relevant:

- Top Navigation Bar: Slim, full-bleed header sitting on the Vellum Sand canvas
- Display Headline Block: The hero typography element that defines the brand
- Underlined Text Link: The only interactive UI element used in body contexts
- Botanical Hero Image: The sole visual content element - a real plant photograph
- Vellum Section Background: The base canvas for all content sections
- Section Divider Rule: The only structural break element
- Inline Body Paragraph: The primary content carrier
- Footer: Closing element with contact and legal

Do:

- Use PP Neue Montreal as the single typeface across every element - no serif, no mono, no display face
- Scale the hero headline to 122-173px weight 500 with letter-spacing -0.045em; that extreme size is the brand's loudest signature
- Let the Vellum Sand (#f4e6cd) fill the full viewport edge-to-edge with no max-width wrapper and no card panels
- Separate sections with 80-120px of vertical space plus optional 1px hairline in #1e211 - never with cards, tinted panels, or shadows
- Mark interactive elements with a 1px underline in #1e211 offset 2-4px below the baseline; never use filled buttons or pill chips
- Use real botanical photography as the only non-neutral color in the system; let leaves and stems break the viewport edges to suggest specimens pressed onto paper
- Apply the vertical 4-stop linear gradient (184deg, #8f774b #ba9d6a #d6bd97 #f4e6cd) as a subtle wash on the hero only, so the page reads as sun-warmed vellum rather than flat beige

Avoid:

- Don't introduce any new color - the system is warm sand plus near-black plus photographic green; any blue, red, or saturated accent breaks the herbalist aesthetic
- Don't use a filled, pill, or rounded button - the interface has no containers, so a button would feel alien against the flat vellum
- Don't wrap content in cards, panels, or boxed surfaces with shadows; sections are separated by space and hairlines only
- Don't use a max-width centered column for the hero headline - the display text bleeds to the viewport edge to read as editorial print
- Don't apply a dark mode or invert the palette; the Vellum Sand is the brand, not just a light-theme choice
- Don't use stock illustration, icons-as-decoration, or geometric shapes; the only visual vocabulary is typography and a real plant
- Don't set the body text below 16px or above 20px - the page intentionally uses tiny captions and massive display sizes, but the readable body stays in this narrow band

Source prompt cues:

**Quick Color Reference**
- text: #1e211e
- background: #f4e6cd
- border: #1e211e (1px hairlines only)
- accent: #ba9d6a (hero gradient only)
- primary action: no distinct CTA color

**Example Component Prompts**
1. Hero section: full-bleed Vellum Sand (#f4e6cd) with the 184deg linear gradient overlay deepening to #8f774b at the top edge. Display headline 'Praxis fur Atlaslogie und Naturheilkunde' at 158px PP Neue Montreal weight 500, letter-spacing -0.045em, line-height 0.90, color #000000, left-aligned, bleeding edge-to-edge across the viewport. A tightly cropped botanical photograph of a nettle plant positioned bottom-right with leaves extending past the viewport, no border, 4px corner radius on visible edges, no shadow.

2. Underlined text link: 16px PP Neue Montreal weight 400, color #1e211e, 1px underline in #1e211e offset 3px below the baseline. No background, no padding, no border-radius.

3. Section divider: full-viewport-width 1px hairline in #1e211e with 80px of vertical padding above and below. No other marks, dots, or gradients.

4. Body paragraph: 18px PP Neue Montreal weight 400, color #1e211e, line-height 1.5, max measure 65 characters, floating left on the Vellum Sand canvas with no container. Paragraph spacing 8px.

5. Top navigation bar: 70px tall, Vellum Sand background, no border or shadow. Left: starburst mark + 'PRAXIS / LEANDRA ISLER' stacked at 14px weight 500. Center: HOME, ANGEBOT, BLOG, UBER MICH, KONTAKT at 14px weight 400. Right: 'TERMIN VEREINBAREN ' as a 1px-underlined link in #1e211e.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
