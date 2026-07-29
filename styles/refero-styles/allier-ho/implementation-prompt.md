# AI Implementation Prompt

Build a Allier Ho-inspired interface using this source-derived style bundle.

Reference site: https://allierho.com
Theme: light
Category: Agency
North star: serif whisper on warm paper

Use these palette anchors:

- Warm Paper `#fcfcfc` for Page canvas, card surfaces, and nav background - the base layer everything sits on
- Deep Ink `#000000` for Primary text, body copy, nav links, and dominant border color - the structural voice
- Press Black `#1c1c1c` for Heading text and heavy borders - slightly softer than pure black for large display sizes
- Charcoal Trace `#262626` for Secondary borders, dividers, and muted text on dark surfaces
- Ash `#a8a8a8` for Helper text, disabled states, and hairline borders on light surfaces
- Dusty Mauve `#6c5f7d` for Accent panel backgrounds, heading color, and chromatic border - a near-gray purple that signals brand moments without shouting
- Pale Sage `#cee6cc` for Secondary heading tint and accent border - a near-gray green that appears as quiet punctuation alongside the mauve

Use these typography anchors:

- Crimson Pro `--font-crimson-pro` for Display headlines at 44-50px, weight 300 with negative tracking. The anti-conventionally light serif whispers authority instead of projecting it; most agencies use 600-700 here, this restraint is the signature move.
- Azeret Mono `--font-azeret-mono` for Body copy, labels, and metadata at 12-18px. Monospace for a portfolio is a deliberate editorial choice - it reads as technical, precise, and un-decorative, contrasting the flowing serif headlines.
- System Sans-Serif `--font-system-sans-serif` for Navigation links and micro-labels at 12px. Neutral utility voice that stays out of the way of the serif/mono dialogue.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1280px.
- Section gap: 100px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Minimal Top Nav: Site navigation bar
- Pill Text Button: Interactive button
- Hero Overlay Panel: Hero text block
- Service List: Metadata sidebar in hero
- Section Heading: Section title
- Project Showcase Card: Work portfolio entry
- Category Tag: Project metadata label
- Footer Page Indicator: Page position marker
- Inline Text Link: Body link
- Work Grid Row: Two-column project layout

Do:

- Use Crimson Pro at weight 300 for all display headlines between 44-50px with letter-spacing around -1.5px - the whisper-weight is the signature
- Set border-radius to 200px on all buttons and tags for the fully pill-shaped interactive language
- Use #fcfcfc as the sole page canvas - never introduce pure white (#ffffff) or cooler grays
- Apply #6c5f7d dusty mauve as the only chromatic surface fill, reserved for hero overlay panels and occasional heading tints
- Pair serif headlines with Azeret Mono body text - the mono/serif dialogue defines the editorial tone
- Keep section gaps at 100px and element gaps at 10px to maintain the gallery-walk rhythm
- Let imagery run edge-to-edge with no borders, radius, or shadow - the photograph or 3D render is the visual

Avoid:

- Don't use Crimson Pro at weight 400 or heavier - the light weight is non-negotiable
- Don't add drop shadows, inner shadows, or glow effects to cards, buttons, or images - the system is flat
- Don't introduce additional accent colors beyond dusty mauve and pale sage - the palette is deliberately two-note
- Don't round corners on cards, panels, or images - only buttons and tags use radius
- Don't use a sans-serif for body copy - Azeret Mono is the body voice; sans-serif is reserved for nav and labels only
- Don't fill buttons with solid color - the pill outline on transparent background is the only button style
- Don't use system serif or serif substitutes for body - Crimson Pro is display-only

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #fcfcfc
- border: #1c1c1c or #a8a8a8
- accent: #6c5f7d (dusty mauve)
- secondary accent: #cee6cc (pale sage)
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Create a hero overlay panel*: 320px wide rectangular block, background #6c5f7d, no border-radius, 40px padding. White Crimson Pro weight 300 at 44px, line-height 1.15, letter-spacing -1.5px. Below the headline, a pill outline button: 200px radius, 10px/18px padding, 1px #000000 border, transparent fill, 12px system sans black text reading "LEARN MORE".

2. *Create a section heading*: Centered Crimson Pro weight 300 at 44px, line-height 1.15, letter-spacing -1.5px, color #000000. Second clause in italic. Below at 40px gap, a centered pill outline button (same spec as above) with text "VIEW ALL WORK".

3. *Create a project showcase card*: Full-width image (no border, no radius, no shadow), 20px top padding, then a caption block: 12px Azeret Mono uppercase title in #000000, followed by 10px gap, 12px system sans category tag in #a8a8a8.

4. *Create the top navigation*: Full-width row, 20px vertical padding, background #fcfcfc. Left: "ALLIER HO" in 12px system sans uppercase, letter-spacing normal. Right: three links "WORK", "ABOUT", "PLAYGROUND" in same style, 40px gap between them. No borders, no background change on hover.

5. *Create a service list sidebar*: Vertical stack of 12px Azeret Mono uppercase labels, 10px row gap, color #6c5f7d. No bullets, no dividers, no borders. First item "SERVICE" slightly larger or in a different color as a section header.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
