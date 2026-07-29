# AI Implementation Prompt

Build a Allfeat-inspired interface using this source-derived style bundle.

Reference site: https://allfeat.org
Theme: dark
Category: Crypto
North star: Backstage monitor at midnight - one teal stage light cutting through warm cream type on charcoal glass.

Use these palette anchors:

- Charcoal Stage `#151515` for Page canvas, primary surface, all dark backgrounds - the base layer every other color sits on
- Warm Cream `#fffbeb` for Primary text, nav links, heading copy, hairline borders on dark surfaces - never pure white, always slightly buttered
- Card Edge `#383835` for Inset 1px card borders, card ambient shadow, subtle separator lines on elevated surfaces
- Mute Cream `#b8b8b8` for Secondary body text, subdued descriptions, muted helper copy
- Ash Gray `#a6a6a6` for Subdued heading text, list separators, inactive link borders
- Bronze Veil `#504f4a` for Badge borders, card hairline accents, low-emphasis outline treatments
- Signal Teal `#00b18c` for Teal action color for filled buttons, selected navigation states, and focused conversion moments.
- Ember Coral `#ff4a5f` for Red action color for filled buttons, selected navigation states, and focused conversion moments

Use these typography anchors:

- TASA Orbiter `--font-tasa-orbiter` for Single typeface across the entire system. Weight 600 for hero and section headlines, weight 500 for subheadings and emphasized body runs, weight 400 for body and metadata. The tight -0.02em tracking on display sizes (54-56px) collapses the headline into a confident slab; the 0.02em loosening on badge/eyebrow text (13-14px) makes labels feel like printed marks.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Pill Primary Button: The default call-to-action - teal fill on charcoal
- Pill Ghost Button: Secondary navigation action - text only inside a pill outline
- Nav Capsule: The header pill containing all nav controls
- Inset-Border Card: Feature/product/insight card - the system's only card pattern
- Hero Radial Wash: Atmospheric background for hero and section transitions
- Display Headline Block: Section-spanning typographic statement
- Eyebrow Label: Section pre-titles - 'OUR SOLUTION', 'PRELUDE'
- Pill Badge: Status, tag, and identifier labels
- Community Node: Circular avatar/badge element in the hero orbital layout
- Central Brand Mark: Hero focal point - the Allfeat logo with headline
- Gradient Accent Border: Decorative hairline that traces card or section edges in coral

Do:

- Use #00b18c fill as the only chromatic CTA - every interactive filled button in the system is this exact teal
- Set all buttons, badges, and nav capsules to 900px radius - this is non-negotiable, the only allowed exception is cards/images at 12px
- Pull all display type to letter-spacing -0.02em and line-height 0.95-1.00 so headlines collapse into confident slabs
- Use the 1px inset #383835 border as the sole card depth treatment - never add a drop shadow on top of it
- Reserve #ff4a5f for eyebrow labels, gradient accents, and emotional emphasis runs inside headlines - never as a button fill or body text color
- Anchor every hero and major section in a soft teal radial wash fading from #00b18c at ~25% opacity to transparent
- Keep body text in TASA Orbiter weight 400 at 16-18px in #fffbeb or #b8b8b8; never go below 13px

Avoid:

- Don't introduce a new accent color - teal and coral are the only chromatic voices in the system
- Don't use 8px or 16px radius on cards or images; the system is strictly 12px for containers and 900px for interactive elements
- Don't use pure white (#ffffff) for text - always #fffbeb, the warm cream tint is part of the brand
- Don't apply drop shadows anywhere - the entire elevation system is inset-only
- Don't break the single-typeface rule by introducing a second font; TASA Orbiter at 400/500/600 covers every need
- Don't set headlines in light or thin weights - 600 is the floor for display sizes, mixing in 400-500 only as muted secondary clauses
- Don't fill buttons with #ff4a5f coral - coral is atmospheric, not actionable; only #00b18c signals an action

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
