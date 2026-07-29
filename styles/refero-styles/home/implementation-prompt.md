# AI Implementation Prompt

Build a Home-inspired interface using this source-derived style bundle.

Reference site: https://www.useparallel.com
Theme: light
Category: SaaS
North star: Warm editorial atelier. Cream paper, charcoal ink, and one ember-orange period of emphasis - a job platform that feels like an art-book spread photographed under amber light.

Use these palette anchors:

- Cream Paper `#e4dfd9` for Page background canvas, hero overlays, editorial section backdrops - the warm off-white that sets the entire system apart from generic SaaS grays
- Pure White `#ffffff` for Card surfaces, product UI mockups, input fields, text on dark photography
- Charcoal Ink `#000000` for Primary text, strong borders, icon strokes, logo wordmark - the maximum-contrast voice
- Near Black `#050505` for Body text and heading color for subtle warmth below pure black
- Pressed Graphite `#171717` for Filled button backgrounds, dark UI surfaces, photo overlay scrims
- Slate `#737373` for Secondary text, subtle heading borders, metadata - the 60% voice
- Iron `#4b4b4b` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Stone `#999694` for Muted body text, caption-level copy, placeholder text
- Pewter `#666666` for Hairline borders on low-emphasis elements, dividers
- Fog `#c7c7c7` for Hairline borders, subtle dividers, ghost outlines - the most frequent border color in the system

Use these typography anchors:

- Rules Font `--font-rules-font` for Editorial display face for all headings - the weight-500 medium is deliberately non-bold, creating a literary, hand-set quality rather than a SaaS marketing shout. Tight -0.02em letter-spacing at 69px tightens the large headline to a single confident line. Substitute: 'Sohne Breit', 'GT America', or 'Inter' at weight 500
- ui-sans-serif `--font-ui-sans-serif` for System sans-serif for all functional text - body copy at 400/16px, UI labels and button text at 500, emphasized sub-labels at 600. The neutral system face keeps the interface quiet so the Rules Font headlines carry all the personality. Substitute: 'Inter', 'Sohne', or 'Geist'

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 24-32px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Navigation Bar: Top-level site navigation
- Pill Toggle (Talent/Employers): Audience switcher
- Ghost Button (Sign in): Low-emphasis action
- Filled Dark Button (Find work / Read more): Primary action
- Hero Search Input: Primary discovery input
- Secondary Text Link (I'm not sure): Tertiary action
- Hero Display Headline: Page-level headline
- Feature Card: Product capability showcase
- Product UI Mockup (embedded in cards): In-context product preview
- Full-Bleed Image Card: Cinematic content section
- 3D Brand Mark (Large P Logo): Brand identity element
- Live Status Indicator (23,237 new jobs): Real-time data signal

Do:

- Use Cream Paper (#e4dfd9) as the default page background for all non-photography sections - never switch to pure gray or pure white canvas
- Apply Rules Font weight 500 at 28px or 69px for all headlines, with -0.02em letter-spacing - never use weight 600+ or bold variants
- Set card border-radius to 20px for all card surfaces, and 8px for standard buttons, 12px for inputs, 9999px for pill toggles and tag chips
- Use the single Ember Dot (#ff6a1f) accent for live-status indicators, the period after hero headlines, and match-score badges - never apply it to large fills, backgrounds, or button states
- Set card padding to 32px on all feature cards and product surfaces
- Use Pressed Graphite (#171717) as the filled button background with white text for primary actions
- Maintain section gaps of 24-32px and element gaps of 8px to preserve the comfortable, editorial breathing rhythm

Avoid:

- Don't introduce additional chromatic colors - the system is intentionally monochrome with one ember accent; adding blues, greens, or other hues breaks the editorial discipline
- Don't use bold (700+) or heavy weights for headlines - the Rules Font at weight 500 is the signature restraint
- Don't apply drop shadows beyond the single soft pattern rgba(0,0,0,0.07) 0px 6px 27px - avoid colored, multi-layer, or hard shadows
- Don't use pure black (#000000) as a filled button background when Pressed Graphite (#171717) is available - the slight warmth matters
- Don't set border-radius to 4px or 0px on cards or buttons - the 8-20px range is the system's tactile signature
- Don't use more than one chromatic element per viewport - the Ember Dot should feel like punctuation, not decoration
- Don't apply the 69px display size to subheadings or body text - reserve it for hero-level headlines only

Source prompt cues:

**Quick Color Reference:**
- Text: #000000 (primary) / #737373 (secondary) / #999694 (muted)
- Background: #e4dfd9 (cream canvas) / #ffffff (card surfaces)
- Border: #c7c7c7 (hairline) / #737373 (visible)
- Accent: #ff6a1f (ember dot - status indicators only)
- primary action: no distinct CTA color

**Example Component Prompts:**

1. Create a feature card: white background (#ffffff), 20px border-radius, 32px padding, subtle shadow rgba(0,0,0,0.07) 0px 6px 27px. Top section contains a mini product UI mockup (mini search bar with white surface, 12px radius). Heading 'Hyper personal matches' in Rules Font weight 500 at 23px, #000000, letter-spacing -0.46px. Body text 'No fake jobs, just fresh direct roles from company sites, tailored to you.' in system sans-serif at 16px weight 400, #737373.

2. Create a hero section: full-bleed dark photography background with warm amber lighting, text centered. Headline 'Find your life's work' in Rules Font weight 500 at 69px, white (#ffffff), letter-spacing -1.38px, followed by an Ember Dot (#ff6a1f) as a period. Subtext in system sans-serif at 19px weight 400, white at 90% opacity. Search input: white background, 12px radius, 24px padding, placeholder 'What are you looking for?' in #999694, with a 40px circular dark arrow button on the right.

3. Create a pill toggle: segmented control with 12px border-radius, cream background (#e4dfd9), active tab is white with shadow rgba(0,0,0,0.07) 0px 6px 27px. Labels 'Talent' and 'Employers' in system sans-serif at 14px weight 500, #000000. 18px horizontal padding, 10px vertical padding per segment, 2px gap between segments.

4. Create a full-bleed image card: edge-to-edge photograph with 20px border-radius, dark scrim overlay (#171717 at 40% opacity), centered button at bottom - 'Start Matching' in Pressed Graphite (#171717) background, white text, 8px radius, 18px horizontal padding.

5. Create a job tag chip: pill shape with 9999px radius, white background, 1px border in #c7c7c7, 10px vertical padding, 16px horizontal padding, text in system sans-serif at 14px weight 500, #000000.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
