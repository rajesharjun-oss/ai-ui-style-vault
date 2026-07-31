# AI Implementation Prompt

Build a Pietrastudio-inspired interface using this source-derived style bundle.

Reference site: https://www.pietrastudio.com
Theme: light
Category: SaaS
North star: sunlit AI workshop on cream paper

Use these palette anchors:

- Ember Coral `#ff5c3c` for Primary CTA fill, active nav, brand accent - a warm vermillion that sits forward against cream backgrounds without feeling aggressive
- Pure White `#ffffff` for Page canvas, card surfaces, button text on dark fills - the base everything else rests on
- Ink Black `#000000` for Primary heading text, body text, dominant borders - the workhorse contrast color used at 1750+ instances
- Cream Paper `#f8f6f2` for Warm off-white surface layer for elevated cards and section bands - gives the page its sunlit warmth without leaving pure white
- Soft Cream `#fffbe7` for Accent card surface, tinted feature panels - a warmer cream for highlight cards that need to stand apart from the base canvas
- Charcoal `#141414` for Secondary text, link text, heavy borders - softer than pure black for UI chrome and metadata
- Iron Gray `#1f2026` for Body text, input borders, body chrome - near-black with a cool cast for dense informational UI
- Mid Gray `#6b6b6b` for Muted body text, helper text, icon borders - the primary de-emphasized text tone
- Silver `#c4c4c4` for Hairline borders, dividers, placeholder text - light structural lines that recede
- Slate `#333333` for Deep body text, secondary headings - sits between charcoal and black for weighted text that isn't headline-level
- Ash `#e8e8ea` for Shadow tint, ultra-light dividers, ghost surfaces - the near-invisible layer
- Goldenrod `#f9e070` for Category tag accent, feature card variant - warm yellow that pairs with coral gradients
- Sage `#57ad6a` for Category tag accent, feature card variant - natural green for growth/scale categories

Use these typography anchors:

- Attila-Bold `--font-attila-bold` for Display headlines - the tall, tightly-tracked serif/grotesque hybrid used for hero and section headings at 32-48px. The negative tracking (-0.02em) is signature: letters pull close at large sizes creating a dense, editorial block of text
- Attila Sans Uniform `--font-attila-sans-uniform` for Largest display moments - uniform-width variant for the biggest headlines where letterform consistency matters more than contrast
- Labil-Bold `--font-labil-bold` for Bold body emphasis and mid-weight headings - the weight-400 bold variant that gives inline emphasis and sub-headings without switching families
- Labil Grotesk `--font-labil-grotesk` for Primary body and UI font - the workhorse grotesque used for body copy, buttons, inputs, cards, and navigation at 12-24px. Tracking sits at -0.01em throughout, a subtle but consistent tighten
- Labil-Regular `--font-labil-regular` for Lighter body weight for body copy and descriptions - weight 300 for long-form paragraphs creates breathing space; weight 400 for compact UI. The 0.143em tracking on some instances suggests uppercase labels or tag text

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 16-24px.
- Element gap: 8-12px.

Build these component patterns where relevant:

- Coral Primary Button: Main call-to-action across the site
- Outlined Ghost Button: Secondary action paired with the primary
- Navigation Link Button: Top-bar utility actions
- Hero Search/Input Field: The central prompt input on the hero
- Feature Card - Gradient Category: Product capability cards with colored category tags
- Logo Bar Section: Social proof band
- Integration Card: Shows platform integrations
- Model Selection Card: Demonstrates AI model routing
- Agent Card (Horizontal): Feature row showing AI agent capabilities
- Navigation Bar: Top site navigation
- Tag / Category Label: Small functional labels on cards
- Hero Gradient Background: Atmospheric warm wash behind the hero headline

Do:

