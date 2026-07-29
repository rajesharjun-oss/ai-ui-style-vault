# Lusion

Source: [Refero Style](https://styles.refero.design/style/1b44386e-31a8-40b0-a577-27c088b51264) 
Reference site: [https://lusion.co](https://lusion.co) 
Captured: 2026-07-29 
Refero published: 2026-01-28T19:49:45.000Z 
Refero modified: 2026-06-05T04:12:58.340Z 
Theme: light 
Category: Agency

## Style Summary

Explore Lusion's light Agency design system: Lavender Mist #f0f1fa, Paper White #ffffff colors, Aeonik typography, and DESIGN.md for AI agents.

North star: 3D sculpture gallery on a frosted lavender plane. Every interface element should feel like a tactile object resting on a pale, slightly cool gallery floor, with the 3D content doing all the chromatic and dramatic work.

## What To Borrow

- Lavender Mist `#f0f1fa` for Page canvas - the dominant background, a cool off-white with a barely-perceptible lavender cast that makes pure black text feel sharper than it would on pure white
- Paper White `#ffffff` for Elevated card and surface backgrounds, button text on dark fills, inverted surfaces
- Ink `#000000` for Primary text, all headings, body copy, icons, and link text - pure black with no softening
- Graphite `#2b2e3a` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Haze `#e4e6ef` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Slate Hollow `#34393f` for Deep surface layer for dark bands or modal overlays, darker than graphite for clear hierarchy separation
- Electric Indigo `#1a2ffb` for Chromatic brand accent - appears as icon stroke, inline highlight marks, and as the signature color inside the 3D hero render. The single source of energy against the otherwise achromatic UI
- Acid Lime `#c1ff00` for Highlight wash for emphasis zones, secondary accent inside 3D compositions - used sparingly as a surprise contrast

- Aeonik `--font-aeonik` for Used for every text element on the site - navigation, body, headings, buttons, inputs. The deliberate weight ceiling at 500 (no bold) and uniformly tight -0.02em tracking create a uniform geometric confidence. Display sizes compress line-height to 0.90, letting the largest headlines (108-144px) feel sculpted rather than set. The 400 weight is the workhorse; 500 is reserved for navigation, labels, and button text where a slight emphasis is needed.

## Avoid

- Don't introduce a third type weight above 500 - bold or black weights break the restrained typographic system
- Don't use white (#ffffff) as the page background; the Lavender Mist canvas is what makes black text and 3D content feel cut and crisp
- Don't fill large UI surfaces with Electric Indigo; it is an accent, not a brand wash - large indigo blocks destroy the gallery-floor metaphor
- Don't add decorative gradients, glassmorphism, or blur effects; surfaces are flat and physical
- Don't use 8px, 12px, or 20px border-radii on cards, buttons, or containers - stick to the defined 3px, 15px, 18px, 87.5px, and 100px values
- Don't add hover states that change background fill or introduce color; rely on opacity shifts and underline reveals against the static canvas
- Don't use the Acid Lime (#c1ff00) as a CTA or text background; it lacks the contrast hierarchy needed for interactive elements and belongs only inside 3D compositions or highlight washes

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
