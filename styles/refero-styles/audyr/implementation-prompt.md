# AI Implementation Prompt

Build a Audyr-inspired interface using this source-derived style bundle.

Reference site: https://audyr.com
Theme: light
Category: SaaS
North star: Ink on cold-pressed paper. The interface reads as a meticulously typeset monograph - black ink, white stock, hairline rules, and the softest possible shadows to suggest depth.

Use these palette anchors:

- Ink `#262626` for High-contrast neutral action fill for primary buttons on light surfaces.
- Pure Paper `#ffffff` for Card surfaces, elevated panels, content backgrounds - the base canvas color sits one step brighter than the page
- Soft Mist `#ededed` for Hairline borders, input outlines, dividers, subtle panel fills - the structural glue that separates regions without lines shouting
- Charcoal `#171717` for Secondary dark surface (pricing card, alternate hero), occasional dark fills where deeper weight is needed than Ink
- Ash `#686868` for Secondary body text, nav links, supporting copy - the first step down from primary text
- Slate `#515151` for Tertiary text, icon strokes on light backgrounds, muted metadata
- Muted `#737373` for Helper text, caption-level copy, secondary icon strokes
- Fog `#929292` for Placeholder text, disabled labels, very low-emphasis text
- Chalk `#cbcbcb` for Shadow residue on dark buttons, ultra-low-contrast surface markers
- Mint Whisper `#ecfdf5` for Primary page canvas and white card surfaces. Use as a supporting accent, not as a status color

Use these typography anchors:

- Inter `--font-inter` for The sole typeface. Weight 600 reserved for section labels and small UI controls; weight 500 for nav and secondary buttons; weight 400 for body and most copy. The system commits to one family rather than pairing a display serif - a deliberate editorial choice that keeps the visual signal monochrome.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 120-160px.
- Card padding: 32px.
- Element gap: 16-20px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide header
- Dark Filled Action Button: Primary CTA
- Ghost Outline Action Button: Secondary action
- Pricing Tier Card: Pricing display (Free, Hobby, Pro)
- Highlighted Pricing Card (Hobby): Featured/Recommended tier
- Pill Badge: Status / label / tag
- Pricing Toggle: Billing period switcher
- Hero Section: Above-the-fold introduction
- Product Mockup Frame: Embedded dashboard screenshot
- Tab Group: Section switcher (used in product mockup)
- Logo Bar: Social proof / 'teams switching from'
- Two-Column Feature Section: Asymmetric content layout

Do:

- Use #262626 as the only filled button background - it is the single visual anchor in the monochrome system
- Apply -0.025em letter-spacing to every text element at every size, from 12px captions up to 48px displays
- Use #ededed for all structural dividers, card borders, and input outlines at 1px
- Set card radii to 14px, button radii to 4px, and badge radii to 9999px - these three radii define the visual language
- Limit the chromatic surface tint (#ecfdf5) to success/popular badges only; never apply it to large surfaces
- Keep shadows to the two soft levels: the diffuse card shadow (lab 0.1 25px 50px -12px) and the button micro-shadow (oklab 0.05 1px 2px)
- Maintain 80-160px section padding to preserve the editorial breathing room

Avoid:

- Don't introduce a brand color accent - the absence of color IS the brand
- Don't use radii outside the 4 / 8 / 14 / 18 / 9999px scale; no 6px or 12px intermediate values
- Don't add drop shadows heavier than the documented card shadow - anything more theatrical breaks the paper-grain feel
- Don't pair Inter with a second typeface for display use - the single-family commitment is structural
- Don't use #ffffff for text on white surfaces, and don't use #ededed for body text - both will fail contrast
- Don't apply gradients - the system is committed to flat, unshaded fills
- Don't use colored status indicators on the marketing site; restrict color to badges and the pricing 'Popular' highlight

Source prompt cues:

primary action: #262626 (filled action)
Create a Primary Action Button: #262626 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
