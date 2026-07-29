# Ciridae Design Reference

## North Star

void chamber with ember pulse a near-black cathedral where the only warm note is a thin line of ember rust, and every surface is defined by hairline borders rather than shadow.

## Theme

dark style for AI interfaces.

## Color System

- Ember Rust `#cc6437` for Accent strokes, icon linework, small text highlights the only chromatic color in an otherwise monochrome system, appearing as a hairline pulse rather than a fill
- Void Black `#0b0b0b` for Primary page canvas and section backgrounds; the foundation of the entire system
- Charcoal Surface `#272a2a` for Card and panel backgrounds on dark sections one step lighter than the canvas to create surface separation without shadow
- Bone `#edebe7` for Light section backgrounds and off-white surfaces where the system flips from dark to bright
- Bone Darker `#dfddd9` for Subtle variant of Bone for layered light surfaces and warm-tinted off-white elements
- Pure White `#ffffff` for All body and heading text, ghost button borders, nav elements the dominant foreground color at 19.7:1 contrast on Void Black
- Abyss `#050505` for Elevated bar backgrounds (top news strip) one shade darker than the main canvas to push the bar forward
- Steel `#484848` for Mid-tone border for secondary solid buttons where Pure White would be too stark

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- Pragmatica Cond Primary display and UI typeface narrow condensed uppercase at 14px for body, 20px for section labels, 32px for hero wordmark. The extreme narrowness and all-caps setting at 14px body size is the system's most signature choice: body text reads as a whisper of architectural type, not conventional prose. Substitute with Oswald or Barlow Condensed if Pragmatica Cond is unavailable. `--font-pragmatica-cond`
- Pragmatica Secondary body typeface used for longer-form prose passages (e.g. the 'AI Operating System' card description at 24px, paragraph text at 15px). Slightly wider than Pragmatica Cond for reading comfort in extended blocks, but still 400 weight no bold ever. Substitute with Inter or Shne. `--font-pragmatica`
- Roboto Mono Monospace micro-type for the top news bar ticker ('NEWS JUN 15, 2026 CRUCIBLE EARLY ACCESS IS NOW OPEN'). The only place monospace appears, creating a clear functional distinction: this is system data, not brand voice. `--font-roboto-mono`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: source-defined
- Density: comfortable
- Page max-width: 1400px
- Section gap: 80px
- Card padding: 32px
- Element gap: 16-20px

## Components

- Ghost Pill Button: Primary interactive control across the site
- News Bar Solid Button: Top-page system announcement trigger
- Pill Badge: Status markers, numbered tags, micro-labels
- System Card: Content panels in the product systems section
- Top News Bar: Site-wide announcement strip fixed at the top of every page
- Constellation Logo Mark: Brand identity anchor in the hero and load contexts
- Hero Section: Full-viewport opening composition
- Backers Logo Strip: Social proof section with inverted light theme

## Implementation Guidance

- Use 1440px border-radius for all buttons, badges, nav items, and pill-shaped interactive elements
- Use 10px border-radius exclusively for card and content containers pill = interactive, rounded-rect = content
- Set all text in uppercase using Pragmatica Cond at weight 400 never use bold, never use mixed case
- Apply -0.02em letter-spacing to all type sizes above 14px; -0.01em is acceptable for 15px body passages
- Define surfaces through background tonal shifts (#0b0b0b #272a2a #edebe7) and 1px hairline borders, never through box-shadow
- Reserve #cc6437 Ember Rust for hairline accent strokes and small text highlights only never use it as a fill
- Use Roboto Mono 11px exclusively for system data (news ticker, metadata, technical labels) to create a clear typographic register

## Guardrails

- Do not introduce bold or semi-bold weights the entire system operates at weight 400 only
- Do not add drop shadows, glow effects, or any box-shadow values the system is intentionally flat
- Do not use color fills on buttons all interactive controls are ghost/outlined with 1px borders
- Do not use mixed-case text or sentence case in any UI label, heading, or body string
- Do not introduce additional accent colors Ember Rust is the only chromatic note permitted
- Do not use non-pill radii (e.g. 4px, 8px) on buttons, badges, or nav items the 1440px pill is the system's signature shape
- Do not use gradients the system is built on flat color fields and blurred photography, not color transitions
