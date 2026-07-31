# AI Implementation Prompt

Build a Metalab-inspired interface using this source-derived style bundle.

Reference site: https://metalab.com
Theme: dark
Category: Agency
North star: black editorial spread - a serif headline breathing in void, annotated by a whisper-quiet grotesque

Use these palette anchors:

- Void `#000000` for Page canvas, primary surface, heading text on light zones - the dominant black that absorbs all surrounding elements
- Bone `#ffffff` for Inverse text on dark surfaces, hairline borders on dark zones, contrast punctuation against the black canvas
- Charcoal `#252525` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color

Use these typography anchors:

- Basis Grotesque Pro `--font-basis-grotesque-pro` for All functional copy: body text, metadata annotations, labels, nav, buttons, lists. The 350 weight (light) handles editorial captioning at 12px - the small annotations like 'EST 2006', 'BC, CA', '12:32 EDT' - while 400 handles body and interactive text at 16px. Slight -0.01em tracking tightens the grotesque into a precise, measured voice. This font does the quiet work; the serif does the talking.
- PP Eiko `--font-pp-eiko` for Display headings only - the 88px ultra-light serif is the signature element. Weight 240 (near-hairline) is a dramatic anti-convention choice: most agencies use 400-500 serifs for authority; Metalab's whisper-weight communicates confidence through restraint, not volume. Tight 0.80 line-height and -0.02em tracking let letters nearly touch, creating a sculptural block of text.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 96px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Dark Elevated Panel: Hero or feature surface - the single depth element in the system
- Pill Toggle: Interactive state indicator or count badge
- Metadata Annotation: Editorial marginalia - dates, locations, timestamps
- Display Headline: Primary heading - sets the editorial tone
- Ghost Button: Subtle interactive element on dark surfaces
- Nav Link: Top-level navigation - minimal, text-only
- Body Copy: Descriptive and supporting text
- List Item: Structured content listing

Do:

- Use PP Eiko at 88px weight 240 exclusively for the largest display moments - never at body sizes where the hairline weight becomes illegible
- Set all display headlines to line-height 0.80 and letter-spacing -0.02em to achieve the sculptural, near-touching letterforms
- Use Basis Grotesque Pro weight 350 at 12px for all metadata annotations (dates, locations, timestamps) - this is the system's editorial signature
- Build depth through a single #252525 surface layer over the #000000 canvas - do not introduce additional grays or shadows
- Apply border-radius 50px to all buttons and elevated panels for the soft, tablet-like silhouette that defines the system
- Anchor all dark pages on the #000000 canvas with #ffffff typography - never invert to a white page background within a dark-theme design
- Use line-height 1.76-2.00 for body copy to match the editorial spaciousness of the display type

Avoid:

- Do not introduce any chromatic color - no blues, reds, greens, or brand accents. The system is achromatic by conviction
- Do not use PP Eiko at sizes below 40px - the weight 240 becomes too thin to render reliably at small sizes
- Do not add drop shadows to any element - depth in this system comes from surface value contrast (#000000 #252525), not elevation effects
- Do not use weight 600+ for any text - the entire system operates in the 240-400 range; heavier weights break the whisper-quiet tone
- Do not add gradients, glows, or any color effects - the flat achromatic palette is the brand identity
- Do not use system serif defaults (Times, Georgia) as substitutes for PP Eiko without matching the ultra-light weight - a regular-weight serif will read as conservative, not editorial
- Do not fill buttons with #ffffff on the dark canvas - it would create the only bright shape on the page and dominate the hierarchy. Use #252525 or transparent

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #000000
- border: #ffffff
- accent: no accent color (achromatic system)
- primary action: no distinct CTA color
- surface elevation: #252525

**Example Component Prompts**

1. Create a hero section: #000000 background, full-bleed. Left-aligned 88px PP Eiko weight 240 headline in #ffffff, line-height 0.80, letter-spacing -0.02em reading 'We Make Interfaces'. Center column: a #252525 rounded panel, border-radius 50px, roughly 380px wide by 500px tall. Right margin: floating 12px Basis Grotesque Pro weight 350 annotations in #ffffff ('EST 2006', '12:32 EDT').

2. Create a navigation bar: minimal text row on #000000 background. 16px Basis Grotesque Pro weight 400 in #ffffff, items left-aligned with 24px gaps, no background fill, no border.

3. Create a ghost button: transparent background on #000000 canvas, #ffffff text at 16px Basis Grotesque Pro weight 400, border-radius 50px, padding 16px horizontal / 8px vertical. No border, no shadow.

4. Create a metadata label: 12px Basis Grotesque Pro weight 350 in #ffffff, positioned as a small floating annotation in the margin of a content layout. No background, no border - just typographic presence.

5. Create a dark elevated card: #252525 fill on #000000 canvas, border-radius 50px, padding 24px. No shadow, no border. Body text inside in #ffffff at 16px Basis Grotesque Pro weight 400, line-height 1.76.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
