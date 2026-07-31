# AI Implementation Prompt

Build a Aaron Poe-inspired interface using this source-derived style bundle.

Reference site: https://aaronpoeandco.com
Theme: light
Category: Agency
North star: Quiet white gallery - coral pink whispers float in vast considered silence, framed only by pill-shaped nav and tightly-tracked type.

Use these palette anchors:

- Coral Rose `#ea587d` for Accent for heading text, hairline borders, and active-state markers - the single chromatic signal in an otherwise achromatic system
- Pure White `#ffffff` for Page canvas, card surfaces, and inverted backgrounds
- Cloud `#f2f2f2` for Pill nav background, subtle surface elevation, and inset border shadows
- Bone `#d9d8d4` for Warm-toned secondary surface tint for alternating bands
- Char `#282828` for Primary text, body copy, and most interface strokes
- Ink `#121212` for Heavier headings, body text, and prominent borders
- Black `#000000` for Maximum-emphasis text, logo wordmark, and strong border lines
- Fog `#b3b3b3` for Muted helper text and disabled-state strokes
- Mist `#cccccc` for Lowest-emphasis borders and decorative dividers

Use these typography anchors:

- -apple-system `--font-apple-system` for System-font fallback for body text and rendering across platforms. Used wherever native OS fonts provide a reliable, performance-optimized default at body size.
- Geist `--font-geist` for Primary display and UI typeface. The 300 weight at micro sizes (8-10px) creates whisper-quiet labels; the negative letter-spacing (-0.056em at 8px, -0.037em at 10px) tightens small type into dense, confident blocks. 400 at 16-18px serves body and subheadings with -0.025em to -0.011em tracking.
- wtqc (custom display) `--font-wtqc-custom-display` for Reserved for prominent display headings (30px, 1.07 line-height, -0.033em tracking) and compact labels (12px, 1.33 line-height). The tight 1.07 line-height on the 30px size gives headings a condensed, editorial feel.
- custom_166638 `--font-custom166638` for custom_166638 - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 720px.
- Section gap: 120px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Wordmark Logo: Brand identity in the top-left corner
- Pill Navigation Bar: Primary site navigation
- Nav Item - Default: Inactive navigation link
- Nav Item - Active (with dot indicator): Current page indicator in the pill nav
- Bio Text Block: Centered hero content - the creator's statement
- Section Heading with Coral Border: Content section titles and category labels
- Ghost Button (Start a Project): Contact / conversion action in the nav
- Hairline Card: Content container for case studies, project tiles, or grouped content
- Inset Border Divider: Ultra-subtle section separation without visible lines
- Project Tile: Portfolio work entry - image or text-based

Do:

- Use #ea587d only on heading text, hairline borders, and the active-nav dot - never as a filled button or background
- Set all headings in Geist or wtqc with negative letter-spacing (-0.033em to -0.056em depending on size) to achieve the compressed editorial feel
- Use 24px border-radius for the pill navigation and 4px for all cards and buttons
- Default to max-width 720px for centered text blocks; let whitespace do the layout work
- Separate cards and sections with 1px solid borders in #cccccc or #e5e5e5 - never with drop shadows
- Use #f2f2f2 as the surface tint for floating elements like the pill nav
- Set body text at 16-18px in #282828 with 1.38-1.5 line-height for comfortable reading

Avoid:

- Do not add drop shadows to cards, buttons, or navigation - the system is intentionally flat
- Do not use #ea587d as a button background fill - the accent only appears on headings and borders
- Do not use large border-radii on cards - keep them at 4px; only the pill nav gets 24px
- Do not introduce new chromatic colors - the system is deliberately monochrome with one pink accent
- Do not use positive letter-spacing - all text tracks tight (negative values) to feel compressed and confident
- Do not fill the page with imagery or illustrations - let typography and whitespace carry the composition
- Do not use dark mode as the default theme - white canvas is the signature; dark (#121212) is reserved for inverted sections only

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
