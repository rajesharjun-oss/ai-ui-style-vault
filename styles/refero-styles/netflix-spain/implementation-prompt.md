# AI Implementation Prompt

Build a Netflix Spain-inspired interface using this source-derived style bundle.

Reference site: https://www.netflix.com
Theme: dark
Category: Media
North star: A black cinema lobby with one red exit sign.

Use these palette anchors:

- Netflix Red `#e50914` for Primary CTAs, brand logo, active states, and the single chromatic accent in the entire system - the only warm color allowed to break the black void
- Pure Black `#000000` for Dominant page canvas and deepest surface - the cinematic background that swallows everything non-essential
- Obsidian `#0f0f0f` for Elevated surface tone, barely distinguishable from black - used for subtle layering and section dividers
- Carbon `#232323` for Card and button surface background - the primary elevated layer above pure black
- Charcoal `#2d2d2d` for Deeper card surface and input field background - secondary surface level for nested elements
- Graphite `#323232` for Rounded card backgrounds and tertiary surface treatment
- Slate `#393939` for Hover states and pressed button backgrounds - a step lighter than carbon for interaction feedback
- Ash `#5a5a5a` for Hairline borders and subtle dividers on dark surfaces
- Steel `#808080` for Muted body text and inactive helper copy
- Fog `#b3b3b3` for Secondary body text, metadata, footer links, and de-emphasized descriptions
- Pure White `#ffffff` for Primary headings, body text, input text, and icon fills - the sole text color that carries information weight
- Cinema Indigo `#192247` for Feature card gradient origin - deep blue-violet used as the cool terminus in card background gradients
- Bordeaux Glow `#461518` for Radial highlight origin on feature cards - a warm deep red that adds atmospheric luminosity to card edges
- Ember Arc `#6f181d` for Horizontal light beam across card midlines - a thin warm glow that bisects feature cards with a soft red line

Use these typography anchors:

- Netflix Sans `--font-netflix-sans` for Netflix Sans is a custom geometric sans optimized for on-screen readability across devices. The wide weight range (400-900) creates a dramatic hierarchy where 900-weight headlines at 56-100px feel like movie marquee titles. Body text stays at 400/500 with tight tracking. The extreme size jump from 24px to 56px signals a sharp two-tier heading system: section titles, then hero displays.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 12px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary CTA Button (Red Filled): The single most important interaction element - sign-up, get started, submit
- Header Sign-In Button: Navigation authentication entry point
- Email Input Field: Email capture for membership registration
- Email Capture Composite: Hero email-to-CTA pattern - the membership conversion unit
- Hero Background Collage: Cinematic atmosphere generator for the landing page
- Trending Rank Card: Numbered content tile showing top-10/popular content with rank overlay
- Feature Reason Card: Marketing card explaining a membership benefit
- Content Row Section: Horizontally scrollable strip of content thumbnails
- Language Selector: Locale switcher in the header
- Pricing Banner: Promotional strip advertising the ad-supported tier
- Horizontal Divider with Glow: Section separator that doubles as a atmospheric light line
- Footer Link List: Site navigation links in the footer

Do:

- Use #e50914 exclusively for the single primary action per view - never decorate, never use it for icons, tags, or secondary links
- Keep all surfaces in the pure black to charcoal range (#000000-#2d2d2d) - the darkness is the brand
- Let content artwork fill 80%+ of the visual real estate; UI chrome should recede
- Use Netflix Sans weight 900 at 56-100px for hero/display headlines to create a marquee-title impact
- Apply 8px border-radius consistently to cards, buttons, and inputs - the system has exactly two radii (2px for links, 8px for containers)
- Layer content posters at slight rotations in hero/collage contexts to create a sense of depth and abundance
- Use #b3b3b3 for all secondary and metadata text - never use a chromatic gray

Avoid:

- Do not introduce any chromatic color other than #e50914 into the system - no blues, greens, or purples as UI accents (gradients on feature cards are the sole exception and are decorative only)
- Do not use drop shadows or box-shadows for elevation - depth comes from surface tone shifts only
- Do not add borders to cards - use tonal contrast between the card surface (#232323) and the page (#000000) instead
- Do not use rounded corners above 16px - the system is rectilinear with subtle softening, never pill-shaped except for tag/badge contexts
- Do not use Netflix Sans weight 400 for headings - reserve it for body copy; headings should be 700 or 900
- Do not place UI text directly on poster artwork without a dark scrim overlay - always protect legibility
- Do not introduce additional accent colors for states (hover, focus) - use #393939 (hover surface) and keep the red button as the only action signal

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #000000
- border: #5a5a5a
- accent: #e50914
- primary action: #e50914 (filled action)

**Example Component Prompts**

1. *Hero with email capture:* Full-bleed black (#000000) background with a centered content block. Headline at 56px Netflix Sans weight 900, #ffffff, line-height 1.0. Subtext at 16px weight 400, #b3b3b3. Email input with dark fill (#2d2d2d), white text, 4px inner radius. Red Get Started button (#e50914, white text, weight 500, 8px radius, 12px 24px padding) with trailing chevron.

2. *Feature reason card:* 16px border-radius card with a Cinema Indigo to Bordeaux gradient background. Heading at 20px weight 700, #ffffff. Description at 16px weight 400, #ffffff. Decorative icon in warm red/orange in the lower-right quadrant. 12px internal padding.

3. *Trending rank row:* Black background section. 'Trending Now' heading at 24px weight 700, #ffffff, with 64px top margin from previous section. Horizontal row of 5 square poster tiles with 8px gaps. Each tile has a large white rank number (100px, weight 900) overlaid on the left edge with a subtle dark outline for legibility, and a small red N-badge in the top-left corner.

4. *Header navigation bar:* Black background bar with 16px vertical padding. Left: 'NETFLIX' wordmark in #e50914, Netflix Sans weight 900, 24px. Right: dark language selector (8px radius, globe icon + 'English' text at 14px #ffffff) followed by a red Sign-In button (#e50914, white text, 14px, 8px radius, 8px 16px padding).

5. *Footer link list:* No container, directly on #000000. Multi-column grid of links in Netflix Sans 400, 13px, #b3b3b3, with 22px row spacing. 2px bottom-border on hover state. No icons, no separators between columns.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
