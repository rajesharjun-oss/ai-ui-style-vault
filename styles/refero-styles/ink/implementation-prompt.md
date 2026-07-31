# AI Implementation Prompt

Build a INK-inspired interface using this source-derived style bundle.

Reference site: https://weareink.co.uk
Theme: light
Category: Agency
North star: Editorial spread on warm paper. A single humanist voice, monochrome with a whisper of taupe, interrupted only by full-bleed photography and a slim band of warm orange.

Use these palette anchors:

- Ink Carbon `#2e2a2b` for Primary text, logo mark, dark surface inversions, footer text on cream - a near-black with a barely-warm undertone that keeps the page from feeling clinical
- Paper White `#ffffff` for Page canvas and nav surface - the warm-white background that everything floats on
- Whisper Taupe `#afa697` for Supporting neutral for secondary UI, dividers, and muted labels.
- Bone Cream `#e6dcd4` for Alternate panel background and footer band - a warm cream that signals a quieter section without leaving the monochrome family
- Lampblack `#212121` for Deep surface for inversions and image overlays - slightly cooler than Ink Carbon, used where absolute darkness is needed without color cast
- Signal Orange `#fe5431` for Decorative illustration accent - appears inside graphic bands and artwork, never as a UI control fill
- Amber Pulse `#ff8000` for Decorative illustration accent - companion to Signal Orange inside warm gradient bands and visual punctuation

Use these typography anchors:

- Good Sans `--font-good-sans` for Single voice across the entire interface - body, nav, buttons, headings, and display all share weight 400. The absence of bold is the signature: hierarchy comes from size and color, not weight.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: .
- Section gap: 160px.
- Card padding: .
- Element gap: 16px.

Build these component patterns where relevant:

- Pill Nav Indicator: Primary navigation trigger
- Wordmark Logo: Brand identity mark
- Hero Statement Block: Opening page headline
- Full-Bleed Project Plate: Portfolio showcase frame
- Project Caption Row: Label and pagination beneath an image
- Decorative Warm Band: Section transition graphic
- Cream Footer Panel: Closing section surface

Do:

- Use Good Sans weight 400 at every size - never introduce bold or medium weights to create hierarchy
- Set section breaks to 160px of vertical whitespace; this is the system's most recognizable rhythm
- Let project images fill 100% viewport width with zero border-radius and zero frame
- Use Whisper Taupe #afa697 for secondary headlines and Ink Carbon #2e2a2b for primary statements in the same block
- Use 100px border-radius on the nav indicator dot - it must read as a perfect circle
- Keep left-edge text alignment with 64px padding from viewport edge on every section
- Use Bone Cream #e6dcd4 only for footer-level coda sections, never mid-page

Avoid:

- Don't add drop-shadows to any element - depth comes from fill, not blur
- Don't use Signal Orange #fe5431 or Amber Pulse #ff8000 as button backgrounds or link colors - they are decoration only
- Don't introduce a max-width container on text blocks - the left-edge 64px padding is the only gutter
- Don't use a second typeface, even for captions - Good Sans 400 covers the entire voice
- Don't add borders, dividers, or rules between sections - let whitespace do the work
- Don't crop project images with rounded corners or contain them in cards
- Don't bold or italicize any text for emphasis - use the taupe-to-carbon color shift instead

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
