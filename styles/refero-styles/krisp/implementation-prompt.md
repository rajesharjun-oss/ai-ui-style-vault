# AI Implementation Prompt

Build a Krisp-inspired interface using this source-derived style bundle.

Reference site: https://krisp.ai
Theme: light
Category: AI
North star: Warm cream paper, inked in indigo, lit by a violet spark - a confident editorial-tech feel.

Use these palette anchors:

- Midnight Iris `#131032` for Primary text, headings, and dark section backgrounds - the deepest near-black with a violet undertone carries the same identity across both light copy and immersive dark bands
- Iris Spark `#614efa` for Filled buttons, link emphasis, active states, gradient stops - the only vivid saturated color in the palette, used as a small functional spark against the cream canvas
- Violet Mist `#dfdcfe` for Soft accent washes, tag backgrounds, decorative highlights - a near-white violet tint that echoes Iris Spark at very low intensity
- Cyan Glow `#98c8ff` for Supporting palette color for small decorative accents when the core palette needs contrast.
- Mint Whisper `#eafdfa` for Pill badge and announcement tag backgrounds - a barely-there cool tint to differentiate informational chips from the warm cream canvas
- Iris Halo `#8374fb` for Soft highlight overlays and secondary gradient midtones - a lighter violet used in multi-stop gradients
- Fog `#918f9f` for Muted body copy, helper text, secondary labels - the primary low-emphasis text color against cream and white surfaces
- Shadow `#5b5971` for Stronger secondary text, metadata - deeper than Fog for labels that need more presence without reaching Midnight Iris
- Ash `#a1a1aa` for Disabled text, placeholder content, very low-emphasis UI elements
- Slate `#1a1a22` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Charcoal `#24232d` for Secondary dark text, very dark UI elements
- Hairline `#e7e7ea` for Borders, dividers, card outlines - a cool light gray that separates surfaces on the warm cream canvas
- Silver `#cccccc` for Shadows, very subtle borders, disabled surface tones
- Snow `#ffffff` for Card surfaces, button text, dark-section text - pure white for maximum contrast on dark backgrounds
- Cloud `#f7f7f8` for Secondary surface, footer background - a cool off-white that sits one step below Snow
- Warm Paper `#f2ece2` for Dominant page canvas - a warm beige that replaces the typical cold white SaaS background, giving the entire site a tactile, editorial feel

Use these typography anchors:

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Single-family geometric humanist sans used for every text role from 10px badges to 58px display headlines

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Filled Violet Button: Primary action button - solid Iris Spark fill with white text
- Dark Outline Button: Secondary action button - used for 'Book a demo' and similar
- Text Link Button: Inline action with chevron - used in nav for 'Get Krisp' with dropdown indicator
- Pill Tab Selector: Segmented control for switching between meeting states (During / After / Before Meeting)
- Announcement Pill Badge: Eyebrow tag above hero headline - 'Introducing Accent Conversion' style
- Gradient Display Headline: Signature hero text treatment - 'Voice AI' portion of the headline
- Feature Card: Content card for feature grids - 'Multilingual meeting support', '1-click sharing'
- Dark Feature Section Card: Feature card variant on dark Midnight Iris background
- Customer Logo Strip: Social proof band showing client logos (Medium, Okta, Skechers, Autodesk, Sony, Cisco, ServiceTitan, GitHub)
- Top Navigation Bar: Site header with logo, menu, and actions
- Webby Award Sticker: Floating badge in bottom-right corner - '20th Annual Webby Awards, Vote for Krisp'
- Icon: UI iconography for features and navigation

Do:

