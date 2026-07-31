# AI Implementation Prompt

Build a Podcorn-inspired interface using this source-derived style bundle.

Reference site: https://podcorn.com
Theme: light
Category: Media
North star: Indie magazine spread on warm blush paper. A cream canvas carrying deep-indigo editorial typography, hand-drawn illustrations framed in hairline rectangles, and a single coral button as the only warm mark on the page.

Use these palette anchors:

- Blush Cream `#fff4f2` for Page canvas - warm off-white that sets the editorial tone and makes the deep-indigo text read like printed ink on heavy paper
- Pure White `#ffffff` for Card surfaces, nav background, button fills on light backgrounds - stacked above the cream canvas to create depth without shadow
- Ink Violet `#090335` for Primary text, headings, filled CTA buttons, nav links, hairline borders - the single dominant color of the entire interface; near-black with a violet undertone gives headings personality without abandoning readability
- Coral Flame `#fc736c` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Peach Whisper `#ffb0a1` for Orange decorative accent for icons, marks, and small graphic details. Do not promote it to the primary CTA color
- Deep Navy `#132645` for Illustration detail fill (SVG artwork) - cooler sibling of Ink Violet used inside drawings to add tonal range to the editorial illustrations
- Graphite `#434352` for Secondary nav text and nav borders - a softer alternative to Ink Violet for tertiary labels and dividers
- Silver Mist `#8993a2` for Muted nav borders and inactive control outlines
- Hairline `#d8d8d8` for Hairline link underlines and subtle dividers
- Zinc Mute `#71717d` for Helper text and tertiary metadata

Use these typography anchors:

- Gilroy `--font-gilroy` for Primary interface typeface - body text, navigation, buttons, card labels, footer. Geometric sans with tight tracking gives UI elements a confident, contemporary voice.
- Georgia `--font-georgia` for Headline and hero typeface - a classical serif reserved for editorial moments. The serif/sans pairing is the site's most distinctive typographic decision: Georgia carries warmth and craft, Gilroy carries clarity and UI density. Mixing these creates an indie-magazine feel that distinguishes Podcorn from generic SaaS layouts.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20-27px.
- Element gap: 20px.

Build these component patterns where relevant:

- Coral CTA Button (Nav): Primary call-to-action in top nav
- Ink Filled Button: Primary action on hero and feature blocks
- Ghost Outlined Button: Secondary action
- Top Navigation Bar: Site header with brand, links, and dual CTAs
- Hero Text Block: First-fold headline and supporting copy
- Illustration Frame: Hand-drawn artwork container
- Feature Card (Two-Column Row): Side-by-side feature explanation blocks
- Brand Logo Strip: Social proof band showing partner brands
- Cookie Consent Dialog: Privacy compliance overlay
- Sign Up Badge: Small label indicating available action

Do:

- Use Georgia 40px weight 700 in Ink Violet for all major headlines - the serif/sans pairing is the site's identity
- Reserve #fc736c Coral for exactly one element per view: the primary CTA. Never use it for backgrounds, text, or decoration
- Apply -0.187em letter-spacing to all Gilroy text to match the compact geometric rhythm
- Frame every hand-drawn illustration with a 1.5-2px Ink Violet #090335 border and 0px radius - the rectangular frame is structural, not optional
- Stack surfaces as Blush Cream canvas White card Coral CTA Ink Violet filled button for depth without shadows
- Use 6px radius for all buttons and 8px for cards - keep corners gentle, never pill-shaped (9999px) on UI controls
- Maintain 80px section gaps and 20-27px internal padding to preserve the airy editorial rhythm

Avoid:

- Never use drop shadows, blurs, or glow effects - depth comes from surface color shifts only
- Never use the Coral accent on text, borders, or icon fills - it is a button-only color
- Never apply Georgia to body text, nav, or buttons - reserve it for headings and hero copy only
- Never round illustration frames - the 0px rectangular border is essential to the editorial frame metaphor
- Never use pure black #000000 for primary text - Ink Violet #090335 is the text standard
- Never place photography or product screenshots inside the cream sections - illustrations only
- Never use emoji, gradient fills, or neon accents - the palette is deliberately limited to cream, white, ink-violet, and coral

Source prompt cues:

**Quick Color Reference**
- text: #090335 (Ink Violet)
- background: #fff4f2 (Blush Cream)
- surface/card: #ffffff (Pure White)
- border: #d8d8d8 (Hairline) or #090335 (Ink Violet for emphasis)
- accent/illustration: #fc736c (Coral) and #ffb0a1 (Peach Whisper)
- primary action: #090335 (filled action)

**3-5 Example Component Prompts**
1. Create a hero section: Blush Cream #fff4f2 background, 1200px max width. Left column holds a Georgia 40px weight 700 Ink Violet headline with line-height 1.44, followed by Gilroy 18px weight 400 body text in Ink Violet, then an Ink Filled Button (#090335 bg, white text, 18px/27px padding, 6px radius). Right column holds an Illustration Frame: 2px Ink Violet border, 0px radius, containing a hand-drawn line illustration using #132645 strokes and #fc736c + #ffb0a1 fills.

2. Build a top navigation bar: white #ffffff background, 64px height, 1px #d8d8d8 bottom border. Left: brand logo with 'Creator Lab' badge. Center: Gilroy 15px weight 500 Ink Violet links. Right: Ghost Outlined 'Log In' button (1px #090335 border, transparent fill, 6px radius, 18px/20px padding) followed by Coral CTA 'Sign Up' (#fc736c fill, white text, 6px radius, 18px/20px padding).

3. Construct a feature row: Blush Cream background, two equal columns with 60px gap. Left column: Georgia 25px weight 700 Ink Violet subheading, Gilroy 18px weight 400 Ink Violet body text. Right column: Illustration Frame with 2px #090335 border, 0px radius, containing custom artwork with #132645 linework and #fc736c fills. No card backgrounds, no shadows.

4. Design a cookie consent dialog: white #ffffff background, 8px radius, fixed bottom-left, 24px padding. Title 'Customize Your Cookie Choices' in Gilroy 16px weight 700 Ink Violet. Body text Gilroy 14px weight 400 in #434352. Three stacked ghost buttons: 1px #090335 border, transparent fill, Ink Violet text, 6px radius, 18px/20px padding.

5. Create a brand logo strip: white #ffffff background band, horizontal flex row of 6-8 grayscale partner logos rendered in #000000, evenly spaced with 40px gap, 40px vertical padding. Logos are monochrome, no color treatment.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
