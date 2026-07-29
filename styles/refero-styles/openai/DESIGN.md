# OpenAI Style Reference

## North Star

OpenAI reads like a research lab notebook at noon. The interface feels quiet, editorial, and exact: white page, black type, soft hairlines, pill controls, and very little decoration.

The system should feel confident because it removes noise. It should not feel sterile through tiny text or harsh spacing; the rhythm comes from generous margins, readable body copy, and very deliberate contrast.

## Color

OpenAI is almost monochrome. The primary action color is not a brand hue; it is black. The rest of the palette is white, muted grays, and translucent black borders.

- `Obsidian` `#000000`: primary text, filled CTA, strongest emphasis.
- `Graphite` `#666666`: captions, helper copy, muted labels, secondary navigation.
- `Smoke` `#8f8f8f`: tertiary copy, disabled controls, placeholder text, icon strokes.
- `Paper` `#ffffff`: page background, cards, panels, input fills.
- `Ash` `#f1f1f1`: subtle surface fills, hover states, language selector style surfaces.
- `Hairline` `rgba(0,0,0,0.12)`: borders, dividers, outlines.
- `Whisper` `rgba(0,0,0,0.04)`: tiny hover and support accents only.

Do not introduce accent colors, gradients, colorful CTA states, or large gray background blocks. The style loses its clarity as soon as color starts competing with the typography.

## Typography

Use OpenAI Sans as the primary typeface, with Inter, Sohne, system-ui, and sans-serif as fallbacks.

The type is readable and gently compressed at larger sizes:

- Body: 17px, line-height 1.65, weight 400, letter-spacing -0.01em.
- Standard UI: 14px, weight 500, compact line-height for nav and buttons.
- Small label: 13px, weight 500, line-height about 1.5.
- Subhead: 18px to 22px, weight 500, letter-spacing -0.01em.
- Section heading: 28px, weight 600, line-height 1.21, slight positive tracking.
- Display: 48px, weight 500, line-height 1.16, letter-spacing -0.03em.

Avoid weights 700 and 800. The system should feel editorial, not loud.

## Spacing And Layout

The spacing density is comfortable. Use a 4px base unit, a max content width around 1200px, and generous section gaps around 32px to 64px.

The most recognizable layout pattern is a centered hero prompt area followed by an asymmetric editorial grid:

- Top nav is restrained, about 64px tall.
- Hero area is mostly empty white canvas with a centered pill prompt/search input.
- Prompt chips sit below the input in a centered row.
- Content below uses a large featured article on the left and smaller stacked cards on the right.
- Footer is multi-column, text-led, and quiet.

Avoid sidebars, marketing gradients, large decorative backgrounds, and dense dashboard framing.

## Shape And Elevation

Controls are pill-first:

- Buttons, tags, chips, and inputs: 9999px radius.
- Cards and images: 6px radius.
- Tiny utility surfaces may use 4px, but do not make it a dominant motif.

Elevation is minimal. Use no card shadows. Structure should come from whitespace, typography, borders, and image size.

## Components

### Filled Action Button

Use solid black with white text. Keep it rare, usually for the single most important action such as `Try ChatGPT`.

### Outlined Pill Button

Use transparent fill, black text, and a 1px hairline border. This is the default for prompt chips, filters, and secondary actions.

### Ghost Text Button

Use black or muted text with no border. This fits nav links, breadcrumbs, and low-pressure actions like `Log in`.

### Search Or Prompt Input

Use a pill shell with a hairline border, transparent or white fill, black text, and Graphite placeholder copy. Keep the interaction calm; avoid bright focus rings.

### Article Card

Cards are mostly image plus typography. Keep backgrounds transparent or Paper, no shadow, 6px image radius, and no heavy internal padding.

### Top Navigation

Use a white 64px nav with a text wordmark, simple text nav items, a search utility icon, a ghost login link, and one black pill CTA.

## Imagery

Imagery should feel documentary, editorial, and research-adjacent. Use real product, people, lab, article, or abstract research visuals with restrained color. Do not use glossy SaaS illustrations, 3D mascot art, gradients, or neon tech backgrounds.

## Do

- Use black as the only filled CTA color.
- Use `rgba(0,0,0,0.12)` for borders and outlines.
- Use 9999px radius for buttons, tags, and inputs.
- Use 6px radius for cards and images.
- Use 17px body copy with generous line-height.
- Trust white space over panels and dividers.
- Keep navigation text-led and calm.

## Do Not

- Do not add accent colors, gradients, or colorful brand fills.
- Do not use card shadows.
- Do not use non-pill buttons.
- Do not use bold display weights.
- Do not shrink body copy below 16px.
- Do not use colored section backgrounds.
- Do not add icons inside every button.
