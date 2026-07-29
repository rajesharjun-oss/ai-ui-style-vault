# Implementation Prompt

Build a UI in the (dot)connect style.

Create a warm off-white, Swiss-engineering interface where typography, whitespace, borders, and one ember-orange accent do the work. The page should feel architectural, precise, and premium, with a text-first hero and sparse abstract 3D object imagery.

Use these hard rules:

- Page canvas: `#fcfbf8`.
- Primary text and dark action fill: `#001011`.
- Secondary text: `#0f1e1f`.
- Card and hover surface: `#ededea`.
- Hairline border: `#c1c4c2`.
- Rare orange accent: `#fd5321`.
- Secondary outline action only: `#007aff`.
- Use Ember orange at most once per viewport.
- Do not use Signal Blue as a filled background.
- Do not use shadows, glows, gradients, or blur.
- Use 1px hairline borders for structure.
- Use AeonikPro as the primary typeface with Inter, Satoshi, and General Sans as fallbacks.
- Enable `font-feature-settings: "dlig" on, "ss02" on, "ss08" on;`.
- Use only weights 400 and 500.
- Display type should be 72px to 101px with line-height 0.8 to 0.9 and tracking around -0.025em.
- Body text should stay between 16px and 21px with slight positive tracking.
- Cards use 20px radius.
- Buttons use 24px radius.
- Arrow pill buttons use 44px radius and include a 32px circular icon slot.
- Use 96px vertical section rhythm.

Build a text-only hero on Bone Canvas. Center the display headline, keep the body copy around 60ch, and place a charcoal arrow-pill CTA below it. Use an Ember button only for a high-intent header or conversion CTA. Add offer cards with 1px borders and no shadows. Add sparse full-width abstract 3D object interludes between text-heavy sections. Do not use photography or lifestyle imagery.

