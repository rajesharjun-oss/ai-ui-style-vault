# Monad - Design Reference

> Editorial tech journal on warm parchment: serif headlines, monospace functional text, pill controls,
> hairline borders, pastel gradient washes, and a data-pipeline diagram language.

## Theme

Monad feels like a technical manual typeset for a literary journal. The page canvas is warm parchment,
not pure white. Untitled Serif carries calm editorial hierarchy at weight 400, while ABC Diatype Mono
handles body copy, navigation, buttons, badges, tags, and every functional UI string.

The design should feel precise, technical, spacious, and slightly analog. Use Lake Blue for one primary
action per screen, keep the rest of the UI in warm grayscale, and reserve pastel colors for decorative
gradient washes and diagrams rather than normal UI fills.

## Core Visual Rules

- Use Parchment (`#f6f3f1`) as the page canvas.
- Use Untitled Serif weight 400 for all headings.
- Use ABC Diatype Mono for body copy and all functional UI text.
- Use Lake Blue (`#2b59d1`) for the single primary CTA only.
- Use Off-Black or ghost variants for secondary actions.
- Use `1px` Ash (`#cecac8`) borders for cards, dividers, and pipeline nodes.
- Use pill-shaped buttons and tags.
- Avoid drop shadows on cards; use borders and surface contrast.
- Keep pastel colors decorative-only unless a specific illustration needs them.

## Quick References

- **Canvas:** `#f6f3f1`
- **Text:** `#242424`
- **Secondary text:** `#4e4d4d`
- **Muted text:** `#797776`
- **Border:** `#cecac8`
- **Primary action:** `#2b59d1`
- **Colored card:** `#cfdaf5`
- **Page max width:** `1432px`
- **Section gap:** `64px`
- **Card padding:** `40px`
- **Element gap:** `16px`
- **Card radius:** `40px`
- **Button radius:** `100px`

## Implementation Notes

Start from `code/css-variables.css` or `code/tailwind-v4.css`. Build primitives for announcement bars,
Lake Blue primary pills, Off-Black secondary pills, ghost pills, text links, pipeline node tags, feature
cards, periwinkle elevated cards, FAQ accordion rows, logo strips, gradient atmospheric washes, and
centered typographic heroes.

For original work, keep the system logic but replace source-specific brand marks, screenshots, names,
copy, diagrams, and exact compositions.

