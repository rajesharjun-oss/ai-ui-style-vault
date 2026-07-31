# reboot

Source: [Refero Style](https://styles.refero.design/style/ac14ea36-ea3e-4a25-bd16-11fb50d806fb)
Reference site: [https://reboot.studio](https://reboot.studio)
Captured: 2026-07-31
Refero published: 2026-02-27T11:56:56.000Z
Refero modified: 2026-06-05T07:46:52.002Z
Theme: light
Category: Agency

## Style Summary

Explore reboot's light Agency design system: Paper Gray #e5e7eb, Editorial Black #000000 colors, Inter typography, and DESIGN.md for AI agents.

North star: quiet atelier on cream paper - a design studio's homepage that reads like a printed monograph, where the only color is the one blue mark in the margin

## What To Borrow

- Paper Gray `#e5e7eb` for Page canvas and hairline borders - the warm off-white ground that all type sits on
- Editorial Black `#000000` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Charcoal Ink `#232323` for Headings and emphasized prose - a near-black that softens headlines against the pure black of running text
- Soft Graphite `#a7a7a7` for Muted body text and secondary metadata - the gray that carries secondary sentences without competing with the lead
- Faded Pencil `#c8c8c8` for Tertiary annotations and the most restrained helper text - the lightest voice in the grayscale scale
- Pure White `#ffffff` for Surface highlights and inverse text on the black pill button
- Sapphire Beam `#00c8fb` for Decorative inline gradient - cyan-to-indigo mark used as a full-stop between sentences, never as a fill or background
- Ember Sunset `#ef3313` for Secondary decorative gradient - warm triple-stop used sparingly for moments that need a chromatic counterpoint to the blue

- Inter `--font-inter` for The sole typographic voice - used for everything from nav metadata to display headlines. Weight 400 carries running prose, weight 500 lifts section lead-ins and the primary action, weight 600 is reserved for the wordmark. The narrow three-size scale (14/16/40) is deliberate: hierarchy comes from luminance and weight, not from a cascading type ramp.

## Avoid

- Don't introduce chromatic colors beyond the two existing gradients - the palette is achromatic plus two accent gradients
- Don't use more than three type sizes; the scale is intentionally 14 / 16 / 40
- Don't use color to signal emphasis - use weight shifts (400 500) and grayscale steps instead
- Don't add backgrounds, borders, or cards to text blocks - text should sit directly on the page canvas
- Don't apply drop shadows to text, buttons, or content blocks; the design is flat by principle
- Don't center text or use multi-column layouts; everything is a single left-aligned column
- Don't scale the blue gradient to fill large areas or use it on the primary button - it is decorative punctuation, not a brand fill

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
