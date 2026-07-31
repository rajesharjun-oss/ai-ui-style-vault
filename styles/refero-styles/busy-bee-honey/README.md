# Busy Bee Honey

Source: [Refero Style](https://styles.refero.design/style/9836e7c2-ac8e-453d-bdef-2677eb078d59)
Reference site: [https://www.busybeehoney.com](https://www.busybeehoney.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:15:32.841Z
Refero modified: 2026-06-05T07:41:34.096Z
Theme: mixed
Category: E-commerce

## Style Summary

Explore Busy Bee Honey's mixed E-commerce design system: Dark Cocoa #3b2722, Cream Parchment #f2ebd0 colors, TayMakawao, Barkman Honey typography, and...

North star: painted barn-side honey label - dark cocoa, gold, and blue stacked like a vintage billboard. Two sentence grounding: massive condensed serif display type bleeds edge-to-edge against solid color bands, and the bear-bottle product sits centered and unframed like the hero of a roadside sign.

## What To Borrow

- Dark Cocoa `#3b2722` for Primary canvas for hero/header, body text on light surfaces, structural borders, dark CTA fills - the most-used chromatic color in the system, carrying 80%+ of text and border weight
- Cream Parchment `#f2ebd0` for Light canvas for alternate sections, text on dark canvases, hairline borders, card surfaces - the warm off-white that makes the dark cocoa feel like printed kraft paper
- Charcoal `#000000` for Hard-edge text and fine borders where absolute contrast is required
- Honeycomb Gold `#ffca50` for Filled CTA buttons on dark sections, full-bleed section canvas, nav fill - the most chromatic and warmest surface, used as functional punctuation against the brown
- Barn Red `#a0342a` for Red outline accent for tags, dividers, and focused UI edges.
- Cornflower Blue `#6aacc2` for Marquee band background, secondary nav fill - the sky/honey-sky blue used as a thin chromatic strip between full-bleed color blocks
- Sage Green `#6fa162` for Subtle accent strip alongside the blue in marquee/decorative bands - an herb-garden green that keeps the blue from feeling isolated

- TayMakawao `--font-taymakawao` for Mega-display headlines - 'KNOW YOUR HONEY'-scale type that bleeds edge to edge, set tight (0.80 lh) with -0.01em tracking so letterforms lock together like wooden cutout letters
- Barkman Honey `--font-barkman-honey` for Secondary display and large numerals - the 'honey drip' serif used for sub-headlines and hero subtext (e.g. 65px section titles), its warmer curves pair against TayMakawao's mechanical weight
- TayBirdie `--font-taybirdie` for UI and small-body workhorse - nav links, footer text, micro-labels, and small caps. Normal tracking keeps it legible at small sizes; the tightest 1.00 lh is reserved for nav rows
- Times New Roman `--font-times-new-roman` for Fallback body text inside the system, also pulls double duty for italic-as-brand-voice moments where a system serif feels more honest than a designed face
- Anonymous Pro `--font-anonymous-pro` for Monospaced flavor for traceability codes, lot numbers, and any 'data' moment that should feel like a printed receipt - positive 0.031em tracking gives the text a stamped/inked feel
- Arial `--font-arial` for Button and micro-copy fallback - the utilitarian text inside pill buttons where neutrality beats the warmer display faces

## Avoid

- Don't introduce drop shadows, glows, or any z-axis elevation - the system is deliberately flat
- Don't set display type with line-height 1.0; tight leading is the signature, not an accident
- Don't put a card, border, or container around the hero product - the bottle sits on the canvas
- Don't use white (#ffffff) for canvas; the cream (#f2ebd0) is warmer and intentional
- Don't use a sans-serif display face - the system only works with the condensed serif 'painted sign' attitude
- Don't use Sage Green (#6fa162) for text or buttons - it is a marquee-strip accent only
- Don't break the full-bleed section into a max-width container with side gutters - bleed to the edge or it loses the billboard quality

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
