# AI Implementation Prompt

Build a Visual-inspired interface using this source-derived style bundle.

Reference site: https://designstripe.com
Theme: light
Category: AI
North star: Warm editorial zine. Cream paper, serif posters, mono marginalia, a single yellow highlighter mark.

Use these palette anchors:

- Vellum `#f6f6f4` for Page background the warm off-white that defines the entire canvas tone
- Paper `#ffffff` for Card surfaces, elevated panels, product mockup backgrounds
- Ink `#000000` for Primary text, heavy structural borders, nav bar outlines
- Carbon `#2c2c26` for Warm near-black for dark panels, footer background, and neutral filled button fill the only filled button in the system
- Ash `#d0d0c8` for Light hairline borders, card outlines, subtle dividers
- Olive Char `#57584b` for Mid-dark structural borders, heavier dividers between sections
- Lichen `#6d6e5e` for Body text, secondary borders, muted paragraph copy
- Sage `#979886` for Nav link text, muted UI labels, breadcrumb text

Use these typography anchors:

- Serif (custom resembles a high-contrast modern editorial serif like Reckless Neue, GT Sectra, or PP Editorial New) All display and heading copy. Used at poster sizes (6496px) for hero headlines and product section titles. The weight 300 at 96px is the signature move whisper-thin strokes at near-poster scale create authority through restraint, not volume. Tight tracking (-0.05em) at all sizes; line-heights under 1.1 let letterspacing do the vertical work `--font-serif-custom-resembles-a-high-contrast-modern-editorial-serif-like-reckless-neue-gt-sectra-or-pp-editorial-new`
- Mono (custom clean geometric monospace) All UI text: navigation, buttons, labels, body copy, metadata, footer links. The mono choice is deliberate it makes every UI element feel like terminal output or code annotation, contrasting the serif's editorial softness. Weight 400 dominates; 500 for button text; 300 reserved for large mono headings (2848px range) `--font-mono-custom-clean-geometric-monospace`

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Neutral Filled Button: Primary action trigger (Waitlist, Join, Submit)
- Ghost Outline Button: Secondary action (Learn More, Read More)
- Section Eyebrow Label: Small all-caps category marker above headlines
- Centered Section Header: Primary headline block for each page section
- Feature Split Card: Side-by-side feature comparison blocks
- Dark Product Panel: Product UI showcase with dark background
- Blog Card: Article preview in blog grid

Do:

- Use the serif at 6496px weight 300 for all hero and section headlines the thin strokes at poster scale are the signature
- Set page background to #f6f6f4 and card surfaces to #ffffff the warm cream is non-negotiable, never use pure #ffffff as the page canvas
- Pair the neutral filled button (#2c2c26 fill, #ffffff text) with the ghost outline button (1px #000000 border) they always appear as a 2-button cluster with 8px gap
- Use mono at 1216px with tracking -0.067em for all UI text, nav, buttons, and body copy this creates the terminal/code-margin feel
- Separate sections with 80px vertical gaps, not with borders or background color shifts the whitespace is the structure
- Place the #fff347 accent as 24px strokes or small fill blocks (max ~120px wide), never as large fills or backgrounds
- Use 8px radius on cards and 3px radius on buttons, tags, and nav elements the radius contrast is deliberate

Avoid:

- Don't use pure #ffffff as the page background always #f6f6f4 for the warm cream canvas
- Don't add drop shadows to cards or buttons the system is intentionally flat, separation comes from 1px borders and color contrast
- Don't use the serif at body sizes (16px or below) it is a display-only face; body copy must be mono
- Don't apply #fff347 to text, large backgrounds, or filled buttons it is a decorative accent only, not an action color
- Don't use cool grays (blues or true neutrals) the entire palette runs warm: olive-sage tones, warm blacks (#2c2c26 not #000000 for surfaces), and cream whites
- Don't use gradients the system is flat color only, with the one exception of the 3D hero render which contains its own internal gradients
- Don't exceed 4 instances of #fff347 per screen the accent loses impact if it appears more than 34 times on a single page

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
