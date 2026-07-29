# AI Implementation Prompt

Build a The1-inspired interface using this source-derived style bundle.

Reference site: https://the1.amsterdam
Theme: light
Category: Other
North star: building-scale typography on painted concrete

Use these palette anchors:

- The Green `#027b49` for Full-bleed identity block for The Green property and any place or section it owns - deep forest green reads as architectural paint, not decoration
- The Pink `#f19ec8` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content
- The Red `#fa4d43` for Full-bleed identity block and dramatic section background - vermillion red carries the most visual weight and anchors expanded menu states and signature moments
- The Yellow `#fbb833` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content
- Concrete `#d9d9d9` for Page canvas and primary surface - the light gray ground every screen sits on, treated as a material (concrete, drywall) rather than a neutral
- Iron `#1f1f1f` for Primary text, pill button fills, and most structural borders - near-black rather than pure black, softer on the concrete canvas while keeping max contrast
- Carbon `#000000` for Hairline borders, icon strokes, and occasional deep accents where maximum bite is needed against the colored blocks

Use these typography anchors:

- KH Teka `--font-kh-teka` for Primary display and heading face - the entire brand voice. Custom condensed sans set at 215px for the hero with letter-spacing -0.06em and line-height 0.70 so descenders kiss the next line and the word reads as a single architectural mass. Same family drops to 60px and 26px for sub-moments and 15-18px for in-line labels, always retaining negative tracking. This single family does every visible word on the site.
- System sans-serif `--font-system-sans-serif` for Utility micro-copy only - availability text, small annotations, fine print. Used sparingly so KH Teka remains the brand voice.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1440px.
- Section gap: 40px.
- Card padding: 0px.
- Element gap: 10px.

Build these component patterns where relevant:

- Pill Button: Primary interactive control for 'Learn more' and 'Contact us' - the only button pattern on the site
- Hamburger Menu Trigger: Top-right menu opener on every page
- Property Identity Card: Full-bleed color-bloc card introducing each property (The Green, The Pink, The Yellow, The Red)
- Status Dot: Wayfinding marker next to each property name
- Hairline Section Divider: Structural break between major page sections
- Display Headline: Hero and section-anchor type - the signature visual element
- Brand Wordmark: Persistent top-left identity mark
- Expanded Menu Panel: Full-viewport overlay when the hamburger is activated
- Inline Text Link: Quiet navigational link in header and card footers
- In-Text CTA Pair: Header pattern: a question phrase followed by a pill button

Do:

- Set every headline in KH Teka weight 400 with letter-spacing -0.06em at 60px and above, -0.03em at 60px and below; the negative tracking is the brand voice
- Use line-height 0.70-0.80 on display type (60px+) so descenders of one line touch the ascenders of the next - the type forms a wall, not a paragraph
- Reserve the four chromatic colors (#027b49, #f19ec8, #fa4d43, #fbb833) as full-bleed identity blocks for properties or named places; never use them for inline accents, icons, or text
- Use #1f1f1f near-black for all body text, borders, and pill-button fills rather than pure #000000; the softer black feels of-a-piece with the concrete canvas
- Let the four brand colors sit edge-to-edge with no card padding, no border, and no shadow - the color block is the component
- Pair every dark Pill Button (border-radius 100px, fill #1f1f1f) with a leading text question in the same line, so the button reads as an answer not an action
- Use 8-10px colored dots in the property's identity color as inline wayfinding marks next to its name

Avoid:

- Do not assign the four chromatic colors to statuses (success/error/warning/info) - they are a fixed identity set, not a semantic palette
- Do not add box-shadows, gradients, or any elevation to cards, buttons, or images - the system is ruthlessly flat
- Do not introduce a second display typeface; KH Teka is the only voice and must own every visible word
- Do not round card corners - properties and sections are full-bleed rectangles; rounding is reserved exclusively for pills (100px) and the hamburger circle
- Do not use a line-height above 1.20 anywhere; display type must be crushed to 0.70-0.80, never relaxed to 1.4-1.6 'for readability'
- Do not use #027b49, #f19ec8, #fa4d43, or #fbb833 for body text, fine print, or button fills - they are surface colors, not content colors
- Do not wrap the hero display type in a max-width container that breaks it across lines naturally; let the headline run full-bleed and break on its own terms

Source prompt cues:

**Quick Color Reference**
- text: #1f1f1f
- background: #d9d9d9
- border: #1f1f1f
- accent: #fa4d43 (and the three siblings #027b49, #f19ec8, #fbb833 - one per property, never generic)
- pill button fill: #1f1f1f
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build a hero section on a #d9d9d9 concrete canvas. Place a display headline in KH Teka weight 400 at 215px, line-height 0.70, letter-spacing -0.06em, color #1f1f1f. The headline should fill nearly the full canvas width and break across two or three lines naturally. Add a small 'THE1' wordmark in KH Teka 26px top-left and a 48px #1f1f1f solid-circle hamburger top-right.

2. Build a property card with zero border-radius, full-bleed fill #027b49 (The Green). Inset a contained architectural photograph in the top two-thirds. Below: property name 'The Green' in KH Teka 26px #1f1f1f, followed by an 8px solid #027b49 status dot, then availability copy in KH Teka 15px #1f1f1f.

3. Build a header pattern: 'Are you the one?' in KH Teka 18px #1f1f1f, immediately followed by a pill button with border-radius 100px, background #1f1f1f, text 'Contact us' in #d9d9d9 at KH Teka 15px, padding 10px 20px. The text question and pill sit on the same baseline as a single conversational unit.

4. Build an expanded menu state: full-viewport #fa4d43 surface. A massive near-black '1' numeral in KH Teka 215px weight 400 is cropped at the left edge of the red field, acting as a graphic mark. A hairline #1f1f1f header bar sits above the red field with the wordmark and a close affordance.

5. Build a section divider: a single 1px solid #1f1f1f horizontal line spanning the full content width with zero padding above or below - the line itself is the break.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
