# AI Implementation Prompt

Build a Apple (Espana)-inspired interface using this source-derived style bundle.

Reference site: https://www.apple.com/macbook-pro
Theme: dark
Category: E-commerce
North star: black theater with luminous hardware

Use these palette anchors:

- True Black `#000000` for Primary canvas, hero background, nav backdrop, full-page surface
- Charcoal `#1d1d1f` for Elevated card surfaces on dark mode, section dividers, body text on light surfaces
- Smoke `#333336` for Nav segment bar, secondary button fills, subtle tonal contrast on dark backgrounds
- Graphite `#424245` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Ash Gray `#86868b` for Muted body text, meta labels, input borders, helper copy
- Platinum `#cccccc` for Icon fills, nav glyphs, decorative outlines at low contrast
- Silk `#f5f5f7` for Primary heading and body text on dark backgrounds, light surface fills, badge backgrounds
- Pure White `#ffffff` for Maximum contrast text, icon fills, light card surfaces, button text
- Apple Blue `#0071e3` for Primary purchase CTA fill - the single chromatic action button, Buy button, focus ring
- Link Blue `#2997ff` for Blue text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Deep Link `#0066cc` for Standard body link color, secondary anchor text
- Ember `#b64400` for New badge accent - small warm punctuation for freshness markers

Use these typography anchors:

- SF Pro Display `--font-sf-pro-display` for Display and headline typography - hero h1, section openers, product names. Weight 600 with aggressive negative tracking (-0.015em at 80px down to -0.003em) gives the type a compressed, architectural presence. The whisper-thin tracking on the largest sizes is signature: 80px headlines feel monolithic rather than decorative.
- SF Pro Display `--font-sf-pro-display` for Subheadings, card titles, eyebrow labels - transitions from display to functional type. Tracking shifts to slightly positive values (+0.007em at 28px, +0.012em at 19px) as size decreases, compensating for optical tightness in shorter strings.
- SF Pro Text `--font-sf-pro-text` for Body copy and primary paragraph text - the 17px/1.47 combination with -0.022em tracking is the workhorse of the system. Used everywhere from hero subtext to footer disclaimers.
- SF Pro Text `--font-sf-pro-text` for Small UI text - nav links, footnotes, legal copy, micro-labels. Tracking goes more negative (-0.037em at 10px) at the smallest sizes to maintain readability despite size.
- SF Pro Text `--font-sf-pro-text` for Logo and brand mark rendering size in the global nav - weight 400 not 600, because the wordmark itself carries the form. Line-height 1.00 keeps it visually compact.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 28px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary CTA Pill Button: The single dominant purchase action on the page
- Ghost Pill Button: Secondary actions and navigation controls
- Glassmorphic Floating Bar: Price + Buy composite floating on hero
- Text Link with Arrow: Inline learn-more navigation
- Dark Card Surface: Feature card on dark backgrounds
- Light Card Surface: Feature card on light backgrounds (alternating sections)
- Section Header: Major section opener (Lo principal., Mas de cerca., etc.)
- Chip Badge with Prismatic Gradient: Product family identifier (M5, M5 Pro, M5 Max)
- Nav Link: Top-level navigation item
- Search Input (Global): Top-right search field
- Eyebrow Product Label: Pre-headline product identifier
- Finishes Swatch: Product color/finish picker item

Do:

- Use #0071e3 fill with #ffffff text and 9999px radius exclusively for the primary Buy action - never introduce a second chromatic button color
- Set display type at 56-80px in SF Pro Display weight 600 with -0.015em to -0.005em letter-spacing for all hero and section openers
- Apply 28px border-radius to every card, product viewer, and light surface container - this single radius defines the system's softness
- Compose body copy at 17px SF Pro Text weight 400 with 1.47 line-height and -0.022em tracking as the universal paragraph spec
- Maintain pure black (#000000) as the page canvas with no gradient or texture - let product photography provide all visual warmth
- Use rgba(66,66,69,0.72) with backdrop-filter blur(20px) saturate(1) for any floating UI element that must layer over photography
- Keep nav text at 80% white opacity (#cccccc equivalent) at 12px weight 400 - full-white nav feels aggressive against the black bar

Avoid:

- Never use a second accent color beyond #0071e3 for actions - the blue is rationed, do not dilute it with green, orange, or purple CTAs
- Never add box-shadows to cards or buttons - the system defines elevation through color and radius alone, shadows would feel cheap
- Never use font-weight 700 anywhere - the system maxes at 600 because 700 reads as desperate on the negative tracking
- Never set headings below 28px - the scale starts at subheading 28px and goes up; small bold text is not in the vocabulary
- Never introduce a new radius below 10px for interactive elements - pills (9999px), cards (28px), and links (10px) are the only curves
- Never use color #0066cc as a button fill - it is link-text only; filling a button with it would confuse the action hierarchy
- Never add background gradients to text blocks or content sections - gradients are reserved for chip badges and decorative product imagery

Source prompt cues:

primary action: #0071e3 (filled action)
Create a Primary Action Button: #0071e3 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
