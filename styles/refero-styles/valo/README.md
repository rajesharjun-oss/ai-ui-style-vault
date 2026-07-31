# Valo

Source: [Refero Style](https://styles.refero.design/style/f65c3888-2eb3-41a1-87b3-f410b667097e)
Reference site: [https://www.valohealth.com](https://www.valohealth.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:34:01.128Z
Refero modified: 2026-06-05T10:06:19.236Z
Theme: dark
Category: AI

## Style Summary

Explore Valo's dark AI design system: Void #000000, Bone #e5e7eb colors, Valo typography, and DESIGN.md for AI agents.

North star: noir observatory at midnight - weight-300 typography floats on pure black while a single teal-violet gradient passes through like a laser line across the room.

## What To Borrow

- Void `#000000` for Page canvas, hero background, all primary surface area. Sets the dark-stage tone for every screen
- Bone `#e5e7eb` for Hairline borders, dividers, and muted secondary text. The workhorse neutral that defines edges without adding visual weight
- Paper `#ffffff` for Primary headings, body text, nav links, and icon strokes. Maximum contrast against Void for clear information hierarchy
- Graphite `#4d4d4d` for Subtle nav borders and disabled/inactive state lines. Sits between Void and Bone for low-emphasis structural lines

- Valo `--font-valo` for Exclusive typeface across all UI: nav links, body copy, section labels, and display headlines. Weight 300 carries headlines and body - the anti-convention whisper-weight creates scientific authority through restraint. Weight 700 is reserved for micro-labels and the few moments that need to anchor a page. The custom cut of this single family is the brand voice.

## Avoid

- Don't use weight 700 for body copy or long-form paragraphs - the voice is light; 700 belongs to subheadings and micro-labels only
- Don't apply the Spectrum Wash gradient to button backgrounds, panel fills, or large-area surfaces - it belongs on text accents, ring strokes, and the footer band only
- Don't introduce card surfaces, drop shadows, or elevated panels - the canvas stays flat; depth comes from type scale, not from z-axis
- Don't use borders thicker than 1px - the entire system runs on hairlines (Bone at 1px); anything heavier breaks the editorial register
- Don't add a chromatic brand color outside the violet blue teal lavender ramp - the system is intentionally near-monochrome with one gradient family
- Don't center body text or multi-line content - the layout is left-aligned and the measure should align with the headline edge
- Don't use stock photography, emoji, or decorative illustration - visuals are limited to the gradient torus and the footer wash; everything else is type and whitespace

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
