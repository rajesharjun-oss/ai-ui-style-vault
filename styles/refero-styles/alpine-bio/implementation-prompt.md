# AI Implementation Prompt

Build a Alpine Bio-inspired interface using this source-derived style bundle.

Reference site: https://alpbio.com
Theme: light
Category: Other
North star: Sun-drenched botanical apothecary on cream parchment

Use these palette anchors:

- Parchment `#f5f5f5` for Page canvas and base background - the neutral ground everything sits on
- Warm Cream `#f8f4e6` for Section backgrounds, footer surface, and warm page rhythm - gives the system its apothecary warmth
- Paper White `#ffffff` for Text on dark imagery, elevated card surfaces, and bright contrast moments
- Mist Gray `#e9e9e9` for Subtle surface fills - nav background, button hover rests, and quiet UI layers
- Ink `#1e1e1f` for Primary body text and structural borders - softer than pure black, warmer against the cream
- Carbon `#000000` for Heading text, heavy borders, icon strokes - the highest-contrast neutral in the system
- Sky Blue `#8ec7e2` for Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Pollen Yellow `#f7ca50` for Highlight labels, breadcrumb tags, scroll-indicator text - rare warm punctuation against the cream

Use these typography anchors:

- Switzer `--font-switzer` for Display and heading type - geometric sans with consistent tight tracking, carries the editorial voice from 20px subheads up to 76px hero headlines
- Geist `--font-geist` for Body and intermediate type - comfortable reading at 15-18px, scales up to 42px for feature sub-heads
- PT Mono `--font-pt-mono` for Nav items, category labels, and small uppercase tags - the only monospace, used to signal nav/system elements distinct from editorial body
- system sans-serif `--font-system-sans-serif` for Micro-copy and fallback - only appears at 12px in utility positions

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 80px.
- Card padding: 12px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Pill Button: The sole action button variant - used for Contact Us, Request a Sample, Learn More, View All
- Ghost Nav Button: The 'Contact Us' control in the top-right of the navigation
- Navigation Bar: Sticky top header carrying brand + section links
- Hero Section: Full-viewport opening with product imagery and overlay headline
- Editorial Body Block: Long-form introductory paragraph below the hero
- Application Showcase Card: Large product photograph cards in a 3-column carousel
- Section Heading: Large editorial headings like 'Applications Showcase'
- Pollen Label: Small warm-amber tag for breadcrumb and category markers
- Carousel Arrow Control: Navigation for the Application Showcase carousel
- Carousel Dot Indicator: Position indicator beneath the Application Showcase
- Scroll Indicator: 'SCROLL DOWN' text at the very bottom of the hero
- Footer Surface: Closing section with warm cream background

Do:

- Use #8ec7e2 fill with #000000 text and 22px radius for every action - this is the only button style in the system
- Apply -0.0500em letter-spacing to every Switzer and Geist heading - the tight tracking is what makes the type feel editorial
- Use Pollen Yellow (#f7ca50) only for small typographic accents: breadcrumb labels, scroll cues, and footer highlights - never as a button fill or large background
- Pair every pill button with a right-side circular arrow icon - the arrow is part of the button's identity, not decoration
- Default to full-bleed left-aligned layouts - content starts from the left edge rather than centering in a max-width container
- Use Warm Cream (#f8f4e6) for alternating section backgrounds to create warm/cool rhythm against the gray canvas
- Choose Switzer for all display and heading sizes 20px and above; reserve Geist for body and PT Mono for nav/labels

Avoid:

- Don't add drop shadows to cards, buttons, or modals - the system is intentionally flat, depth comes from surface color only
- Don't introduce new chromatic colors - the palette is sky blue + pollen yellow + warm neutrals, nothing else
- Don't use the pollen yellow as a CTA or button background - it's a typographic accent only
- Don't center content in a max-width container for body sections - the editorial feel depends on left-aligned, edge-to-edge composition
- Don't use type weights above 500 - Switzer and Geist at 400-500 carry the whole system, bolder weights would break the quiet tone
- Don't apply borders to the Primary Pill Button - it relies on the sky-blue fill alone for its identity
- Don't use dark mode - the entire system is calibrated around the cream canvas; inverting it would destroy the apothecary warmth

Source prompt cues:

**Quick Color Reference**
- text: #1e1e1f (body), #000000 (headings)
- background: #f5f5f5 (canvas), #f8f4e6 (warm sections)
- border: #000000 (structural), #e9e9e9 (subtle)
- accent: #f7ca50 (Pollen Yellow - labels only)
- primary action: no distinct CTA color

**Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.


3. *Application Showcase card*: Full-bleed product photograph (RTD shake, protein bars, or coffee cream) filling the card with 22px border-radius. White PT Mono 13px label at bottom-left of image. No border, no shadow, no internal padding.

4. *Section heading + carousel*: 'Applications Showcase' in Switzer 48px weight 400, #1e1e1f, left-aligned. Two circular carousel arrow controls (Mist Gray fill, Carbon arrow) right-aligned. Row of small Carbon/light-gray dots centered below the card grid.

5. *Navigation bar*: Sticky top, Mist Gray (#e9e9e9) background, 3px radius. Logo 'Alpine Bio' left, nav items (INGREDIENTS, APPLICATIONS, COMPANY, INTEL) in PT Mono 13px weight 400, #000000 center-left. Sky Blue (#8ec7e2) pill Contact Us button with arrow icon, right-aligned.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
