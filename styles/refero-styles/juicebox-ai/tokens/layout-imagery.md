# Layout & Imagery

## Layout

The page is a max-width 1200px centered column on a Parchment canvas, but hero sections break out to full-bleed Royal Plum washes that extend edge-to-edge. Each section follows a two-column pattern: product screenshot on the left (or full-bleed background), descriptive copy on the right with eyebrow chip heading body paired CTA buttons. Section gaps are 80px, generous enough to let each feature breathe. The hero is a centered single-column composition: announcement chip 72px display headline 18px body paragraph paired CTAs then a search bar floats over the purple field. The customer logo strip is a single horizontal row on a Parchment band, evenly spaced, no cards. The 'How it works' section uses a section index tag in mono, then a tab bar with three uppercase mono labels, then a full-width two-column feature block. Navigation is a single top bar - logo left, nav center, sign-in and CTAs right - with a thin announcement strip above it in Royal Plum. No sidebar, no mega-menu visible, no sticky behavior beyond the announcement.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Parchment | `#f8f6f8` | Base page canvas - the warmest neutral in the stack, carries a faint violet cast that connects to the brand purple |
| 1 | Paper | `#ffffff` | Card and elevated surface - sits one step brighter than the canvas, creates the primary surface distinction |
| 2 | Plum Mist | `#eee8fd` | Tinted lilac accent surface for feature blocks and product frame interiors; the lightest stop in the purple gradient family |
| 3 | Royal Plum | `#6a2f8d` | Full-bleed brand surface for hero washes, announcement banner, and product frame backgrounds |

## Elevation

The system avoids drop shadows entirely. Elevation is communicated through a four-tier surface lightness stack (Parchment Paper Plum Mist Royal Plum) and a 1px Hairline #d9d9d9 border that draws every structural line. The only shadow in the codebase is an inset rgba(0,0,0,0.5) 0 0 12px reserved for active/pressed button states - never used on cards, never used for floating panels. This keeps the interface feeling like a printed document on cream paper rather than a layered glass UI.

## Imagery

Imagery is minimal and product-led. The site uses no lifestyle photography, no stock imagery, and no decorative illustrations outside of SVG icons. The dominant visual element is product UI screenshots - talent search results, candidate cards, profile detail panels - placed inside Royal Plum #6a2f8d frames that bleed off the screen edge. These product frames are the 'hero image' equivalent: they prove the product works by showing it working. A subtle dot/grain texture overlays the purple hero backgrounds to add tactile depth without competing with the product UI. Customer logos appear as monochrome Smoke #574e57 marks on a Parchment band - social proof, not decoration. Icons throughout are 1px-stroke line icons in Obsidian, consistent stroke weight, no filled variants. The overall density is text-dominant with the product screenshot as the single visual punctuation per section.
