# AI Implementation Prompt

Build a Analogue aF-1-inspired interface using this source-derived style bundle.

Reference site: https://af1.analogueshop.com
Theme: light
Category: E-commerce
North star: Vogue spread meets Bauhaus blueprint

Use these palette anchors:

- Cobalt Signal `#002fff` for Violet action color for filled buttons, selected navigation states, and focused conversion moments.
- Pure White `#ffffff` for Page canvas, card surfaces, button text on cobalt fill, heading text on dark sections
- Graphite `#171717` for Primary body text, heading text, hairline borders, icon strokes - the workhorse near-black that carries UI structure
- Carbon `#070707` for Deepest text, dark gradient anchor points, near-black accents where maximum contrast is needed
- Ink `#000000` for Absolute black for borders, icons, and the film-strip frame effect - appears most in structural borders rather than type
- Fog `#ededed` for Soft card surface lift, input fields, subtle background differentiation from pure white canvas
- Mist `#b9b9b9` for Light surface wash, disabled or decorative backgrounds
- Dove `#c3c3c3` for Mid-neutral border for tertiary dividers
- Iron `#696969` for Muted body copy, secondary borders, placeholder text - the dominant mid-gray carrying prose-level hierarchy

Use these typography anchors:

- ITC Garamond Std Light Narrow `--font-itc-garamond-std-light-narrow` for Editorial serif - deployed for the brand-defining typographic moments: the 'Analogue aF-1' wordmark, the nostalgic pull-quote ('Remember when every shot was a moment to cherish?'), and section-level statements. Light weight at large sizes is deliberately anti-luxury-tech; a Garamond at 64px weight 400 whispers where most product pages shout with bold sans. Narrow variant tightens the serif into modern proportions.
- Graphik Medium `--font-graphik-medium` for Geometric sans for all functional UI: navigation, buttons, input fields, captions, body labels, and the massive 150px display headline. Single weight (400) at every size creates a remarkably consistent voice - no bold/light toggle. The 150px instance is the 'af-1' hero display. Extremely tight tracking (-0.067em at the largest size) pushes the geometric forms into near-architectural density.
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 50px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Action Button: The single most important interactive element - a filled cobalt blue pill that commands the visual hierarchy
- Ghost/Dismiss Button: Secondary negative action - opt-out companion to the primary CTA
- Email Input Field: Signup form input for the hero newsletter capture
- Scroll Prompt Pill: Persistent floating CTA at the bottom of hero sections
- Product Image Card: Showcase of the camera product at multiple angles
- Pre-Order Action Card: Right-column purchase block in the product detail section
- Testimonial Mini Card: Social proof - features a person and their handle
- Film-Strip Full-Bleed Frame: Editorial photography section with analog film border treatment
- Hero Gradient Banner: Atmospheric product reveal at page top
- Brand Wordmark: Top-center logo lockup
- Language Selector: Top-right locale switcher
- Press Logo Strip: Media mention band at section transition

Do:

- Use Garamond weight 400 at 40-64px for editorial moments - quotes, product names, section openers. This is the system's signature voice.
- Reserve #002fff exclusively for the single primary action on any given screen. Never use it for decoration, tags, or secondary buttons.
- Apply 20px radius to cards and 30px radius to product imagery. The rounded softness is a counterpoint to the stark black/white palette.
- Anchor sections with 50px vertical gaps and keep card padding at 20px. The compact density is intentional - the system breathes through whitespace, not through padding bloat.
- Use Graphik Medium at weight 400 exclusively. Do not introduce bold or light variants - the single-weight consistency is the design language.
- Frame full-bleed photography with the film-strip perforation motif when presenting analog/nostalgic imagery. The border IS the brand statement.
- Set letter-spacing at -0.018em or tighter for any display text above 30px. The tight tracking pushes geometric forms into architectural density.

Avoid:

- Never apply #002fff to backgrounds, icons, or text - it is a button fill only. Decorative blue dilutes its power as the system's one action color.
- Do not introduce drop shadows. The system uses flat surfaces and hairline borders. The only shadow permitted is the inset white glow on inputs.
- Do not use bold weights on Garamond. The light weight is the point - bold Garamond breaks the editorial whisper into a shout.
- Never use corner radii below 10px for interactive elements. The rounded geometry is non-negotiable for the premium feel.
- Do not add gradients to UI components. Gradients appear only as atmospheric washes on full-bleed sections, never on buttons, cards, or inputs.
- Do not use warm colors, greens, oranges, or reds for any state. The system is achromatic + cobalt. If you need a success/error state, use the neutral scale (#171717, #696969).
- Do not use Garamond for functional UI text (buttons, labels, inputs). It is reserved for editorial moments. Graphik handles everything functional.

Source prompt cues:

**Quick Color Reference**
- Background: #ffffff
- Surface: #ededed
- Primary text: #171717
- Muted text: #696969
- Border/divider: #ededed
- primary action: #002fff (filled action)

**3-5 Example Component Prompts**
1. **Hero Section**: Full-bleed white canvas. Centered wordmark 'analogue' in Graphik Medium 14px, #000000. Headline 'Analogue aF-1' in Graphik Medium 150px, #ffffff, letter-spacing -10px, centered over a radial blue gradient (rgb(0,54,140) rgb(0,79,206) rgb(237,237,237)). Subtitle in Graphik Medium 14px, #ededed. Email input (#ffffff, 15px padding, 15px radius) inline with a primary action button (#002fff, 10px 20px padding, 10px radius, white text 'Stay tuned').

2. **Film-Strip Editorial Section**: Full-bleed dark photograph with a black film-perforation pattern (sprocket holes) running vertically on left and right edges. Centered serif headline in #ffffff, ITC Garamond Std Light Narrow 40px, weight 400, letter-spacing -0.88px. Scroll prompt pill floating at bottom center (#ffffff background, 100px radius, 'Keep scrolling' in Graphik Medium 12px, #696969).

3. **Pre-Order Card**: Right-aligned block. Heading 'Pre-order now' in Graphik Medium 34px, #171717, letter-spacing -1.02px. Subtitle in Graphik Medium 14px, #696969. Price ' 449.99' in Graphik Medium 22px, #171717. Primary button (#002fff fill, white text 'Pre-order now', 10px radius, 10px 20px padding). Ghost button below (transparent, #171717 border 1px, 'No Thanks', 10px radius). Payment note in Graphik Medium 11px, #696969.

4. **Product Detail Card**: Background #ededed, border-radius 30px, no shadow. Camera product render centered. No text inside the card. Cards stack vertically in the left column of a 2-column layout, with 50px gaps between them.

5. **Press Logo Strip**: White background band. Five logos in a horizontal row, separated by 1px vertical dividers in #ededed. Logo text in #696969, Graphik Medium 12px. Centered, max-width 1200px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
