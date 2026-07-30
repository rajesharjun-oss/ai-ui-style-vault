# AI Implementation Prompt

Build a Sing-sing-inspired interface using this source-derived style bundle.

Reference site: https://sing-sing.co
Theme: light
Category: Agency
North star: butter-paper broadsheet at golden hour - a warm saffron canvas with sea-glass ink.

Use these palette anchors:

- Marigold `#fcd579` for Page canvas, full-bleed backgrounds, the base layer every other element sits on
- Sea Glass `#81d6b9` for Decorative stroke accent - horizontal stripe pattern, top page divider, wordmark underline, gradient terminus
- Inkstone `#171717` for Primary text, nav labels, headings, logo wordmark, and all interface borders
- Marigold Gradient `#81d6b9` for Right terminus of the signature horizontal gradient (teal warm gold) used for stripe fades and section dividers

Use these typography anchors:

- untitledsans `--font-untitledsans` for Primary typeface across all contexts - body copy, nav, footer, links, and the colossal display wordmark. The 147px size at tight tracking (-0.025em) is the identity: the word 'Sing' becomes a spatial event, not a heading. Weight 400 carries body and nav; weight 700 anchors headings and footer emphasis. Kern feature is active throughout to manage the extreme size range.
- signifier `--font-signifier` for Secondary editorial typeface - used for rotated/vertical captions beside photography and occasional body annotations. Its serif presence contrasts the grotesk wordmark to introduce a magazine-like voice. Normal letter-spacing; the small size keeps it as whisper copy, never a headline.

Use these layout rules:

- Base spacing: 6px.
- Density: compact.
- Page max-width: .
- Section gap: 35px.
- Card padding: 0px.
- Element gap: 5-7px.

Build these component patterns where relevant:

- Striped Header Band: Signature top-of-page element
- Index Label: Top-right navigation indicator
- Display Wordmark: Brand identity and section openers
- Editorial Image Block: Full-bleed photography placement
- Rotated Caption: Editorial annotation beside imagery
- Gradient Stripe Divider: Section separator and rhythm device
- Footer Wordmark: Page-bottom brand anchor

Do:

- Use #fcd579 as the only page background - never introduce white or gray canvases
- Let display type reach 147px with -0.025em tracking; restraint at small sizes is the contrast that makes the scale work
- Place teal (#81d6b9) only as thin horizontal lines, single underlines, and gradient strokes - never as fills or blocks
- Use the teal-to-yellow linear-gradient(90deg, #81d6b9 40%, #efcb75 100%) for any divider that needs to feel structural
- Keep all radii at 0px - sharp edges are part of the editorial language
- Let photography fill its container edge-to-edge with raw crops, no rounding or masking
- Activate "kern" on all untitledsans and signifier text to handle the extreme type range

Avoid:

- Do not introduce shadows, cards, or elevated surfaces - the system is flat by design
- Do not add white, gray, or off-white backgrounds; marigold is the only canvas
- Do not use teal (#81d6b9) as a button fill or large color block - it is a line/stroke accent only
- Do not create rounded corners on any element; the aesthetic is architectural and sharp
- Do not use multiple accent colors; the system is two chromatic notes (teal + yellow) on black ink
- Do not add decorative borders, boxes, or containers around text or images
- Do not use a traditional grid card system - layout is art-directed, not modular

Source prompt cues:

**Quick Color Reference**
- text: #171717
- background: #fcd579 (marigold canvas - the only surface)
- border/accent: #81d6b9 (teal - stroke only, never fill)
- gradient: linear-gradient(90deg, #81d6b9 40%, #efcb75 100%)
- nav link: #171717 on #fcd579
- primary action: no distinct CTA color

**Example Component Prompts**
1. *Striped header band*: Full-bleed #fcd579 background. Overlay 1px #81d6b9 horizontal lines spaced 14px apart, occupying the top 300px of the viewport. 5px padding-top.

2. *Display wordmark with underline*: untitledsans weight 400, 147px, #171717, letter-spacing -0.025em, line-height 1.0. Below baseline, a 2px line using linear-gradient(90deg, #81d6b9 40%, #efcb75 100%) spanning full width.

3. *Editorial image block with rotated caption*: Full-width #fcd579 background. Left 60% holds a photograph with 0px radius, raw crop to edges, no border. Right 40% contains signifier 21px weight 400, #171717, rotated -90 , vertically centered in the gutter.

4. *Index nav link*: untitledsans 16px weight 400, #171717, positioned absolute top-right with 5px padding. Single word, no underline, no background. On #fcd579 canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
