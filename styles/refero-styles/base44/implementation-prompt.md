# AI Implementation Prompt

Build a Base44-inspired interface using this source-derived style bundle.

Reference site: https://base44.com
Theme: light
Category: AI
North star: sunlit notepad with a lime highlighter

Use these palette anchors:

- Canvas Bone `#faf9f7` for Page background, section bands, large surface fills - the warm off-white that defines the entire atmosphere
- Card White `#ffffff` for Card surfaces, elevated panels, input backgrounds, footer - pure white sitting on the bone canvas
- Ink Black `#0f0f0f` for Primary text, filled action buttons, icon strokes, nav color - the dominant near-black that carries all type and the filled dark CTA
- Graphite `#232529` for Secondary text, button text, nav strokes - slightly softer than Ink Black for de-emphasized copy
- Hairline `#d1d1d1` for Default 1px borders on cards, inputs, dividers - the thinnest structural line
- Soft Border `#e6e6e6` for Secondary borders, subtle surface backgrounds - softer than Hairline for nested edges
- Muted Ink `#a0a0a0` for Tertiary text, disabled states, muted icon strokes
- Lime Wash `#ebffb1` for Primary CTA fill (Start Building button) - a pale lime that glows against the bone canvas like a fresh highlighter mark
- Lime Edge `#ade900` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Ember Orange `#ff631f` for Logo color, decorative fill accents, secondary action - vivid orange used sparingly to anchor brand identity

Use these typography anchors:

- WixMadeforText `--font-wixmadefortext` for Primary UI sans - body text, buttons, nav, inputs, badges, all chrome. The geometric forms and slightly expanded tracking on small sizes (0.025em at 12px, 0.18em uppercase) give it a friendly, slightly humanist feel that keeps 16px body text comfortable to scan
- WixMisoRegular `--font-wixmisoregular` for Display headline face - used at 48-56px with tight tracking (-0.02em) and very tight line-height (1.05). The single weight at 400 creates a calm, confident headline that doesn't shout - authority through spaciousness. Body sizes (20-24px) share the same character, keeping the type system coherent across scales
- WixMisoLight `--font-wixmisolight` for Secondary display - lighter weight version for subheadings (25px) and lead body text (17px), creating tonal contrast against the Regular headlines. Same family guarantees harmony while the weight difference adds hierarchy without size jumps

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Lime CTA Pill: Primary action button
- Ink Filled Pill: Secondary dark action
- Ghost Pill Button: Tertiary action, suggestion chips
- Frosted Nav Pill: Sticky header CTA container
- Text Link Button: Inline nav and footer links
- Flat White Card: Standard content card, FAQ items, feature blocks
- Soft Shadow Card: Hero input container, elevated prompt card
- Ghost Input: Prompt input, search field
- Orange Submit Circle: Action trigger inside input
- Uppercase Eyebrow Label: Section labels, category tags
- Accordion FAQ Row: FAQ item
- Top Navigation Bar: Site header

Do:

- Use WixMisoRegular at 48-56px weight 400 with -0.96px tracking for all primary headlines - the single-weight serif creates calm authority without shouting
- Set all buttons and tags to 9999px (pill) radius - the fully-rounded shape is the system's defining silhouette
- Use #ebffb1 fill + #ade900 border for the primary CTA, never plain black or blue - the lime glow is the brand's signature action
- Maintain hairline borders at 1px #d1d1d1 for all structural dividers - never use heavier borders or visible elevation to separate content
- Keep the page canvas at #faf9f7 (warm bone) and use #ffffff only for cards that need to lift off the canvas - the two-tone surface system is the entire depth model
- Apply the uppercase eyebrow label treatment (12px, 0.18em tracking, weight 500) to all section labels - it transforms small text into architectural wayfinding
- Use cubic-bezier(0.22, 1, 0.36, 1) for all entrance animations - the spring-like ease-out matches the warm, unhurried atmosphere

Avoid:

- Don't add drop shadows to cards - the system uses background contrast (white on bone) for hierarchy, not elevation. Reserve the single shadow for the hero prompt card only
- Don't use #ff631f orange on text or large fills - it's reserved for the logo, decorative accents, and the submit circle inside the input
- Don't set headline weight above 400 - the system uses weight and tracking for hierarchy, not boldness. Heavier weights would break the calm, spacious feel
- Don't use saturated blue for links or actions - the system has no traditional 'info blue'; interactive elements are either lime, black, or ghost
- Don't create dark sections - the page is entirely light-mode. Use the sunset gradient band for atmospheric breaks, never a full dark background
- Don't use borders heavier than 1px - the hairline aesthetic is the entire structural language. Thicker borders feel heavy and corporate
- Don't use corner radii below 8px on any surface - the system rounds generously (8px cards, 30px hero card, 9999px pills). Sharp corners clash with the warm, friendly tone

Source prompt cues:

primary action: #0f0f0f (filled action)
Create a Primary Action Button: #0f0f0f background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
