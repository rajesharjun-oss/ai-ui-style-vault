# AI Implementation Prompt

Build a Quicken-inspired interface using this source-derived style bundle.

Reference site: https://www.quicken.com
Theme: mixed
Category: Fintech
North star: electric violet on white marble

Use these palette anchors:

- Voltage Violet `#471cff` for Primary action buttons, active nav items, key links, brand emphasis - the single chromatic pulse of the interface; everything else defers to it
- Deep Iris `#0f0733` for Dark section backgrounds, hero canvas, high-contrast text on light surfaces - the midnight counterpart that anchors alternating dark bands
- Signal Red `#eb0130` for Promotional accents, sale/urgency indicators, highlight strokes - used sparingly to flag attention without competing with the primary violet
- Lilac Whisper `#dbd3ff` for Soft card and container borders - a low-contrast violet edge that brands outlines without adding visual weight
- Periwinkle Mist `#bbc5fa` for Cooler card border tone for grouping and container edges - second step in the violet border scale for layered cards
- Coral Burst `#ff5a43` for Error and warning badge fills, alert pills - warm contrast against the cool violet system
- Aqua Pop `#7ae7fb` for Decorative badge backgrounds, hero trust-pill fill - cool cyan that brightens dark sections
- Ink Black `#18181f` for Primary body and heading text, dominant border color, icon strokes - the near-black that carries all readable content
- Carbon `#494949` for Secondary text, muted nav, supporting borders - the mid-gray step between ink and white
- Pure White `#ffffff` for Page and card backgrounds, text on dark surfaces, button fills for ghost variants
- Frost Blue `#f0f5fa` for Subtle surface tint for alternating bands, header backgrounds - barely-there cool wash
- Linen Gray `#eaecf7` for Table dividers, hairline borders in data-heavy layouts - a cool neutral that doesn't fight the violet palette

Use these typography anchors:

- Haffer `--font-haffer` for Single-family system for everything from body to display. Weight 400 carries body, nav, and table text; weight 600 handles headings, buttons, and emphasis. The custom geometric construction gives a contemporary financial-tech voice - rounder apertures than Inter, tighter terminals than Geist.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary Action Button: Main CTA for conversion moments
- Ghost Action Button: Secondary CTA paired beside a primary
- Hero Headline: Top-of-page value proposition
- Trust Badge Pill: Social proof or category label above hero headline
- Pricing Tier Card: Product plan comparison on pricing sections
- Promotional Badge: Highlight discount or urgency markers
- Feature Showcase Card: Dark-section feature highlight with illustration
- Feature Comparison Table: Side-by-side plan feature matrix
- Top Navigation Bar: Persistent site navigation
- Phone Mockup Frame: Hero product visualization
- Centered Section Header: Transitional section introduction
- Inline Feature Icon: Category indicator on pricing and feature cards

Do:

- Use Voltage Violet (#471cff) exclusively for the single most important action per screen - never split attention across multiple violet CTAs
- Set card borders to Lilac Whisper (#dbd3ff) or Periwinkle Mist (#bbc5fa) instead of neutral gray to reinforce brand identity at every edge
- Set all buttons to 400px border-radius - pill shapes are non-negotiable in this system and signal action
- Tighten letter-spacing progressively: -0.030em at 16px, -0.033em at 26-30px, -0.045em at 48px+
- Alternate between white and Deep Iris (#0f0733) sections to create rhythm - never let two dark sections sit adjacent without a white break
- Anchor dark sections with white text at full opacity; use Lilac Whisper (#dbd3ff) for secondary text on dark rather than dimmed white
- Use Signal Red (#eb0130) only for discount badges and urgency - never as a replacement for the primary action color

Avoid:

- Don't introduce new hues - the system is binary: violet accents on white, or white on Deep Iris
- Don't use drop shadows on components other than the pricing card stack - depth should come from color and border
- Don't use sharp 0px or minimal 4px corner radii on cards - 16px is the minimum card radius and buttons must stay pill-shaped
- Don't place body text below 14px or above 18px - the system avoids both micro-copy and large body type
- Don't use #18181f and #000000 interchangeably - #000000 is reserved for navigation chrome; body text uses #18181f
- Don't add gradients - the system is flat by design; depth comes from violet-to-Deep-Iris section contrast
- Don't use weight 400 for headings or weight 600 for body - the binary weight assignment is part of the typographic signature

Source prompt cues:

**Quick Color Reference**
- text: #18181f
- background: #ffffff
- border: #dbd3ff or #bbc5fa
- accent: Voltage Violet #471cff
- primary action: #471cff (filled action)
- dark surface: #0f0733

**Example Component Prompts**

1. Create a Primary Action Button: #471cff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a pricing tier card: white background, 16px corner radius, 1.5px border in #bbc5fa, padding 24px. A violet icon tile (32x32px, #471cff, 8px radius) sits top-left. Plan name at 20px Haffer weight 600 #18181f below. Description at 14px #494949. A price line showing $3.99/month at 22px weight 600, a strikethrough $7.00 at 14px #494949, and a Signal Red badge (#eb0130, white text, 20px radius, 4px 8px padding) reading '50% off'. Feature checklist below with small violet checkmarks. Footer row: filled Voltage Violet button + ghost violet button, both 400px radius.

3. Create a feature showcase card: Deep Iris (#0f0733) background, 16px radius, full-bleed product visualization in the upper 60% (chart or UI mock in violet/cyan/white). Lower 40% is white with 24px padding, heading at 26px Haffer weight 600 #18181f, body at 16px #494949, and a violet text link (#471cff, no underline by default, underline on hover).

4. Create a comparison table: white background, 1px row dividers in #eaecf7, three columns. Each column header has a 40x40px violet icon tile (#471cff, 8px radius) above the plan name at 16px weight 600. Feature rows at 16px weight 400 #18181f on the left, with violet circle checkmarks (8px filled #471cff) in the appropriate cells.

5. Create a centered section header: white background, 48px Haffer weight 600 #18181f heading centered with -0.045em letter-spacing, and a Voltage Violet pill button (#471cff, white text, 400px radius, 12px 24px padding) centered 16px below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
