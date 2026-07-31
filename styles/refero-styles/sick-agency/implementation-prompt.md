# AI Implementation Prompt

Build a SICK AGENCY-inspired interface using this source-derived style bundle.

Reference site: https://sick.agency
Theme: mixed
Category: Agency
North star: Loud printed broadside on a brick wall - a maximalist zine spread screaming from a screen.

Use these palette anchors:

- Voltage Yellow `#ffc700` for Primary section background and dominant display text color. Headings, borders, and full-bleed canvas bands. Carries the highest visual weight on the page
- Radioactive Orange `#ff4e27` for Secondary section background and accent border color. Outlined action borders, dividers, icon strokes, and full-bleed canvas bands that create contrast with the yellow
- Electric Cobalt `#0029ff` for Primary action background and tertiary section background. The only filled button color in the system; also used for full-bleed canvas bands and decorative sticker badges
- Burnt Sienna `#4d170c` for Error and warning state. Input border in invalid state. Reads as a deep brick-red against the lighter orange, preserving the system's warm-color vocabulary
- Ink Black `#000000` for Body text on light/yellow backgrounds, and the dominant border color across all surface bands. Functions as a hairline outline and text color wherever contrast is needed against yellow or white
- Bone White `#ffffff` for Body text and button text on cobalt and orange surfaces. The inverse of Ink Black - the two together carry all foreground-to-background contrast in the system

Use these typography anchors:

- Morganite `--font-morganite` for Hero display face for the single largest typographic statement per page. The extreme 0.70 line-height stacks letterforms with no air between lines - type is treated as a solid block, not a paragraph. This face defines the agency's shock-value identity.
- Thunder `--font-thunder` for Secondary display face used at near-hero scale. The light weight is anti-convention for a 122px headline - most agencies use 700-900 here. Thunder's 300 whispers while still occupying monumental space, creating tension between volume and restraint. Substituted by ITC Avant Garde Gothic, Futura, or any geometric humanist sans.
- Sentient `--font-sentient` for Workhorse text face for body copy, buttons, inputs, links, and small labels. Carries tight negative tracking (-0.0100em to -0.0200em) even at body sizes, which is a serif's signature in a sans-dominated layout. Substituted by any transitional serif.
- Times `--font-times` for Fine-print and micro-label face for legal text, tiny annotations, and icon-adjacent micro-copy. Its system-serif feel is a deliberate contrast to the custom display faces, creating a visual fossil-record effect.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: .
- Element gap: .

Build these component patterns where relevant:

- Primary Action Button: Filled cobalt pill button - the only filled button in the system
- Outlined Ghost Button: Outlined action used when a second action is needed beside the primary
- Display Heading (Black): Morganite 900 set at 229px with 0.70 line-height
- Display Heading (Light): Thunder 300 set at 122px
- Body Text Block: Sentient 16px / 1.44 on colored canvas
- Text Input: Form field with sharp corners and thick black border
- Sticker Badge: Decorative circular badge used as a CTA anchor or section marker
- Hairline Divider: Thin black line used to separate text blocks inside a colored section
- Full-Bleed Section Band: The atomic layout unit - a single color field filling the viewport horizontally
- Decorative Illustration Sticker: Small hand-drawn illustrated objects placed on the canvas as visual personality
- Micro Label: Sentient 12px label for tags, metadata, and small annotations
- Vertical Type Stack: Sentient or Thunder set 90 rotated, used as a poster-style edge element

Do:

- Use #0029ff as the filled button background and #ffc700 as the dominant section canvas - these are the system's two anchor colors and must both appear on every page.
- Set display headings at 122px (Thunder 300) or 229px (Morganite 900); never use a display face below 80px or above 240px.
- Use 999px border-radius only on buttons, badges, and decorative stickers - keep form fields, section bands, and dividers at 0px sharp corners.
- Use Sentient at 12-24px with negative tracking (-0.0100em to -0.0200em) for all body and small text; use Times only for 10px fine print and micro-annotations.
- Stack sections as full-bleed color bands in #ffc700 / #ff4e27 / #0029ff order with 0px gap and no gradient transitions between them.
- Use #4d170c only as an error-state input border - never as a section background, decorative element, or button fill.
- Anchor one corner of a hero with a circular Sticker Badge in a contrasting system color; treat it as a CTA and a visual punctuation mark simultaneously.

Avoid:

- Do not introduce grays, off-whites, beige, or any desaturated color into the system - neutrals are only #000000 and #ffffff, used for text and borders.
- Do not add box-shadow, drop-shadow, or blur to any element - depth comes from color contrast between full-bleed bands, never from elevation.
- Do not use rounded corners (4px, 8px, 16px) on cards, sections, or containers - sharp 0px corners and 999px pills are the only two radii allowed.
- Do not set display type below 80px or set body type above 24px - the gap between body and display is what creates the broadside scale, and closing it destroys the system.
- Do not use Morganite 900 with line-height above 0.80 - its identity depends on near-touching stacked lines; looser leading would turn it into a generic display face.
- Do not place a primary action button on a white or near-white background - the system has no white surface; buttons live on yellow, orange, or cobalt fields.
- Do not use photographic backgrounds, gradients, or textures - surfaces are always flat solid color.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
