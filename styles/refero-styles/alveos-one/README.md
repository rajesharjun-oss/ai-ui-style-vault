# Alveos One

Source: [Refero Style](https://styles.refero.design/style/811f0fc6-3353-4ed6-bf3e-c98b261dcc1c) 
Reference site: [https://www.alveoslabs.com](https://www.alveoslabs.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:14:36.585Z 
Refero modified: 2026-06-03T19:54:31.498Z 
Theme: light 
Category: Other

## Style Summary

Explore Alveos One's light Other design system: Linen Canvas #fcf9f7, Bone White #ffffff colors, sans-serif, Hanken Grotesk typography, and DESIGN.md for AI...

North star: warm river-stone sanctuary - a still, cream-lit meditation room where a single graphite object rests in a pool of soft amber light.

## What To Borrow

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

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Hanken Grotesk `--font-hanken-grotesk` for Primary brand typeface for all navigation, body, headings, and lists. Weight 400 carries body and long-form copy; 500-600 lifts subheadings and buttons; 700 anchors the largest display sizes. Carries custom OpenType features (blwf, cv03, cv04, cv09, cv11) that shape the letterforms into their editorial geometry - not a system stack.
- System Sans `--font-system-sans` for Utility and icon font. Used at micro sizes (10-12px) for eyebrow labels, meta tags, and icon-adjacent text, where the unusually wide 0.4440em tracking creates the spaced-out all-caps aesthetic typical of premium wellness branding.
- SF Mono `--font-sf-mono` for Micro-verification labels (e.g. 'Verified by BrandPush.co'). Tight 0.02em tracking, monospaced at 9px - the smallest typographic element on the site, sitting beneath press logos.
- Inter `--font-inter` for Occasional fallback body copy. Lowest frequency of all fonts - appears sparingly in body contexts.
- -apple-system `--font-apple-system` for -apple-system - detected in extracted data but not described by AI

## Avoid

- Do not introduce any chromatic color - the system is 0% colorful by design and any saturated hue would break the wellness aesthetic
- Do not use sharp 0px corners or small 4px radii on feature cards - the 25px radius is what makes the imagery feel like spa product photography
- Do not use a brand-colored CTA (blue, green, red) - the near-black filled button is a deliberate anti-convention choice that signals premium health product, not SaaS
- Do not use heavy or layered shadows - the design relies on a single faint shadow or no shadow at all
- Do not use multiple gradients across the site - the radial hero gradient is the only one; content sections stay flat
- Do not pair Hanken Grotesk with a geometric or condensed display face - the brand voice is built on a single grotesque family at varied weights
- Do not center-align long body paragraphs - use centered alignment only for headlines, hero copy, and single-line metadata; body text in cards and sections should remain left-aligned

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
