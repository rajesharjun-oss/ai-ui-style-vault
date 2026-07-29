# AI Implementation Prompt

Build a Alison Roman-inspired interface using this source-derived style bundle.

Reference site: https://www.alisoneroman.com
Theme: light
Category: Other
North star: cookbook pages on warm cream paper - a printed spread from an artisan food memoir, translated to screen with zero loss of tactility

Use these palette anchors:

- Aubergine Ink `#290a08` for Primary text, headings, filled action buttons, footer text - the warm near-black that anchors every screen; it is the only chromatic dark in the system and the only acceptable fill for primary actions
- Vintage Burgundy `#810c00` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Buttery Highlight `#fff3cc` for Link text and selected heading accent - a pale custard yellow used sparingly to mark hyperlinks and tiny editorial highlights, sitting at AAA contrast on the ink
- Parchment Canvas `#f6f0e1` for Page background - the dominant warm cream that defines the entire site mood; every screen sits on this surface
- Linen Card `#fffaec` for Card surfaces, list-item backgrounds, subtle elevated zones - a step lighter than the canvas, the only card treatment in the system
- Hairline Mist `#e5e7eb` for All borders and dividers throughout the system; used on cards, body blocks, links, and structural dividers - the single hairline color of the site
- Paper White `#ffffff` for Button borders, reverse text on dark fills, and the lightest possible surface lift; the only true white in the palette

Use these typography anchors:

- Jannon Neo `--font-jannon-neo` for Display and heading serif - carries every headline, section title, and large editorial moment from 20px through a dramatic 120px. The custom transitional serif with weight 300 for the largest sizes is the signature choice: the 'Books by Alison Roman' hero and book titles sit at whisper-light weight, giving the page a printed-book authority rather than a SaaS-bold shout. Substitute with Cormorant Garamond or EB Garamond at light weights.
- Modale Antique `--font-modale-antique` for Body, button, card, and UI serif - a slightly more grounded old-style serif for all running text, button labels, card descriptions, and footer lines. The workhorse that lets Jannon Neo's headlines breathe. Substitute with Lora or Source Serif Pro.
- -apple-system `--font-apple-system` for System fallback for legacy card content blocks; only present at 29px with normal tracking - used as a safety net rather than a deliberate voice

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-96px.
- Card padding: 24-48px.
- Element gap: 24px.

Build these component patterns where relevant:

- Filled Order Button: Primary action for purchasing a book
- Editorial Book Section: Showcase a single book with cover and description
- Hero Headline Block: Page-level title like 'Books by Alison Roman'
- Inline Editorial Link: Hyperlink within body copy (e.g. 'here')
- Description Card / Book Plate: The cream rectangle behind a book cover in the visual stack
- Footer / Nav Bar: Top navigation and bottom footer
- Book Cover Image: Primary product visual
- Section Divider Spacer: Vertical separation between book sections

Do:

- Set every page background to Parchment Canvas (#f6f0e1); do not introduce a true white page.
- Use Jannon Neo weight 300 for any text 48px or larger; the whisper-light serif is the headline voice.
- Reserve the Filled Order Button as the only chromatic action - fill #290a08, text #ffffff, 0px radius, 8px 16px padding.
- Space sections 80-96px apart with whitespace alone; never use a horizontal rule or background band to separate sections.
- Apply -0.03em letter-spacing to any display-size Jannon Neo text; the tight tracking is what makes the serif feel printed rather than digital.
- Mark every inline link with Buttery Highlight (#fff3cc) text color - do not use blue, do not use underline.
- Use Linen (#fffaec) for any card or list surface that needs to lift off the canvas; 0px radius, no border, no shadow.

Avoid:

- Do not introduce drop shadows, glows, or blurred elevations anywhere - the system is intentionally flat.
- Do not use a border-radius on any element; the 0px geometry is the design's signature.
- Do not use blue for links, buttons, or accents - Buttery Highlight is the only accent color for hyperlinks.
- Do not use Vintage Burgundy (#810c00) for UI chrome, text, or buttons; it is reserved for book-cover backgrounds only.
- Do not use system sans-serifs (Inter, Helvetica) for headlines - the Jannon Neo serif is the identity.
- Do not fill more than 15% of any page with a non-cream, non-ink color; the system is overwhelmingly two-tone.
- Do not stack sections on alternating background colors; the cream canvas is continuous from top to bottom.

Source prompt cues:

**Quick Color Reference**
- background: #f6f0e1 (Parchment Canvas)
- card/surface: #fffaec (Linen)
- text: #290a08 (Aubergine Ink)
- border: #e5e7eb (Hairline Mist)
- link accent: #fff3cc (Buttery Highlight)
- primary action: #290a08 (filled action)

**3 Example Component Prompts**

1. Build a centered hero headline on a #f6f0e1 canvas. Set the text in Jannon Neo (substitute: Cormorant Garamond) at 96px, weight 300, color #290a08, letter-spacing -0.03em, line-height 1.0. Add 113px of padding above and below. No subtitle, no button, no decoration.

2. Build a two-column book section. Left column: a square book cover image with 0px radius and a 1px #e5e7eb border, sitting inside a #fffaec card with 48px padding. Right column: a Jannon Neo 40px weight 300 title in #290a08 with -0.02em tracking, followed by a Modale Antique 20px weight 400 description in #290a08, then a filled button. The button is #290a08 background, #ffffff text in Modale Antique 18px weight 400, 0px radius, 8px vertical and 16px horizontal padding, with a 12px gap before an inline arrow glyph.

3. Build an inline editorial link. Body text is Modale Antique 20px weight 400 in #290a08 on a #f6f0e1 background. The link word itself is colored #fff3cc with no underline. No other color treatment is used on the link.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
