# Essie Wine

Source: [Refero Style](https://styles.refero.design/style/07f5281d-2a18-4e12-a8ff-d54d3e03d198)
Reference site: [https://www.essiewine.com](https://www.essiewine.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:36:23.532Z
Refero modified: 2026-06-05T09:48:05.728Z
Theme: mixed
Category: Other

## Style Summary

Explore Essie Wine's mixed Other design system: Ink Teal #062d32, Dusty Rose #c9a9b5 colors, BasicCommercial LT Com Roman, Adobe Caslon typography, and...

North star: Dusty rose chapbook with mustard chapter breaks

## What To Borrow

- Ink Teal `#062d32` for Primary type, illustration linework, nav wordmark, heading hairlines - the near-black that reads as warm ink rather than flat black, giving the serif type a hand-printed quality
- Dusty Rose `#c9a9b5` for Hero section field - the signature chapter color. Used as a full-bleed canvas behind the line-art illustration to create the soft, sun-bleached, evening-light atmosphere
- Mustard Olive `#aa9e54` for Booking and function-section field - the warm, earthy second chapter. Appears as a full-bleed background that pushes serif headings and form labels into high-contrast territory
- Slate Teal `#344b52` for Secondary text, link borders, tertiary headings - a lighter wash of Ink Teal for passages that shouldn't compete with the primary wordmark
- Warm Bone `#e9e9e2` for Soft canvas variant, off-white surface, hairline divider tone - the off-white that warms the page between full-color sections
- Mid Gray `#767676` for Input rule color - the single mid-gray used for form-field bottom borders, giving inputs a printed-on-paper feel rather than a digital-frame feel
- Carbon `#000000` for Maximum-contrast text, form labels, submit-button type - pure black is reserved for the moments that need to feel stamped or pressed
- Paper White `#ffffff` for Default page canvas and the lightest of the three section fields. Provides the resting breath between the rose hero and the mustard form

- BasicCommercial LT Com Roman `--font-basiccommercial-lt-com-roman` for Primary serif for body copy and mid-size headings. The transitional serif does the heavy editorial lifting - long-form descriptions, section headers, booking copy. Light weight (300) on display sizes gives the type a drawn-on-paper confidence rather than a marketing-bold shout.
- Adobe Caslon `--font-adobe-caslon` for Display serif reserved for the largest editorial headings. Caslon's old-style figures and bracketed serifs are used sparingly as a typographic event - when it appears, it signals 'this is the title, read me first.'
- Elementa `--font-elementa` for Geometric sans for nav, buttons, form labels, and the wordmark. Always set in small caps with positive tracking - it functions as the 'metadata' voice. Its 0.042em letter-spacing on 16px is the single most distinctive micro-typographic decision on the site: it makes every label read as a printed stamp rather than a UI element.

## Avoid

- Do not introduce a filled CTA button. The only action is the outlined submit button with a 1px black border and transparent fill.
- Do not use shadows, gradients, or any elevation effect. Depth comes from section color shifts only.
- Do not use photography, product shots, or 3D renders. The line-art illustration in #062d32 is the only imagery.
- Do not apply the chapter colors (#c9a9b5, #aa9e54) as small accent swatches, badges, or icon fills - they are full-bleed fields, not accents.
- Do not add a sticky/floating action bar, mega-menu, sidebar, or any persistent secondary navigation. The top bar is the only chrome.
- Do not round corners, use pill shapes, or apply any border-radius. All containers, buttons, and inputs are sharp-cornered.
- Do not use multiple sans-serif weights to create hierarchy. Hierarchy comes from the serif/sans pairing and size, not from bold/regular variation.

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
