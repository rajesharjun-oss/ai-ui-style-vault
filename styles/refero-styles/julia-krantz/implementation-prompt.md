# AI Implementation Prompt

Build a Julia Krantz-inspired interface using this source-derived style bundle.

Reference site: https://juliakrantz.com
Theme: dark
Category: Agency
North star: Darkroom contact sheet - a grid of photographic tiles on pure black, identity spelled in barely-visible weight-300 letterforms.

Use these palette anchors:

- Void `#000000` for Page canvas, all section backgrounds - the true floor of the UI; every element floats above absolute black
- Salt `#f8f8f8` for All text, links, nav labels, borders, icons - the single foreground tone serving every text and UI edge function against black
- Ash `#707070` for Secondary labels, muted nav text, subdued body copy - mid-tone for visual hierarchy without introducing any hue

Use these typography anchors:

- DM Sans `--font-dm-sans` for All body copy, navigation labels, press list items, links, captions. Weight 300 across every size - the site refuses to bold anything in this family, keeping the text layer visually quiet against photography.
- ClashDisplay `--font-clashdisplay` for Project initials on tiles (44px weight 300, tracking -0.04em), section codes and labels (12-14px weight 300, tracking +0.05em to +0.14em), name logotype. The 44px weight-300 display setting - a nearly invisible letterform over a photograph - is the signature visual move of the portfolio.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 30px.
- Card padding: 16px.
- Element gap: 6px.

Build these component patterns where relevant:

- Project Grid Tile: Primary portfolio navigation - each tile is a cropped photograph with abbreviated project code overlaid
- Name Logotype: Primary identity mark in the top-left header
- Navigation Link: Top-right global nav: Magic Fabric , Bio, Contact
- About Bio Block: Multi-column text section with label headers
- Press List Item: Numbered external press links within the bio section
- Email CTA Link: Contact email in the top-right of the header, the site's only direct CTA
- Section Divider: Horizontal rule separating header from bio section and bio section from grid
- Category Label: Small uppercase tag beneath project initials on tiles
- Archive Year Badge: Year label on archive tiles (e.g. '- 2009', '- 2011')

Do:

- Use #000000 for all backgrounds - the CSS token --bg: #000 is absolute; never substitute dark gray or near-black
- Set all ClashDisplay display headings (44px tile codes) at weight 300 with letter-spacing -0.04em - the ultra-light setting against photography is the signature move
- Apply 1px solid rgba(248,248,248,0.12) for every structural border: tile separators, section dividers, column rules
- Keep all interactive hover states to color/filter transitions only - color: rgba(248,248,248,0.45) for links, filter: brightness(0.82) for image tiles, 0.2s ease
- Use 0px border-radius on every element - tiles, any containers, any interactive elements. The sharp-corner rule is absolute
- Maintain DM Sans weight 300 for all body, nav, and label text - no bold text anywhere in the UI layer
- Express secondary hierarchy through #707070 (section labels, numbers, category tags) - never through size increases or weight changes

Avoid:

- Never add any color to the UI chrome - buttons, links, labels, borders must remain in the #f8f8f8 / #707070 / rgba opacity system only
- Never round corners - no border-radius on tiles, containers, or any interactive element; 0px is non-negotiable
- Never use font weight above 500 - ClashDisplay 500 is the ceiling and used only for the name logotype; DM Sans stays at 300
- Never add box-shadows or elevation - the design has zero shadow tokens; depth comes from contrast with the black canvas only
- Never add hover backgrounds or button fills - interactive states change text opacity or image brightness only, never add a background color
- Never introduce gradients, overlays, or tinted backgrounds - the CSS tokens confirm no gradient system exists; #000 is the only background
- Never separate the category label from its tile project code with more than 4px margin - the tight stacking (4px marginBottom between elements) is the spatial rhythm

Source prompt cues:

**Quick Color Reference**
- Page background: #000000
- Primary text / all UI elements: #f8f8f8
- Secondary / muted text: #707070
- Borders / dividers: rgba(248,248,248,0.12)
- Overlay text on images: rgba(248,248,248,0.45)
- No accent colors exist - the palette is purely achromatic

**Example Component Prompts**

1. **Project Grid Tile**: Black background tile with full-bleed photograph. Top-left: sequential number in DM Sans 10px weight 300 #707070, then project code (e.g. 'Fd') in ClashDisplay 44px weight 300 #f8f8f8 letter-spacing -0.04em, then category label 'PRACTICE' in DM Sans 10px weight 300 #707070 letter-spacing 0.14em. All text padded 16px from edges. Border: 1px solid rgba(248,248,248,0.12). Border-radius: 0px. Hover: filter brightness(0.82) transition 0.2s ease.

2. **Page Header**: Full-width bar, #000000 background, 16px horizontal padding, 52px height. Left: 'Julia Krantz' in ClashDisplay 29px weight 500 #f8f8f8 letter-spacing -0.04em. Right: 'julia@magicfabricblog.com ' in DM Sans 12px weight 300 #f8f8f8 with small dot indicator, then nav links 'Magic Fabric ', 'Bio', 'Contact' in DM Sans 12px weight 300 #f8f8f8 letter-spacing 0.06em, 32px gap between items. Bottom border: 1px solid rgba(248,248,248,0.12).

3. **Bio Multi-Column Section**: #000000 background, 16px padding, 5 columns with 32px gaps. Each column starts with an uppercase label ('ABOUT', 'PRESS') in DM Sans 10px weight 300 #707070 letter-spacing 0.07em, margin-bottom 4px. Body text in DM Sans 13px weight 300 #f8f8f8 line-height 1.72. Numbered list items use #707070 for the number and #f8f8f8 for the link text. External links append ' ' glyph.

4. **Category Label / Tag**: DM Sans 10px weight 300 #707070 letter-spacing 0.14em. Uppercase. No background, no border, no padding. Values are 'PRACTICE', 'ARCHIVE', or 'BLOG'. Sits 4px below project title.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