- Use the coral #ff5c3c for exactly one primary action per screen - never two coral CTAs competing
- Set display headlines in Attila-Bold at 40-48px with tracking -0.02em; the tight tracking is the editorial signature
- Apply the warm gradient swatch system (Royal, Sky, Verdant, Magenta, Sunrise) only to category tags and decorative cards - not to body text or backgrounds
- Layer shadows as inset highlights + warm-tinted drops: the cream-on-cream shadow is what separates cards from the canvas
- Use 12px radius as the default card radius, 8px for buttons and inputs, 9999px for tags - this three-tier radius system is the structural rhythm
- Keep body copy in Labil Grotesk at 16px with 1.5 line-height; the 0.143em uppercase tracking is reserved for small all-caps labels only
- Maintain a warm white palette: #ffffff for the page canvas, #f8f6f2 for elevated surfaces, #fffbe7 for accent cards - never introduce cool grays

Avoid:

- Do not use coral for secondary actions, links, or decorative elements - it loses its action weight if scattered
- Do not use Attila for body copy or UI text - it is display-only and overwhelms at small sizes
- Do not apply the category gradient swatches as full card backgrounds or page sections - they are tag-sized accents
- Do not introduce drop shadows in cool gray tones; all shadows should carry the warm pink/cream tint to match the surface palette
- Do not use sharp 0px radii on cards or images - the rounded geometry is essential to the soft, paper-like feel
- Do not stack multiple saturated colors in a single component - one chromatic accent per element, with grayscale for everything else
- Do not use letter-spacing wider than -0.01em on body text; the system is consistently tight-tracked and loosening it breaks the type voice

Source prompt cues:

primary action: #ff5c3c (filled action)
Create a Primary Action Button: #ff5c3c background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
Quick Color Reference:
- text: #000000 (headlines, body)
- background: #ffffff (canvas), #f8f6f2 (elevated surface), #fffbe7 (accent card)
- border: #c4c4c4 (hairline), #141414 (strong)
- accent: #ff5c3c (coral, primary action only)
- category tag gradients: Royal #5b3af7, Sky #4160ff, Verdant #38c585, Magenta #c83ad6, Sunrise #ff4a4a

Example Component Prompts:


2. Create a feature agent card grid: 3 columns of white cards on #f8f6f2 section background, 80px section padding. Each card: white surface, 16px radius, warm-tinted shadow (rgba(239,227,225,0.3) 5px 5px 24px), 20px padding. Top-left: a gradient pill tag (e.g., Royal gradient, 9999px radius, white 12px bold text). Heading at 20px Labil-Bold weight 400, #000000. Description at 14px Labil-Regular weight 300, #6b6b6b. Bottom: a coral text link 'Learn more ' in 14px Labil-Bold, #ff5c3c. Cards separated by 24px gap.

3. Create a logo bar section: full-width #fffbe7 background, 60px vertical padding. Centered label 'Trusted by leading commerce teams' at 14px Labil-Regular weight 400, #6b6b6b, 0.143em tracking. Below: a responsive grid of 12 grayscale brand logos at uniform 24px height, evenly spaced with 40px gaps, arranged in 2 rows.

4. Create a navigation bar: 64px height, white background, subtle 1px bottom border #e8e8ea. Left: 'Pietra' wordmark in Labil-Bold 20px #000000. Center: nav links (Products, Solutions, Resources, Help Videos, Pricing) at 14px Labil Grotesk weight 500, #000000, with 32px horizontal gaps. Right: 'Book demo' and 'Sign in' as plain text links, then a coral filled button 'Start for free' with 8px radius, #ff5c3c fill, white 14px Labil-Bold text, 10px 16px padding.

5. Create an integration showcase card: #fffbe7 background, 20px radius, 24px padding, warm soft shadow. Heading at 24px Attila-Bold weight 400, #000000, letter-spacing -0.24px, reading 'The only AI that connects to your real time data'. Below: a 4x2 grid of small monochrome brand icons (32px) with 24px gaps, each on a subtle white circular background (40px diameter, #ffffff, 1px #e8e8ea border).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
