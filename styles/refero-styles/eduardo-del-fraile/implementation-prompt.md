# AI Implementation Prompt

Build a Eduardo del Fraile-inspired interface using this source-derived style bundle.

Reference site: https://www.eduardodelfraile.com
Theme: dark
Category: Design
North star: Black gallery vitrine - a darkened room where one object glows in white text

Use these palette anchors:

- Void `#000000` for Page background, full-bleed canvas for all content
- Bone White `#ffffff` for All text, navigation, footer instructions, and thin UI strokes
- Ash Gray `#888888` for Secondary or muted text, de-emphasized labels, inactive hints

Use these typography anchors:

- Akzidenz-Grotesk `--font-akzidenz-grotesk` for Sole typeface across navigation, body, footer, and brand mark. The weight 400/700 pairing is the entire hierarchy system - no color, no size jumps, no italic to differentiate roles. At 14-15px the grotesk reads as utilitarian editorial; at 20-21px it becomes signage. Normal tracking preserves the geometric, mechanical feel.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Brand Mark (Wordmark): Site identifier in top-left
- Text Navigation Link: Primary navigation items in top-right
- Social Icon Link: Instagram entry in top-right
- Footer Instruction Text: Scroll-hint labels at bottom-left
- Full-Bleed Showcase Frame: Container for 3D content in the page body
- Language Toggle: Locale switcher in nav (ESP)

Do:

- Set the page background to #000000 on every screen - there is no light variant and no secondary surface color.
- Use only Akzidenz-Grotesk at 14, 15, 20, or 21px with weight 400 or 700; line-height 1.3; tracking 0. Never introduce a second typeface.
- Build navigation as raw text links in #ffffff with 0px border-radius and 20px gap between items - no pills, no fills, no underlines.
- Let 3D or photographic content sit directly on the black canvas with no frame, card, or shadow around it.
- Use weight 700 (bold) as the sole way to emphasize - never use color, italics, or size jumps larger than 6px to create hierarchy.
- Use #888888 only for genuinely de-emphasized secondary text; never for interactive states or active nav.
- Keep all UI micro-copy short and instructional (one to three words) so the void stays empty.

Avoid:

- Do not add accent colors, brand fills, or chromatic highlights of any kind - the palette is strictly black, white, and ash gray.
- Do not apply border-radius to anything - buttons, cards, tags, and images all stay at 0px.
- Do not introduce drop shadows, inner glows, or elevated card layers; the canvas must remain flat.
- Do not use italic, condensed, or extended Akzidenz weights; the family is restricted to 400 and 700.
- Do not wrap the 3D content in a bordered card, a gradient backdrop, or a vignette - it should float on pure black.
- Do not use #ffffff as a filled button background; the system has no filled buttons - actions are text or icons only.
- Do not exceed 21px for any UI text - the grotesk's editorial scale is part of the signature.

Source prompt cues:

Quick Color Reference
- text: #ffffff
- background: #000000
- border: none (no border system; use #ffffff only for 1px hairlines if absolutely needed)
- accent: none
- primary action: no distinct CTA color

Example Component Prompts
1. Top navigation: Place the wordmark 'Eduardo del Fraile' flush-left at the top edge, and the links 'Work', 'About', 'Contact', 'ESP' followed by a 14px Instagram line-icon flush-right. All text is Akzidenz-Grotesk 15px weight 400, color #ffffff, with 20px gap between links. No background, no border, no underline.
2. Full-bleed showcase: Render a 3D object (e.g. a matte ceramic bottle) centered on a pure #000000 canvas. The object occupies ~70% of the viewport height, lit with a single overhead key light. No frame, no card, no border, no shadow around the object. The canvas is edge-to-edge with no margin.
3. Footer: Bottom-left, two short instructions in Akzidenz-Grotesk 14px weight 400 #ffffff, separated by 20px gap: 'Scroll with the mouse' and 'Scroll with L and R keyboard arrows'. No icons, no buttons, no background.
4. De-emphasized helper text: A label like 'ESP' or a secondary annotation in #888888 Akzidenz-Grotesk 14px weight 400 - only when the text is not interactive and must recede behind the primary white type.
5. Active section title: Use Akzidenz-Grotesk 20px weight 700 #ffffff for a section heading. This is the only typographic emphasis allowed - do not change color, add a background, or add a divider line.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
