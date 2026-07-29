# AI Implementation Prompt

Build a Goodnotes-inspired interface using this source-derived style bundle.

Reference site: https://www.goodnotes.com
Theme: light
Category: Productivity
North star: Paper-white command canvas - a blank notebook page where every tool snap into place without decoration.

Use these palette anchors:

- Pure Canvas `#ffffff` for Page background, card backgrounds, button text on cyan CTA
- Midnight Ink `#000000` for Primary headlines, body text, borders on UI chrome
- Deep Charcoal `#1e1e1e` for Ghost button text and borders, secondary headings, icon strokes
- Graphite `#111213` for Dark nav backgrounds, dark section surfaces, link text in dark contexts
- Slate `#565656` for Body copy on cards, secondary descriptive text
- Fog `#888889` for Muted helper text, captions, de-emphasised labels
- Ash `#666666` for Tertiary text, subtle UI labels
- Steel `#333333` for Badge text, mid-weight secondary content
- Border Medium `#e8e8e8` for Tab underlines, nav separators, light hairline dividers
- Border Soft `#bebebe` for Card outlines, modal borders, container edges
- Aqua Spark `#57d2ee` for Blue action color for filled buttons, selected navigation states, and focused conversion moments.
- Teal Deep `#45bfdb` for Brand surface wash, teal background sections
- Cyan Mist `#bcedf8` for Outlined button borders, soft teal ring accents
- Cyan Text `#6dd9f2` for Blue outline accent for tags, dividers, and focused UI edges.
- Sky Link `#0299e0` for Hyperlinks and underline accents in body copy
- Highlighter Yellow `#f2e6b3` for Text highlight wash - mimics physical highlighter pen on note-taking UI screenshots

Use these typography anchors:

- Roobert `--font-roobert` for Single-font system - every piece of UI copy, from 10px captions to 48px hero headlines, is Roobert. The rounded geometric forms mirror the tablet/handwriting brand; weight 700 at 48px with -0.05em tracking creates dense, close-set display text that reads like a confident pencil stroke rather than a digital shout.
- Font Awesome 6 Brands `--font-font-awesome-6-brands` for Social/brand icon glyph set used in badges and footer; monochromatic, no resizing

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button (Aqua Fill): Main conversion action - "Start Free"
- Ghost Navigation Button: Dropdown triggers in top navigation (Product, Built For, Resources)
- Teal Tinted Feature Button: Tab or section-switch controls within feature sections
- White Content Card: Feature and benefit cards in grid sections
- Tab Navigation Strip: In-page content switcher (Whiteboard / PDF Annotation / Documents / Notebooks)
- Product UI Screenshot Card: Product showcase: embedded screenshot of the Goodnotes app interface
- Logo Marquee Strip: Social-proof partner/customer logos in horizontal scrolling ticker
- Highlighter Text Accent: Inline emphasis within body copy, mimicking physical highlighter pen
- "Learn More" Text Link: Secondary navigation within feature sections
- Section Heading Block: Top of each page section - centered or left-aligned headline + subtext

Do:

- Use #57d2ee exclusively for the primary filled CTA button - no other UI element should share this fill color, keeping it as the sole chromatic action signal.
- Apply Roobert at weight 700 with letter-spacing -0.05em (-2.4px) for all 48px display headlines; tighten tracking proportionally down the scale to -0.016em at 20-22px.
- Define card and container edges with 0.5-1px solid #bebebe or #e8e8e8 borders - never use box-shadow for surface elevation.
- Use 10px border-radius universally across buttons, cards, inputs, and UI chrome; reserve 4px only for focus/link rings.
- Keep body copy at #565656 or #666666 on white cards - reserve #000000 for headings and primary labels only.
- Use #f2e6b3 as an inline background highlight on emphasized text spans - apply it flat (no radius) to mirror a physical highlighter stroke.
- Separate section content with 80px vertical gaps on desktop; use 24px element gap within card grids and between grouped UI elements.

Avoid:

- Never add box-shadow to cards, modals, or buttons - all surface separation must come from borders, not elevation.
- Never use a second chromatic fill color for buttons; ghost (#1e1e1 border) and tinted-teal (rgba(87,210,238,0.1)) variants must stay visually subordinate to the cyan CTA.
- Never set headline letter-spacing to 0 or positive values at sizes above 24px - the negative tracking is the signature of the display voice.
- Never substitute a different typeface for Roobert; if the custom font fails to load, fall back to Plus Jakarta Sans or DM Sans - not Inter or system-ui.
- Never use #0299e0 (Sky Link) as a button fill or a section color - it is reserved for inline hyperlinks and "Learn more" text in white-background contexts only.
- Never apply the teal tinted button (rgba(87,210,238,0.1)) with a border-radius - it is a 0px radius tab control, not a pill or rounded button.
- Never center-align body copy paragraphs beyond 600px width - long centered text breaks readability; left-align body text in two-column feature sections.

Source prompt cues:

**Quick Color Reference**
- text (primary): #000000
- text (secondary): #565656
- background: #ffffff
- border: #bebebe (cards), #e8e8e8 (dividers/tabs)
- accent / brand: #57d2ee
- primary action: #57d2ee (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #57d2ee background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **White Feature Card**: Background #ffffff, border 1px solid #bebebe, border-radius 10px, padding 24px. Card title: Roobert 600, 22px, #000000, letter-spacing -0.35px. Body: Roobert 400, 16px, #565656, line-height 1.4. "Learn more " link: #0299e0, Roobert 500, 14px.

3. **Tab Navigation Strip**: Full-width strip, border-bottom 1px solid #e8e8e8, no radius. Active tab: Roobert 600, 16px, #000000, border-bottom 2px solid #000000, padding 10px 20px. Inactive: Roobert 400, 16px, #666666, padding 10px 20px.

4. **Ghost Nav Button**: Background transparent, text #1e1e1e, border 1px solid #1e1e1e, border-radius 10px, padding 10px 12px, Roobert 400, 15px. Used for dropdown triggers - no fill, no shadow.

5. **Section Heading Block**: Roobert 700, 40px, #000000, letter-spacing -1.68px, line-height 1.11, centered. Below it: Roobert 400, 18px, #666666, line-height 1.4, centered, max-width 560px. Vertical gap between heading and subtext: 16px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
