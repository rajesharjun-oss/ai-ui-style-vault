# AI Implementation Prompt

Build a Toggl Track-inspired interface using this source-derived style bundle.

Reference site: https://toggl.com
Theme: mixed
Category: Productivity
North star: Plum theater marquee - a deep aubergine stage where a single magenta spotlight word illuminates each headline.

Use these palette anchors:

- Plum `#2c1338` for Hero, header, and footer canvases; brand mark background. Near-black aubergine that reads as the brand's signature dark
- Heather `#412a4c` for Primary headings and UI text on light surfaces; secondary dark surface when Plum is too heavy. The workhorse purple
- Magenta `#e57cd8` for Filled CTA buttons, emphasis words inside headlines, selected nav state, star ratings, and decorative dots. The only vivid hue - rationed to one word or one control per screen
- Lavender Smoke `#564260` for Body copy and link text on warm-white surfaces where Heather would feel too heavy. Carries the brand tint into running text
- Dusty Mauve `#6b5a74` for Secondary body text, descriptions, helper text, and muted icon strokes on light surfaces. Desaturated enough to recede behind headings
- Stone Violet `#817187` for Borders and dividers on light surfaces; button borders for outlined variants; disabled or placeholder text
- Ink `#000000` for Primary text and high-contrast borders on light surfaces; footer text on dark Plum
- Bone `#fefbfa` for Page background for all content sections, card surfaces, and text color on dark Plum headers
- Silver `#d5d0d7` for Hairline borders, list separators, and input outlines across cards and tables. The structural neutral grid
- Fog `#c0b8c3` for Subtle borders and dividers where Silver reads too dark; secondary placeholder text on inputs
- Blush `#fdeae2` for Soft warm wash for icon fills, decorative card backgrounds, and nav hover states. The warmest surface tint
- Petal `#fcf1f8` for Elevated card and modal surfaces above Bone. Carries a pink whisper without competing with Magenta
- Orchid Mist `#fae5f7` for Highlighted card background for featured or selected content blocks
- Bubblegum Wash `#f7d8f3` for Pale pink surface for secondary buttons, tag backgrounds, and the softest brand-tinted fill
- Amber `#ffde91` for Yellow action color for filled buttons, selected navigation states, and focused conversion moments.

Use these typography anchors:

- Inter `--font-inter` for All body copy, navigation links, UI labels, table data, and secondary headings. Inter's neutrality keeps the content calm while GT Haptik performs on the headlines. Weight 500 for nav and buttons, 700 for subheadings, 800 for compact stat callouts.
- GT Haptik `--font-gt-haptik` for Display headlines and large section titles. GT Haptik's geometric warmth with rounded terminals gives the brand a friendly, non-corporate voice; weight 700 at 43-69px with tight 1.1 line-height creates dense, confident heroes. Substitute: Inter Tight, Manrope, or Outfit.
- GT Haptik Rotalic `--font-gt-haptik-rotalic` for The single highlighted word inside every hero and section headline - rendered in Magenta (#e57cd8) with a right-leaning italic slant. This is the brand's theatrical signature: one word per headline gets the spotlight. Substitute: Inter Tight Italic with manual skew, or Manrope Italic.
- GT Haptik Medium Rotalic `--font-gt-haptik-medium-rotalic` for GT Haptik Medium Rotalic - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 75px.
- Card padding: 30px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Filled Button (Magenta): Main call-to-action for hero and section CTAs
- Ghost Button (Outlined on Dark): Secondary action on Plum hero bands
- Try-for-Free Pill Button: Persistent top-right nav CTA
- Nav Link (Header): Primary navigation items
- Feature Card (Bone): Content cards in feature grids and product showcases
- Highlighted Feature Card (Petal): Elevated or selected feature card
- Pill Tag / Tab: Filter pills, tab selectors, category tags
- Star Rating Badge: Social proof and review aggregates
- Mega Menu Panel: Product and Solutions dropdown navigation
- Data Table Card: Product UI preview - time entries, reports
- Calendar Week Card: Calendar view product UI preview
- Integration Icon Cluster: Social proof for 100+ integrations

Do:

- Render every hero or section headline with exactly one Magenta emphasis word set in GT Haptik Rotalic - this is the brand's signature move.
- Use 26px border-radius for all primary action buttons and nav controls; reserve 200px for pills, tags, and trial CTAs only.
- Set display sizes (43px+) with line-height at or below 1.2 - the tight leading makes GT Haptik feel dense and confident.
- Build depth through Plum-to-Bone band contrast, not shadows. Cards get 1px Silver borders on Bone surfaces.
- Use Inter for everything below the fold: body, labels, table cells, nav. Reserve GT Haptik for display and section headlines.
- Keep the page on Bone (#fefbfa) for content sections and Plum (#2c1338) for hero/header/footer - these are the only two canvas colors.
- Ration Magenta to one element per screen: a CTA, an emphasis word, a selected state, or a decorative dot. Never two.

Avoid:

- Don't use drop shadows on cards, buttons, or modals - the design language is flat with surface tint contrast instead.
- Don't set the pink emphasis word in upright GT Haptik - it must be in the Rotalic variant to carry the theatrical meaning.
- Don't use Magenta as a background wash, gradient, or large surface fill. It only appears on filled buttons, emphasis words, and small dots.
- Don't introduce a second accent hue. The system is monochromatic purple with one spotlight pink - adding teal, green, or orange breaks the duotone.
- Don't use pure white (#ffffff) for backgrounds - Bone (#fefbfa) is the canvas. Pure white reads as cold and unbranded against the warm tints.
- Don't apply corner radii smaller than 10px or larger than 200px. The system has three: 10px (cards/inputs), 26px (buttons), 200px (pills).
- Don't set display headlines above 1.25 line-height - loose leading makes GT Haptik feel airy and undermines the dense, confident voice.

Source prompt cues:

**Quick Color Reference**
- text (primary on light): #000000
- text (on dark Plum): #fefbfa
- text (muted/body on light): #6b5a74
- text (headings on light): #412a4c
- background (light canvas): #fefbfa
- background (dark stage): #2c1338
- border (hairline): #d5d0d7
- accent / emphasis: #e57cd8 (Magenta)
- primary action: #e57cd8 (filled action)

**3 Example Component Prompts**

1. Create a Primary Action Button: #e57cd8 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Feature card grid:* Three cards on #fefbfa background, 30px padding, 10px border-radius, 1px #d5d0d7 border. Each card has a 40px Blush (#fdeae2) icon circle with a monochrome outline icon, then Inter weight 700 at 22px #412a4c heading, then Inter weight 400 at 16px #6b5a74 body text, with 15px vertical gap between elements.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
