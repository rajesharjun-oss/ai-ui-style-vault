# IKEA

Source: [Refero Style](https://styles.refero.design/style/e7b37c82-239c-48d5-b293-79a2bfa235cc)
Reference site: [https://www.ikea.com](https://www.ikea.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:03:49.756Z
Refero modified: 2026-06-05T10:18:20.342Z
Theme: light
Category: E-commerce

## Style Summary

Explore IKEA's light E-commerce design system: IKEA Yellow #ffdb00, Ink Black #111111 colors, Noto IKEA typography, and DESIGN.md for AI agents.

North star: sunlit Swedish flat-pack showroom

## What To Borrow

- IKEA Yellow `#ffdb00` for Primary CTA fills, featured card backgrounds, hero accent panels, the singular chromatic workhorse of the system
- Ink Black `#111111` for Primary text, body copy, headings, dominant borders (851 occurrences), icon strokes
- Pure White `#ffffff` for Page background, card surfaces, nav background, button text on dark fills
- Warm White `#fffefb` for Slightly off-white surface variant for buttons and cards - barely warmer than pure white, breaks digital coldness
- Steel Gray `#818181` for Secondary text, muted borders, disabled icon states
- True Black `#000000` for SVG icon fills, input borders, true-black accents where maximum contrast is needed
- Link Blue `#0159a3` for Text link color, used extensively across navigation and body links - the only blue in the system
- Soft Pink `#ffa6da` for Occasional decorative highlight, used sparingly on select link elements or promotional accents

- Noto IKEA `--font-noto-ikea` for Sole typeface - custom IKEA-branded Noto variant. Two-weight system (regular 400, bold 700) is deliberate restraint: no italics, no medium weight, no light. The 700 headlines at 36-51px carry the entire brand voice; body at 16px stays neutral. Letter-spacing tightens as size grows, giving display text a compressed, architectural quality.

## Avoid

- Do not introduce shadows, elevation, or any depth effects - the system is entirely flat
- Do not use more than one border radius - 8px everywhere, no exceptions
- Do not add additional font weights (300, 500, 600) - the binary 400/700 system is the constraint
- Do not place body text directly on photography without a gradient overlay
- Do not use the blue #0159a3 as a CTA button fill - it is link-only, not action
- Do not soften the letter-spacing - the negative tracking is structural, not decorative
- Do not add accent gradients or color transitions - the system rejects all gradient fills on surfaces

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
