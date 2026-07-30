# AI Implementation Prompt

Build a Beau-inspired interface using this source-derived style bundle.

Reference site: https://beau.to
Theme: light
Category: SaaS
North star: Ink on warm parchment - confident monochromatic editorial with a single theatrical gradient spotlight.

Use these palette anchors:

- Paper White `#ffffff` for Primary page canvas, card surfaces, button text on dark fills
- Warm Parchment `#f6f4f1` for Alternate section surface - gives the cream/ivory warmth that stops the page from feeling clinical
- Ink Black `#000000` for Primary text, dark feature card surfaces, filled pill button background, hairline borders - the structural backbone of every screen
- Soft Graphite `#666666` for Secondary text, muted helper copy, quiet borders on neutral sections
- Mid Ash `#999999` for Tertiary metadata, section subtitles, low-emphasis text
- Pale Mist `#b3b3b3` for Disabled badge fill, very low-emphasis surface washes

Use these typography anchors:

- Geist `--font-geist` for Sole typeface across nav, body, headings, and buttons. Weight 400 carries body and most copy; weight 500 is reserved for subheadings, labels, and emphasis. The Geist stylistic sets ss01, ss03, ss04 are enabled - these alter the alternate single-storey 'a', the geometric 'g', and the modernist '$' to give the type a custom editorial feel. Substitute with Inter at the same weights if Geist is unavailable.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 72px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Pill Button (Primary): Primary action - the only filled button in the system
- Ghost Text Link: Secondary navigation and inline links
- Dark Feature Card: High-emphasis content block - inverted surface for key value propositions
- Gradient-Framed Product Card: Showcases the product interface inside a gradient border frame
- Feature Pill: Compact feature highlight - icon + short label in a pill
- Navigation Bar: Sticky top header with brand mark, center links, and right-aligned CTA
- Upload Interface Card: In-context product UI showing document upload state
- Form Verification Mockup: Product UI showing the verification result state
- Gradient Section Band: Full-width section wash - the gradient's headline appearance
- Section Heading Stack: The canonical headline + subhead block at the top of every section
- Two-Column Feature Row: Standard content rhythm: product visual left, text right (or alternating)

Do:

- Use the broadcast gradient (135deg, #ff8308 #ff5043 #392bd5) exclusively for product frames, feature pills, and at most one full-width section band per page
- Set all buttons and feature pills to 200px border-radius - the fully pill-shaped button is a core signature
- Set all cards, images, and badges to 6px border-radius - subtle, never rounded enough to feel friendly
- Apply Geist 500 for headings and labels, Geist 400 for body - never introduce weight 600 or 700; the narrow weight axis is intentional
- Use #f6f4f1 as the warm parchment for alternate section surfaces rather than a hard border or divider
- Enable font features 'ss01', 'ss03', 'ss04' on all Geist text - these stylistic sets are part of the brand voice
- Use 72px as the standard section gap and 24px as the element gap inside cards

Avoid:

- Do not introduce any chromatic color outside the broadcast gradient - the system is monochrome by design
- Do not use 6px or 8px radius on buttons or pills - only 200px (full pill) is correct
- Do not use heavy shadows or elevation - the only approved shadow is the 2px 6%-black atmospheric haze
- Do not use type weights outside 400 and 500 - bold and semibold would break the restrained editorial voice
- Do not place white cards on the gradient band - use dark (#000000) feature cards or let the gradient breathe
- Do not use #0000ee or browser-default link blue - links are always black with optional underline
- Do not crowd sections - if a section feels tight, increase the 72px gap rather than reducing font sizes

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- alternate surface: #f6f4f1
- border: #000000 (structural) / #e5e5e5 (hairline)
- accent gradient: linear-gradient(135deg, #ff8308, #ff5043 50%, #392bd5)
- primary action: #000000 (filled action)

**Example Component Prompts**
1. *Create a section hero:* Centered display headline at 56px Geist 500, #000000, letter-spacing -1.12px, line-height 1.10. Subhead at 17px Geist 400, #666666, line-height 1.40. 96px top/bottom padding, max-width 1200px centered.

2. *Create a dark feature card:* 6px border-radius, #000000 background, 24px padding, optional shadow rgba(0,0,0,0.06) 0px 2px 6px. Heading at 28px Geist 500 white, body at 17px Geist 400 white. Sit beside a gradient-framed product screenshot.

3. *Create a gradient product frame:* Outer container with 6px border-radius and 3px padding filled by the broadcast gradient (135deg, #ff8308 #ff5043 50% #392bd5). Inner container is a white #ffffff product screenshot at 6px radius.

4. *Create a feature pill:* 200px border-radius, broadcast gradient background, 12px 18px padding. Icon + label in Geist 500 14px white, letter-spacing -0.14px. Use in a 3-column grid with 24px gaps.

5. *Create the navigation bar:* White background, no border, 96px vertical padding. Left: brand mark in Geist 500. Center: two ghost text links in Geist 400 14px black. Right: a single filled pill button (#000000 bg, white text, 200px radius, 12px 18px padding).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
