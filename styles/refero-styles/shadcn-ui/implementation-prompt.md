# Implementation Prompt

Build a compact, monochrome developer-tool interface inspired by shadcn/ui.

Use `#ffffff` as the page and card background. Use `#f4f4f5` and `#fafafa` for muted or recessed panels. Use `#09090b` for primary text, `#71717b` for muted copy, and `#e4e4e7` for hairline borders. Avoid brand gradients, decorative color floods, and multi-accent palettes.

Use Geist Sans or Inter as the primary font. Use Geist Mono only for code snippets, keyboard shortcuts, token labels, and command rows. Keep most UI text between `12px` and `16px`. Headings should stay measured: 24px, 30px, 36px, and 48px. Use weight 500 or 600 for headings and actions.

Use `18px` radius for buttons, inputs, select triggers, badges, tabs, and dropdowns. Use `24px` radius for cards, modals, command palettes, and preview panels. Use `9999px` radius only for true pills. Keep `8px` radius only for tiny embedded previews and icon slots.

Build with small reusable primitives: primary button, secondary button, outline button, ghost button, input, badge, tab list, command palette, card, popover, sidebar nav, and component preview panel. Normal cards should have `1px solid #e4e4e7` borders and no shadow. Overlays can use `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`.

Use `#e7000b` only for destructive buttons, error text, danger borders, or destructive icons. Do not use red as a regular accent color.
