# AI Implementation Prompt

Build a Surfshark-inspired interface using this source-derived style bundle.

Reference site: https://surfshark.com
Theme: light
Category: SaaS
North star: crisp ocean horizon at golden hour - warm coral sun meets teal sea, all floating on white sand

Use these palette anchors:

- Surfshark Teal `#1ebfbf` for Brand mark icon, accent highlights, inline link emphasis - the signature chromatic thread that ties logo, headings, and accent text together
- Coral Pulse `#fa3556` for Primary action buttons, high-urgency CTAs - warm pink-red against the cool palette creates immediate conversion pull
- Promo Gold `#ffc200` for Promotional banner background, limited-time deal strips - golden yellow reserved exclusively for urgency framing
- Charcoal Ink `#16191c` for Primary text, dark hero backgrounds, footer surfaces, button text on coral - near-black with a hint of cool depth
- Pure White `#ffffff` for Page canvas, card surfaces, button text on dark fills, text on coral CTAs
- Fog White `#f9f9f9` for Alternate canvas surface, subtle card backgrounds, soft section differentiation from pure white
- Tide Tint `#e8f7f8` for Faint teal-tinted surface wash - barely-perceptible background variant for feature blocks
- Ash Gray `#dadadd` for Light borders, dividers, subtle separation lines - cooler-toned hairline color
- Mist Gray `#bfbfc0` for Secondary borders, disabled states, heavy-use divider color (highest neutral frequency after black)
- Slate `#5b6065` for Muted body text, secondary copy, icon strokes in resting state
- Graphite `#393e41` for Navigation borders, tertiary UI elements, slightly lighter than Charcoal for layered depth
- Carbon `#000000` for Maximum-contrast borders, SVG icon fills, structural strokes - used heavily for crisp 1px rules
- Deep Abyss `#1e2327` for Alternate dark surface - slightly bluer than Charcoal, used in distinct dark panels

Use these typography anchors:

- Inter `--font-inter` for Sole typeface across the entire product - 400 for body and descriptions, 600 for navigation, subheadings, and emphasis, 700 for display headlines and button labels. Inter's geometric neutrality and tall x-height keep the system legible at 12px captions while the 60px display weight holds authority without requiring a custom display face.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Promo Banner: Top-of-page limited-time deal strip
- Primary Navigation: Sticky top navigation bar
- Hero Card (Dark): Full-bleed conversion-focused hero
- Coral Filled Button: Primary conversion action
- Dark Filled Button: Secondary action on light backgrounds
- Text Link with Arrow: Inline navigational link
- Checkmark Feature List: Benefit bullet list in hero/feature blocks
- Feature Card (Light): Product feature highlight card
- Feature Card (Dark): Alternating dark feature panel
- Reviewer Avatar Strip: Social proof header above testimonials
- Testimonial Block: Centered quote with attribution
- Pill Tag (Rating Badge): Star-rating display chip

Do:

- Use Inter exclusively - never introduce a secondary typeface for display or body.
- Apply the three-color accent rule: teal for brand identity, coral for conversion, yellow for time-sensitive promos only.
- Use 12px radius for standard buttons and 48px radius for feature cards - these two radii define the system's personality.
- Maintain the dark light dark section rhythm: alternate between #16191c panels and #ffffff/#f9f9f9 sections at 64px gaps.
- Set display headlines at 60px Inter weight 700 with -1.5px letter-spacing - tighter tracking on large sizes is non-negotiable.
- Use #fa3556 filled coral buttons for the single primary action per view; switch to #16191c dark buttons for secondary actions to avoid CTA competition.
- Anchor every page with the yellow promo banner above the nav when a deal is active; never move it below the fold.

Avoid:

- Don't use #1ebfbf as a button fill - teal is for brand identity, icons, and inline accent text, not for conversion surfaces.
- Don't apply shadows to cards - the system relies on background contrast and 48px radius for elevation, not drop shadows.
- Don't use border-radius values outside the scale: 8, 12, 32, 48, 64, 96px. Intermediate values break the visual language.
- Don't place two coral CTAs in the same viewport - one coral per view, the rest dark or ghost.
- Don't use the yellow #ffc200 outside promotional banners - leaking it into feature blocks dilutes its urgency signal.
- Don't use serif, display, or decorative fonts - Inter at multiple weights covers the full hierarchy.
- Don't set body text below 16px on marketing pages; 14px is the minimum and only for captions and micro-copy.

Source prompt cues:

primary action: #fa3556 (filled action)
Create a Primary Action Button: #fa3556 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
