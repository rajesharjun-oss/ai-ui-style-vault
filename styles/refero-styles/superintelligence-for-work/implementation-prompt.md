# AI Implementation Prompt

Build a Superintelligence for work-inspired interface using this source-derived style bundle.

Reference site: https://sanalabs.com
Theme: light
Category: AI
North star: Architectural monograph on vellum - where the only ornament is letter-spacing and the only color is a single electric blue pressed into white space.

Use these palette anchors:

- Ink `#090909` for Primary text, hairlines, card and input borders, list dividers, link underlines - the dominant dark anchor of the system
- Pure Black `#000000` for Icon fills, heading underlines, occasional deep accents where maximum weight is needed
- Bone `#ffffff` for Page background, card surface, text on filled buttons, button borders for ghost controls
- Linen `#efefed` for Section band background, elevated card surface, the warm neutral that gives the white space its temperature
- Ash `#d9d9d9` for Footer divider, hairline rules where Ink would be too heavy
- Cobalt Pulse `#0057f3` for Single primary action fill per page - the only chromatic punctuation, reserved for the decisive CTA and never used decoratively
- Ember Signal `#ff5102` for Rare secondary action or notification accent - a warm counterpoint to Cobalt Pulse, used at most once per surface

Use these typography anchors:

- Sana Sans `--font-sana-sans` for Sole typeface across the entire system - display headlines at 83px set weight 500 with -2.5% tracking for a carved, architectural feel; section headings at 48px weight 500 with -0.96px tracking; body copy at 15-16px weight 400 with barely-perceptible negative tracking. The font is geometric and humanist, and the refusal to go above weight 500 is deliberate: confidence comes from restraint, not boldness.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 16-24px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Primary CTA Button: The single decisive action on any page
- Ghost Navigation Button: Secondary action in the header
- Pill Notification Toast: Persistent status banner (e.g. acquisition announcement)
- Top Navigation Bar: Primary site navigation
- Brand Logo Strip: Social proof via customer logos
- Feature Pill Item: Sub-feature below a product section header
- Section Header Block: Centered title and subtitle for each product section
- Editorial Product Showcase: Full-bleed photographic still-life that presents a product screenshot in a real-world context
- Testimonial Video Card: Full-bleed video preview with quote overlay
- Card with Soft Radius: Elevated content blocks (pricing, features, content tiles)
- Footer: Site-wide footer with links and legal

Do:

- Use Sana Sans weight 500 for all headings and never exceed weight 500 - confidence comes from size and tracking, not boldness
- Set display headlines at 83px with -2.49px letter-spacing so the type reads as carved, not rendered
- Reserve Cobalt Pulse #0057f3 for exactly one filled CTA per visible surface; every other button stays ghost or neutral
- Use Linen #efefed bands to separate sections instead of borders, shadows, or dividers
- Make all buttons pill-shaped with 32-36px radius - angular buttons break the editorial language
- Default to 4px multiples for all spacing; element gap 8-16px, card padding 16-24px, section gap 80-120px
- Set body copy at 15-16px with line-height 1.4-1.6 in Sana Sans weight 400

Avoid:

- Don't add box-shadow to any component - depth comes from surface color shifts, not elevation
- Don't use Cobalt Pulse decoratively on icons, illustrations, tags, or backgrounds - it is a CTA color only
- Don't introduce gradients - the system is built on flat, single-value surfaces
- Don't go above weight 500 in the type scale; bold/700 breaks the restrained voice
- Don't use #0000ee or any unstyled link blue - links inherit Ink #090909
- Don't add corner radii smaller than 6px or use sharp 0px corners on content blocks
- Don't place colored backgrounds under text - every text surface is white, linen, or photographic

Source prompt cues:

**Quick Color Reference**
- text: #090909
- background: #ffffff
- band surface: #efefed
- border / hairline: #090909 (at 1px) or #d9d9d9 (footer)
- accent: #0057f3
- primary action: #000000 (filled action)
- rare accent: #ff5102 (use sparingly)

**3-5 Example Component Prompts**

1. *Build a hero section*: White #ffffff background, full viewport height, max-width 1200px centered. Headline at 83px Sana Sans weight 500, color #090909, letter-spacing -2.49px, line-height 0.95, centered. Subtext at 16px weight 400, #090909, max-width 560px, centered, 16px below headline.

2. Create a Primary Action Button: #000000 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. *Build a ghost nav button*: Pill shape, 32px radius, 1px solid #090909 border, white #ffffff background, text 'Book an intro' at 14px Sana Sans weight 500 in #090909, padding 8px 16px. No shadow.

4. *Build a testimonial video card*: Full-bleed edge-to-edge photographic background (portrait of a person, warm tones). Overlaid left-aligned at ~120px from left edge: small white Spotify logo, then 32-40px quote text in white Sana Sans weight 500, then 14-15px attribution in white weight 400. Below attribution, a ghost button with 1px white border, white text 'Watch video', 32px radius, padding 8px 16px.

5. *Build a content card*: 16px corner radius, white #ffffff background, no shadow, padding 24px. Sits on a #efefed Linen band. Title 16px weight 500 #090909, body 14px weight 400 #090909, 8px gap between title and body.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
