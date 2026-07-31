# AI Implementation Prompt

Build a Hugo-inspired interface using this source-derived style bundle.

Reference site: https://www.hugoandmarie.com
Theme: light
Category: Agency
North star: Monochrome gallery catalog - editorial photography mounted on infinite white, framed by whisper-thin serif.

Use these palette anchors:

- Paper White `#ffffff` for Page background, card surfaces, badge fills, nav dividers, input fields - the dominant surface that recedes to let imagery speak
- Ink Black `#000000` for Primary text, dense border structure, dark image overlays - the structural anchor for rules and headings
- Soft Ink `#0a0a0a` for Dark borders and separators for elevated surfaces and inverted UI.
- Graphite `#767676` for Input field borders - the only place a mid-gray border appears, marking form-field edges without competing with imagery
- Smoke `#b3b3b3` for Muted icon strokes, separators, and secondary graphic details. Do not promote it to the primary CTA color
- Ash `#cccccc` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.

Use these typography anchors:

- saol-display `--font-saol-display` for Ceremonial headlines and editorial titles - ultralight serif at 100px with 0.95 line-height creates near-touching baselines that feel like fashion-magazine coverlines. This is the only place dramatic typography appears; everything else defers to sans-serif.
- soehne `--font-soehne` for All interface text - nav links at 16px weight 300, section headings at 20-22px weight 300, body at 16px weight 400 with comfortable 1.64 leading, supporting copy at 14px. The weight-300 default for nav and headings is a signature choice: it makes the UI feel editorial and unpressured rather than assertive.
- soehne-mono `--font-soehne-mono` for Badge labels and small metadata - monospace at 13px marks categorically different content (tags, IDs, status) from the proportional body text

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 90px.
- Card padding: 0px.
- Element gap: 5px.

Build these component patterns where relevant:

- Editorial Text Link: Primary navigation and inline CTAs
- Hairline Divider: Section separator
- Display Headline (Overlay): Hero text over full-bleed photography
- Pill Badge: Filter and category tags
- Three-Column Service Block: Agency/Studio/Contact overview grid
- Image Grid Thumbnail: Artist portfolio grid items
- Full-Bleed Editorial Hero: Page-opening image section
- Section Header Row: Content section titles with secondary action
- Navigation Bar: Top-level site navigation

Do:

- Use soehne weight 300 as the default for all navigation and section headings - never default to 400 or higher for UI chrome
- Use saol-display weight 100 at 100px with 0.95 line-height for ceremonial display moments; never use it below 48px
- Render all buttons and links as text-with-arrow ( ), never as filled rectangles - the system has no filled buttons
- Apply 9999px radius exclusively to badges; keep all other elements (cards, images, inputs) at 0px radius
- Separate content sections with 1px solid #0a0a0a hairlines, not whitespace gaps or shadows
- Use white (#ffffff) as the only surface color for cards and content blocks - never introduce tints, off-whites, or gray fills for grouping
- Place imagery edge-to-edge with no border, padding, or radius when used as a section anchor

Avoid:

- Never introduce a chromatic accent color, brand color, or decorative gradient - the system is strictly achromatic and adding color breaks the editorial contract
- Never apply box-shadow, drop-shadow, or any elevation effect - depth is communicated through image bleed and hairline rules, not shadows
- Never use soehne-mono for body copy or navigation - reserve it exclusively for badge labels and small metadata
- Never use saol-display at body sizes (14-22px) - it is a display face only; body work belongs to soehne
- Never add border-radius to cards, images, or inputs - 0px radius is the system default for all non-badge elements
- Never use filled background colors for buttons or interactive elements - text links and hairline buttons are the only interactive pattern
- Never use a font weight above 400 in soehne for UI text - heavier weights break the restrained editorial tone

Source prompt cues:

**Quick Color Reference**
- text: #0a0a0a
- background: #ffffff
- border: #0a0a0a
- accent: none (system is strictly achromatic)
- muted text/icons: #b3b3b3
- input border: #767676
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Full-bleed editorial hero**: Edge-to-edge image filling 100vw and 100vh. Centered overlay text in saol-display 100px weight 100, color #ffffff, line-height 0.95, letter-spacing -1px. No border, no padding, no chrome. A thin white decorative line sits below the text.

2. **Three-column service overview**: White background, three equal columns spanning full width. Each column separated by a 1px solid #0a0a0a vertical border. Column heading in soehne 20px weight 300, 'Explore ' in 14px weight 300 below, body copy in soehne 16px weight 400 with 1.64 line-height. No card backgrounds, no padding, no radius.

3. **Artist portfolio grid**: White background, multi-row horizontal grid of square portrait image thumbnails. Images have 0px radius, no border, no gap larger than 8px. No captions, no hover effects. A section header above: 'Artist Bureau' in soehne 16px weight 400, 'Watch Reel ' below in 14px weight 300, with pill badges ('Latest', 'Femme & Childlike') aligned right. Separated from grid by a 1px solid #0a0a0a horizontal rule.

4. **Navigation bar**: Full-width white bar, 1px solid #0a0a0a border-bottom. Logo 'Hugo & Marie' in soehne 14px weight 300 on the far left. Center: three nav links (Creative Agency / Artist Bureau / Helium ) in soehne 16px weight 300, #0a0a0a, with 30px horizontal padding between each. 'Info' on the far right. No background fill, no buttons, no icons.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
