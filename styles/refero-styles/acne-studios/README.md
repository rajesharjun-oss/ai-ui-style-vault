# Acne Studios

Source: [Refero Style](https://styles.refero.design/style/234e9a17-236d-4446-9d58-f83f6806d012) 
Reference site: [https://acnestudios.com](https://acnestudios.com) 
Captured: 2026-07-29 
Refero published: 2026-02-16T12:02:09.000Z 
Refero modified: 2026-06-05T04:29:01.005Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Acne Studios's light E-commerce design system: Electric Cobalt #0018a8, Ink Black #000000 colors, Helvetica Monospaced Pro, Acne Studios (custom...

North star: Minimalist gallery white space with bold photographic moments - a fashion magazine laid flat on marble.

## What To Borrow

- Electric Cobalt `#0018a8` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Ink Black `#000000` for Primary text, logo wordmark, icon strokes, nav labels, and footer copy. Used at 21:1 contrast on white for absolute legibility
- Graphite `#6b6b6b` for Supporting neutral for secondary UI, dividers, and muted labels.
- Paper White `#ffffff` for Page canvas, product card backgrounds, and nav bar surface. The dominant ground that lets editorial photography breathe
- Bone `#f2f2f2` for Subtle box-shadow tint and hairline border for elevated overlays. Used minimally - the system prefers whitespace to tinted surfaces

- Helvetica Monospaced Pro `--font-helvetica-monospaced-pro` for Helvetica Monospaced Pro - detected in extracted data but not described by AI
- Acne Studios (custom wordmark) `--font-acne-studios-custom-wordmark` for Oversized brand wordmark overlaid on hero photography. The custom face has geometric construction with humanist terminals; no system font replicates it, but its character is closest to a wide-aperture geometric sans.
- Helvetica Neue / system sans `--font-helvetica-neue-system-sans` for All functional UI text: nav links, section labels, product captions, footer. Always rendered uppercase with generous tracking - this typographic treatment is the single most recognizable non-photographic element on the site.

## Avoid

- Do not introduce filled CTA buttons, pill shapes, or rounded containers - they break the editorial-flat aesthetic
- Do not apply box-shadow to product cards, nav, or content tiles; separation comes from whitespace alone
- Do not use colors outside the five-token palette for interface chrome - photography supplies all chromatic richness
- Do not set type below 9px or render body text in anything other than uppercase with tracking for nav-adjacent labels
- Do not center body content or constrain to a max-width - layouts should be full-bleed to feel like a magazine spread
- Do not add borders, dividers, or background fills to product cells - they must bleed into each other
- Do not use #0018a8 as decorative illustration color; it is reserved for functional interactive states

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
