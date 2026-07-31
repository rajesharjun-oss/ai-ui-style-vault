# AI Implementation Prompt

Build a Freytag Anderson-inspired interface using this source-derived style bundle.

Reference site: https://www.freytaganderson.com
Theme: mixed
Category: Agency
North star: cinema curtain rising on a single word.

Use these palette anchors:

- Paper `#fafafa` for Page canvas, base surface behind text - off-white, never pure white, to soften photographic edges
- Ink `#000000` for Primary text, hairline borders, link underlines - the only chromatic accent in the system is its absence of color
- Charcoal `#1c1c1c` for Dark content surface for text-only sections - warm-leaning black that softens contrast against pure ink
- Midnight Soil `#141109` for Deepest dark surface, used for the most recessed bands - barely distinguishable from charcoal but warmer
- Ash `#dcdcdc` for Hairline borders, disabled borders, subtle dividers - a neutral gray that whispers structure without drawing the eye
- Driftwood `#c2b5ae` for Warm taupe accent surface, used sparingly as a tonal break in dark sections - the only non-achromatic hint in the palette

Use these typography anchors:

- FAVORIT `--font-favorit` for The single typeface for everything: hero titles at 41px weight 400, body at 17px weight 400, captions at 15px weight 300. Weight 300 is the signature choice for secondary text - it creates hierarchy through restraint rather than bold contrast. Slight negative tracking (-0.02em to -0.022em) tightens the grotesque's default rhythm. The same family voices headlines, navigation, buttons, and body, which is unusual - most systems differentiate roles through typefaces. Here, FAVORIT's dual weight and tight letterforms carry the entire hierarchy alone.
- Clarkson `--font-clarkson` for Reserved for micro-copy or supporting text in specific contexts - appears at low frequency and never headlines. Could be a FAVORIT alternate cut rather than a true second family.
- halyard-display `--font-halyard-display` for Rare accent - appears in button or micro-label contexts. Functions as a display-only voice when FAVORIT needs to step aside.

Use these layout rules:

- Base spacing: 6px.
- Density: spacious.
- Page max-width: .
- Section gap: .
- Card padding: 43px.
- Element gap: 17px.

Build these component patterns where relevant:

- Ghost Pill Button: Primary interactive control
- Outlined Pill Button (Light): Secondary action on dark/photographic backgrounds
- Hamburger Menu: Sole navigation control
- Hero Title: Opening statement over cinematic media
- Section Statement: Large declarative text introducing a content block
- Three-Column Body Block: Detailed descriptive text in a constrained grid
- Photographic Hero: Primary content surface - not a component but a structural device
- Dark Content Section: Text-only section with photographic weight
- Image Grid Item (implied): Project thumbnail in portfolio contexts

Do:

- Keep the palette to six neutrals - never introduce a chromatic accent color; the design's power comes from restraint.
- Anchor all text to the top-left viewport corner on full-bleed media; centering or middle-alignment breaks the title-card logic.
- Use FAVORIT exclusively for UI and body - do not import secondary typefaces for hierarchy; let weight (300 vs 400) and size do the work.
- Set body line-height to 1.7 - generous leading is part of the system's quiet, slow-reading rhythm.
- Use 288px bottom padding between major sections to create the cinematic breath between acts.
- Let photographs and video fill the viewport edge-to-edge with no border, radius, or overlay chrome.
- Use pill geometry (border-radius: 300px) for every button - there is no square or slightly-rounded button in this system.

Avoid:

- Do not add a chromatic accent color (blue, red, green) - the system is deliberately achromatic and a single hue would shatter the cinema metaphor.
- Do not add card shadows, drop shadows, or elevation tokens - the design is flat, relying on color contrast and whitespace for separation.
- Do not center text horizontally - the top-left anchor is the system's defining gesture.
- Do not add a traditional navigation bar with visible menu items - the hamburger is the only nav surface.
- Do not use multiple typefaces to create hierarchy - FAVORIT is the only voice, period.
- Do not frame or round images - photographs are presented raw, full-bleed, unbordered.
- Do not use bold (600+) weights - the system speaks at 300 and 400 only; heavier weights would break the whispered tone.

Source prompt cues:

Quick Color Reference:
- text: #000000 (primary), #fafafa (on dark/photo)
- background: #fafafa (default), #1c1c1c (dark section), #141109 (deepest)
- border: #000000 (default), #fafafa (on dark), #dcdcdc (subtle divider)
- accent: none (achromatic only)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a full-bleed hero section: viewport-filling photographic or video background, no overlay. Headline at 41px FAVORIT weight 400, #fafafa, letter-spacing -0.9px, line-height 1.18. Text anchored to the top-left viewport corner with 24px padding. Hamburger menu icon (two 1px lines) in #fafafa, top-right corner.

2. Create a dark intertitle section: solid #1c1c1c background, no texture. Section statement at 41px FAVORIT weight 400, #fafafa, letter-spacing -0.9px, anchored top-left. Below at 120px gap, a three-column grid of body text at 17px FAVORIT weight 400, #fafafa, line-height 1.7, letter-spacing -0.34px. 288px padding-bottom before the next section.

3. Create a ghost pill button: border-radius 300px, 1px solid #000000 border, transparent background, padding 12px vertical 20px horizontal. Label at 15px FAVORIT weight 400, #000000, letter-spacing -0.3px. On dark backgrounds, swap border and text to #fafafa.

4. Create a body text block: 17px FAVORIT weight 400, #fafafa on #1c1c1c surface, line-height 1.7, letter-spacing -0.34px. Paragraph spacing 17px. No column dividers - the grid is implied through alignment alone.

5. Create a section transition: 288px of empty space between the previous section and the next, functioning as a cinematic intermission. No dividers, no spacers, no visual markers.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
