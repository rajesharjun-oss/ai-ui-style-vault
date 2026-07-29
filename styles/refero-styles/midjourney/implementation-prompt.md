# AI Implementation Prompt

Build a Midjourney-inspired interface using this source-derived style bundle.

Reference site: https://midjourney.com
Theme: dark
Category: AI
North star: Deep-ocean bioluminescent terminal. A pressurized darkness where intelligence visibly generates itself in ASCII streams, and controls appear as faintly glowing specimens.

Use these palette anchors:

- Abyssal Blue `#0f1c36` for Secondary surface backgrounds, button background variant - a step lighter than Cosmic Void for subtle depth layering
- Steel Navy `#1d293d` for Card surfaces, nav background, interactive container backgrounds
- Deep Slate `#314062` for Elevated card or hover state backgrounds
- Mist `#cad5e2` for Primary body text, general UI text - slightly blue-gray rather than pure white, reducing harshness against the dark void backgrounds
- Fog `#e5e7eb` for Borders, dividers, icon strokes throughout the UI
- Ash `#2e3038` for Secondary text, subdued labels
- Ghost White `#ffffff` for Heading text at maximum contrast
- Ice Blue `#ebf8ff` for High-brightness text on dark surfaces, link contrast text
- Portal Blue `#63b3ed` for Hyperlinks, inline text links - the single fully saturated accent visible in body content, connecting to Midjourney's Discord/community ecosystem
- Bioluminescent Green `#004f3b` for Sign Up pill button background (20% opacity tint) - deep green specimen glow against void
- Terminal Amber `#733e0a` for Explore pill button background (20% opacity tint) - amber specimen variant
- Crimson Depth `#8b0836` for Log In pill button background (20% opacity tint) - deep red specimen variant
- Specimen Green `#00bc7d` for Icon strokes and decorative SVG fills - vivid but used sparingly in iconography only
- Warning Amber `#f0b100` for Icon and UI accent strokes - section heading icons (Projects , About )
- Fault Red `#ff2056` for Icon strokes, error-adjacent SVG fills

Use these typography anchors:

- JetBrains Mono `--font-jetbrains-mono` for Every typographic role on this site - navigation labels, body copy, headings, buttons, links. Using a monospace font as the universal typeface (not just for code) makes the entire interface read as an active terminal output. 30px at lineHeight 1.25 serves section headings; 16px at 1.50 serves body and UI labels; 14px at 1.63 serves captions and metadata.
- DM Sans `--font-dm-sans` for Secondary UI copy and body text in prose sections - appears at 16px only. Weight 500 for emphasis within body blocks. Provides a subtle humanist contrast against the monospace primary, used sparingly so the terminal character of JetBrains Mono dominates.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 800px.
- Section gap: 64px.
- Card padding: 32px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Sign Up Pill Button: Primary registration CTA in navigation
- Log In Pill Button: Secondary auth action in navigation
- Explore Pill Button: Navigation action for main product discovery
- Documentation Tab: Navigation label for technical docs section
- Section Heading with Icon: Page section titles (About, Projects, Careers)
- Project Image Card: Visual showcase grid for AI-generated imagery
- Sticky Navigation Bar: Primary site navigation across all pages
- Hero ASCII Animation Background: Full-viewport hero visual
- Inline Body Link: Hyperlinks within prose content
- Background Gradient Surface: Full-page atmospheric depth layer

Do:

- Use JetBrains Mono as the primary typeface for all UI elements - navigation, headings, buttons, body copy - treating monospace as the visual identity, not a code-context exception.
- Apply the three-color pill button system (green/amber/red tints at ~20% opacity) only for the Sign Up / Explore / Log In triad - do not extend the specimen-color scheme to other button types.
- Set all page backgrounds to #06051d or the gradient variant linear-gradient(0deg, #06051d 30%, #061434) - never use pure #000000, which would flatten the violet cosmic depth.
- Use 9999px border-radius for all pill buttons and 8px for all card/image containers - no intermediate values; the contrast between fully rounded and gently rounded is the shape system.
- Render section headings at 30px JetBrains Mono weight 400 with a small amber #f0b100 icon prefix - never increase to bold weights, the whisper-weight at large sizes is the signature.
- Use #63b3ed Portal Blue exclusively for inline hyperlinks and flat navigation text links - it is the only fully visible chromatic color in body content.
- Maintain 64px vertical gap between page sections to preserve the spacious, pressurized-void atmosphere between content blocks.

Avoid:

- Do not use any sans-serif or serif font as a heading font - DM Sans is for body prose only; JetBrains Mono must dominate the typographic hierarchy.
- Do not create solid-fill opaque buttons - the translucent 20% opacity tinted backgrounds on pills are the system; solid fills break the bioluminescent specimen aesthetic.
- Do not introduce light backgrounds (#ffffff, light grays) into page sections - the design has no light mode; all surfaces must remain within the #06051d to #314062 dark range.
- Do not use more than three accent tint colors for buttons - the red/green/amber specimen triad is a closed system; adding new button colors dilutes the precision.
- Do not bold section headings or use font-weight above 500 anywhere in the UI - weight 400 at display sizes is the deliberate anti-convention choice that defines the visual voice.
- Do not add decorative imagery or photography - the only permitted visuals are AI-generated monochromatic renders and the ASCII/generative text hero.
- Do not apply colored backgrounds to body text sections - prose content must sit directly on #06051d Cosmic Void with #cad5e2 Mist text, no content cards with contrasting backgrounds.

Source prompt cues:

**Quick Color Reference**
- Page background: #06051d (with gradient to #061434)
- Primary text: #cad5e2
- Headings: #ffffff
- Inline links: #63b3ed
- Borders/dividers: #e5e7eb
- Nav surface: #1d293d
- Sign Up button bg: #004f3b at 20% opacity, text: #00bc7d
- Log In button bg: #8b0836 at 20% opacity, text: #fff1f2
- Explore button bg: #733e0a at 20% opacity, text: #fefce8

**Example Component Prompts**

1. **Hero section**: Full-viewport background using linear-gradient(0deg, #06051d 30%, #061434). Center a dense ASCII text animation in #cad5e2 at ~5% opacity forming a sphere shape. Overlay the text 'Midjourney' at 36px JetBrains Mono weight 400 #ffffff centered. Place three pill buttons (Sign Up green, Log In red, Explore amber) horizontally centered at bottom of hero with 16px gaps.

2. **Navigation bar**: Full-width #1d293d background, 8px vertical padding, 48px horizontal padding. Left: 'Documentation' (JetBrains Mono 14px #63b3ed, no padding, 0px radius) and 'Explore' pill (amber tint). Right: 'Sign Up' (green pill) and 'Log In' (red pill). Pills use 9999px radius, 8px 20px padding, white border at 10% opacity.

3. **Section heading**: Left-aligned amber icon (16px #f0b100) + text label 'Projects' at 30px JetBrains Mono weight 400 #ffffff with 8px gap between icon and text. No bold, no uppercase, no letter-spacing modification.

4. **Project image grid**: 4-column grid, 8px column and row gap. Each cell: square-aspect image with 8px border-radius, monochromatic blue-violet AI-generated content, #e5e7eb border at 15% opacity. No hover text, no captions below images.

5. **Body prose block**: Max-width 640px within the 800px page column. JetBrains Mono 16px weight 400, #cad5e2, lineHeight 1.5. Inline links in #63b3ed with no underline. Paragraph gap: 16px. Sits directly on #06051d background with no card container.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
