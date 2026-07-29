# Implementation Prompt

Use the PLATFORM style language for this UI.

Create a monochrome art-gallery catalog interface: pure white canvas, pure black type and borders, compact 15px body text, 1px outlines, zero radius, zero shadows, and artwork images as the only color. The result should feel like a printed exhibition catalog, not a conventional ecommerce store.

Core rules:

- Use `#ffffff` as the page background and card surface.
- Use `#000000` for all primary text, links, icons, card borders, navigation borders, and interactive UI.
- Use `#dddddd` only for gray section bands or subtle dividers.
- Use `#b3b3b3` for muted placeholders and low-priority metadata.
- Do not introduce chromatic colors for UI.
- Use MediumLLWeb if available; otherwise use Sohne, Inter, or Neue Haas Grotesk.
- Use only five type sizes: 12px, 15px, 20px, 48px, and 72px.
- Use 15px at 1.20 line-height as the default body rhythm.
- Use 400 as the default weight and 500 only for labels, artist names, and prices.
- Enable tabular numerals for prices.
- Set every border radius to 0px.
- Use 1px borders only.
- Do not use shadows, glows, blur, gradients, or decorative backgrounds.

Recommended structure:

- Flat top navigation with 1px black bottom border, PLATFORM label, shop links, region selector, account, saved items, and search.
- Full-bleed hero spotlight with dark artwork/photo background and centered white overlay type.
- Section header band with gray or white surface, left label, center description, right underlined link, and 1px black divider.
- 4-column artwork grid inside a 1280px container.
- Artwork cards with 1px black border, 0px radius, image edge-to-edge, and centered metadata stack.
- Footer with 1px black top border and compact multi-column link lists.

Avoid:

- Rounded cards or buttons.
- Colorful badges, pills, or status labels.
- Commercial-looking CTA buttons.
- Heavy ecommerce chrome.
- Decorative icons beyond minimal utility glyphs.
- Lifestyle imagery or room staging.

The UI should behave like a gallery wall: quiet, exact, flat, and artwork-led.
