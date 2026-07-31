# Pietrastudio

Source: [Refero Style](https://styles.refero.design/style/577eb7d8-3555-4378-83df-0cebebc4782f)
Reference site: [https://www.pietrastudio.com](https://www.pietrastudio.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:38:26.650Z
Refero modified: 2026-06-05T08:59:10.716Z
Theme: light
Category: SaaS

## Style Summary

Explore Pietrastudio's light SaaS design system: Ember Coral #ff5c3c, Pure White #ffffff colors, Attila-Bold, Attila Sans Uniform typography, and DESIGN.md...

North star: sunlit AI workshop on cream paper

## What To Borrow

- Ember Coral `#ff5c3c` for Primary CTA fill, active nav, brand accent - a warm vermillion that sits forward against cream backgrounds without feeling aggressive
- Pure White `#ffffff` for Page canvas, card surfaces, button text on dark fills - the base everything else rests on
- Ink Black `#000000` for Primary heading text, body text, dominant borders - the workhorse contrast color used at 1750+ instances
- Cream Paper `#f8f6f2` for Warm off-white surface layer for elevated cards and section bands - gives the page its sunlit warmth without leaving pure white
- Soft Cream `#fffbe7` for Accent card surface, tinted feature panels - a warmer cream for highlight cards that need to stand apart from the base canvas
- Charcoal `#141414` for Secondary text, link text, heavy borders - softer than pure black for UI chrome and metadata
- Iron Gray `#1f2026` for Body text, input borders, body chrome - near-black with a cool cast for dense informational UI
- Mid Gray `#6b6b6b` for Muted body text, helper text, icon borders - the primary de-emphasized text tone
- Silver `#c4c4c4` for Hairline borders, dividers, placeholder text - light structural lines that recede
- Slate `#333333` for Deep body text, secondary headings - sits between charcoal and black for weighted text that isn't headline-level
- Ash `#e8e8ea` for Shadow tint, ultra-light dividers, ghost surfaces - the near-invisible layer
- Goldenrod `#f9e070` for Category tag accent, feature card variant - warm yellow that pairs with coral gradients
- Sage `#57ad6a` for Category tag accent, feature card variant - natural green for growth/scale categories

- Attila-Bold `--font-attila-bold` for Display headlines - the tall, tightly-tracked serif/grotesque hybrid used for hero and section headings at 32-48px. The negative tracking (-0.02em) is signature: letters pull close at large sizes creating a dense, editorial block of text
- Attila Sans Uniform `--font-attila-sans-uniform` for Largest display moments - uniform-width variant for the biggest headlines where letterform consistency matters more than contrast
- Labil-Bold `--font-labil-bold` for Bold body emphasis and mid-weight headings - the weight-400 bold variant that gives inline emphasis and sub-headings without switching families
- Labil Grotesk `--font-labil-grotesk` for Primary body and UI font - the workhorse grotesque used for body copy, buttons, inputs, cards, and navigation at 12-24px. Tracking sits at -0.01em throughout, a subtle but consistent tighten
- Labil-Regular `--font-labil-regular` for Lighter body weight for body copy and descriptions - weight 300 for long-form paragraphs creates breathing space; weight 400 for compact UI. The 0.143em tracking on some instances suggests uppercase labels or tag text

## Avoid

- Do not use coral for secondary actions, links, or decorative elements - it loses its action weight if scattered
- Do not use Attila for body copy or UI text - it is display-only and overwhelms at small sizes
- Do not apply the category gradient swatches as full card backgrounds or page sections - they are tag-sized accents
- Do not introduce drop shadows in cool gray tones; all shadows should carry the warm pink/cream tint to match the surface palette
- Do not use sharp 0px radii on cards or images - the rounded geometry is essential to the soft, paper-like feel
- Do not stack multiple saturated colors in a single component - one chromatic accent per element, with grayscale for everything else
- Do not use letter-spacing wider than -0.01em on body text; the system is consistently tight-tracked and loosening it breaks the type voice

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
