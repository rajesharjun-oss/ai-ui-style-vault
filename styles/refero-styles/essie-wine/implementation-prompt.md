# AI Implementation Prompt

Build a Essie Wine-inspired interface using this source-derived style bundle.

Reference site: https://www.essiewine.com
Theme: mixed
Category: Other
North star: Dusty rose chapbook with mustard chapter breaks

Use these palette anchors:

- Ink Teal `#062d32` for Primary type, illustration linework, nav wordmark, heading hairlines - the near-black that reads as warm ink rather than flat black, giving the serif type a hand-printed quality
- Dusty Rose `#c9a9b5` for Hero section field - the signature chapter color. Used as a full-bleed canvas behind the line-art illustration to create the soft, sun-bleached, evening-light atmosphere
- Mustard Olive `#aa9e54` for Booking and function-section field - the warm, earthy second chapter. Appears as a full-bleed background that pushes serif headings and form labels into high-contrast territory
- Slate Teal `#344b52` for Secondary text, link borders, tertiary headings - a lighter wash of Ink Teal for passages that shouldn't compete with the primary wordmark
- Warm Bone `#e9e9e2` for Soft canvas variant, off-white surface, hairline divider tone - the off-white that warms the page between full-color sections
- Mid Gray `#767676` for Input rule color - the single mid-gray used for form-field bottom borders, giving inputs a printed-on-paper feel rather than a digital-frame feel
- Carbon `#000000` for Maximum-contrast text, form labels, submit-button type - pure black is reserved for the moments that need to feel stamped or pressed
- Paper White `#ffffff` for Default page canvas and the lightest of the three section fields. Provides the resting breath between the rose hero and the mustard form

Use these typography anchors:

- BasicCommercial LT Com Roman `--font-basiccommercial-lt-com-roman` for Primary serif for body copy and mid-size headings. The transitional serif does the heavy editorial lifting - long-form descriptions, section headers, booking copy. Light weight (300) on display sizes gives the type a drawn-on-paper confidence rather than a marketing-bold shout.
- Adobe Caslon `--font-adobe-caslon` for Display serif reserved for the largest editorial headings. Caslon's old-style figures and bracketed serifs are used sparingly as a typographic event - when it appears, it signals 'this is the title, read me first.'
- Elementa `--font-elementa` for Geometric sans for nav, buttons, form labels, and the wordmark. Always set in small caps with positive tracking - it functions as the 'metadata' voice. Its 0.042em letter-spacing on 16px is the single most distinctive micro-typographic decision on the site: it makes every label read as a printed stamp rather than a UI element.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 150px.
- Card padding: 27px.
- Element gap: 23px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Hero Illustration Panel: Above-the-fold brand storytelling
- Centered Serif Body Block: Long-form editorial description
- Section Heading (Serif Display): Chapter title for colored sections
- Underline Input Field: Form data entry
- Outlined Submit Button: Primary form action
- Ghost Nav Link: Top-bar navigation item
- Footer (Dusty Rose Repeat): Page closure

Do:

- Use the three chapter colors as full-bleed section fields: #c9a9b5 rose, #aa9e54 mustard, #ffffff white. Never tint them, mix them, or apply them as small accents.
- Set all labels, nav items, and button text in Elementa small caps with 0.042em letter-spacing - the printed-stamp tracking is the signature micro-typographic move.
- Use #062d32 Ink Teal for all primary type and illustration linework. Reserve #000000 Carbon for the highest-contrast moments (form labels, submit button).
- Give sections 100-150px vertical padding and use 150px as the default section-gap. The page should breathe like a printed page, not a dashboard.
- Use bottom-border-only inputs (1px #767676) with no box, no fill, no radius. The input field IS a printed line on a colored page.
- Let one large serif paragraph (BasicCommercial 38-49px) carry editorial sections. Do not split editorial body copy into multiple short paragraphs or sub-headings.
- Keep all corners square - 0px radius everywhere. The design's identity is print, not material.

Avoid:

- Do not introduce a filled CTA button. The only action is the outlined submit button with a 1px black border and transparent fill.
- Do not use shadows, gradients, or any elevation effect. Depth comes from section color shifts only.
- Do not use photography, product shots, or 3D renders. The line-art illustration in #062d32 is the only imagery.
- Do not apply the chapter colors (#c9a9b5, #aa9e54) as small accent swatches, badges, or icon fills - they are full-bleed fields, not accents.
- Do not add a sticky/floating action bar, mega-menu, sidebar, or any persistent secondary navigation. The top bar is the only chrome.
- Do not round corners, use pill shapes, or apply any border-radius. All containers, buttons, and inputs are sharp-cornered.
- Do not use multiple sans-serif weights to create hierarchy. Hierarchy comes from the serif/sans pairing and size, not from bold/regular variation.

Source prompt cues:

**Quick Color Reference**
- text: #062d32 (Ink Teal)
- background: #ffffff (Paper White)
- border: #767676 (Mid Gray) for inputs, #062d32 for nav/illustration
- accent: #c9a9b5 (Dusty Rose) and #aa9e54 (Mustard Olive) - used as full-bleed section fields, never as small UI accents
- primary action: #062d32 (outlined action border)

**Example Component Prompts**

1. **Hero Section**: Full-bleed #c9a9b5 dusty-rose background, 150px top/bottom padding. Single line-art illustration in #062d32 stroke centered, ~60% viewport width. No headline, no subtext, no button - the illustration is the hero.

2. **About / Editorial Body Block**: Full-bleed #ffffff background, 150px section padding. Centered BasicCommercial serif, weight 300, 49px, line-height 1.18, color #062d32, max-width 900px. One paragraph, no headings, no images.

3. **Section Heading on Mustard Field**: Full-bleed #aa9e54 background, 150px top padding. Caslon serif, weight 300, 49px, line-height 1.18, color #000000, centered. 100px bottom padding before form.

4. **Booking Form**: Two-column grid (50/50, 27px row gap) on #aa9e54 field. Each field: Elementa small-caps label (16px, 0.042em tracking, #000000) above, then 1px #767676 bottom-border input with BasicCommercial 19px text in #062d32. No boxes, no fill, 0px radius.

5. **Top Navigation**: Single row, full width, transparent background. 'Essie Wine' wordmark left in Elementa 16px small caps, 0.042em tracking, #062d32. Nav links spread across top with 35px column gap, same type spec. 3px #062d32 bottom border on hover/active.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
