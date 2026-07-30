# AI Implementation Prompt

Build a LottieFiles-inspired interface using this source-derived style bundle.

Reference site: https://lottiefiles.com
Theme: light
Category: Other
North star: Bright motion studio with teal accent

Use these palette anchors:

- Lottie Teal `#019d91` for Teal action color for filled buttons, selected navigation states, and focused conversion moments.
- Ink `#09090b` for Primary text, headings, dark card surfaces, footer background, icon strokes - near-black with a barely-perceptible cool cast
- Charcoal `#18181b` for Dark card backgrounds, elevated dark surfaces, strong icon strokes, secondary dark UI blocks
- Slate 700 `#27272a` for Dark muted surfaces and inverse muted backgrounds
- Steel `#71717b` for Muted body text, secondary copy, icon fills, helper labels - sits between the primary ink and lighter grays
- Fog `#9f9fa9` for Subtle text, tertiary metadata, low-priority descriptions
- Cloud `#e4e4e7` for Hairline borders, input outlines, subtle dividers between UI sections
- Mist `#f2f2f3` for Largest-volume border color across the UI; subtle separators, input borders, form outlines
- Warm Gray `#f4f4f5` for Page canvas and soft card surfaces - the dominant background tone beneath white
- Paper `#ffffff` for Pure white surfaces: raised cards, button fills, content containers on top of warm-gray canvas
- Sunshine `#f0b100` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Mint Wash `#b7ffe7` for Soft decorative fill in illustration/illustration-adjacent graphics
- Mint Pop `#61f7cf` for Bright decorative fill used in hero illustration characters and supporting graphics
- Ember `#ff6900` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color

Use these typography anchors:

- DM Sans `--font-dm-sans` for Display and heading family. Used for hero headlines (48-96px, weight 500), section headings (24-32px, weight 500), and large body (20px, weight 400). Letter-spacing tightens aggressively at large sizes - -0.0500em at 96px pulls characters into a compressed, poster-like composition that feels editorial rather than utilitarian. The medium weight (500) is the headline default, avoiding the heavy 700-800 convention used by most SaaS sites.
- Inter `--font-inter` for Utility and body family. Owns all body copy (16px), navigation (14px medium), buttons (14px medium), small labels (10-12px medium), and supporting icons. Consistent -0.0100em letter-spacing keeps it visually aligned to DM Sans at smaller sizes. Two-weight discipline (regular and medium only) keeps the interface feeling light and fast.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Teal Button: Main call-to-action - sign-up, start, explore
- Outline Button: Secondary action - contact, learn more
- Ghost Button: Tertiary or nav-adjacent action
- Search Field: Animation search input in header and hero
- Language Toggle: Locale selector in header
- Feature Tile: Compact 4-column feature highlight with icon
- Brand Case-Study Card: Featured customer animation showcase
- Animation Preview Tile: Lottie animation grid item
- Dark Feature Card: Inverted card for emphasis sections
- Hero Headline: Page-top display headline
- Trust Logo Strip: Social proof band beneath hero
- Footer Block: Site footer

Do:

- Use #019d91 fill + #ffffff text for every primary action button (Get started, Sign up, Explore, See all).
- Apply border-radius 8px to buttons and inputs, 16px to standard cards, 24px to feature/hero panels, 48px to oversized dark hero panels.
- Headlines 32px and above must use DM Sans weight 500 with the matching negative letter-spacing: -0.0300em at 32px, -0.0400em at 48-64px, -0.0500em at 96px.
- Body, navigation, buttons, and small UI copy use Inter only - never mix DM Sans into utility text below 24px.
- Set page background to #f4f4f5 and place raised white cards (#ffffff) on top with 24px or 32px padding.
- Use 1px solid #e4e4e7 or #f2f2f3 as the only border treatment - never thicker than 1px on standard UI.
- Place colorful illustrations and animation thumbnails on the warm-gray canvas with no card chrome - let the artwork be the visual, not a wrapper.

Avoid:

- Never use #000000 pure black as a card or surface fill - use #09090b or #18181b instead so surfaces feel ink-toned, not harsh.
- Never apply weight 700 or 800 to headlines - the system uses weight 500 even at 96px display sizes.
- Never use a drop shadow on cards - the elevation language is built from background contrast and rounded corners, not shadows.
- Never combine #019d91 with bold gradients, glassmorphism, or neon glow - the teal must read as a flat, confident fill.
- Never use #ff6900 (ember) for decoration or branding - it is reserved for warning/attention states.
- Never put body copy below 14px - captions stop at 12px and labels at 10px, and always use weight 500 for non-body sizes under 16px.
- Never break the spacing rhythm: gaps inside components are 4-8px, component-internal padding is 16-24px, between sections is 80px.

Source prompt cues:

Quick Color Reference:
- Primary text: #09090b
- Page background: #f4f4f5
- Card surface: #ffffff
- Border: #e4e4e7
- Accent: #019d91 (teal)
- primary action: #019d91 (filled action)

Example Component Prompts:
1. Create a Primary Action Button: #019d91 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. Create a feature tile row (4 columns): off-white tiles (#ffffff), 16px radius, 24px padding. Each tile has a 32px colored icon block (yellow #f0b100, pink #ff8a80, teal #61f7cf, dark-blue #111827) with a mono icon, then an Inter 14px weight 500 label in #09090b, then Inter 14px weight 400 helper text in #71717b. 16px gap between tiles.
3. Create an animation preview grid: 5 columns on warm-gray (#f4f4f5) canvas, each tile is a white (#ffffff) card with 16px radius, no shadow, transparent inner area where the Lottie animation plays. 16px gap between columns and rows.
4. Create a search input (large): white fill (#ffffff), 1px border #e4e4e7, 8px radius, 16px vertical padding, Inter 16px placeholder text in #71717b, small search icon on the left, K hint chip on the right.
5. Create a footer: full-bleed #09090b fill, white (#ffffff) text, Inter 14px weight 500 for column headers and Inter 14px weight 400 for links in #71717b. Multi-column grid (4-5 columns), logo top-left, social icons right-aligned, 80px top padding and 80px bottom padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
