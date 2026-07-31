# AI Implementation Prompt

Build a Duolingo-inspired interface using this source-derived style bundle.

Reference site: https://www.duolingo.com
Theme: light
Category: SaaS
North star: Green playground with thick marker outlines

Use these palette anchors:

- Ecto Green `#58cc02` for Green outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Lingot Lime `#a5ed6e` for Outlined-action border and link accent - used as the chromatic border on link and button elements in 256+ instances. The lighter green outline gives interactive elements a glowing, highlighter-pen quality against white backgrounds
- Eel Light `#d7ffb8` for Soft highlight and pale border - lightest green used for card outlines, soft surface washes, and the bottom shadow border on filled green buttons to create a 3D pressable effect
- Macaw Blue `#1cb0f6` for Secondary action accent - body borders, link text, and outlined button borders for secondary actions like language-specific CTAs. The cyan-blue sibling to the green system, signaling alternative or complementary actions
- Eel Dark Blue `#042c60` for Deep heading text and border - navy blue used for emphasis headings and key border treatments, providing weight and contrast without competing with the green primary
- Midnight `#000437` for Dark surface and button text - near-black violet used for dark-surface sections and as button label text on green fills
- Graphite `#3c3c3c` for Dominant neutral border - the workhorse gray used for hundreds of list and card borders throughout navigation, lists, and structural dividers. Not a background, a border system
- Ash `#777777` for Secondary text and nav borders - medium gray for navigation chrome, secondary text labels, and subtle structural borders
- Charcoal `#4b4b4b` for Body text and icon borders - darker gray for body copy and icon outlines, sitting between the lighter Ash and the darker structural Graphite
- Paper `#ffffff` for Page and card surface - the white canvas on which all content sits. Also used as text on dark surfaces and as border color for ghost buttons
- Ink `#000000` for Pure black for SVG illustration fills and maximum-contrast text where needed

Use these typography anchors:

- din-round `--font-din-round` for Primary UI typeface - used for body text, navigation, buttons, links, lists, and smaller headings. The rounded terminals and friendly weight create an approachable, educational tone. Weight 500 for body, weight 700 for emphasis and button labels. The +0.053em letter-spacing is wider than typical, giving text a breezy, open feel.
- feather `--font-feather` for Display face for large feature headlines - bold, heavy, and tight (letter-spacing: -0.02em). Reserved exclusively for oversized section headlines. The extreme weight contrast against the lighter din-round body creates a shout/whisper rhythm: feather headlines announce, din-round explains.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 100px.
- Card padding: 16-24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary Filled Button: Main call-to-action (Get Started, Start Learning)
- Ghost/Outlined Secondary Button: Secondary action (I Already Have An Account, Certify Your English)
- Lingot Outlined Link: Inline text links and nav links throughout content
- Language Selector Pill: Language/course picker in footer and nav
- Section Heading Block: Large feature section headers
- Top Navigation Bar: Sticky header with logo and language switcher
- Feature Illustration Panel: Large character illustrations accompanying feature sections
- Hero CTA Stack: Primary action area on landing page
- Course/Language Grid: Grid of language options with flags
- List/Table Row: Structured data rows in tables and lists
- Feature Section Block: Alternating text + illustration sections

Do:

- Use #58cc02 as the filled background for all primary action buttons and as the color for large display headings
- Use #a5ed6 as the 2px border color for outlined/ghost links and secondary buttons - this lighter green outline is the system's most distinctive repeated element
- Set border-radius to 12px on all buttons, links, and pills - this is the only radius in the system
- Use feather at 48-64px weight 700 with -0.02em letter-spacing for section headlines, and din-round for everything else
- Add a 2-3px solid bottom border in a darker shade to green filled buttons to create the pressable 3D effect - never use box-shadow
- Use the wide letter-spacing of ~0.053em on all din-round text - the open, airy tracking is part of the brand voice
- Pair every feature section with a flat cartoon illustration - the system expects character art as a content element, not decoration

Avoid:

- Do not use drop shadows on any element - depth comes from solid borders, never from blurred shadow stacks
- Do not use gradients - the system is strictly flat solid colors with no gradient transitions
- Do not use card containers with background fills or box-shadows - sections are separated by white space alone
- Do not set body radius below or above 12px - the system has exactly one radius value and it should be used uniformly
- Do not use feather for body text or anything under 32px - it is exclusively a display face for oversized headlines
- Do not introduce new accent colors outside the established palette of green, blue, dark blue, and midnight
- Do not use the light green #a5ed6 as a filled background - it is exclusively a border/outline color

Source prompt cues:

**Quick Color Reference**
- text: #3c3c3c (primary), #777777 (secondary), #4b4b4b (body)
- Create an Outlined Primary Action: Transparent background, #a5ed6e border and text, 9999px radius, compact pill padding. Use it for the main CTA instead of a filled button.
- border: #3c3c3c (structural), #a5ed6e (outlined action border), #1cb0f6 (secondary action border)
- accent: #1cb0f6 (blue secondary)
- primary action: #a5ed6e (outlined action border)

**Example Component Prompts**
1. Create a ghost outlined button: white background, 2px border in #a5ed6e, label text in #a5ed6e at 15px din-round weight 700, 12px radius, 16px vertical and 24px horizontal padding. No shadow, no fill - the border IS the visual identity.

2. Create a section heading: text in feather weight 700 at 48px, letter-spacing -0.02em, color #58cc02. No background, sits directly on white with 100px vertical space above and below.

3. Create a language selector pill: white background, 12px radius, 10px vertical and 16px horizontal padding. Left side: flag emoji. Right side: language name in din-round weight 700 at 13px, uppercase, color #4b4b4b. Subtle 1px border in #e5e5e5.

4. Create a feature section: two-column layout, left column has a headline in din-round weight 700 at 32px color #042c60 with 0.053em letter-spacing, plus a body paragraph in din-round weight 500 at 15px color #4b4b4b. Right column has a full-color flat cartoon illustration. 100px vertical gap between this section and the next.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
