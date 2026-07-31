# AI Implementation Prompt

Build a Stink Studios-inspired interface using this source-derived style bundle.

Reference site: https://www.stinkstudios.com
Theme: dark
Category: Agency
North star: cinema studio at midnight - the projector hums, the room is black, only the reel glows.

Use these palette anchors:

- Void `#000000` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Bone `#ffffff` for Primary text, heading strokes, nav links, icon strokes, badge fills, logo type - the only high-contrast value in the system
- Soot `#050505` for Subtle tonal break from pure black for nested surfaces and hairline borders that need to feel present without breaking the dark mode
- Ember Coral `#e1695e` for Accent warmth for marquee display moments, logo gradient highlight, and select project card color treatments - borrowed from the work, never applied to UI chrome
- Burnt Sienna `#573332` for Deep warm surface for warm-toned project cards and content imagery containers - the shadow side of the coral accent

Use these typography anchors:

- Helvetica `--font-helvetica` for Primary workhorse - body copy at 16px/400, secondary headings at 23px/400, nav and links at 16px/400, and the massive 52px/300 hero logo treatment. Weight 300 is the default for large display: whisper-thin against the heavy black canvas creates a neon-on-velvet tension.
- Times New Roman `--font-times-new-roman` for Display serif for editorial pull-quotes and manifesto text - the 60px size with -0.05em tracking creates a fashion-magazine weight that contrasts Helvetica's geometric neutrality. Used sparingly for sentences that need gravitas.
- Courier New `--font-courier-new` for Monospace for tags, badges, index numbers, and micro-labels - the 0.10em positive tracking turns utility text into graphic texture, like film slate markings

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 60-180px.
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Full-Bleed Hero Reel: Opening cinematic frame
- Manifesto Statement Block: Editorial typographic section
- Work Grid Card: Project showcase tile
- Bottom-Right Nav Cluster: Primary site navigation
- Monospace Tag: Project metadata label
- Ghost Link: Inline text link
- Full-Bleed Image Block: Immersive project frame
- Circular Icon Button: Compact utility trigger
- Text Input: Form field on dark canvas

Do:

- Use 52px Helvetica weight 300 for any logo or hero wordmark, with -2.08px letter-spacing to compress the caps into a cinematic block
- Reserve 60px Times New Roman weight 400 for editorial statements and manifesto copy - never for navigation, labels, or body
- Apply 0.10em positive letter-spacing to all Courier New 14px text (tags, badges, index numbers) to read as slate-marking texture
- Let the page canvas be #000000 universally - do not introduce light section bands; the system is monochrome by intention
- Use 20px gap between navigation links and 60px minimum margin-top between major editorial sections
- Set every image to full-bleed (100vw) with 0px radius when it is the section's primary content
- Signal interactivity through a 1px white bottom border appearing on hover - never through color shifts or background fills

Avoid:

- Do not introduce colored buttons, colored backgrounds, or gradient UI elements - the accent palette belongs to the work, not the chrome
- Do not use box-shadow or elevation on cards, buttons, or navigation - this system is deliberately flat; depth comes from imagery, not stacking
- Do not use rounded corners on cards or work tiles - 0px radius is the signature; rounded containers would break the cinematic frame
- Do not combine the serif display (Times New Roman) with the monospace (Courier New) on the same line or within the same component
- Do not add light-mode toggle, theme switcher UI, or alternate color schemes - dark is the only mode
- Do not use font-weight above 700 for Helvetica - the system lives in the 300-700 range; black weight would break the whisper-thin display logic
- Do not pad work cards with internal whitespace - imagery bleeds to the cell edges, and titles overlay the image directly

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #000000
- border: #050505
- accent: #e1695e (project content only, not UI)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero with wordmark**: Full-viewport (100vw x 100vh) cinematic image as background. Centered or top-left wordmark at 52px Helvetica weight 300 in #ffffff with -2.08px letter-spacing and 0.90 line-height. No overlay gradient, no button - just the image and the type.

2. **Manifesto section**: #000000 background, 60px Times New Roman weight 400 in #ffffff at -3px letter-spacing, left-aligned with 60px left margin, 1.00 line-height. Single declarative sentence, 2-3 lines tall. No icon, no border, no supporting media.

3. **Work grid tile**: Full-bleed image filling a 50vw x auto cell with 0px radius. Bottom-left overlay text in 19px Helvetica 400 #ffffff at -0.38px letter-spacing. No padding, no border, no shadow. Caption in 14px Courier New 400 #ffffff at 1.4px letter-spacing above the title.

4. **Bottom-right nav**: Fixed position bottom-right, 32px from edges. Links at 16px Helvetica 400 #ffffff separated by 20px gap: 'Work', 'About', 'News', 'Contact'. 1px #ffffff bottom border appears on hover. Followed by a 16px circular icon button with 10px radius and 1px #ffffff border.

5. **Ghost link in body copy**: 16px Helvetica 400 #ffffff inline within a paragraph. No underline by default. On hover, 1px #ffffff bottom border fades in over 200ms.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
