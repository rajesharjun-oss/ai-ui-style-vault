# AI Implementation Prompt

Build a Secure and powerful crypto wallet | Ctrl Wallet-inspired interface using this source-derived style bundle.

Reference site: https://ctrl.xyz
Theme: light
Category: Crypto
North star: sticker-bombed white lab - confetti cards on surgical chrome

Use these palette anchors:

- Acid Lime `#05c92f` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Sticker Yellow `#fcea59` for Decorative accent card backgrounds, icon fills, confetti highlights on hero and feature spreads
- Cotton Pink `#ffd0e2` for Decorative accent card backgrounds, soft chromatic punctuation on feature layouts
- Powder Blue `#a7cbf6` for Decorative accent card backgrounds, informational callout surfaces
- Obsidian `#000000` for Primary text, primary icon strokes, hairline borders, filled download button in nav
- Carbon `#0f0f0f` for Secondary dark surface, button borders, card borders, strong interactive strokes
- Ash Gray `#5a585a` for Muted body text, link borders, nav sublabels, secondary icon strokes
- Slate Gray `#6e726e` for Helper text, low-emphasis borders, tertiary metadata
- Paper White `#f9faf9` for Page canvas, primary background, FAQ item surfaces
- Pure White `#ffffff` for Card surfaces, input fields, elevated content panels
- Bone `#ecefec` for Nav pill background, FAQ accordion rows, soft card surfaces, muted chips
- Plaster `#eeeeee` for Input field backgrounds, subtle disabled surfaces

Use these typography anchors:

- Tomato Grotesk `--font-tomato-grotesk` for The single typeface carrying the entire brand - a custom geometric grotesque deployed at extreme display sizes (up to 176px) with aggressively tight leading (0.77-0.80) that makes headlines feel like architectural cutouts rather than composed type. Weight 600 at display, 500 at body and UI. The tight line-height at hero scale is the signature: it stacks 'Take' and 'Ctrl.' into a single visual block.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 26px.
- Element gap: 18px.

Build these component patterns where relevant:

- Green Download Pill: Primary action CTA
- Black Nav Download Button: Secondary action CTA in navigation
- Ghost Nav Pill: Navigation container with secondary links
- Confetti Accent Card: Decorative feature cards with chromatic fills
- FAQ Accordion Row: Expandable FAQ item
- Display Headline: Hero and section title text
- Section Eyebrow: Small text above display headlines
- Social Auth Icon Cluster: OAuth provider buttons
- Phone Mockup Container: Product preview frame
- Chrome Dots Icon: Browser/extension indicator
- Plus Toggle Icon: Expand/collapse indicator for accordions

Do:

- Use #05c92f (Acid Lime) exclusively for the primary download/CTA pill - it is the only chromatic action color in the system
- Set display headlines at 153-176px with line-height 0.77-0.80 to achieve the architectural cutout effect
- Use 17.5px radius for cards and 35px radius for buttons/inputs - this two-tier rounding is the system's structural signature
- Communicate elevation through surface color shifts (#f9faf9 #ffffff #ecefec) and 1px borders, never through drop shadows
- Scatter chromatic confetti cards (yellow, pink, blue) across feature sections to inject energy into the monochrome canvas - limit to 2-3 per visual field
- Keep all body and UI text at weight 500, all display text at weight 600 - do not introduce weight 400 or 700
- Use Tomato Grotesk as the sole typeface; never pair it with a second font family

Avoid:

- Do not use drop shadows, glows, or blur effects - the system is intentionally flat and border-driven
- Do not use more than one chromatic accent card color in a single visual grouping - the confetti effect requires spacing between colors
- Do not set display text with line-height above 0.90 - the tight compression is what makes the headlines feel monumental
- Do not introduce a second action color for secondary CTAs - use black-filled or ghost buttons instead of more chromatic pills
- Do not use sharp corners (0px radius) on any interactive element - minimum 9px on nav, 17.5px on cards, 35px on buttons
- Do not pair the green CTA with another green element on the same screen - it must remain the single chromatic focal point
- Do not use #000000 and #0f0f0f interchangeably - reserve #0f0f0f for borders and dark surfaces, #000000 for primary text and nav

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
