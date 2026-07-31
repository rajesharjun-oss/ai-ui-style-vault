# Raw Materials

Source: [Refero Style](https://styles.refero.design/style/274e85fb-a34d-4e41-9369-be03065b971b)
Reference site: [https://therawmaterials.com](https://therawmaterials.com)
Captured: 2026-07-31
Refero published: 2026-03-05T13:10:02.000Z
Refero modified: 2026-06-05T07:25:16.550Z
Theme: light
Category: Design

## Style Summary

Explore Raw Materials's light Design design system: Ember Orange #ff3d00, Pulse Violet #5900cc colors, StabilGrotesk, Optimistic Text typography, and...

North star: brutalist editorial on warm cream

## What To Borrow

- Ember Orange `#ff3d00` for Orange supporting accent for decorative details and low-frequency emphasis
- Pulse Violet `#5900cc` for Violet supporting accent for decorative details and low-frequency emphasis.
- Cobalt Blue `#2835f8` for Violet supporting accent for decorative details and low-frequency emphasis.
- Crimson `#ff003d` for Red supporting accent for decorative details and low-frequency emphasis
- Caution Yellow `#ffff00` for Yellow supporting accent for decorative details and low-frequency emphasis.
- Voltage Green `#05ff00` for Green supporting accent for decorative details and low-frequency emphasis
- Electric Blue `#1b73e6` for Headings and body text on cream, mid-saturation blue used in content
- Sky Cyan `#00c2ff` for Headings and accent text, cool counterpoint to warm cream
- Forest `#008163` for Card fills, moderate green for body-level content blocks
- Tangerine `#ff5c00` for Card fills, warm orange variant for content blocks
- Signal Red `#ee2526` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color
- Ink `#0e0e0e` for Dark supporting neutral for text, icons, and strong contrast.
- Bone Cream `#f4e9e1` for Primary page canvas, nav text on color blocks, card surface
- Paper White `#ffffff` for Active nav card, elevated card surface, input fields
- Charcoal `#242320` for Dark surface fill, image overlays, secondary text on light
- Sage `#cee4cd` for Tinted section background, warm green wash
- Blush `#e4d0cd` for Tinted section background, warm pink wash
- Sand `#e7e4d0` for Tinted section background, warm yellow wash, card fill
- Sky Tint `#cddae4` for Tinted section background, cool blue wash, image-related surfaces
- Celadon `#ddded3` for Tinted section background, muted green wash
- Olive Slate `#444639` for Dark olive section background, secondary text
- Forest Slate `#374936` for Dark green section background, heading text on light
- Cocoa Slate `#4a3937` for Dark warm section background, heading text on light
- Plum Slate `#493648` for Dark purple section background, heading text on light

- StabilGrotesk `--font-stabilgrotesk` for Workhorse - every nav label, body text, button, badge, card label, and sub-heading up to 46px. The only font that touches interactive UI
- Optimistic Text `--font-optimistic-text` for Large display headlines at 80-193px, sometimes body pull-quote at 23px
- KlarheitKurrent `--font-klarheitkurrent` for The largest display voice - 200-259px hero type, also mid-size editorial headings at 79-107px
- HTQ-Waldenburg-FettSchmal `--font-htq-waldenburg-fettschmal` for Narrow bold display for compressed-impact headlines, the only font using "case" feature
- RightGrotesk `--font-rightgrotesk` for Bold geometric display for 199px poster-scale headlines
- Moderat `--font-moderat` for Wide-tracked display - the +0.084em tracking is a signature, used for all-caps subhead labels
- Courier New `--font-courier-new` for Monospaced system fallback for data tables, tiny index numbers

## Avoid

- Don't add drop-shadows, inner-shadows, or any blur effects - the system is entirely flat
- Don't use a single 'primary' brand color for CTAs - buttons inherit their section's accent color
- Don't set body text below 16px or above 20px - the body range is tight by design
- Don't apply letter-spacing wider than +0.01em to body or subheading text - only the +0.084em Moderat all-caps labels and +0.112em Optimistic uppercase use wide tracking
- Don't introduce a new color outside the seven nav hues and the five tinted washes - the palette is deliberately finite
- Don't use rounded corners smaller than 16px on any container - 4px or 8px corners will read as a different system
- Don't place display headlines centered on the canvas - they are always left-aligned and bleed right

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
