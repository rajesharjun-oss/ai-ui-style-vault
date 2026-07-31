# AI Implementation Prompt

Build a Kippo-inspired interface using this source-derived style bundle.

Reference site: https://kippo.com
Theme: dark
Category: Other
North star: Pixel arcade boot screen in a black void. Monospace glyphs traced in white neon against a pure black void, with a single hot-pink power-up color that should feel rare and electric when it appears.

Use these palette anchors:

- Kippo Pink `#ee1f66` for Primary action background, accent headings, active badges - the only chromatic voice in the system, rationed to feel like a power-up rather than a brand wash
- Void Black `#000000` for Page canvas, card backgrounds, image fills - the infinite dark that everything else floats on
- Carbon `#29292a` for Elevated card surfaces and secondary panels - barely-distinguishable dark gray for cards that need to step forward from the black canvas
- Ash `#333333` for Subtle borders and dividers where white is too loud - a near-black separator for nested or secondary content
- Ghost White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Sunset Gradient `#ffc400` for Gradient start stop - used only on the warm-to-cool decorative band behind the phone mockup and small accent elements
- Terminal Cyan `#33beff` for Gradient start for cool accents - used sparingly in decorative gradient bands

Use these typography anchors:

- Source Code Pro `--font-source-code-pro` for Sole typeface - used for every text element from nav links to body copy to display headlines. Monospace at 42px/weight 700 with 0.3-0.5em tracking in all-caps creates a retro arcade marquee feel; at 16px/weight 400 it reads as clean monospace body. The slashed-zero feature is enabled, reinforcing the terminal/CRT aesthetic.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 100px.
- Card padding: 30px.
- Element gap: 15px.

Build these component patterns where relevant:

- Primary CTA Button: Filled magenta action - the only solid-fill button in the system
- Ghost Outline Button: Secondary actions, nav-adjacent controls
- Navigation Link: Top-bar nav items
- Outlined Card: Content container - feature blocks, media tiles, info panels
- Press Logo Strip: Social proof band
- App Store Badge: Download CTA
- QR Code Block: Alternative download entry
- Phone Mockup Frame: Hero product showcase
- Code-Style Card Stack: Feature illustration - profile cards fanned out
- Code Block / Terminal Snippet: Feature explainer - product UI preview
- Logo Wordmark: Brand identifier in nav
- Section Heading Pair: Section-level headlines

Do:

- Use Source Code Pro for every text element - body, headings, buttons, nav, labels. No secondary font.
- Set all UI text to uppercase with letter-spacing 0.1em minimum; display headlines should reach 0.3-0.5em tracking.
- Define cards with a 1px #ffffff border on a #000000 or #29292a fill - never with shadow, never with a colored fill.
- Reserve #ee1f66 for the primary CTA background, the accent word in two-tone display headlines, and active/border-current-page states. Use it no more than once per viewport section.
- Use 10px radius for buttons and tags, 15px for cards and images, 50px for icon buttons. Never exceed 15px on rectangular surfaces.
- Maintain generous vertical breathing room: 100-150px between major sections, 30px inside cards, 15px between inline elements.
- Enable the 'zero' font-feature on Source Code Pro so the numeral 0 is slashed - it reinforces the terminal identity.

Avoid:

- Don't introduce a second typeface (no Inter, no Helvetica, no sans-serif fallback for body). Monospace-only is the identity.
- Don't fill cards with color, gradient, or image. Cards are transparent panels - the border is the card.
- Don't use drop shadows for elevation. Depth comes from overlapping layers and outline contrast, never from blur.
- Don't dilute #ee1f66 by using it for body text, borders on non-action elements, or large background areas. It must remain rare.
- Don't use border-radius larger than 15px on rectangular surfaces, and never use fully-rounded pill shapes on buttons (10px max).
- Don't mix light and dark themes - this is a dark-only system. No white-background sections, no theme toggle.
- Don't use red, green, or yellow for semantic states (success/error/warning) - those colors are decorative only in this system, and the dark canvas + white text + single pink accent is the entire signal vocabulary.

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #000000
- surface (elevated card): #29292a
- border: #ffffff (1px)
- accent / primary action: #ee1f66 (filled action)

**Example Component Prompts**
1. Build a hero section on #000000. Left column: two-tone display headline in Source Code Pro 42px weight 700 uppercase, letter-spacing 0.5em, line-height 1.19 - first word in #ee1f66, rest in #ffffff. Subtitle in Source Code Pro 16px weight 400, #ffffff, line-height 1.88. Below: App Store and Google Play badges side by side, then a QR code in a 1px #ffffff-bordered square. Right column: iPhone mockup (radius 40px) on a gradient backdrop (linear-gradient(to right, #ffc400, #ff33e0)).

2. Build a press logo strip. Black canvas, centered max-width 1200px. Label 'AS SEEN ON' in Source Code Pro 12px weight 700 uppercase, tracking 0.1em, #ffffff. Below: a single horizontal row of publication logos (Mashable in its blue, TechCrunch in green, etc.) spaced 60-80px apart. No borders, no card background - logos float on the void.

3. Build an outlined feature card. Background #000000, border 1px #ffffff, radius 15px, padding 30px. Title in Source Code Pro 16px weight 700 uppercase, tracking 0.1em, #ffffff. Body in Source Code Pro 16px weight 400, #ffffff, line-height 1.88. No shadow, no fill, no gradient.

4. Build a primary CTA button. Background #ee1f66, text #ffffff, Source Code Pro 12px weight 700 uppercase, letter-spacing 0.1em, padding 10px 15px, border-radius 10px, no border. This is the only filled button in the system - every other button is a white outline on transparent.

5. Build a section heading pair. Source Code Pro 42px weight 700 uppercase, letter-spacing 0.3-0.5em, line-height 1.19. First key noun in #ee1f66, remaining words in #ffffff. The two-color split within one sentence is a Kippo signature - do not apply it to body text or subheadings.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
