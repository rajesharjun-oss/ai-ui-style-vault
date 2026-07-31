# AI Implementation Prompt

Build a Mr. Pops-inspired interface using this source-derived style bundle.

Reference site: https://mrpops.ua/en
Theme: light
Category: E-commerce
North star: retro ice cream parlor on cream paper. A bright white shopfront with cherry-red trim, stacked marquee letters, and warm cream cards beneath full-bleed food photography.

Use these palette anchors:

- Cherry Marquee `#b00e2f` for Brand accent, heading text, link color, icon stroke, outlined button border, footer headline - vivid warm red used as the single chromatic signal across an otherwise cream-and-white interface
- Cream Bisque `#fee5ca` for Secondary surface for cards, callout panels, and the cart/bag detail button - warm near-white that reads as paper, not gray
- Canvas White `#ffffff` for Page background, card surface, input fill, button text on dark
- Ink Black `#000000` for Primary body text, icon fills, heavy borders, SVG fill - the only true dark
- Slate Mid `#aaaaaa` for Muted secondary text, disabled placeholders, low-emphasis dividers

Use these typography anchors:

- Cervo `--font-cervo` for Display and headings only. Set extremely tight (line-height 0.75 on the 144px hero, 0.9 on 64-72px) and tracked slightly outward at 0.05em - the condensed letterforms and compressed leading make the headline read as a hand-painted sign rather than a web type block. Weight 400 carries the body, weight 500 amplifies emphasis within the display.
- HelveticaNeueCyr `--font-helveticaneuecyr` for Body, UI, navigation, footer, input, captions. Light 400 weight throughout with generous 1.3-1.4 leading on running text - the whisper-weight keeps chrome from competing with the Cervo display, so the marquee headline always wins the eye.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 40px.
- Card padding: 30px.
- Element gap: 10px.

Build these component patterns where relevant:

- Marquee Display Headline: Hero and section title
- Cherry Outline Button: Primary call to action
- Cream Filled Button: Secondary call to action (cart, bag, less prominent action)
- Ghost Navigation Item: Top nav links (Flavours, Menu)
- Cream Bisque Card: Featured product, flavor panel, content block
- Hero Photograph Frame: Full-bleed lifestyle / food photography
- Inline Red Label: Section link or 'FLAVOURS' style trigger
- Paragraph Block: Long-form body copy beside the hero
- Cart Badge: Top-right shopping bag count
- Scroll Cue Arrow: Down-arrow prompt at the bottom of the hero
- Footer Band: Site footer

Do:

- Stack Cervo display type four lines deep and let line-height collapse to 0.75 on the 144px hero size.
- Use Cherry Marquee (#b00e2f) as outline, link, and accent text - never as a filled button background.
- Set 0.05em positive letter-spacing on every Cervo size from 22px upward.
- Build every interactive element with a 300px (pill) radius.
- Lift secondary content with Cream Bisque (#fee5ca) fills at 40px radius, not with shadows.
- Let hero photography bleed edge-to-edge with text overlaid directly on the image - no scrim.
- Keep body copy in HelveticaNeueCyr weight 400 at 15-16px with 1.3-1.4 line-height so the display type stays the loudest thing on the page.

Avoid:

- Don't fill a button solid Cherry Marquee - the brand signal is the red outline, not a red block.
- Don't apply drop shadows to cards, buttons, or panels - depth comes from cream surfaces, not elevation stacks.
- Don't set Cervo with line-height above 1.0 on display sizes; the compressed leading is the signature.
- Don't introduce gray or cool neutrals - every neutral should be warm (cream, white) or pure black.
- Don't use a second chromatic accent - Cherry Marquee is the only color allowed beyond the cream/black/white system.
- Don't switch the canvas to dark or use a dark-mode pattern - the brand is locked to a sunlit light theme.
- Don't set negative letter-spacing on Cervo - the 0.05em outward tracking is what makes the marquee read as signage.

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Ink Black)
- background: #ffffff (Canvas White)
- border: #b00e2f (Cherry Marquee) for accent outlines; #000000 for neutral borders
- accent: #b00e2f (Cherry Marquee) for headings, links, icons, outlines
- surface: #fee5ca (Cream Bisque) for secondary cards and the cream button
- primary action: #b00e2f (filled action)

**Example Component Prompts**
1. Build a hero section: edge-to-edge photograph fills the viewport. Cervo weight 400 at 144px, line-height 0.75, letter-spacing 0.05em, uppercase, color #000000, stacked in four lines top-left. One word in the third line recolored #b00e2f. A paragraph of 16px HelveticaNeueCyr weight 400 in #000000 sits in a ~440px column to the right of the headline.
2. Build a Cherry Marquee outline button: 1px solid #b00e2f border, transparent fill, #b00e2f text, 300px border-radius, 16px HelveticaNeueCyr, 30px horizontal padding, 10px vertical padding.
3. Build a Cream Bisque secondary button: #fee5ca background, no border, #000000 text, 300px border-radius, 16px HelveticaNeueCyr, 30px horizontal padding.
4. Build a Cream Bisque content card: #fee5ca background, 40px border-radius, 30px padding, 22px Cervo weight 400 heading in #000000 with 0.05em tracking, 16px HelveticaNeueCyr body text below in #000000.
5. Build the top navigation: logo top-left in #b00e2f, three items (cart, 'Flavours', 'Menu') top-right, 1px #000000 borders on the two text links, 300px radius, 15px HelveticaNeueCyr, 30px gap between items.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
