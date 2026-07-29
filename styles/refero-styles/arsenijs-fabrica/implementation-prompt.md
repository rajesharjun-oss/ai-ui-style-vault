# AI Implementation Prompt

Build a Arsenijs Fabrica-inspired interface using this source-derived style bundle.

Reference site: https://www.arsenijsfabrica.com
Theme: light
Category: E-commerce
North star: Editorial beauty spread under gallery lights. Pure-white gallery walls, a single warm strobe pulsing orange against the monochrome, type set thin as glass and hung with generous negative space.

Use these palette anchors:

- Ember Orange `#f15730` for Filled CTA buttons, primary action backgrounds - deep saturated orange that reads as confident rather than playful, the only color with enough chroma to anchor a click target against the white field
- Tangerine Blaze `#f7651a` for Promotional surface fills (email capture modal, featured product cards, stat callout backgrounds) - slightly brighter and more luminous than Ember, used where orange must own an entire region of the layout
- Apricot Whisper `#ff8562` for Borders on outlined cards, link underlines, icon strokes, accent hairlines - the lightest orange, functioning as a warm-tinted structural color rather than a fill
- Graphite Black `#111111` for Body text, default borders, the dominant structural color - a true near-black, not warm, used for the bulk of hairline rules and paragraph copy
- Inkwell `#0d1717` for Heading text, navigation text, primary headings - a deep black with the faintest cool-green undertone that gives headlines a quiet cast against pure white
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark/orange surfaces - the unchanging ground tone across every section
- Mist Gray `#eeeeee` for Soft card borders, hairline dividers on white surfaces where Graphite would feel too heavy
- Smoke `#818181` for Secondary captions, muted helper text, subdued icon strokes - the only mid-gray in the palette, used sparingly to fade metadata without going fully light

Use these typography anchors:

- Onest `--font-onest` for Sole brand typeface. The 200-300 weights at display sizes (48-152px) define the editorial couture voice - thin strokes hung on a white wall with aggressive negative letter-spacing. Weights 400-500 handle body and UI; 600-800 reserved for occasional emphasis. Substantial negative letter-spacing contracts large text to the width of small, producing the 'cut from a single line' effect. Substitute with Inter or General Sans if Onest is unavailable.
- Times `--font-times` for Times - detected in extracted data but not described by AI
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Announcement Bar: Slim black strip delivering free-shipping and gift-purchase notices
- Main Navigation: Sticky header carrying logo, primary links, and utility icons (search, account, cart)
- Hero Overlay Section: Full-bleed product photography with display headline and CTA overlaid
- Pill CTA Button (Primary): Filled action button for checkout, subscribe, and 'shop now' actions
- Pill CTA Button (Ghost/White): Secondary action overlaid on imagery or orange surfaces
- Pill Button (On Orange Modal): Form submit button inside the email capture modal
- Email Capture Modal: Centered overlay prompting newsletter signup with 10% discount
- Outlined Product Card: Grid card for product listings with orange hairline border
- Stat Callout Block: Large-percentage proof point (e.g. '98% natural ingredients')
- Feature Row: Horizontal list of trust signals with line-art icons (leaf = natural, rabbit = cruelty-free)
- Close Button (Modal X): Dismisses the email capture overlay
- Navigation Icon Button: Utility actions in the header (search, account, cart)

Do:

- Set all display sizes (48px and above) in Onest weight 200-300 - the whisper-weight headline is the brand's editorial signature
- Use letter-spacing in negative em values across the entire type scale, tightening to -0.091em at 152px display
- Reserve Ember Orange (#f15730) for filled buttons and Tangerine Blaze (#f7651a) for entire promotional surfaces; never mix them in the same component
- Use Apricot Whisper (#ff8562) for 1-2px hairline borders on cards and link underlines - not for fills
- Apply 600px border-radius to every button and 30px to every input - the pill is non-negotiable for actions
- Default card corners to 10px and product image corners to 15px
- Use Mist Gray (#eeeeee) for borders only on white surfaces where Graphite would feel too heavy

Avoid:

- Don't apply box-shadows to cards, buttons, or modals - the system communicates depth with borders and color alone
- Don't use Orange for body text - its contrast on white fails accessibility, keep it for fills, borders, and large display numbers only
- Don't use weights 600-800 for body text or UI labels - reserve them for the rare emphasis moment
- Don't introduce a second accent color or hue - the orange must remain the single chromatic note
- Don't use 0px or 4px border-radius on cards or images - the 10px/15px minimum is part of the soft editorial feel
- Don't center product card text - left-align all UI copy; centering is reserved for the hero overlay and modal content
- Don't apply gradients to surface fills - the only observed gradient is a single progress-bar indicator on a dark surface

Source prompt cues:

**Quick Color Reference**
- text: #111111 (body) / #0d1717 (headings)
- background: #ffffff
- border: #111111 (structural) / #ff8562 (accent hairlines)
- accent: #ff8562 (borders, icons, links)
- primary action: #f15730 (filled action)
- promotional surface: #f7651a (modals, featured blocks)

**Example Component Prompts**

1. Create a Primary Action Button: #f15730 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Email capture modal**: Centered on dimmed page. Background #f7651a, 10px radius, ~480px wide. Header heart icon (2px #ffffff stroke) + 'skincare community' in Onest 300 italic 32px #ffffff. Body copy Onest 400 16px #ffffff. Email input: transparent, 2px #ffffff border, 30px radius, 13px 20px padding. Submit button: background #ffffff, text #f15730, 600px radius, 15px 48px padding, Onest 500 16px. Close X top-right: 2px #ffffff lines.

3. **Product card**: Background #ffffff, border 1.5px #ff8562, 10px radius, 20px padding. Product image fills card width. Title below in Onest 500 16px #0d1717. No shadow.

4. **Stat callout**: '98%' in Onest 200 at 152px #111111, line-height 0.90, letter-spacing -13.83px. Label 'Percentage of natural ingredients' in Onest 400 14px #818181 directly beneath. No background, no border.

5. **Trust signal row**: Horizontal inline list. Each item: 20px line-art icon in #111111 + 10px gap + label in Onest 400 14px #111111. 40px gap between items. No background fill.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
