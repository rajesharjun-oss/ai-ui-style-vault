# AI Implementation Prompt

Build a Alveos One-inspired interface using this source-derived style bundle.

Reference site: https://www.alveoslabs.com
Theme: light
Category: Other
North star: warm river-stone sanctuary - a still, cream-lit meditation room where a single graphite object rests in a pool of soft amber light.

Use these palette anchors:

- Linen Canvas `#fcf9f7` for Page background, hero gradient origin - warm cream base that absorbs the entire site into a unified off-white
- Bone White `#ffffff` for Card surfaces, section backgrounds, raised panels against the linen canvas
- Graphite Ink `#000000` for Primary text, dominant border color across cards and sections - the system's typographic anchor
- Nightshade Black `#05060b` for Primary action button fill, footer background - near-black with a faint cool undertone
- Deep Harbor `#030f1c` for Alternate dark surface, nav background - indistinguishable from Nightshade but carries a subtle navy tilt
- Charcoal Slate `#1d1d1d` for Body borders, secondary surfaces, image card borders - slightly softer than pure black
- Iron Grey `#262628` for Icon strokes, heading borders, secondary fills - mid-dark neutral for iconography
- Obsidian `#111112` for Nav text, body borders - the darkest readable neutral after Nightshade
- Stone Grey `#575757` for Muted body text, default body border - the primary mid-grey for paragraph copy and dividers
- Ash `#717171` for Helper text, icon strokes, link borders - lighter mid-grey for secondary metadata
- Pebble `#989695` for Subtle body borders, low-emphasis copy - barely-there dividers
- Concrete `#a5a5a5` for Faint body text and dividers - used sparingly for ultra-low emphasis
- Dove `#bababa` for Button border, icon fill, disabled-state borders - the lightest mid-tone
- Clay Shadow `#d1cfcd` for Soft shadow color, card box-shadows, subtle background fills - warm-tinted shadow grey that matches the canvas
- Haze `#ecedef` for Subtle card borders, low-contrast dividers - the cool counterpoint to Clay Shadow

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Hanken Grotesk `--font-hanken-grotesk` for Primary brand typeface for all navigation, body, headings, and lists. Weight 400 carries body and long-form copy; 500-600 lifts subheadings and buttons; 700 anchors the largest display sizes. Carries custom OpenType features (blwf, cv03, cv04, cv09, cv11) that shape the letterforms into their editorial geometry - not a system stack.
- System Sans `--font-system-sans` for Utility and icon font. Used at micro sizes (10-12px) for eyebrow labels, meta tags, and icon-adjacent text, where the unusually wide 0.4440em tracking creates the spaced-out all-caps aesthetic typical of premium wellness branding.
- SF Mono `--font-sf-mono` for Micro-verification labels (e.g. 'Verified by BrandPush.co'). Tight 0.02em tracking, monospaced at 9px - the smallest typographic element on the site, sitting beneath press logos.
- Inter `--font-inter` for Occasional fallback body copy. Lowest frequency of all fonts - appears sparingly in body contexts.
- -apple-system `--font-apple-system` for -apple-system - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Sticky header over hero and scroll content
- Pre-Order CTA Button: Primary action - the only conversion button in the header and repeated throughout the site
- Pill Eyebrow Label: Section intro tag sitting above the hero headline
- Hero Section with Spotlight: Full-viewport opening that frames the product
- Image Feature Card: Large rounded lifestyle photograph with overlaid text - the primary content card
- Two-Column Card Grid: Primary content arrangement for feature showcases
- Press Logos Bar: Social proof section - 'AS SEEN ON'
- Outlined Secondary Button: Alternative to the filled CTA for non-primary actions
- Dark Footer: Site footer on Nightshade Black background

Do:

- Use 25px border-radius for all image cards, feature cards, and photograph containers - this is the dominant corner geometry and defines the soft, premium feel
- Use Nightshade Black #05060b as the primary action button fill with white text and 12px radius - never introduce a chromatic CTA color
- Set the page canvas to Linen Canvas #fcf9f7 for all body sections and let Bone White #ffffff surface only as raised cards
- Use Hanken Grotesk for all primary type and enable its custom OpenType features ('blwf', 'cv03', 'cv04', 'cv09', 'cv11') to preserve the editorial letterform shapes
- Apply 0.4440em letter-spacing to small all-caps labels (10-12px) - the wide tracking is a signature element of the brand voice
- Use the warm radial gradient (Linen Canvas Clay Shadow) only for the hero spotlight - do not reuse it in content sections
- Keep shadows nearly invisible: rgba(0,0,0,0.05-0.08) at low blur radii. Elevation should be implied through contrast and radius, not drop-shadow weight

Avoid:

- Do not introduce any chromatic color - the system is 0% colorful by design and any saturated hue would break the wellness aesthetic
- Do not use sharp 0px corners or small 4px radii on feature cards - the 25px radius is what makes the imagery feel like spa product photography
- Do not use a brand-colored CTA (blue, green, red) - the near-black filled button is a deliberate anti-convention choice that signals premium health product, not SaaS
- Do not use heavy or layered shadows - the design relies on a single faint shadow or no shadow at all
- Do not use multiple gradients across the site - the radial hero gradient is the only one; content sections stay flat
- Do not pair Hanken Grotesk with a geometric or condensed display face - the brand voice is built on a single grotesque family at varied weights
- Do not center-align long body paragraphs - use centered alignment only for headlines, hero copy, and single-line metadata; body text in cards and sections should remain left-aligned

Source prompt cues:

**Quick Color Reference**
- text: #000000 (primary), #1d1d1d (body), #575757 (muted)
- background: #fcf9f7 (canvas), #ffffff (cards)
- border: #d1cfcd (soft), #1d1d1d (strong), #575757 (default)
- accent: none (system is 0% colorful)
- primary action: #05060b (filled action)

**Example Component Prompts**

1. Build a hero section: background radial-gradient(50% 95% at 50% 108.6%, #fcf9f7 0%, #a89c8a 100%). Centered pill label (background #ffffff, text #262628, border 1px #d1cfcd, Hanken Grotesk 12px weight 500, padding 7px 14px, radius 100px). Display headline at 52px Hanken Grotesk weight 600, color #000000. Subtext at 18px weight 400, color #1d1d1d, max-width 560px.

2. Build an image feature card: full-bleed photograph, 25px border-radius, dark vertical gradient overlay (transparent rgba(0,0,0,0.7) at bottom). White headline 28px Hanken Grotesk weight 600, white body 16px weight 400, both bottom-left with 24px padding. Box-shadow rgba(0,0,0,0.05) 0px 2px 10px.

3. Build a Pre-Order button: background #05060b, color #ffffff, Hanken Grotesk 16px weight 500, padding 10px 20px, border-radius 12px. No border, no shadow.

4. Build the press logos bar: centered 'AS SEEN ON' in 12px Hanken Grotesk weight 500, letter-spacing 0.4440em, color #1d1d1d, flanked by 1px horizontal lines in #1d1d1d extending ~120px each side. Row of 5 press logos in #000000, 24-32px tall, evenly spaced. Below: 'AND OVER 500 NEWS SITES' in tracked-out caps + 'Verified by BrandPush.co' in 9px SF Mono weight 600.

5. Build a dark footer: background #05060b, padding 48px vertical, text in #ffffff at 80% opacity, Hanken Grotesk 14px weight 400, links separated by 20px gap.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
