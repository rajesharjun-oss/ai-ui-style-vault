# Family - Style Reference

> Storybook spread on cream parchment: a friendly crypto product framed by warm paper surfaces, flat illustration accents, compact pills, and quiet pressed-in cards.

**Theme:** light

Family is a paper-first crypto product style. It uses a warm off-white canvas, restrained typography, flat cards with inset borders, and colorful hand-drawn illustration clusters to bring personality. Product surfaces should feel pressed into the page rather than floating above it. The system is playful through drawings and accent text, not through busy UI chrome.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Cream Canvas | `#fbfaf9` | `--color-cream-canvas` | Page background, full-bleed sections, nav surface |
| Stone Surface | `#f2f0ed` | `--color-stone-surface` | Card surface, grouped panels, inset border tone |
| Stone Border | `#e5d5c3` | `--color-stone-border` | Decorative hairlines and illustration borders |
| Pure White | `#ffffff` | `--color-pure-white` | Feature cards where hairline borders need to register |
| Sand Pill | `#f6f4ef` | `--color-sand-pill` | Secondary pill CTA background |
| Ink Black | `#121212` | `--color-ink-black` | Primary CTA fill, dark surfaces, strongest text |
| Heading Charcoal | `#343433` | `--color-heading-charcoal` | Headings, nav labels, illustration strokes |
| Body Brown | `#474645` | `--color-body-brown` | Body text and secondary copy |
| Muted Gray | `#7e7e7d` | `--color-muted-gray` | Helper text, inactive nav, tertiary labels |
| Ember Orange | `#ff3e00` | `--color-ember-orange` | Demo links, accent text, short emphasized phrases |
| Link Blue | `#0086fc` | `--color-link-blue` | Inline links and feature list emphasis |
| Sky Blue | `#64c6ff` | `--color-sky-blue` | Illustration fill and decorative accents |
| Alt Blue | `#00b2ff` | `--color-alt-blue` | Secondary illustration fill and icon accent |
| Grass Green | `#00c978` | `--color-grass-green` | Green accent text and decorative marks |
| Mint | `#00ca48` | `--color-mint` | Green wash and soft highlight areas |
| Sun Yellow | `#ffcd6c` | `--color-sun-yellow` | Illustration fill and warm decorative shapes |
| Gold | `#d48f00` | `--color-gold` | Yellow accent text |
| Honey | `#ffbb26` | `--color-honey` | Yellow wash and highlight bands |
| Coral Pink | `#ff58ae` | `--color-coral-pink` | Badge fill and illustration accent |
| Plum Violet | `#9f4fff` | `--color-plum-violet` | Violet wash and decorative highlight |
| Alert Red | `#ff2b3a` | `--color-alert-red` | Destructive or error accents only |

## Tokens - Typography

- Display family: `Family`, with careful fallback to Inter only when the custom font is not available.
- Body/UI family: `Inter`, then `ui-sans-serif`.
- Display usage: 44px to 68px, weight 500, tight tracking.
- Body usage: 16px to 17px, weight 400, comfortable line height.
- UI labels: 12px to 15px, weight 500 to 600.

| Step | Size | Weight | Line height | Tracking | Role |
|------|------|--------|-------------|----------|------|
| Micro | 12px | 400-600 | 19px | -0.01px | Tiny labels and metadata |
| Caption | 15px | 600 | 22px | -0.14px | Pills, badges, compact labels |
| Body | 17px | 400 | 26px | -0.22px | Main body copy |
| Subheading | 19px | 400 | 27px | -0.3px | Secondary headings |
| Heading | 23px | 500 | 25px | -0.44px | Card headings |
| Heading Large | 44px | 400-500 | 53px | -0.88px | Section headings |
| Display | 68px | 500 | 75px | -2.1px | Hero headline |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 80px to 120px |
| Card padding | 32px |
| Element gap | 8px to 12px |
| Spacing scale | 4, 8, 12, 16, 20, 24, 28, 32, 36, 48, 60, 76, 80, 92, 96, 104px |
| Small radius | 2px |
| Badges | 6px |
| Nav and cards | 10px |
| Large panels | 17px to 24px |
| Buttons | 32px |
| Illustration blobs | 40px to 72px |
| Pills | 9999px |

## Components

- Hero: centered text block with asymmetrical flat illustration clusters around it.
- Navigation: cream or transparent paper bar with compact labels and a dark pill CTA.
- Primary CTA: `#121212` background, cream or white text, 32px pill radius.
- Secondary CTA: `#f6f4ef` sand fill, dark text, 32px pill radius.
- Inline demo link: underlined text, `#ff3e00`, no filled background.
- Feature cards: white or stone surface, 10px radius, 1px inset border in `#f2f0ed`, 32px padding.
- Dark feature card: black surface with a soft shadow, used sparingly as the only heavy tonal shift.
- Badges: 6px radius, compact type, accent fills from the illustration palette.

## Layout And Imagery

Use a 1200px centered page model. Full-bleed sections sit on cream canvas, with stone panels for grouped content. Keep the interface flat and pressed-in. Illustration clusters can include abstract mascots, confetti-like shapes, coins, stars, hearts, gears, or leaves, but they should frame the text rather than overlap it.

## Do

- Use the custom Family typeface for 44px to 68px display headings.
- Use 10px radius for cards and nav surfaces.
- Use 32px or 9999px only for pill buttons and badges.
- Define cards with a 1px inset border in `#f2f0ed`.
- Use `#ff3e00` for demo links and accent text, not filled buttons.
- Set body text in Inter 400 at 16px to 17px.
- Keep every full-bleed section on `#fbfaf9`, with `#f2f0ed` for grouped depth.

## Do Not

- Do not use heavy drop shadows.
- Do not use `#0086fc` as a filled CTA background.
- Do not introduce gradients.
- Do not use Inter at display sizes when the Family typeface is available.
- Do not separate surfaces with white-on-white.
- Do not decorate pill buttons beyond the dark and sand variants.
- Do not use `#ff2b3a` outside destructive or error contexts.
