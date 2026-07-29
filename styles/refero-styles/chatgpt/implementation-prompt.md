# Implementation Prompt

Build a restrained achromatic chat/productivity interface inspired by the ChatGPT Refero style system.

Use a Sidebar Mist left rail, Pure White conversation canvas, system UI typography, Graphite Ink text, compact 6px spacing, 10px rounded controls, and hairline borders. The written content should be the visual center; every control should recede until it is needed.

## Required Style Decisions

- Sidebar background: Sidebar Mist `#f9f9f9`.
- Main canvas: Pure White `#ffffff`.
- Primary text and icons: Graphite Ink `#0d0d0d`.
- Secondary text: Mid Ash `#5d5d5d`.
- Muted helper text: Hollow `#8f8f8f`.
- Borders: Hairline `#0000001a`.
- Hover wash: Hover Veil `#0000000d`.
- Tooltip/pressed surfaces: Ink Press `#000000`.
- Modal scrim: Deep Charcoal `#00000080`.
- No chromatic accent colors.
- No shadows.
- No custom webfonts.

## Typography Direction

Use the system font stack only:

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

Use 16px body text with 1.5 line height, 14px captions with 1.43 line height, and 24px weight 600 only for welcome headings.

## Layout Direction

Create:

- A 260px to 280px Sidebar Mist left rail.
- A 52px sidebar header strip.
- A scrollable chat history with transparent rows.
- A Pure White main conversation column.
- A centered 720px to 768px reading width.
- 24px section gaps and 6px element gaps.
- Hairline dividers between sidebar sections.

## Avoid

- Any chromatic accent color.
- Drop shadows for elevation.
- Custom fonts.
- Text above 24px.
- Default navigation row fills.
- Decorative images or abstract graphics.
- Color-coded status chips.
- Pure black body text; use Graphite Ink instead.
