# AI Implementation Prompt

Build a Mews-inspired interface using this source-derived style bundle.

Reference site: https://www.mews.com/en
Theme: light
Category: SaaS
North star: Hospitality command center at pink dawn. A white-walled, sunlit workspace where bold black type, warm cream cards, and a single candy-pink action button define every screen - playful confidence over enterprise restraint.

Use these palette anchors:

- Canvas White `#ffffff` for Primary page background, top of surface stack
- Warm Cream `#fffcf6` for Card and elevated surface backgrounds, gentle warmth against pure white
- Ink Black `#000000` for Primary text, icons, borders, and dark hero panels - the dominant structural color
- Charcoal `#333333` for Secondary text and softer borders where pure black would feel too heavy
- Deep Panel `#161616` for Dark feature cards, inverse surface for hero blocks, and high-contrast panels
- Fog Gray `#8c8c8c` for Muted helper text, disabled button fills, and tertiary borders
- Mist Gray `#cccccc` for Hairline dividers, nav separators, subtle structural borders
- Lilac Mist `#c4c9dd` for Cool-toned decorative borders, illustration fills, and subtle chrome highlights
- Bubblegum `#ff83da` for Primary brand accent - pill-shaped CTAs, announcement bar background, active highlights; vivid pink against white is the visual signature
- Cotton Pink `#ffc5ee` for Softer pink surface for secondary buttons and pastel card variants
- Blush Mist `#f7e1f7` for Lightest pink wash for category tile backgrounds and quiet brand surfaces
- Ice Blue `#d2f4ff` for Cool supporting accent for product UI screenshots, informational tiles, and category surface variation
- Voltage Lime `#e8ff5b` for High-energy accent for spotlight highlights, image overlays, and surprise moments - used sparingly for visual punctuation

Use these typography anchors:

- Soehne `--font-soehne` for Single typeface across all UI. Body and UI copy at 400-500, navigation and labels at 500-600, subheads at 700, and display headlines at 900 - the extreme weight contrast between 400 body and 900 display is the signature typographic move. Aggressive negative tracking (-0.025em at display sizes) tightens headlines into bold block-like forms that feel architectural rather than airy.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary CTA Button: Top-level conversion action - the signature pink pill
- Ghost / Outline Button: Secondary action paired with the primary CTA
- Navigation Pill (Active State): Active state indicator inside nav menus
- Dark Hero Panel: Full-bleed dark surface for hero copy blocks
- Solution / Category Card: Grid tile for product verticals (Hotels, Groups & Chains, etc.)
- Product Screenshot Frame: Container for in-app product imagery on the right side of hero sections
- FAQ Accordion Item: Expandable question/answer list
- Announcement Bar: Slim top bar for product news or feature highlights
- Top Navigation Bar: Primary site navigation
- Eyebrow / Category Label: Small all-caps label above section headings
- Product Feature Pill: Rounded tag for highlighting product capabilities (Property Management, Revenue, Payments, Point of Sale)
- Link with Arrow: Inline navigational link ending with directional arrow

Do:

- Use the candy-pink #ff83da pill CTA (#ff83da fill, white text, 9999px radius, 12-14px vertical padding) as the single primary action on any screen - never duplicate it for multiple competing actions.
- Set display headlines at weight 900 Soehne with -0.025em letter-spacing; this tight black-heavy lockup against white is the brand's signature typographic moment.
- Stack surface levels as: #ffffff (canvas) #fffcf6 (card) #c4c9dd (border) #161616 (dark panel) - preserve the warm-cream-on-white layering instead of defaulting to cool grays.
- Use 4px radius for cards and 8px for inputs; reserve 9999px exclusively for CTA buttons, active nav pills, and tags.
- Keep body text at 16px Soehne 400 with 1.5 line-height in #333333 on white or cream surfaces - never below 14px for running text.
- Drop chromatic accents (pink, ice blue, lime) onto supporting tiles, FAQ toggles, and product UI highlights only - the canvas and body should remain achromatic.
- Let product screenshots breathe in 80px section gaps with 1280px max-width containers; spacing rhythm is generous and architectural.

Avoid:

- Don't use the pink CTA fill for anything other than the primary conversion - ghost, outline, and text-link alternatives exist for secondary actions.
- Don't set headlines in weights below 700; the 900/400 contrast between display and body is the brand's voice - flattening to 600 kills the energy.
- Don't add drop shadows to cards; the design relies on flat warm-cream surfaces and hairline borders for separation - shadows would feel corporate and wrong.
- Don't use the lime #e8ff5b or ice blue #d2f4ff on body text or large surfaces; they're accent and supporting-tile colors only.
- Don't introduce new rounded radii (12px, 16px, 24px) - stick to the 4px / 8px / 9999px scale or the visual rhythm collapses.
- Don't use cool grays (#94a3b8, #64748b) for text or borders; the system runs warm with #333333, #8c8c8c, and #cccccc.
- Don't add decorative gradients; the design is flat, photographic, or product-screenshot-driven - gradients would clash with the editorial flatness.

Source prompt cues:

primary action: #e8ff5b (filled action)
Create a Primary Action Button: #e8ff5b background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
**Quick Color Reference**
- text: #000000
- secondary text: #333333
- background: #ffffff
- card surface: #fffcf6
- border: #c4c9dd (cards), #cccccc (dividers)

**Example Component Prompts**


2. **Solution Category Card**: 4px border-radius, #fffcf6 fill, 1px #c4c9dd border, padding 32px. Top-left: 24px black icon. Title: Soehne 20px weight 700, #000000. Description: 15px weight 400, #333333, 1.5 line-height. Bottom: 12px all-caps link 'MEWS FOR HOTELS ' in Soehne weight 600 with +0.030em letter-spacing.


4. **FAQ Accordion Row**: Full-width, separated by 1px #cccccc hairline. Question: 18px Soehne weight 600, #000000. Right side: 28px circle with #ffc5ee background, black plus icon. When expanded, answer text 16px weight 400 in #333333 with 1.5 line-height.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
