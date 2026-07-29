# Layout And Imagery

## Layout

- Full-bleed dark canvas with max-width 1200px inner content.
- Sticky top navigation with glass blur, logo, ghost nav buttons, login link, and white CTA.
- Centered hero with oversized serif headline.
- Compact AI prompt or CTA module below the headline.
- Section gaps around 80px.
- Category grid is typically 3 columns with 12-15px gaps.
- Product mockup sections can use heavy internal padding around 90px.
- Light or silver panels should appear as deliberate interruptions, not as the default surface.

## Imagery

- Use full-bleed cloud or sky photography for the hero atmosphere.
- Keep imagery cool, desaturated, and aspirational.
- Show product through tilted iPhone renders on dark stages.
- Use minimal monoline SVG icons in white or black.
- Avoid lifestyle photography, generic abstract shapes, and bright decorative illustrations.

## Gradients

```css
--gradient-dark-chrome: linear-gradient(135deg, rgb(43, 43, 44), rgb(19, 19, 19));
--gradient-sky-atmosphere: linear-gradient(rgb(15, 16, 17), rgb(19, 29, 39) 18%, rgb(26, 71, 136) 37%, rgb(64, 138, 193) 69%, rgb(64, 138, 193) 102%);
```

Use gradients for atmospheric backgrounds or product chrome only. Do not apply them to text, buttons, or feature-card fills.

## Motion

- State transitions: 0.2s ease.
- Atmospheric reveal: 2.5s cubic-bezier(0.455, 0.03, 0.515, 0.955).
- Border trace animation may be used sparingly.
- Avoid bouncy, overshooting, or highly playful movement.

