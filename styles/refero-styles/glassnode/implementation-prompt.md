# AI Implementation Prompt

Build a Glassnode-inspired crypto analytics UI. Use it as a style reference, not as a clone of the source site.

## Required Feel

The interface must feel like a sober institutional research console: cool gray canvas, white cards, black and gray typography, hairline borders, 2px components, and chart-first imagery. It should feel data-rich but carefully organized.

## Core Rules

- Use `#edeff2` as the page canvas.
- Use `#ffffff` for cards, inputs, and elevated surfaces.
- Use `#1a1a1a` for dark editorial bands.
- Use `#000000` or `#1a1a1a` for primary filled buttons on light surfaces.
- Use inverse white buttons on dark bands.
- Do not invent a colored CTA.
- Use `#e2e7fc` only as a soft accent wash or chart fill.
- Use Inter for nearly all text.
- Use a geometric bold display face only for the 56px hero headline.
- Keep all radii at 2px.
- Use 1px `#dedfe1` borders for cards, inputs, and dividers.
- Avoid gradients, colored icons, and decorative photography in product UI.

## Suggested Page Structure

1. Dark announcement bar.
2. White top nav with logo, links, ghost CTA, and filled dark CTA.
3. Light hero with left-side headline/copy/CTA and right-side chart widget.
4. Dark feature band with chart illustration and bullet list.
5. Light report grid with partner report cards.
6. Monochrome logo strip on cloud canvas.
7. Dark subscribe band with inverse email form.
8. Dark footer with compact link columns.

## Component Recipes

Primary filled button:

- Background: `#000000` or `#1a1a1a`.
- Text: `#ffffff`.
- Font: Inter, 16px, weight 500.
- Padding: 12px 24px.
- Radius: 2px.
- Shadow: subtle 2px button drop.

Ghost outline button:

- Background: transparent or white.
- Text: `#000000`.
- Border: `1px solid #000000` or `#dedfe1`.
- Font: Inter, 14-16px, weight 500.
- Padding: 10px 20px.
- Radius: 2px.

Hero chart widget:

- Background: `#ffffff`.
- Border: `1px solid #dedfe1`.
- Radius: 2px.
- Shadow: layered hero widget shadow.
- Include tab header, line chart, pale lavender area fill, and compact search/select input.

Partner report card:

- Background: `#ffffff`.
- Border: `1px solid #dedfe1`.
- Radius: 2px.
- No shadow.
- Cover image at top.
- 16px content padding.
- 12px uppercase label in `#6f6f6f`.
- 20px title, Inter 700, black.
- 14px description, `#5a5a5a`, clamp to 3 lines.

Dark feature block:

- Background: `#1a1a1a`.
- Two-column grid.
- Heading: Inter 24px, weight 700, white.
- Body: Inter 16px, `#a0a0a0`.
- Use white or gray chart-line icons only.

Subscribe form:

- Background band: `#1a1a1a`.
- Input: white background, `1px solid #dedfe1`, 2px radius.
- Placeholder: `#808080`.
- Submit: white fill, black text, 2px radius.

## Do Not

- Do not use saturated brand colors, colorful gradients, or colored icon fills.
- Do not use radius above 2px.
- Do not use glow effects.
- Do not use the display face for small text.
- Do not place white cards on white backgrounds without borders.
- Do not break the 8px spacing scale.
- Do not make the product UI photographic or playful.

