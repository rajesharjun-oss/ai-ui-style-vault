# AI Implementation Prompt

Build a Stark-inspired interface using this source-derived style bundle.

Reference site: https://www.getstark.co
Theme: light
Category: SaaS
North star: midnight lecture hall with yellow highlighter

Use these palette anchors:

- Midnight Navy `#10284b` for Hero background, primary headings, footer surface - the dominant brand color establishes authority and anchors the dark-to-light page split. Used as a background field for the above-the-fold section and as body-text color on the cream secondary surface
- Stark Violet `#381fd1` for Primary action fills (Get started, Sign up, Request demo), card border accents, active nav state, decorative icon strokes, and inline emphasis text. The vivid violet against midnight navy creates a switched-on, electric feel without aggression
- Highlighter Yellow `#fedb63` for Diagonal text-highlight gradient fill, one specific secondary CTA, and illustration accent. Yellow never decorates broadly - it marks, underlines, and punctuates specific words within dark-on-light headlines
- Lilac Tint `#e5e0ff` for Soft button surface variant, gentle tinted card backgrounds. A desaturated wash of the violet brand that softens interactive elements without competing with the primary action
- Mint Splash `#99d6cc` for Decorative illustration accent in feature cards and dashboard widgets. Used sparingly in flat geometric shapes within artwork, not in core UI controls
- Page Canvas `#faf5ff` for Lightly purple-tinted near-white page background. The faint violet cast unifies the cream and white surfaces under one chromatic family
- Cream Field `#f6f6eb` for Secondary section surface and body-text color on the dark hero. The warm greenish-cream provides a relaxed counterpoint to the midnight navy and is the dominant body-text/link color on the dark section
- Carbon `#000000` for Body text on light surfaces, icon strokes, and high-contrast elements. Not used as a background - the system prefers the midnight navy for darkness
- Pure White `#ffffff` for Text on dark hero, card surfaces, nav backgrounds, product screenshot frames. The bright surface that holds product imagery and dashboard content
- Hairline Gray `#e5e7eb` for Universal border color for cards, inputs, dividers, link underlines, and structural separators. The single achromatic border workhorse

Use these typography anchors:

- ArminGrotesk `--font-armingrotesk` for The single custom typeface carries the entire brand voice. Weight 900 is the hero display weapon (110px headline) - used at maximum volume for the opening statement. Weight 600 handles section headings and subheadings (24-48px). Weight 500 is the button and label workhorse. Weight 400 is body text. The geometric grotesque construction gives a contemporary, slightly technical authority.
- RobotoMono `--font-robotomono` for All-caps eyebrow labels and section markers (e.g., 'EXPLORE THE STARK PLATFORM', 'SPEED UP DESIGN & DEV'). The monospaced mono with wide tracking creates a distinct utilitarian signal that sits above the display heading and below the nav - a consistent navigational breadcrumb layer.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 56px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Violet Primary Button: Main conversion action
- Yellow Secondary Button: Alternate call-to-action on dark hero
- Ghost Outline Button: Tertiary action in navigation
- Pill Label: Category and feature eyebrow tags
- Hero Stat Card: Animated metric callout on hero
- Status Legend Card: Right-side stack on hero
- Product Screenshot Frame: Desktop and mobile app previews
- Feature Card with Illustration: Four-column feature grid
- Navigation Bar: Top-level site navigation
- Highlighted Text Run: Inline emphasis within headings
- Avatar Group + Label: Social proof element
- Decorative Dot Pattern: Hero background texture

Do:

- Use ArminGrotesk weight 900 at 110px with -2.2px letter-spacing for the primary hero headline - this is the signature wall-of-text moment.
- Apply the diagonal yellow highlighter gradient (transparent 50% #fedb63 50%) to one or two words inside a dark-on-light headline to create inline emphasis.
- Set primary action buttons to #381fd1 fill with white text, 6px radius, and 8pxx24px padding. Never use the midnight navy as a button fill.
- Use RobotoMono 700 at 13px with 0.08em tracking for all uppercase eyebrow labels above section headings.
- Alternate between midnight-navy hero sections and cream (#f6f6eb) body sections to maintain the dark-to-light page split.
- Set the page background to #faf5ff (not pure white) to carry the subtle violet cast across all light surfaces.
- Use #e5e7eb hairline borders at 1px for all card edges, input fields, and structural dividers - the system relies on lines, not shadows.

Avoid:

- Do not use weight 400 or 500 for the hero display headline - the 900 weight at 110px is the brand's signature and must be deployed at maximum volume.
- Do not apply the yellow highlighter gradient to more than 2-3 words in a single headline; it dilutes the marking-pen effect.
- Do not use shadows for cards on the cream or light purple surfaces - the system prefers flat surfaces with hairline borders.
- Do not introduce a second brand-violet shade; #381fd1 is the single chromatic action color and must remain uncontested.
- Do not set body text below 16px or use letter-spacing wider than -0.01em at display sizes - the tight tracking is essential to the geometric grotesque feel.
- Do not place CTA buttons on the midnight-navy hero without sufficient contrast padding or a distinctive fill - the violet and yellow must be the only bright spots on the dark field.
- Do not use the cream (#f6f6eb) as a background for the hero - it is exclusively a secondary-section surface that appears after the dark fold.

Source prompt cues:

**Quick Color Reference**
- Text (light surfaces): #000000
- Text (dark hero): #ffffff
- Page background: #faf5ff
- Cream section: #f6f6eb
- Border: #e5e7eb
- primary action: #381fd1 (filled action)
- Highlighter accent: #fedb63

**3 Example Component Prompts**

1. *Hero Headline with Yellow Highlight*: Create a hero section on #10284b background. Display headline 'Digital accessibility compliance on autopilot' in ArminGrotesk weight 900 at 110px, color #ffffff, letter-spacing -2.2px, line-height 1.10. Apply the word 'autopilot' with a diagonal yellow highlighter using background: linear-gradient(to right bottom, transparent 50%, #fedb63 50%). Below: body text in ArminGrotesk 400 at 20px, color #f6f6eb, max-width 600px centered.

2. *Violet Primary CTA Button*: Create a filled button with #381fd1 background, white text in ArminGrotesk 500 at 16px, 6px border-radius, 8px padding-top, 8px padding-bottom, 24px padding-left, 24px padding-right, letter-spacing 0.32px. No border, no shadow. Label: 'Get started for free'.

3. *Feature Card Grid Item*: Create a card on #faf5ff background with 40px border-radius, 24px padding. Top: flat geometric illustration using #99d6cc, #fedb63, #381fd1, and #10284b. Below illustration: uppercase label in RobotoMono 700 at 13px, color #381fd1, letter-spacing 1.04px. Then: heading in ArminGrotesk 600 at 24px, color #10284b. Then: body text in ArminGrotesk 400 at 16px, color #000000, line-height 1.50.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
