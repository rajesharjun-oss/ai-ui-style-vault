# AI Implementation Prompt

Build a Dribbble-inspired interface using this source-derived style bundle.

Reference site: https://dribbble.com
Theme: light
Category: Design
North star: gallery wall at design week a quiet white room where one magenta spotlight circles each piece

Use these palette anchors:

- Dribbble Pink `#ea4c89` for Brand signature accent search submit button, PRO badge, logo mark, active heart, hover pulses one vivid magenta against the monochrome canvas makes the brand unmistakable at any size
- Midnight Ink `#0d0c22` for Primary text, filled primary buttons, dark surface fills, icon strokes a near-black with a cool blue undertone that reads warmer than pure black against white
- Deep Plum `#060318` for Navigation bar fill, darkest text tokens, logo wordmark slightly cooler and deeper than Midnight Ink for the fixed header band
- Charcoal Plum `#3d3d4e` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Smoke `#6e6d7a` for Secondary/muted body text, helper labels, view-count and heart-count numbers carries the dense meta layer beneath thumbnails
- Fog `#9e9ea7` for Tertiary text, placeholder text, disabled icons, checkbox idle state the lightest readable neutral
- Mist `#f3f3f6` for Soft surface fill, input field backgrounds, hover wells, secondary panels the only off-white surface that sits above the page canvas
- Frost Border `#e2e8f2` for Hairline borders, divider lines, input outlines, card edges on hover a cool-tinted off-white that reads as a boundary, not a fill

Use these typography anchors:

- Mona Sans Sole typeface across the product Mona Sans is a custom geometric humanist sans drawn by GitHub, used for everything from 9px meta labels to 48px hero headlines. Its openness keeps dense 4-column grids readable, and the 450/500 mid-weights carry the designer's brand without shouting `--font-mona-sans`

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Filled Dark CTA: Primary action button (Log in, Sign up, Start a Project Brief)
- Ghost Navigation Button: Secondary text link in the nav band
- Dribbble Pink Search Submit: Search action button the only persistent pink element on most pages
- Search Input: Primary search field in the hero
- Category Pill: Popular-tag filter chip below the search bar
- Filter Tab: Category navigation in the content band (Discover, Animation, Branding, etc.)
- Filter Dropdown Trigger: 'Popular' and 'Filters' selectors
- Shot Thumbnail Card: Single piece of design work in the discovery grid

Do:

- Use #ea4c89 only for brand-anchored moments: search submit, PRO badge, logo mark, heart-fill, and one-per-page highlight. Never paint a large surface pink.
- Set filled primary buttons to #0d0c22 fill, white text, 8px radius, 10px 18px padding, Mona Sans 14px weight 600.
- Build the navigation as a 64px tall #060318 band with white text in Mona Sans 14px weight 500 never add a shadow or border beneath it.
- Use Mona Sans at 48px weight 700 with line-height 1.08 for hero headlines; let the work below it provide the visual weight.
- Keep the 4-column thumbnail grid on a pure white canvas with 8px image radius and 12px meta gap no card backgrounds, no shadows, no dividers between tiles.
- Render the PRO badge as #ea4c89 fill, white text, 4px radius, 9px weight 700 uppercase, inline with the designer name.
- Maintain 40px between content bands and 8px between meta items in the shot card the rhythm should feel dense but breathable.

Avoid:

- Don't use #ea4c89 for body text, icons, borders, or large fills it loses its meaning when overused.
- Don't add drop shadows to cards, buttons, or the navigation the system relies on color contrast and 8px radii for hierarchy.
- Don't use any color other than Midnight Ink or Deep Plum for filled dark buttons avoid #3d3d4 for primary CTAs.
- Don't apply radii above 16px to standard UI thumbnails are 8px, hero frames are 16px, and anything rounder reads as wrong.
- Don't introduce a second accent color the palette is monochrome plus one magenta, and a second accent will dilute the brand signal.
- Don't set body copy below 12px or above 16px the system compresses information at 1314px and reserves 48px for the hero only.
- Don't decorate the dark navigation with gradients, glows, or transparency keep it a flat #060318 band.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
