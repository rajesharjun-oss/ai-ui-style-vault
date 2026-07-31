# AI Implementation Prompt

Build a Drepute-inspired interface using this source-derived style bundle.

Reference site: https://drepute.xyz
Theme: dark
Category: Other
North star: midnight observatory over still water - a single sentence floats beneath a field of stars

Use these palette anchors:

- Pure White `#ffffff` for Primary text on dark hero, input fills, light surfaces
- Deep Ink `#000000` for Dominant text and border color across body, nav, and dividers
- Obsidian `#161616` for Dark canvas and hero surface - the page's atmospheric base
- Ash Gray `#bfbfbf` for Subtle input borders, ghost box-shadows, disabled hairlines
- Fog `#a9a9a9` for Secondary body text, muted borders, low-emphasis dividers
- Steel `#7f8080` for Navigation and link borders, tertiary text on light surfaces
- Slate Blue `#8995a9` for Outlined ghost-button border - the only chromatic interactive treatment
- Lagoon Teal `#00a4a6` for Sole accent - link border, indicating the single interactive edge in the system

Use these typography anchors:

- Source Sans Pro `--font-source-sans-pro` for Workhorse sans for body, buttons, nav, inputs, and all UI microcopy; weight 700 reserved for emphasis
- Playfair Display `--font-playfair-display` for Display serif for hero headlines ('Launching Soon') - the single expressive type voice; weight 400 italic-leaning elegance rather than bold
- Montserrat `--font-montserrat` for Wordmark only - 'DREPUTE' set wide at 0.154em to function as a typographic constellation above the hero
- GD Sherpa `--font-gd-sherpa` for Custom brand secondary; deployed alongside Source Sans Pro for select links and image overlays
- Times `--font-times` for Times - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 56px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Full-Bleed Hero: Atmospheric landing surface
- Wordmark Lockup: Brand identity element
- Ghost Outlined Button: Outlined call-to-action
- Minimal Link: Inline navigation link
- Top Notification Bar: Slim promotional strip
- Text Input Field: Form input for email/name capture
- Subscribe Form Block: Email capture below the hero
- Section Divider: Visual break between dark hero and light content
- Chat Widget Bubble: Floating support affordance

Do:

- Use Playfair Display weight 400 exclusively for display text - never go above weight 400; the lightness is the luxury.
- Set the wordmark in Montserrat 700 with 0.154em letter-spacing - this tracking is the brand's signature and must not be reduced.
- Keep the canvas at #161616 for all dark surfaces and reserve #ffffff for light sections below the fold.
- Use 4px radius on every rounded element - buttons, inputs, cards. The system has no soft corners.
- Anchor headlines at 56px+ on Playfair Display and pair with Source Sans Pro 14-16px for all supporting text.
- Use 24px column gaps and 24px element padding as the default rhythm; 56px vertical section padding for hero-style blocks.
- Let the teal #00a4a6 appear only as a single link border - never as a fill, button background, or large surface.

Avoid:

- Do not add shadows, gradients, or glows to any component - the system is flat and photographic.
- Do not introduce pills, circles, or any radius above 4px.
- Do not use color fills on buttons - all actions are ghost/outlined with border-only treatment.
- Do not use Playfair Display below 44px - it is a display face, not a body face.
- Do not place body text directly over the hero photograph without a #161616 backing layer - contrast must remain AAA.
- Do not add more than one chromatic accent - the teal is singular; adding another color breaks the cinematic restraint.
- Do not use bold (600+) on the wordmark - weight 700 is the ceiling, and it only applies to Montserrat.

Source prompt cues:

**Quick Color Reference**
- background: #161616 (dark) / #ffffff (light)
- text: #ffffff (on dark) / #000000 (on light)
- border: #a9a9a9 (body) / #8995a9 (button)
- accent: #00a4a6 (teal link border only)
- muted text: #7f8080
- primary action: #00a4a6 (outlined action border)

**Example Component Prompts**
1. Build the hero: full-viewport #161616 background with a full-bleed landscape photograph. Center 'Launching Soon' in Playfair Display 62px weight 400, #ffffff, normal tracking, vertically centered. Top-center wordmark 'DREPUTE' in Montserrat 700, 26px, #ffffff, letter-spacing 0.154em (4px), uppercase, 56px from top edge.
2. Build the ghost outlined button: transparent fill, 1px #8995a9 border, 4px radius, 8px vertical and 24px horizontal padding. Text: Source Sans Pro 14px weight 700, color #8995a9, uppercase. On hover, border darkens to #000000.
3. Build the subscribe form section: #161616 background, 56px vertical padding. Heading 'Subscribe' in Playfair Display 44px weight 400, #ffffff, centered. 32px gap below. Single horizontal row: email input (#ffffff fill, 1px #bfbfbf border, 4px radius, Source Sans Pro 16px) + ghost button (1px #8995a9 border, Source Sans Pro 14px 700, 4px radius), 24px gap between them.
4. Build the top notification bar: full-width #ffffff strip, 56px vertical padding, centered single-line content in Source Sans Pro 14px #000000. Include an inline link with 1px #00a4a6 border-bottom on hover, and a ghost button (1px #000000 border, 4px radius, Source Sans Pro 14px 700) to the right.
5. Build the chat widget: 48px circle, #161616 fill, 1px rgba(191,191,191,0.3) ring, fixed bottom-right with 24px margins, single white line-icon centered inside.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
