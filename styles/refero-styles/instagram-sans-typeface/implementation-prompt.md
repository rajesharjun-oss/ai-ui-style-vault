# AI Implementation Prompt

Build a Instagram Sans Typeface-inspired interface using this source-derived style bundle.

Reference site: https://about.instagram.com/brand/type
Theme: mixed
Category: Media
North star: Living type museum. Oversized black letterforms on slabs of neon, displayed like sculpture in a white room.

Use these palette anchors:

- Signal Pink `#ff0169` for Gradient origin - Instagram brand gradient start point, the chromatic anchor in the system
- Plasma Magenta `#d300c5` for Gradient midpoint - bridges hot pink into ultraviolet, used in the brand gradient only
- Ultraviolet `#7638fa` for Gradient terminus - deep violet end of the Instagram brand gradient, the cool counterweight
- Hot Magenta `#f689ff` for Full-bleed color panel - left half of the hero split, the loudest single surface in the system
- Lavender Mist `#c4a4f7` for Full-bleed accent band - right half of the hero split and secondary color sections, softens the magenta
- Graphite `#1c1e21` for Body text, button borders, list dividers, nav borders - the primary near-black for all text and hairline rules
- Pure Black `#000000` for Specimen letterforms, Instagram camera icon outlines, high-contrast graphic moments - flat black with no warmth
- Paper White `#ffffff` for Content canvas, text on color panels, button text, input backgrounds - the neutral ground that lets color panels pop
- Hairline Gray `#cccccc` for Subtle button borders and disabled-state rules
- Link Indigo `#385898` for Violet accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color

Use these typography anchors:

- Instagram Sans `--font-instagram-sans` for The brand's custom geometric sans. Used for everything from 12px captions to 389px specimen hero letterforms. Single weight 400 across the entire scale - the typeface achieves personality through geometry and tight negative tracking rather than weight contrast. Letter-spacing tightens as size grows: -0.02em at body, -0.03em at 32-46px, -0.035em at 62px and above.
- Instagram Sans Headline `--font-instagram-sans-headline` for Distinct variant for the 468px mega-specimen display - looser tracking (-0.006em) than the base family because at 468px the tight tracking would close letter apertures. Used only for the largest type specimen on the page.
- Helvetica `--font-helvetica` for System fallback appearing at 12px (likely OS-rendered small text) and 224px (possible secondary specimen). Treat as fallback only - Instagram Sans is the intended primary at all sizes.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: .
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Hero Split Panel: Full-bleed 50/50 split, left panel Hot Magenta (#f689ff), right panel Lavender Mist (#c4a4f7), no border, no radius
- Glyph Specimen with Construction Overlay: Oversized black letterform on color ground, overlaid with Bezier curve construction lines in Hot Magenta
- White Content Section: Body text block on white canvas between color panels
- Lavender Accent Band: Full-bleed Lavender Mist section carrying a large black icon
- Instagram Gradient Camera Logo: Brand mark in top-right of white content sections
- Text Link: Inline link within body copy
- Download/Action Button (outlined): Secondary action - downloading the typeface, viewing glyphs
- Section Label: Small all-caps or sentence-case label above a section

Do:

- Use Instagram Sans at 400 weight only - the typeface has no weight variants, so do not fake bold or light with CSS
- Apply 51px paddingLeft and paddingRight on all content sections to match the lateral breathing room of the specimen panels
- Tighten letter-spacing as type grows: -0.02em at 16px, -0.03em at 32-46px, -0.035em at 62px and above
- Use the Instagram brand gradient only as a full asset (the camera logo) or as a 72.44deg linear gradient - never rotate, never recolor, never reverse the stop order
- Render specimen letterforms in Pure Black (#000000) with 0px radius - the sharp edges of the glyph geometry are the point
- Place oversized construction-line overlays (pink circles + lines) on glyph specimens to reveal typeface design intent
- Alternate full-bleed color bands (Hot Magenta, Lavender Mist) with white content sections to create editorial rhythm

Avoid:

- Do not use filled solid-color CTA buttons - the system expresses action through outlined Ghost buttons with Graphite borders
- Do not apply the brand gradient as a background wash, overlay, or card fill - it is reserved for the camera logo and the single signature gradient instance
- Do not use #385898 (Link Indigo) for buttons, fills, or large surface areas - it is a text-link color only
- Do not use font-weight 600+ or italic in Instagram Sans - the family ships weight 400 only
- Do not add drop shadows to specimen letterforms, cards, or panels - the system is flat, shadowless, and relies on scale contrast
- Do not use the Hot Magenta (#f689ff) as a text or small-icon color - it is a full-bleed surface panel color only
- Do not introduce additional typefaces - Helvetica appears only as a system fallback, never as an intentional design choice

Source prompt cues:

**Quick Color Reference**
- text: #1c1e21
- background: #ffffff
- color panel surface: #f689ff (left) / #c4a4f7 (right)
- border: #1c1e21
- accent: brand gradient (#ff0169 #d300c5 #7638fa at 72.44deg)
- link: #385898
- primary action: #385898 (outlined action border)

**Example Component Prompts**
1. *Create a hero split panel*: Left half background #f689ff, right half background #c4a4f7, full-bleed (no max-width). Left side: white Instagram Sans weight 400 at 62px, letter-spacing -2.17px, line-height 1.05, text 'Hello Instagram Sans'. Right side: a single black Instagram Sans glyph at 389px, letter-spacing -13.62px, line-height 1.00, overlaid with 1px solid #f689ff construction lines connecting pink circle anchor points.
2. *Create a white content section*: Background #ffffff, padding 48px 51px. Body text in Instagram Sans weight 400 at 16px, line-height 1.34, letter-spacing -0.32px, color #1c1e21. Instagram gradient camera logo (72.44deg, #ff0169 #d300c5 #7638fa) anchored top-right at 48px size.
3. *Create an outlined download button*: Background transparent, border 1px solid #1c1e21, border-radius 3px, padding 16px 24px, text 'Download' in Instagram Sans weight 400 at 16px, color #1c1e21.
4. *Create a lavender accent band*: Full-bleed background #c4a4f7, padding 48px 51px, centered Pure Black (#000000) Instagram camera icon outline at 200px, no fill, 0px radius.
5. *Create a text link*: 16px Instagram Sans weight 400, color #385898, border-bottom 1px solid #385898, no background, inline within body text.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
