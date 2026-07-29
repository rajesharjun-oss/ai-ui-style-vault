# Implementation Prompt

Build the UI in the Letter Refero style.

Create a premium private-banking gallery interface. Start with a full-bleed dark vault hero on `#191b1f`, then move into white and mist-white editorial sections with tinted product panels. Use high-contrast serif headlines and extended-grotesque UI text. Keep the interface flat, square, and precise. Let 3D metallic/prismatic renders provide the visual depth.

Color rules:

- Dark hero and dark nav: `#191b1f`.
- Main light canvas: `#ffffff`.
- Soft alternate surface: `#f6f9f9`.
- Muted text: `#9fabad`.
- Hairlines and low-contrast borders: `#e6ebec`.
- Tinted product panels: `#fcede1`, `#eefcef`, `#e6def0`.
- Filled action colors: `#186f64`, `#536eff`, `#154ea5`.
- Do not use action colors for body text, broad backgrounds, or ordinary borders.

Typography rules:

- Headlines must use an Albra Sans-like serif.
- Body, nav, buttons, links, and card descriptions use a Neufile Grotesk Extended-like sans.
- Hero headline: 80px, 600, 1.1 line-height, positive tracking.
- Section heading: 46px, 600, 1.2 line-height.
- Product card heading: 22px serif, 600, 1.2 line-height.
- Body text: 16px sans, 400, 1.4 line-height.

Layout rules:

- Max content width: 1200px.
- Section gaps: 64-96px.
- Product card padding: 32px.
- Use white and mist-white sections after the dark hero.
- Use 50/50 split sections with text on the left and 3D render on the right.
- Use two-column tinted feature cards for product rows.

Component rules:

- Buttons use 2px radius, 12px vertical padding, and 27px horizontal padding.
- Filled buttons are teal, violet, or blue and have no shadow.
- Place a matching-color ghost text link beside filled actions.
- Cards are 0px radius with no shadow or border unless a hairline is structurally needed.
- 3D renders float without masks, borders, shadows, or containers.
- Gradients belong only inside renders or light effects, not UI components.

Avoid rounded friendly UI, pill buttons, card shadows, glass effects, generic SaaS grids, flat illustrations, stock photography, and sans-serif headlines.

