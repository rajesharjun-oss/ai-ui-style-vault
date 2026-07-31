# AI Implementation Prompt

Build a Sackville-inspired interface using this source-derived style bundle.

Reference site: https://sackville.co
Theme: light
Category: E-commerce
North star: Cobalt zine pressed onto cream - a hand-inked editorial spread where the illustration is the hero and the UI is just typeset text on warm paper.

Use these palette anchors:

- Cream Paper `#f3f4ee` for Page canvas, card surfaces - the warm off-white that makes every ink color feel like print
- Bone White `#f8f8f8` for Alternate surface wash, subtle section differentiation from the cream canvas
- Press Black `#231f20` for Primary text, borders, dividers, icon strokes - the near-black ink that anchors every screen
- Charcoal Headline `#383435` for Display heading text - slightly lifted from press black for softer masthead weight
- Mid Gray `#9a9a9a` for Muted helper text, hairline borders, secondary metadata
- Pure Black `#000000` for Icon fills, maximum-contrast borders, nav accent
- Cobalt Ink `#245dc5` for Primary brand color - illustrated duotone wash, outlined action borders, interactive text - saturated blue against cream creates the risograph-print signature
- Peach Wash `#ffc6a6` for Secondary illustration accent, decorative borders, warm tonal fill - the cheek-pink of risograph layering
- Fire Red `#f04736` for Outlined action borders, emphasis strokes, error-like accent - used as editorial red rather than as a functional error state
- Vermillion `#f52302` for Deep red-orange accent for borders and fills - the warmest ink in the riso palette
- Crimson `#d42121` for Deep red accent - used sparingly in illustration washes and emphasis borders
- Marigold `#feee71` for Yellow accent fill, spot-color highlights, decorative emphasis - the third riso plate
- Terracotta `#b45e42` for Warm brown accent for body and heading borders - the earthiest ink in the editorial palette

Use these typography anchors:

- FoundersGrotesk `--font-foundersgrotesk` for Workhorse type for everything from body to display - single weight 400 with no bold variants means hierarchy is created purely through size, line-height, and letter-spacing, not weight contrast. The aggressive negative line-heights (0.80 at 130px) create magazine-cover masthead pressure. Substitute: Neue Haas Grotesk, Inter, Sohne.
- TimesNow SemiLight `--font-timesnow-semilight` for Editorial serif contrast for select headings and navigation - a humanist serif breaks the grotesque monotony at key moments, creating the magazine-section-divider effect. Substitute: Times Now, Tiempos, Source Serif.
- Sackville Script (hand-drawn wordmark) `--font-sackville-script-hand-drawn-wordmark` for Custom hand-inked cursive used only for the brand wordmark - overlaid on illustrations and hero compositions. Not a UI font. No substitute; this is the signature mark.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 43px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Age-Gate Oval Button (Primary Action): The signature interactive element - a fully oval outlined button that replaces a conventional filled CTA
- Secondary Text Link (I'm Under 21): Text-only fallback option below the primary oval button
- Age Verification Eyebrow: The question prompt above the age-gate button
- Hand-Drawn Wordmark: Brand identity mark overlaid on hero illustrations
- Duotone Illustration Panel: Full-bleed editorial artwork that dominates hero and section compositions
- Section Divider Rule: Horizontal separator between content sections
- Product Card: E-commerce or collection grid item
- Editorial Headline Block: Magazine-style display heading for section titles and hero copy
- Riso-Color Border Accent: Decorative border in secondary palette colors
- Navigation Bar: Top-level site navigation

Do:

- Use Cobalt Ink (#245dc5) as the outlined action border for all primary interactive elements - never fill a button with it; the outline is the brand's signature
- Set display type at 72px+ with line-height 0.80-0.85 to create the magazine-masthead compression that defines the system's editorial weight
- Let the cream canvas (#f3f4ee) show - do not cover it with white surfaces or dark mode equivalents; the warm paper tone is the brand's foundation
- Use the riso accent palette (Peach Wash, Fire Red, Marigold, Vermillion, Terracotta) only in illustration washes, decorative borders, and spot-color emphasis - never as functional UI fills for buttons, badges, or states
- Reserve TimesNow SemiLight for at most one or two heading moments per page - it breaks the grotesque monotony and should feel like a rare editorial interruption
- Keep the wordmark as a hand-drawn asset overlaid on illustration panels - do not re-create it in a web font or place it on flat surfaces without imagery
- Use the 81px radius exclusively for the age-gate oval and any other large interactive prompts - the stretched ellipse is a system signature, not a default

Avoid:

- Do not fill any button with Cobalt Ink, Fire Red, or any chromatic color - the system is outlined-action only; filled buttons would break the zine aesthetic
- Do not introduce box-shadows, drop-shadows, or any elevation effects - the design is flat by principle; depth comes from color contrast and illustration density, not from blur or offset
- Do not use a white (#ffffff) canvas - the cream (#f3f4ee) is warmer and is the reason the ink colors read as print rather than screen
- Do not set body text in the serif TimesNow SemiLight - it is a display contrast font only; body copy stays in FoundersGrotesk 400
- Do not apply bold or semibold weights - the type system is single-weight (400) by design; hierarchy is size and line-height, never weight
- Do not round cards or images beyond 10px - the 50px and 81px radii are reserved for buttons and the oval action; everything else stays close to sharp
- Do not add gradients, blurs, or glow effects to any element - the palette is risograph-flat; any smooth tonal transition breaks the print illusion

Source prompt cues:

Quick Color Reference:
- text: #231f20 (Press Black)
- background: #f3f4ee (Cream Paper)
- border: #231f20 (Press Black, 1px hairlines)
- accent: #245dc5 (Cobalt Ink)
- secondary accent: #ffc6a6 (Peach Wash)
- primary action: #245dc5 (outlined action border)

3-5 Example Component Prompts:

1. Create an age-gate oval button: transparent fill, 1.5px solid border in #245dc5, border-radius 81px, padding 18px 72px. Text: 'I'M OVER 21' in FoundersGrotesk 400, 42px, line-height 0.94, color #245dc5. On the cream canvas (#f3f4ee). No shadow, no hover fill change - the outline IS the affordance.

2. Create an editorial headline block: text in FoundersGrotesk 400, 99px, line-height 0.80, color #231f20. Two or three words max. No bold, no underline, no color accent - the size and negative leading do all the work. Background is the cream canvas (#f3f4ee) with no container.

3. Create a duotone illustration panel: full-bleed left half of a split layout, no border, no radius. Illustration rendered in #245dc5 on the #f3f4ee negative space. Overlay the hand-drawn 'Sackville' cursive wordmark at 100% width across the top in #245dc5. No peach or red accents in this version - pure two-color riso.

4. Create a product card: no background fill, no border, no shadow, no radius. Product image fills the card area at 10px corner radius only if the image is rectangular. Metadata below: product name in FoundersGrotesk 400, 22px, line-height 1.15, color #231f20. Price in same type, 16px, color #383435. The card is the image, not a frame.

5. Create a riso-accent callout block: 1px solid border in Fire Red (#f04736) or Marigold (#feee71) at 1-2px stroke, padding 16px 20px, on the cream canvas. Interior text in FoundersGrotesk 400, 22px, color #231f20. The colored border is the only visual signal - no fill, no icon, no badge shape.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
