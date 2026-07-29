# Implementation Prompt

Build a disciplined monochrome developer-platform interface in the Vercel style.

Use Paper White (`#fafafa`) as the page canvas and Pure White (`#ffffff`) for elevated cards, inset highlights, and input fields. Use Obsidian (`#171717`) for primary text, filled buttons, dark cards, and list markers. Use Charcoal (`#4d4d4d`) for body copy and secondary button labels. Use Stone (`#666666`), Slate (`#7d7d7d`), Graphite (`#8f8f8f`), Smoke (`#a8a8a8`), and Ash (`#c9c9c9`) for muted hierarchy. Use Hairline (`#ebebeb`) for borders and rings. Use Carbon (`#000000`) only for the triangle mark and SVG fills. Use Terminal Green (`#297a3a`) only for command confirmations, links, tags, or very short technical emphasis.

Typography is binary. Use Geist Sans for display, body, nav, cards, and buttons. Use Geist Mono for labels, metadata, code blocks, CLI output, uppercase eyebrows, and tiny stamps. Headlines use weight 400 to 450 with tight tracking: 64px uses -3.84px, 56px uses -3.36px, 30px uses -1.5px. Body copy is 14px to 16px, weight 400, line-height 1.43 to 1.5. Labels are Geist Mono 11px to 12px uppercase with 0.071em tracking. Do not use heavy heading weights.

Use a 4px base grid, 1280px max width, 96px to 128px section gaps, 16px card padding, and 12px element gaps. Cards, buttons, and bordered containers use 6px radius. Nav blocks can use 2px radius. Use 9999px only for compact nav/header pills. Build elevation with rings only: `0 0 0 1px rgba(0,0,0,0.08), 0 0 0 2px #fafafa`. Never use blurred drop shadows.

Expected components:

- Sticky 64px nav: Paper White, wordmark with triangle mark left, Geist Sans nav items, right-side ghost and filled actions.
- Filled black button: Obsidian fill, Pure White text, 6px radius, Geist Sans 14px/400.
- Ghost outline button: transparent fill, Charcoal text, Hairline ring, 6px radius.
- Bordered card: Pure White, 6px radius, stacked hairline rings, 16px padding.
- Inverted card: Obsidian fill, white text, 6px radius, used sparingly.
- CLI output panel: white surface, Geist Mono 12px, triangle command prefixes, green checkmark confirmations.
- Eyebrow label: Geist Mono 11px uppercase, 0.071em tracking.
- Hero composition: asymmetric headline, black triangle mark, small metadata/eyebrow stack, no background image.

The page should feel precise, compact, terminal-native, and paper-like. Avoid photography, decorative illustration, broad gradients, drop shadows, soft rounded cards, colorful badges, and any extra accent colors.
