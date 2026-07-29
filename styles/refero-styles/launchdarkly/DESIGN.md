# LaunchDarkly Design Notes

LaunchDarkly is a dark neon control-room system. It uses a midnight canvas, charcoal panels, cool violet-blue signal color, dense developer UI, and product screenshots as proof. The design is technical without becoming cluttered because shape, spacing, and glow are disciplined.

## Visual Principles

- Keep the whole page on a dark midnight canvas.
- Use violet-to-blue as an electronic signal, not as a broad decorative rainbow.
- Use 30px radius for user-facing controls and cards.
- Use 60px radius for the top nav pill and full-width pill containers.
- Use bright white product screenshots on the dark page for visual tension.
- Use glow for elevation instead of drop shadows.
- Keep body content left-aligned outside hero blocks.

## Color System

The palette is Midnight Ink, Carbon, Smoke, Graphite, Steel, Slate, Fog, Ash, Paper, Voltage Blue, Signal Violet, and Plasma Cyan. Voltage Blue is the filled primary CTA. Signal Violet is the brand emphasis color for hero text, outlines, links, and gradient endpoints. Plasma Cyan is a rare ambient glow endpoint.

## Typography

Use a custom grotesk such as Sohne if licensed, or Inter, Geist, or Space Grotesk as substitutes. Weight 500 dominates headings. Huge display headlines use tight line-height around 1.0 to 1.09. Use a mono font for SDK names, code, and technical identifiers.

## Layout

Use a 1200px content width, large 80px to 120px section gaps, and 32px to 48px card padding. Common layouts include a centered hero, logo strip, tabbed feature section, two-column product screenshot sections, code integration blocks, and three-column resource cards.

## Elevation

Do not rely on regular drop shadows. Use blue/violet glow halos such as `rgba(64,91,255,0.25)` or `rgba(112,132,255,0.19)`. Product screenshots can appear as bright white panels with subtle glow on the dark canvas.
