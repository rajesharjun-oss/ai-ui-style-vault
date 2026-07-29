# Netflix Design Reference

## North Star

Build a cinematic streaming interface where the house lights are down and the content is the event. The canvas should be pure black, the typography should be direct and high contrast, and the only saturated signal should be Netflix Red. Everything else exists to make posters, trailers, and signup actions feel immediate.

The style is not a generic dark dashboard. It is a content theater with one red action language.

## Theme

- Mode: dark.
- Canvas: pure black.
- Accent: Netflix Red.
- Text: chalk white.
- Secondary text: silver gray.
- Shape: simple rectangles with restrained rounding.
- Depth: imagery, gradients, and layering rather than shadows.

## Color System

Core colors:

- Netflix Red: `#e50914` for the logo, primary CTAs, active indicators, and key interactive moments.
- Feature Card Gradient Base: `#1d153f` for tokenized card backgrounds.
- Feature Card Gradient: `linear-gradient(149deg, #192247, #210e17)` for secondary feature cards.
- Deep Space: `#000000` for all main page and section backgrounds.
- Graphite: `#2d2d2d` for subtle surfaces and component backgrounds.
- Charcoal: `#414141` for inactive controls and deeper component surfaces.
- Slate: `#5a5a5a` for borders on inputs and interactive elements.
- Ash: `#808080` for placeholder text and quiet icons.
- Silver: `#b3b3b3` for footer links and secondary body copy.
- Chalk White: `#ffffff` for primary headings, body text, and icon fills.

Use red with discipline. If everything is red, nothing feels urgent.

## Typography

Primary family: `Netflix Sans`.  
Substitutes: Roboto, Inter, system sans.

Rules:

- Use one type family across the experience.
- Use 700 or 900 for major promotional headlines and ranking numerals.
- Use 400 and 500 for form labels, body text, footer links, and minor controls.
- Avoid decorative display fonts.
- Keep headings direct, compact, and high contrast.

Type scale:

- Caption: 13px, line-height 1.5.
- Body: 16px, line-height 1.5.
- Subheading: 20px, line-height 1.25.
- Heading small: 24px, line-height 1.2.
- Heading: 56px, line-height 1.17.
- Display: 100px, line-height 1.

## Layout

- Page max width: about 1280px.
- Full-bleed black background.
- Hero should feel viewport-scale and centered.
- Header should be minimal, usually logo left and utility actions right.
- Main content should stack horizontal shelves and multi-column card grids.
- Section gap: about 48px.
- Card padding: 24px.
- Element gap: 16px.

The page should feel like an endless browsable library, not a brochure.

## Shape

- Buttons: 4px radius.
- Inputs: 4px radius.
- Large content cards: 16px radius.
- Promotional banner: 8px radius.
- Keep poster art sharp and rectangular.

The geometry should be functional, not playful.

## Elevation

Avoid traditional box shadows.

Use depth through:

- Pure black surroundings.
- Dimmed poster-collage backdrops.
- Deep gradient feature cards.
- High-contrast white text.
- Content imagery that glows against black.

## Imagery

Imagery is the product.

- Use high-quality poster art, movie stills, or show thumbnails.
- Hero can use a dimmed full-bleed collage behind the signup copy.
- Shelves should use vertical poster cards with little or no framing.
- Trending cards can overlay large 100px ranking numerals.
- Feature icons may use subtle dimensional gradients, but UI controls stay flat.

## AI Build Notes

Start with a black page, red logo, minimal header, centered signup hero, and one email input plus red CTA. Add poster shelves and gradient feature cards after the hero. Keep the UI dark and disciplined; the media art provides the visual richness.

