# AI Implementation Prompt

Build a Incommonwith-inspired interface using this source-derived style bundle.

Reference site: https://www.incommonwith.com
Theme: light
Category: E-commerce
North star: Editorial atelier in oxblood ink - warm cream pages, sunlit interior photography, and a single deep burgundy ink that carries every word, border, and link like fine letterpress.

Use these palette anchors:

- Oxblood Ink `#4a0a05` for All body text, headings, links, borders, outlined actions, and footer type - the singular chromatic voice; warmth and gravity without aggression
- Cream Paper `#fafaf9` for Primary page background; the warm off-white that gives the site its paper-stock feel
- Aged Linen `#f8f7f1` for Secondary surface, subtle card backgrounds, and pill-tag fills - slightly greener/warmer than the page, used for soft differentiation
- Warm Stone `#bcb6a6` for Muted background wash and tertiary surface - the only mid-tone neutral, used sparingly for section backgrounds
- Dusty Clay `#a2827f` for Muted captions, helper text, and de-emphasized UI labels. Do not promote it to the primary CTA color

Use these typography anchors:

- Mier A `--font-mier-a` for Primary UI and body sans - used for navigation, body copy, captions, dates, links, and all functional text. Weight 400 only; the system trusts size and color contrast to carry hierarchy, never weight. Substitute: Inter or Untitled Sans (free: Inter).
- Caslon Ionic `--font-caslon-ionic` for Sole serif - reserved exclusively for category names, journal headlines, and brand wordmark at 24px. The single appearance of a classical letterform creates a literary counterpoint to the neo-grotesque UI. Substitute: Cormorant Garamond or Libre Caslon Text.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 0px.
- Element gap: 12px.

Build these component patterns where relevant:

- Editorial Top Navigation: Primary site navigation
- Full-Bleed Hero with Overlaid Headline: Landing page hero
- Product Category Card: Catalog category tile
- Journal Editorial Card: Editorial/press content card
- Text Link / Outlined Action: Primary interactive element
- Sidebar Section Label: Section identifier
- Horizontal Scroll Carousel: Product category browser
- Section Divider: Vertical rhythm separator
- Pill Tag: Category or filter label
- Multi-Column Footer: Site footer with contact and navigation

Do:

- Use #4a0a05 oxblood for all text, borders, and links - it is the only chromatic color and must carry every word, rule, and interactive element
- Pair Caslon Ionic serif at 24px for category names, journal headlines, and the wordmark with Mier A sans at 13-18px for all body, nav, and UI text
- Let photography fill its container edge-to-edge with 0px border-radius and 0px padding - images are full-bleed, never framed or rounded
- Use 12px gaps in navigation rows and between related elements; 64px between major sections to let photography breathe
- Set page backgrounds to #fafaf9 warm cream - never pure #ffffff; the warm off-white is essential to the paper-stock feel
- Use horizontal scroll carousels with small arrow controls for product categories rather than paginated grids or filters
- Date-stamp journal cards with small sidebar labels in a separate column, not badges or pills overlaid on images

Avoid:

- Don't use filled colored buttons - the system is entirely text-link driven; an outlined/underlined text link in #4a0a05 is the only action style
- Don't apply border-radius to images, cards, or panels - only pill tags at 9999px may be rounded; everything else is sharp
- Don't use drop shadows for elevation - depth comes from photography and warm color temperature, never from box-shadow
- Don't use pure white (#ffffff) backgrounds - always use #fafaf9 or #f8f7f1; the warmth is the brand
- Don't introduce accent colors beyond oxblood - the palette is intentionally narrow; adding blue, green, or other hues breaks the editorial coherence
- Don't use system fonts or substitute the Caslon/Mier pairing - the serif-sans tension is the brand's typographic identity
- Don't center-align body text or use large display headlines - the system is left-aligned and restrained; headlines are 24px, not 48px+

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
