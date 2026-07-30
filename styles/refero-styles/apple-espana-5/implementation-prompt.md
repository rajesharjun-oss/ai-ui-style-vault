# AI Implementation Prompt

Build a Apple (Espana)-inspired interface using this source-derived style bundle.

Reference site: https://apple.com
Theme: light
Category: E-commerce
North star: Museum gallery in soft daylight - the gallery is a single, immersive, weightless white room where each product is spotlit against a faintly tinted wall.

Use these palette anchors:

- Fog White `#f5f5f7` for Dominant page canvas, section backgrounds, footer
- Pure White `#ffffff` for Nav background, button text, elevated surface
- Obsidian `#1d1d1f` for Primary headline and body text - the only true dark for editorial content
- Carbon `#000000` for Nav glyphs, link underlines, dark text on light surfaces
- Pewter `#707070` for Secondary body text, footer copy, muted helper text
- Slate `#505050` for Tertiary body text and subdued link states
- Graphite `#474747` for Nav and link text at rest - sits between body text and pure black
- Iron `#333333` for Nav icons (fill) and button text - the dominant dark accent in chrome
- Silver `#858585` for Icon strokes, tertiary glyphs, muted UI controls
- Pale Mist `#d6d6d6` for Hairline dividers, subtle borders between content blocks
- Ash Veil `#e2e2e5` for Button backgrounds for secondary filled actions (dark mode variant)
- Iris Blue `#0071e3` for Filled primary action buttons - the sole chromatic CTA, signals the only commitment the page asks of you
- Sapphire `#0066cc` for Outlined action buttons, body and link text - darker blue for outlined variants and inline links
- Sky Signal `#2997ff` for Outlined action buttons on dark sections, secondary CTAs - lighter blue for ghost buttons against dark hero bands
- Cornflower `#509be7` for Hover state for inline links, decorative link accent
- Ice Wash `#aad0f6` for Gradient section background wash - the pale blue tint behind iPad Air / MacBook Air hero bands

Use these typography anchors:

- SF Pro Display `--font-sf-pro-display` for Product headlines, large editorial display text. Used at 56px/600 for hero titles like 'MacBook Air' and 40px/600 for section subheads. The tighter 1.07 line height at 56px is signature - it lets the headline sit as a single visual block without breathing room between lines.
- SF Pro Text `--font-sf-pro-text` for Navigation, body copy, buttons, footer, subheads below display. The 17px/400/1.47 body setting appears 221 times - this is the workhorse. The 12px/400/1.33 setting handles everything in the footer and micro-copy. 44px/400/1.00 is the nav logo wordmark.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 980px.
- Section gap: 80-120px.
- Card padding: 0px.
- Element gap: 12px.

Build these component patterns where relevant:

- Filled Primary Button: The single chromatic CTA on any page - signals the most important action
- Outlined Secondary Button: Companion action to the filled primary, typically 'Comprar' or 'Comprar un iPhone'
- Ghost Outline Button (Dark Surface): Outlined action variant used on dark hero bands like Apple TV+ carousel
- Text Link: Inline links in body copy, footer terms, and the global message bar
- Global Nav Bar: Persistent top navigation across all pages
- Global Message Bar: Promotional ribbon below the nav - financing offers, launch announcements
- Product Hero Section: The dominant unit of the page - one product per full-width section
- Button Pair (CTA Cluster): The action duo under every product headline
- Entertainment Carousel: Full-bleed horizontal scroll for Apple TV+ content
- Product Lineup Display: Showcase of product variants (iPhone 17 colors, MacBook angles)
- iPad Air Wordmark: Product name with mixed-weight treatment
- Footer Link List: Dense grid of navigational and legal links at the page bottom

Do:

- Use border-radius 980px on all buttons and pill tags - this is the system's defining shape language.
- Use SF Pro Display weight 600 for product headlines at 40px or 56px; never use display weight 400 for headlines.
- Center all hero text stacks horizontally - the system is symmetrical, not left-aligned.
- Use #0071e3 exclusively for filled primary action buttons; use #0066cc for outlined buttons and inline links. These are the only two blues in the action set.
- Separate product sections with a change in background tint (#f5f5f7 #aad0f6 dark photo), never with a border or divider line.
- Set body text at 17px/400/1.47 with letter-spacing -0.022em - this is the workhorse setting and appears in 221 instances.
- Use a 44px-tall nav bar with backdrop-filter blur(20px) saturate(1.8) - the frosted glass effect is essential to the page's weightless feel.

Avoid:

- Don't add box-shadows to buttons, cards, or sections - elevation comes from color contrast, not shadows.
- Don't use the brand blue (#0071e3) for anything other than filled primary action buttons; links and outlines use #0066cc.
- Don't left-align product headlines; the system is always centered.
- Don't use border-radius values below 980px on buttons - no square buttons, no 4px or 8px pill variants.
- Don't place horizontal rules or border lines between sections; use background color shifts instead.
- Don't use SF Pro Display at sizes below 21px; that family is reserved for headlines and large body. Use SF Pro Text for everything under 21px.
- Don't introduce secondary accent colors, gradients, or decorative backgrounds within the product hero areas - the product render is the only visual interest.

Source prompt cues:

**Quick Color Reference**
- text (primary): #1d1d1f
- text (secondary): #707070
- text (nav glyphs): #333333
- background (canvas): #f5f5f7
- border / hairline: #d6d6d6
- accent (nav text, links): #0066cc
- primary action: #0071e3 (filled action)

**Example Component Prompts**

1. **Product Hero Section**: Full-bleed section, background #f5f5f7. Centered headline at 56px SF Pro Display weight 600, color #1d1d1f, letter-spacing -0.28px. Subhead at 21px SF Pro Display weight 400, color #1d1d1f. Below the text, a centered button pair with 8px gap: filled blue button (#0071e3, white text, 980px radius, 11px 21px padding) and outlined blue button (transparent background, 1px solid #0066cc border, #0066cc text, 980px radius, 11px 21px padding). Below the buttons, a large product render at full section width with no card or shadow.

2. **Filled Primary Button**: border-radius 980px, background #0071e3, color #ffffff, padding 11px 21px, font 14px SF Pro Text weight 400, letter-spacing -0.22px. No border, no shadow.

3. **Outlined Secondary Button**: border-radius 980px, background transparent, 1px solid border #0066cc, color #0066cc, padding 11px 21px, font 14px SF Pro Text weight 400.

4. **Global Nav Bar**: Height 44px, full viewport width, background #ffffff, backdrop-filter saturate(1.8) blur(20px). Apple logo glyph on the left, nav items centered at 12px SF Pro Text weight 400 in #1d1d1f, search and bag icons on the right. A thin 1px bottom border in #d6d6d6 may appear on scroll.

5. **Product Lineup Section**: Full-width section on background #aad0f6. A horizontal arrangement of product renders (no cards, no borders) photographed with soft natural shadows. Section padding-top 80px, section padding-bottom 80px. Headline at 40px SF Pro Display weight 600 centered above.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
