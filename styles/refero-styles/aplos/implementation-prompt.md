# AI Implementation Prompt

Build a Aplos-inspired interface using this source-derived style bundle.

Reference site: https://aplos.world
Theme: light
Category: E-commerce
North star: Old-world apothecary at dusk

Use these palette anchors:

- Bone `#f2f1ed` for Page background, large section canvases - the warm off-white that gives the system its paper-like editorial feel
- Paper White `#ffffff` for Card surfaces, elevated panels, light benefit cards - sits one step above Bone to create lift without shadows
- Cocoa `#3b3429` for Dark accent cards, inverted text blocks - warm near-black that softens pure ink and keeps dark sections feeling organic rather than digital
- Ink `#000000` for Primary text, nav links, logo wordmark, hairline borders, hero backdrop
- Stone `#646464` for Secondary body copy, muted helper text, subdued descriptions
- Ash `#b4aeac` for Subtle link hover shadows, barely-there elevation hints

Use these typography anchors:

- Goudy Old Style `--font-goudy-old-style` for Sole typeface for headlines, section titles, product names, card titles, and editorial body - a classical Venetian serif that signals craft and heritage. The narrow weight range (400 only) and tight line-heights (1.05-1.08) let the type sit in dense, menu-like stacks. Letter-spacing of -0.012em tightens optical gaps in display sizes without losing the serif's elegance.
- System Sans (UI chrome) `--font-system-sans-ui-chrome` for Inferred secondary face for navigation, buttons, captions, and dense utility text where serif would be illegible at small sizes. Kept restrained so the serif remains dominant.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 96-120px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Announcement Bar: Top utility strip
- Primary Navigation: Site header with logo + nav links
- Dark Hero Section: Full-bleed editorial hero
- Outlined CTA Button (Light): Primary action on dark hero
- Ghost Text Link: Secondary action (Learn More, Shop Now)
- Benefits Section Heading: Editorial section title
- Benefit Card (Light): Standard feature card
- Benefit Card (Dark / Cocoa): High-contrast accent card
- Product Collection Card: Featured product showcase
- Section Divider Spacer: Vertical rhythm control

Do:

- Set all section backgrounds to Bone (#f2f1ed); reserve pure white only for card surfaces that need lift.
- Use Goudy Old Style at 26px and 40px with letter-spacing -0.012em for every heading and product name - the serif IS the brand.
- Anchor all CTAs to 5px radius with 9px 12px padding; never round buttons to pill or full-circle.
- Place 96-120px of vertical whitespace between major sections to maintain the printed-menu cadence.
- Use Cocoa (#3b3429) for inverted accent cards to add tonal variety - never introduce chromatic color where grayscale shift can do the work.
- Keep hero photography full-bleed on Ink (#000000) with white serif headlines; the contrast does the dramatization.
- Set secondary body copy in Stone (#646464) at 14-16px sans-serif, never in the serif at small sizes.

Avoid:

- Don't introduce any chromatic color (blue, green, red, etc.) - the system is deliberately 0% colorful and any hue will break the apothecary language.
- Don't use large border-radius (12px+) or pill shapes - the 5px radius is non-negotiable and keeps the system feeling editorial, not app-like.
- Don't use bold weights (600+) for headings - Goudy Old Style 400 only; the whisper-weight serif is the signature.
- Don't add drop shadows, glows, or gradient overlays - elevation comes from tonal contrast between Bone, Paper, and Cocoa, not from blur effects.
- Don't use a sans-serif for product names or section titles - those are exclusively Goudy Old Style domain.
- Don't crowd sections with dense grids - the rhythm depends on 96-120px breathing room between blocks.
- Don't place dark text directly on Cocoa (#3b3429) without testing contrast - use white (#ffffff) text on Cocoa surfaces.

Source prompt cues:

**Quick Color Reference**
- Background: #f2f1ed (Bone)
- Surface: #ffffff (Paper White)
- Text: #000000 (Ink)
- Secondary text: #646464 (Stone)
- Accent surface: #3b3429 (Cocoa)
- primary action: no distinct CTA color

**Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Benefits Section**: Bone (#f2f1ed) background. Centered Goudy Old Style heading 40px #000000, letter-spacing -0.48px. Below, sans-serif paragraph 16px #646464, max-width 600px, centered. 3-column card grid below with 24px gaps.

3. **Cocoa Accent Card**: #3b3429 background, 5px radius, 24px padding. Goudy Old Style title 26px #ffffff at top-left, letter-spacing -0.31px. Small sans-serif number '01' in 14px #ffffff positioned bottom-left.

4. **Light Benefit Card**: #ffffff background, 1px border #e5e3df, 5px radius, 24px padding. Goudy Old Style title 26px #000000 top-left, small sans-serif number '02' in 14px #646464 bottom-left.

5. **Product Collection Card**: Large product image (bottle crop) occupying top 65% of card, edge-to-edge with no border-radius on image. Overlapping white text panel at lower-left: Goudy Old Style product name 26px #000000, sans-serif description 14px #646464 below, no panel background - text floats on the image.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
