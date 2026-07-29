# AI Implementation Prompt

Build a UY Studio-inspired interface using this source-derived style bundle.

Reference site: https://www.uy-studio.com
Theme: light
Category: E-commerce
North star: Monastic stone gallery a quiet concrete-walled space where perfume bottles sit on white plinths, lit by one weight-400 voice and four warm grays.

Use these palette anchors:

- Soot `#24241f` for Primary text, all icon strokes, hairline borders, nav links, footer text the single dark voice of the system
- Limestone `#d1d3cf` for Page canvas, announcement bar, nav background the warm-tinted near-gray that replaces white as the system's base tone
- Chalk `#e5e5e5` for Secondary surface, subtle borders, product photo backgrounds a slightly cooler neutral for layering atop Limestone
- Graphite `#333333` for Dark button fill the only filled surface in the system, used sparingly for a single tonal shift from the Soot text

Use these typography anchors:

- GP Universal typeface used for nav, body, headings, buttons, and footer at weight 400 only. The single-weight constraint is the signature: no bold, no light, no medium. Hierarchy comes from size (1348px) and tracking (0.0110em body, 0.0390em display), not weight contrast. The slight positive tracking gives the type an editorial, architectural quality. `--font-gp`
- GTStandard-M GTStandard-M detected in extracted data but not described by AI `--font-gtstandard-m`

Use these layout rules:

- Base spacing: source-defined.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page brand message strip
- Main Navigation: Primary site navigation
- Hero Image with Overlay Text: Full-bleed editorial banner
- Product Card: Individual product listing in the grid
- Product Grid: 5-column product listing
- Newsletter Input: Email signup field
- Footer Link Column: Footer navigation links
- Language Toggle: Language selector

Do:

- Use GP at weight 400 for ALL text from 13px footer notes to 48px display lines. No bold, no semibold, no light variants exist in this system.
- Use Limestone (#d1d3cf) as the page background for every screen. Never substitute pure white (#ffffff) the warm gray tint is the system's identity.
- Use Soot (#24241f) for all text, icon strokes, and 1px borders. The warm-tinted near-black replaces standard #000 and ties the type to the concrete textures in the photography.
- Apply 0.0390em letter-spacing to display sizes (30px+) and 0.0110em to body sizes (1316px). The dual-tracking system is how hierarchy is expressed in a single-weight world.
- Use 0px border-radius on all cards, images, and containers. 3px radius is reserved exclusively for text inputs. Sharp edges reinforce the architectural, gallery-like feel.
- Present products as full-bleed photography on Chalk (#e5e5e5) surfaces with no card borders or shadows. The photograph IS the card.
- Use text links with underlines as the primary interaction pattern. Filled buttons in Graphite (#333333) are reserved for single-purpose dark actions and should appear at most once...

Avoid:

- Don't introduce bold, semibold, or light font weights. Weight 400 is the only voice adding weight would break the flat, even texture that defines the system.
- Don't add saturated colors, brand hues, or accent fills. The palette is four warm grays only any chromatic color would shatter the monastic quality.
- Don't use box-shadow or drop-shadow for elevation. Depth comes from the warm-gray surface stack (Limestone Chalk Graphite Soot), not from shadows.
- Don't round corners on cards, images, or containers. 0px everywhere except inputs. Rounded corners would soften the architectural, museum-pedestal feel.
- Don't use color or weight to indicate interactive states. Use Soot underlines on hover, position shifts on active, and the underline-on-current pattern for navigation state.
- Don't add decorative gradients, patterns, background textures, or ornamental graphics. The only imagery is product photography against real textures.
- Don't use filled, colored, or rounded icon buttons. Icons are stroke-only in Soot, inline with text at the same baseline. The interface is text-first.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
