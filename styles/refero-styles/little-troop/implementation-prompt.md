# AI Implementation Prompt

Build a Little Troop-inspired interface using this source-derived style bundle.

Reference site: https://littletroop.com
Theme: light
Category: Agency
North star: Monochrome gallery with chromatic artworks. A black pearl floating in white void.

Use these palette anchors:

- Pure Black `#000000` for All text, all borders, the nav mark, section dividers, filter indicators. The structural ink of the entire system - every line, frame, and glyph is black on white
- Pure White `#ffffff` for Page canvas and inverse text. The only surface; cards do not introduce a separate fill - they borrow the page and let imagery do the work

Use these typography anchors:

- Arial Narrow `--font-arial-narrow` for The functional voice of the entire interface - navigation, body, metadata, project captions, filter labels, footer copy. Narrow letterforms in a generous white field create a typesetter's galley feel; everything reads as a running label rather than as UI chrome.
- Times Now `--font-times-now` for The single display voice, reserved for the hero headline curved around the orb. Weight 250 is anti-convention - most studios reach for 600-800 bold serifs. This whisper-weight, paired with a sculptural -0.066em tracking and 0.79 line-height, makes the text feel like a ribbon on the surface rather than a title above it. When the system needs authority, it gets it through restraint, not volume.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 100px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Project Grid Card: Project thumbnail in the work index
- Project Spotlight Card: Featured project presentation
- Project Index Filter: Category filter for the work grid
- Hero Orb with Curved Text: Splash/hero moment
- Footer Credit Block: Studio identity and current work status
- Section Header: Section label for project groupings
- Penguin Brand Mark: Studio logo / nav anchor

Do:

- Use 50px border-radius on every rectangular element - cards, tags, buttons, frames. This is the system's only shape.
- Restrict the palette to #000000 and #ffffff for all chrome, text, and borders. Color is the exclusive property of project imagery.
- Set Arial Narrow at 14-16px for every functional element - nav, labels, body, metadata. Reserve Times Now weight 250 for at most one display moment per page.
- Apply 100px+ section gaps between major content blocks. The system needs white void to breathe.
- Let full-bleed imagery fill cards edge-to-edge inside the 50px radius - no padding, no captions inside the frame.
- Use 20px padding for card metadata blocks beneath cards. Keep that rhythm consistent.
- Anchor the nav and footer to viewport edges with extreme lateral margins (100-230px) so items read as floating labels.

Avoid:

- Do not introduce a third color, a shadow, a gradient, or any surface tint. The two-color discipline is the brand.
- Do not use a bold display weight for headlines. Times Now weight 250 is the only display voice; if you need more presence, increase size, never weight.
- Do not use rectangular corners anywhere. Even small chips, tags, and buttons get 50px radius.
- Do not add borders, outlines, or focus rings that aren't pure 1px black. No colored states, no tinted hovers.
- Do not break the white canvas with a panel, sidebar, or container surface. The page is the only surface.
- Do not center-align body or metadata text. The footer credit and project captions are left- or right-aligned to specific edges.
- Do not use a sans-serif system font for display. The serif at ultra-light weight is what separates this system from every other minimalist agency portfolio.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000
- inverse text: #ffffff
- accent: none (the system is two-color; the penguin's red beak is the only chromatic mark and should not be replicated as a token)
- primary action: no distinct CTA color

**Example Component Prompts**
1. *Project Grid Card* - Full-bleed image inside a 50px border-radius frame, no border, no shadow, no padding. Image fills the frame edge-to-edge. Below the frame, Arial Narrow 14px #000000 title left-aligned, then a one-line Arial Narrow 14px #000000 description.
2. *Section Header* - Arial Narrow 16px #000000 label top-left of the band (e.g., 'Project Index'). A small penguin mark sits adjacent in black with a red beak. 100px of pure white space below before the next band begins.
3. *Project Index Filter* - A horizontal row of categories in Arial Narrow 14px #000000, each preceded by a 12px circle with a 1px #000000 border and white fill. Items wrap to a second row if needed. No backgrounds, no pills, no chips.
4. *Top Navigation* - Five items spread edge-to-edge: 'Work' far-left, 'News' left-of-center, penguin mark centered, 'Info' right-of-center, 'Contact' far-right. Arial Narrow 14px #000000. No background, no border, no container.
5. *Project Spotlight Card* - A single oversized 50px-radius frame (roughly 2.5x grid card area) filled with project hero artwork. A second 50px-radius card overlaps it with a small z-offset and 2-3 rotation. No borders, no shadows - only the radius gives them physical presence.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
