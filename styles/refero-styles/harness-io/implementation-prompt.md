# Implementation Prompt

Build a dark DevOps mission-control interface in the Harness.io style.

Use Void Canvas (`#070707`) as the full page background. Stack surfaces upward with Carbon Plate (`#0d0e12`) for cards, Obsidian (`#141418`) for nested panels and code blocks, and Iron Edge (`#2e3038`) for dividers and hover overlays. Use Pure White (`#ffffff`) for primary text and the only filled button. Use Ash (`#c8cad0`) and Graphite (`#aeaeb7`) for secondary copy. Define card edges with Fog (`#d9dae5`) light borders, even on dark surfaces. Do not use dark borders on cards.

Accent color is rationed. Use Phosphor Mint (`#70dcd3`) for one featured card or stat panel per viewport. Use Signal Blue (`#0092e4`) and Current Blue (`#00ade4`) for active links, nav state, and focus accents. Do not use mint and blue as competing accents in the same section. Use Verdant Edge (`#75ae4c`) only as a supporting outlined status/action accent.

Use Calsans or a wide-tracked geometric sans for headings. Headlines at 56px or larger must use positive tracking around `0.056em`; never tighten Calsans. Use Geist or Inter/system fallback for all body, nav, buttons, forms, badges, activity feeds, and metadata. Body copy is 16px/1.5, weight 400, with slight positive tracking. Buttons use Geist 16px.

Use an 8px base unit, 1200px max width, 80px section gaps, 24px card padding, and 16px element gaps. Cards use 20px radius. Nested cards use 16px. Inputs use 5px. Buttons and badges use 800px pill radius. Avoid card shadows; the light border is the elevation.

Expected components:

- Hero headline: Calsans 88px/300, Pure White, positive tracking, optional first phrase in Phosphor Mint.
- Filled pill button: Pure White fill, Void Canvas text, 800px radius, 12px by 24px padding, Geist 16px/500.
- Ghost pill button: transparent, Pure White border/text, 800px radius.
- Dark surface card: Carbon Plate, 1px Fog border, 20px radius, 24px padding, no shadow.
- Phosphor accent card: Phosphor Mint fill, 20px radius, used at most once per viewport.
- Code surface: Obsidian, 16px radius, Geist/code-like 13px to 14px copy, nested in a dark card.
- Activity row: avatar, commit/PR message, metadata, status dot, Iron Edge divider.
- Input field: Carbon Plate fill, Iron Edge border, Deep Signal focus border, 5px radius.
- Status badge: outlined pill, 800px radius, tiny widely tracked Geist text.
- 3D product visual: dark rendered object or light-ribbon visual bleeding into the black canvas.

The page must stay dark end to end. Avoid light sections, drop shadows, colorful buttons, multiple accents in one section, dark card borders, stock photography, and flat generic illustrations.
