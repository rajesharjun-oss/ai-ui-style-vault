# AI Implementation Prompt

Build a Slite-inspired interface using this source-derived style bundle.

Reference site: https://slite.com
Theme: light
Category: SaaS
North star: Warm parchment notebook with terracotta pen - every surface is cream paper, every accent a single ember-orange stroke.

Use these palette anchors:

- Parchment Cream `#fdf9f4` for Page canvas and primary card surface - the warm off-white that defines Slite's identity. Never use cold white #ffffff at the page level
- Star White `#ffffff` for Elevated surfaces - product mockup cards, tooltips, white-product interiors stacked on top of the cream canvas
- Dust Sand `#f9efe4` for Secondary surface and tag/chip background - a half-step darker than the canvas. Tag pills, secondary buttons, and warm-emphasis callouts
- Moon Silver `#ecedef` for Hairline borders, dividers, and 2px outlined button borders - the only border tone used at full opacity
- Shade Ink `#2d2f34` for Primary heading and body text - slightly warm near-black. The headline color
- Shade Charcoal `#3f434a` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Shade Slate `#5e646e` for Tertiary body text, captions, helper copy - the quietest readable gray
- Shade Fog `#9da3af` for Disabled states, placeholder text, and the lightest non-white neutral - used sparingly on the page
- Shade Dusk `#6a707c` for Small print and fine print text - pricing footnotes, micro-copy beneath headings
- Border Mist `#d9dde6` for Card borders and stroke at low contrast - slightly bluer than Moon Silver, used when a card edge needs to be felt but not seen
- Ember Orange `#f67748` for Primary action - filled CTA buttons, selected card border accent, featured testimonial card background, and the scribble-annotation color. The single saturated brand color, used sparingly so it always feels like a deliberate highlight
- Neptune Blue `#74a6f1` for Secondary action accent - used on at most one button per page (e.g. alternating testimonial CTA) and link-text accents. Never the primary CTA
- Verification Green `#479a53` for Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Verified Mint `#bbf7d0` for Green decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color
- Tag Violet `#4b51c3` for Violet text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Illustration Violet `#6b70d6` for Decorative illustration fill - light-violet shapes in product mockups, paired with Tag Violet as a tonal pair

Use these typography anchors:

- Garnett `--font-garnett` for Display and editorial headings. Used at 64px (display), 36px (h1), 28px (h2), 24px (large body), 12px (small links). The serif-like Garnett paired with a humanist sans is Slite's signature typographic contrast - it makes the page feel like a designed document rather than a dashboard.
- UniversalSans `--font-universalsans` for Body text, UI controls, navigation, buttons, and supporting headlines. Carries almost all of the page's content. The 50px / weight 400 / line-height 1.5 hero variant is a deliberate departure from typical 700-weight display sizes - it lets the Garnett headline above do the work, while UniversalSans handles the breathing paragraph copy beneath.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: .
- Element gap: 8px.

Build these component patterns where relevant:

- Primary CTA Button (Ember Pill): The single orange button on the page - reserved for the main conversion action.
- Dark CTA Button (Charcoal Pill): Secondary high-emphasis action, typically 'Start for free'.
- Outlined Pill Button: Medium-emphasis action - Book demo, secondary nav actions.
- Ghost Text Button: Low-emphasis inline action - nav items, sub-actions inside cards.
- Square Ghost Button: Compact UI control - close buttons, icon toggles, inline editors.
- Dust Tag Chip: Feature highlight tags and category labels - the most-repeated component on the page.
- Status Pill (Verified / Self-maintained): Trust and maintenance indicators inside product screenshots.
- Cream Feature Card: Primary marketing card - 3-column feature grid items, testimonial cards.
- White Product Card: Product screenshot containers and tooltips stacked on the cream canvas.
- Compact UI Card: Inline product UI mock elements - sidebar items, list rows, agent chips.
- Ember Testimonial Card: Featured customer quote - the only orange-filled card.
- Logo Trust Bar: Social proof - '3,000+ companies trust Slite' row.

Do:

- Set the page canvas to #fdf9f4 - never use cold white #ffffff as the page background
- Use #f67748 for exactly one filled CTA per section; everything else is charcoal, outlined, or ghost
- Use Garnett for headlines and UniversalSans for body - never use UniversalSans at 40px+ display sizes
- Set button border-radius to 999px (pill) for all primary actions, 8px only for tiny square icon buttons
- Set card border-radius to 32px for marketing cards, 12-18px for product mockup containers
- Use #f9efe4 dust backgrounds for tag chips and secondary surfaces, not solid gray
- Hand-draw a 1.5px #f67748 circle or underline around exactly one key word in any hero headline

Avoid:

- Do not introduce a second saturated color as a brand accent - #f67748 must remain the only chromatic surface color
- Do not use 700-weight UniversalSans at display sizes - 50px hero text is always weight 400
- Do not stack more than one shadow elevation on a single element; the three-layer shadow is the maximum
- Do not use pure black #000000 for body text - always #2d2f34 (Shade Ink) or #3f434a (Shade Charcoal)
- Do not use #ecedef or #d9dde6 as background fills - these are border tones only
- Do not break the pill/tag radius system with square chips or rounded-but-not-pill buttons
- Do not place #f67748 fills on large backgrounds (more than 20% of a section) - it dilutes the CTA signal

Source prompt cues:

**Quick Color Reference**
- text: #2d2f34 (headings) / #3f434a (body) / #5e646e (tertiary)
- background: #fdf9f4 (canvas) / #ffffff (elevated) / #f9efe4 (dust surface)
- border: #ecedef (hairline) / #d9dde6 (soft card edge)
- accent: #f67748 (ember - used for the single primary CTA, selected card border, and headline scribble annotation only)
- primary action: #f67748 (filled action)

**3-5 Example Component Prompts**

1. **Hero Headline with Scribble Annotation**: Centered Garnett 64px weight 500, color #2d2f34, line-height 1.2. One key word (e.g. 'Verified') wrapped in a hand-drawn 1.5px stroke #f67748 oval, positioned slightly above and around the word. Below: UniversalSans 19px weight 400, color #3f434a, line-height 1.4, max-width 640px centered.

2. Create a Primary Action Button: #f67748 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. **Dust Tag Chip Row**: Horizontal row of 3 pills, each #f9efe4 background, #3f434a text, UniversalSans 13px weight 500, border-radius 9999px, padding 8px 16px, 8px gap between chips. Centered above feature sections.

4. **Cream Feature Card**: #f9efe4 background, border-radius 32px, padding 48px 24px 32px, no shadow. Optional 2px solid #f67748 left border for highlighted/selected cards. Contains a Garnett 24px weight 500 title in #2d2f34, UniversalSans 15px weight 400 body in #5e646e.

5. **White Product Card**: #ffffff background, border-radius 12px, box-shadow 0 1px 3px rgba(0,0,0,0.1) + 0 2px 6px rgba(0,0,0,0.05) + 0 4px 12px rgba(0,0,0,0.01). Contains a product UI mockup (sidebar + content area) rendered in actual working state, not a stylized render.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
