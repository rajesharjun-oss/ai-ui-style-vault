# AI Implementation Prompt

Build a Valo-inspired interface using this source-derived style bundle.

Reference site: https://www.valohealth.com
Theme: dark
Category: AI
North star: noir observatory at midnight - weight-300 typography floats on pure black while a single teal-violet gradient passes through like a laser line across the room.

Use these palette anchors:

- Void `#000000` for Page canvas, hero background, all primary surface area. Sets the dark-stage tone for every screen
- Bone `#e5e7eb` for Hairline borders, dividers, and muted secondary text. The workhorse neutral that defines edges without adding visual weight
- Paper `#ffffff` for Primary headings, body text, nav links, and icon strokes. Maximum contrast against Void for clear information hierarchy
- Graphite `#4d4d4d` for Subtle nav borders and disabled/inactive state lines. Sits between Void and Bone for low-emphasis structural lines

Use these typography anchors:

- Valo `--font-valo` for Exclusive typeface across all UI: nav links, body copy, section labels, and display headlines. Weight 300 carries headlines and body - the anti-convention whisper-weight creates scientific authority through restraint. Weight 700 is reserved for micro-labels and the few moments that need to anchor a page. The custom cut of this single family is the brand voice.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 45px.
- Card padding: .
- Element gap: 18-20px.

Build these component patterns where relevant:

- Top Navigation Bar: Global site navigation anchored to top of every page
- Hero Display Headline: Opening page-level statement, left-aligned on dark canvas
- Hero Subhead Paragraph: Supporting description under the display headline
- Section Label Tag: Micro-category label introducing each major content section
- Gradient Torus Visual: Decorative conceptual illustration representing the feedback loop of drug discovery
- Numbered Content Block: Sequential feature/item layout with index number and description
- Circle Arrow Link Button: Inline call-to-action for secondary navigation ("Explore our approach", "Join our team")
- Content Section Heading: Mid-page section title introducing a new content block
- Gradient Footer Band: Atmospheric closing zone with site links and copyright
- Hairline Section Divider: Vertical separation between content sections

Do:

- Set all display and body text in Valo weight 300 - the whisper-weight is the brand voice, not a fallback
- Apply the Spectrum Wash gradient to exactly one word per headline maximum - chromatic type is punctuation, not paint
- Use 9999px radius for every interactive element (buttons, link icons, tags) - circles are the only geometric interaction shape in the system
- Set display headlines at -2.7px letter-spacing (100px) and -0.78px (60px) - the negative tracking tightens large type to feel carved rather than typed
- Use 0.1em letter-spacing on all small-caps labels, nav items, and numbered prefixes - the wide tracking signals scientific precision
- Anchor every section with the uppercase Section Label Tag at 10px - the typographic flag gives pages a magazine-like structure
- Use the 01, 02 numbered pattern for sequential content blocks - sequencing reads as methodical, fitting the discovery narrative

Avoid:

- Don't use weight 700 for body copy or long-form paragraphs - the voice is light; 700 belongs to subheadings and micro-labels only
- Don't apply the Spectrum Wash gradient to button backgrounds, panel fills, or large-area surfaces - it belongs on text accents, ring strokes, and the footer band only
- Don't introduce card surfaces, drop shadows, or elevated panels - the canvas stays flat; depth comes from type scale, not from z-axis
- Don't use borders thicker than 1px - the entire system runs on hairlines (Bone at 1px); anything heavier breaks the editorial register
- Don't add a chromatic brand color outside the violet blue teal lavender ramp - the system is intentionally near-monochrome with one gradient family
- Don't center body text or multi-line content - the layout is left-aligned and the measure should align with the headline edge
- Don't use stock photography, emoji, or decorative illustration - visuals are limited to the gradient torus and the footer wash; everything else is type and whitespace

Source prompt cues:

**Quick Color Reference**
- text: #ffffff (Paper)
- background: #000000 (Void)
- border: #e5e7eb (Bone), 1px
- accent gradient: linear-gradient(270deg, rgb(158,61,178), rgb(27,102,248), rgb(36,218,217), rgb(179,198,232))
- footer gradient: linear-gradient(90deg, rgb(30,35,60), rgb(10,64,153)) transitioning to the teal-mint wash
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a hero section on #000000. Headline at 100px Valo weight 300, #ffffff, line-height 1.0, letter-spacing -2.7px. Render the single word "aha" inline using the Spectrum Wash gradient as the text color. Below: 15px Valo weight 400, #e5e7eb, line-height 1.63, max-width matching the headline measure. No buttons, no images.

2. Build a paired text-and-visual section. Left: a 400px-diameter thin ring (2px stroke) filled with the Spectrum Wash gradient as stroke color, centered vertically. Right: a 38px Valo weight 300 #ffffff section heading at line-height 1.2, followed by a 15px #e5e7eb intro paragraph, then a numbered list (01, 02) at 13px #e5e7eb numerals (0.1em tracking) paired with 18px weight 700 #ffffff subheadings and 15px weight 400 #e5e7eb bodies. Close with a 48px circular ghost button (1px #e5e7eb border, white arrow icon) paired with an 18px #ffffff text link.

3. Build a full-bleed footer band. Background: linear-gradient(90deg, #1e233c, #0a4099) blending into a teal-violet wash. Left: 24px Valo weight 400 #ffffff wordmark. Right: a row of 13px Valo weight 400 #ffffff links at 20px gaps (Privacy Policy, Terms, Cookie Consent, Preferences, Twitter, LinkedIn, (C) 2026 Valo Health). No top border - the gradient defines the zone.

4. Build a section label. 10px Valo weight 400 #ffffff, uppercase, letter-spacing 1.0px. Place 36px above its parent content block. No background, no border.

5. Build a top navigation bar. Background: #000000 (transparent over canvas). Left: 24px Valo weight 400 #ffffff "Valo" wordmark. Right: 5 nav items at 13px Valo weight 400 #ffffff with 27px horizontal gaps and 7px top/bottom padding. No background fill, no border-bottom.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
