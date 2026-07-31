# AI Implementation Prompt

Build a RainbowKit-inspired interface using this source-derived style bundle.

Reference site: https://www.rainbowkit.com
Theme: dark
Category: Crypto
North star: Neon wallet modal floating in a black void - the blue-to-violet aurora glows through the dark.

Use these palette anchors:

- Signal Blue `#0e76fd` for Primary CTA fill, active states, brand wordmark, link emphasis - the only chromatic blue with enough surface area to carry identity
- Electric Violet `#7a70ff` for Gradient terminus, brand-secondary accent - appears only as the cool half of the aurora
- Deep Iris `#38228f` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Hyper Pink `#ff5ca0` for Accent spectrum - demonstration option in the wallet-customization showcase, not a UI-state color
- Ember Red `#fa423c` for Accent spectrum - demonstration option in wallet-customization showcase
- Solar Orange `#ff801f` for Accent spectrum - demonstration option in wallet-customization showcase
- Toxic Green `#1db847` for Accent spectrum - demonstration option in wallet-customization showcase
- Void `#000000` for Page canvas, deepest surfaces, inverted button borders - true black anchors the entire system
- Obsidian `#1b1c1e` for Card surfaces, code blocks, modal containers, body text on light - the workhorse elevated surface
- Shadow `#121314` for Shadow tint color (used in box-shadow rgba), near-black with a hint of warmth
- Graphite `#25292e` for Hairline borders, dividers, icon stroke, secondary text on dark - the most-used neutral border in the system
- Slate `#2f3334` for Secondary borders, subtle dividers between sections - sits between Graphite and Pewter
- Carbon `#353a3b` for Tertiary icon fills, disabled-state borders, subtle backgrounds
- Pewter `#646566` for Disabled button background, low-emphasis surfaces - never for text
- Fog `#95979c` for Muted helper text, icon secondary, placeholder text - the only gray that carries readable information
- Snow `#ffffff` for Primary text, inverted button fill, light-surface backgrounds, icon glyphs, hairline highlight borders
- Mist `#f0f1f5` for Light-theme surface fallback, very subtle off-white for section backgrounds on the demo

Use these typography anchors:

- SFRounded `--font-sfrounded` for Primary typeface for all UI - rounded geometric sans, chosen because the soft terminals make technical Web3 copy feel approachable rather than intimidating
- SFMono `--font-sfmono` for Code snippets, terminal commands, technical strings - the npm install command in the hero
- system-ui `--font-system-ui` for Fallback body copy when the web font hasn't loaded - barely visible because SFRounded dominates
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Gradient Primary CTA: The hero action - invites the visitor into the documentation.
- Solid Blue Pill Button: Secondary CTAs and persistent nav actions like 'Connect Wallet'.
- Ghost Nav Button (Logo + Version): Brand identification in the nav bar with version metadata.
- Terminal Code Block: Copy-paste installation command in the hero.
- Wallet Connection Modal: The product showcase - the actual RainbowKit component floating on the landing page.
- Wallet List Item: Selectable option inside the connection modal.
- What-is-a-Wallet Info Card: Educational companion card explaining wallets next to the connection modal.
- Mobile Preview Card: Showcases the wallet UI on a phone frame, demonstrating responsive behavior.
- Section Heading Block: Centered section titles with supporting copy.
- Partner Logo Grid Item: Brand trust marker - a 6xn grid of partner logos.
- Inset Highlight Border: The defining visual signature of interactive elements on dark surfaces.
- Gradient Brand Wordmark: The 'RainbowKit' hero title.

Do:

- Use 9999px radius for every button, tag, and pill - the radius is the brand's friendliness signal
- Apply the 1px inset white border (rgba(255,255,255,0.12)) to all elevated interactive elements on Obsidian surfaces
- Use the aurora gradient (linear-gradient(to right, #3898ff, #7a70ff)) only for primary hero CTAs and the wordmark - reserving it makes it feel premium
- Default to #0e76fd for all secondary action buttons and link emphasis
- Set body copy at 16px SFRounded weight 400 with 0.27px letter-spacing; headlines at 40-52px weight 700 with 0.88-1.3px letter-spacing
- Float product cards with rgba(0, 0, 0, 0.4) 0px 8px 24px 0px - the heavy shadow is what makes a modal feel like a window into the product
- Keep the canvas at true #000000 - never warm it with off-black, the void is the point

Avoid:

- Don't use the chromatic accent colors (Hyper Pink, Ember Red, Solar Orange, Toxic Green) as semantic UI states - they are demonstration options, not success/error/warning tokens
- Don't apply shadow to text or the canvas itself - shadows belong to floating cards only, the background is shadowless
- Don't use negative letter-spacing - SFRounded is designed for positive tracking; tightening it fights the rounded letterforms
- Don't introduce a second body font - SFRounded handles everything from 11px captions to 52px displays; a serif or system fallback breaks the cohesion
- Don't place white or light-colored cards on the canvas - every surface must stay in the Obsidian/Graphite range to preserve the void
- Don't use #25292 for text - it's a border color, contrast on it is insufficient for readable copy
- Don't round images of phones or product screenshots with small radii - they should be 24px+ or fully inherit the device frame

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
