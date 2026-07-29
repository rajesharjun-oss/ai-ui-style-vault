# Implementation Prompt

Build a dark motion-library interface in the GSAP style.

Use Just Black (`#0e100f`) as the page canvas, not pure black. Use Surface Cream (`#fffce1`) for headings, body copy, nav links, button text, and button borders, not pure white. Use Off Black (`#191919`) for nested dark surfaces and the footer. Use Surface 25 (`#42433d`) for hairline dividers and low-contrast outlines. Use Surface 50 (`#7c7c6f`) for muted copy and idle labels.

Color is taxonomy. Keep this mapping fixed: GSAP/Core = green (`#0ae448` and `#abff84`), SVG = orange (`#ff8709`), Scroll = pink (`#fec5fb`), Text = lilac (`#9d95ff`), UI = blue (`#00bae2`). Lipstick Pink (`#f100cb`) is only a deep decorative gradient stop. Do not use these colors as random accents.

Use Mori or a close Inter Tight/Sohne/DM Sans fallback as the only type family. Body and UI text use weight 400 at 16px to 19px with line-height 1.15. Large display uses weight 600. The hero headline should reach 224px, line-height 0.9, -0.02em tracking, and may bleed toward viewport edges. Do not add a second font.

Use a 4px base grid, 1280px max content width, 80px section gaps, 24px card padding, and 16px element gaps. Cards and small tags use 8px radius. All main buttons are outlined pills with 100px radius. No filled CTA buttons. The primary CTA can be a transparent pill with a 1.5px to 2px green-to-light-green gradient stroke.

Expected components:

- Hero display headline: Surface Cream, Mori 224px/600, line-height 0.9, tight tracking, overlapping organic gradient shapes.
- Outlined cream pill button: transparent, Surface Cream text and border, 100px radius, 15px by 24px padding, Mori 18px/600.
- Gradient-stroked CTA pill: transparent fill, green gradient border, Surface Cream text, 100px radius.
- Category color label: single-word discipline name in its fixed mapped color.
- Curly-bracket annotation: small Surface Cream label like `{ Tools }` before each section.
- Tool feature block: two-column row, organic gradient illustration, category label, cream heading, body copy, outlined pill, and 1px Surface 25 divider.
- Organic gradient illustration: soft 3D-like pill/blob/dome tied to the discipline color, no drop shadow, loose overlap.
- Showcase card: Off Black, 8px radius, 24px padding, cream heading, contained preview.
- Footer: Off Black, Surface 25 top divider, cream multi-column links.

The page should feel kinetic, typographic, and showcase-like. Avoid filled buttons, random neon, pure white, pure black, drop shadows, stock photos, dashboard screenshots, and conventional SaaS card grids.
