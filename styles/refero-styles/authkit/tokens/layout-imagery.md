# Layout & Imagery

## Layout

Full-bleed dark canvas, max-width 1200px content container centered. Hero is a single centered illuminated wordmark ('AuthKit' in gradient display type) under a small eyebrow label, with three floating glass auth-form cards layered behind/below in an overlapping fan (left card tilted left, center card scaled largest, right card tilted right). Below the hero, a light/dark theme toggle sits centered. Feature row is a horizontal 6-icon timeline with thin connecting lines between circular icon tiles. Section rhythm: every section opens with a centered eyebrow label flanked by fading horizontal lines, then a large centered heading (44-48px), then a single line of muted body copy (16-18px), max ~640px width. Customization section features a mock browser-window frame with the auth card centered, surrounded by floating UI inspector panels (color swatches, radius sliders, logo icon picker, button text field, page background field) positioned at the corners of the canvas like a design-tool workspace.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Midnight Canvas | `#05060f` | Full-bleed page background, deepest layer |
| 1 | Steel Plate | `#2f343` | Elevated panels, ghost-button fills |
| 2 | Frosted Glass | `#bad6f708` | Translucent card surface - barely-visible tint that reads as glass above the canvas |
| 3 | Deep Glass | `#05060ff7` | Auth-form modal surface - nearly opaque midnight with frosted-edge shadow stack |

## Elevation

- **Auth-form modal card:** `inset 0 1px 1px rgba(216, 236, 248, 0.2), inset 0 24px 48px rgba(168, 216, 245, 0.06), 0 16px 32px rgba(0, 0, 0, 0.3)`
- **Feature card:** `inset 0 1px 1px rgba(199, 211, 234, 0.12), inset 0 24px 48px rgba(199, 211, 234, 0.05), 0 24px 32px rgba(6, 6, 14, 0.7)`
- **Floating auth-card (hero):** `inset 0 1px 1px rgba(216, 236, 248, 0.2), inset 0 24px 48px rgba(168, 216, 245, 0.06), 0 16px 32px rgba(0, 0, 0, 0.3)`
- **Glow halo (behind hero wordmark):** `0 0 6px rgba(186, 207, 247, 0.32), 0 0 12px rgba(238, 186, 247, 0.24)`

## Imagery

Visuals are dominated by glass-morphism auth-form mockups (email/password inputs, social-login buttons, passwordless code-entry) rendered as floating translucent cards against the midnight canvas. Feature icons are line-art mono glyphs in #d1e4fa inside circular frosted tiles. A faint blueprint grid (1px lines at rgba(186,215,247,0.06)) covers the full page as ambient atmosphere, and a conic-gradient spotlight halo glows at the top of the hero. No photography, no lifestyle imagery, no product screenshots - the product IS the visual: login boxes arranged like glass prototypes in a dark studio.
