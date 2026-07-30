# LottieFiles

Source: [Refero Style](https://styles.refero.design/style/a80507cb-afda-46dd-a2b9-ba91f3a78e78)
Reference site: [https://lottiefiles.com](https://lottiefiles.com)
Captured: 2026-07-30
Refero published: 2026-02-19T13:28:03.000Z
Refero modified: 2026-07-03T11:31:11.437Z
Theme: light
Category: Other

## Style Summary

Explore LottieFiles's light Other design system: Lottie Teal #019d91, Ink #09090b colors, DM Sans, Inter typography, and DESIGN.md for AI agents.

North star: Bright motion studio with teal accent

## What To Borrow

- Lottie Teal `#019d91` for Teal action color for filled buttons, selected navigation states, and focused conversion moments.
- Ink `#09090b` for Primary text, headings, dark card surfaces, footer background, icon strokes - near-black with a barely-perceptible cool cast
- Charcoal `#18181b` for Dark card backgrounds, elevated dark surfaces, strong icon strokes, secondary dark UI blocks
- Slate 700 `#27272a` for Dark muted surfaces and inverse muted backgrounds
- Steel `#71717b` for Muted body text, secondary copy, icon fills, helper labels - sits between the primary ink and lighter grays
- Fog `#9f9fa9` for Subtle text, tertiary metadata, low-priority descriptions
- Cloud `#e4e4e7` for Hairline borders, input outlines, subtle dividers between UI sections
- Mist `#f2f2f3` for Largest-volume border color across the UI; subtle separators, input borders, form outlines
- Warm Gray `#f4f4f5` for Page canvas and soft card surfaces - the dominant background tone beneath white
- Paper `#ffffff` for Pure white surfaces: raised cards, button fills, content containers on top of warm-gray canvas
- Sunshine `#f0b100` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Mint Wash `#b7ffe7` for Soft decorative fill in illustration/illustration-adjacent graphics
- Mint Pop `#61f7cf` for Bright decorative fill used in hero illustration characters and supporting graphics
- Ember `#ff6900` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color

- DM Sans `--font-dm-sans` for Display and heading family. Used for hero headlines (48-96px, weight 500), section headings (24-32px, weight 500), and large body (20px, weight 400). Letter-spacing tightens aggressively at large sizes - -0.0500em at 96px pulls characters into a compressed, poster-like composition that feels editorial rather than utilitarian. The medium weight (500) is the headline default, avoiding the heavy 700-800 convention used by most SaaS sites.
- Inter `--font-inter` for Utility and body family. Owns all body copy (16px), navigation (14px medium), buttons (14px medium), small labels (10-12px medium), and supporting icons. Consistent -0.0100em letter-spacing keeps it visually aligned to DM Sans at smaller sizes. Two-weight discipline (regular and medium only) keeps the interface feeling light and fast.

## Avoid

- Never use #000000 pure black as a card or surface fill - use #09090b or #18181b instead so surfaces feel ink-toned, not harsh.
- Never apply weight 700 or 800 to headlines - the system uses weight 500 even at 96px display sizes.
- Never use a drop shadow on cards - the elevation language is built from background contrast and rounded corners, not shadows.
- Never combine #019d91 with bold gradients, glassmorphism, or neon glow - the teal must read as a flat, confident fill.
- Never use #ff6900 (ember) for decoration or branding - it is reserved for warning/attention states.
- Never put body copy below 14px - captions stop at 12px and labels at 10px, and always use weight 500 for non-body sizes under 16px.
- Never break the spacing rhythm: gaps inside components are 4-8px, component-internal padding is 16-24px, between sections is 80px.

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
