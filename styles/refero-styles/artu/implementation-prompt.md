# AI Implementation Prompt

Build a ARTU-inspired interface using this source-derived style bundle.

Reference site: https://artu.works
Theme: light
Category: E-commerce
North star: Gallery wall on white paper. ARTU treats the browser as a museum spread - massive product photography, hairline rules, and a single shock of lime at the bottom edge to close the room.

Use these palette anchors:

- Canvas White `#ffffff` for Page background, card surface, image plate - the entire site sits on pure white
- Ink Black `#000000` for All text, hairline borders, navigation, link underlines, image frames - the sole structural color
- Terminal Lime `#d7ff66` for Footer band, surface highlight wash, terminal accent - high-chroma green that signals a page boundary the way a colored edge stops a gallery wall
- Signal Red `#ff1313` for Decorative border strokes, icon outlines, hairline rules in editorial layouts - used at sub-readable contrast as graphic punctuation, never as body text

Use these typography anchors:

- HelveticaNeuePro `--font-helveticaneuepro` for Universal type family for navigation, body, headings, inputs, and footer - the only weight on the site (400), set in all-caps across the nav and footer, with positive tracking 0.0140em-0.0240em that gives the single weight a mechanical, catalog-like cadence

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1440px.
- Section gap: 32px.
- Card padding: 0px.
- Element gap: 11px.

Build these component patterns where relevant:

- Top Navigation Bar: Persistent global navigation
- Full-bleed Hero Image: Opening viewport statement
- Editorial Image Grid: Scrolling product gallery
- Hairline Divider: Section separator
- Decorative Red Border: Editorial graphic accent
- Carousel Arrows: Image slider controls
- Lime Footer Band: Page terminal / site footer
- Footer Link Row: Secondary navigation
- Image Thumbnail Link: Product teaser

Do:

- Use only one type family (HelveticaNeuePro or Neue Haas Grotesk substitute) and one weight (400) across the entire site
- Set all navigation and footer text in uppercase with positive tracking 0.014-0.024em
- Reserve #d7ff66 for the footer band or a single terminal surface - never spread it across the page
- Use 1px solid #000000 hairlines for all section dividers and image borders
- Let product photography fill the viewport at 0px radius with no overlay text or CTA
- Keep 0px border-radius on every image, card, button, and tag - sharpness is the brand

Avoid:

- Don't introduce a second type weight, a serif, or a display face - 400 Helvetica is the system
- Don't use #ff1313 for body text, headings, or CTAs - its 3.9:1 contrast on white is the point; it belongs only in thin decorative strokes
- Don't add drop shadows, gradients, or glass effects - the site is flat by design
- Don't use rounded corners on any element - not images, not buttons, not tags
- Don't fill the page with the lime green - it only appears as the closing footer band
- Don't add a sticky header, sidebar, or modal - the layout is one continuous gallery scroll
- Don't break the all-caps nav convention with mixed-case menu items or sentence-case headings

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (1px hairlines)
- accent surface: #d7ff66 (footer band only)
- decorative stroke: #ff1313 (thin lines, sub-readable contrast)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Top Navigation Bar** - White background, no border. Left: 'artu' logo in 400 HelveticaNeuePro at 20px, #000000, lowercase. Right of logo, comma-separated: PRODUCTS, STORES, ABOUT, NEWS, CONTACTS in 400 weight, all-caps, 0.022em tracking, #000000. Far right: EN, CART (0), MENU in same style. 17px padding-top, 32px gap between items, 11px row gap. No background fill, no sticky behavior.

2. **Full-bleed Hero Image** - Edge-to-edge photograph spanning 100% viewport width, 0px radius, no border except a 1px solid #000000 hairline at the bottom. No overlay text, no caption, no button. Bottom-right corner: two 18px black arrows ( ) at 1px stroke weight, sitting on the white margin below the image, 32px from the right edge.

3. **Editorial Image Grid Section** - White canvas, asymmetric 3-column grid where images are sized independently (one image at 55% width, one at 40%, one at 45%, one at 30%, etc.) with 32px gaps. All images at 0px radius, no borders, no captions. Below the grid, a 1px solid #000000 full-width hairline divider, then 32px of whitespace, then the footer band.

4. **Lime Footer Band** - Full-width strip filled #d7ff66, height ~24-32px set by padding, no text inside, no border. It is a pure colored wall that closes the page; no other element on the site should use this color.

5. **Decorative Red Hairline** - A 1px solid #ff1313 line used as a graphic mark inside an editorial content block, either as a horizontal rule between two stacked images or as a thin frame around a small icon. Contrast is intentionally low on white - it is seen as a line, not read as text.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
