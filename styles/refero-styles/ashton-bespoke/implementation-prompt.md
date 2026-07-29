# AI Implementation Prompt

Build a Ashton Bespoke-inspired interface using this source-derived style bundle.

Reference site: https://www.ashtonbespoke.co.uk
Theme: light
Category: Other
North star: Stone cathedral of craftsmanship - warm parchment surface, one whisper of burgundy, letterspaced serif that breathes.

Use these palette anchors:

- Burnt Wine `#38141b` for Footer background, sectional dark bands, atmospheric accent - the sole chromatic note in an otherwise achromatic palette, used sparingly to anchor gravity
- Ink Stone `#262626` for Primary text, hairline borders, image frames, nav links - the structural near-black that defines every edge and label
- Warm Parchment `#e0ded8` for Dominant page canvas, section backgrounds, card surfaces - warm stone tone that gives the site its gallery-like, hand-made feel
- White `#ffffff` for Elevated surfaces, inverted text on dark sections, nav text over imagery, subtle highlight washes

Use these typography anchors:

- Arial `--font-arial` for Body text fallback - sparse usage suggests it appears in long-form paragraphs where readability supersedes brand expression
- Legquinne VF `--font-legquinne-vf` for Display and heading serif - the single voice of the brand. Variable font allows optical weight tuning per context. Custom typeface; no system equivalent.
- Basis Grotesque Pro `--font-basis-grotesque-pro` for Navigation links, small caps-style captions, and compact body labels - the quiet supporting sans that stays out of the serif's way
- Basisgrotesquepro 500 `--font-basisgrotesquepro-500` for Basisgrotesquepro 500 - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 120px.
- Card padding: 32px.
- Element gap: 24px.

Build these component patterns where relevant:

- Full-Bleed Cinematic Hero: Opening statement section
- Monogram Brand Mark: Brand identity anchor
- Editorial Statement Block: Centered mission/manifesto display
- Split Image-Text Section: Two-column editorial layout
- Transparent Top Navigation: Site navigation
- Hairline-Bordered Image Frame: Image presentation
- Wine Footer: Closing section
- Underlined Inline Link: Text-level navigation
- Section Anchor Tag: Section divider indicator

Do:

- Set headlines in Legquinne VF (or Cormorant Garamond) at 32-60px with tracking between 0.017em and 0.031em - the wide letter-spacing is signature, not optional
- Use #e0ded8 as the dominant canvas for at least 60% of the page; it is the brand's defining surface
- Reserve #38141b exclusively for the footer or at most one dark section per page - its power depends on scarcity
- Keep interfaces borderless or use 1px solid #262626 hairlines only; never apply shadows, gradients, or rounded corners larger than 4px to UI elements
- Let photographs be full-bleed or edge-to-edge with no decorative frame beyond a 1px border; the image is the component
- Use generous vertical rhythm: 80-120px between sections, 24-32px between text blocks - editorial spacing, not app spacing
- Pair the serif display with Basis Grotesque Pro for all navigation, labels, and captions; never substitute a slab or geometric sans

Avoid:

- Do not introduce bright or saturated colors - the palette is deliberately achromatic with one wine note
- Do not apply border-radius larger than 4px to cards, images, or buttons; the editorial feel requires sharp geometry
- Do not use shadows, glows, or blur effects on any UI element; depth comes from photography and spacing, not elevation
- Do not set the serif below 24px or above 60px - the typeface is designed for display scale, not body or billboard
- Do not center body paragraphs or use justified text; body copy is left-aligned at line-height 1.40
- Do not add icons, badges, tags, or decorative elements; the site is typographic and photographic, not symbolic
- Do not use button fills or background colors on interactive elements; links are text-only with underlines

Source prompt cues:

**Quick Color Reference**
- text: #262626 (Ink Stone)
- background: #e0ded8 (Warm Parchment)
- border: #262626 (Ink Stone, 1px hairline)
- accent: #38141b (Burnt Wine) - footer/atmospheric only
- white: #ffffff - elevated surface, text on dark
- primary action: no distinct CTA color

**Example Component Prompts**
1. *Full-bleed hero*: 100vh background video or image, no overlay chrome. Centered headline at 60px Legquinne VF weight 500, #ffffff, letter-spacing 1.86px, line-height 1.10. Single line, sentence case in small caps style. Transparent nav floats above with white 'ASHTON BESPOKE' wordmark left, four white text links right.

2. *Editorial statement block*: Full-width parchment (#e0ded8) section, 200px vertical padding. Centered interlocking 'AB' monogram at 80px, #262626. Below: two-line serif headline at 46px Legquinne VF, line-height 1.10, tracking 1.01px, #262626. Caption at 15px Basis Grotesque Pro, tracking 0.32px, #262626, centered, 32px gap above.

3. *Split image-text section*: Two-column 50/50 layout, no gap between columns. Left column: heading at 46px Legquinne VF + three short body paragraphs at 16px Arial, line-height 1.40, #262626, 24px gap between paragraphs. Right column: full-bleed photograph with 1px solid #262626 border, no radius, no caption.

4. *Inline text link*: 1px solid underline in #262626 offset 3px from baseline. No color change, no background, no padding. Link text at 18px Basis Grotesque Pro. Used for navigation and cross-references only.

5. *Wine footer*: Full-width #38141b band, 120px vertical padding. Content in #ffffff: small sans-serif label at 15px Basis Grotesque Pro tracking 0.32px, followed by a short serif sign-off at 32px Legquinne VF. No links, no social icons, no form - just text on wine.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
