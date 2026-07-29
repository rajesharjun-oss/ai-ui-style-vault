# AI Implementation Prompt

Build a Intra-inspired interface using this source-derived style bundle.

Reference site: https://intracbr.com.au
Theme: light
Category: Other
North star: white-walled gallery placard with one giant black eye

Use these palette anchors:

- Paper White `#ffffff` for Page canvas, card surfaces, type knocked out of black panels
- Ink Black `#212529` for Primary text, bold panels, the dominant non-white surface - carries a barely-perceptible cool tint that softens it from pure #000
- Pure Black `#000000` for Button strokes, logo fill, and the heaviest typographic moments where absolute zero contrast is required
- Hairline Gray `#e4e4e4` for Dividers, card borders, image outlines, table rules - the only mid-tone in the system

Use these typography anchors:

- Whyte `--font-whyte` for Single-weight type system. 95px display headlines for the wordmark and section titles carry the brand's editorial weight; 18-20px reads as body and meta; 16px as captions and link lists. The single weight (400) at all sizes is a signature choice - no bold, no light, the hierarchy is built through SIZE, not stroke. Substitute with Inter, Sohne, or Neue Haas Grotesk.
- -apple-system `--font-apple-system` for System fallback for environments where Whyte is unavailable; inherits macOS/iOS native rhythm. Use only as the last-resort stack, not the primary voice.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 100px.
- Card padding: 40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Eye Logo Lockup: Primary brand mark - the most identifiable asset on the site
- Display Wordmark Section: Editorial section header - replaces what a colored banner or card would do on a conventional site
- Body Text Block: Long-form copy describing the venue, menu philosophy, hours
- Hairline Divider: Section separation
- Product Card (Coffee Bag): Showcase tile for available single-origin beans
- Outlined Action Button: Navigation and call-to-action control
- Editorial Photo Block: Documentary imagery of the venue and team
- Metadata Row: Hours, locations, and structured information
- Link List (Footer/Info): Secondary navigation and contact links
- Black Panel Block: Inverse section - the only large dark surface on the site

Do:

- Use 95px Whyte weight 400 as the only display size - never split into bold/regular variants, let the SIZE carry hierarchy.
- Hold the page to four colors total: #ffffff canvas, #212529 ink, #000000 for the heaviest moments, #e4e4e4 hairlines.
- Use 0px border-radius on every component - cards, buttons, images, tags. Sharp corners are the brand.
- Set section padding to 100px top and bottom, with 50px horizontal gutters - the breathing room IS the layout.
- Let product photography supply color: when a colored element is needed, use a real product image rather than introducing a new brand color.
- Use 1px outlined buttons with 6px horizontal / 1px vertical padding - the bar should feel like a typographic underline, not a conventional CTA.
- Keep the body line-height at 1.50 and the display line-height at 1.00 - never let the giant headlines feel airy.

Avoid:

- Don't introduce a chromatic accent color for buttons, links, badges, or icons - there is no brand color in this system, the packaging supplies the only saturation.
- Don't use drop shadows, gradients, or blur effects - surfaces are flat, defined only by hairline borders.
- Don't use rounded corners anywhere, even on tags or avatars - everything is a sharp rectangle.
- Don't use bold (weight 600+) or light (weight 300) cuts of Whyte - weight 400 is the only voice, all hierarchy is typographic scale.
- Don't add icons, emojis, or decorative glyphs to the UI - the eye mark and the wordmark are the only marks.
- Don't split the giant wordmark into multiple lines or hyphenate it - "CAFE", "HOURS", "INTRA" each occupy one line at 95px.
- Don't apply a hover color change to links - the underline is the affordance, not a color shift.

Source prompt cues:

Quick Color Reference:
- text: #212529
- background: #ffffff
- border/hairline: #e4e4e4
- accent: #000000 (logo fill, button strokes)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create an editorial hero: full-bleed #ffffff canvas. Centered or left-aligned display wordmark "CAFE" at 95px Whyte weight 400, line-height 1.0, color #212529. 100px top and bottom padding. No background panel, no button, no subhead - the word IS the section.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

3. Create a metadata/hours row: two-column or stacked list. Labels in 16px Whyte weight 400 color #212529, values in 16px Whyte weight 400 color #212529, 15px vertical padding between rows. No icons, no dividers, no color coding.

4. Create an outlined navigation button: 1px #000000 border, 0px radius, 6px horizontal padding x 1px vertical padding. Text "BUY IN-STORE" at 16-20px Whyte weight 400 color #000000. Sits in the top bar, uppercase or title case, no fill, no shadow.

5. Create a black inverse panel: full-width #212529 background, 100px vertical padding. White (#ffffff) 95px display text centered or left-aligned, line-height 1.0. Use to punctuate the page and provide a visual counterweight to the white canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
