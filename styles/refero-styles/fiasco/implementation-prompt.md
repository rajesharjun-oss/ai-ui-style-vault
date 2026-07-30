# AI Implementation Prompt

Build a Fiasco-inspired interface using this source-derived style bundle.

Reference site: https://fiasco.design
Theme: light
Category: Agency
North star: "editorial gallery on cream paper" - warm off-white canvas with confident black type and single-color project cards.

Use these palette anchors:

- Canvas Cream `#f8f9f3` for Page background, button borders, soft surface
- Ink Black `#1d1e19` for Primary text, nav borders, link borders, all structural outlines
- Stone Mist `#e9eae2` for Nav borders, icon strokes, subtle dividers, secondary borders
- Shadow Stone `#d0d1cc` for Card and hero box-shadow base, low-contrast elevation
- Carbon `#151612` for Footer background, deep surface for dark sections
- Pewter `#686e77` for Input border, muted form fields
- Sulfur Yellow `#fff714` for Featured project card fill, callout blocks - the loudest accent, reserved for hero-grade emphasis
- Carnation Pink `#fbc2d1` for Project card background, soft accent block
- Sky Blue `#84bdff` for Project card background, cool accent block
- Ember Orange `#fd6b01` for Project card background, warm accent block
- Cobalt Violet `#204ce5` for Filled button background - the only chromatic action in the system, used sparingly
- Midnight `#112337` for Input text, deep navy utility for form labels
- Lichen Green `#03ac47` for Project card background, rare accent block

Use these typography anchors:

- area-normal `--font-area-normal` for Primary workhorse - body, UI labels, buttons, inputs, project titles. Wide weight range lets it carry both fine 14px body copy and 80px display headlines without leaving the family.
- HAL Timezone `--font-hal-timezone` for Nav labels, small caps treatments, secondary headings. The 100-weight gives nav items a thin, almost editorial feel that contrasts with the bolder body sans.
- Gooper `--font-gooper` for Display and editorial headlines with personality - used for large pull-quotes, italic-feeling treatments, and section titles. The tight 0.8 line-height at 40px gives headlines a compressed, magazine-like density.
- OC Highway `--font-oc-highway` for Micro-labels and tracked-out uppercase tags (e.g. '01:27 UK' timestamp). The +0.10em tracking makes 10px text readable as a label.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 22px.
- Element gap: 12px.

Build these component patterns where relevant:

- Pill Button (Primary): Primary CTA
- Ghost Pill Button: Secondary action
- Project Card: Work/case study tile
- Hero Block: Above-the-fold showcase
- Text Input: Form field
- Tag Pill: Category/discipline label
- Nav Link: Top navigation item
- Section Heading (Display): Hero/page title
- Project Title (Italic): Card heading
- Section Label: Pre-title / kicker
- Footer Block: Site footer

Do:

- Use pill-shaped buttons (800px radius) for every interactive element - never square or slightly-rounded buttons
- Let project cards own color: pick one vivid hex from the accent set per card, keep the rest of the page in warm neutrals
- Set body copy at 18px in area-normal 400 - the system reads at editorial size, not product-UI size
- Anchor all headlines in Ink Black (#1d1e19) and let the canvas (#f8f9f3) carry the warmth - never introduce white
- Reserve 40px radius exclusively for hero and feature surfaces; cards stay at 8px to maintain the gallery hierarchy
- Apply the heavy 0 28px 80px shadow only to hero blocks and project cards - the depth comes from a small number of well-placed shadows, not constant elevation
- Use OC Highway at 10px with +0.10em tracking for micro-labels and timestamps - the tracked uppercase is a signature detail

Avoid:

- Don't use the chromatic accent palette for buttons, nav, or text - they belong only to project card backgrounds
- Don't mix multiple vivid colors on the same card or section - one color field per surface
- Don't introduce pure black (#000000) as a fill - Ink Black (#1d1e19) is the system black, the tiny warm shift is the difference
- Don't use more than one shadow tier per page level - the heavy shadow is for cards/hero, the faint one for inputs, nothing else
- Don't set body text below 18px - the system is editorial, not data-dense
- Don't use Cobalt Violet (#204ce5) for anything other than a single filled primary action - it's the system's only chromatic action and overuse flattens its meaning
- Don't round inputs at 8px - the 3px input radius creates a deliberate contrast with the pill buttons and is part of the system language

Source prompt cues:

Quick Color Reference:
- text: #1d1e19 (Ink Black)
- background: #f8f9f3 (Canvas Cream)
- border: #1d1e19 (Ink Black for structural) / #e9eae2 (Stone Mist for subtle)
- accent: #fff714 (Sulfur Yellow - the loudest project card color)
- primary action: #204ce5 (filled action)
- form input border: #686e77 (Pewter)

Example Component Prompts:

1. Create a project card: 8px border-radius, 22px padding on all sides, background #fff714 (Sulfur Yellow). Project image at top filling card width. Below: italic Gooper 500 19px in #1d1e19 reading the project title. Description in area-normal 400 18px in #1d1e19. Two tag pills at the bottom: 800px radius, 6px 12px padding, 1px #1d1e19 border, area-normal 400 13px #1d1e19. Apply shadow rgba(0,0,0,0.16) 0 28px 80px.

2. Create a hero section: cream canvas (#f8f9f3). Centered headline in area-normal 500 72px, color #1d1e19, letter-spacing -0.029em, line-height 1.1, max-width 720px. Below: a full-bleed visual block, 40px border-radius, 600px tall, with the heavy shadow rgba(0,0,0,0.16) 0 28px 80px.

3. Create a ghost button: 800px border-radius, 12px 20px padding, 1px solid #1d1e19 border, no fill. Text in area-normal 500 14px, color #1d1e19. No shadow. Pair with a second identical button to the right for a dual-action pattern.

4. Create a text input: 3px border-radius, 1px solid #686e77 border, 12px horizontal padding, area-normal 400 18px in #112337, with the faint shadow rgba(18,25,97,0.08) 0 1px 4px. Placeholder in #686e77 at the same size.

5. Create a nav bar: cream canvas background, left-aligned 'Fiasco' wordmark in area-normal 600 24px #1d1e19. Right-aligned cluster of links in HAL Timezone 400 20px #1d1e19, separated by ~24px gaps. Append a 10px OC Highway timestamp with +0.10em tracking at the far right in #1d1e19.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
