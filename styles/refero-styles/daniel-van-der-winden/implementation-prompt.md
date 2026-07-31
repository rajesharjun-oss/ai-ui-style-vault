# AI Implementation Prompt

Build a Daniel van der Winden-inspired interface using this source-derived style bundle.

Reference site: https://www.daniel.pizza
Theme: light
Category: Agency
North star: Printed monograph on vellum

Use these palette anchors:

- Vellum `#e5e7eb` for Page canvas, hairline dividers, link underlines, card-edge borders - the warm-gray field that holds all content
- Ink Black `#111827` for Primary text, nav links, body copy - the default reading color
- Graphite `#374151` for Secondary body text, list items, supporting copy - one step lighter than primary ink
- Charcoal `#2a2a28` for Headings and editorial emphasis - slightly warm dark for serif display
- Stone `#717272` for Tertiary text, icon fills, meta labels
- Pebble `#909191` for Muted body text, image captions, fine print
- Ash `#c4c6c8` for Rarely-used border, subtle structural separator
- Slate `#7b7c7c` for Subdued heading variant, de-emphasized titles
- Pressed Ink `#222222` for Primary action button fill - the only dark surface on the canvas, creating the only moment of visual weight
- Midnight `#1a202c` for Secondary dark surface, alternate button fill

Use these typography anchors:

- Degular `--font-degular` for UI and body sans - navigation, buttons, body copy, metadata, links, tags, resume dates. Carries all functional text. Weights step from 400 body to 700 for emphasis in headings and dates.
- Blanco `--font-blanco` for Editorial serif - hero headline, resume role titles, section headings, and any text that should read as 'published' rather than 'navigational'. Single weight 400, letting size and the serif's own authority carry hierarchy.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 720px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Sidebar Nav: Persistent left rail navigation
- Email Me Button: Primary and only action on the page
- Social Link Row: Secondary contact links beside the primary action
- Photo Collage Block: Hero visual element overlapping the text column
- Resume Entry: Date-anchored experience block
- Section Heading: Editorial section title
- External Link with Arrow: Outbound link indicator
- Nav Link: Text-only navigation item
- Body Text Block: Prose paragraph for bio and descriptions

Do:

- Use #e5e7eb as the only surface; never introduce a white card or alternate background.
- Pair Blanco 400 for all headings and titles; reserve Degular for UI, body, and metadata.
- Use the single dark fill (#222222) for exactly one action per viewport - scarcity makes it land.
- Set border-radius to 3px for images, buttons, and tags; 8px is reserved for larger interactive surfaces.
- Anchor resume entries with date labels in the narrow left column, titles in the right - never inline.
- Let photographs overlap the text column; avoid placing images in rigid boxed containers.
- Set body text at 18px Degular 400 #374151 with 1.5 line-height; this is the reading rhythm of the entire site.

Avoid:

- Do not introduce chromatic color - the 3% colorfulness is deliberate, not a limitation to fix.
- Do not add shadows, gradients, or glow effects; elevation is achieved through fill contrast only.
- Do not use Blanco for body text or nav; it is a display face, not a reading face.
- Do not create card containers with backgrounds or borders for content blocks - content sits directly on the vellum.
- Do not use 9999px pill radius; this system's 3px radius is a quiet, bookish choice.
- Do not bold body text for emphasis; use size, color, or the Blanco/Degular font swap instead.
- Do not center-align body paragraphs; left-align at a fixed reading width to preserve the editorial column.

Source prompt cues:

**Quick Color Reference**
- text: #111827
- background: #e5e7eb
- border: #e5e7eb
- accent: none (monochrome system)
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a sidebar nav: fixed left column 180px wide, wordmark 'Daniel van der Winden' in Degular 500 16px #111827 at top, nav links (Journal, Library, Links, Magazine, Newsletter, Work) in Degular 500 16px #111827 stacked vertically at bottom with 12px gap. No background, no border.

2. Create a resume entry: two-column row, left column 80px wide with date '2023-2028' in Degular 14px #717272, right column with role title 'Co-Founder of TRANSCRIPT Magazine' in Blanco 400 22px #2a2a28 followed by description in Degular 400 18px #374151 line-height 1.5. Separate from next entry with a 1px #e5e7eb hairline and 32px vertical gap.

3. Create a hero block: two black-and-white photographs overlapping in the left third, shifted up and down by 40px to create a collage effect. Right two-thirds holds a Blanco 400 40px #2a2a28 headline followed by 3 paragraphs of Degular 400 18px #374151 body text with 27px margin-bottom. Images have 3px border-radius, no shadow.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

5. Create a section heading: Blanco 400 28px in #2a2a28, left-aligned, no underline, sitting 40px above its content block. This is an editorial chapter title, not a UI label.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
