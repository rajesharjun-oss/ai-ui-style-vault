# AI Implementation Prompt

Build a North Kingdom-inspired interface using this source-derived style bundle.

Reference site: https://www.northkingdom.com
Theme: dark
Category: Agency
North star: cinematic void with luminous type - a black film-studio soundstage where a single wordmark glows

Use these palette anchors:

- Void Ink `#050311` for Page canvas, section backgrounds, dark surface base - the near-black stage on which all content sits, carrying a barely-perceptible cool-violet undertone that keeps it from feeling clinical
- Pure White `#ffffff` for Primary text, headline color, hairline borders, icon strokes, button outlines - the only high-contrast voice in the system; when something needs to be seen, it is white
- Carbon Black `#000000` for Monochrome icon fills, brand marks, and high-contrast graphic details. Do not promote it to the primary CTA color
- Ash Gray `#9b9aa0` for Muted body text, secondary headings, subtle borders, disabled states - carries all secondary information without competing with the white voice
- Graphite `#44424d` for Dividers, low-emphasis borders, hairline separators between sections - quiet structural lines that organize the dark canvas without drawing attention

Use these typography anchors:

- FKGroteskNeue `--font-fkgroteskneue` for Universal type family - used for navigation, body, headings, badges, buttons, cards, and the massive hero wordmark. A neo-grotesque sans with tabular numerals as a deliberate feature. The single weight (400) is the system's signature: the hero 'North Kingdom' wordmark achieves its cinematic weight through sheer size, not font weight. Substitute: Space Grotesk or Inter at matching weight.
- Arial `--font-arial` for System fallback for button labels, icons, and input fields - used where the custom font license or loading constraints prevent the primary face from rendering

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Hero Wordmark Display: Primary brand expression - full-viewport typographic statement
- 3D Brand Emblem Card: Central brand icon - visual anchor within the hero wordmark
- Top Navigation Bar: Site navigation - minimal, non-competing
- Image Card: Project thumbnail / work showcase tile
- Outlined Button: Primary interactive element
- Pill Input Field: Form input - newsletter, contact, search
- Full-Pill Badge / Tag: Category labels, filters, metadata chips
- Play Button Overlay: Video trigger - appears on hero emblem and video thumbnails
- Section Divider: Structural separator between content bands
- Footer Block: Site footer - contact, social, legal
- Grid Project Layout: Work portfolio grid - the 'Work' page pattern

Do:

- Set all body text and headings in FKGroteskNeue weight 400 - the single weight is the system's voice; never introduce bold or light variants
- Use #050311 as the page canvas for every full-width background; let sections flow as uninterrupted bands of void
- Apply 8px border-radius to all image containers and project cards; use 4px for buttons; reserve 26px exclusively for input fields
- Let white (#ffffff) carry all primary information: text, borders, icons, button outlines - it is the only voice that speaks loudly
- Use #9b9aa0 for secondary text and muted borders; it should never compete with white for attention
- Let the hero wordmark be enormous - typographic scale is the design system, not color or imagery
- Include "tnum" font-feature-settings on all FKGroteskNeune usage to preserve tabular numeral alignment

Avoid:

- Never introduce a chromatic brand color - the system is monochrome; color appears only inside the 3D emblem artwork
- Never use drop shadows, glows, or blur effects - depth comes from value contrast, not elevation
- Never use border-radius above 8px on cards or images - the 26px and 100px values are reserved for inputs and pills only
- Never use more than one font weight - the system speaks in a single 400 voice at varying sizes
- Never place white text on white surfaces or dark text on the void without testing contrast - the system depends on absolute clarity between two values
- Never use gradients on backgrounds - the canvas is a solid void; gradients were not detected in the system
- Never add decorative borders or ornamental elements - the aesthetic is architectural minimalism, not illustration

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
