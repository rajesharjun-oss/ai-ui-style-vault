# AI Implementation Prompt

Build a LogoArchive-inspired interface using this source-derived style bundle.

Reference site: https://www.logo-archive.org
Theme: dark
Category: Design
North star: midnight gallery of iconic marks

Use these palette anchors:

- Canvas Charcoal `#27272a` for Page background, primary canvas surface
- Elevated Ink `#18181b` for Card surfaces, product window backgrounds, logo tiles - one step deeper than canvas for contrast
- Slate Surface `#343538` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Deep Void `#000000` for Nav fills, deepest surface tone, pure black accents
- Near Black `#0c0c0e` for List borders, hairline dividers, subtle structural edges
- Pure White `#ffffff` for Primary text, icons, borders, high-contrast elements - the dominant interface color
- Fog Gray `#a8afb7` for Muted body text, secondary headings, subtle borders - readable but recessive
- Mist Gray `#dadee4` for Light borders, disabled-state text, very subtle dividers
- Dim Stone `#8c8c8d` for Placeholder/disabled surfaces, inactive list backgrounds
- Signal Yellow `#fde533` for Yellow outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

Use these typography anchors:

- Suisse International `--font-suisse-international` for Primary typeface for all UI text, body, navigation, buttons, and most headings
- Suisse Works Book `--font-suisse-works-book` for Italic display emphasis in hero and section headlines

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary CTA Button: Main call-to-action for conversion (pricing, signup)
- Secondary Button: Secondary actions (pricing, learn more)
- Ghost Nav Button: Top-right utility actions (Log in)
- Feature Badge: Pill label above section headings (e.g., 'A new format of logo inspiration')
- Logo Tile Card: Individual logo display in the product grid
- Product Window Frame: Desktop app screenshot container
- Mobile Device Frame: Mobile app screenshot container
- Nav Bar: Top navigation, site-wide
- Hero Headline: Primary page headline
- Subtext Paragraph: Supporting copy below headlines or CTAs
- Pricing Card: Subscription tier display
- Feature List Row: Checklist item in pricing or feature sections

Do:

- Use #fde533 only for primary CTAs, badges, and the logo mark - never for body text, icons, or decorative elements
- Pair Suisse International roman (400) with italic (Suisse Works Book) for editorial emphasis in display copy
- Use 999px border-radius for all buttons, badges, and interactive pills
- Layer surfaces using the tonal stack: #000000 #0c0c0 #18181b #27272a #343538
- Set body text to #a8afb7 at 14-16px with 1.75 line-height for readable, recessive supporting copy
- Keep all borders 1px and use #27272a or #343538 - never thicker, never chromatic
- Center-align hero and section headlines; left-align body and list content

Avoid:

- Don't introduce a second accent color - the system is monochromatic with one yellow signal
- Don't use box-shadow for elevation - rely on tonal surface contrast only
- Don't use display sizes below 65px for headlines - the scale jumps from 28px to 65px intentionally
- Don't use system fonts or non-Swiss grotesques - the typographic identity is precise and mechanical
- Don't add gradients - the system is fully flat
- Don't use light-theme colors or white backgrounds - the system is dark-first
- Don't use borders thicker than 1px or with high contrast - borders are always hairline and subtle

Source prompt cues:

Quick Color Reference:
- background (canvas): #27272a
- elevated surface: #18181b
- primary text: #ffffff
- muted text: #a8afb7
- border: #27272a or #343538
- accent / primary action: #27272a (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #27272a background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Pricing card: Background #18181b, 1px #27272a border, 28px radius, 32px padding. Tier name at 24px weight 500 in #ffffff. Price at 65px weight 400 in #fde533. Feature list rows: 14px #ffffff text, 8px gap from checkmark icon, 4px vertical padding. CTA button at bottom: #fde533 filled pill.

3. Feature badge: Pill shape, 999px radius, 4px 8px padding, #fde533 background, #000000 text, 12px Suisse International weight 500. Centered above a section headline.

4. Logo grid tile: Background #18181b, 20px radius, 1px #27272a border, 32px padding. White logo icon centered. Arranged in a 6-column grid with 16px gaps.

5. Nav bar: Full-width, 64px height, background #000000 or transparent. White 'LA' monogram at far left, ghost pill button (1px #343538 border, #ffffff text, 999px radius) at far right.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
