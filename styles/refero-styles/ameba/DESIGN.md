# Ameba Design Reference

## Essence

Ameba feels like a dark AI operations room where a single blue signal emerges from a near-black system. The atmospheric layer is dark, cold, and precise. The product layer is clean, white, and document-like. The style works when the hero feels cinematic but the actual UI remains crisp and operational.

## Color System

Midnight Ink is the main canvas for hero, feature, and atmospheric sections. Signal Blue is the authoritative action color and should appear only on the primary CTA, active timeline bars, and the main particle visualization. Arc Cyan is not a UI color; it belongs to glow halos and atmospheric particles. Halo Violet bridges Signal Blue into Midnight Ink in radial background washes. Product UI surfaces are White with Silver Border hairlines. Carbon, Slate Body, and Mist support text hierarchy.

## Typography

F37 Bolton is the headline voice. Use weight 300 for display and section headings with negative tracking around -0.019em at 54px and above. Open Sauce Sans is the body and UI family, keeping labels and copy legible. IBM Plex Mono is reserved for system metadata, data tags, status labels, and code-like fragments with tracked letter spacing.

## Shape And Space

Radii are modest and industrial. Cards and buttons use 8px. Tags and images use 4px. Do not round above 8px. There are no drop shadows; the system uses hairline borders, dark surfaces, and a single radial glow for depth. Spacing is comfortable, with roughly 80px section gaps, 24px card padding, and compact 12px to 16px internal gaps.

## Layout Rhythm

Use a dark hero with a radial Midnight Ink and deep blue wash behind the focal object. Pair it with one filled Signal Blue CTA. Follow with white product screenshots inside browser chrome or clean document containers. Feature sections can return to Midnight Ink, but product surfaces should stay white and bordered, as if inserted into the dark atmospheric shell.

## Components

- Dark hero with radial glow from deep blue into Midnight Ink and a particle or network visualization.
- Signal Blue CTA with 8px radius, white text, no shadow, and no gradient fill.
- Transparent or solid Midnight Ink feature card with hairline border and no glassy white overlay.
- White product surface with Silver Border hairlines, browser chrome, sidebar, table rows, and clean controls.
- IBM Plex Mono data badge with uppercase tracked metadata.
- Active timeline bar using Signal Blue only.
- Chat or command input bar with 8px radius, dark fill, hairline edge, and Signal Blue send/action.
- Metric card with F37 Bolton heading, Open Sauce Sans explanatory copy, and IBM Plex Mono value.
- Product screenshot frame with dark title bar and white content surface.
- Footer or dark link block with understated Open Sauce links and no extra color.

## Implementation Direction

Start with Midnight Ink. Add one radial glow, one Signal Blue CTA, and one clean white product screenshot. Keep Arc Cyan atmospheric only. Use IBM Plex Mono for machine-readable details. Avoid shadows, warm colors, rounded pills, transparent white glass cards, blue gradients on buttons, and body text that is too small to read.
