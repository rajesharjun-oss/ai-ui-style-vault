# AI Implementation Prompt

Build a Altason-inspired interface using this source-derived style bundle.

Reference site: https://atlason.com
Theme: light
Category: Agency
North star: architectural monochrome broadsheet

Use these palette anchors:

- Ink Black `#000000` for Primary text, hairline borders, structural rules, image borders, heading fills - the dominant ink that draws the entire page
- Paper White `#ffffff` for Page canvas, card surfaces, reverse text on dark blocks - the surface that lets the black type speak
- Charcoal Plate `#212121` for Dark surface blocks and image backgrounds where white reverse type sits - a softer alternative to pure black for large dark areas
- Silver Hairline `#b0b0b0` for Subtle dividers and muted secondary links - a quiet mid-gray that recedes behind the black ink without disappearing

Use these typography anchors:

- Haas Grotesk DS Pro `--font-haas-grotesk-ds-pro` for Display and section wordmarks - used at 48-288px with extremely tight leading (0.77-0.80) so multi-line display type nearly touches. The DS variant's compressed proportions are what let 288px headlines fit within a single viewport without breaking rhythm. Substitute: Neue Haas Grotesk Display, or Akzidenz-Grotesk Pro Medium
- Haas Grotesk TX Pro `--font-haas-grotesk-tx-pro` for Body copy, captions, image labels, navigation links, UI text. Weight 400 for body, weight 500 for navigation labels and emphasis. The 36px size at line-height 0.90 creates a tight subheading that bridges body and display scales. Substitute: Neue Haas Grotesk Text, or Inter

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 20px.
- Element gap: 8-10px.

Build these component patterns where relevant:

- Display Wordmark: Brand name or section title rendered as oversized type
- Section Heading: Column or section labels in the three-column grid
- Portfolio Tile: Image card displaying a project thumbnail with caption
- Footer Contact Block: Multi-column footer with studio address, contacts, and press info
- Three-Column Page Grid: Primary layout structure dividing the page into three equal-width columns
- Hairline Rule: Structural 1px border used to subdivide the page
- Image Frame: Border treatment for all portfolio and content images
- Navigation Link: Text-based navigation item in the footer or header
- Dark Image Panel: Large image or section with a dark/charcoal background where reverse white type sits

Do:

- Use Haas Grotesk DS Pro weight 500 at 48-288px for all display headings with line-height 0.77-0.80
- Set all border-radius to 0px - corners are always sharp
- Use 1px solid #000000 borders to frame every image and separate every column
- Use 112-288px padding-bottom for major section breaks to create architectural breathing room
- Use weight 500 (not 700) for emphasis - the medium weight at large sizes carries all the authority needed
- Set body text in Haas Grotesk TX Pro weight 400 at 18px with line-height 1.30
- Use #212121 as the only dark surface - reserve #000000 for text and borders, not large fills

Avoid:

- Never introduce chromatic colors - the palette is strictly black, white, and gray
- Never add box-shadow, drop-shadow, or any elevation effect - the page is flat
- Never use border-radius greater than 0px on any element
- Never use weight 700+ for headings - medium (500) is the heaviest weight in the system
- Never set display type with line-height above 0.85 - the tight leading is what makes oversized type feel structural
- Never use colored hover or active states on links - navigation is purely typographic and static
- Never center text within columns - all text aligns left within its column

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (1px solid)
- dark surface: #212121
- muted/divider: #b0b0b0
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Create a portfolio tile: white canvas, 1px solid #000000 border around a rectangular image, 20px gap below. Caption in Haas Grotesk TX Pro weight 400, 16px, #000000, line-height 1.20, left-aligned directly under the image.

2. Create a display wordmark: the word 'Studio' in Haas Grotesk DS Pro weight 500 at 230px, #000000, line-height 0.77, left-aligned, occupying the full height of a three-column layout's first column. No decoration, no underline, no color.

3. Create a footer contact block: four narrow columns separated by 1px solid #000000 vertical borders, 20px padding-top, 48px padding-left on the first column. Labels in Haas Grotesk TX Pro weight 500 at 16px, values in weight 400 at 16px, all #000000 on #ffffff.

4. Create a dark image panel: #212121 background filling a full column, containing a single line of white text in Haas Grotesk TX Pro weight 500 at 36px, line-height 0.90, bottom-left aligned with 20px padding.

5. Create a three-column page grid: full-bleed white layout divided into three equal-width columns by 1px solid #000000 vertical rules. No max-width, no centering, no gaps - the rules ARE the gutters. Each column holds its own vertical content stack.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
