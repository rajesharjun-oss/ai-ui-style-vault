# PostNew

Source: [Refero Style](https://styles.refero.design/style/4f76756b-0f06-47a3-baad-d3846b23e132)
Reference site: [https://www.postnew.xyz](https://www.postnew.xyz)
Captured: 2026-07-31
Refero published: 2026-04-30T03:26:59.852Z
Refero modified: 2026-06-05T10:54:52.156Z
Theme: dark
Category: Design

## Style Summary

Explore PostNew's dark Design design system: Canvas Black #1a1a1a, Bone White #fafafa colors, ABC Diatype Medium, System Sans-Serif typography, and...

North star: After-hours gallery with daylight spreads

## What To Borrow

- Canvas Black `#1a1a1a` for Page background, gallery vitrine, frame around content - a near-black not-quite-pure-black that lets imagery breathe without the harshness of #000
- Bone White `#fafafa` for Primary text, nav labels, icon strokes, light surface fill - the only light token, reserved for foreground against Canvas Black
- Slate Surface `#242424` for Elevated cards, button backgrounds, secondary surface panels - one step lighter than canvas to create depth without contrast drama
- Ash `#5d5d5d` for Muted UI elements, inactive dots, decorative fills - the 6.3:1 ratio against white keeps it legible but clearly secondary
- Absolute Black `#000000` for Hairline borders, high-contrast text, deepest shadow line - used sparingly where maximum definition is needed against the canvas

- ABC Diatype Medium `--font-abc-diatype-medium` for Editorial display and body - the only display face, used at just two sizes (18px / 22px) with -0.025em tracking. The single weight (500) is deliberate: no bold, no light. The OpenType features (blwf, cv03-cv11, ss09-ss10) activate specific character alternates that give it a subtly editorial personality. Substitute with Inter Tight Medium or Sohne Medium if ABC Diatype is unavailable.
- System Sans-Serif `--font-system-sans-serif` for UI chrome only - nav labels (Index, Feed, Profile), view toggle icons, scroll dots. At 12px it is intentionally small and quiet, the typographic equivalent of architectural labeling. Do not promote to editorial content.

## Avoid

- Do not introduce saturated brand colors, accent hues, or semantic states (success/error/warning) - they break the achromatic gallery frame.
- Do not round corners on cards, buttons, images, or frames - 0px radius is structural to the system.
- Do not add shadows or elevation effects - depth comes from #1a1a1a #242424 #5d5d5d surface steps, not from box-shadows.
- Do not use more than two type sizes from ABC Diatype - 18px and 22px are the complete editorial scale.
- Do not use the system sans above 12px - it is chrome-only typography, not editorial.
- Do not center-align editorial body text - the design uses flush-left or full-bleed compositions, not centered paragraphs.
- Do not add gradients - the system is flat; any gradient breaks the gallery wall metaphor.

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
