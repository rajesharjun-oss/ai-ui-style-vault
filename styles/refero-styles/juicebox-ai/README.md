# Juicebox.ai

Source: [Refero Style](https://styles.refero.design/style/2186dddd-60ee-4898-b11d-88483daf477e) 
Reference site: [https://juicebox.ai](https://juicebox.ai) 
Captured: 2026-07-29 
Refero published: 2026-05-07T22:37:37.205Z 
Refero modified: 2026-06-03T22:07:16.832Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Juicebox.ai's light SaaS design system: Royal Plum #6a2f8d, Plum Mist #eee8fd colors, sans-serif, Roobert typography, and DESIGN.md for AI agents.

North star: Talent command center on cream paper

## What To Borrow

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

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Roobert `--font-roobert` for Display and heading face - used exclusively for h1/h2 and section titles. Carries aggressive negative tracking (-0.04em at 64-72px) that tightens large headlines into compact, confident blocks. Its single weight (400) and neo-grotesque proportions give the system an editorial, not-marketing posture.
- Haas Grot Text Web (55 Roman + 65 Medium) `--font-haas-grot-text-web-55-roman-65-medium` for Body and UI text face - paragraph copy, button labels, nav items, captions, form fields. The 55 Roman at weight 400 handles body; 65 Medium at 500 covers labels and meta; 700 Bold appears in inline emphasis. Slightly negative tracking (-0.01em to -0.02em) keeps dense UI text feeling engineered rather than soft.
- DM Mono `--font-dm-mono` for Technical/label face - section index tags ([01] FEATURES), tab labels (SEARCH (PEOPLEGPT), INSIGHTS, ENGAGEMENT), and uppercase chip labels. Wide positive tracking (up to 0.077em) makes it read as a monospaced code label, not body copy. Used to mark engineering provenance on interface elements.
- Haas Grot Text Web 65 Medium `--font-haas-grot-text-web-65-medium` for Haas Grot Text Web 65 Medium - detected in extracted data but not described by AI
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI
- Neue Haas Grotesk Text `--font-neue-haas-grotesk-text` for Neue Haas Grotesk Text - detected in extracted data but not described by AI

## Avoid

- Don't use #000000 for text - use #1d161d Obsidian. Pure black fights the warm Parchment canvas and breaks the system's subtle violet undertone.
- Don't round corners above 2px. The system is intentionally rectangular; pills, 8px, or 12px radii immediately read as a different product.
- Don't introduce drop shadows on cards or sections. Elevation comes from the two-tier Parchment-to-Paper surface, not from box-shadow. The single inset shadow rgba(0,0,0,0.5) 0 0 12px inset is reserved for active/pressed button states only.
- Don't use Royal Plum #6a2f8d as a text color on white backgrounds. It fails contrast for body copy; reserve it for headings on Plum Mist, for buttons, and for decorative elements.
- Don't combine Roobert with a different display face, and don't set headlines at weight 700. The single 400 weight is the whole signature - bolding a headline breaks the editorial tone.
- Don't add new saturated colors. The palette is intentionally near-monochrome with one brand purple, one green emphasis, and one lilac outline. Introducing teal, red, or amber immediately dilutes the system.
- Don't use color for body text emphasis. Use Obsidian #1d161d bold for inline emphasis and the green #2f8d6 only for individual highlighted words, never for full sentences.

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
