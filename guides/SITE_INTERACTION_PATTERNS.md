# Site Interaction Patterns

Use this guide when a website needs richer navigation or a stronger first screen than a static hero. These patterns were added from observed public website behavior and user-provided screenshots, then generalized for original vault-led builds.

For landing pages, animated product tours, cinematic heroes, scroll stories, or motion graphics websites, also run `scripts/select-motion-references.ps1` and read `motion/LANDING_PAGE_MOTION_GUIDE.md` before implementation.

## Pattern: Rotating Editorial Hero

Use when:

- The product is visual: retail, food, travel, venue, event, real estate, wellness, portfolio, luxury services, or hospitality.
- Multiple offers or categories need first-viewport exposure without building separate hero sections.
- The brand has strong image assets or can provide a small set of rights-cleared images.

Build:

- A full-bleed image or video stage with 2 to 5 hero slides.
- One stable headline block that updates with the active slide.
- A visible progress state: dots, counters, thumbnails, or a small rail.
- Manual controls for previous, next, and pause when autoplay exists.
- A CTA that stays visually consistent across slides.

Implementation notes:

- Use `object-fit: cover` and stable hero dimensions so image changes do not shift layout.
- Preload the next slide only; do not load a huge carousel upfront.
- Respect `prefers-reduced-motion`; disable autoplay or reduce transition duration.
- Keep overlay contrast strong enough for text on every slide.
- Do not use external protected images from the reference site. Use owned, licensed, generated, or user-provided media.

Good adaptations:

- Wedding site: couple portrait, ceremony venue, family moment, reception preview.
- Restaurant site: dining room, signature plate, private dining, chef moment.
- Product showroom: category lifestyle scenes, featured brand edit, consultation CTA.
- SaaS launch: product state screenshots, customer workflow scenes, feature spotlight.

Avoid:

- Long autoplay loops with no user control.
- Text jumping to different positions on each slide.
- Crops that hide the product or person on mobile.
- Over-darkening all images until the hero becomes generic.

## Pattern: Product Taxonomy Mega Menu

Use when:

- A site has enough categories that a simple dropdown becomes cramped.
- Users need to browse by product family, use case, or department.
- Search and discovery are core to conversion.

Build:

- A full-width panel under the top nav.
- 3 to 5 taxonomy columns with clear headings.
- Simple text links for dense category lists.
- A visible active nav indicator, such as a small caret, underline, or top notch.

Example structure:

- Kitchen: hoods, hobs, ovens, microwaves, warming drawers, sinks and taps, dishwashers.
- Cooling: refrigeration, wine coolers, beverage coolers.
- Laundry: washing machines, dryers, washer-dryers.

Implementation notes:

- Keep column spacing predictable and use vertical dividers only when they improve scanning.
- Make the menu keyboard reachable: open on focus/Enter, close on Escape, support Tab order.
- On mobile, convert columns to accordion sections or a drill-down drawer.
- Highlight links with text weight or underline, not noisy cards.

## Pattern: Brand Logo Mega Menu

Use when:

- A retailer, marketplace, agency, or directory needs brand discovery.
- Brand recognition matters more than category copy.

Build:

- A spacious panel with a grid of monochrome or subdued logos.
- Consistent logo boxes or optical alignment so mismatched source logos do not look chaotic.
- Optional filters for category, region, price tier, or availability when the brand set is large.

Implementation notes:

- Use permission-cleared logos only.
- If logos are unavailable or licensing is unclear, use text brand names in a quiet grid.
- Provide accessible text labels for every logo link.
- Avoid letting logos dominate the entire visual system unless the page is specifically a brand directory.

## Pattern: Split Utility Mega Menu

Use when:

- The menu combines informational navigation with a featured action.
- The site needs About, Store, Support, Social, or Contact menus.

Build:

- A split panel: text links on one side, featured card/image/CTA in the middle, contact or social actions on the other side.
- One primary action, such as `Go to store`, `Book consultation`, `Start brief`, or `Contact us`.
- A calm divider system that separates content groups without feeling like a dashboard.

Implementation notes:

- Keep the featured image optional and replaceable.
- Use real button semantics for actions and real links for navigation.
- Do not trap focus in the menu unless it behaves like a modal drawer.
- Close the menu when users click outside, press Escape, or choose a link.

## Pattern: Icon Category Drawer

Use when:

- Categories are visual and compact enough to scan as icons.
- The user is already in a shopping, catalog, booking, or filtering mindset.

Build:

- A left rail for top-level menu groups such as `Shop all`, `Shop by categories`, `FAQs`.
- A right grid of icons with category labels.
- Stable grid cells with consistent icon sizes and text wrapping.

Implementation notes:

- Use a proven icon library when possible.
- Do not use decorative icons without text labels.
- Keep labels short, but allow two lines for long category names.
- On mobile, use a single-column list with icons, labels, and optional counts.

## Pattern Selection

| Site Need | Prefer |
|---|---|
| Strong visual first impression | Rotating Editorial Hero |
| Many product families | Product Taxonomy Mega Menu |
| Brand-led retail or marketplace | Brand Logo Mega Menu |
| About/support/store navigation | Split Utility Mega Menu |
| Shopping category browsing | Icon Category Drawer |

## QA Checklist

- Hero images change without layout shift.
- All dropdowns work with keyboard, pointer, touch, and Escape.
- Menus do not cover page headings, forms, or important CTAs in an unusable way.
- Mobile menu has its own layout, not a squeezed desktop panel.
- Text fits inside buttons, links, and category cells.
- Active menu state is visible.
- Images and logos are owned, licensed, generated, or user-provided.
- The final implementation is adapted to the target product rather than copied from the reference.
