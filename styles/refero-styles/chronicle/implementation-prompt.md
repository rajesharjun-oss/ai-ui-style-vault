# AI Implementation Prompt

Build a Chronicle-inspired interface using this source-derived style bundle.

Reference site: https://chroniclehq.com
Theme: light
Category: SaaS
North star: Typographer's proof sheet - a composited page where precision of letterform carries the entire visual weight, color is an intrusion, and the grid is the design.

Use these palette anchors:

- Pitch Black `#050505` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Midnight `#000000` for Filled action button backgrounds (Try Chronicle, Talk to sales, Try for free); icon fills; strongest contrast anchor
- Charcoal `#151515` for Navigation link text and active nav states
- Obsidian `#292929` for Footer fine print and copyright text
- Graphite `#6b6b6b` for Body text, UI borders, ghost button borders and text - the workhorse mid-tone
- Pewter `#7e7e7e` for Secondary body copy and captions
- Ash `#929292` for Disabled or inactive button text and borders
- Silver `#b3b3b3` for Subtle background dividers and muted separators
- Fog `#e2e2e2` for Card borders, image borders, input borders - the hairline rule color
- Limestone `#f3f3f3` for Alternating section backgrounds, testimonial section canvas, muted surface fills
- Cloud `#ffffff` for Primary page canvas, card surfaces, link text on filled black buttons

Use these typography anchors:

- Diatype `--font-diatype` for Single typeface for the entire system - headings, body, nav, buttons. Weight 400 for body and secondary text; weight 500 for prominent headings and CTAs. Negative tracking of -0.03em at display sizes creates mechanical compression uncommon in SaaS type - the letterforms feel pressed into the page rather than set on it. No serif, no decorative fallback: if Diatype is absent, the design loses its primary identity marker.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1212px.
- Section gap: 80-128px.
- Card padding: 24-30px.
- Element gap: 8px.

Build these component patterns where relevant:

- Filled Black CTA Button: Primary call-to-action - 'Try for free', 'Try Chronicle'
- Ghost Underline Button: Secondary text action - 'Watch video', tab-style navigation items
- Muted Ghost Button: Inactive or de-emphasized action
- Pill Tab Button: Horizontal tab navigation - presentation type selectors (Sales proposal, Pitch deck, etc.)
- Testimonial Card: Social proof - customer quote with logo, name, role
- Product Preview Frame: In-page presentation screenshot / app preview
- Logo Trust Bar: Social proof partner / customer logos
- Navigation Bar: Primary site header
- Section Divider Tab Row: Tabbed content switcher above the hero product preview
- AI Prompt Input Card: Product UI element - chat/prompt card visible in feature section

Do:

- Use #000000 or #050505 as the filled button background - never use a chromatic color for any interactive element
- Apply Diatype with letter-spacing -0.030em at 54px display and -0.023em at 32px headings; body text at 16px uses 0 tracking
- Alternate page sections between #ffffff and #f3f3f3 backgrounds to create rhythm without decorative elements
- Use 4px border-radius for all buttons, inputs, and tags; 8px for cards and image frames only
- Maintain 1px solid #e2e2e2 hairline borders on image frames and card edges - never use thicker strokes
- Reserve electric blue and any chromatic color strictly for rendered product UI content inside frames, never in navigation, buttons, or backgrounds
- Use the single shadow token (rgba(5,5,5,0.08) 0px 2px 24px 0px) only for white cards sitting on gray surfaces - no shadow on white-on-white

Avoid:

- Never introduce a brand color (blue, purple, green) into navigation, buttons, section backgrounds, or typography - the UI is intentionally achromatic
- Never round buttons or inputs beyond 4px - pill-shaped buttons would break the editorial typographic register
- Never use font weights above 500 - Diatype at 400/500 is the full weight range; heavier weights crush the mechanical letterform quality
- Never stack more than two type sizes within a single content block without re-establishing hierarchy through #6b6b6b muted color rather than additional size steps
- Never apply more than one shadow elevation level - the system uses a single subtle card shadow; adding layered shadows introduces unwanted depth
- Never center-align body paragraphs or subheadings - all text below headline level is left-aligned
- Never use #b3b3b3 or #929292 as text colors for meaningful content - these tones exist only for disabled states and decorative separators

Source prompt cues:

**Quick Color Reference**
- text (primary): #050505
- text (secondary): #6b6b6b
- background (canvas): #ffffff
- background (tinted section): #f3f3f3
- border: #e2e2e2
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Section**: White (#ffffff) background, max-width 1212px. Left column: headline Diatype 54px weight 500, #050505, letter-spacing -1.62px, line-height 1.00. Subheading body 16px weight 400, #6b6b6b, line-height 1.40. Two buttons: filled (#000000 bg, #ffffff text, Diatype 14px weight 500, 4px radius, 10px/24px padding) and ghost underline (transparent bg, rgba(0,0,0,0.56) text and border, no radius, 10px vertical padding). Right column: product preview in a #e2e2e2 bordered 8px radius frame.

2. **Testimonial Card**: Background #ffffff, 8px border-radius, shadow rgba(5,5,5,0.08) 0px 2px 24px 0px, 24px internal padding. Top: company name Diatype 14px weight 500 #050505 with small icon left. Middle: quote text 16px weight 400 #050505 line-height 1.40. Bottom: circular photo 32px, name 14px weight 500 #050505, role 12px #6b6b6b.

3. **Navigation Bar**: White background, height 54px, 24px horizontal padding, max-width 1212px centered. Logo left (Diatype 14px weight 500 #050505 + diamond icon). Center nav links: Diatype 14px weight 400 #151515, 24px column gap. Right: 'Login' ghost text (#151515, no border, no bg) + 'Try for free' filled black button (4px radius, 10px/16px padding, #ffffff text).

4. **Tab Row**: Horizontal flex row, 8px gap. Each tab: Diatype 14px weight 400, inactive rgba(0,0,0,0.4), active #050505 with 1px bottom border #050505. No background, no border-radius, 10px vertical padding, 0 horizontal padding.

5. **Feature Section (Split Layout)**: #f3f3f3 background band, 80px vertical padding, 1212px max-width. Left 50%: product screenshot or photo with 8px radius and #e2e2e2 1px border. Right 50%: stacked text list - items at Diatype 20px weight 500 #050505 (active) and 20px weight 400 #6b6b6b (inactive). Body description 16px weight 400 #6b6b6b line-height 1.40 below active item.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
