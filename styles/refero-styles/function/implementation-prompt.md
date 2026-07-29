# AI Implementation Prompt

Build a Function-inspired interface using this source-derived style bundle.

Reference site: https://www.functionhealth.com
Theme: light
Category: Other
North star: warm apothecary journal on parchment

Use these palette anchors:

- Parchment `#fef9ef` for Page canvas and primary surface - never use pure white; this warm off-white is the system's base tone
- Aged Paper `#f5eee1` for Card and panel surfaces, subtle wash backgrounds - one step deeper than the canvas to create soft elevation without shadows
- Warm Taupe `#d1c9bf` for Hairline borders, divider lines, card outlines - replaces cold gray with a tone that belongs to the cream family
- Ink `#2a2b2f` for Primary text, heading fills, strong borders - near-black with a barely-warm cast to harmonize with parchment rather than fight it
- Charcoal `#333333` for Secondary text, body copy, default icon fills, structural borders - slightly softer than Ink for reading-length passages
- Graphite `#515151` for Muted helper text, captions, secondary metadata - never below 14px without sufficient weight to maintain AAA contrast on parchment
- Ash `#808988` for Input borders, disabled state outlines, placeholder text - the only cool-leaning neutral, used only on form elements
- Pure Black `#000000` for SVG fill default, logo mark - reserve for vector illustration, never use as text or background

Use these typography anchors:

- Financier Display `--font-financier-display` for Display and editorial headlines - weight 400 for roman, weight 300 for italic accent words within the same headline (e.g. 'Testing is easy' pairs roman with italic). The mix of roman + italic serif in one line is the system's most distinctive typographic move. Substitute: GT Super, Domaine Display, Tiempos Headline
- Ftbase `--font-ftbase` for Body, navigation, buttons, UI labels, and all interface text. Weight 300 is used for hero subhead and large descriptive passages; weight 400 for body; weight 600 for button labels and strong UI; weight 700 reserved for emphasis. The consistent -0.023em tracking pulls the type into a tight, confident block that contrasts the generous serif spacing. Substitute: Inter, Sohne, or Untitled Sans
- Fragment mono `--font-fragment-mono` for Tiny all-caps labels in badge and eyebrow contexts - monospace gives a clinical, data-precise feel for markers like 'HSA/FSA Eligible'. Use sparingly; Ftbase caps at 600+ serve most label needs

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 64-96px.
- Card padding: 24-32px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary CTA Button: Main conversion action - 'Start testing', 'Get started'
- Outlined Secondary Button: Supporting action - 'See how it works', 'Learn more'
- Ghost Text Button: Nav links, low-priority actions, 'Log in'
- Announcement Bar: Top-of-page promotional message - 'Use your HSA/FSA funds'
- Primary Navigation Bar: Site-wide navigation
- Numbered Step Card: How-it-works feature step ('01', '02', '03')
- Doctor Testimonial Card: Social proof with credentialed endorsement
- Hero Stat Block: Key metric in hero or feature sections - '160+ lab tests', '$1 per day'
- Eyebrow Label: Section pre-title - 'HSA/FSA Eligible', 'Step 01'
- Disease Tag: Inline condition marker - 'Prostate cancer', 'Anemia'
- Bar Chart Widget: Data visualization in feature cards and results previews
- Input Field: Form input - search, email, date

Do:

- Use Financier Display for all editorial headlines, always pairing roman and italic weights within the same line to create the signature typographic rhythm
- Set body and UI text in Ftbase with the global -0.023em tracking, never override it per element
- Default to the cream surface stack (Parchment Aged Paper Taupe Outline) for elevation before reaching for shadows
- Apply the 40px border-radius to all buttons and the 24px radius to all cards - rectangular shapes break the system's identity
- Reserve #b05a36 for exactly three uses: primary CTAs, eyebrow labels, and active/selected states - never as body text or large surface fills
- Use the terracotta bullet '-' with 16px horizontal spacing when listing inline items like diseases or categories
- Keep hero photography warm-toned with a dark overlay so headlines in white or parchment remain legible

Avoid:

- Never use pure white (#ffffff) as a background - it kills the parchment warmth that defines the brand
- Don't set body text in anything other than Ftbase; the serif is for editorial headlines only
- Don't use small sharp drop shadows; elevation must come from color stepping or the two approved shadow recipes
- Don't apply the terracotta to large background areas, decorative blocks, or text over 24px - it overwhelms when undiluted
- Avoid rectangular buttons or square card corners; the rounded shape family (40px / 24px / 9999px) is non-negotiable
- Don't introduce a second accent color - the system is monochromatic warm with one rust accent, and a second hue breaks the apothecary mood
- Don't use the -0.023em tracking on the serif Financier Display - it belongs only to Ftbase

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
