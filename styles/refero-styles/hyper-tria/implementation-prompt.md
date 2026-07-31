# AI Implementation Prompt

Build a Hyper Tria-inspired interface using this source-derived style bundle.

Reference site: https://hypertria.com
Theme: mixed
Category: Agency
North star: chrome monolith in a white gallery

Use these palette anchors:

- Ember Red `#ee3a49` for Wordmark, navigation text, kicker labels, and the single chromatic accent that makes the otherwise monochrome system read as a brand. The warmth against pure black and white creates editorial urgency without tipping into alarm
- Hyper Green `#0fa64b` for Reserved for the rotating circular brand badge and high-prominence brand moments. A single saturated spot of color in an otherwise achromatic system - used sparingly so it lands as identity, not decoration
- Signal Blue `#007bff` for Outlined/ghost action border, image frame accent, and link underline. Functions as the system's cool counterweight to the warm Ember Red - used for bordered interactive elements rather than filled buttons
- Obsidian `#000000` for Page canvas in the hero, primary text color in light sections, and the dominant border color across all UI elements. Carries the heaviest weight in the system - defines edges, type, and spatial structure
- Paper `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Graphite `#666666` for Secondary navigation text and border color for tertiary UI elements. The middle tone that prevents the black/white binary from feeling stark in repetitive nav and list contexts

Use these typography anchors:

- Aeonik `--font-aeonik` for Primary typeface for all display, heading, and body text. Weight 300 at 75-90px with line-heights near 0.90-1.00 creates the system's signature sculptural headlines - letterforms lock together through aggressive negative tracking (-0.053em) rather than spacing. Mid-weight 400-500 handles body and UI at 19-20px with 1.45-1.70 line-height for generous readability.
- -apple-system `--font-apple-system` for System fallback for nav items, footer micro-copy, and supporting UI text where the custom Aeonik isn't loaded. Carries no distinctive role - purely a graceful degradation layer.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1400px.
- Section gap: 100px.
- Card padding: 25-28px.
- Element gap: 10-20px.

Build these component patterns where relevant:

- Dark Hero Stage: Full-bleed black canvas hosting the agency's signature 3D metallic wordmark
- Light Editorial Section: White-background work showcase with alternating image+text layout
- Light Navigation Bar: Sticky top navigation for content sections
- Dark Navigation Bar: Navigation variant for the black hero stage
- Outlined Arrow Link: Primary project-level call-to-action
- Rotating Circular Brand Badge: Persistent brand identifier across the hero and footer
- Kicker Label: Project category or section identifier above headlines
- Image Frame: Product/project photography container
- Section Divider: Implicit separator between light and dark sections

Do:

- Use Aeonik weight 300 at 75-90px with line-height 0.90-1.00 and letter-spacing -4px to -5px for all display headlines
- Maintain 100px vertical gaps between major sections to preserve the gallery's breathing rhythm
- Set border-radius to 0px on all cards, buttons, tags, inputs, and image containers
- Use Ember Red (#ee3a49) exclusively for the wordmark, navigation text, and kicker labels - never as a background fill
- Transition between black (#000000) and white (#ffffff) section backgrounds as the primary spatial separator instead of rules or shadows
- Keep body text at 19px Aeonik weight 400 with line-height 1.48 and slight positive tracking (0.19px) for editorial readability
- Render the hero wordmark as a 3D metallic/chrome treatment when possible - the reflective surface is the system's most recognizable signature

Avoid:

- Never add border-radius to any element - the sharp-edged geometry is a defining system constraint
- Never use a filled button background as a CTA - the system signals actions through outlined/ghost borders or typographic arrows only
- Never use shadows or box-elevation for depth - rely on background color contrast and typographic scale instead
- Never apply Ember Red (#ee3a49) to large background fills - it is an accent color for text and small marks only
- Never set display headline letter-spacing to 0 or positive values - the aggressive negative tracking on large type is signature
- Never use multiple chromatic colors in the same view - the system is monochrome with single-color punctuation per section
- Never use illustrations, abstract graphics, or decorative imagery - product photography and 3D type are the only visual elements

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff (content) / #000000 (hero)
- border: #000000 (primary) / #666666 (secondary)
- accent (wordmark, nav, kicker): #ee3a49
- badge accent: #0fa64b
- primary action: #007bff (outlined action border)

**Example Component Prompts**

1. *Create a dark hero stage:* Full-bleed #000000 background. Render the wordmark 'Hyper Branding' in Aeonik weight 300 at 90px, line-height 0.90, letter-spacing -4.77px, as a 3D chrome/metallic treatment. Place a circular brand badge (~90px diameter, #ffffff fill, rotating black 'Hyper Branding' text around circumference, bold black 'H' monogram center, #0fa64b accent) in the lower-right quadrant. Add a white top nav with items separated by thin characters.

2. *Create a light editorial work section:* White #ffffff background, 100px padding top/bottom. Two-column layout constrained to 1400px max-width. Left column: product photograph (1:1 aspect, no border-radius, no shadow, clean studio background). Right column: kicker label 'Your Breakfast Box' in Aeonik 20px weight 400, #000000, 28px below it a headline 'AN OUT OF THE BOX CONCEPT' in Aeonik 35px weight 400, letter-spacing -0.7px, #000000. Below the headline at 44px: a thin black L-shaped arrow line (~50px wide, 2px stroke, no fill) as the project link.

3. *Create the light navigation bar:* White #ffffff background, no border. Left-aligned wordmark 'Hyper Branding' in #ee3a49, Aeonik 20px weight 400. Center: nav items ('Agency', 'Works', 'Contact') in #ee3a49, Aeonik 14px weight 400, 18px horizontal gap between items. Right-aligned: language toggle 'En/Gr' in #000000, Aeonik 14px weight 400.

4. *Create an outlined/ghost action link:* No background fill. 1px solid #007bff border. Zero border-radius. Aeonik 14px weight 500, #007bff text. Padding 8px 18px. Functions as a ghost/outlined interactive element, not a filled CTA.

5. *Create a rotating brand badge:* 90px diameter circle, #ffffff background. Inner ring: black #000000 text 'Hyper Branding' repeated, set in a circular path at 11px Aeonik weight 400. Center: bold 'H' monogram in Aeonik weight 500, 24px, #000000. Single #0fa64b green dot or accent mark as a visual signature element.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
