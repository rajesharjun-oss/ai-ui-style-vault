# AI Implementation Prompt

Build a Fidele Editions-inspired interface using this source-derived style bundle.

Reference site: https://fidele-editions.com
Theme: light
Category: E-commerce
North star: Risograph blue ink on warm cream paper. A single fluorescent blue floods headlines, the announcement bar, and a giant asterisk logo, stamped onto a flat cream stock with zero shadows and near-zero rounding - the page reads as a printed broadsheet, not a SaaS interface.

Use these palette anchors:

- Fidele Blue `#1664eb` for Headlines, nav links, brand asterisk, announcement bar fill, body borders - the single chromatic ink of the system; whenever color appears, this is it
- Lighter Press Blue `#4f89ec` for Secondary blue used for subtle borders, icon tints, and decorative strokes where Fidele Blue would dominate
- Link Blue `#006ce5` for Deeper blue for inline hyperlinks within running text, slightly darker than the primary to read as a separate interactive state
- Paper White `#f8f7ef` for Page canvas and card surfaces - a warm off-white that gives the entire system its print-stock identity; never use pure #ffffff for page background
- Card Cream `#e2e2df` for Elevated surface for cards, panels, and product tiles - one step warmer/darker than Paper White for layering without shadows
- Pure White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Press Black `#121212` for Body text, dark backgrounds, and the rare filled button - near-black rather than pure black, softening contrast on the cream stock

Use these typography anchors:

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- BaselGrotesk `--font-baselgrotesk` for The sole typeface of the system. Book weight (400) for body and most UI; Regular (400) for lists and some headings; Bold (700) for the rarest emphasis. Display sizes (62px) use line-height 0.92 with -0.049em tracking - characters nearly touch. Small labels (14px) use +0.063em tracking - wide, airy, stamped. The contrast between these two tracking regimes is the type signature.
- OTMagister `--font-otmagister` for Occasional display headlines where a more editorial/serif-leaning voice is wanted. Same 62px display size and tight 0.92 leading as BaselGrotesk display, -0.016em tracking.
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI
- Assistant `--font-assistant` for Assistant - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 64px.
- Card padding: 16px.
- Element gap: 5px.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page promotional strip
- Top Navigation Bar: Primary site navigation
- Hero Image Block: Full-bleed editorial photograph
- Product Card: Grid tile for a book, zine, t-shirt, or blanket
- Product Grid: Shop 'What's on: Latest' listing
- Outlined Action Button: Primary interactive control
- Photo Strip Section: Full-bleed editorial image band
- Split Feature Section: Two-column image+content block
- Giant Asterisk Mark: Brand signature / decorative element
- Product Detail Link: Title link under a product image
- Language Selector: Top-bar utility
- Icon Button (Search/Cart): Top-bar utility

Do:

- Use #f8f7ef as the page canvas on every screen - never substitute #ffffff for the base background.
- Set display type (62px) with line-height 0.92 and letter-spacing -0.049em; characters must nearly touch to feel printed, not rendered.
- Set body and label type (14-16px) with tracking +0.043em to +0.067em - the wide tracking is half the editorial voice.
- Reserve Fidele Blue (#1664eb) for type, the announcement bar, nav links, the asterisk, and outlined actions - one ink, used with volume.
- Keep all corner radii at 0-4px; the page should read as cut paper, not as rounded UI cards.
- Let the product grid float on Paper White without card backgrounds; the 1px white border around each product image is the only frame.
- Use full-bleed image sections (photo strips, hero) with no rounding, no overlay, no caption - let the photography do the work.

Avoid:

- Don't introduce drop shadows, inner shadows, or glow effects - the system is deliberately flat and reads as paper, not glass.
- Don't use any chromatic color other than Fidele Blue, Lighter Press Blue, and Link Blue - the cream + blue duotone is the entire palette.
- Don't use filled solid-color buttons for primary actions; the system's primary control is the outlined Fidele Blue action.
- Don't set display type with generous line-height (1.2-1.5) - the crushed 0.92 leading is a signature, not a default.
- Don't round cards, images, or tags beyond 4px; anything rounder breaks the print-stock metaphor.
- Don't add gradients, textures, or noise - surfaces are flat solids, period.
- Don't use #ffffff as a page background; it must remain the warm Paper White #f8f7ef to keep the editorial warmth.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
