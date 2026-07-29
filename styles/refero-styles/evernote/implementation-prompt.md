# AI Implementation Prompt

Build a Evernote-inspired interface using this source-derived style bundle.

Reference site: https://evernote.com
Theme: light
Category: Productivity
North star: Afternoon sun on cream paper - a warm, lived-in notebook where white cards float on beige, dark text breathes, and one lime-green highlighter marks the important things.

Use these palette anchors:

- Lime Sprout `#94e130` for Primary action button, icon highlights, accent tags - the singular chromatic punctuation that makes actions feel switched on against the cream canvas
- Paper Cream `#f9f6f2` for Page canvas, hero background, section backgrounds - warm off-white that replaces standard white with a paper-like quality
- Ivory Card `#f4eee5` for Alternate card surface, warm-toned elevated panels that sit one step deeper than the cream canvas
- Pure White `#ffffff` for Elevated card surfaces, product screenshot containers, button text on dark fills
- Slate Border `#e7e7e7` for Card borders, hairline dividers between content sections and list items
- Smoke `#a1a1a1` for Muted link borders, nav underlines, subtle structural dividers
- Stone `#737373` for Helper text, tertiary body content, subdued annotations
- Graphite `#4e4d4c` for Secondary text, icon strokes, subdued UI labels
- Iron `#262626` for Dark surface elements, body borders on inverted sections
- Charcoal `#141414` for Primary text, dark filled buttons, heading color - the near-black that carries all weight in the type system
- Onyx `#000000` for Maximum-contrast borders, footer rules, SVG fills where absolute black is needed

Use these typography anchors:

- Figtree `--font-figtree` for Primary typeface across all UI - display, headings, body, nav, buttons. Weight 300 at 72px hero is a signature choice: whisper-light headlines that feel editorial and confident rather than bold-and-shouting. The geometric humanist forms of Figtree at 300 weight give the warm cream canvas a modern editorial feel.
- Inter `--font-inter` for Secondary body text at 16-20px, likely fallback or supplementary paragraph copy. Used sparingly alongside Figtree for longer-form descriptive text.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Primary CTA Button (Dark): Main conversion button on light backgrounds - the default call-to-action
- Primary CTA Button (Lime): Energy-action button used on dark sections to make CTAs pop
- Ghost Nav Button: Secondary nav-level action like 'Download' - lower-emphasis than the primary CTA
- Text Link: Inline link in body copy or nav
- Top Navigation Bar: Primary site navigation
- Feature Card: Card in the features carousel - one capability per card
- Product Screenshot Card: Large product preview image with browser-chrome frame
- Category Icon Square: Small colored block that color-codes a feature card category
- Dark Contrast Section: High-energy section that breaks the cream rhythm with full-black background
- Carousel Navigation: Pagination control for card carousels
- Tag/Pill Badge: Category tag like 'Organize' on dark section

Do:

- Use Paper Cream #f9f6f2 as the default page canvas - never switch to pure white for full-page backgrounds
- Set hero headlines at 72px Figtree weight 300 with -3.6px letter-spacing for the signature airy editorial feel
- Apply Lime Sprout #94e130 only to one element per viewport: a CTA, an icon, or a tag - never as a background fill
- Use 5px border-radius for all buttons and 10px for cards - this subtle rounding is core to the warm, non-techy personality
- Maintain a minimum 80px gap between major sections to preserve the generous breathing room visible in the layout
- Pair the dark filled CTA on cream backgrounds with the lime filled CTA on dark sections - the CTA color flips with the surface
- Use colored 40px icon squares (blue/green/yellow/purple) on feature cards to create category coding without adding text labels

Avoid:

- Don't use pure white #ffffff as a page background - it breaks the warm paper system
- Don't apply weight 600 or above to display headlines - weight 300 is the signature, heavier weights feel corporate
- Don't use Lime Sprout for large background fills, gradients, or decorative bands - it loses its energy when used at scale
- Don't add drop shadows to cards - the system relies on flat hairline borders (#e7e7e7) for separation, not elevation
- Don't use fully rounded (9999px) buttons - 5px is the intentional subtle rounding, not pill-shaped
- Don't introduce more than one additional accent color per screen - the cream + charcoal + lime triad is the system
- Don't use letter-spacing looser than -0.03em on headings - the tight tracking is what makes the large type feel modern rather than textbook

Source prompt cues:

**Quick Color Reference**
- Background: #f9f6f2 (Paper Cream)
- Card surface: #ffffff (Pure White)
- Border: #e7e7e7 (Slate Border)
- Text primary: #141414 (Charcoal)
- Text secondary: #4e4d4c (Graphite)
- Accent / primary action: #94e130 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #94e130 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature Card**: White #ffffff background, 1px #e7e7e7 border, 10px border-radius, 32px padding. 40x40px icon square in #94e130 (lime) at top-left with 10px radius, containing a white outlined icon. Title at 20px Figtree weight 500 in #141414. Body at 16px Figtree weight 400 in #4e4d4c.



5. **Carousel Control Row**: Two 32px circular buttons, 1px #141414 border, white fill, centered arrow icons. Horizontally centered, 24px gap between them, placed 24px below the card row.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
