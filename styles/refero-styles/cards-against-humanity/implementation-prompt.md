# AI Implementation Prompt

Build a Cards Against Humanity-inspired interface using this source-derived style bundle.

Reference site: https://www.cardsagainsthumanity.com
Theme: dark
Category: Media
North star: Scattered playing cards on a velvet game table - the design language is the game itself, not a wrapper around it.

Use these palette anchors:

- Game Night Black `#000000` for Page background, card shadows, button borders, heading text on light surfaces
- Card White `#ffffff` for Card surfaces, body text on dark, button borders, input fills
- Signal Red `#fe2f2f` for Primary accent border on cards and badges - the brand's loudest punctuation, used as outline not fill
- Royal Violet `#7333f1` for Primary accent border on cards and badges - deep saturated purple carrying the brand's irreverent energy
- Antique Gold `#d7b73b` for Primary accent border on cards and badges - warm yellow-gold that rounds out the three-color system
- Lemon Card `#fffe5b` for Card face fill for highlighted playing cards in the scattered background
- Lavender Card `#ede5ff` for Card face fill for pastel playing cards, soft purple surface
- Cobalt Card `#1b5bff` for Card face fill for blue playing cards, saturated blue accent surface
- Sky Card `#a0e9ff` for Card face fill for light blue playing cards
- Bubblegum Card `#ffa0f0` for Card face fill for pink playing cards
- Mint Card `#b4ff91` for Card face fill for green playing cards
- Tangerine Card `#ff9559` for Card face fill for orange playing cards

Use these typography anchors:

- Helvetica Neue LT `--font-helvetica-neue-lt` for The site's sole typeface. Weight 800 dominates everything from body up through 80px display - this anti-hierarchy choice makes the brand feel like it's shouting a punchline rather than presenting information. Tight leading at display sizes (0.98-1.07) creates an impactful block, generous leading on body (2.0-2.86) lets the heavy weight breathe. No letter-spacing tricks; the geometry of Helvetica at 800 weight does all the work.
- Helvetica Neue `--font-helvetica-neue` for Helvetica Neue - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 50px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Playing Card (Core Content Unit): The fundamental content container - white rectangle with black text, used for both product cards and content blocks
- Outlined Pill Button (Primary): Main action button on dark backgrounds
- Outlined Pill Button (On Light): Action button on white card surfaces
- Bordered Accent Card: Featured card with chromatic border for emphasis
- Pastel Card: Colored playing card surface used in the scattered background composition
- Cookie/Modal Dialog: Overlay consent interface
- Top Navigation Bar: Site header with brand and nav links
- Section Display Heading: Hero-level typography for section openers like "Buy the game."
- Checkbox Control: Form input within the cookie settings dialog
- Badge / Tag: Small accent labels, potentially for product variants or tags

Do:

- Use weight 800 for all headings and display text - the heavy Helvetica is the brand's voice
- Apply the 2px inset shadow as border treatment on all interactive elements instead of stroke or drop-shadow
- Use pill shapes (38-64px radius) for all buttons and badges
- Compose backgrounds with scattered white cards at varied rotations to reinforce the game-table atmosphere
- Restrict chromatic color to the three brand accents (Signal Red, Royal Violet, Antique Gold) used as borders only, not fills
- Set display text line-height to 0.98-1.07 at 55px+ sizes for tight, impactful stacking
- Invert color polarity (black on white / white on black) at section boundaries rather than introducing new colors

Avoid:

- Don't use weight 400 for anything above 16px - the site's voice is uniformly heavy
- Don't apply drop shadows for elevation - the 2px inset border system is the only depth treatment
- Don't fill large areas with chromatic color - accent colors are outlines, not backgrounds
- Don't use border-radius below 13px on cards or below 32px on buttons - the geometry must read as physical cards
- Don't add gradient fills - the palette is strictly flat, the only complexity comes from scattered card composition
- Don't use letter-spacing tricks - the raw Helvetica geometry at weight 800 is the entire typographic system
- Don't introduce blues, greens, or pinks as UI chrome - those colors exist only as card face fills in decorative scatter

Source prompt cues:

**Quick Color Reference**
- text (on dark): #ffffff
- text (on light): #000000
- background (dark sections): #000000
- background (light sections): #ffffff
- border / accent outline: use Signal Red (#fe2f2f), Royal Violet (#7333f1), or Antique Gold (#d7b73b) - pick one per element
- primary action: #000000 (filled action)

**Example Component Prompts**
1. Hero section on black (#000000). Scattered white card rectangles in the background, rotated -15 to +20 at various sizes, some with 2px borders in Signal Red, Royal Violet, or Antique Gold. Headline: "Cards Against Humanity" at 80px, Helvetica Neue LT weight 800, #ffffff, line-height 0.98. Subtext at 20px weight 800, #ffffff.

2. Outlined pill button: transparent fill, 2px white (#ffffff) inset border, 38px border-radius, 12px vertical / 32px horizontal padding. Text: 16px Helvetica Neue LT weight 800, #ffffff, centered.

3. Content card: white (#ffffff) background, 2px black (#000000) inset shadow as border, 13px border-radius, 20px padding. Heading inside: 28px weight 800, #000000, line-height 1.3. Body text: 16px weight 400, #000000, line-height 2.38.

4. Cookie/modal dialog: centered overlay on darkened scrim. Background #000000, 13px border-radius, 30px padding. Heading "Cookie Settings" at 24px weight 800, #ffffff. Body text at 14px weight 400, #ffffff. Three outlined pill buttons (Accept All / Reject All / Confirm My Choices) at the bottom, white 2px borders on transparent fill, 38px radius.

5. Section divider/transition: full-bleed band switching from #000000 to #ffffff. Display heading at 65px weight 800, color inverts with the background. 50px vertical padding above and below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
