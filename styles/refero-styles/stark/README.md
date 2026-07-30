# Stark

Source: [Refero Style](https://styles.refero.design/style/ea9c37e8-c56c-42aa-8e81-9b55222a5cd3)
Reference site: [https://www.getstark.co](https://www.getstark.co)
Captured: 2026-07-30
Refero published: 2026-04-30T03:35:01.793Z
Refero modified: 2026-06-05T13:00:11.641Z
Theme: light
Category: SaaS

## Style Summary

Explore Stark's light SaaS design system: Midnight Navy #10284b, Stark Violet #381fd1 colors, ArminGrotesk, RobotoMono typography, and DESIGN.md for AI agents.

North star: midnight lecture hall with yellow highlighter

## What To Borrow

- Midnight Navy `#10284b` for Hero background, primary headings, footer surface - the dominant brand color establishes authority and anchors the dark-to-light page split. Used as a background field for the above-the-fold section and as body-text color on the cream secondary surface
- Stark Violet `#381fd1` for Primary action fills (Get started, Sign up, Request demo), card border accents, active nav state, decorative icon strokes, and inline emphasis text. The vivid violet against midnight navy creates a switched-on, electric feel without aggression
- Highlighter Yellow `#fedb63` for Diagonal text-highlight gradient fill, one specific secondary CTA, and illustration accent. Yellow never decorates broadly - it marks, underlines, and punctuates specific words within dark-on-light headlines
- Lilac Tint `#e5e0ff` for Soft button surface variant, gentle tinted card backgrounds. A desaturated wash of the violet brand that softens interactive elements without competing with the primary action
- Mint Splash `#99d6cc` for Decorative illustration accent in feature cards and dashboard widgets. Used sparingly in flat geometric shapes within artwork, not in core UI controls
- Page Canvas `#faf5ff` for Lightly purple-tinted near-white page background. The faint violet cast unifies the cream and white surfaces under one chromatic family
- Cream Field `#f6f6eb` for Secondary section surface and body-text color on the dark hero. The warm greenish-cream provides a relaxed counterpoint to the midnight navy and is the dominant body-text/link color on the dark section
- Carbon `#000000` for Body text on light surfaces, icon strokes, and high-contrast elements. Not used as a background - the system prefers the midnight navy for darkness
- Pure White `#ffffff` for Text on dark hero, card surfaces, nav backgrounds, product screenshot frames. The bright surface that holds product imagery and dashboard content
- Hairline Gray `#e5e7eb` for Universal border color for cards, inputs, dividers, link underlines, and structural separators. The single achromatic border workhorse

- ArminGrotesk `--font-armingrotesk` for The single custom typeface carries the entire brand voice. Weight 900 is the hero display weapon (110px headline) - used at maximum volume for the opening statement. Weight 600 handles section headings and subheadings (24-48px). Weight 500 is the button and label workhorse. Weight 400 is body text. The geometric grotesque construction gives a contemporary, slightly technical authority.
- RobotoMono `--font-robotomono` for All-caps eyebrow labels and section markers (e.g., 'EXPLORE THE STARK PLATFORM', 'SPEED UP DESIGN & DEV'). The monospaced mono with wide tracking creates a distinct utilitarian signal that sits above the display heading and below the nav - a consistent navigational breadcrumb layer.

## Avoid

- Do not use weight 400 or 500 for the hero display headline - the 900 weight at 110px is the brand's signature and must be deployed at maximum volume.
- Do not apply the yellow highlighter gradient to more than 2-3 words in a single headline; it dilutes the marking-pen effect.
- Do not use shadows for cards on the cream or light purple surfaces - the system prefers flat surfaces with hairline borders.
- Do not introduce a second brand-violet shade; #381fd1 is the single chromatic action color and must remain uncontested.
- Do not set body text below 16px or use letter-spacing wider than -0.01em at display sizes - the tight tracking is essential to the geometric grotesque feel.
- Do not place CTA buttons on the midnight-navy hero without sufficient contrast padding or a distinctive fill - the violet and yellow must be the only bright spots on the dark field.
- Do not use the cream (#f6f6eb) as a background for the hero - it is exclusively a secondary-section surface that appears after the dark fold.

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
