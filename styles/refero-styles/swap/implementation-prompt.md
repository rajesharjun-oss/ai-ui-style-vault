# AI Implementation Prompt

Build a Swap-inspired interface using this source-derived style bundle.

Reference site: https://www.swap-commerce.com
Theme: light
Category: E-commerce
North star: Mint editorial greenhouse - pale sage rooms with vivid lime accents and whisper-weight serif type.

Use these palette anchors:

- Mint Wash `#f2ffe3` for Page canvas, section backgrounds, hero wash - the dominant surface tone
- Forest Depth `#0d5b3b` for Deep green card backgrounds, contrast surfaces, gradient anchor
- Pine Shadow `#083a26` for Darkest green for emphasis cards, gradient endpoints, high-contrast text on light surfaces
- Spring Gradient Start `#82ff87` for Gradient anchor for display type and decorative washes
- Citrus Gradient End `#deff82` for Gradient endpoint for display type - yellow-green warmth in hero text
- Charcoal Ink `#000000` for Primary text, hairline borders, dark action buttons, icon strokes
- Cream Paper `#ffffff` for Card surfaces, button text on dark fills, input backgrounds, elevated overlays
- Stone Charcoal `#2d3637` for Secondary dark surface, icon fills, dark borders, muted dark mode text
- Warm Mist `#e9e7e2` for Alternate section backgrounds, disabled states, cream-toned surfaces
- Silver Border `#cccccc` for Light dividers, inactive borders, subtle separators
- Sage Gray `#838676` for Muted accent card backgrounds, secondary decorative surfaces
- Eucalyptus `#9cb0a8` for Muted sage for outlined secondary action borders, subtle green-tinted UI

Use these typography anchors:

- mainFont `--font-mainfont` for mainFont - detected in extracted data but not described by AI
- Custom Editorial Serif (swap-serif) `--font-custom-editorial-serif-swap-serif` for Display and headline serif - used exclusively for hero/headline contexts at 72-120px. Weight 100 for maximum impact headlines, weight 300 for sub-headlines. Negative letter-spacing (-0.017em) tightens the high-contrast strokes for fashion-editorial density. This ultra-thin serif against pale mint is the signature combination - it borrows from luxury print typography (Bodoni/Didone lineage) to make a commerce platform feel like a magazine spread.
- Custom UI Sans (swap-sans) `--font-custom-ui-sans-swap-sans` for Primary interface and body typeface - 16px for body, 15px for compact UI, 18px for lead paragraphs, 24px and 30px for section sub-headings. Weight 400 is default, 500 for emphasis, 700 for labels and small caps eyebrow text. Slight negative tracking (-0.01em) tightens the geometric forms for a precise, modern feel. The sans is functional and quiet - it never competes with the display serif.
- secondaryFont `--font-secondaryfont` for secondaryFont - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 30px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Primary Lime Pill Button: Main call-to-action across hero and section CTAs
- Secondary Black Pill Button: Secondary action alongside primary CTAs (e.g. "Book a Demo")
- Outlined Ghost Button: Tertiary or alternative actions
- Hero Gradient Display Block: Oversized brand statement in hero and feature sections
- Soft Card: Content cards, feature blocks, brand story panels
- Brand Logo Grid Card: Customer/partner logo showcase section
- Section Header with Eyebrow: Section introduction with small caps label and serif headline
- Pill Input Field: Email capture, form fields, search
- Eyebrow Label: Small all-caps section identifier above headlines
- Top Navigation Bar: Primary site navigation
- Full-Bleed Hero Section: Opening brand statement
- Logo Strip Section: Social proof via partner/customer logos

Do:

- Use the custom display serif at weight 100 for all hero/feature headlines - this whisper-thin weight is the signature; never substitute with bold sans headlines
- Use 200px border-radius for all buttons and tags to maintain the pill-shaped language
- Pair the vivid lime (#a3fda7) fill with pure black (#000000) text on all primary CTAs for 17:1 contrast
- Apply the 90deg green-to-citrus gradient as background-clip text only on display-sized serif headlines (72px+)
- Set section gaps to 80-120px to preserve the editorial breathing room between content blocks
- Use the pale mint (#f2ffe3) as the primary canvas and reserve white (#ffffff) for card surfaces and inputs - never invert this hierarchy
- Set the display serif to line-height 0.95 and letter-spacing -0.017em to maintain the tight, fashion-editorial density

Avoid:

- Never use bold or semibold weights for display headlines - the ultra-thin serif is the brand signature
- Never use sharp or small border-radii on buttons - anything below 100px breaks the pill language
- Never apply the green-to-citrus gradient to body text, UI labels, or anything below 48px
- Never use a dark or charcoal page background - the entire system is built on pale mint and white
- Never use colored body text - all paragraph and UI copy stays in black (#000000) or charcoal (#2d3637)
- Never add heavy drop shadows - the only shadow allowed is the 28px soft black-9% blur on cards
- Never use multiple chromatic accent colors simultaneously - lime is the sole accent; sage gray and forest green appear only in gradients or specific card contexts

Source prompt cues:

**Quick Color Reference**
- Text: #000000
- Background (canvas): #f2ffe3
- Surface (card): #ffffff
- Border: #cccccc (light) / #000000 (emphasis)
- Accent: #a3fda7
- primary action: #a3fda7 (filled action)

**Example Component Prompts**

1. Create a hero section: pale mint (#f2ffe3) full-bleed background, 120px top padding. Centered serif headline at 72px weight 100, #000000, letter-spacing -0.017em, line-height 0.95. Subtext below at 18px sans weight 400, #2d3637. Two CTAs side by side with 12px gap: a lime pill (#a3fda7 fill, #000000 text, 200px radius, 12px 24px padding, 16px weight 500) and a black pill (#000000 fill, #ffffff text, 200px radius, same padding).

2. Create a Primary Action Button: #a3fda7 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. Create a soft content card: white (#ffffff) background, 24px border-radius, 30px padding, shadow 0px 0px 28px 0px rgba(0,0,0,0.09). Eyebrow label in 12px sans weight 700 uppercase, #000000. Serif headline at 30px weight 300, #000000, -0.017em tracking. Body at 16px sans weight 400, #2d3637.

4. Create a pill input field: white (#ffffff) fill, 1px #cccccc border, 100px border-radius, 14px 24px padding, 16px sans weight 400, placeholder #999999. Focus state: border becomes #a3fda7 (vivid lime).

5. Create a gradient display statement block: pale mint (#f2ffe3) background, 100px vertical padding. Oversized serif text at 120px weight 100, line-height 0.95, letter-spacing -0.017em, with linear-gradient(90deg, #82ff87, #a3fda7 50%, #deff82) applied as background-clip text. The gradient should fill the text glyphs, not the background.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
