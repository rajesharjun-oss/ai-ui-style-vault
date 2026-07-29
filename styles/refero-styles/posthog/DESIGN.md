# PostHog Style Reference

## North Star

PostHog feels like a warm desktop OS pinned to a corkboard. The page itself is a desk surface, while main content lives in white application windows with file-like title bars, side icons, tab rows, toolbars, and hairline dividers.

The system is friendly but technical. Its warmth comes from sandy and olive neutrals, small printed-paper geometry, and rounded brand typography. Its precision comes from tight spacing, IBM Plex Sans controls, hairline borders, and developer-tool metaphors.

## Color

The palette is warm, tactile, and restrained. Sandy surfaces create the workspace; white windows hold content; amber and blue carry action.

- `Sandy Desk` `#e1d7c2`: outer page canvas, low-emphasis panels, placeholder blocks.
- `Paper White` `#ffffff`: application windows, primary cards, popovers, main content surfaces.
- `Cream Paper` `#fdfdf8`: secondary windows and warm off-white hover surfaces.
- `Soft Linen` `#eeefe9`: nested cards, secondary buttons, subtle grouped surfaces.
- `Pale Stone` `#e5e7e0`: hover backgrounds, selected list items, disabled surfaces.
- `Deep Moss` `#23251d`: primary text and headings; use this instead of pure black.
- `Olive Char` `#4d4f46`: body text, secondary icons, SVG fills, sidebar labels.
- `Sage Gray` `#65675e`: inactive tabs, muted body text, tertiary content.
- `Ash Green` `#9ea096`: placeholders, disabled controls, low-emphasis icons.
- `Faded Pewter` `#b3b3af`: subtle dividers and softer border details.
- `Warm Mist` `#bfc1b7`: primary hairline border.
- `Signal Blue` `#2f80fa`: active states, live links, selected navigation, focused conversion moments.
- `Amber Glow` `#eb9d2a`: single primary CTA.
- `Dark Amber` `#cd8407`: primary CTA hover and active states.
- `Burnished Gold` `#b17816`: outlined actions and amber-context links.
- `Marigold` `#f1a82c`: decorative illustration fills and icon accents.
- `Flame Orange` `#f54e00`: highlight backgrounds, feature tag fills, decorative warm emphasis.
- `Moss Green` `#6aa84f`: supporting green wash and small status-like badges.

Do not use pure white as the outer page background. Do not introduce extra accent colors. Do not use the PostHog spectrum gradient for UI controls; reserve it for logo or decorative text treatments.

## Typography

Use three type roles:

- Brand/body: `Open Runde`, with Inter Tight or DM Sans fallback.
- UI/control: `IBM Plex Sans Variable`, with IBM Plex Sans or Inter fallback.
- Code: `ui-monospace`, with SFMono-Regular, Menlo, and Consolas fallback.

Open Runde handles headings, body, and most brand text. Apply `-0.025em` letter-spacing at 18px and above to keep the compact feel.

IBM Plex Sans handles navigation, controls, labels, form text, and developer-facing microcopy. This makes the UI feel precise while Open Runde keeps the page warm.

Recommended roles:

- Micro: 12px, line-height 1.33, control labels and small metadata.
- Caption: 14px, line-height 1.43.
- Body: 16px, line-height 1.5.
- Subheading: 19px, line-height 1.56, tracking -0.025em.
- Heading: 21px, line-height 1.4, tracking -0.025em.
- Large heading: 24px, line-height 1.33, tracking -0.025em.
- Display: 36px, line-height 1.5.

## Layout

The model is a desktop OS workspace:

- A full-bleed `Sandy Desk` canvas.
- A left sidebar around 60px to 100px wide with file/folder icon entries.
- A centered main `Application Window` around 958px max width.
- A right-side illustration panel that can bleed off the edge.
- A minimal top navigation over the sandy canvas.
- Window content arranged with tabs, toolbars, feature grids, and hairline dividers.

The density is compact. Use 8px element gaps, 16px card padding, 48px section gaps, and tight clusters of toolbar controls. Sections should be separated by borders and rhythm, not background color changes.

## Shape And Elevation

The shape language is intentionally tiny-radius and paper-like:

- Cards: 4px.
- Inputs: 4px.
- Buttons: 4px.
- Main windows: 6px.
- Tags: 9999px, but only for small badges.

The system avoids elevation. Do not add drop shadows to cards or windows. Use 1px `Warm Mist` borders for separation. The main exception is modal overlay shadow: `rgba(0,0,0,0.25) 0px 25px 50px -12px`.

## Components

### Application Window

White surface, 6px radius, 1px `Warm Mist` border, no shadow. It contains a 36px title bar with filename, window controls, and optional frosted blur. Internal padding usually ranges from 16px to 32px.

### Sidebar File Entry

Vertical icon-plus-label item. Use 16px to 20px icons, IBM Plex Sans 13px/500 labels, Olive Char text, 8px internal spacing, and 16px between entries. Hover uses Pale Stone with 4px radius. Active icon fill uses Signal Blue.

### Amber CTA Button

Amber Glow background, Deep Moss text, 4px radius, 6px 12px padding, IBM Plex Sans 14px/500. Hover shifts to Dark Amber. Use only one filled CTA per page.

### Outlined Action Button

Transparent fill, 1.5px Burnished Gold border, Burnished Gold text, 4px radius, 6px 12px padding. Use as a secondary action beside the filled amber CTA.

### Ghost Toolbar Button

Transparent background, Deep Moss icon or text, 4px radius, 2px 4px padding. Hover uses Pale Stone. Use for formatting controls and utility toggles.

### Tab Bar Item

Inactive tabs use Sage Gray with IBM Plex Sans 13px/500. Active tabs use Signal Blue text and a 2px Signal Blue bottom border. Use white for the active tab background and transparent for inactive tabs.

### Tag Pill

Small categorical badge only. Use 9999px radius, 2px 8px padding, 12px type. Use Flame Orange, Moss Green, or Marigold fills depending on category.

### Product Feature Card

White card, 1px Warm Mist border, 4px radius, 16px padding, no shadow. Include a small accent icon, 19px/600 heading, and 15px/400 body. Hover can shift to Soft Linen.

### Illustrated Decoration Panel

Use flat or isometric illustrations with thick 2px Olive Char outlines and selective Marigold, Signal Blue, and Flame Orange fills. Let illustrations flank the main window and bleed off edge; do not trap them in cards.

## Imagery

Imagery is diagrammatic, flat, and tactile. Use cutout-like illustrations, file icons, simple objects, and product metaphors. Avoid photography, glassmorphism, glossy 3D, or generic SaaS hero art.

## Do

- Use Sandy Desk as the outer canvas.
- Use Paper White windows for major content.
- Apply 4px radius to cards, buttons, and inputs.
- Use 1px Warm Mist borders instead of shadows.
- Use Amber Glow for the single primary CTA.
- Use Burnished Gold for outlined secondary actions.
- Use Signal Blue only for active states, live links, and selected navigation.
- Keep Open Runde and IBM Plex Sans in their intended roles.

## Do Not

- Do not use white or gray as the outer page background.
- Do not add drop shadows to cards or windows.
- Do not use container radii larger than 6px.
- Do not introduce extra accent colors.
- Do not use the spectrum gradient for controls.
- Do not use pill shapes on anything larger than a small tag.
- Do not use pure black for primary text.
