# AI Implementation Prompt

Build a Fey-inspired interface using this source-derived style bundle.

Reference site: https://feyapp.com
Theme: light
Category: Fintech
North star: a printed broadsheet on warm paper - type and silence, nothing else.

Use these palette anchors:

- Warm Paper `#fafafa` for Page background - the only surface; everything floats on this warm off-white
- Graphite `#595959` for Body text, nav labels, footer copy - medium-dark gray keeps long-form reading comfortable without high-contrast harshness
- Ink `#1c1c1c` for Secondary body text, navigation labels, and subdued headings.

Use these typography anchors:

- -apple-system `--font-apple-system` for Body and navigation. At 21px / 600 / line-height 1.55 with -0.01em tracking, the system stack carries the entire page - the signature is the size and rhythm, not a custom face. 13px / 400 nav labels use the same -0.002em micro-tracking. A 16px / 400 utility size appears for small captions.
- Wealthsimple Sans Display `--font-wealthsimple-sans-display` for Reserved for the "Wealthsimple" link - a single display-grade cut at 21px / 700 / -0.01em. It signals partnership without changing the page's monochrome restraint.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 520px.
- Section gap: 48px.
- Card padding: 0px.
- Element gap: 8px.

Build these component patterns where relevant:

- Editorial Text Column: Main content container
- Inline Emphasis Word: Inline bold highlight within a paragraph
- Inline Text Link: The single navigational link in the body
- Signature Hand-Off Glyphs: Closing illustration

Do:

- Set body copy at 21px / weight 600 / line-height 1.55 with -0.01em tracking - this IS the brand voice.
- Use exactly two text colors: #595959 for narrative and #1c1c1c for emphasis and links. Nothing else.
- Constrain content to a ~520px centered column; let white space do the layout work.
- Separate paragraphs with ~29px margin-bottom for editorial rhythm.
- Keep the page to a single surface color (#fafafa) - no cards, no panels, no shadows.

Avoid:

- Do not introduce accent colors, buttons, or CTAs - this page is a declaration, not an action.
- Do not add headings (h1/h2/h3) - the 21px body carries the hierarchy through weight and color alone.
- Do not use shadows, borders, or background fills on text containers.
- Do not break the 520px column with sidebars, images, or multi-column layouts.
- Do not use a display or serif font for body copy - the system stack at 21px / 600 is the intended voice.
- Do not add hover states beyond color/weight transitions on links; no transform, scale, or shadow effects.

Source prompt cues:

Quick Color Reference:
- text: #595959 (body) / #1c1c1c (emphasis + links)
- background: #fafafa
- border: none
- accent: none
- primary action: no distinct CTA color

Example Component Prompts:
1. "Create an editorial announcement page: full-bleed #fafafa background, a single centered column at 520px max-width. Body paragraphs at 21px, -apple-system, weight 600, line-height 1.55, letter-spacing -0.01em, color #595959. Paragraphs separated by 29px margin-bottom. No headings, no cards, no buttons."
2. "Add inline emphasis: render 'Fey joined' at the same 21px / 600 / -0.01em, but in color #1c1c1c instead of #595959. No underline, no background - color and weight carry the contrast."
3. "Create the single text link: 'Wealthsimple' at 21px / 600 / -0.01em, color #1c1c1c, optionally in Wealthsimple Sans Display weight 700. No default underline; let color signal interactivity."
4. "Add the left-edge nav indicator: five thin horizontal lines at the page's left margin (40px from viewport edge), 8px row-gap between lines, in #595959. Vertically centered against the text column."
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
