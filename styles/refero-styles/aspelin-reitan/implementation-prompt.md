# AI Implementation Prompt

Build a Aspelin Reitan-inspired interface using this source-derived style bundle.

Reference site: https://www.aspelineiendom.no
Theme: light
Category: Other
North star: Candlelit architectural archive - the page reads like a portfolio of built places pinned to a warm cream wall, with a single line of white type floating over each full-bleed image.

Use these palette anchors:

- Warm Parchment `#ffebd0` for Gray accent for outlined action borders, linked labels, and lightweight interactive emphasis.
- Candlelight `#fff8e9` for Lighter cream for elevated surfaces and secondary text on dark - a half-step above Parchment for subtle layering
- Obsidian `#000000` for Structural borders, section dividers, image edge treatments - used as a hairline, never as a fill
- Walnut Shell `#2f2116` for Dark canvas behind full-bleed photographs, footer backgrounds, and dark editorial sections - the deep brown that makes white type glow warm
- Aged Bronze `#4f3622` for Secondary dark surface and border on dark sections - a half-step lighter than Walnut for subtle layering on dark
- Amber Glow `#fee197` for Navigation borders, active state accents, warning/attention states, and the single chromatic punctuation in an otherwise warm-neutral system
- Muted Gold `#987f61` for Link borders and heading underlines on dark sections - a desaturated brass for typographic detail without breaking the monochrome feel

Use these typography anchors:

- ModernEra `--font-modernera` for Sole typeface for body, navigation, buttons, links, headings, and overlay captions - a custom humanist sans that sits at 400 for body and 500 for emphasis. The entire type scale tops out at 40px, which is anti-SaaS: no 56px or 72px display sizes, no dramatic weight jumps. Authority comes from restraint, not volume.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 100px.
- Card padding: 40px.
- Element gap: 12-20px.

Build these component patterns where relevant:

- Outlined Navigation Button: Primary interactive element in the header
- Ghost Link with Border: Text links throughout content sections
- Full-Bleed Editorial Hero: Opening section of each major page
- Portfolio Image Card: Project or case-study thumbnails in the portfolio grid
- Two-Column Project Layout: Portfolio detail or story sections
- Dark Overlay Section: Editorial story or mood sections between cream content areas
- Header Bar: Persistent navigation across all pages
- Navigation Item: Menu links in the header
- Section Heading: Titles for content blocks on cream backgrounds
- Footer: Bottom of page
- Outlined Action Button (Cream Section): Interactive buttons when on a cream background
- Input Field: Form inputs (newsletter, contact)

Do:

- Use outlined buttons with 8px radius exclusively - no filled CTAs. Pair with 1px borders in Warm Parchment on dark or Obsidian on cream.
- Let full-bleed photography carry the visual weight. Keep UI chrome transparent or minimal over photographs.
- Stay within the type scale: 16, 18, 20, 24, 28, 40px. Do not exceed 40px for display text - the restrained scale is the signature.
- Use Warm Parchment (#ffebd0) as the dominant canvas for content sections and Walnut Shell (#2f2116) for dark editorial breaks.
- Maintain 100px vertical section gaps to preserve the spacious, gallery-walk rhythm.
- Pair every link with a visible border or bottom-line treatment - the line IS the affordance, not a color change.
- Set body text at 18px / 1.25 in ModernEra 400 - never below 16px, and keep line-height generous.

Avoid:

- Do not introduce filled CTA buttons, drop shadows, or gradient backgrounds - the system is flat and outlined by design.
- Do not add chromatic colors beyond Amber Glow (#fee197) and Muted Gold (#987f61). The palette is warm-neutral only.
- Do not use display sizes above 40px or bold weights above 500. The system whispers; it does not shout.
- Do not apply border-radius to images or cards. Only buttons and links get 8px. Images and cards are sharp-cornered.
- Do not place white text on Warm Parchment backgrounds - contrast is reserved for Walnut Shell dark sections.
- Do not add icons, illustrations, or decorative graphics over photographs. The photograph is the only visual layer.
- Do not use multiple typefaces. ModernEra is the sole family - no serifs, no display fonts, no mono.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
