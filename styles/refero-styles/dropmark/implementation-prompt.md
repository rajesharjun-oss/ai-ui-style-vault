# AI Implementation Prompt

Build a Dropmark-inspired interface using this source-derived style bundle.

Reference site: https://dropmark.com
Theme: light
Category: Productivity
North star: Warm paper atelier with cubist murals

Use these palette anchors:

- Cyan Signal `#00affa` for Blue accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Cream Paper `#f7f7f1` for Page canvas, section backgrounds, soft card surfaces - the warm off-white ground everything sits on
- Pure White `#ffffff` for Inset cards, modal surfaces, inverse button text, nav background
- Stone Gray `#dcdcd4` for Subtle accent surfaces, inset focus rings, warm shadow tints
- Graphite `#404040` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Mid Ink `#333333` for Button text and border on dark surfaces, icon stroke
- Charcoal `#111111` for Headline text alternative, deep emphasis borders
- Pewter `#7f7f7f` for Secondary body text, muted helper text, inactive state text
- Ink Black `#000000` for SVG illustration linework, deepest icon fills
- Midnight Violet `#1e2554` for Illustration primary - the dominant dark shape color in cubist murals
- Deep Iris `#2c2a6c` for Illustration mid-tone - secondary dark purple in mural compositions
- Coral Burst `#ff5d43` for Illustration warm accent - orange-red shape fills in murals
- Aqua Glow `#38dede` for Illustration cool accent and icon highlight - teal punctuation in murals
- Vivid Amethyst `#9164fa` for Illustration bright accent - saturated purple shape fills
- Blush `#f8b3b8` for Illustration soft accent - pink shape fills for warmth in murals

Use these typography anchors:

- DropmarkRealHead `--font-dropmarkrealhead` for Display and section headings only - used at 60px for hero, 40px for section titles, 24px for sub-section headings. Medium weight is deliberate; avoids the heavy 700 convention to keep headlines calm and editorial rather than assertive.
- DropmarkRealText `--font-dropmarkrealtext` for Body, buttons, nav, list, footer, supporting UI. 400 for body and links, 600 for emphasized sub-labels and button text, 700 reserved for occasional inline emphasis. Functions as the working sans - every non-heading element uses it.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 60px.
- Card padding: 30px.
- Element gap: 10-20px.

Build these component patterns where relevant:

- Primary Action Button (filled): Main conversion CTA on hero and section blocks
- Outlined Action Button: Secondary conversion CTA paired with primary
- Dark Filled Button: Top-right nav conversion ('Sign up')
- Text Link: Inline links, footer links, nav links
- Nav Bar: Top-of-page site navigation
- Hero Section: Above-the-fold headline and primary conversion
- Feature Card (horizontal): Feature highlight blocks below the hero
- Illustration Mural Band: Full-bleed decorative art between sections
- Statistics Panel: Dark emphasis block ('Trusted for 15+ years')
- Logo Strip: Social proof - customer/team logos
- Footer Link Group: Footer column links

Do:

- Use #00affa exclusively for the outlined action border and filled primary button - no other UI element should carry color
- Set border-radius to 3px for nav, buttons, and tags; reserve 60px for true pill shapes only
- Anchor headlines at DropmarkRealHead weight 500 - do not bold-up to 600/700 for display text
- Keep the page background #f7f7f1; use #ffffff only for inset cards and elevated surfaces
- Lean on the accent illustration palette (#1e2554, #2c2a6c, #ff5d43, #38dede, #9164fa, #f8b3b8) for mural art only, never for UI components
- Use 1px #404040 hairline borders as the primary structural divider, not boxes or shadows
- Pair every primary CTA with a #00affa outlined secondary action to maintain the two-button rhythm

Avoid:

- Do not introduce additional chromatic colors into the UI - the system is intentionally monochrome with one cyan accent
- Do not use drop shadows for elevation; depth comes from surface color and illustration, not shadow
- Do not use border-radius larger than 3px on cards or buttons - the flat editorial geometry is the signature
- Do not bold body text above 600; 700 should appear only for rare inline emphasis
- Do not use #00affa as a text or background tint for non-action elements like tags, badges, or icons
- Do not place the illustration palette colors on text, borders, or background fills - they belong inside mural compositions
- Do not use the cream #f7f7f1 for buttons or CTAs; the canvas color must not compete with actions

Source prompt cues:

Quick Color Reference:
- text: #404040
- background: #f7f7f1
- border: #404040 (hairline), #dcdcd4 (subtle)
- accent: #00affa
- primary action: #00affa (outlined action border)

Example Component Prompts:
1. Build a hero section: cream #f7f7f1 background, centered headline 'Your headline here' in DropmarkRealHead weight 500 at 60px in #404040, subhead in DropmarkRealText 400 at 17px in #404040. Below it, place a filled #00affa button ('Get started') with white text, 3px radius, 12px 24px padding, DropmarkRealText 600 at 16px. Next to it, an outlined #00affa secondary button ('Learn more') with 2px #00affa border, #00affa text, 3px radius, 10px 22px padding.

2. Build a feature card: no card chrome, sits on cream. Left column 4:3 image tile (cubist illustration using #1e2554, #38dede, #ff5d43), right column text block. Heading in DropmarkRealText 600 at 20px #404040, body in DropmarkRealText 400 at 16px #404040, CTA link 'Find out more' in #00affa. 30px vertical gap from next block.

3. Build a statistics panel: #404040 background, white text, padding 40px. Big number in DropmarkRealHead 500 at 40px white, label in DropmarkRealText 400 at 15px white at 80% opacity.

4. Build the top nav: cream #f7f7f1 background, 1px bottom border in #dcdcd4. Left: cyan #00affa drop icon + 'Dropmark' wordmark in DropmarkRealText 600. Right: text links spaced 30px apart in DropmarkRealText 400 at 15px #404040, ending with a dark filled #404040 'Sign up' button, white text, 3px radius, 8px 16px padding.

5. Build a full-bleed illustration mural band: 0px page margin, 300-400px tall, filled with geometric shapes in #1e2554, #2c2a6c, #ff5d43, #38dede, #9164fa, #f8b3b8 on #f7f7f1 ground. No text, no UI chrome - pure brand art acting as section divider.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
