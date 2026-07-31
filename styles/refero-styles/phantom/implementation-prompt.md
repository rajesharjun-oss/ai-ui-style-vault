# AI Implementation Prompt

Build a Phantom-inspired interface using this source-derived style bundle.

Reference site: https://phantom.com
Theme: mixed
Category: Crypto
North star: lavender candy shop at dusk. A monochromatic violet world where everything is a soft pill on a near-white plane, interrupted by a mischievous ghost and pastel highlights.

Use these palette anchors:

- Aubergine `#3c315b` for Primary brand - navigation borders, nav text, heading text, card surfaces in dark sections, icon strokes. The structural spine of the entire system
- Ghost Lavender `#e2dffe` for Primary action - filled CTA button background, violet glow shadow on buttons. The light-on-light button that only reveals its presence through a soft 4px halo
- Periwinkle `#ab9ff2` for Secondary action - brighter lavender for secondary CTAs, decorative fills, icon accents. Adds saturation to the pale-violet world
- Cornflower Pop `#4a87f2` for Accent button - occasional vivid blue button for emphasis or differentiation. Use sparingly as a high-energy interruption
- Buttercream `#ffffc4` for Accent button - pale yellow button fill for variety in multi-action contexts. Pastel punctuation in the candy palette
- Blush Mist `#ffdadc` for Accent button - near-gray pink button for warmth and tonal range. The softest of the pastel set
- Mint Signal `#2ec08b` for Success badge - vivid green for status indicators, positive confirmations, live signals
- Paper White `#fdfcfe` for Canvas - page background, card surfaces, button borders, text on dark backgrounds. Near-white with the faintest cool tint
- Obsidian `#1c1c1c` for Body text, heading text on light backgrounds, button borders, card borders. The near-black ink for all foreground content
- Fog `#86848d` for Muted text, icon strokes, secondary nav borders. The quiet gray for non-emphasized elements
- Ash `#e9e8ea` for Button background, subtle surface fill. The neutral pale surface beneath lavender hero panels
- Bone `#f4f2f4` for Surface background - light section panels, button fills. The warmest of the near-white neutrals

Use these typography anchors:

- Phantom `--font-phantom` for Custom typeface used for everything. Weight 350 is the default body and display weight - unconventional lightness creates an airy, anti-bold personality. Weight 400 reserved for body copy that needs slightly more presence. Sizes scale dramatically from 13px caption to 96px display. Tight -0.025em letter-spacing at all sizes creates compressed, high-density headlines. Line-height collapses to 1.0-1.1 at display sizes for sculptural headline forms.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 48px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Pill Navigation Bar: Primary site navigation
- Download Button (Header): Primary CTA in navigation
- Hero Section (Dark): Full-bleed hero with inverted color treatment
- Hero Section (Light): Full-bleed hero on light background
- Muted Purple Hero Panel: Intermediate hero - soft violet wash
- See More Link Button: Inline section navigation
- Ghost Character Accent: Decorative brand element within headlines
- Pastel Accent Button Set: Multi-variant action buttons for variety
- Logo Lockup: Brand mark
- Search Icon Button: Header utility action
- Success Badge: Status indicator
- Card Surface: Content container

Do:

- Use 100px border-radius for all navigation containers, buttons, and tags - the pill geometry is the system's defining silhouette
- Set all text at weight 350 by default; reserve weight 400 for body copy that needs extra legibility
- Apply -0.025em letter-spacing at every type size - the tight tracking is non-negotiable for brand fidelity
- Use Ghost Lavender (#e2dffe) as the primary CTA fill, paired with the rgb(226,223,254) 0px 0px 4px 0px glow shadow
- Alternate between light and Aubergine dark sections to create rhythm - both modes are equally native to the system
- Collapse line-height to 1.0-1.1 for display sizes 64px and above; let the massive type breathe vertically without gaps
- Replace a vowel in display headlines with the ghost mascot rendered in Periwinkle (#ab9ff2) for brand playfulness

Avoid:

- Don't use drop shadows beyond the single 4px violet glow on primary CTAs - the system stays flat
- Don't set text at weight 600+ - the 350 whisper-weight is the brand's voice, not a choice for emphasis
- Don't use sharp corners under 16px - the world is pills and soft capsules
- Don't introduce saturated colors outside the pastel accent set (#4a87f2, #ffffc4, #ffdadc) - the palette is intentionally narrow
- Don't set body text larger than 16px weight 400 or use line-height above 1.4 - readability rules apply but stay restrained
- Don't use high-contrast decorative elements like gradients, patterns, or backgrounds images - surface is always flat color
- Don't add border-radius values below 24px on cards or 16px on smaller elements - every container should feel soft

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
