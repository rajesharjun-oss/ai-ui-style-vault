# AI Implementation Prompt

Build a Tech Barcelona-inspired interface using this source-derived style bundle.

Reference site: https://techbarcelona.com/en
Theme: mixed
Category: Other
North star: Editorial tech manifesto on white marble

Use these palette anchors:

- Cobalt Action `#0075ff` for Primary CTA buttons, the only chromatic accent in the entire interface - one vivid blue against monochrome neutrals, used sparingly so it signals action without competing with content
- Ink Black `#090707` for Headline color, image borders, large display text - near-black with the slightest warmth, chosen over pure black to feel printed rather than digital
- Graphite `#212529` for Body text, nav links, icon strokes, card borders - the working neutral for interface chrome and readable paragraph copy
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark hero and dark logo backgrounds - establishes the light-mode base and all content surfaces
- Hairline Gray `#cccccc` for Subtle dividers and secondary borders - thin separator lines on light surfaces where #212529 would be too heavy
- Pure Black `#000000` for Dark borders and separators for elevated surfaces and inverted UI.
- Shadow Whisper `#eeeeee` for Near-invisible ambient shadow tint for button states - a 1px 1px wash so faint it barely registers, used instead of full drop-shadows

Use these typography anchors:

- FavoritPro-Light `--font-favoritpro-light` for Single-family type system used for every interface element - nav, body, buttons, headlines, and 80px display. Weight 400 throughout is a signature choice: the system relies on scale jumps (14px body 50px subhead 80px display) rather than bold weights to establish hierarchy, giving the entire site an understated, editorial cadence

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 50-80px.
- Card padding: 16px.
- Element gap: 4-10px.

Build these component patterns where relevant:

- Primary Action Button: The only filled chromatic button in the system
- Ghost Button: Secondary or tertiary action on light surfaces
- Top Navigation Bar: Persistent header across all pages
- Hero Block: Full-bleed dark opening band
- Stats Ticker Bar: Horizontal numerical proof band
- Full-Bleed Image Block: Editorial photography section
- Story Card: Content preview tile for articles/news
- Section Divider: Vertical or horizontal rule between content blocks
- Language Switcher: Locale toggle in nav
- Category Tag: Small label for content taxonomy

Do:

- Use FavoritPro 400 at every size and weight - do not introduce bold or medium weights; hierarchy comes from scale alone
- Use #0075ff exclusively for filled primary action buttons - never as a background surface, icon fill, or decorative accent
- Set headline letter-spacing to -0.045em at 50px and above to compress the display type into confident, tight masses
- Use 0px border-radius on all components - buttons, cards, inputs, and images all share sharp corners to maintain editorial discipline
- Maintain at least 50px vertical space between major content sections to let the large typography breathe
- Use +0.08em and +0.09em letter-spacing only for uppercase labels and tracked-out metadata, never on sentence-case body text
- Let the dark hero band (#000000) appear once per page; all subsequent sections should resolve to white #ffffff canvas

Avoid:

- Do not use shadows or elevation effects - the system is intentionally flat with hairline borders only
- Do not introduce additional chromatic colors - the blue/cobalt is the sole accent and its power depends on singularity
- Do not use bold (600+) or semibold weights - the entire interface speaks at weight 400 and louder weights would break the voice
- Do not apply rounded corners (border-radius) to any element - the squared-off geometry is load-bearing
- Do not add gradients, textures, or background patterns to any surface - every surface is a flat solid color
- Do not use #ffffff as a filled button background for actions - the only filled action color is #0075ff; everything else is ghost or text-link
- Do not compress line-height below 1.0 on display sizes - the tight tracking combined with the geometric letterforms already create visual density

Source prompt cues:

primary action: #0075ff (filled action)
Create a Primary Action Button: #0075ff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
