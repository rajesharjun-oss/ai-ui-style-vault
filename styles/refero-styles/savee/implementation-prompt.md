# AI Implementation Prompt

Build a Savee-inspired interface using this source-derived style bundle.

Reference site: https://savee.it
Theme: dark
Category: Design
North star: Black canvas for visual curators

Use these palette anchors:

- Electric Indigo `#1500ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Obsidian `#050505` for Page canvas, deepest background - the void that all content sits on
- Charcoal `#151515` for Elevated surface, product preview frames, secondary panels
- Graphite `#1e1e1e` for Deeper overlay surface, hover states on dark cards, input fields
- Paper `#fdfdfd` for Primary text, inverted surface, button text, high-contrast foreground
- Silver `#e5e5e5` for Hairline borders, dividers, subtle structural edges
- Pearl `#d4d4d4` for Secondary text, subdued headings, placeholder body copy
- Slate `#2f2f2f` for Footer borders, low-contrast dividers between dark zones
- Ash `#a3a3a3` for Muted helper text, inactive icons, de-emphasized metadata
- Stone `#737373` for Tertiary text, timestamps, supplementary labels

Use these typography anchors:

- Savee Font `--font-savee-font` for The sole typeface - a custom geometric sans used at every scale. Weight 400 carries the editorial body and nav; weight 500 appears on buttons and emphasized labels. The 96px display at 0.96 line-height with -0.04em tracking is the system's signature: it compresses into a dense confident block rather than stretching vertically, making the headline feel sculptural.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary Pill Button: The sole filled action in the system
- Ghost Pill Button: Secondary action that doesn't compete with the primary
- Navigation Bar: Minimal top-level site navigation
- Display Headline: Hero-level typography that defines the page
- Editorial Body Block: Long-form persuasive text at unusual scale
- Partner Logo Strip: Social proof band
- Product Preview Frame: Large product screenshot or video container below the hero
- Text Link: Inline navigation within body copy
- Subhead Caption: Descriptive subtext under headlines
- Full-Width Section Spacer: Vertical rhythm between page sections
- Footer Divider: Low-contrast structural edge

Do:

- Use #1500ff Electric Indigo exclusively for the single primary CTA on any given screen - never for secondary actions, links, icons, or decorative elements
- Set display headlines at 96px with line-height 0.96 and letter-spacing -0.04em so the type compresses into a confident sculptural block rather than stretching
- Apply 9999px border-radius to every button, tag, and pill - the pill shape is the system's only control geometry
- Use 14px radius for card and product preview surfaces, and nothing else - keep the shape vocabulary to exactly two radii
- Let the Obsidian canvas (#050505) be the separator between sections - add 64-80px of empty space rather than lines, color shifts, or gradient transitions
- Set body prose at 36px when it needs to carry editorial weight; drop to 18px for functional descriptions. Never use 14-16px for primary page copy
- Keep all text in the neutral palette (#fdfdfd, #d4d4d4, #a3a3a3) - the only chromatic color is the CTA indigo

Avoid:

- Never use #1500ff for anything other than the primary CTA fill - not for links, not for icons, not for hover states, not for badges
- Never add drop shadows or elevation glows to cards - the system uses surface color shifts (#050505 #151515 #1e1e1e) for hierarchy, not shadows
- Never set body text below 16px for primary content - captions and metadata can go to 13-14px, but main copy stays large
- Never introduce additional accent colors, even in illustrations or partner logos - the partner strip stays grayscale to preserve the indigo's dominance
- Never use border-radius values between 0px and 9999px for buttons - the system is binary: fully rounded pills or 14px card corners, nothing in between
- Never apply gradients to backgrounds, buttons, or text - the system is flat monochrome with one solid color exception
- Never use line-height above 1.50 for any text size - the tight line-heights (0.96-1.38) are the system's editorial signature

Source prompt cues:

**Quick Color Reference**
- text: #fdfdfd
- background: #050505
- border: #e5e5e5
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
- primary action: no distinct CTA color

**Example Component Prompts**


2. Create an editorial body section: #050505 background. Left-aligned prose at 36px Savee Font weight 400, #fdfdfd, line-height 1.13, letter-spacing -0.36px. Max-width 800px. No drop shadows, no card backgrounds - text sits directly on the void.

3. Create a product preview frame: #151515 background, 14px border-radius, full content width (max 1200px), no border, no shadow. Suggests a dark app interface screenshot.


5. Create a partner logo strip: single horizontal row of 8 grayscale logos in #a3a3a3, evenly spaced across full content width. Preceded by a caption at 13px #737373 reading 'Used by leading design studios and teams'. No colored logos, no hover effects.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
