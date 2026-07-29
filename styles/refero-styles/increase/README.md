# Increase

Source: [Refero Style](https://styles.refero.design/style/1ad4f49f-275a-4268-8ed1-677dc3c6e475) 
Reference site: [https://increase.com](https://increase.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T01:34:21.920Z 
Refero modified: 2026-06-03T21:11:54.282Z 
Theme: light 
Category: Fintech

## Style Summary

Explore Increase's light Fintech design system: Inkwell Navy #1a2b3b, Slate 600 #314352 colors, Untitled Sans, Input Mono typography, and DESIGN.md for AI...

North star: institutional blueprint on vellum - one electric chartreuse stripe cuts the navy calm, mint data signals pulse beneath it.

## What To Borrow

- Inkwell Navy `#1a2b3b` for Primary text, nav text, icon strokes, hairline borders - the structural graphite of every screen. Used as filled button background for primary actions to project institutional weight rather than enthusiasm
- Slate 600 `#314352` for Secondary borders and supporting text where Inkwell Navy is too heavy - outlines on cards, tertiary headings, subdued dividers
- Abyss `#0d1726` for Dark code-block and terminal surfaces - deeper than Inkwell Navy so syntax highlighting reads with high voltage against the near-black
- Graphite `#687887` for Muted helper text, inactive nav links, secondary button outlines - recedes so the navy headlines and mint accents can carry the hierarchy
- Steel `#8995a1` for Tertiary text and disabled-state borders - the quietest navy in the scale, used where information is supplementary
- Fog `#edf0f2` for Page canvas - the warm off-white that holds all content; section bands alternate with pure white to create quiet vertical rhythm
- Pure White `#ffffff` for Card surfaces, form inputs, nav background - the elevated layer that floats above Fog with minimal shadow
- Silver `#caced2` for Hairline dividers, input borders at rest, table separators - the thread that separates without announcing itself
- Mist `#e1e5e9` for Card edges and subtle surface tints where a second neutral step is needed between white and Fog
- Pewter `#bdc2c8` for Body-level borders, subtle rule lines, the quietest non-white neutral
- Voltage `#e4ff33` for Announcement bar, high-attention data highlights, occasional feature accent - the single chromatic punctuation that earns the eye's attention by being used sparingly. Never decorates, always signals
- Mint Signal `#31f2bf` for Green outline accent for tags, dividers, and focused UI edges

- Untitled Sans `--font-untitled-sans` for Primary interface and display typeface - custom geometric grotesque. Weight 400 runs the body and UI; weight 500 lifts subheadings; weight 700 anchors the wordmark. Negative letter-spacing (-0.04em at display sizes, -0.01em at body) tightens the grotesque into a dense, architectural feel - the closer the eye gets to a heading, the more the letters close ranks, producing a precise, financial-document quality.
- Input Mono `--font-input-mono` for Code, API identifiers, numerical data, and inline technical labels. Alternates and stylistic sets ss01/ss02/ss12 are active - these micro-detailed glyph variants give the monospace a humanist, designed quality rather than a default-terminal feel, reinforcing that the product is engineered with intention.

## Avoid

- Don't use Mint Signal (#31f2bf) or Voltage (#e4ff33) as a primary button fill - they are signal colors, not action colors.
- Don't add a second saturated accent - the system runs on navy + chartreuse + mint only; introducing a fourth chromatic breaks the institutional register.
- Don't use straight #000000 for text on white surfaces - Inkwell Navy reads as authoritative while pure black reads as unfinished.
- Don't soften the hero gradients with blur or rounded edges - the angular, faceted geometry is what makes them read as financial infrastructure rather than marketing artwork.
- Don't use letter-spacing greater than -0.01em at body sizes - the negative tracking is what makes Untitled Sans feel architectural; loosening it dissolves the brand.
- Don't promote the code-syntax blue (#33bbff) into the UI palette - it exists only inside the code-block context.
- Don't add a dark mode variant without rebuilding the canvas as a warmer near-black (#0d1726-family) - the cool gray-navy scale does not invert cleanly to a black scale.

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
