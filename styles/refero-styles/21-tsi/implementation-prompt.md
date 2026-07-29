# Implementation Prompt

Use the 21 TSI style for this UI.

Create a dark luxury-fashion editorial interface. The page canvas is true black (`#000000`). UI text, borders, hairlines, and simple primitive shapes are white (`#ffffff`). The only color should come from full-bleed editorial photography with crimson lighting around `#b62b1a`; do not apply crimson as a CSS background, border, or CTA color.

Typography:

- Use Saans for all text. If unavailable, use Inter or Manrope as a precise geometric sans fallback.
- Do not introduce a second typeface.
- Use 12px to 20px uppercase labels with weight 380 and positive tracking around `0.05em` or `0.6px`.
- Use oversized display type from 47px upward with weight 300 or 570, line-height 1.0 to 1.14, and tracking around `-0.025em`.
- Avoid intermediate heading sizes between 20px and 47px.

Layout:

- Do not use a max-width content container.
- Use full-bleed sections and images.
- The hero photograph should be 100vw wide and around 90vh tall.
- Do not place body text or primary headlines on top of the photograph.
- Give large display headlines their own black space above or below image sections.

Components:

- Top nav: 1px white hairline edge-to-edge, then 12px uppercase Saans labels in white.
- Logo: text `21|TSI`, with the vertical separator drawn as a 1px white bar.
- Ghost pill button: transparent fill, 1px white border, 70px radius, 10px 20px padding, 12px uppercase Saans, weight 380, 0.6px tracking.
- Active indicator: optional 4px white dot before a utility label.
- Body card: only when needed, black or transparent fill, 1px `#4d4d4d` border, 8px radius, 20px padding.
- Circular frame: square crop with 594px radius for rare portrait vignettes.

Imagery:

- Use a single fashion subject, profile or three-quarter pose, off-center composition, deep black shadows, warm crimson side lighting, bronzed skin, and motion in hair or fabric.
- No clean white studio background, no busy group scene, no direct-eye-contact portrait as the hero.

Avoid colored CTAs, soft shadows, glass effects, gradients, icon fonts, decorative illustrations, conventional SaaS containers, and dense information blocks. The result should feel like a luxury campaign interface, almost silent except for type and photography.
