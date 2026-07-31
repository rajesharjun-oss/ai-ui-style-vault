# AI Implementation Prompt

Build a Yellowbird(R)-inspired interface using this source-derived style bundle.

Reference site: https://www.yellowbirdfoods.com
Theme: light
Category: E-commerce
North star: Retro condiment billboard in midday sun - a single yellow plane under a black sun, every letter drawn with a fat marker.

Use these palette anchors:

- Sunglow `#ffe845` for Brand canvas - the dominant page background across all sections, hero, footer, and announcement bar; also fills product category tags and sticker burst shapes
- Sauce Bottle Black `#000000` for Primary text, all borders and hairlines, product card strokes, mascot linework, and the filled primary action button background - does the heavy structural and typographic lifting
- Pure White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Buttermilk `#fbfaf2` for Alternate card surface for quieter product tiles - an off-white that reads as warm cream against the saturated yellow canvas
- Cool Link Blue `#007aff` for Ghost/outlined secondary action border - a borrowed utility color for low-emphasis links, never used for filled buttons or primary navigation

Use these typography anchors:

- Gooper `--font-gooper` for Signature wordmark display - the massive 'Yellowbird' logotype and any oversized display headings; a custom bubbly, ultra-chunky display face that functions as the brand's icon. Tight tracking (-0.028em) keeps the rounded forms from feeling wobbly at 91px
- ABC Monument Grotesk `--font-abc-monument-grotesk` for Primary workhorse - nav links, body copy, product names, section headings, button text, footer, and hero subhead. The single weight (400) carries all roles from 14px caption to 61px hero subhead, unified by negative tracking that tightens as size grows (-0.04em at 14px to -0.011em at 61px)
- Pitch Sans `--font-pitch-sans` for Secondary utility - used for badges, tags, micro-labels, and supporting metadata where a slightly more compact feel is needed. Weight 600 for badge text adds the only weight contrast in the system

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 20px.

Build these component patterns where relevant:

- Announcement Bar: Slim site-wide utility bar above the nav
- Primary Navigation Header: Main site nav anchored to the top of every page
- Hero Wordmark Block: Above-the-fold brand statement replacing a typical headline+subhead+CTA
- Hero Subhead Paragraph: Long-form intro text under the hero wordmark
- Product Card: Primary commerce tile for sauce SKUs in the featured grid
- Product Category Badge: Label tag overlaid on product cards (CLASSIC, ORGANIC, SMALL BATCH)
- Primary Action Button: The single filled CTA - used for SHOP ALL and checkout actions
- Ghost Secondary Action: Outlined secondary button for lower-emphasis links
- Starburst Sticker: Decorative seal/burst shape for callouts and trust signals
- Testimonial Quote Block: Full-width customer quote band
- Section Divider: Horizontal separator between content bands
- Starburst Mascot Mark: Small brand icon used in nav center and testimonial accent

Do:

- Use #ffe845 as the full-bleed canvas for every full-width section - hero, product grids, testimonials, and footer should all sit on yellow, never on white or gray
- Set body and heading copy in Monument Grotesk weight 400 only; the system has no bold weight for this face, so hierarchy comes from size and tracking, not weight
- Use 30px border-radius on all product cards and images; 14px on primary buttons; 6px on category badges - these three radii define the shape language
- Separate sections by color swap (yellow band cream card yellow band), not by shadows or dividers - the design is deliberately flat
- Use the Gooper 91px display face only for the wordmark and equivalent brand statements; never for product names, body, or UI text
- Size all CTAs in Monument Grotesk 18px all caps with -0.011em tracking - consistency in button typography is a signature
- Apply the starburst sticker pattern to exactly one callout per viewport - it loses impact as a repeated motif

Avoid:

- Never introduce a new chromatic color beyond the yellow/black/white/cream/blue set - the system's power is its two-color discipline
- Never add drop shadows, inner glows, or blur effects to cards or buttons - separation comes from solid black strokes, not elevation
- Never use the blue (#007aff) as a filled button background or for navigation; it is a ghost-border utility color only
- Never use a font weight heavier than 400 for Monument Grotesk; the face doesn't ship bold, and faking bold breaks the geometric evenness
- Never place body copy on white over the yellow canvas without a card surface - floating text on white feels broken; always commit to cream or pure white as a card surface
- Never use positive letter-spacing on body or display text - the only positive tracking (0.05em) is reserved for Pitch Sans testimonial attributions
- Never reduce the wordmark below 61px or substitute a standard display face for Gooper; the bubbly custom face is the brand's most recognizable element

Source prompt cues:

**Quick Color Reference**
- Canvas: #ffe845
- Text: #000000
- Card surface: #ffffff
- Alternate card: #fbfaf2
- Border/stroke: #000000
- primary action: #ffe845 (filled action)
- Secondary action: #007aff (outlined ghost border only)

**3-5 Example Component Prompts**

1. **Product Card**: White (#ffffff) background, 1.5px solid #000000 border, 30px border-radius, 24px padding. Centered sauce bottle product image. Category badge overlaid at top-center: #ffe845 fill, 1.5px #000000 border, 6px radius, Pitch Sans 16px weight 600, all caps, #000000. Product name below in Monument Grotesk 27px, #000000, letter-spacing -0.011em.

2. Create a Primary Action Button: #ffe845 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. **Hero Subhead Paragraph**: Full-bleed #ffe845 background, no card. Monument Grotesk 45px, weight 400, line-height 1.0, letter-spacing -0.014em, #000000, centered, max-width 900px. ~80px vertical padding above and below.

4. **Starburst Sticker**: #ffe845 fill, 1.5px #000000 stroke, 36px border-radius with hand-drawn jagged edge, rotated ~5 . Monument Grotesk 18px, weight 400, #000000, all caps, centered inside. Place at top-right of viewport as a single decorative callout.

5. **Testimonial Quote Section**: Full-bleed #ffe845 background. Monument Grotesk 45px, weight 400, #000000, centered, with oversized curly quotes. Attribution in Pitch Sans 16px, letter-spacing 0.05em, all caps, #000000, below the quote. Carousel arrow controls in #000000 at the far left and right edges.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
