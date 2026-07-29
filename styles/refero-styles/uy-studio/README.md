# UY Studio

Source: [Refero Style](https://styles.refero.design/style/b376d42c-b2cb-4a52-8cec-ebf19cf1883f)  
Reference site: [https://www.uy-studio.com](https://www.uy-studio.com)  
Captured: 2026-07-29  
Refero published: 2026-04-30T02:14:31.563Z  
Refero modified: 2026-06-05T07:22:27.322Z  
Theme: light  
Category: E-commerce

## Style Summary

Explore UY Studio's light E-commerce design system: Soot #24241f, Limestone #d1d3cf colors, GP, GTStandard-M typography, and DESIGN.md for AI agents.

North star: Monastic stone gallery a quiet concrete-walled space where perfume bottles sit on white plinths, lit by one weight-400 voice and four warm grays.

## What To Borrow

- Soot `#24241f` as Primary text, all icon strokes, hairline borders, nav links, footer text the single dark voice of the system
- Limestone `#d1d3cf` as Page canvas, announcement bar, nav background the warm-tinted near-gray that replaces white as the system's base tone
- Chalk `#e5e5e5` as Secondary surface, subtle borders, product photo backgrounds a slightly cooler neutral for layering atop Limestone
- Graphite `#333333` as Dark button fill the only filled surface in the system, used sparingly for a single tonal shift from the Soot text
- GP Universal typeface used for nav, body, headings, buttons, and footer at weight 400 only. The single-weight constraint is the signature: no bold, no light, no medium. Hierarchy comes from size (1348px) and tracking (0.0110em body, 0.0390em display), not weight contrast. The slight positive tracking gives the type an editorial, architectural quality. `--font-gp` for the source typography voice
- GTStandard-M GTStandard-M detected in extracted data but not described by AI `--font-gtstandard-m` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: cards 0px, images 0px, inputs 3px, buttons 0px

## Avoid

- Don't introduce bold, semibold, or light font weights. Weight 400 is the only voice adding weight would break the flat, even texture that defines the system.
- Don't add saturated colors, brand hues, or accent fills. The palette is four warm grays only any chromatic color would shatter the monastic quality.
- Don't use box-shadow or drop-shadow for elevation. Depth comes from the warm-gray surface stack (Limestone Chalk Graphite Soot), not from shadows.
- Don't round corners on cards, images, or containers. 0px everywhere except inputs. Rounded corners would soften the architectural, museum-pedestal feel.
- Don't use color or weight to indicate interactive states. Use Soot underlines on hover, position shifts on active, and the underline-on-current pattern for navigation state.
- Don't add decorative gradients, patterns, background textures, or ornamental graphics. The only imagery is product photography against real textures.
- Don't use filled, colored, or rounded icon buttons. Icons are stroke-only in Soot, inline with text at the same baseline. The interface is text-first.

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
