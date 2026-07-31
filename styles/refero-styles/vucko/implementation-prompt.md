# AI Implementation Prompt

Build a Vucko-inspired interface using this source-derived style bundle.

Reference site: https://vucko.co
Theme: light
Category: Agency
North star: oversized type on white gallery floor - a type-specimen book where the wordmark is the room.

Use these palette anchors:

- Ink `#000000` for Primary text, all borders, dark surface blocks, and the hero wordmark - the structural backbone of every screen
- Paper `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Faint Ash `#eeeeee` for Subtle surface tint for secondary cards or de-emphasized blocks, barely distinguishable from Paper
- Steel `#888a8b` for Muted secondary text and ghost-list items in service lists - the only non-black text color, used to create tonal hierarchy without introducing hue
- Charcoal `#222222` for Alternate dark surface for nav or panel backgrounds - a softer dark than Ink when full black is too severe

Use these typography anchors:

- Suisse Int'l `--font-suisse-intl` for Sole typeface across the entire system. Weight 700 carries all display and heading roles up to 211px for the hero wordmark; weight 400 handles body and link text. The 211px weight-700 wordmark with -0.057em tracking is the signature - it turns the brand name into a room-scale installation. Weight 500 appears in nav and transitional text. The aggressive negative tracking on display sizes (-0.057em at 211px, -0.020em at 55px) tightens the Swiss grotesque geometry into a denser, more monolithic block - the type is meant to read as architecture, not as text.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 58px.
- Card padding: 24px.
- Element gap: 23px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal site-wide navigation
- Hero Display Wordmark: Primary brand statement on landing
- Floating Showcase Card: Featured project overlay on hero
- Tagline Section: Brand statement below hero
- Project Showcase Card (Full-bleed): Client work presentation in portfolio
- Service Block (Media + Text): Individual service description in services section
- Service List Display: Large-scale service category headings
- Pill Tag / Button: Project labels, nav indicators, and pill-shaped interactive elements
- Underline Text Link: Primary text-based link style
- Scroll Indicator: Navigation hint at hero boundary

Do:

- Use #000000 (Ink) for all primary text, borders, and dark surface blocks - it is the only structural color in the system
- Set the hero wordmark at 211px Suisse weight 700 with letter-spacing -12.03px - the type is meant to fill the room
- Apply 56px horizontal padding on the main container and 58px vertical gaps between major sections
- Use 9999px border-radius for all pill-shaped elements: nav dot, tags, and pill buttons
- Use tonal hierarchy (Ink vs Steel at #888a8b) rather than size or weight to create secondary text emphasis
- Use 9.6px border-radius for project cards and content containers
- Apply negative letter-spacing on all display sizes: -12.03px at 211px, -6.84px at 120px, -1.1px at 55px, -0.43px at 43px

Avoid:

- Never add colored CTA buttons - this system uses underlined text links and neutral pill elements only
- Never use drop shadows, glow effects, or any form of CSS elevation - depth comes from whitespace and contrast alone
- Never center body text - all running text should be left-aligned
- Never use borders thicker than 1px
- Never introduce chromatic colors into the UI chrome - color belongs exclusively inside project showcase content
- Never use display sizes (55px+) for body copy or secondary content - reserve them for headlines and service titles only
- Never break the whitespace rhythm - maintain 58px minimum between major sections and let the type do the work

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000
- muted text: #888a8b
- subtle surface: #eeeeee
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a hero section: white (#ffffff) background, 56px horizontal padding. Display wordmark at 211px Suisse weight 700, color #000000, letter-spacing -12.03px, line-height 1.0. A small yellow card (~9.6px radius, 24px padding) with black bold project title at 43px is positioned absolutely in the upper-right area of the hero.

2. Create a project showcase card: full-bleed within 56px container padding, 9.6px border-radius. Background is a blue-to-purple gradient. Centered white display text at 55px Suisse weight 700 with letter-spacing -1.1px. A white pill button (9999px radius, 10px 15px padding, black text at 17px) overlaid near the bottom.

3. Create a services section: split layout with 23px column gap. Left: a 200px black (#000000) square block with body text below at 17px Suisse weight 400 in #000000. Right: three stacked display headings at 55px Suisse weight 700, the first in #000000, the remaining two in #888a8b, each on its own line with letter-spacing -1.1px and line-height 1.13.

4. Create a top navigation bar: white background, no border, 56px horizontal padding. Left-aligned 'VUCKO' at 17px Suisse weight 700. Centered location/time text at 17px Suisse weight 400. Right-aligned nav links at 17px Suisse weight 400. A small 8px black (#000000) dot with 9999px radius at the far right.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
