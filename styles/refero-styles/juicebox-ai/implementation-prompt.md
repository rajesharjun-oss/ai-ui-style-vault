# AI Implementation Prompt

Build a Juicebox.ai-inspired interface using this source-derived style bundle.

Reference site: https://juicebox.ai
Theme: light
Category: SaaS
North star: Talent command center on cream paper

Use these palette anchors:

- Royal Plum `#6a2f8d` for Primary brand color - hero washes, product frames, active nav indicator, link accents, and decorative section bands. Carries 100% of the chromatic brand weight; the system is monochrome until this color appears
- Plum Mist `#eee8fd` for Tinted lilac surface used for soft product/section backgrounds and as the lightest stop in purple gradient washes. Pairs with Royal Plum to create a two-stop purple atmosphere without needing darker midtones
- Lilac Outline `#da9efd` for Decorative stroke accent - used sparingly on illustration outlines, diagram borders, and ornamental SVG marks that sit over plum surfaces
- Forest Mark `#2f8d6e` for Green outline accent for tags, dividers, and focused UI edges
- Obsidian `#1d161d` for Primary text and heading color. Slightly warm-tinted near-black that reads softer than pure #000 on cream backgrounds; the canonical ink for all reading content
- Graphite `#2a232a` for Primary action button background (dark filled CTA) and deep border color. The non-chromatic counterpart to Royal Plum - same near-black temperature, used wherever a button needs to feel grounded and serious
- Smoke `#574e57` for Secondary text, input borders, form labels, and muted UI chrome. The mid-neutral that carries the majority of metadata and helper copy
- Warm Gray `#786c78` for Muted body text, tag labels, and tertiary borders. Reads as a soft taupe on cream - used for de-emphasized prose and quiet UI labels
- Mist Gray `#a89ea8` for Disabled text, placeholder copy, and the lightest readable neutral. Used where content must recede but remain legible
- Hairline `#d9d9d9` for Default border color for cards, dividers, input fields, and table rows. The single hairline that draws almost every structural line on the site
- Parchment `#f8f6f8` for Page background canvas - a warm near-white with a barely-perceptible violet cast that ties the neutral surface to the Royal Plum accent without competing with it
- Paper `#ffffff` for Card and elevated surface background. Sits one step brighter than Parchment to create a subtle two-tier surface stack without using shadows
- Carbon `#000000` for Pure black reserved for SVG strokes, icon fills, and the deepest image borders. Not used for text or buttons - those live in the warmer Obsidian/Graphite family

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Roobert `--font-roobert` for Display and heading face - used exclusively for h1/h2 and section titles. Carries aggressive negative tracking (-0.04em at 64-72px) that tightens large headlines into compact, confident blocks. Its single weight (400) and neo-grotesque proportions give the system an editorial, not-marketing posture.
- Haas Grot Text Web (55 Roman + 65 Medium) `--font-haas-grot-text-web-55-roman-65-medium` for Body and UI text face - paragraph copy, button labels, nav items, captions, form fields. The 55 Roman at weight 400 handles body; 65 Medium at 500 covers labels and meta; 700 Bold appears in inline emphasis. Slightly negative tracking (-0.01em to -0.02em) keeps dense UI text feeling engineered rather than soft.
- DM Mono `--font-dm-mono` for Technical/label face - section index tags ([01] FEATURES), tab labels (SEARCH (PEOPLEGPT), INSIGHTS, ENGAGEMENT), and uppercase chip labels. Wide positive tracking (up to 0.077em) makes it read as a monospaced code label, not body copy. Used to mark engineering provenance on interface elements.
- Haas Grot Text Web 65 Medium `--font-haas-grot-text-web-65-medium` for Haas Grot Text Web 65 Medium - detected in extracted data but not described by AI
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI
- Neue Haas Grotesk Text `--font-neue-haas-grotesk-text` for Neue Haas Grotesk Text - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Filled Dark CTA: Primary action button - 'TRY FOR FREE', primary form submit
- Outlined Ghost Button: Secondary action button - 'BOOK A DEMO', nav actions
- Compact Pill Button: Announcement/eyebrow link - 'NEW TRY JUICEBOX AGENTS '
- Feature Tab Bar: Section navigation under 'How it works'
- Search Bar: Hero-aligned talent search input
- Customer Logo Strip: Social proof band - flexport, ramp, Verkada, samsara, Quora, CURSOR, Anyscale
- Section Index Tag: Eyebrow label above section headlines - '[01] FEATURES'
- Purple Product Frame: Product screenshot container on purple hero sections
- Product Card List: Talent results table inside the product frame
- Two-Column Feature Block: Standard feature section layout - product left, copy right
- Top Announcement Banner: Site-wide top bar with funding/product news
- Top Navigation: Primary site navigation

