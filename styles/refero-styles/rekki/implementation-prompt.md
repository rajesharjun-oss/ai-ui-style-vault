# AI Implementation Prompt

Build a REKKI-inspired interface using this source-derived style bundle.

Reference site: https://rekki.com
Theme: dark
Category: SaaS
North star: Mission control dashboard in a darkroom

Use these palette anchors:

- Signal Blue `#0063e1` for Primary CTA fill, active nav indicator, brand accent dots, link highlights - the single chromatic voice in an otherwise silent monochrome system
- Obsidian `#000000` for Page canvas, dominant background, hairline divider color, icon fill - the floor of the entire system
- Carbon `#040910` for Card surface base, deep panel backgrounds - first step above the page canvas
- Graphite `#0d0d0d` for Elevated card surfaces, section backgrounds, border fills - the mid-surface layer
- Iron `#1f1f1f` for Input field backgrounds, form controls, tertiary surfaces
- Steel `#2b2c2e` for Highest card elevation, modal surfaces, hover-state surfaces - the ceiling of the surface stack
- Ash `#858585` for Body text, muted labels, secondary borders, link underlines - the workhorse neutral for non-heading text
- Smoke `#979797` for Icon strokes, tertiary button borders, low-priority text
- Fog `#8c8c8c` for Link text, subdued navigation labels
- Paper `#ffffff` for Light neutral action fill for buttons on dark surfaces.

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Diatype REKKI `--font-diatype-rekki` for Primary brand typeface - body text at 16-20px weight 400, large headlines at 56-86px weight 400 with aggressive negative tracking (as tight as -0.064em at 86px). The whisper-weight headlines are signature: no bold shouting, just precise geometric calm. Subheadings/nav at 16-20px weight 400-600.
- Diatype REKKI Bolder Rounded `--font-diatype-rekki-bolder-rounded` for Display variant for the most prominent brand moments - heavier geometric terminals, used sparingly at 72px for hero declarations and at 12-20px weight 700 for emphasis labels in nav/inputs.
- OCD-GARRI `--font-ocd-garri` for Secondary utility face - likely for product UI labels, status indicators, or monospaced-feeling tabular data within the embedded product screenshots. Carries slight positive letter-spacing (0.033-0.038em) giving it a structured, instrument-label quality.
- Diatype REKKI Regular `--font-diatype-rekki-regular` for Diatype REKKI Regular - detected in extracted data but not described by AI
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary CTA Button: The singular conversion action
- Navigation Header Button: Compact header action
- Nav Link: Primary navigation text
- Hero Display Heading: Page-level headline
- Section Heading: Subsection headline
- Product UI Panel Card: Embedded product screenshot container
- Standard Card: Content grouping surface
- Feature Card with Image: Marketing card with visual
- Text Input: Form input field
- Status Pill / Tag: State indicator or category label
- Cookie Consent Banner: Legal/privacy overlay
- Logo Mark: Brand identity

Do:

- Use #0063e1 exclusively for the single primary CTA per viewport - never for decorative elements, illustrations, or non-action accents
- Apply -0.064em letter-spacing on display type (72px+) and scale proportionally down to -0.005em at body sizes (12px)
- Use Diatype REKKI weight 400 for all headlines - no bold weights for display type; authority comes from size and tracking, not weight
- Communicate card elevation through the rgba(255,255,255,0.12) 1px inset border, never through drop shadows
- Maintain the 5-level surface stack (Obsidian Carbon Graphite Iron Steel) with clear 3-5% luminance steps between each level
- Use 59px border-radius for all pill-shaped buttons and 16px radius for content cards - never mix the two radii on the same element type
- Let product UI screenshots occupy the visual focal point of marketing sections rather than stock photography or lifestyle imagery

Avoid:

- Never use multiple chromatic accent colors - the system is monochromatic + one blue; introducing green, red, or purple breaks the entire visual language
- Never apply drop shadows to cards or panels; the inset white border IS the elevation system
- Never set body text below #858585 contrast against the black canvas; use Paper #ffffff for any text that needs to be read at a glance
- Never use bold (700) weights for headlines; Diatype REKKI weight 400 at large sizes with tight tracking is the signature - bolding destroys it
- Never use letter-spacing greater than 0em on display type; the negative tracking is what makes the headlines feel architectural
- Never place white or light-colored cards on the dark canvas; all surfaces must stay in the black-to-charcoal range
- Never use rounded images or organic shapes for the logo or brand mark - the geometry is angular and precise

Source prompt cues:

**Quick Color Reference**
- text: #ffffff (headings, primary), #858585 (body, secondary)
- background: #000000 (page), #0d0d0d (cards), #2b2c2e (elevated)
- border: rgba(255,255,255,0.12) 1px inset (cards), #858585 (hairline dividers)
- accent: #0063e1 (brand blue, status dots, highlights)
- primary action: #0063e1 (filled action)

**Example Component Prompts**

1. **Hero Section**: Full-bleed #000000 background. Centered Diatype REKKI display headline at 86px weight 400, #ffffff, letter-spacing -0.064em, line-height 1.0. Subtext at 18px weight 400, #858585. Primary CTA: pill button, #0063e1 fill, white text at 16px, 59px border-radius, 20px 32px padding.

2. **Product Feature Card**: 16px border-radius, #0d0d0d background, 1px inset border rgba(255,255,255,0.12). 24px internal padding. Heading at 20px Diatype REKKI weight 400, #ffffff, -0.027em tracking. Body text at 16px #858585. Embedded product screenshot fills the lower half with 8px radius.

3. **Navigation Header**: 80px tall, transparent over #000000. Logo (REKKI wordmark + mark) in #ffffff, left-aligned. Four nav links in Diatype REKKI 16px weight 400, #858585, centered. Pill CTA button right-aligned: #0063e1 fill, 59px radius, white text at 12-14px.

4. **Dark Form Input**: 48px tall, #1f1f1f background, 8px border-radius, outer glow rgba(255,255,255,0.2) 0px 0px 1px 0px. Diatype REKKI Bolder Rounded 16px, #ffffff text, #858585 placeholder. 16px horizontal padding.

5. **Logo Wall / Social Proof**: Horizontal row of 4-6 customer wordmarks in #858585 on #000000 background, evenly spaced with 60px gaps, no logos, no backgrounds, text-only treatment.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