- Use #f2ece2 (Warm Paper) as the default page canvas - never substitute pure white at the root level
- Apply the Iris Spark to Cyan Glow gradient only on display-size headlines (42px+); never on body or heading text
- Use 8px border-radius for all buttons and small interactive elements; 16px for cards; 9999px for pills and tabs
- Double-duty #131032 (Midnight Iris) as both text color on light surfaces and background color on dark sections - the hue reads as the same brand identity in both contexts
- Separate action button styles by fill: Iris Spark (#614efa) for one type, Slate (#1a1a22) for the other - never use two violet buttons side by side
- Use Hairline (#e7e7ea) at 1px for card borders and dividers; achieve elevation through surface color shifts rather than shadows
- Keep #918f9f (Fog) as the only muted body text color; never use Ash (#a1a1aa) for primary copy

Avoid:

- Don't introduce new saturated colors - Iris Spark is the only vivid hue, and it should appear at most 1-2 times per viewport
- Don't apply drop shadows to cards or panels - surface shifts on the Warm Paper canvas are the elevation system
- Don't use pure #000000 for text - Midnight Iris (#131032) carries the brand undertone
- Don't place white cards on white backgrounds; always layer Snow (#ffffff) on Warm Paper (#f2ece2) or Cloud (#f7f7f8) for separation
- Don't use gradients on body, heading, or subheading text - the gradient treatment is reserved for display headlines only
- Don't use border-radius larger than 8px on buttons - the 8px radius is the button signature, not pills
- Don't show customer logos in full color - they must be muted to grayscale/gray to maintain the quiet editorial feel

Source prompt cues:

primary action: no distinct CTA color
**Quick Color Reference:**
- text: #131032 (Midnight Iris)
- background: #f2ece2 (Warm Paper)
- card/surface: #ffffff (Snow)
- border: #e7e7ea (Hairline)
- muted text: #918f9f (Fog)
- accent/filled button: #614efa (Iris Spark)
- dark section background: #131032 (Midnight Iris)

**Example Component Prompts:**

1. **Create a hero section on Warm Paper canvas (#f2ece2).** Eyebrow pill badge: Mint Whisper background (#eafdfa), Midnight Iris text (#131032), 14px weight 500, 9999px radius, padding 6px 14px. Display headline at 48px Plus Jakarta Sans weight 700: split into two parts - first word(s) in the linear-gradient(90deg, #614efa 0%, #98c8ff 100%) text-fill treatment, remaining words in solid #131032. Subtext at 18px weight 400, #918f9f. Single filled button: #614efa background, white text weight 600, 8px radius, padding 12px 20px.

2. **Create a 2x2 feature card grid.** Canvas: Warm Paper (#f2ece2). Each card: white (#ffffff) background, 1px Hairline (#e7e7ea) border, 16px radius, padding 32px 28px. Top of each card: 24px outlined icon in Iris Spark (#614efa) with 1.5px stroke. Title: 22px weight 600, #131032. Body: 16px weight 400, #918f9f. 24px gap between cards.

3. **Create a dark feature section.** Full-bleed background #131032, padding 80-96px vertical. Section heading: 36px weight 600, #ffffff, left-aligned. Cards below: transparent or very subtle lift background, 16px radius, padding 32px 28px, thin border rgba(255,255,255,0.1). Each card title: 22px weight 600, #ffffff, preceded by a small 6px coral-red dot. Body: 16px weight 400, #918f9f. Use a pill-shaped tab selector (9999px radius) at the top with Snow (#ffffff) active state.

4. **Create a customer logo strip.** Single row on Warm Paper canvas, 8 logos evenly distributed. Each logo rendered in grayscale with opacity 0.6-0.7, color #918f9f. 48-64px vertical padding above and below. No labels or captions. Logos scale to ~80px height max.

5. **Create a sticky top navigation.** White background, 64px height, full width with max-width 1200px inner container. Left: 'krisp' wordmark in #131032, 22px weight 700. Center-left: 5 nav items in #131032 weight 500, 16px, with small chevron-down icons on 3 items. Right cluster: 'Sign in' as plain text link (#131032), 'Book a demo' as dark filled button (#1a1a22 background, white text, 8px radius, 12px 20px padding), 'Get Krisp' as violet filled button (#614efa background, white text, 8px radius, 12px 20px padding, with small downward chevron icon).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
