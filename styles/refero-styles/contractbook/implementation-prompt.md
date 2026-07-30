# AI Implementation Prompt

Build a Contractbook-inspired interface using this source-derived style bundle.

Reference site: https://contractbook.com
Theme: light
Category: SaaS
North star: cream-paper contracts under ultramarine sky

Use these palette anchors:

- Ultramarine `#1009f6` for Feature card backgrounds, brand-emphasis headlines, footer primary CTA - vivid violet-blue carries the entire brand voice, used as punctuation against the monochromatic cream field
- Gold `#ffba09` for Primary action buttons (Request a demo), accent cards - warm yellow against neutral surfaces creates the only chromatic urgency in an otherwise achromatic system
- Forest `#304801` for Decorative illustration and testimonial card accents - deep dark green used in editorial color blocks
- Tangerine `#ff3b09` for Decorative scribble accents and highlight strokes in illustrations
- Royal `#505cf9` for Soft highlight washes and secondary illustration fills - lighter companion to ultramarine
- Sky `#add3e5` for Pastel card surfaces and muted testimonial accents - near-gray blue used as a quiet cool counterpoint to the warm beige field
- Thistle `#e3c7de` for Pastel illustration fills and testimonial card tints - near-gray mauve
- Mint `#00e9a7` for Decorative green accent for illustration highlights
- Cream `#f0f0ec` for Page background, card surfaces, input fills - warm off-white dominates the entire canvas
- Pearl `#f7f7f3` for Elevated card surfaces, lighter than cream - used for nested content blocks
- White `#ffffff` for Pure white cards and inverted button text
- Smoke `#d4d4d0` for Muted helper text and secondary labels
- Concrete `#eaeae6` for Hairline borders, subtle dividers, disabled states
- Washed Black `#1a1a1a` for Primary text, headings, body copy - slightly softer than pure black for warmer reading
- Ink `#222222` for Secondary text and nav items
- Charcoal `#4d4d4d` for Muted body text, captions, metadata
- Dim `#6d6868` for Tertiary text, timestamps, fine print
- Black `#000000` for Button text on bright fills, strong borders

Use these typography anchors:

- Abcwhyte `--font-abcwhyte` for Single sans-serif family used for everything - display headings, body, nav, buttons, inputs, footer. At 48px/700 with tight 1.25 line-height for hero headlines, dropping to 16px/400 with 1.5 line-height for body. The uniformity of one family at all sizes gives the system a document-like coherence rather than a display/body contrast.
- Abcwhyte `--font-abcwhyte` for UI micro-copy - nav labels, tag chips, small captions, footer links

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 120px.
- Card padding: 48px.
- Element gap: 14px.

Build these component patterns where relevant:

- Gold Pill Button (Primary): Highest-emphasis call-to-action
- Outlined Pill Button: Secondary action
- White Pill Button: Inverted secondary
- Cream Feature Card: Content card with generous padding
- Hero Panel Card: Large rounded content block
- Ultramarine Brand Card: Full-bleed accent card
- Form Input: Text and select input fields
- Nav Bar: Top navigation
- Testimonial Card: Customer quote block
- Video Player Thumbnail: Embedded video preview
- Demo Request Form: Contact/sales form
- Footer: Site footer

Do:

- Use 999px or 9999px border-radius on ALL buttons, nav items, and tags - pill shapes are non-negotiable
- Use #ffba09 fill with #1a1a1a text for the single highest-emphasis action on any page
- Use #f0f0ec as the default page background and #ffffff or #f7f7f3 for elevated card surfaces
- Use Abcwhyte (or substitute Inter/DM Sans) as the ONLY font family across all sizes and weights
- Use 24px radius for standard cards and 40px radius for hero panels and images - never intermediate values
- Separate content layers with color and spacing, not shadows - this system is intentionally flat
- Use #1009f6 ultramarine sparingly: feature panels, brand headlines, footer CTA - never as a general accent

Avoid:

- Do not add box-shadow to any card, button, or panel - elevation comes from color and space, never shadow
- Do not use a serif or display font for headlines - the single-family approach is the signature
- Do not use #1009f6 for body text or borders - reserve ultramarine for card backgrounds and brand emphasis only
- Do not use sharp corners (0-8px radius) on content cards - minimum card radius is 24px
- Do not introduce a second primary action color - gold (#ffba09) is the only filled chromatic button
- Do not use pure black (#000000) for body text - use #1a1a1a for warmer reading
- Do not crowd sections - maintain 120px vertical gaps between major sections

Source prompt cues:

**Quick Color Reference**
- Background: #f0f0ec
- Surface (card): #ffffff or #f7f7f3
- Text: #1a1a1a
- Border: #d4d4d0 or #1a1a1a
- Brand accent: #1009f6 (ultramarine)
- primary action: #ffba09 (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #ffba09 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. **Hero section card**: #ffffff background, 40px border-radius, 48px padding. Display headline at 48px Abcwhyte/700 in #1a1a1a, line-height 1.25. Body text at 16px/400 in #1a1a1a, line-height 1.5. Two buttons side by side: gold pill + outlined pill.
3. **Feature card**: #f0f0ec background, 24px border-radius, 48px padding. Heading at 32px/700 #1a1a1a, body at 16px/400.
4. **Ultramarine accent card**: #1009f6 background, 24px border-radius, 48px padding. White heading at 28px/700, white body at 16px/400.
5. **Form input**: #f0f0ec background, 1px solid #b3b3b3 border, 4px border-radius, padding 9px 14px, Abcwhyte 14px/400 #1a1a1a.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
