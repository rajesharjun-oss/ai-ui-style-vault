# AI Implementation Prompt

Build a NCDA-inspired interface using this source-derived style bundle.

Reference site: https://ncda.biz
Theme: mixed
Category: Agency
North star: Architectural monograph in negative space. The NCDA wordmark at 62px is cropped by the viewport edge, turning a logo into a wall.

Use these palette anchors:

- Onyx `#191919` for Primary text, hairline borders, full-bleed dark surface bands - the near-black ink of the system
- Pure Black `#000000` for Secondary text fills, deepest borders, and image overlays where maximum contrast against white is required
- Paper `#ffffff` for Page canvas, surface backgrounds, inverse text on dark bands
- Concrete `#808080` for Secondary descriptive text, muted link borders, subdued meta-information - the gray of footnotes and captions

Use these typography anchors:

- TWK Everett `--font-twk-everett` for All interface and display type - a neo-grotesque with tall x-height and geometric openness. The sole weight (400) across the entire range from 11px captions to 62px display creates a monolithic typographic voice. At 62px it receives aggressive negative tracking (-0.05em) that pulls the letterforms into a continuous architectural band; at 11px it switches to slight positive tracking (+0.04em) for utilitarian legibility in timestamps and labels.
- TWK Everett Mono `--font-twk-everett-mono` for Monospaced companion for data and technical annotations - used sparingly in body contexts where tabular alignment or code-like precision is needed. Single size at 21px with -0.01em tracking.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: .
- Section gap: 64-150px.
- Card padding: 0px.
- Element gap: 15px.

Build these component patterns where relevant:

- Architectural Wordmark Display: Brand identity rendered as a full-width layout device
- Dual-City Live Clock: Persistent header utility - time stamps in two zones
- Menu Trigger: Sole navigation element - top-right anchor
- Studio Description Block: Identity statement on the landing canvas
- Full-Bleed Dark Band: Section break / project image container
- Hairline Rule Link: Inline link or navigation divider
- Time-Indexed Label: Metadata / project reference tag

Do:

- Use TWK Everett Regular (400) at every size from 11px to 62px - never introduce bold or medium weights, the single-weight system is the signature
- Set the wordmark or any display text at 62px with -0.05em letter-spacing and line-height 0.80 to create the continuous architectural band effect
- Apply +0.04em letter-spacing to all text at 11px and below - the positive tracking is what makes captions read as technical annotations rather than body type
- Crop type and imagery at the viewport edge - the bleed is structural, never add padding to prevent it
- Use #191919 Onyx for all borders and dark surface bands; reserve #000000 Pure Black for text fills where maximum contrast is critical
- Separate content sections with full-bleed #191919 bands - no gradients, no soft transitions between white and dark
- Keep interactive elements text-only - no buttons, no icons, no filled rectangles; use 1px #808080 hairline rules to indicate links

Avoid:

- Do not introduce any chromatic color - the system is 0% colorfulness by design, any hue breaks the monograph language
- Do not add border-radius to any element - all corners are sharp 0px, rounded shapes would undermine the architectural print language
- Do not use drop shadows or elevation effects - depth comes from scale and negative space, not from shadow stacks
- Do not set body or paragraph type at 62px - that size is reserved for the wordmark and display headlines that function as layout architecture
- Do not use more than two type sizes on a single screen - the system relies on extreme size contrast (15px body vs 62px display), intermediate sizes dilute the rhythm
- Do not add icons, arrows, or decorative glyphs to the Menu trigger or any navigation - the plain text label is the entire affordance
- Do not center-align body text - left-align everything; centering is reserved for the wordmark, everything else hangs from a left edge

Source prompt cues:

**Quick Color Reference**
- text: #000000 (primary), #808080 (secondary), #ffffff (inverse on dark)
- background: #ffffff (canvas), #191919 (dark band)
- border: #191919 (structural), #808080 (hairline/link)
- accent: none - system is 0% chromatic
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build the landing hero: white #ffffff canvas. Top-left: two monospaced timestamps '09:58:21 HK' and '21:58:21 NYC' in TWK Everett 11px, weight 400, letter-spacing +0.04em (0.44px), color #000000, separated by 53px gap. Top-right: 'Menu' in TWK Everett 15px, weight 400, #000000, flush right. Upper-right quadrant: description block ~400px wide, 'NC Design and Architecture Ltd.' in #000000, remainder in #808080, TWK Everett 15px, line-height 1.44, 59px left padding. Lower 60%: 'NCDA' in TWK Everett 62px, line-height 0.80, letter-spacing -3.1px (-0.05em), #000000, sized to overflow viewport horizontally and crop on both edges.

2. Build a project section band: full-viewport-width rectangle, background #191919, height 100vh, no border, no radius, no shadow. Image inside fills the band edge-to-edge with no padding or margin.

3. Build a time-indexed label: plain text in TWK Everett 11px, weight 400, color #808080, letter-spacing +0.04em, no background, no border, no badge shape - just spaced gray type inline with content.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
