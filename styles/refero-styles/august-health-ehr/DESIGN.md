# August Health EHR Design Reference

## North Star

Warm cream pharmacy with violet ink a humanist clinical surface that softens healthcare's typical sterility.

## Theme

light style for SaaS interfaces.

## Color System

- Primary Indigo `#4865ff` for Primary action buttons, active nav state, icon accents the single saturated focal color that makes CTAs unmistakably interactive
- Deep Ink `#080331` for Headlines, body text, primary borders near-black violet that pairs warmth with the serif typeface
- Midnight Violet `#1b1463` for Navigation borders, secondary surfaces, gradient terminus darker sibling to Primary Indigo for layered depth
- Forest `#328a3b` for Green action color for filled buttons, selected navigation states, and focused conversion moments
- Ember `#ff6d39` for Tinted card surfaces, portrait frame backgrounds warm orange that signals energy and human warmth
- Blossom `#f098d7` for Tinted feature card backgrounds, hero photo frame mid-pink for category-coded surfaces
- Petal `#ffaefe` for Light pink surface washes and button backgrounds lightest tint in the pink family for soft fills
- Meadow `#114e0b` for Dark green button background variant deep saturated green for contrasting pill buttons

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- Reckless Neue All headings and display text. A contemporary editorial serif used exclusively at weight 400 (regular) no bold. This is anti-convention: most healthtech brands use sans-serif or bold serifs; the regular-weight serif at large sizes creates a literary, trustworthy quality without shouting. Largest sizes (48-64px) anchor section headlines, while 24-32px serves subheadings. `--font-reckless-neue`
- Saans Body text, UI controls, navigation, buttons, cards, labels, and everything non-headline. Weight 400 for body and descriptions, weight 500 for buttons and nav links where slight emphasis is needed. The geometric humanist sans provides clarity and warmth at small sizes, contrasting the editorial serif headings. `--font-saans`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 8px
- Density: comfortable
- Page max-width: 1200px
- Section gap: 64px
- Card padding: 32px
- Element gap: 16px

## Components

- Primary CTA Button: Main call-to-action across all pages
- Ghost/Text Button: Secondary actions and inline links
- Pill Navigation Bar: Sticky top navigation
- Tinted Feature Card: Product capability showcase
- White Product Card: UI screenshot or detailed feature container
- Circular Portrait Frame: Hero decorative photography
- Info Badge/Pill: Category labels and tags
- Video Player Block: Case study and testimonial content

## Implementation Guidance

- Use 1600px border-radius for all interactive elements: buttons, badges, nav bar, and image frames to maintain the pill-shaped consistency
- Set the page canvas to Cream (#f8f3eb), not pure white the warm tone is the brand's emotional foundation
- Apply warm-tinted shadows (rgba(75,68,57,0.1)) to all elevated elements instead of cool gray shadows
- Pair Reckless Neue (serif, weight 400 only) for all headings with Saans (sans, weights 400-500) for all body and UI text
- Use Primary Indigo (#4865ff) exclusively for the primary action do not dilute with secondary action colors when a strong CTA is needed
- Layer surfaces as: cream canvas white card tinted card vibrant accent to create depth without heavy shadows
- Maintain 64px minimum vertical spacing between sections and 32px internal padding for all card containers
- Center-align hero and section headlines for editorial compositions; use left-align only for product UI and dense content areas

## Guardrails

- Do not use bold (600+) weights with Reckless Neue the serif's power is in its regular weight restraint
- Do not apply cool gray shadows (rgba(0,0,0,...)) warm brown shadows are part of the visual identity
- Do not use pure white (#ffffff) as the page background cream is the base, white is for surfaces on top
- Do not use the accent colors (Forest, Ember, Blossom) for primary CTAs reserve Primary Indigo for that role
- Do not add more than two weights to any text element the system is intentionally restrained (400/500 for sans, 400 for serif)
- Do not use sharp corners (0px radius) on cards or buttons the minimum card radius is 16px, buttons are always pills
- Do not break the cream/white/tinted surface hierarchy by placing a colored accent directly on cream without a white card container
- Do not use green for success states or red for error states unless explicitly required the accent colors are decorative, not semantic
