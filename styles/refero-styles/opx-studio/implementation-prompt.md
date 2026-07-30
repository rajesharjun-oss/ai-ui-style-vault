# AI Implementation Prompt

Build a OPX Studio-inspired interface using this source-derived style bundle.

Reference site: https://opx.studio
Theme: dark
Category: Agency
North star: Dark gallery monolith - a near-black exhibition hall where monumental white type and full-bleed photography do all the talking, and borders whisper at #292a2c.

Use these palette anchors:

- Void Black `#020202` for Page canvas - the base background across all sections
- Surface Black `#000000` for Section surfaces and image containment backgrounds, barely distinguishable from canvas to keep elevation flat
- Charcoal Hairline `#292a2c` for Structural dividers and borders - the only mid-tone in the system, carrying 900 occurrences as the skeleton between sections and elements
- Bone White `#ffffff` for Primary text, nav labels, project titles, and 1px pill-button borders - the sole signal of interactivity
- Ash Gray `#9b9b9b` for Muted helper text and secondary metadata in footer and supporting copy - recedes against the void

Use these typography anchors:

- OPX-Medium `--font-opx-medium` for Primary brand display and text face - a single weight (400) scaling across body, nav, subheadings, and monumental display. Custom face with a humanist-geometric tension; the anti-convention of using weight 400 (not bold) at 111px display size lets the headline dominate through scale alone rather than visual weight
- Open Sans `--font-open-sans` for Secondary supporting copy - used in hero subtext and longer descriptive passages where a more relaxed, open-licensed humanist is desired
- Untitled `--font-untitled` for Small label text for pill buttons and tag-like links (e.g. "View case study") - the only weight-500 usage in the system, giving micro-UI slightly more presence
- Helvetica `--font-helvetica` for System fallback for incidental body text and metadata

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 100-200px.
- Card padding: .
- Element gap: 30px.

Build these component patterns where relevant:

- Display Navigation Link: Primary top-bar nav item ("Projects", "Studio")
- Editorial Hero Headline: Opening statement on the home canvas
- Featured Project Block: Single full-bleed project case study (e.g. KB&Co)
- Project Card (Grid Item): Individual case study tile in the 3-column project grid
- Pill CTA Button ('View case study'): Primary call-to-action linking to a case study
- Section Heading: Mid-page editorial section titles
- Footer Column Block: Structured contact and meta information at page bottom
- Body Paragraph: Supporting descriptive copy
- Social/External Link: Footer or inline outbound link
- Section Divider: Horizontal separator between major content bands

Do:

- Use OPX-Medium 400 at 80-111px for display headlines with line-height locked at 1.00-1.07 - never bold the display
- Apply the #292a2c 1px hairline as the only divider between sections and around interactive elements
- Set all CTA buttons as 1px white-stroke pills at 45px radius with 7px/15px padding - no filled buttons
- Let photography fill its container edge-to-edge at 0px radius - never frame or round project imagery
- Maintain 100-200px vertical padding between major sections to preserve the editorial pacing
- Use #9b9b9b exclusively for muted metadata and helper text; reserve #ffffff for all primary content
- Keep the navigation to two-word labels set in OPX-Medium - the page is the navigation

Avoid:

- Do not introduce a brand color, accent, or gradient - the system is monochrome by design
- Do not use box-shadows, glows, or any drop-shadow elevation
- Do not bold the display type - authority comes from size (80-111px), not weight
- Do not round the project imagery or apply a card background - images sit on the void directly
- Do not use #9b9b9b on a #ffffff surface - it fails contrast (2.8:1); it's only valid on the dark canvas
- Do not add icons, bullets, or decorative glyphs to the nav or links - type is the only ornament
- Do not tighten body line-height below 1.67 - the relaxed leading is the only counterpoint to the display text's compression

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #020202
- border: #292a2c
- accent: #ffffff (white stroke only, no fill)
- muted text: #9b9b9b
- primary action: no distinct CTA color

**Example Component Prompts**
1. Create a hero headline: #020202 canvas. Display type in OPX-Medium (substitute: Sohne) weight 400, 111px, #ffffff, line-height 1.00, left-aligned with 100px left padding and 200px top padding.
2. Create a project card: full-bleed photograph at 0px radius filling the card width. 30px gap below, then OPX-Medium weight 400, 20px, #ffffff for the project title. 15px gap, then a pill 'View case study' button: 1px solid #ffffff border, transparent fill, 45px border-radius, 7px/15px padding, label in Untitled weight 500, 14px, #ffffff.
3. Create a section divider: 1px solid #292a2c hairline spanning 100% width, with 150px vertical padding above and below the rule.
4. Create a footer column: OPX-Medium weight 400, 20px, #ffffff column label. 20px gap, then 2-3 lines of OPX-Medium weight 400, 18px, #9b9b9b body text. Arrange in a 3-column grid with 50px column gutters.
5. Create a body paragraph: Open Sans (substitute: Source Sans 3) weight 400, 18px, #ffffff, line-height 1.67, on #020202 canvas, with 30px margin-bottom.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
