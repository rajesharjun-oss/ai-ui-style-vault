# AI Implementation Prompt

Build a Zelt-inspired interface using this source-derived style bundle.

Reference site: https://zelt.app
Theme: light
Category: SaaS
North star: Amber on raw linen - the single honey accent glows against warm cream and near-black ink, as if sunlight fell across a paper spread.

Use these palette anchors:

- Ink `#121718` for Primary text, icon strokes, hairline borders, default link text - near-black with a barely-warm cast that harmonizes with the cream canvas rather than fighting it
- Paper `#ffffff` for Elevated card surfaces, button text on amber, icon fills - the brightest stop in the stack, used sparingly to lift content above the cream canvas
- Linen `#f6f3ef` for Card backgrounds, soft surface fill, inset panels - the warm off-white that sits one step above the page canvas
- Parchment `#e4e0dd` for Page canvas, outer body background - the warm light gray that gives the entire interface its sunlit quality
- Graphite `#2f2f2f` for Dark surface fill for inverted cards, footer band, contrast blocks - darker than Ink so it reads as a deliberate charcoal panel
- Slate `#444444` for Secondary neutral action background, muted utility surfaces - sits between Ink and the canvas for low-emphasis interactive fills
- Honey `#ffcd6d` for Primary action fill for the demo and get-started buttons, key brand moments - the single saturated color in the system, reserved for decisions that move the user forward
- Apricot `#ffe2aa` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

Use these typography anchors:

- sans-serif (system) `--font-sans-serif-system` for Full type system - weight 500/700 at 76-101px with tracking as tight as -0.043em gives headlines a quiet authority without resorting to a serif; weight 400 at 16-18px handles body; the huge size range (8px 101px) is editorial in proportion, not product-UI proportions

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24-32px.
- Element gap: 12-16px.

Build these component patterns where relevant:

- Primary Action Button: Highest-emphasis call-to-action across the marketing site
- Secondary Ghost Button: Lower-emphasis action or link-style button
- Pill Tag / Badge: Status pill and category labels
- Top Notification Bar: Site-wide announcement strip across the top of every page
- Floating Navigation Bar: Primary site navigation
- Nav Link: Individual navigation item
- Hero Headline Block: Above-the-fold primary message
- Card Surface (Light): Content container for features, pricing tiers, and grouped information
- Card Surface (Dark): Inverted card for contrast sections and the footer
- Scroll Indicator: Floating affordance hinting at more content below the fold
- Icon: All UI iconography throughout the system
- Close / Dismiss Icon: Remove affordance for banners, modals, toasts

Do:

- Use Honey (#ffcd6d) for exactly one element per viewport - the primary action - and nothing else.
- Set all interactive surfaces (buttons, nav, tags, cards) to a 12px border-radius; the pill silhouette is the system signature.
- Pair weight 500/700 with sizes 58px and above, and apply tracking as tight as -0.043em - the headlines earn their weight through restraint, not volume.
- Keep page canvas at Parchment (#e4e0dd) and lift content with White or Linen cards using 1px Ink hairline borders at low opacity; never use drop shadows for elevation.
- Center hero blocks with a single 76-86px headline, an 18px subtitle, and a single Honey button - no hero imagery competes with the type.
- Use Apricot (#ffe2aa) for ambient warmth (notification bar, soft tags) and Honey (#ffcd6d) only for action - the two ambers have distinct jobs.
- Maintain 80px section gaps and let the cream canvas breathe; the spaciousness is the brand as much as the color is.

Avoid:

- Don't introduce a second saturated color - the system is monochrome warm with one amber accent, and any second hue breaks the spell.
- Don't apply drop shadows to cards, buttons, or nav - delineation is done with hairline 1px borders and surface fill alone.
- Don't set headlines below weight 500 at display sizes; the tight tracking only reads as confident when paired with sufficient weight.
- Don't round corners below 8px on interactive elements and below 12px on cards/buttons - sharp corners fight the pill-shaped language.
- Don't use blue, purple, or any cool hue for links, icons, or accents; all chromatic energy comes from the warm amber family.
- Don't fill large surfaces with Honey - the accent loses its meaning when it covers anything bigger than a button.
- Don't set body text below 16px or above 18px - the system is editorial in proportion, not dense data-UI proportions.

Source prompt cues:

Quick Color Reference:
 text: #121718 (Ink)
 background: #e4e0dd (Parchment canvas)
 card surface: #ffffff (Paper) or #f6f3ef (Linen)
 border: #121718 at ~8% opacity (1px hairline)
 accent: #ffcd6d (Honey) / #ffe2aa (Apricot)
 primary action: no distinct CTA color

Example Component Prompts:

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. Floating nav: White (#ffffff) surface, 12px radius, 1px #121718 border at 8% opacity, 60px tall, centered horizontally, no shadow. Logo text 'zelt' at 18px weight 700 in #121718 on the left. Nav links at 15px weight 400 in #121718 centered. Primary 'See demo' button on the right: #ffcd6d fill, #121718 text, 12px radius, 8px 20px padding.

3. Feature card: White (#ffffff) background, 12px radius, 1px #121718 border at 8% opacity, 32px padding. Heading at 24px weight 500, #121718, letter-spacing -0.17px. Body text at 16px weight 400, #121718, 16px top margin.

4. Top notification bar: Full-width #ffe2aa band, 44px tall, centered content. Left side: small pill tag with #ffe2aa fill (slightly darker), #121718 text at 13px weight 500, 4px 12px padding, 12px radius. Center: announcement text at 14px weight 400 in #121718. Right: 16px X icon in #121718.

5. Dark contrast section: #2f2f2f background, full-width band, 80px vertical padding. White (#ffffff) text, display headline at 58px weight 500 with letter-spacing -1.45px. Content centered, max-width 1200px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
