# Morphic

Source: [Refero Style](https://styles.refero.design/style/1d4cbd69-ee0f-4f13-ba7d-14d3eaed7349) 
Reference site: [https://morphic.com](https://morphic.com) 
Captured: 2026-07-29 
Refero published: 2026-05-07T18:58:00.502Z 
Refero modified: 2026-06-03T19:35:01.756Z 
Theme: dark 
Category: AI

## Style Summary

Explore Morphic's dark AI design system: Pure Black #000000, Surface One #212121 colors, Inter typography, and DESIGN.md for AI agents.

North star: Dark cinema canvas for AI storytelling. Pure black absorbs everything except the blue pulse of a single accent and the glow of generated imagery.

## What To Borrow

- Pure Black `#000000` for Page canvas, hero backgrounds, full-bleed sections - the void that makes all imagery and accent color read as luminous
- Surface One `#212121` for Primary card surface, elevated panels, and section backgrounds one level above the canvas
- Surface Two `#292929` for Secondary button background (ghost/outlined), nested cards, and hover surfaces one step lighter than Surface One
- Surface Three `#333333` for Tertiary button background, highest elevation layer, and active-state surface tints
- Paper White `#ffffff` for Primary headings, button text, logo, and high-emphasis copy on dark surfaces
- Fog `#e5e7eb` for Hairline borders and dividers - applied at very low opacity so cards have edge definition without visual weight
- Mist `#f5f5f5` for Soft highlight washes, secondary text on light surfaces, and subtle icon fills
- Mid Gray `#999999` for Muted body text, inactive labels, and disabled-state copy
- Steel `#737373` for Link text in resting state, secondary annotations, and icon strokes at low contrast
- Graphite `#666666` for Tertiary headings, caption text, and supporting metadata
- Slate `#525252` for Lowest-emphasis body text, helper copy, and subdued annotations
- Charcoal `#404040` for Icon strokes and outlines at medium contrast, secondary borders
- Electric Blue `#0075ff` for Blue action color for filled buttons, selected navigation states, and focused conversion moments.

- Inter `--font-inter` for Sole typeface across all UI, headings, and body. The complete weight range (400-700) allows a single family to carry the full hierarchy: 700 for display headlines, 600 for section headers, 500 for buttons and nav, 400 for body and captions. Inter's geometric neutrality and tall x-height make it ideal for a dark canvas where character width and spacing carry more visual weight than personality.

## Avoid

- Never use a second chromatic color - the system is deliberately monochromatic with one blue accent; adding any other hue breaks the cinema-canvas concept
- Never apply drop shadows to UI components - shadows are reserved for image cards in the showcase grid only
- Never use #ffffff text for body copy - body text should be #999999 or lower contrast; white is reserved for headings, buttons, and high-emphasis labels
- Never center-align body paragraphs - only headlines, CTAs, and the hero text block are centered; body copy is left-aligned
- Never use border-radius values outside the defined scale (7px, 10px, 16px, 24px, 32px, 100px) - ad-hoc radii will break the system's geometric consistency
- Never place a colored background behind text blocks - the canvas must remain pure black; cards float on the void, they don't fill it
- Never use gradient backgrounds - the system is strictly flat; depth comes from the surface stack, not color transitions

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
