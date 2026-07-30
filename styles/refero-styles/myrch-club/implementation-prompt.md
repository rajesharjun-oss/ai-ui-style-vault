# AI Implementation Prompt

Build a Myrch Club-inspired interface using this source-derived style bundle.

Reference site: https://www.myrch.club
Theme: light
Category: Media
North star: white-walled exhibition vitrine - editorial serif labels floating in generous negative space, disrupted by a single red script signature

Use these palette anchors:

- Canvas White `#ffffff` for Page background, image surfaces, inverted text on dark chips
- Gallery Gray `#f9f9f9` for Card and product tile backgrounds - sets objects apart from the page with a whisper of warmth
- Hairline Gray `#cfcfcf` for Dividers, secondary borders, placeholder structure
- Caption Gray `#888888` for Secondary text, metadata, timestamps, muted helper labels
- Ink Black `#111111` for Primary text, filled filter chips, button borders, headings - the dominant interface color
- True Black `#000000` for Hard borders and text where maximum contrast is needed
- Signature Red `#ff0000` for The wordmark only - a pure, unmoderated red used at oversized scale behind the header as a brand watermark; never used for buttons, links, or functional UI

Use these typography anchors:

- Times New Roman `--font-times-new-roman` for Primary body and interface type - used for descriptions, product metadata, and general reading text. The serif choice signals editorial/archive intent; a humanist serif substitute like EB Garamond or Lora preserves the curatorial atmosphere
- Arial Narrow `--font-arial-narrow` for Secondary structural type - condensed sans for compact labels, filter chips, navigation, and the 42px brand name in the header. The narrow proportions contrast the serif body and create catalog/inventory utility. Substitute with a condensed grotesk like Barlow Condensed or Roboto Condensed

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1280px.
- Section gap: 40px.
- Card padding: 30px.
- Element gap: 20px.

Build these component patterns where relevant:

- Header Brand Lockup: Site identity in the top-left
- Red Script Watermark: Brand signature bleeding behind the header
- Description Block: Introductory paragraph beneath the brand
- Filter Chip - Active: Currently selected category filter
- Filter Chip - Inactive: Unselected category filter
- Curatorial Caption: Tiny attribution line under the chips
- Product Grid Card: Individual merch item tile
- Product Image Frame: Photograph container within a card
- Card Label Row: Metadata strip beneath each product image
- Instagram Icon Button: Social link in the top-right corner

Do:

- Set all product tiles on a #f9f9f9 gallery card with 10px radius and 30px internal padding.
- Use Times 16px weight 400 for all body and description copy; use Arial Narrow 14px for labels, chips, and metadata.
- Reserve #ff0000 exclusively for the oversized script wordmark behind the header; treat it as a signature artwork, not a functional color.
- Use #111111 as the dominant interface color for text, filled chips, and borders - keep the palette strictly black-on-white for everything else.
- Use 10px border-radius for all chips, buttons, and cards as a single consistent rhythm.
- Separate content with hairline #cfcfcf borders and color shifts rather than drop shadows.
- Allow generous whitespace - section gaps of 40px and card padding of 30px - to preserve the gallery/archive feel.

Avoid:

- Do not use #ff0000 for buttons, links, tags, error states, or any functional UI element.
- Do not introduce additional accent colors - the system is strictly monochrome with one red artwork exception.
- Do not use heavy or stacked shadows; the single 20px 30%-opacity blur is the maximum elevation allowed.
- Do not use bold or display-weight typography; both Times and Arial Narrow appear at weight 400 only.
- Do not fill buttons with chromatic colors - buttons should be #111111 fill on #ffffff or outlined #111111.
- Do not use rounded or pill shapes (9999px radius) - the 10px radius is deliberate and consistent.
- Do not add gradients, glows, or colored backgrounds to the product cards.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
