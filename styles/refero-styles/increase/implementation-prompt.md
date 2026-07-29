# AI Implementation Prompt

Build a Increase-inspired interface using this source-derived style bundle.

Reference site: https://increase.com
Theme: light
Category: Fintech
North star: institutional blueprint on vellum - one electric chartreuse stripe cuts the navy calm, mint data signals pulse beneath it.

Use these palette anchors:

- Inkwell Navy `#1a2b3b` for Primary text, nav text, icon strokes, hairline borders - the structural graphite of every screen. Used as filled button background for primary actions to project institutional weight rather than enthusiasm
- Slate 600 `#314352` for Secondary borders and supporting text where Inkwell Navy is too heavy - outlines on cards, tertiary headings, subdued dividers
- Abyss `#0d1726` for Dark code-block and terminal surfaces - deeper than Inkwell Navy so syntax highlighting reads with high voltage against the near-black
- Graphite `#687887` for Muted helper text, inactive nav links, secondary button outlines - recedes so the navy headlines and mint accents can carry the hierarchy
- Steel `#8995a1` for Tertiary text and disabled-state borders - the quietest navy in the scale, used where information is supplementary
- Fog `#edf0f2` for Page canvas - the warm off-white that holds all content; section bands alternate with pure white to create quiet vertical rhythm
- Pure White `#ffffff` for Card surfaces, form inputs, nav background - the elevated layer that floats above Fog with minimal shadow
- Silver `#caced2` for Hairline dividers, input borders at rest, table separators - the thread that separates without announcing itself
- Mist `#e1e5e9` for Card edges and subtle surface tints where a second neutral step is needed between white and Fog
- Pewter `#bdc2c8` for Body-level borders, subtle rule lines, the quietest non-white neutral
- Voltage `#e4ff33` for Announcement bar, high-attention data highlights, occasional feature accent - the single chromatic punctuation that earns the eye's attention by being used sparingly. Never decorates, always signals
- Mint Signal `#31f2bf` for Green outline accent for tags, dividers, and focused UI edges

Use these typography anchors:

- Untitled Sans `--font-untitled-sans` for Primary interface and display typeface - custom geometric grotesque. Weight 400 runs the body and UI; weight 500 lifts subheadings; weight 700 anchors the wordmark. Negative letter-spacing (-0.04em at display sizes, -0.01em at body) tightens the grotesque into a dense, architectural feel - the closer the eye gets to a heading, the more the letters close ranks, producing a precise, financial-document quality.
- Input Mono `--font-input-mono` for Code, API identifiers, numerical data, and inline technical labels. Alternates and stylistic sets ss01/ss02/ss12 are active - these micro-detailed glyph variants give the monospace a humanist, designed quality rather than a default-terminal feel, reinforcing that the product is engineered with intention.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20-24px.
- Element gap: 8-12px.

Build these component patterns where relevant:

- Announcement Bar: Full-bleed top-of-page strip for time-bound news, awards, and feature launches.
- Top Navigation: Primary header carrying brand, product taxonomy, account actions.
- Primary Filled Button: The default action affordance - sign-up, create, submit.
- Ghost / Outlined Button: Secondary actions - 'Contact sales', 'Sign in', 'Learn more'.
- Hero Headline: Page-opening display line establishing product category.
- Hero Subtext: Supporting paragraph under the headline.
- Code Block Card: Live API demonstration embedded in hero and feature sections.
- Product Feature Card: Feature highlight in a 4-column grid (ACH, Cards, Bank accounts, Wires, etc.).
- Icon Badge: Reusable icon container for feature cards and inline labels.
- Trust Logo Bar: Social proof band beneath the hero.
- Gradient Accent Visual: Decorative hero backdrop and feature-section color washes.
- Form Input: Text input in the hero demo card ('Send an ACH transfer').

Do:

- Use Inkwell Navy (#1a2b3b) as the only filled-button background - never a chromatic fill for a primary action.
- Set display type at 90px with -5.4px letter-spacing to preserve the dense, financial-document quality of headlines.
- Apply the Voltage (#e4ff33) announcement-bar color only on full-bleed strips or single token highlights - never on cards, buttons, or text.
- Use 12px radius for cards and 8px radius for buttons, inputs, and nav; reserve 999px exclusively for pill tags.
- Pair Untitled Sans for prose and UI with Input Mono (with ss01/ss02/ss12 active) for all code, numbers, and API identifiers.
- Let cards float on Fog (#edf0f2) canvas with the navy-tinted three-layer shadow stack rather than hard borders.
- Render the four-step gradient (chartreuse mint cyan blue) only as angular geometric blocks behind hero copy - never as soft glows or button backgrounds.

Avoid:

- Don't use Mint Signal (#31f2bf) or Voltage (#e4ff33) as a primary button fill - they are signal colors, not action colors.
- Don't add a second saturated accent - the system runs on navy + chartreuse + mint only; introducing a fourth chromatic breaks the institutional register.
- Don't use straight #000000 for text on white surfaces - Inkwell Navy reads as authoritative while pure black reads as unfinished.
- Don't soften the hero gradients with blur or rounded edges - the angular, faceted geometry is what makes them read as financial infrastructure rather than marketing artwork.
- Don't use letter-spacing greater than -0.01em at body sizes - the negative tracking is what makes Untitled Sans feel architectural; loosening it dissolves the brand.
- Don't promote the code-syntax blue (#33bbff) into the UI palette - it exists only inside the code-block context.
- Don't add a dark mode variant without rebuilding the canvas as a warmer near-black (#0d1726-family) - the cool gray-navy scale does not invert cleanly to a black scale.

Source prompt cues:

**Quick Color Reference**
- text: #1a2b3b (Inkwell Navy)
- background: #edf0f2 (Fog canvas), #ffffff (cards)
- border: #caced2 (Silver hairline), #1a2b3b (Inkwell structural)
- accent: #31f2bf (Mint Signal) for icons/data flow
- voltage: #e4ff33 (announcement bar only)
- primary action: #1a2b3b (filled action)

**3 Example Component Prompts**

1. *Build the hero block*: 1200px max-width container on Fog (#edf0f2) canvas. Left column: 90px Untitled Sans weight 500 headline in Inkwell Navy (#1a2b3b) with -5.4px letter-spacing, line-height 1.0. Below: 20px weight 400 Graphite (#687887) subtext at line-height 1.4, max-width 540px. Two buttons side by side with 12px gap: a filled Inkwell Navy button (8px radius, 10px 20px padding, white text, trailing chevron) and a ghost button (transparent, 1px Inkwell Navy border, 8px radius, same padding). Right column: dark code card (Abyss #0d1726, 12px radius, 24px padding) stacked behind a white form card (12px radius, Mist #e1e5e9 1px border, subtle tinted shadow), with a floating angular gradient block (chartreuse-to-blue linear gradient) behind both.

2. *Build a product feature card*: White (#ffffff) background, 12px radius, 1px Mist (#e1e5e9) border, 20px padding, navy-tinted three-layer shadow. Top-left: 48x48px mint icon badge - 8px radius, near-white mint fill, Mint Signal (#31f2bf) 1.5px stroke icon centered. Below: 16px weight 500 Inkwell Navy title, 8px gap, 13px Graphite (#687887) description, max two lines. 4-column grid, 24px gap between cards.

3. *Build the announcement bar*: Full-bleed Voltage (#e4ff33) background strip, 4px vertical padding, centered Inkwell Navy (#1a2b3b) text at 14px weight 500 with -0.14px letter-spacing, trailing inline chevron. No border, no shadow, no radius - the bar must read as a flat, urgent message.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
