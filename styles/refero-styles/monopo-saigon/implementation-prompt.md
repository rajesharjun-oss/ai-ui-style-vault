# AI Implementation Prompt

Build a polished UI in the monopo saigon style.

Use a monochrome editorial gallery system with one full-viewport iridescent hero media moment. The interface itself must stay black, white, and gray. Do not invent colored buttons, badges, links, charts, or cards.

Typography:

- Use Roobert-style type for nearly everything.
- Use display headlines up to 225px, weight 400.
- Use atmospheric section headlines around 78px, weight 300.
- Use Roobert 11px to 18px for nav, labels, project titles, and body UI.
- Use Raleway only as a rare 54px heading accent.
- Use system-ui only for micro labels and cookie copy.

Layout:

- Use a centered 1078px max-width container.
- Use a full-viewport hero with one enormous centered headline over iridescent liquid media.
- Keep top navigation transparent and minimal: wordmark left, locale center, menu right.
- Use asymmetric editorial sections after the hero.
- Use full-width project list rows, not card grids.
- Keep the footer compact with muted address blocks.

Components:

- Dark ghost pill button: transparent fill, translucent white border, white text, 75px radius, Roobert 16px.
- Light ghost pill button: transparent fill, black border, black text, 75px radius, Roobert 16px.
- Filled neutral pill: `#636363` fill, white text, white border, 75px radius, only for consent or utility actions.
- Text links: no underline, no background, 0px radius.
- Project rows: sharp image, no card surface, no shadow, title below.

Strict rules:

- Do not introduce chromatic UI colors.
- Do not use shadows or elevation.
- Do not use rounded cards, rounded images, or rounded inputs.
- Do not use gradients outside the hero media.
- Do not use radii between 1px and 74px.
- Do not make motion fast. Use `cubic-bezier(0.19, 1, 0.22, 1)` for 0.8s to 1.25s transitions.
