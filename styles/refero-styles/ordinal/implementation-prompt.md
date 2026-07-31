# AI Implementation Prompt

Build a Ordinal-inspired interface using this source-derived style bundle.

Reference site: https://www.meetassembly.com
Theme: dark
Category: SaaS
North star: dark observatory with one mint filament - a near-black room where a single neon green switch glows as the only thing that matters

Use these palette anchors:

- Void Canvas `#151316` for Page background, hero canvas, footer - near-black with a faint violet undertone that keeps the dark from feeling flat or sterile
- Paper `#ffffff` for Primary text and icon color on dark surfaces; borders on dark UI; inverted text on light feature cards
- Elevated Surface `#444245` for Card and panel surface above the void canvas - subtle lift achieved through one tonal step rather than shadow
- Mist `#8e8e8e` for Muted body text, hairline dividers, inactive icon strokes, and low-emphasis borders on dark backgrounds
- Smoke `#585657` for Mid-weight borders and subtle UI separators - slightly darker than Mist for structural rules
- Ash `#b9b9b9` for Light-mode body borders and secondary text on warm light sections
- Bone `#f4f2ee` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Charcoal `#222222` for Primary text on light feature sections and nav borders in light mode
- Mint Filament `#8ef5b5` for The single chromatic accent - filled primary CTAs, eyebrow pill labels, active nav indicator, logo glow, and green-text logo tints. Against #151316 the contrast is 14:1, making it legible as both text and fill

Use these typography anchors:

- Inter `--font-inter` for Entire UI - body, nav, headings, buttons, cards. Only two weights used (regular 400, medium 500) which is the core typographic discipline: no bold display weight, no light italic, just calm and confident Inter. The 13px/17px pair forms the dense product text; 40-60px carries the marketing voice. Headlines use -0.03em tracking to pull letters tight against the dark canvas.
- Inconsolata (custom-mapped eyebrow face) `--font-inconsolata-custom-mapped-eyebrow-face` for Eyebrow labels, status pills, and small ALL CAPS markers like 'ASSEMBLY 15 NOW ORDINAL', 'SCHEDULING', 'WATCH A DEMO 4:15'. The monospace character at 13-17px is a deliberate break from Inter's proportions - signals 'metadata / system status / not body content'. 0.01em positive tracking on the eyebrow adds the ALL CAPS breath small caps need.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Persistent header on dark canvas
- Mint Pill CTA (Primary): Highest-emphasis action button - reserved for the single most important action per screen
- Ghost Outlined Button: Secondary action beside a mint CTA
- Eyebrow Label Pill: Section or status marker above headlines
- Hero Headline: Page-level value proposition
- Product Screenshot Frame: Hero visual - the product UI is the image
- Feature Block Card: Feature explanation in the light section of the page
- Feature Section Heading: Section-level title in the light/mixed area
- Logo Wall Cell: Social proof - customer logos
- Calendar Product Surface: Screenshot inside the hero - demonstrates the scheduling grid
- Social Platform Icon Tile: Brand-color icon set inside feature block
- Footer: Closing surface

Do:

- Use #8ef5b5 for exactly one filled action per view - never two mint buttons side by side
- Pair every mint CTA with a #ffffff ghost outlined button as the secondary action
- Set border-radius to 5px for cards, inputs, and small buttons; reserve 1440px only for pill CTAs and eyebrow labels
- Restrict headings to Inter weight 500 - no 600/700, no italic; the calm weight IS the hierarchy
- Apply -1.8px letter-spacing at 60px and -0.01em at body sizes to maintain Inter's tight display rhythm
- Render eyebrows as Inconsolata 13px 500 in #8ef5b5, uppercase, inside a 1440px pill with a 1px green border
- Keep the page 95%+ achromatic - mint appears only on the active CTA, the eyebrow label, and ~50% of customer logos

Avoid:

- Don't introduce a second brand color - the system is monochrome + one mint, nothing else
- Don't use shadows to separate cards from the void - step the surface to #444245 instead
- Don't set headings in bold or semibold; weight 500 is the ceiling
- Don't use decorative gradients on body content - the teal charcoal gradient only appears behind the hero product screenshot
- Don't add rounded corners larger than 18px to cards - the system reads precise, not soft
- Don't use the mint as a background fill for large sections; it loses the 'single switch' effect
- Don't stack the ghost button on ghost button; every secondary action must be ghost, and the tertiary is a text link

Source prompt cues:

primary action: #8ef5b5 (filled action)
Create a Primary Action Button: #8ef5b5 background, #222222 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
**Quick Color Reference**
- text (on dark): #ffffff
- text (muted): #8e8e8e
- background: #151316
- card surface: #444245
- border: #585657
- accent: #8ef5b5 (primary action, eyebrow label, active state)
- light-section background: #ffffff, text #222222

**Example Component Prompts**


2. *Product screenshot card*: White #ffffff surface, 5px radius, soft shadow 0 20px 60px rgba(0,0,0,0.5). Sits on a 170deg gradient from #24574d to #3a3a3a as backdrop.


4. *Logo wall row*: 8-column grid on #151316, no card chrome, 40px row height, logos rendered flat in #8ef5b5 (highlighted) or #ffffff (neutral). 1px #585657 top border on the section.

5. *Eyebrow label*: 1440px pill, 1px #8ef5b5 border, 5px/16px padding, Inconsolata 13px 500 #8ef5b5, uppercase, letter-spacing 0.01em. Use above section headings to mark theme.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
