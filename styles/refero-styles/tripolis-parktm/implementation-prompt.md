# AI Implementation Prompt

Build a Tripolis-ParkTM-inspired interface using this source-derived style bundle.

Reference site: https://www.tripolis-park.com
Theme: light
Category: Other
North star: luminous violet portal - soft lavender light bleeding through frosted glass edges, achromatic content floating above.

Use these palette anchors:

- Aurora Lilac `#c5b0ec` for Hero gradient start, atmospheric section backgrounds - the soft entry tone of the brand's signature violet wash
- Deep Iris `#7c4fb8` for Hero gradient deep stop, section transition anchors - the rich violet terminus that gives the gradient its weight
- Midnight Ink `#000000` for Primary text, heading strokes, hairline borders, icon fills, link color
- Carbon Mist `#2d2d2d` for Secondary text, subdued headings - softer than pure black for less critical copy
- Frost White `#ffffff` for Page canvas, card surfaces, text on dark/gradient backgrounds, ghost button fill
- Ash Veil `#b5b5b5` for Muted helper text, disabled states, tertiary metadata
- Smoke Line `#cccccc` for Hairline dividers, subtle structural lines, secondary borders
- Pale Mist `#e2e2e2` for Light borders, input field outlines, card edge definition
- Concrete Gray `#808080` for Surface variation, muted backgrounds, placeholder fills

Use these typography anchors:

- Matter `--font-matter` for Primary workhorse sans - body copy at 14px and 18px, subheadings at 27px. The humanist proportions and subtle warmth make long-form reading comfortable. Tabular numerals ('tnum') are enabled site-wide, signaling precision and data-readiness across all sizes.
- Matter `--font-matter` for Medium-weight emphasis - used for key headings and callouts at 27px and 47px with -0.025em tracking. The medium weight (not bold) keeps the voice measured and confident rather than aggressive.
- Matter `--font-matter` for SemiBold display weight - reserved for the most prominent headings at 47px with -0.024em tracking. The jump from Medium to SemiBold at the same size is rare and intentional: it creates a deliberate weight tier for hero-level statements.
- IvarHeadline `--font-ivarheadline` for Serif display face for editorial-style headings at 47px. The contrast with Matter's sans body creates a typographic duet - serif headlines anchor emotion and permanence, sans body delivers clarity. Tracking at -0.015em to -0.01em keeps the serif tight and contemporary rather than traditional.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 88-110px.
- Card padding: 23-36px.
- Element gap: 5-23px.

Build these component patterns where relevant:

- Hero Gradient Banner: Full-bleed section background with brand signature gradient
- Bordered Title Frame: Compositional device for brand/title display in hero
- Display Heading: Hero-level statement headline
- Tagline Subtext: Supporting text under hero/display headings
- Ghost Navigation Button: Outlined/ghost-style action button in navigation
- Section Divider Arc: Organic curve separator between sections
- Navigation Bar: Top-level site navigation
- Body Text Block: Paragraph content
- Heading with Underline Accent: Section heading with decorative element
- Image Frame: Photographic or illustrative content container

Do:

- Use the Aurora Lilac Deep Iris gradient (135deg) as the full-bleed background for hero sections, section transitions, and atmospheric dividers - never as a small accent or button fill.
- Set all display text at 47px with IvarHeadline Medium (serif) or Matter Medium/SemiBold (sans) with tracking between -0.015em and -0.025em - never set display copy at body sizes with display weight.
- Apply tabular numerals ('tnum') via font-feature-settings on all Matter text - it signals precision and is a non-negotiable brand mark.
- Use 0px border-radius on all components - cards, buttons, tags, frames. The sharp-cornered geometry is core to the system; rounding would undermine the architectural feel.
- Pair white text (#ffffff) on gradient/violet backgrounds, and Midnight Ink (#000000) on white surfaces - never use gray text on white for primary content.
- Use hairline borders (1px) in white on dark surfaces and Midnight Ink or Smoke Line (#cccccc) on light surfaces for structural framing.
- Maintain a 6px base unit for all spacing - derive all padding, margins, and gaps as multiples (12px, 18px, 23px, 36px).

Avoid:

- Don't introduce additional colors to the palette - the system is achromatic + violet gradient. No green, blue, red, or warm accents outside the gradient.
- Don't use border-radius greater than 0px on any component - no rounded buttons, no pill tags, no curved cards. The sharp geometry is intentional.
- Don't set headings at weights above 600 (SemiBold) - the system relies on the Medium-to-SemiBold tier, not heavy/black weights.
- Don't apply drop shadows or elevation effects - the design uses flat surfaces with hairline borders for separation, never shadows.
- Don't use the gradient on small UI elements (buttons, badges, icons) - it belongs only on large atmospheric surfaces.
- Don't set body text below 14px or above 18px - the 14-18px range is the only readable zone for this system.
- Don't mix serif and sans within the same heading - choose IvarHeadline OR Matter for any single headline, not both.

Source prompt cues:

**Quick Color Reference**
- Text: #000000 (Midnight Ink)
- Background: #ffffff (Frost White)
- Border: #cccccc (Smoke Line)
- Accent: #7c4fb8 (Deep Iris)
- Gradient field: #b9a3e8 (Aurora Lilac) with linear-gradient(135deg, #c5b0ec 0%, #a78bdb 45%, #7c4fb8 100%)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Section**: Full-bleed background with linear-gradient(135deg, #c5b0ec 0%, #a78bdb 45%, #7c4fb8 100%). Centered bordered frame: 1px white border, transparent fill, 0px radius, 14px 23px padding, containing 'Tripolis-ParkTM' at 27px Matter Regular weight 400 in #ffffff. Below: tagline at 18px Matter Regular in #ffffff, line-height 1.25. Section min-height 100vh, flexbox centered.

2. **Display Heading on White**: 'A window to new technology' at 47px IvarHeadline Medium, line-height 1.08, letter-spacing -0.7px, color #000000. 23px margin-bottom. Followed by body text at 14px Matter Regular, line-height 1.20, color #2d2d2d, max-width 65ch.

3. **Ghost Navigation Button**: Transparent background, 1px solid #000000 border, 0px radius, padding 5px 14px, text at 14px Matter Regular in #000000. On hover: border remains 1px but color shifts to #808080 - no fill change.

4. **Content Card on White**: Background #ffffff, 0px radius, 1px solid #e2e2e2 border, padding 23px. Heading at 27px Matter Medium in #000000 with -0.025em tracking. Body at 14px Matter Regular in #2d2d2d. No shadow.

5. **Gradient Section Divider**: Full-width 200px tall section with the Aurora Lilac Deep Iris gradient. Overlay a large curved SVG arc in a lighter variant of the gradient. Content: 47px IvarHeadline Medium in #ffffff, line-height 1.08, letter-spacing -0.7px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
