# AI Implementation Prompt

Build a Piet Oudolf-inspired interface using this source-derived style bundle.

Reference site: https://oudolf.com
Theme: light
Category: Agency
North star: Botanical index on white paper.

Use these palette anchors:

- Field White `#ffffff` for Page canvas, text on dark inverted sections, and link underline anchor for body copy
- Charcoal Black `#000000` for SVG icon fills and absolute typographic black where maximum contrast is needed (headings against light imagery)
- Lead Gray `#808080` for Primary type, all link and border lines, and the connective tissue of the system - every hairline rule, navigation separator, and body character sits here
- Ash Gray `#b3b3b3` for Navigation labels, muted metadata, footer text, and the secondary tonal floor that recedes behind lead-gray working type
- Smoke `#999999` for Subtle border accent used sparingly to separate tertiary structural elements

Use these typography anchors:

- Maison Neue Book `--font-maison-neue-book` for Signature display face for project titles and section headings - 60px at weight 300 is the defining choice, letting each garden name whisper across the page rather than announce
- UniversLTStd-Light `--font-universltstd-light` for Workhorse sans for navigation, country-code labels, body, footer, and all meta information - 12px handles the tiny geo tags above project names, 15px carries paragraph body at generous 1.87 leading for editorial breathing room

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 60px.
- Card padding: 40px.
- Element gap: 6px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Country Code Tag: Geographic metadata for each project entry
- Project Title Link: Primary clickable entry - the core content unit
- Side Margin Label: Vertical section indicator
- Inline Link: Connected text link within body or nav
- Search Icon: Utility trigger in the top right of navigation
- Footer: Site colophon and secondary links

Do:

- Set all project and section titles at exactly 60px Maison Neue Book weight 300 - never bold, never above 300
- Use 12px UniversLTStd-Light for all metadata, country codes, and side labels at 1.6 line-height
- Use 15px UniversLTStd-Light for body copy and navigation at 1.87 line-height for editorial airiness
- Render every link with a 1px #808080 underline offset 3px from the baseline - no fill, no border box, no background color
- Indent every project link exactly 22px from the country code column so the tag and title align as a herbarium pair
- Let the page breathe: use 60px horizontal padding on hero sections and 40px vertical padding on the nav bar
- Keep the page at 0% colorfulness - grayscale only, no accent hues, no brand color, no filled buttons

Avoid:

- Never introduce a brand color, accent, or fill of any kind - the monochromatic palette is the identity
- Never set a project title below 48px or above 64px - the 60px headline scale is a fixed point of the system
- Never add shadows, gradients, glows, or any form of z-axis depth to cards, buttons, or containers
- Never round corners - all radii are 0px; the system is deliberately rectilinear like a printed page
- Never bold body or heading type - weight 300 is the ceiling for display, weight 400 for everything else
- Never place more than 6px between an inline link and its sibling, or more than 3px between text and its underline
- Never use a filled button, pill, or chip - interaction is expressed only through typographic underlines

Source prompt cues:

**Quick Color Reference**
- background: #ffffff
- text: #808080
- border / underline: #808080
- muted text: #b3b3b3
- max contrast / SVG: #000000
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Project Title Entry**: Render a single list item on a white background. Above the title, set a 12px UniversLTStd-Light country code label in #808080 with 1.6 line-height. Below it, set the project name at 60px Maison Neue Book weight 300, #808080, 1.25 line-height, with a 1px #808080 underline offset 3px below the baseline. Left-indent the title 22px from the country code. Gap between the code and title: 3px.

2. **Top Navigation Bar**: Full-bleed white bar with 40px top and bottom padding. Left-aligned wordmark 'Piet Oudolf' in 15px UniversLTStd-Light #808080. Centered group of nav links ('Projects', 'Information', 'Private Garden') at 15px UniversLTStd-Light #808080, each underlined with a 1px #808080 line offset 3px below baseline, separated by 6px margins. Right-aligned search icon as a 16px black SVG glyph. No background, no border, no shadow.

3. **Side Margin Section Label**: Set 'Public gardens' in 12px UniversLTStd-Light #808080, rotated 90 counter-clockwise, positioned in the left page margin (60px from page edge). 1.6 line-height. No background, no border.

4. **Footer Colophon**: Left-aligned block at the bottom of the page, 60px vertical gap above. Text in 12px UniversLTStd-Light #b3b3b3 at 2.33 line-height. No dividers, no columns, no links styled differently from body.

5. **Inline Body Link**: Within a paragraph of 15px UniversLTStd-Light #808080 at 1.87 line-height, set a linked phrase at the same size and color, with a 1px #808080 underline offset 3px below the baseline. No color change, no background, no border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
