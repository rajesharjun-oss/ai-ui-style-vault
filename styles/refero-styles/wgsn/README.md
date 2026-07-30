# WGSN

Source: [Refero Style](https://styles.refero.design/style/6cf3aec4-d028-44b0-b634-cc93e6c08e3c)
Reference site: [https://www.wgsn.com/en](https://www.wgsn.com/en)
Captured: 2026-07-30
Refero published: 2026-04-30T02:23:48.481Z
Refero modified: 2026-06-05T12:22:19.829Z
Theme: light
Category: SaaS

## Style Summary

Explore WGSN's light SaaS design system: Paper White #ffffff, Bone Warm #f6f2eb colors, DM Sans typography, and DESIGN.md for AI agents.

North star: editorial monochrome showroom

## What To Borrow

- Paper White `#ffffff` for Primary canvas, card surfaces, button text, and the base against which every other neutral is measured. Carries ~21:1 contrast with deep charcoal for all body and display text
- Bone Warm `#f6f2eb` for Secondary surface wash - the system's only warm neutral. Used as a soft section background to break white-on-white monotony and evoke paper-stock texture. Contrasts 14.4:1 with charcoal text
- Ash Mist `#f5f5f5` for Input field backgrounds, inset card wells, and disabled surface states. The cool-gray complement to Bone Warm - use the warm tone for sections, the cool tone for form wells
- Graphite Border `#666666` for Default hairline border color (444 border usages - by far the most-used neutral in the system). Also used for muted helper text and icon outlines. The structural divider color of the entire UI
- Smoke Border `#999999` for Secondary hairline borders and placeholder text - used when #666666 would feel too heavy against a light surface
- Pearl Border `#cccccc` for Subtle dividers and very light borders in nav-adjacent contexts where separation should be nearly invisible
- Silver Border `#bdbdbd` for Light link borders, particularly for outlined navigation links that need separation without emphasis
- Slate Text `#333333` for Secondary body copy, link borders, and UI text that should recede from primary content. Pairs with Paper White for ~12.6:1 contrast
- Carbon Input `#495057` for Input field text color - a cool desaturated charcoal that feels typographic rather than aggressive, distinct from the warmer #333333 used elsewhere
- Obsidian `#212121` for Primary action fill, primary nav background, and the deepest neutral in the system. Used for the filled CTA button, sticky header band, and dark surface blocks. Contrasts 16.1:1 with white - strong enough for any text role
- Pure Black `#000000` for Maximum-emphasis text, heading borders, and accent strokes. Reserved for the most important typographic moments and thin rule lines - never used as a large fill surface (use Obsidian instead)

- DM Sans `--font-dm-sans` for Sole typeface across all UI, body, and display contexts. A geometric-humanist sans with optical-size-friendly proportions - its clean terminals and open counters let it survive at 12px metadata and 92px display equally well. Weight 400 carries all body and utility text; weight 500 handles button labels and emphasized inline text; weight 700 is reserved for headlines and section titles. The 92px display step is the system's signature - used for hero statements with tight tracking (letter-spacing: -0.0110em) to give display headlines a condensed, editorial authority. All-uppercase button and label text uses the wider 0.0560em tracking for letterform breathing room.

## Avoid

- Never introduce chromatic color - the system is 0% colorful by design, and any accent hue would break the editorial monochrome logic.
- Never use shadows for elevation - the only shadow pattern in the system is the 1px inset border on links; do not add drop shadows to cards or buttons.
- Never use #000000 as a large filled surface - use #212121 (Obsidian) for dark backgrounds and reserve pure black for text and thin accent strokes only.
- Never use sharp 0px corners on images or cards - everything that contains an image uses 16px radius; flat-cornered images would feel foreign.
- Never use display-weight tracking on body text - the -0.0110em is calibrated for 40px+ sizes; applying it to 16px body copy will over-condense letters and hurt readability.
- Never use uppercase for body copy - uppercase is reserved for eyebrows, badges, and button labels where the 0.0560em tracking provides necessary letter spacing.
- Never use the warm Bone Warm (#f6f2eb) for form fields or interactive surfaces - it is a sectional wash only; form wells should use the cool Ash Mist (#f5f5f5) to signal input.

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
