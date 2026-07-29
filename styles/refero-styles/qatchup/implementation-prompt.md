# AI Implementation Prompt

Build a Qatchup-inspired interface using this source-derived style bundle.

Reference site: https://www.qatchup.com
Theme: light
Category: SaaS
North star: Ink on warm paper, whispered quietly.

Use these palette anchors:

- Charcoal `#080808` for Primary headings, high-emphasis text - the deepest ink against the warm white canvas, anchoring headlines at maximum contrast
- Graphite `#222222` for Body text, icon strokes, secondary headings - slightly lighter than Charcoal for body density where pure black feels too heavy
- Mid Ink `#292929` for Filled button background, dark UI surfaces, strong border emphasis - the primary action surface; charcoal-darker than body text for weight contrast against pills
- Steel `#696969` for Default border color, card edges, icon strokes at rest - the structural hairline that carries the entire layout; appears in 260 borderColor uses, making it the most-used stroke in the system
- Fog `#999999` for Muted secondary borders, low-emphasis dividers - a lighter hairline for de-emphasized structure
- Ash `#b2b2b2` for Card inner borders, subtle dividers inside containers - softer than Steel for nested elements
- Slate `#8d8d8d` for Disabled or inactive border state, decorative dividers - sits between Steel and Fog for tertiary structural lines
- Mist `#cccccc` for Subtle shadow contribution, light card shadow base - a desaturated mid-gray for soft elevation
- Silk `#e4e4e7` for Image borders, body content dividers, light surface separators - the lightest visible structural line, near-white with just enough definition
- Bone `#fafafa` for Page canvas, card surfaces, link border, light text on dark - the warm white foundation; every other neutral reads against this base
- Cream `#f4f4f5` for Secondary button fill, elevated surface tone, subtle hover state - one step warmer/lighter than Bone for nested surfaces

Use these typography anchors:

- Aspekta `--font-aspekta` for All UI text - headlines at 40-56px use weight 400 with aggressive negative tracking (-0.035em to -0.020em) to create a condensed, modern feel; body text at 16-18px uses weight 400 with lighter tracking (-0.011em to -0.010em); weight 500 reserved for button labels and emphasis. The tight letter-spacing at display sizes is signature - it pulls letters together so headlines read as confident blocks rather than airy sentences.
- Fasthand `--font-fasthand` for Handwritten accent for emotional kickers and signatures - the 'Listen!' above the hero headline, the 'Open Letter' section intro. One weight, one size, used at most once per section. This is the human voice in an otherwise architectural system; it appears only where the brand needs warmth over precision.
- Aspekta 500 `--font-aspekta-500` for Aspekta 500 - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 24-32px.
- Element gap: 10-16px.

Build these component patterns where relevant:

- Dark Pill Button: Primary action control
- Light Pill Button: Secondary action control
- Floating Content Card: Content panel - feedback widget, feature block
- Modal/Card with Deep Elevation: Elevated overlay or popover
- Rounded Image Frame: Image container
- Navigation Bar: Top-level page navigation
- Centered Hero Block: First-screen hero pattern
- Two-Column Letter Layout: Long-form narrative sections
- Feedback Option Row: Selectable item in the feedback widget
- Grid Background Pattern: Subtle page texture
- Wordmark Lockup: Brand identity in header/footer
- Illustrative Crowd Border: Decorative full-bleed illustration

Do:

- Use 100px or 999px radius for all interactive elements - pill buttons and fully rounded tags only
- Set Aspekta at 48-56px with -0.030em to -0.035em letter-spacing for all display headlines
- Use #696969 (Steel) as the default border color for cards, dividers, and structural lines
- Layer shadows with a hairline ring (0px 0px 0px 1px) first, then soft drop shadows - never use a single hard shadow
- Reserve Fasthand for at most one emotional kicker per section - the 'Listen!' or 'Open Letter' moment
- Keep all UI elements in the neutral palette; color appears only in decorative illustration
- Maintain 80-120px vertical rhythm between sections - the whitespace is part of the brand

Avoid:

- Don't introduce a chromatic accent color for buttons, links, or text - the system has none
- Don't use square or 4-8px radius on cards - the 32px radius is structural to the brand
- Don't apply the decorative rainbow illustration style to icons, controls, or functional graphics
- Don't use Aspekta weight 500 for body text - reserve it for button labels and single-word emphasis
- Don't add background colors to sections - the system relies on whitespace and the warm-white canvas for separation
- Don't use gradients on UI elements - the system is flat and matte, elevation comes from shadow only
- Don't set letter-spacing to 0 or positive values on display sizes - the tight tracking is signature

Source prompt cues:

**Quick Color Reference**
- text (primary): #080808
- text (body): #222222
- text (muted): #696969
- background: #fafafa
- border: #696969
- primary action: #292929 (filled action)

**Example Component Prompts**
1. Create a primary CTA button: 100px border-radius, #292929 background, #fafafa text, Aspekta weight 500 at 16px, padding 11px vertical / 22px horizontal. No border.

2. Create a content card: #fafafa background, 32px border-radius, padding 28px, shadow stack of hairline ring + soft multi-layer drop (rgba(19,19,22,0.05) 0px 0px 0px 1px + rgba(0,0,0,0.04) 0px 2px 3px 0px + rgba(34,42,53,0.04) 0px 4px 6px 0px). No visible border - shadow defines the edge.

3. Create a hero headline: centered on #fafafa canvas. Fasthand accent at 32px in #696969 ('Listen!'). Then Aspekta 400 at 48px, #080808, letter-spacing -1.44px, 2 lines. Body subtext at 16px Aspekta 400, #696969, max-width 480px centered.

4. Create a two-column letter section: left column at 40% width with Aspekta 40px heading at #080808 (letter-spacing -0.8px). Right column at 55% width with Aspekta 18px body at #696969, line-height 1.56. 48px gap between columns.

5. Create a feedback option row: 24px icon (outlined, #292929 stroke) + Aspekta 500 at 16px title (#080808) + Aspekta 400 at 14px description (#696969). Horizontal layout, 12px padding vertical, 16px gap between icon and text.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
