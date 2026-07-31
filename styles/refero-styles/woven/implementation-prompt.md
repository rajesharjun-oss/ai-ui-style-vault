# AI Implementation Prompt

Build a Woven-inspired interface using this source-derived style bundle.

Reference site: https://wovenwhisky.com
Theme: light
Category: E-commerce
North star: Ink on cream parchment. A distiller's editorial spread where warm cream canvases, a single dark ink color, and wide-tracked uppercase type create the only visual structure; product photography provides all the color.

Use these palette anchors:

- Parchment Cream `#eeede5` for Page canvas, footer surface, and dominant background - the warm off-white that gives the entire site its editorial, paper-like feel
- Ink Black `#232323` for Primary text, all hairline borders, footer ink, and the near-black that forms every structural line on the page
- Pure White `#ffffff` for Product card surfaces, alternating section backgrounds, and high-contrast text on dark or photographic surfaces
- Iron Gray `#4a4a4a` for Secondary body text, subdued borders, and the muted text layer that sits between primary ink and background
- Soft Stone `#ddddda` for Subtle surface differentiation beneath cards and secondary panels - barely warmer than the cream canvas

Use these typography anchors:

- Spezia Semi-Mono `--font-spezia-semi-mono` for The workhorse typeface for body copy, navigation links, card text, list items, and most UI labels. Semi-mono construction gives it a precise, typeset quality that reinforces the editorial identity. 700 weight is used sparingly for emphasis within mono-spaced blocks.
- Spezia Medium `--font-spezia-medium` for Headline and display font - the proportional companion to the Semi-Mono, used for the hero wordmark 'WOVEN' and section titles. Single weight keeps the type system disciplined; contrast comes from size and tracking, not weight.
- Figtree `--font-figtree` for Small UI utility font for buttons, icon labels, and tight navigation tags. Rounds out the system where a humanist sans feels warmer than the mono family.
- Spezia Semi-Mono Light `--font-spezia-semi-mono-light` for Lighter voice for inputs, helper text, and link descriptions - a whisper-weight variation that creates hierarchy without bold.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 120-160px.
- Card padding: 26px.
- Element gap: 20px.

Build these component patterns where relevant:

- Minimal Header Bar: Site-wide navigation
- Hero Overlay Wordmark: Full-viewport brand statement
- Split Footer-Letterhead Bar: Brand seal and category navigation
- Section Heading Block: Subsection label
- Latest Releases Dual Card: Side-by-side product showcase
- Product Range Card: E-commerce product tile
- Underlined Text Link: Navigation and category links
- Ghost Icon Button: Cart and menu triggers
- Circular Brand Seal: Decorative wordmark medallion
- Image Container: Product photography frame

Do:

- Use Parchment Cream (#eeede5) as the page canvas for every primary section; alternate to pure white (#ffffff) only for product card surfaces and one or two contrast bands
- Set all body and UI text in Spezia Semi-Mono, 14-15px, with letter-spacing of 0.063-0.094em for uppercase labels and 0.121-0.167em for nav and tag text
- Use 1px #232323 hairlines for every border - cards, product frames, footer rules, link underlines - never use any other color for borders
- Keep corner radius at 0px for all cards, buttons, tags, inputs, and images; the system relies on sharp edges, not curves
- Center section headings in uppercase Spezia Semi-Mono 14px and let 40-60px of vertical space do the visual separation work
- Use Spezia Medium at 32px+ for all display headlines and the wordmark; this is the only proportional (non-mono) face in the system
- Break multi-word links into one-word-per-line stacked columns to create the editorial columnar rhythm in header and footer areas
- Let product photography provide all color in the system; never introduce chromatic accents, gradients, or brand colors

Avoid:

- Never add a chromatic accent color, gradient, or brand fill - the system is 0% colorful by design
- Never use rounded corners on cards, buttons, inputs, or images - 0px radius is intentional and defines the editorial print look
- Never apply box-shadow, drop-shadow, or blur effects - surfaces separate through color and hairline borders only
- Never use bold (700) weight for body paragraphs; reserve 700 for short emphasized spans within mono text blocks
- Never set headings left-aligned with body copy; section titles are always centered with generous vertical space above and below
- Never introduce an icon system with fills, duotones, or color - icons are single-weight 1.5-2px #232323 line work only
- Never place text directly on a product photograph without a cream or white surface underneath; readability requires a solid layer
- Never use display sizes below 32px for the wordmark or section openers; the type scale's authority comes from its restraint at small sizes and generosity at large ones

Source prompt cues:

**Quick Color Reference**
- Canvas: #eeede5 (Parchment Cream)
- Card surface: #ffffff (Pure White)
- Primary text/border: #232323 (Ink Black)
- Secondary text: #4a4a4a (Iron Gray)
- Subtle surface: #ddddda (Soft Stone)
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Hero section*: Full-bleed photograph of an amber whisky bottle as background. Overlaid centered wordmark 'WOVEN' in Spezia Medium, ~200px, #ffffff at 60% opacity. Below the hero viewport, a 90px-tall Parchment Cream (#eeede5) band with the centered uppercase label 'EXPERIENCE WHISKY' in Figtree 12px, letter-spacing 0.167em, #232323.

2. *Product range card*: White (#ffffff) card, 0px radius, 1px #232323 hairline border, ~45% page width. Bottle photograph fills the upper 75% edge-to-edge with no padding. Below, 26px card padding containing the product name 'HOMEMADE' centered in Spezia Semi-Mono 14px uppercase, letter-spacing 0.094em, and the price ' 45' 10px below in Figtree 14px, #232323. No shadow.

3. *Split footer-letterhead bar*: Parchment Cream (#eeede5) band, 160px tall. Centered circular seal (160px diameter, 1px #232323 border) containing stacked uppercase text 'WOVEN / WHISKY MAKERS / THE WORLDWIDE'. Below at the band edges: left-aligned three-line link 'WORLDWIDE / WHISKY / MAKERS' and right-aligned 'BLENDING / BEYOND / BORDERS', each word underlined with a 1px #232323 rule, 12px uppercase, Spezia Semi-Mono.

4. *Section heading with product grid*: Parchment Cream (#eeede5) canvas. Centered uppercase label 'DISCOVER OUR RANGE' in Spezia Semi-Mono 14px, letter-spacing 1.17px, #232323, with 50px space below. Two product cards side by side, 8px gap, 0px radius, 1px #232323 border, white fill, edge-to-edge bottle photos above centered name + price.

5. *Underlined stacked text link*: Narrow left-aligned column, each word on its own line: 'WORLDWIDE' / 'WHISKY' / 'MAKERS'. Spezia Semi-Mono 12px, uppercase, #232323, letter-spacing 0.167em, 1px #232323 underline beneath each word. No color change on hover, no background - the underline is the entire interactive affordance.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
