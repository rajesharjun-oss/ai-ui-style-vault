# AI Implementation Prompt

Build a Lusion-inspired interface using this source-derived style bundle.

Reference site: https://lusion.co
Theme: light
Category: Agency
North star: 3D sculpture gallery on a frosted lavender plane. Every interface element should feel like a tactile object resting on a pale, slightly cool gallery floor, with the 3D content doing all the chromatic and dramatic work.

Use these palette anchors:

- Lavender Mist `#f0f1fa` for Page canvas - the dominant background, a cool off-white with a barely-perceptible lavender cast that makes pure black text feel sharper than it would on pure white
- Paper White `#ffffff` for Elevated card and surface backgrounds, button text on dark fills, inverted surfaces
- Ink `#000000` for Primary text, all headings, body copy, icons, and link text - pure black with no softening
- Graphite `#2b2e3a` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Haze `#e4e6ef` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Slate Hollow `#34393f` for Deep surface layer for dark bands or modal overlays, darker than graphite for clear hierarchy separation
- Electric Indigo `#1a2ffb` for Chromatic brand accent - appears as icon stroke, inline highlight marks, and as the signature color inside the 3D hero render. The single source of energy against the otherwise achromatic UI
- Acid Lime `#c1ff00` for Highlight wash for emphasis zones, secondary accent inside 3D compositions - used sparingly as a surprise contrast

Use these typography anchors:

- Aeonik `--font-aeonik` for Used for every text element on the site - navigation, body, headings, buttons, inputs. The deliberate weight ceiling at 500 (no bold) and uniformly tight -0.02em tracking create a uniform geometric confidence. Display sizes compress line-height to 0.90, letting the largest headlines (108-144px) feel sculpted rather than set. The 400 weight is the workhorse; 500 is reserved for navigation, labels, and button text where a slight emphasis is needed.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1400px.
- Section gap: 72px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Pill Action Button: Primary call-to-action (e.g. 'LET'S TALK')
- Ghost Navigation Link: Header menu items and inline links
- Menu Toggle Button: Header right-side menu trigger
- Hero Image Container: Large 3D artwork display
- Card Surface: Content cards, secondary information blocks
- Scroll Indicator: Bottom-of-viewport prompt
- Input Field: Form inputs in contact or newsletter areas
- Header Bar: Site-wide navigation
- Section Divider Tick: Visual rhythm element between sections

Do:

- Use Lavender Mist (#f0f1fa) as the canvas for every full-page background; never use pure white as the page base - the slight lavender cast is the brand
- Set all text to pure black (#000000) with Aeonik at weight 400-500 and tracking -0.02em; never introduce a bold weight or a softer gray for emphasis
- Use the 87.5px pill radius for all action buttons and the 100px radius for all image/hero containers; these two radii are the signature shape language
- Reach for Electric Indigo (#1a2ffb) only as a chromatic punctuation - icon stroke, inline highlight, focus ring on inputs - never as a large filled surface
- Keep shadows at the single 4% black whisper stack (0px 6px 10px + 0px 2px 4px); do not stack multiple elevations or introduce colored shadows
- Space sections at 72px vertical rhythm; let the generous breathing room and 3D content do the work rather than adding dividers or borders
- Use Aeonik at the full size range from 12px caption through 144px display; let the type scale itself create hierarchy rather than color or weight variation

Avoid:

- Don't introduce a third type weight above 500 - bold or black weights break the restrained typographic system
- Don't use white (#ffffff) as the page background; the Lavender Mist canvas is what makes black text and 3D content feel cut and crisp
- Don't fill large UI surfaces with Electric Indigo; it is an accent, not a brand wash - large indigo blocks destroy the gallery-floor metaphor
- Don't add decorative gradients, glassmorphism, or blur effects; surfaces are flat and physical
- Don't use 8px, 12px, or 20px border-radii on cards, buttons, or containers - stick to the defined 3px, 15px, 18px, 87.5px, and 100px values
- Don't add hover states that change background fill or introduce color; rely on opacity shifts and underline reveals against the static canvas
- Don't use the Acid Lime (#c1ff00) as a CTA or text background; it lacks the contrast hierarchy needed for interactive elements and belongs only inside 3D compositions or highlight washes

Source prompt cues:

Quick Color Reference:
- text: #000000 (pure black, all sizes and weights)
- background (canvas): #f0f1fa (Lavender Mist)
- surface (cards): #ffffff (white)
- border: #e4e6ef (Haze)
- accent: #1a2ffb (Electric Indigo, for icons and focus rings only)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a hero section: Lavender Mist (#f0f1fa) canvas. Centered headline in Aeonik 50px weight 500, #000000, letter-spacing -1.0px, line-height 1.10, 3 lines max. Below, a full-width 3D render container at 100px border-radius, bleeding edge-to-edge, no padding, no border, no shadow. Centered below the container, a 'SCROLL TO EXPLORE' label in Aeonik 12px weight 500, #000000, uppercase, flanked by plus signs.

2. Create a header navigation bar: Transparent on Lavender Mist (#f0f1fa), 24px vertical padding. Left: 'LUSION' wordmark in Aeonik 16px weight 500, #000000. Center: short descriptive line in Aeonik 16px weight 400, #000000. Right: a pill button (background #2b2e3a, text #ffffff, Aeonik 14px weight 500, uppercase, padding 14px 24px, radius 87.5px) with a small white dash icon to the left of the label, followed by a 'MENU' text trigger in Aeonik 14px weight 500, #000000, with a dash icon.

3. Create a card grid: White (#ffffff) cards at 15px border-radius, 24px padding, optional 1px border in #e4e6ef. Title in Aeonik 22px weight 500, #000000. Body in Aeonik 16px weight 400, #000000. No drop shadow on the card itself; rely on the white-on-lavender contrast for separation. Space cards with 24-32px gap in a 3-column grid, max-width 1200px centered on the Lavender Mist canvas.

4. Create an input field: Background #ffffff, border 1px solid #e4e6ef, 18px border-radius, padding 14px 18px. Placeholder text in Aeonik 16px weight 400 in a muted gray. Focus state: border switches to Electric Indigo (#1a2ffb), no other change - no glow, no shadow, no background shift.

5. Create a section divider: On the Lavender Mist canvas, place a centered horizontal row of three small plus signs (+) in #000000, Aeonik 16px, spaced 16px apart, serving as a decorative tick separator between content blocks. No lines, no background change.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
