# Ambrook

Source: [Refero Style](https://styles.refero.design/style/f3c955e4-0fea-462d-b05f-868552e9628c) 
Reference site: [https://ambrook.com](https://ambrook.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:14:49.393Z 
Refero modified: 2026-06-03T20:05:27.382Z 
Theme: light 
Category: Fintech

## Style Summary

Explore Ambrook's light Fintech design system: Parchment #fcfaf1, Bone #efe9e0 colors, Lateral, Lateral Narrow typography, and DESIGN.md for AI agents.

North star: harvest ledger on butcher paper

## What To Borrow

- Parchment `#fcfaf1` for Page canvas and card surfaces - warm off-white replaces pure #ffffff to keep the system grounded in an agricultural, paper-like register
- Bone `#efe9e0` for Secondary surface for footer, soft sections, and hairline borders that need separation from the parchment canvas without harsh contrast
- Pure White `#ffffff` for Elevated card and product-mockup surface - used sparingly to lift specific panels (like the Ledger screenshot) above the parchment base
- Loam `#c7bcaf` for Subtle dividers, card edges, and low-emphasis borders between the canvas and content blocks
- Bark `#96897b` for Muted helper text, metadata, and supporting labels where a softer voice is needed than primary body copy
- Saddle `#50463c` for Secondary body text and subdued icon fills - a warm brown-gray that recedes without disappearing
- Ink `#211b15` for Primary text, heading strokes, and the dominant border color across the system. Warm near-black with a hint of umber keeps the interface from feeling clinical
- Charcoal Olive `#252a23` for Dark mode-style panels, product UI containers, and high-emphasis icon fills - used when a section needs to invert the warm page into something product-focused
- Deep Olive `#434f40` for Navigation borders, icon strokes, and the most-used neutral divider in the system - a moss-toned dark that reads as organic rather than industrial
- Sage `#7a9779` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Honey Amber `#e8b672` for Primary action button fill - the system's singular chromatic accent for CTAs, earning attention through warmth rather than saturation
- Wheat `#f0c891` for Lighter amber used for heading borders, icon accents, and subtle decorative strokes where honey would be too heavy

- Lateral `--font-lateral` for Workhorse sans for body, nav, buttons, inputs, and secondary headings. Weight 400 for running text, 500 for buttons and emphasis. Custom letterforms give it subtle warmth a generic sans would miss - slightly humanist proportions rather than mechanical geometric.
- Lateral Narrow `--font-lateral-narrow` for Condensed variant for tighter column headings and subhead text where horizontal space is constrained but body voice is still wanted.
- Lateral Display `--font-lateral-display` for Hero and section display face. Used at weight 500 (not the default 700) for major headlines - this restraint is signature: the type whispers authority instead of shouting. Slight serif character in the terminals gives it an editorial, almost newspaper-headline feel that matches the agricultural brand voice.

## Avoid

- Don't use pure #ffffff as a page background - parchment #fcfaf1 is the canvas signature.
- Don't set headlines at weight 700 - the system's authority comes from 500 and restraint.
- Don't introduce blue, red, or other saturated primaries - the only chromatic accent is honey amber #e8b672.
- Don't use pill-shaped (9999px) buttons - the system is defined by subtle 3.75px rounding.
- Don't fill illustrations with color - they must remain monochrome line art in #211b15.
- Don't use stock-polished or studio photography - documentary, full-sun, candid subjects only.
- Don't add drop shadows to cards or panels - the system relies on border color and surface warmth for separation.

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
