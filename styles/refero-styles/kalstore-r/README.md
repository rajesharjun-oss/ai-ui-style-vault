# Kalstore(R)

Source: [Refero Style](https://styles.refero.design/style/e854a4f7-4243-44a7-92e2-e22db22bef1b)
Reference site: [https://kal-store.com](https://kal-store.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:16:55.210Z
Refero modified: 2026-06-05T11:21:12.120Z
Theme: light
Category: E-commerce

## Style Summary

Explore Kalstore(R)'s light E-commerce design system: Paper White #faf9f7, Ink #242424 colors, ABCDiatype, Arial typography, and DESIGN.md for AI agents.

North star: Paper atelier on a quiet morning. The interface is warm off-white, sparsely set, and lets one mustard accent and oversized editorial type do the talking.

## What To Borrow

- Paper White `#faf9f7` for Page canvas - warm off-white that mimics uncoated paper stock; the default surface behind everything
- Ink `#242424` for Primary text, icon strokes, and dominant border color. Slightly softened from pure black to sit comfortably on the warm canvas
- Felt Gray `#d3d3d3` for Hairline dividers, card borders, list separators - the structural neutral that holds the layout together without drawing attention
- Linen `#edecea` for Subtle surface elevation for nav backgrounds and hover states; slightly cooler than Paper White to create depth without contrast
- Parchment `#e0ddd7` for Warm-toned surface for body sections and secondary cards; introduces a faint paper-fiber warmth against the cooler Linen
- Slate `#727272` for Muted secondary text and subdued borders for de-emphasized content like timestamps and helper labels
- Ash `#8d9090` for Tertiary text and disabled-state borders; sits between Slate and Felt Gray in the neutral ladder
- Charcoal `#585a5a` for Navigation borders and medium-emphasis UI structure; a bridge between the near-black Ink and the mid-grays
- Pure White `#ffffff` for Badge fills, icon backgrounds, and the highest surface elevation - used sparingly to lift elements above Linen and Parchment
- Mustard `#f1ba35` for Primary action color - CTA buttons, nav accents, and badge highlights. A warm sunlit yellow that reads as a sticky-note moment against the monochrome layout
- Espresso `#30250b` for Dark accent paired with Mustard on badges and nav - provides a near-black complement that makes the yellow pop without using pure black
- Terracotta `#d26c46` for Editorial accent - appears in the typographic art palette and decorative product imagery. Rust-orange warmth that belongs in illustrations, not buttons
- Sage `#458e71` for Editorial accent - a muted forest green used in the typographic art palette. Decorative, not functional
- Cobalt `#3b59a3` for Editorial accent - deep ultramarine from the typographic art palette. The strongest chromatic statement in the decorative system
- Rust `#6c3c3c` for Editorial accent - dark brick red from the typographic art palette, echoing the warmth of Terracotta but grounded
- Sky Dust `#90abc8` for Editorial accent - a washed, chalky blue used in the typographic art palette. The lightest chromatic in the decorative system

- ABCDiatype `--font-abcdiatype` for The only typeface. A neo-grotesque editorial sans used at every register - 19px body copy, 25px section headings, and dramatic 71-140px display treatments with tight tracking. The wide weight range (400-500) keeps the system monovariational; hierarchy comes from size, not weight contrast.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Don't use chromatic colors for functional UI - no green for success, no red for error, no blue for info. The system is monochrome with one warm accent.
- Don't apply box-shadows with opacity above 10% - the elevation philosophy is paper-lift, not digital pop.
- Don't use bold weights (600+) - the system maxes out at weight 500; hierarchy comes from size, not weight contrast.
- Don't use pure black (#000000) for text or backgrounds - use #242424 Ink to maintain warmth on the paper-tone canvas.
- Don't add gradients - the raw data shows zero gradient usage; the system is entirely flat surfaces.
- Don't use button padding larger than 8px vertical - the compact 6x8px button size is a signature; larger padding would break the restrained feel.
- Don't place Mustard (#f1ba35) on large filled surfaces - it works as a button fill or badge, not as a section background.

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
