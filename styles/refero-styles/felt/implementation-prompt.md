# AI Implementation Prompt

Build a Felt-inspired interface using this source-derived style bundle.

Reference site: https://www.felt.com
Theme: dark
Category: SaaS
North star: topographic atlas at dusk - moss-green pages, serif headlines, one amber needle

Use these palette anchors:

- Moss Canvas `#314218` for Page background, hero sections, dominant canvas - the deep mossy green that carries the entire site and grounds the editorial atmosphere
- Fern `#3d521e` for Mid-green surface for cards, elevated panels, and the topside of the surface stack
- Lichen `#64754b` for Muted green for secondary surfaces, borders on cards, and subtle dividers against the canvas
- Forest Floor `#212f0c` for Deeper green for nested surface layers and inset product UI backgrounds
- Deep Bog `#18210c` for Darkest green for the deepest surface layer, code blocks, and high-contrast panels
- Amber Compass `#dc8c46` for Primary action - filled CTA buttons, link borders, active link text. The single warm accent that cuts through the green monochrome like a compass needle
- Bone White `#ffffff` for Primary text, heading color, button text on amber fills, and the dominant border for ghost/outlined controls
- Parchment `#eeeeee` for Light surface for embedded product UI, inset map views, and light-mode panel surfaces against the dark canvas
- Charcoal `#333333` for Text and borders inside the light parchment product UI panels - the dark-on-light text color for embedded app surfaces
- Limestone `#d8dcd2` for Soft warm-tinted gray for badge backgrounds, subtle borders, and muted helper text inside light panels
- Ink `#000000` for SVG fills, max-contrast elements, and the map marker pin color

Use these typography anchors:

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- GT Alpina Standard `--font-gt-alpina-standard` for Display and heading serif - the editorial headline face. Used at large sizes for hero headlines and section titles. The tight negative tracking (-0.033em to -0.040em) and line-height under 1.0 give the serif a compressed, almost carved-into-stone quality that evokes old cartographic title plates. This is the signature type choice: a humanist serif that feels hand-drawn rather than mechanical.
- Atlas Grotesk `--font-atlas-grotesk` for Primary UI and body sans-serif - handles navigation, body text, button labels, badges, and links. The slight positive tracking (0.033em) on body sizes adds legibility on the dark green canvas. The grotesque geometry provides a clean utility counterpoint to the expressive serif headlines.
- Times New Roman `--font-times-new-roman` for Fallback system serif at extreme display sizes. The 101px / 0.88 line-height ratio confirms the compressed display treatment for the largest headlines.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Amber CTA Button: Primary action - filled button for conversion moments
- Ghost Link Button: Secondary action - text link with underline border treatment
- Navigation Bar: Top-level site navigation
- Hero Section: Above-the-fold headline and CTA zone
- Scrolling Ticker Banner: Top announcement bar
- Product UI Panel: Embedded application screenshot / product surface
- Client Logo Row: Social proof - trusted-by brand logos
- Feature Section: Mid-page content blocks with headline + product visual
- Badge / Tag: Category labels and metadata tags
- Map Marker Pin: Interactive map point indicator

Do:

- Use GT Alpina Standard weight 300 for all display and section headlines - the thin serif is the brand's most distinctive choice and must carry the editorial voice
- Set display headlines at 86px with line-height 0.88 and letter-spacing -3.44px for the compressed, carved-into-stone effect
- Use Amber Compass (#dc8c46) exclusively for filled CTAs and accent moments - never as a surface fill or decorative wash
- Step surfaces using the green scale: Moss Canvas (#314218) Fern (#3d521e) Lichen (#64754b) for elevation, not shadows
- Set body and UI text in Atlas Grotesk weight 400 with 0.033em letter-spacing for legibility on the dark green canvas
- Embed product UI panels in light surface (#ffffff) with 6px radius and the single subtle shadow to create contrast against the dark page
- Maintain centered, magazine-style layouts with 80px section gaps - the page rhythm should feel like turning pages in an atlas

Avoid:

- Don't use Amber Compass (#dc8c46) for body text, backgrounds, or large surface areas - it loses its compass-needle effect when overused
- Don't set serif headlines at line-height above 1.0 - the compressed treatment is essential to the editorial feel
- Don't apply multiple shadow layers - Felt uses elevation through color stepping, not shadow stacks
- Don't use pure black (#000000) as a page background - the mossy green tones are the canvas, not black
- Don't replace GT Alpina Standard with a geometric or grotesque display face - the serif is the brand identity
- Don't use border-radius above 6px on cards, images, or product panels - only buttons get the 20px pill radius
- Don't introduce new accent hues - the entire palette is green monochrome plus one warm amber; any other color breaks the system

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
