# AI Implementation Prompt

Build a Electronic Materials Office(R)-inspired interface using this source-derived style bundle.

Reference site: https://electronicmaterialsoffice.com
Theme: dark
Category: E-commerce
North star: Incandescent ember in a charcoal gallery

Use these palette anchors:

- Studio Charcoal `#202020` for Page canvas and card surfaces - the floor of the dark gallery, never pure black so the eye can rest on edge softness
- Bone White `#ffffff` for Primary text, hairline borders on images, and the rare inverted surface. Carries all type hierarchy on its own
- Ash Gray `#9d9d9d` for Muted text, subtle card borders, inactive labels - the only middle gray in the scale, used when white is too loud
- Mid Felt `#eaeaea` for Light surface wash for inverted panels or modal scrims - the off-white that sits between bone and the dark canvas
- Carbon `#000000` for Deepest accent for icon strokes and contrast borders where the charcoal canvas is too light to hold an edge
- Ember Orange `#f45500` for Filled primary action button - the only chromatic surface in the UI, always paired with a 30px orange halo so it glows like a filament; 30px outer glow on the primary CTA - duplicates the Ember Orange hex but exists as a box-shadow, not a fill, so the button appears lit from within
- Lavender Link `#9e9eff` for Inline link color and the outlined secondary action border - a desaturated cool counterpoint to the warm orange ember, keeping actions readable against charcoal

Use these typography anchors:

- GT-Flexa `--font-gt-flexa` for Display and heading workhorse. Weight 200 carries every headline above 24px - the 200 weight is the signature: at 68px and 86px the letterforms dissolve into atmosphere rather than shout. Weight 400 steps in for sub-headings and card captions where a whisper isn't enough. Line-heights collapse toward 1.0 at the largest sizes so display type stacks like a column of breath.
- Tobias-light `--font-tobias-light` for Secondary display voice for section headers and the footer wordmark. Used at a step below GT-Flexa 200 to create tonal contrast - Tobias feels more architectural, more labeled, while GT-Flexa feels ambient. Negative letter-spacing tightens the wide proportions of the Tobias Light cut.
- Times `--font-times` for Body text and hero paragraph copy - a deliberate serif counterpoint to the geometric display fonts. The serif adds warmth and editorial gravity to product descriptions without ever growing larger than body size.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48-128px.
- Card padding: 24px.
- Element gap: 4-8px.

Build these component patterns where relevant:

- Primary CTA - Ember Button: The single filled action on any screen (Pre-order, Buy).
- Secondary CTA - White Ghost Button: Companion to the Ember button when two actions sit side by side.
- Lavender Outlined Action: Tertiary or nav-level action (e.g. About, Updates in the header).
- Inline Lavender Link: Anchor text inside paragraphs or feature captions.
- Video / Media Card: Hero film or product video frame.
- Feature Card: 2x2 or 3x2 grid cell in the Key Features section.
- Hero Headline Block: Opening product announcement that fills the first scroll.
- Section Header (Tobias Voice): Delineates major sections (e.g. KEY FEATURES).
- Editorial Paragraph: Body copy under hero or in product descriptions.
- Top Navigation Bar: Persistent header across all pages.
- Footer: Closing block of the page.
- Play Overlay Button: Centered trigger over video frames.

Do:

- Use GT-Flexa weight 200 for every display headline at 42px and above - the whisper weight is the signature
- Apply the Ember Orange (#f45500) filled button with its 30px rgba(245,86,0,0.6) glow exactly once per viewport
- Keep all card radii at 20px and all button radii at 20px - never break to 4px or 8px
- Use #9e9eff for all inline links and outlined nav actions - it is the only cool chromatic in the system
- Hold the page canvas at #202020, not #000000 - the slight lift gives product photography room to breathe
- Let Tobias-light 32-42px carry section labels with its -2.6px tracking - it provides the architectural voice
- Define surface edges with 1px #9d9d9d or #ffffff borders rather than shadow or background shifts

Avoid:

- Do not use Times or any serif for headings, labels, or UI chrome - it is body copy only
- Do not apply the Ember Orange glow to anything other than the primary CTA
- Do not introduce additional saturated brand colors - the system is orange + violet on charcoal
- Do not use weight 400 or above for display headlines above 42px - the 200 weight is non-negotiable
- Do not add box-shadows to cards, images, or navigation - shadows are reserved for the two button variants
- Do not center body copy or paragraph text - left alignment only, matching the hero headline
- Do not round anything below 16px - the system commits to soft, large radii

Source prompt cues:

Quick Color Reference
- text: #ffffff
- background: #202020
- border: #9d9d9d
- accent (link/outline): #9e9eff
- primary action: #f45500 (filled action)

Example Component Prompts
1. Hero section: #202020 canvas, 20px-radius media card 1200px wide with a 1px #9d9d9d border, centered 'Play film' pill button (#ffffff fill, #000000 text, 20px radius). Below at 48px: GT-Flexa 200 headline at 68px line-height 1.06, color #ffffff, left aligned.
2. Feature card: 20px radius, 1px #9d9d9d border, charcoal background. Top half is a square product photograph bleeding to the card edge. Bottom half has 24px padding with a two-line caption in Tobias-light 32px weight 400, letter-spacing -1.5px, color #ffffff.
3. Create a Primary Action Button: #f45500 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
4. Ghost secondary action: transparent background, 1px #ffffff border, 20px radius, white text, 30px rgba(255,255,255,0.3) glow.
5. Outlined nav link: 1px #9e9eff border, 20px radius, #9e9eff text, ~8px vertical padding, 14px horizontal padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
