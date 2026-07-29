# Linear

Source: https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1

Product/site reference: https://linear.app

## Snapshot

- **Mood:** Midnight precision instrument for modern software teams.
- **Theme:** Dark, compact, engineering-grade, product-led.
- **Core grammar:** Near-black surfaces, paper-white type, acid-lime primary action, 0.5px hairline borders, tight Inter Variable typography, Berkeley Mono metadata.
- **Best for:** Developer tools, issue trackers, AI agent workspaces, project management products, command centers, engineering dashboards.

Linear is a dark product system that treats the interface like a precision tool. The page sits on a `#08090a` void canvas, cards rise one step through `#0f1011` and `#161718`, and almost every boundary is a quiet graphite hairline. The single chromatic UI action is acid lime `#e4f222`.

## Folder Map

- `DESIGN.md` - style summary and implementation guidance.
- `implementation-prompt.md` - prompt for an AI agent building in this direction.
- `source.md` - source link and capture notes.
- `tokens/` - markdown design tokens by category.
- `code/css-variables.css` - reusable CSS custom properties and example classes.
- `code/tailwind-v4.css` - Tailwind v4 theme variables and component helpers.
- `code/design-tokens.json` - structured tokens for AI/code ingestion.
- `screenshots/README.md` - screenshot capture notes.

## Fast Build Notes

- Use `#08090a` as the full-page canvas.
- Use `#0f1011` for cards and nav surfaces.
- Use `#161718` for deeper elevated panels.
- Use `#23252a` for borders, dividers, and ghost outlines.
- Use `#e4f222` only for the primary CTA and active UI indicators.
- Use Inter Variable for UI, body, nav, and headings.
- Use Berkeley Mono only for issue IDs, shortcuts, and technical metadata.
- Keep buttons at 6px radius and cards at 12px max.