Do:

- Use #6a2f8d Royal Plum exclusively as a brand accent - hero washes, active states, product frames, the submit button on the search bar, and the announcement banner. Never use it for body text or for more than one element on a single screen.
- Set all display headlines (40-72px) in Roobert 400 with letter-spacing between -0.03em and -0.04em. The aggressive negative tracking is the signature - do not relax it.
- Use DM Mono with 0.077em tracking for every section eyebrow label, tab label, and technical tag. The mono face signals 'this is metadata, not prose'.
- Default to 2px border-radius on every interactive element - buttons, inputs, cards, tags, and product frames. Square edges are part of the system's engineering posture.
- Build the page surface stack in three tiers only: Parchment #f8f6f8 (page) Paper #ffffff (cards) Plum Mist #eee8fd (accented sections). Use surface lightness, not shadows, to imply elevation.
- Pair Filled Dark CTA (#2a232a) and Outlined Ghost Button (1px #1d161d border) at identical dimensions and padding so they read as a matched set side-by-side in every feature section.
- Set body copy at 14-18px in Haas Grot 400 with line-height 1.43-1.56 and tracking -0.01em. Never go below 14px or above 1.56 line-height for paragraph text.

Avoid:

- Don't use #000000 for text - use #1d161d Obsidian. Pure black fights the warm Parchment canvas and breaks the system's subtle violet undertone.
- Don't round corners above 2px. The system is intentionally rectangular; pills, 8px, or 12px radii immediately read as a different product.
- Don't introduce drop shadows on cards or sections. Elevation comes from the two-tier Parchment-to-Paper surface, not from box-shadow. The single inset shadow rgba(0,0,0,0.5) 0 0 12px inset is reserved for active/pressed button states only.
- Don't use Royal Plum #6a2f8d as a text color on white backgrounds. It fails contrast for body copy; reserve it for headings on Plum Mist, for buttons, and for decorative elements.
- Don't combine Roobert with a different display face, and don't set headlines at weight 700. The single 400 weight is the whole signature - bolding a headline breaks the editorial tone.
- Don't add new saturated colors. The palette is intentionally near-monochrome with one brand purple, one green emphasis, and one lilac outline. Introducing teal, red, or amber immediately dilutes the system.
- Don't use color for body text emphasis. Use Obsidian #1d161d bold for inline emphasis and the green #2f8d6 only for individual highlighted words, never for full sentences.

Source prompt cues:

**Quick Color Reference**
- text: #1d161d (Obsidian)
- background: #f8f6f8 (Parchment)
- border: #d9d9d9 (Hairline)
- accent: #6a2f8d (Royal Plum)
- muted text: #574e57 (Smoke)
- primary action: #6a2f8d (filled action)

**3 Example Component Prompts**

1. Create a Primary Action Button: #6a2f8d background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.


3. **Section Eyebrow + Tab Bar**: DM Mono 12px [01] FEATURES label in Smoke #574e57 with 0.077em tracking, 24px above the heading. Heading-lg 48px Roobert 400, Obsidian #1d161d, letter-spacing -1.44px. Below: 1px Hairline #d9d9d9 divider spanning the full content width, then a horizontal row of three DM Mono 12px uppercase tab labels (SEARCH (PEOPLEGPT), INSIGHTS, ENGAGEMENT) in Smoke #574e57, separated by 1px dividers, with a 2px Royal Plum #6a2f8d bottom border under the active tab.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
