# AI Implementation Prompt

Build a Sana Agents-inspired interface using this source-derived style bundle.

Reference site: https://sana.ai
Theme: light
Category: AI
North star: Lime spark on editorial white

Use these palette anchors:

- Ink Black `#0a1217` for Primary text, dark card surfaces, sign-up panel, filled primary buttons on light backgrounds
- Paper White `#ffffff` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Frost Wash `#e4eff7` for Soft tinted surface for light product cards and secondary panels the only chromatic step between paper white and ink black
- Stone Gray `#85898b` for Muted helper text, footer labels, and desaturated secondary copy
- Obsidian `#000000` for Hairline borders, nav text, and input outlines where the sharpest contrast edge is required
- Electric Lime `#cdfe00` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color

Use these typography anchors:

- Sana Serif Hero display headline only. A weight-400 serif at 72px is the system's signature move: most AI brands shout with bold sans, Sana whispers with editorial type and lets the scale carry authority. The serif counterforms and bracket serifs give the wordmark a literary, humanist quality absent from typical product UI. `--font-sana-serif`
- Sana Sans All UI, body, navigation, buttons, and subheadings. The 450 weight is a distinctive mid-step between regular and medium used for button labels and nav links instead of jumping to 500, producing quieter emphasis. Tabular numerals (tnum) and lining figures (lnum) are always on, giving all numeric data a consistent grid. `--font-sana-sans`

Use these layout rules:

- Base spacing: source-defined.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Hero Headline (Sana Serif Display): The 72px serif display that opens the page
- Product Card Dark (Sana Agents): Full-bleed dark product showcase card
- Product Card Light (Sana Learn): Full-bleed light product showcase card
- Pill Button Filled Dark: Primary action on light backgrounds
- Pill Button Accent Lime: Highlighted action on dark surfaces
- Pill Button Ghost/White: Secondary action on dark surfaces, or outlined action on light surfaces
- OAuth Button (Google): Third-party authentication action
- Sign-Up CTA Card: Conversion panel for account creation

Do:

- Use Sana Serif exclusively for the 72px hero headline at weight 400 it is the system's only serif, and diluting it to smaller sizes destroys its editorial authority
- Apply 24px border-radius to all cards, inputs, and panel containers; use 9999px exclusively for pill-shaped buttons and tags
- Restrict #cdfe00 (Electric Lime) to filled action buttons sitting on #0a1217 (Ink Black) surfaces the lime-on-ink contrast is the entire purpose of the accent
- Use Sana Sans weight 450 for button labels and nav links rather than 500 the 450 step is what makes the body type feel quiet and considered
- Set font-feature-settings to "lnum" on, "tnum" on for all Sana Sans usage tabular numerals ensure numeric data aligns cleanly in tables, prices, and timestamps
- Create depth through surface color shifts (white frost ink) rather than box-shadows the system is flat by design
- Keep the hero headline centered and the rest of the layout left-aligned centering is reserved for the single editorial moment

Avoid:

- Do not use Sana Serif below 56px weight 400 at small sizes loses its authority and reads as thin/generic
- Do not place #cdfe00 on #ffffff or #e4eff7 surfaces the contrast is insufficient and the lime loses its electric quality
- Do not introduce a second accent color the system is monochromatic with exactly one chromatic note, adding more dilutes the poster-like discipline
- Do not apply drop shadows to cards or panels depth comes from the white frost ink surface stack, not elevation
- Do not use sharp corners (0px radius) on any container the 24px radius defines the system's soft, tactile personality
- Do not center-align body text, card content, or navigation links only the hero display headline gets centered treatment
- Do not add gradients, patterns, or background imagery to surfaces the design language is pure flat color blocks

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
