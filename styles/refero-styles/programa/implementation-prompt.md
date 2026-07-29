# AI Implementation Prompt

Build a Programa-inspired interface using this source-derived style bundle.

Reference site: https://programa.design
Theme: light
Category: Design
North star: Swiss design studio at high noon. A white gallery wall lit by a single yellow desk lamp everything is grayscale until a button, badge, or highlight demands attention, and then that one yellow note carries the whole room.

Use these palette anchors:

- Ink Black `#1a1a1a` for Primary text, all borders, icon strokes, logo, divider lines, button outlines the structural ink that defines every shape on the page
- Paper White `#ffffff` for Page canvas, card surfaces, text on dark fills, input fields
- Fog Gray `#f4f4f4` for Soft section background, alternate surface, and quiet card fill
- Ash Gray `#a3a3a3` for Muted secondary text, inactive links, placeholder copy, tertiary metadata
- Highlighter Yellow `#fbff2b` for Primary action background, focus highlights, tag fills the single chromatic accent that makes interactive elements feel switched on against the monochrome system

Use these typography anchors:

- Neue Haas Grotesk Text The single typeface carries every voice on the site nav, body, headings, buttons, inputs. Weight 400 is the default for body and nav; weight 500 is reserved for emphasized inline labels (e.g. 'Last Updated:') and section opens. The choice of a neo-grotesque with consistent -0.03em tracking at every size creates optical tightness even at 42px, avoiding the airy looseness most sans-serifs default to. This is a Swiss-tool typeface, not a personality typeface restraint is the signature. `--font-neue-haas-grotesk-text`
- neue-haas-grotesk-text neue-haas-grotesk-text detected in extracted data but not described by AI `--font-neue-haas-grotesk-text`

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Top Navigation Bar: Sticky-style header anchoring page identity and primary destinations
- Primary CTA Button: The single high-emphasis action on any screen
- Ghost Text Button: Secondary, low-emphasis action paired with the primary CTA
- Page Heading: Hero heading for content pages
- Info Banner: Metadata callout (e.g. 'Last Updated') below the page heading
- Numbered Section Block: Ordered content list with bold lead-in label
- Logo Lockup: Brand mark + wordmark for header and footer
- Form Input: Text entry field

Do:

- Use #fbff2b fill with 1px #1a1a1a border exclusively for the single primary action per screen never use the yellow as a background for large surfaces or decorative blocks.
- Set all text at -0.03em letter-spacing using the Neue Haas Grotesk Text scale (14/16/17/20/24/42px) do not introduce a second typeface or loosen tracking at display sizes.
- Apply 10px border-radius to buttons, nav elements, and inputs; reserve 16px for larger card surfaces and info banners.
- Build vertical rhythm on the 6px base unit: 8px between list items, 12px for element gaps, 16px for card padding, 48-96px for section separation.
- Use #f4f4f4 as the only mid-surface between white and the yellow accent never introduce additional gray tints or gradient washes.
- Keep page layout centered with a 1200px max-width and 111px left margin for content blocks; let white space carry the visual weight.
- Communicate hierarchy through weight (400 vs 500), not color or size variation the system has exactly two weights and a tight type scale.

Avoid:

- Don't introduce drop shadows, glow effects, or blur elevation is flat and border-defined.
- Don't use #fbff2b on more than one element per viewport its power comes from scarcity.
- Don't add a second accent color; the palette is monochrome + one yellow-green signal.
- Don't use Ash Gray (#a3a3a3) for body copy it's a 2.5:1 contrast fail on white; reserve it for placeholders and inactive metadata only.
- Don't increase border-radius above 16px the slightly squared geometry is part of the identity.
- Don't break the 6px spacing grid with arbitrary pixel values; every gap should be a multiple of 6.
- Don't add a subtitle or eyebrow text above page headings the 42px heading stands alone.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
