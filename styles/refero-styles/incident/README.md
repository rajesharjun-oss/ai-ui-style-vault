# Incident

Source: [Refero Style](https://styles.refero.design/style/d9a60077-619a-4cb7-95ed-0c428c2b51ed)
Reference site: [https://incident.io](https://incident.io)
Captured: 2026-07-31
Refero published: 2026-04-30T00:21:46.602Z
Refero modified: 2026-06-05T09:39:33.461Z
Theme: light
Category: Dev Tools

## Style Summary

Explore Incident's light Dev Tools design system: Signal Orange #f25533, Concrete #efefef colors, Times (system serif), Arial (system sans) typography, and...

North star: Technical broadsheet on concrete. Times-serif headlines float on a warm-gray page with hairline black rules and a single orange flare that breaks the calm like a signal beacon.

## What To Borrow

- Signal Orange `#f25533` for Brand accent, logo mark, decorative SVG fills, nav emphasis - the single warm chromatic note that cuts through the monochrome system
- Concrete `#efefef` for Page canvas, button background - the dominant surface tone that gives the system its paper-like warmth
- Ink `#000000` for Primary text, hairline borders (920+ uses), button outlines - pure black carries all structural line work
- Paper `#ffffff` for Card surfaces, nav fills - the white layer that sits on top of the concrete canvas
- Carbon `#161618` for Near-black for nav strokes, emphasis text, and the tinted shadow base - softer than pure ink for layered elements
- Mist `#dadada` for Subtle drop-shadow tone, decorative image edge tint
- Fog `#cccccc` for Secondary shadow tone, decorative image edge tint
- Parchment `#e4d9c8` for Warm cream decorative surface - near-gray but carries a beige cast that ties to the orange family
- Alert Red `#ff492c` for Orange decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color
- Ember `#f1641e` for Orange outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color

- Times (system serif) `--font-times-system-serif` for Body text, headings, nav items, hero copy, card content, list items, footer - Times carries 770+ uses and is the signature typographic choice. A serif body face on a B2B incident-management product is anti-convention: it borrows the authority of a legal broadsheet or technical manual, replacing the usual Inter/system-ui with something that reads as deliberately editorial. Weight 400 for body, 700 for emphasis and headings.
- Arial (system sans) `--font-arial-system-sans` for Small UI micro-text: button labels, nav utility text, icon-adjacent labels. Arial at 13px handles the functional labels while Times carries the voice - a deliberate serif/sans split where Times says something and Arial just tags it.

## Avoid

- Do not use sans-serif (Inter, system-ui) for body copy or headings - replacing Times breaks the editorial identity
- Do not add colored button fills (blue, orange, green) for primary actions - the system uses neutral concrete buttons with black borders
- Do not use gradients - no gradient was detected in the source and the flat editorial aesthetic rejects them
- Do not use heavy drop-shadows for elevation - shadows are reserved for image containers at 2-4% opacity only
- Do not introduce blue or green as brand or accent colors - the chromatic palette is exclusively warm (orange family and amber)
- Do not round buttons beyond 4px or use pill shapes - the slightly squared button geometry reinforces the broadsheet feel
- Do not use color to indicate active or selected states - rely on weight (400 700) and underline affordances within the serif system

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
