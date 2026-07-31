# AI Implementation Prompt

Build a ONE-inspired interface using this source-derived style bundle.

Reference site: https://one-is.com
Theme: light
Category: Agency
North star: art monograph on warm paper

Use these palette anchors:

- Ink `#000000` for Primary text, hairline borders, video frame outlines, pill button stroke - the only chromatic event in the UI
- Paper `#fbfbfa` for Soft icon strokes, subtle dividers, and low-emphasis decorative details. Do not promote it to the primary CTA color
- Ash `#bec0c5` for Muted text in the cycling manifesto, list dividers, inactive link tone - desaturated gray stays quiet next to ink

Use these typography anchors:

- MagicUiPro `--font-magicuipro` for Single-family system: body text and micro-headlines both sit in the 18-24px range at medium weight, with weight 600 reserved for the active manifesto item and button labels. The tight -0.01em tracking and modest size range mean type never breaks 24px - the page treats every word as a label, not a headline.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: 32px.
- Element gap: 16px.

Build these component patterns where relevant:

- Ghost Pill Button: Primary navigation CTA (Contact)
- Wordmark: Brand identity, top-left anchor
- Cinematic Video Plate: Primary content surface
- Caption Block: Annotation under video plates
- Cycling Manifesto List: Repetitive, rhythmic brand expression
- Project Thumbnail: Companion still alongside the manifesto
- Top Navigation Bar: Persistent page chrome
- Centered Play Control: Video interaction state

Do:

- Use only #000000 for text, borders, and outline strokes; #fbfbfa for any filled surface; #bec0c5 only for muted/secondary text and list dividers
- Set every button radius to 999px and every card/video frame radius to 12px
- Restrict type to 18px, 20px, and 24px at weight 500 or 600 with -0.01em letter-spacing
- Give video plates and section breaks at least 96px vertical breathing room
- Let the wordmark and Ghost Pill Button sit at the page edges with no centered nav or breadcrumbs
- Carry dark video content inside a 12px-radius frame rather than bleeding full-bleed against the Paper canvas
- Treat the manifesto list as a single column with weight/color as the only state indicator - no checkmarks, arrows, or icons

Avoid:

- Do not introduce accent colors, brand hues, or saturated fills - the palette is strictly ink/paper/ash
- Do not add box-shadows, gradients, or background blurs to any surface
- Do not scale type above 24px or below 18px - both would break the label-scale system
- Do not use weight 400 or 700; the system is bound to 500 and 600 only
- Do not use square or 4px radii on buttons; pill is the only allowed control shape
- Do not add a filled/solid button variant; the Ghost Pill Button is the sole interactive pattern
- Do not add icons, badges, or secondary navigation in the header - the chrome is exactly two elements

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
