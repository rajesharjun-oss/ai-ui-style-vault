# AI Implementation Prompt

Build a Yinka Ilori Studio-inspired interface using this source-derived style bundle.

Reference site: https://yinkailori.com
Theme: light
Category: Design
North star: West African textile gallery on blush paper

Use these palette anchors:

- Blush Paper `#f5e5e5` for Page canvas, breathing space between pattern sections, card surfaces on quiet pages
- Ink `#000000` for Body text, navigation links, hairline borders, structural grid lines, icon strokes
- Rose `#d9698c` for Wavy stripe fill in hero/pattern compositions, deeper pink surface variant

Use these typography anchors:

- Haas Grotesk Display R Web `--font-haas-grotesk-display-r-web` for All UI text: navigation links, body copy, footer, labels. The 14px weight 400 is the default for everything clickable; 20px weight 500 for subheadings and journal titles. This is the working typeface - small, neutral, Swiss-grid functional.
- Yinka Sans Ultra `--font-yinka-sans-ultra` for Exclusive to the studio wordmark and oversized display moments. The +0.04em tracking at 120px is critical - it gives the dense letterforms air without losing the custom geometric character. Custom face only used at this display scale; never below 80px.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 175px.
- Card padding: 30px.
- Element gap: 15px.

Build these component patterns where relevant:

- Split Navigation Bar: Primary site navigation
- Hero Pattern Banner: Full-bleed opening visual
- Wordmark Overlay: Studio identity on pattern backgrounds
- Scroll Indicator: Downward scroll cue
- Quiet Pink Section: Breathing space between pattern compositions
- Project Card: Portfolio project entry
- Journal Entry Card: Editorial/blog listing
- Footer Link List: Site footer navigation and legal
- Full-Bleed Project Image: Portfolio showcase

Do:

- Alternate pattern sections with quiet #f5e5e5 fields - never place two pattern compositions adjacent without 175px+ of breathing pink between them
- Use Yinka Sans Ultra exclusively at 120px with 4.8px letter-spacing for the wordmark and never below 80px
- Keep all UI text at exactly 14px Haas Grotesk weight 400; use 20px weight 500 only for subheadings and journal titles
- Apply the 80px horizontal padding to all section content and the 175px vertical section gap to create editorial breathing room
- Use #f5e5e5 as the only canvas color and #000000 as the only structural/text color outside of SVG pattern artwork
- Let the split navigation (left cluster + right cluster, 30px column gap) persist across every page state including full-bleed pattern sections
- Treat empty #f5e5e5 space as a deliberate design element - resist the urge to fill it

Avoid:

- Never add box-shadows, gradients, or border-radius to any component - the system is strictly flat and sharp-cornered
- Never introduce blue, green, or cool tones as UI colors - the palette is warm pink/orange/green within patterns, neutral outside
- Never use a type size between 20px and 120px - the scale is intentionally binary: small functional type or massive display type
- Never apply background colors to cards, buttons, or links - all UI chrome is transparent on the #f5e5e5 canvas
- Never decorate navigation with icons, buttons, or containers - it must remain plain uppercase text links
- Never compress section gaps below 175px between pattern and quiet sections - the rhythm requires dramatic vertical distance
- Never use Yinka Sans Ultra for navigation, body text, or anything below display scale - it is a wordmark face only

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #f5e5e5
- border: #000000 (hairline structural lines)
- accent: #d9698c (deeper rose, used in pattern compositions)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a full-bleed hero pattern section: SVG composition covering 100vh. Base fill #f5e5e5. Vertical wavy stripes in #d9698c and warm orange, full height, distributed evenly across width. Grid of solid green circles (~80px diameter) in 7 columns x 4 rows, offset to overlap the stripes. Center overlay text: 'YINKA ILORI' in Yinka Sans Ultra 120px weight 500, #f5e5e5, letter-spacing 4.8px, centered horizontally in upper third.

2. Create a quiet section: full-viewport #f5e5e5 background, zero content, 175px padding-top and padding-bottom. Functions as visual breath between pattern sections. No borders, no shadows.

3. Create a split navigation bar: sticky top, 80px padding-left and padding-right, #f5e5e5 background. Left-aligned: 'WORK' and 'ABOUT' in Haas Grotesk 14px weight 500 #000000, 30px gap. Right-aligned: 'JOURNAL', 'CONTACT', 'STORE', 'FOUNDATION' same spec, 30px gap. Uppercase. No background, no border, no underline.

4. Create a journal entry: title in Haas Grotesk 20px weight 500 #000000, 15px below a date in 14px weight 400. No card chrome, no border, sits directly on #f5e5e5 canvas with 30px padding-bottom.

5. Create a scroll indicator: single downward arrow character ( ) at 20px, #f5e5e5, centered horizontally, positioned at bottom of a pattern section with 30px from edge. No animation, static element.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
