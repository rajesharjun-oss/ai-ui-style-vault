# AI Implementation Prompt

Build a Oevra-inspired interface using this source-derived style bundle.

Reference site: https://oevra.com
Theme: light
Category: Productivity
North star: sage greenhouse at dawn

Use these palette anchors:

- Eucalyptus `#ffffff` for Headline accents, body text emphasis, hairline borders, single filled CTA - the only chromatic voice in the entire system. Muted enough to never shout, present enough to carry the brand; Full-bleed background gradient behind hero and section text. The green is a breath, not a wall - it fades to white at the edges so text remains the focus
- Ink Black `#000000` for Primary text, dividers, image borders, icon strokes. Used at 1px hairline weight almost exclusively - never as a fill
- Pure Canvas `#ffffff` for Page background, card surfaces, button text on filled green CTAs. The dominant surface color across the entire site
- Graphite `#4e4e4e` for Secondary body text, muted link borders, helper copy, footer text. Quieter than black but still AA-readable on white
- Mist `#c8c8c8` for Subtle surface wash for elevated panels, image placeholder backgrounds, very faint dividers. Used sparingly to add depth without darkening the page

Use these typography anchors:

- space-regular `--font-space-regular` for space-regular - detected in extracted data but not described by AI
- Suisse Int'l `--font-suisse-intl` for Display and headline face. Light weight at 45-90px is the signature - headlines whisper instead of shout, creating a contemplative, editorial tone. Used for all section headlines, hero copy, and feature titles.
- Suisse Int'l `--font-suisse-intl` for Secondary body and footer text. Regular weight adds density to descriptions and supporting paragraphs beneath light-weight headlines.
- Space Grotesk `--font-space-grotesk` for Primary body, UI labels, buttons, and navigation text. The geometric counter-forms pair with Suisse to give dense text a different texture from the display headlines.
- System Sans `--font-system-sans` for Micro-utility text, scroll indicators, and fine-print captions where a 1-2 word label sits in the margins.
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI
- suisse-light `--font-suisse-light` for suisse-light - detected in extracted data but not described by AI
- suisse-regular `--font-suisse-regular` for suisse-regular - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 75px.
- Card padding: 30px.
- Element gap: 23px.

Build these component patterns where relevant:

- Navigation Bar: Top-level site navigation
- Display Headline Block: Hero and section headlines
- Inset Headline Image: Photo embedded mid-headline
- Ghost Pill Button: Primary call-to-action
- Filled Green Button: Sole chromatic CTA (SIGN UP in nav context)
- Section Label: Small uppercase eyebrow above headlines
- Numbered Feature Item: Step indicators in feature lists
- Image Card: Product screenshot or photograph container
- Body Description Block: Supporting paragraph text
- Vertical Scroll Indicator: Page-position cue on left margin
- Footer Link Column: Footer navigation list
- Hairline Divider: Visual separation

Do:

- Use Suisse Int'l at 300/400 weight for all headlines, scaled 45-90px with line-height 1.0-1.1
- Apply the Sage Mist radial gradient as the default page background wash - it should breathe, not saturate
- Reach for #778643 on text, borders, and the single filled CTA - never on large filled surfaces
- Use 15px border-radius on cards and images, 22.5px on all interactive elements (buttons, links, pills)
- Set section gaps at 75px and card padding at 30px - the spaciousness IS the brand
- Keep body text at 15px with 1.3 line-height in #4e4e4 for graphite-toned supporting copy
- Pair every display headline with a short uppercase section label (8-12px) as its anchor

Avoid:

- Do not introduce a second chromatic color - the entire palette is one green and four neutrals
- Do not use bold or semibold weights for headlines; light weight at large size is the signature
- Do not apply box-shadows, glows, or blur effects for elevation - separation comes from whitespace and hairlines
- Do not use sharp corners (0-4px radius) on any surface or interactive element
- Do not use #778643 as a solid page or section background - it must always be diluted by the gradient or rendered as a thin line
- Do not crowd the layout with small text; if a paragraph exceeds 3 lines, the type is too small for the system
- Do not use icon fills or saturated illustrations - the visual language is photography, type, and gradient only

Source prompt cues:

**Quick Color Reference**
- background: #ffffff (with #778643 radial gradient wash)
- text: #000000 (primary), #4e4e4e (secondary), #778643 (accent)
- border: #000000 or #4e4e4e at 1px hairline
- accent: #778643
- primary action: #778643 (filled action)

**Example Component Prompts**
1. *Hero Section*: Full-bleed #ffffff base with radial-gradient(ellipse at 50% 50%, rgba(119,134,67,0.35), rgba(119,134,67,0.08) 50%, #ffffff 100%). Centered display headline at 90px Suisse Int'l weight 300, color #ffffff, line-height 1.0, spanning 3 lines. Below: 15px Space Grotesk weight 400, color #4e4e4e, max-width 45ch. Ghost pill CTA at bottom-right: 1px white stroke, 22.5px radius, 11px/23px padding, 12px Space Grotesk uppercase label + arrow.

2. *Feature Section on White*: White background. 8px uppercase section label '#778643' left-aligned, 45px Suisse Int'l weight 300 headline in #778643. Small 60px square photograph with 15px radius inset into the headline line. Below: 15px Space Grotesk body in #4e4e4e, 30px gap to ghost outline button (1px #000 stroke, 22.5px radius).

3. *Numbered Feature Row*: Three columns at section base, 60px column gap. Each item: 8px '#778643' number (01, 02, 03) above 12px Space Grotesk uppercase label in #000000.

4. *Product Image Card*: Photograph at 15px border-radius with 1px #000000 hairline border, positioned bottom-right of section, overlapping the text column slightly. No padding, no shadow.

5. *Navigation Bar*: Transparent over gradient. Left: 12px white logo + 'oevra'. Right: 8-12px white Space Grotesk uppercase nav links (ABOUT, LOGIN) + white outlined pill button (SIGN UP) at 22.5px radius, 1px white stroke, 11px/23px padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
