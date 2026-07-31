# AI Implementation Prompt

Build a Incident-inspired interface using this source-derived style bundle.

Reference site: https://incident.io
Theme: light
Category: Dev Tools
North star: Technical broadsheet on concrete. Times-serif headlines float on a warm-gray page with hairline black rules and a single orange flare that breaks the calm like a signal beacon.

Use these palette anchors:

- Signal Orange `#f25533` for Brand accent, logo mark, decorative SVG fills, nav emphasis - the single warm chromatic note that cuts through the monochrome system
- Concrete `#efefef` for Page canvas, button background - the dominant surface tone that gives the system its paper-like warmth
- Ink `#000000` for Primary text, hairline borders (920+ uses), button outlines - pure black carries all structural line work
- Paper `#ffffff` for Card surfaces, nav fills - the white layer that sits on top of the concrete canvas
- Carbon `#161618` for Near-black for nav strokes, emphasis text, and the tinted shadow base - softer than pure ink for layered elements
- Mist `#dadada` for Subtle drop-shadow tone, decorative image edge tint
- Fog `#cccccc` for Secondary shadow tone, decorative image edge tint
- Parchment `#e4d9c8` for Warm cream decorative surface - near-gray but carries a beige cast that ties to the orange family
- Alert Red `#ff492c` for Orange decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color
- Ember `#f1641e` for Orange outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color

Use these typography anchors:

- Times (system serif) `--font-times-system-serif` for Body text, headings, nav items, hero copy, card content, list items, footer - Times carries 770+ uses and is the signature typographic choice. A serif body face on a B2B incident-management product is anti-convention: it borrows the authority of a legal broadsheet or technical manual, replacing the usual Inter/system-ui with something that reads as deliberately editorial. Weight 400 for body, 700 for emphasis and headings.
- Arial (system sans) `--font-arial-system-sans` for Small UI micro-text: button labels, nav utility text, icon-adjacent labels. Arial at 13px handles the functional labels while Times carries the voice - a deliberate serif/sans split where Times says something and Arial just tags it.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Navigation Bar: Top-level site navigation
- Neutral Button: Primary interactive action
- Critical Alert Banner: Outage or incident status display
- Warning Alert Banner: Degraded service or maintenance notice
- Status Tag / Pill: Component-level status indicator (e.g. Website, App)
- Status Card: Container for a single incident report
- Section Heading (Serif): Page and section titles
- Text Link: Inline navigation to subpages or external resources
- File-Type Illustration: Decorative graphic for file format references
- Product Feature Card: Text-first card describing a product capability

Do:

- Use Times (or Source Serif Pro as substitute) for all body copy, headings, nav items, and hero text - the serif face is the brand voice
- Set the page canvas to #efefef (Concrete) and let cards sit in #ffffff (Paper) above it - never invert to a white page with gray cards
- Use #000000 for all structural borders and hairline rules - borderColor is the dominant role of pure black in this system
- Use Signal Orange (#f25533) only for brand marks, logo elements, decorative fills, and file-type illustrations - never for action buttons or functional UI
- Set button background to #efefef with a 1px black border, 4px radius, and 1px/6px padding - buttons should feel like labeled frames, not filled actions
- Keep the type scale tight: 13px (Arial micro-labels), 16px (Times body), 19px (Times body-lg), 24px (Times heading-sm), 32px (Times heading) - do not introduce sizes outside this range
- Use status-tinted card borders (red for critical, amber for warning) to communicate severity - the border color does the semantic work, not a colored background fill

Avoid:

- Do not use sans-serif (Inter, system-ui) for body copy or headings - replacing Times breaks the editorial identity
- Do not add colored button fills (blue, orange, green) for primary actions - the system uses neutral concrete buttons with black borders
- Do not use gradients - no gradient was detected in the source and the flat editorial aesthetic rejects them
- Do not use heavy drop-shadows for elevation - shadows are reserved for image containers at 2-4% opacity only
- Do not introduce blue or green as brand or accent colors - the chromatic palette is exclusively warm (orange family and amber)
- Do not round buttons beyond 4px or use pill shapes - the slightly squared button geometry reinforces the broadsheet feel
- Do not use color to indicate active or selected states - rely on weight (400 700) and underline affordances within the serif system

Source prompt cues:

Quick Color Reference:
- Text: #000000 (Ink) for body, #161618 (Carbon) for emphasis
- Background: #efefef (Concrete) page canvas, #ffffff (Paper) cards
- Border: #000000 (Ink) for all structural hairlines
- Accent: #f25533 (Signal Orange) for brand marks and decorative fills only
- Status critical: #ff492c (Alert Red)
- Status warning: #f1641e (Ember)
- primary action: no distinct CTA color

3-5 Example Component Prompts:

1. Create a critical alert banner: soft red-pink wash background, Alert Red (#ff492c) warning triangle icon on the left. Headline 'Service disruption detected' in Times 16px weight 700, #000000. Body text in Times 16px weight 400, #000000. Full-width with 8px border-radius, sitting on a white card with a light red border.

2. Create a neutral button: #efefef background, 1px solid #000000 border, 4px border-radius, padding 1px top/bottom and 6px left/right. Label 'Get started' in Arial 13px weight 400, #000000. No shadow, no fill change on hover.

3. Create a page section heading: 'On-call gets the right people in the room' in Times 32px weight 700, #000000, on a #efefef page canvas. Below it, a body paragraph in Times 16px weight 400 at 19px line-height. No decorative elements, no underline, no accent color.

4. Create a status card: white (#ffffff) background, 12px border-radius, light amber-tinted (#f1641e at low opacity) 1px border. 24px internal padding. Contains a warning triangle icon in Ember (#f1641e), a Times 16px weight 700 headline, and a Times 16px weight 400 description.

5. Create a file-type illustration: a document shape with a folded top-right corner, filled in Signal Orange (#f25533), with 'PNG' in white Arial bold 32px centered. Flat - no shadow, no border, no gradient. Sits on the #efefef page canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
