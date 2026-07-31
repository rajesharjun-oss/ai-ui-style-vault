# AI Implementation Prompt

Build a Pastel-inspired interface using this source-derived style bundle.

Reference site: https://usepastel.com
Theme: light
Category: SaaS
North star: Quiet paper notebook with one vivid ink stamp

Use these palette anchors:

- Paper Stone `#f5f5f4` for Light supporting surface for subtle backgrounds and section separation.
- Chalk `#e6e3e2` for Secondary card surface, subtle section bands one step above canvas
- Ink Black `#111111` for Primary headings, body text, icon strokes - the dominant text and graphic color across all contexts
- Graphite `#222222` for Secondary headings, card titles, slightly softer than Ink Black for hierarchical depth
- Fog Gray `#78716b` for Muted helper text, icon hints, tertiary metadata - warm gray that sits naturally on Paper Stone
- Smoke `#646464` for Secondary icon color, disabled-adjacent UI elements
- Ice Line `#d1dee8` for Hairline borders, card outlines, structural dividers - cool blue-tinted gray that distinguishes borders from text
- Ash `#d7d3d1` for Subtle link underlines, very light decorative borders
- Charcoal Block `#45403c` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure White `#ffffff` for Button text on dark or accent surfaces, inverse text on dark blocks
- Cobalt Stamp `#165dfb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color

Use these typography anchors:

- Figtree `--font-figtree` for Sole display and text family. 58px/45px/35px carry weight 500-600 for headlines with -0.016em tracking that pulls characters tight; 18-21px at weight 400-500 is the body and subheading range; 14-16px at weight 400-500 is caption and small UI. Negative letter-spacing scales with size - tighter at display, near-zero at body. The geometric humanist shapes of Figtree (rounded but not soft) match the 8.8px corner radius system.
- Inter `--font-inter` for Secondary micro-copy context only (appears in 6 instances at 14px) - treat as fallback/utility, not a display voice. Figtree handles all visible brand communication.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 50-80px.
- Card padding: 20-24px.
- Element gap: 12-20px.

Build these component patterns where relevant:

- Cobalt Primary Button: The only filled chromatic button. Used for the single most important action on any screen (Start a free trial, Get started).
- Charcoal Secondary Button: Dark neutral button for account-level actions (Sign up in nav).
- Ghost Outline Button: Secondary action paired with the primary (Watch demo next to Start a free trial).
- Login Text Button: Low-emphasis nav entry, present in header right cluster.
- Use-Case Card: Screenshot showcase card in the 'Works on any file' grid - demonstrates the product on different surface types.
- Testimonial Block: Quote + attribution + avatar, placed under hero headline and in social proof sections.
- Logo Trust Strip: Row of monochrome partner/client logos.
- Problem Pill Label: Small uppercase or sentence-case tag introducing a section (e.g., 'Problem' eyebrow).
- Feature Checklist Item: Inline trust signals like "14-day free trial" and "No credit card required" near CTAs.
- Top Navigation Bar: Sticky or static top bar with brand mark left, center links, right actions.
- Section Headline: Large section-opening text ('Works on any file...', 'Trusted by fast moving agencies...').
- Image Placeholder Block: Empty/loading state for large showcase images and illustrations.

Do:

- Use Cobalt Stamp #165dfb only for filled primary buttons, active links, and the brand logomark dot - never for headings, icons, or decorative washes
- Set border-radius to 8.8px for every card, button, and contained image; reserve 15px for larger decorative surfaces and 120px only for the brand mark
- Set body text to Figtree 16-18px weight 400 in Ink Black #111111; reserve Fog Gray #78716b exclusively for helper metadata and small icon hints
- Apply negative letter-spacing: -0.016em at 58px, -0.014em at 45px, scaling down to normal at 18px and below
- Separate sections using background color shifts between Paper Stone and Chalk rather than borders, dividers, or shadows
- Keep CTAs flat - no drop shadow, no gradient, no hover lift; the Cobalt Stamp fill is the entire elevation signal
- Default page canvas to Paper Stone #f5f5f4; use Pure White #ffffff only inside cards sitting on the canvas, never as the page background

Avoid:

- Don't introduce additional accent colors - the system is 1% colorful by design; a second chromatic hue breaks the 'one stamp' identity
- Don't use pure #000000 - Ink Black is #111111, Graphite is #222222, Charcoal Block is #45403c; always retain the warm undertone
- Don't add box-shadows to cards or buttons - the design uses flat surfaces with hairline borders as its elevation language
- Don't round corners to 12px, 16px, or 9999px for cards or buttons - 8.8px is a deliberate, non-standard value that defines the system
- Don't use letter-spacing 0 or positive values on headlines - negative tracking at 35px and above is a signature of this system
- Don't use Cobalt Stamp for large text blocks, section backgrounds, or illustration fills - it loses urgency when used at scale
- Don't use Inter for display or body copy - Figtree is the only visible brand voice; Inter is a utility fallback

Source prompt cues:

Quick Color Reference:
- text: #111111 (Ink Black)
- background: #f5f5f4 (Paper Stone)
- border: #d1dee8 (Ice Line)
- muted text: #78716b (Fog Gray)
- accent: #165dfb (Cobalt Stamp)
- primary action: no distinct CTA color

Example Component Prompts:
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. Create a use-case card grid (4 columns). Each card: Pure White #ffffff fill, 1px #d1dee8 border, 8.8px radius, no shadow. Inner image: 8.8px radius, fills card width minus 20px padding. Caption below image: Figtree 14px weight 400, #111111.

3. Create a testimonial block. Quote: Figtree 21px weight 400, #111111, line-height 1.5. Attribution row: 32px circular avatar + name in 14px weight 500 #111111 + role in 14px weight 400 #78716b. 20px vertical gap between quote and attribution.

4. Create a section eyebrow pill: 'Problem' label in Figtree 12px weight 500, #78716b text, on Chalk #e6e3e2 fill, 9999px radius, 4px 12px padding. Center it above a Figtree 35px weight 500 #111111 headline with -0.014em tracking.

5. Create a logo trust strip: 5 monochrome partner logos in Ink Black #111111 at 24px optical height, evenly spaced across a 1200px container, no dividers, sitting directly on the Paper Stone canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
