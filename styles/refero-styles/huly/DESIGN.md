# Huly - Design Reference

> Midnight workspace interface with a narrow iris-blue to ember-coral aurora, layered graphite surfaces,
> pill-first controls, and alternating dark/light product storytelling sections.

## Theme

Huly reads as a cosmic productivity workspace: dark surfaces, a focused two-color brand palette, and
real product UI acting as the main visual evidence. The visual system should feel precise, atmospheric,
and product-led rather than decorative or generic.

Use dark mode for product-heavy screens and light sections for editorial/product explanation. Decide the
surface mode before composing components; do not mix dark and light treatments inside one component.

## Core Visual Rules

- Use a tight chromatic vocabulary: Electric Iris and Ember Pulse carry the brand.
- Make controls pill-first, especially buttons, chips, tags, and filters.
- Prefer borders and surface contrast over heavy shadows on dark UI.
- Use the aurora gradient as a special accent, not a full-page wash.
- Treat product screenshots or real UI previews as the primary hero asset.
- Alternate dark and light bands with generous vertical rhythm.

## Quick References

- **Dark canvas:** `#303236`
- **Deep hero base:** `#090a0c`
- **Dark card:** `#111111`
- **Primary accent:** `#5683da`
- **Warm accent:** `#ff8964`
- **Primary text on dark:** `#ffffff`
- **Primary text on light:** `#050506`
- **Page max width:** `1200px`
- **Section gap:** `96px`
- **Card padding:** `24px`
- **Element gap:** `12px`
- **Pill radius:** `9999px`
- **Card radius:** `12px`
- **Panel radius:** `30px`

## Implementation Notes

Start with the tokens in `code/css-variables.css` or `code/tailwind-v4.css`. For React/Tailwind apps,
map the custom properties into the app theme and build reusable primitives for buttons, chips, cards,
panels, section bands, and product preview frames.

For original work, keep the system logic but replace source-specific brand marks, screenshots, names,
copy, and exact compositions.

