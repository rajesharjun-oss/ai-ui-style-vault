# My Brentano

Source: [Refero Style](https://styles.refero.design/style/d211aaa4-e09b-4ef9-a9bf-f6fa8495de73)
Reference site: [https://mybrentano.ch](https://mybrentano.ch)
Captured: 2026-07-30
Refero published: 2026-04-30T02:12:18.705Z
Refero modified: 2026-06-05T12:39:14.435Z
Theme: light
Category: E-commerce

## Style Summary

Explore My Brentano's light E-commerce design system: Charcoal Ink #212529, Pure Press #000000 colors, Studio Feixen Sans Writer Book Regular, Studio Feixen...

North star: Pharmacy broadsheet on cream paper. A Swiss editorial layout where one typewriter voice does all the speaking and warm-toned product photography supplies the only color.

## What To Borrow

- Charcoal Ink `#212529` for Body text, headings, nav text, footer text, most borders - the dominant text and structural color, slightly softer than pure black for warmth
- Pure Press `#000000` for Secondary text, button borders, link borders, input outlines, nav separators - true black for maximum contrast on outlined elements
- Bone White `#ffffff` for Page canvas, card surfaces, button fills, input backgrounds - the ground that all ink sits on

- Studio Feixen Sans Writer Book Regular `--font-studio-feixen-sans-writer-book-regular` for Studio Feixen Sans Writer Book Regular - detected in extracted data but not described by AI
- Studio Feixen Sans Writer `--font-studio-feixen-sans-writer` for Primary typeface for all text - body, headings, nav, links, buttons, lists. The Writer variant carries a typewriter/letterpress quality with subtle ink-trapped details that a geometric sans cannot replicate. Weight 700 is used sparingly only on the 60px display; everything else stays at 400, making the single bold moment feel intentional and declarative.
- Studio Feixen Sans `--font-studio-feixen-sans` for Secondary sans variant for select body passages and inputs where the typewriter serifs would be too loud. The same family, stripped of the Writer details, creates a quiet alternation within the same typographic world.

## Avoid

- Never introduce an accent or brand color - the system is intentionally near-monochrome, and color belongs only to photography
- Never apply shadows, glows, or any form of elevation - surfaces must remain flat like printed paper
- Never use bold weight (700) for anything smaller than 30px - the single bold moment must remain monumental
- Never round corners on cards, images, or input fields - 0px radius is non-negotiable
- Never use more than two typefaces per view; alternate between Writer and Sans within the same family only
- Never center-align body paragraphs or set them narrower than 50% of the viewport - the grid is left-aligned and generous
- Never apply a colored background to the page - the cream warmth comes from the paper-tone canvas and the imagery, not from a tint

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
