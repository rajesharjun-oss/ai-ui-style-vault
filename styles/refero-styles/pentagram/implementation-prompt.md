# AI Implementation Prompt

Build a Pentagram-inspired interface using this source-derived style bundle.

Reference site: https://pentagram.com
Theme: light
Category: Agency
North star: Gallery wall of compressed restraint

Use these palette anchors:

- Paper White `#ffffff` for Page canvas, card surfaces, text on dark bands
- Ink `#1a1a1a` for Primary body text, heading text, hairline borders, link color - the near-black that carries 90% of all strokes
- True Black `#000000` for Solid surface fills for dark bands, inverted text backgrounds, inverted footer
- Graphite `#222222` for Elevated dark surface, input field fills on dark contexts
- Carbon `#333333` for Card border on light surfaces, subtle structural dividers
- Ash `#767676` for Muted body text, secondary metadata, less-prominent captions
- Fog `#8c8c8c` for Light borders, low-emphasis dividers, placeholder text
- Mist `#ededed` for Tinted light surface between pure white and true black bands
- Haze `#e3e4e5` for Subtle alt-row surface, hover wash, low-contrast card fill

Use these typography anchors:

- Plain `--font-plain` for All roles - display, headings, body, caption, nav, button. The single typeface carries the entire site. Weight contrast is limited (400 vs 500) so hierarchy comes from size and tracking, not boldness. The 52px display at -0.02em tracking is anti-display: it whispers instead of shouts. Line-heights under 1.1 on 32-52px create stacked, compressed blocks where headings read as solid slabs. Open features 'kern' and 'case' hint at a typeface with carefully spaced uppercase alternates - the 'case' feature likely gives access to stylistic capital forms.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1400px.
- Section gap: 96px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Text Navigation Bar: Primary site navigation
- Full-Bleed Editorial Hero: Opening visual for a project or the homepage
- Project Thumbnail Card: Showcase a project in the grid
- Project Thumbnail Card with Imagery: Showcase a project that uses a designed mark/identity
- Dark Band Section: Break page rhythm, introduce new context
- Inline Tagline Pill: Occasional textual accent between sections
- Heading-Only Introduction: Section opening before a grid or list
- Footer (Inverted): Site footer
- Dot Pagination: Hero carousel / project slider indicator
- Search Trigger: Open site search

Do:

- Use only the nine achromatic tokens - any chromatic color in the interface breaks the system. Color belongs inside project thumbnails, not on chrome.
- Set the tightest tracking (-0.02em) on any text 27px or larger; use -0.01em below that. Tracking is the primary hierarchy tool.
- Build cards as borderless blocks with sharp corners (no radius) when the thumbnail is a solid color swatch; reserve 8px radius for cards that contain photography or compound layouts.
- Alternate between Paper White and True Black bands at 96px vertical breaks - the rhythm of light/dark is the page's structural skeleton.
- Use weight 400 for everything by default; reach 500 only for project names in cards and nav links. Never use weight 600 or above.
- Set display headings at line-height 1.00-1.05 so lines stack into a compressed slab. Body copy opens to 1.88 for breathing room - the contrast between tight display and airy body is deliberate.
- Let the 4-column project grid do the visual work: large solid-color blocks fill 1:1 tiles, with a 24px gap below for two lines of Plain 400/500 metadata in 16/13px.

Avoid:

- Don't add any color to navigation, buttons, or backgrounds. The interface is 100% achromatic - color only appears inside project thumbnails.
- Don't use border-radius above 8px on cards or 4px on buttons. Sharp corners read as editorial plates; rounding undermines the gallery-catalog feel.
- Don't introduce filled buttons, outlined buttons, or ghost buttons. There is no button component - every affordance is a text link, an image, or a dot.
- Don't use weight 600+ or italic. The typeface's weight range stops at 500; anything heavier breaks the compressed-restraint language.
- Don't add icons inside body content. The only icon on the entire site is the search affordance in the nav.
- Don't use background colors on text or dividers for emphasis. Emphasis comes from size, tracking, and the Paper White / Ink contrast pair - never from color fill or tint.
- Don't use shadows, gradients, or glow effects. Elevation is communicated purely through band alternation (white black white), not through drop shadows.

Source prompt cues:

**Quick Color Reference**
- text: #1a1a1a
- background: #ffffff
- dark band: #000000
- border: #1a1a1a
- muted text: #767676
- primary action: #000000 (filled action)

**Example Component Prompts**
1. *Dark band section*: Full-width band, #000000 background, 64px padding top/bottom. Heading 'Our Future is the Ultimate Project' in Plain weight 400 at 52px, line-height 1.00, letter-spacing -0.02em, color #ffffff. Optional body paragraph below at Plain 400 16px, line-height 1.88, color #767676, max-width 640px.

2. *Project card grid (white band)*: 4-column CSS grid, 24px gap, on #ffffff canvas. Each card has no border, no radius. Card thumbnail is a solid color block (e.g. #2a6ec7 or #2d3a2a) filling a 1:1 aspect ratio. Below the block, 24px gap, project name in Plain 500 16px #1a1a1a, one-line description in Plain 400 13px #767676.

3. *Full-bleed hero*: Edge-to-edge image filling full viewport width, ~70vh height, no border-radius. Project name in Plain 400 13px #ffffff at bottom-left with 24px padding from edges. Small dot pagination row at bottom-right, 6px circles, 6px gap, active dot #ffffff, inactive dots at 40% opacity white.

4. *Top navigation bar*: #ffffff background, 8px padding top/bottom. Left: 'Pentagram' wordmark in Plain 500 16px #1a1a1a. Right: text links 'Work', 'About', 'News', 'Contact', 'Archive' in Plain 400 16px #1a1a1a, letter-spacing -0.01em, with a small search icon between Contact and Archive. No borders, no background fills on links.

5. *Inline tagline*: Centered text 'We design Everything~ for Everyone~' in Plain 400 16px #8c8c8c, sitting alone in a #ffffff band with 96px padding top/bottom, no other elements on the line.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
