# AI Implementation Prompt

Build a Charlie Phipps-inspired interface using this source-derived style bundle.

Reference site: https://phippscharlie.com
Theme: mixed
Category: Design
North star: oversized editorial gallery wall - a single massive Helvetica headline and one full-bleed photograph, nothing else

Use these palette anchors:

- Canvas Black `#101011` for Base page canvas beneath full-bleed photography and dark bands; primary text on light surfaces; link underlines in dark contexts
- Paper White `#ffffff` for Primary text color on dark/photographic backgrounds; content section background; dominant border color (hairline rules and dividers across the layout)
- Ink Black `#000000` for Heading and body text on light surfaces; second structural border color - used wherever a slightly harder edge than #101011 is needed
- Fog Gray `#ededed` for Subtle surface tint separating content blocks from white paper; soft borders on body text and cards where a pure white hairline would disappear
- Smoke Gray `#bab7b2` for Muted heading accent - used for secondary headings and borders where the hierarchy needs to recede below the primary type
- Ash Gray `#888888` for Body text metadata, link underlines in light contexts, and mid-weight borders - the workhorse neutral for anything that should be seen but not foregrounded
- Charcoal `#262627` for Deepest secondary border and muted text on light sections - just one step lighter than canvas black, used to keep dark elements feeling part of the same family
- Void `#080809` for Near-pure black for the darkest link borders and emphasis text - visually indistinguishable from #000000 but kept distinct in the scale for deepest emphasis

Use these typography anchors:

- Helvetica Neue `--font-helvetica-neue` for The entire typographic system. Weight 400 at 162px is the signature move - most portfolios would use 700-900 for a hero this large; Phipps uses regular, letting the sheer size and aggressive negative tracking carry authority instead of stroke weight. LineHeight of 0.90 on the display size means the two-line hero actually visually interlocks. All other text (body, labels, navigation, links) is the same family at the same weight - there is no secondary typeface voice.
- Times `--font-times` for Used only as 13px image captions or photo metadata - the serif appears as a deliberate editorial counterpoint to the Helvetica system, breaking the all-grotesque monotony at micro scale

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 80px.
- Card padding: 13px.
- Element gap: 26px.

Build these component patterns where relevant:

- Full-Bleed Hero Photograph: Opening screen background
- Display Headline: One-line statement over the hero
- Thin Top Navigation: Persistent site chrome
- Section Label (EXPLORE / LATEST WORKS): Small-caps section identifier
- Editorial Section Headline: Large body-section opener
- Body Description Block: Centered contextual paragraph
- Social Link Row: Footer-level external links
- Scroll Indicator: Single down-arrow cue at viewport bottom
- Project Card (case study tile): Image-first work sample in the project index
- Email Contact Link: Bottom-right footer contact

Do:

- Use Helvetica Neue at weight 400 exclusively for the entire interface - never introduce a bold, medium, or light variant; the single-weight system is the signature
- Set the display headline to 162px with lineHeight 0.90 and letter-spacing -3.89px; let the line break where it breaks and allow the viewport to crop the text
- Use the spacing scale of 6 / 13 / 26 / 41px only - no arbitrary in-between values, and reserve 41px for the largest section breaks
- Place full-bleed photography behind text without overlay gradients or darkening scrims - the image's own contrast must carry legibility, or shift the text position to a clean area of the photo
- Keep the color palette 100% achromatic - #101011 canvas, #ffffff text-on-photo, #000000 text-on-paper, and the gray scale for borders and metadata only
- Float navigation at the viewport edge in three positions (left / center / right) using 13-16px text - never box it, border it, or background it
- End editorial section headlines with a period ("Selected works (C)2022.") - the declarative full stop is part of the typographic voice

Avoid:

- Do not introduce any chromatic color - no brand reds, no accent blues, no button fills; the photograph is the only color source
- Do not add border-radius to any element - keep all corners at 0px; rounded corners would break the printed-poster logic
- Do not use box-shadows, drop-shadows, or any elevation effects - the design is flat against the photographic plane by intent
- Do not swap the display weight to 700 or 800 in any context - if a heading needs more weight, increase size instead; 400 at scale is the only authority the system allows
- Do not wrap text content in cards, panels, or bordered containers - sections are separated by whitespace alone, never by chrome
- Do not use icons for social links, email, or navigation - text plus the external arrow is the entire icon vocabulary
- Do not use uppercase tracking-wide labels for body copy - only the small section identifiers (EXPLORE, LATEST WORKS) use the stacked-label pattern

Source prompt cues:

**Quick Color Reference**
- text (on white): #000000
- text (on photo/dark): #ffffff
- background (content sections): #ffffff
- background (canvas/beneath photo): #101011
- border / hairline: #ededed (light) or #000000 (emphasis)
- muted text: #888888
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Full-bleed photographic hero** - Start every page with a 100vw x 100vh photograph filling the viewport edge-to-edge. Place a Helvetica Neue 162px / weight 400 / lineHeight 0.90 / letter-spacing -3.89px headline in #ffffff, anchored top-left, allowed to crop off the right viewport edge. Add the brand name in 16px Helvetica Neue 400 at the top-left corner and two more nav links at top-center and top-right. No overlay, no gradient, no scrim - the photograph must be the entire background.

2. **Editorial content opener** - A white (#ffffff) content section, max-width 1400px centered. Left margin holds a stacked label: "EXPLORE" in 16px Helvetica Neue 400 #000000 on line one, "(04)" on line two, "Case Studies" on line three. To the right, a 52px Helvetica Neue 400 #000000 headline with lineHeight 1.00 and letter-spacing -0.62px, ending with a period. Below the headline, a paragraph at 21px / lineHeight 1.2 / #000000, max-width 520px.

3. **Project photograph tile** - A single full-bleed photograph at its native aspect ratio (target 4:3 or 16:9), 0px border-radius, no padding, no border, no shadow, no caption overlay. If a caption is needed, place a 13px Times 400 #000000 string directly below the image with 13px top margin. The image is the entire component - no card surface.

4. **Footer link row** - Three inline text links at 16px Helvetica Neue 400 in #ffffff, separated by 26px horizontal gap. Each link is just the platform or page name (e.g. "Instagram", "LinkedIn", "Email") with a thin arrow appended to external links. No icons, no underlines by default, no buttons. Positioned flush-left or flush-right at the viewport bottom edge with 26px page padding.

5. **Scroll indicator** - A single glyph in 16px Helvetica Neue 400 #ffffff, positioned absolute at bottom-left of the hero viewport. No animation, no label, no border. Disappears after the user scrolls past the first screen.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
