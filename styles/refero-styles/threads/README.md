# Threads

Source: [Refero Style](https://styles.refero.design/style/3b46c64e-b733-4d70-8cd0-531ca1f92937)
Reference site: [https://www.threads.com](https://www.threads.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:59:12.567Z
Refero modified: 2026-06-05T07:39:06.829Z
Theme: light
Category: Media

## Style Summary

Explore Threads's light Media design system: Ink Black #000000, Paper White #fafafa colors, system-ui typography, and DESIGN.md for AI agents.

North star: newspaper column on frosted glass

## What To Borrow

- Ink Black `#000000` for Primary text, icon strokes, structural borders, and the filled Log in button - the load-bearing color that carries almost every interface element
- Paper White `#fafafa` for Page canvas and the topmost surface layer - warm off-white that softens the contrast of pure black text
- Mist Gray `#efefef` for Secondary surface beneath the elevated feed container - the shadow-tinted plane that gives the feed column its lifted feel
- Cloud Gray `#d5d5d5` for Post dividers and card outline borders - the thinnest structural separator between stacked feed items
- Ash Gray `#969696` for Secondary borders on buttons, muted metadata text, and placeholder strokes - the middle-tone neutral for inactive controls
- Graphite `#424242` for Body text borders, secondary icon fills, and medium-emphasis strokes - sits between Ink Black and Ash Gray for tertiary text and outlines
- Meta Blue `#385898` for Outlined link borders, hyperlink text, verified-badge fill, and icon accents - the single chromatic note in the system, used for interactive emphasis without ever filling a large surface

- system-ui `--font-system-ui` for Entire interface - system-ui at 15px/400 for post body text, 15px/600 for usernames, 13px/400 for timestamps and metadata, 12px/400 for fine print. The choice of system-ui rather than a webfont keeps rendering native to each platform; the narrow size range (12-17px) and tight 1.33-1.4 line-height create the compact, information-dense rhythm of a social feed where many posts share a single screen

## Avoid

- Don't introduce a second chromatic color - the system is monochrome plus one blue, and adding another breaks the newspaper discipline
- Don't use colored or gradient fills on buttons, cards, or surfaces - the only filled surface is the Ink Black Log in button
- Don't use shadows on individual post cards - the single elevation halo belongs to the feed container only
- Don't render text larger than 20px - the system operates in a 12-17px window and oversized type breaks the compact rhythm
- Don't use a webfont when system-ui renders natively - replacing it with a custom face shifts the personality away from neutral utility
- Don't put borders or backgrounds on sidebar icon buttons - they must read as a column of marks on a blank rail
- Don't round card corners above 8px for embedded link previews or media - large radii on those elements compete with the feed container's own 18px curve

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
