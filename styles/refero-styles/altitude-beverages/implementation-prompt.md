# AI Implementation Prompt

Build a Altitude Beverages-inspired interface using this source-derived style bundle.

Reference site: https://altitudebev.com
Theme: mixed
Category: E-commerce
North star: Monochrome editorial spread. Imagine a fashion magazine spread stripped of all color except the product photography - the type and whitespace do all the storytelling.

Use these palette anchors:

- Canvas White `#fafafa` for Page background, card surfaces, primary canvas - the dominant near-white that lets photography and type carry all visual weight
- Warm Ash `#d9d9d9` for Elevated surface backgrounds for cards, buttons, and nav pill container - a warm gray one step darker than canvas for subtle layering without shadows
- Mid Gray `#cdcdce` for Hairline borders, link underlines, and divider lines - sits between canvas and text to create structure without weight
- Ink Black `#07060b` for Primary text, button labels, heading copy - a near-pure black with a faint blue undertone for maximum contrast against the warm canvas
- Pure Black `#000000` for Navigation borders and secondary text accents - used sparingly where a slightly harder edge is needed
- Glacial Mist `#ddfcff` for Faint cool-tinted accent on borders and fills - a barely-perceptible icy wash that adds micro-contrast without breaking the monochrome discipline

Use these typography anchors:

- HelveticaNowDisplay `--font-helveticanowdisplay` for Display and hero headlines - weight 800 at 160px with -0.05em tracking is the signature: massively compressed, ultra-bold statement type that dominates the viewport. Also used at 18px/500 for emphasized inline labels and 11px for caption-level brand marks
- EditorialNew `--font-editorialnew` for Editorial body and subheadings - the light-weight serif (weight 200) at 40-60px creates the 'fashion magazine pull-quote' feeling. The extreme thinness against the massive Helvetica display generates typographic tension. Also flows at 14-16px for editorial paragraph text
- DepartureMono `--font-departuremono` for Monospaced utility face for navigation labels, button text, form inputs, and small data - uppercase tracked monospace signals 'technical/informational' against the display serif and sans
- ui-sans-serif `--font-ui-sans-serif` for Fallback body text and generic UI copy - system sans at 16px handles the long tail of small interface labels that don't warrant the custom faces

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 36-80px.
- Card padding: 16-24px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Pill Navigation Bar: Primary site navigation
- Pill Text Button: Outlined/ghost action trigger
- Display Hero Headline: Primary page statement
- Editorial Subheadline: Supporting editorial text below display
- Product Feature Card: Large hero product showcase
- Floating Product Card: Compact product preview with details
- Dark Gradient Section: Full-bleed tonal reset between light sections
- Monospace Label Tag: Small category or metadata indicator
- Circular Icon Button: Standalone utility action (profile, account)
- Hairline Divider: Structural separation between elements

Do:

- Use HelveticaNowDisplay weight 800 at 160px for the primary hero headline - it must feel oversized and compressed, never comfortable or safe
- Pair the ultra-bold display with EditorialNew weight 200 for subheadings - the 200-vs-800 contrast is the typographic identity
- Keep all UI chrome to the monochrome palette (#fafafa, #d9d9d9, #07060b, #cdcdce) - color belongs only in product photography
- Use 100px border-radius for navigation pills and primary buttons; 44px for product cards and content containers
- Set all navigation, button labels, and metadata in DepartureMono uppercase at 11-12px with -0.071em tracking
- Maintain a section gap of 36-80px between major content blocks to let the editorial whitespace breathe
- Let product photography be the only chromatic element - never introduce a brand accent color into UI components

Avoid:

- Do not add shadows to any component - use surface color steps (#fafafa #d9d9d9) and gradient transitions for all depth
- Do not use rounded corners below 44px for cards or 100px for buttons - the system is defined by its pill/lozenge geometry
- Do not set body text in HelveticaNowDisplay - reserve that face for display headlines at 60px+ only
- Do not use color for buttons, badges, or interactive elements - all actions are black text on warm gray or white surfaces
- Do not break the light/dark alternation with a chromatic section - the dark gradient is the only non-monochrome surface
- Do not use line-heights above 1.06 for headlines - the tight leading is part of the compressed, editorial feel
- Do not add icons or illustrations to the UI - the system relies on photography, monogram marks, and pure typography

Source prompt cues:

Quick Color Reference:
- background: #fafafa
- surface (cards, nav pill, buttons): #d9d9d9
- border (hairlines, dividers): #cdcdce
- text: #07060b
- accent (micro-contrast only): #ddfcff
- primary action: no distinct CTA color

Example Component Prompts:
1. Create a hero section: #fafafa background. Headline 'Low-Key Sophisticated Rosemary Spritz' at 160px HelveticaNowDisplay weight 800, #07060b, letter-spacing -0.05em, line-height 0.90. Subtext 'Non-Alcoholic Pairings for Perfect Vibes' at 18px EditorialNew weight 200, #07060b. Below, a pill text button with #fafafa fill, 1px #cdcdce border, 100px radius, 16px 20px padding, label 'SHOP' in DepartureMono 12px uppercase #07060b.
2. Create a product feature card: 44px border-radius, full-bleed warm orange product photograph of a beverage can. In the bottom-right corner, overlap a 44px-radius secondary card with #d9d9d9 background, 16px padding, containing a small product image, product name in EditorialNew 16px #07060b, and a DepartureMono 11px uppercase label 'Herbal | Bittersweet | Refreshing' in #07060b.
3. Create the pill navigation: a 100px-radius floating container with #d9d9d9 background, horizontally centered at the top of the page. Inside, four monospace links - 'SHOP', 'ABOUT', 'FIND US', 'CART (0)' - in DepartureMono 12px uppercase #07060b with 24px horizontal padding each. To the top-left, the wordmark 'altitude' in HelveticaNowDisplay 18px weight 500 #07060b. To the top-right, a 40px circular icon button with #d9d9d9 background containing a small 'A' monogram in HelveticaNowDisplay 11px weight 800.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
