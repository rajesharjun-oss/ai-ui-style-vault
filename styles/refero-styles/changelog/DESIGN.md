# Changelog Design Reference

## North Star

An observatory console behind dark glass: a full-bleed black documentation surface where release notes feel precise, calm, and engineered. The system is almost monochrome. Its personality comes from typography, hairline borders, pill actions, and carefully stepped near-black surfaces.

## Theme

Dark, compact, developer-focused, documentation-first.

## Palette

The palette is a disciplined stack of black and gray. Treat `#08090a` as the canvas and build depth by moving one step lighter at a time. Keep chromatic color almost absent. White is not a neutral afterthought here; it is the main action and heading signal.

Use `#f7f8f8` for headings, logos, outlined buttons, and high-contrast UI. Use `#d0d6e0` for readable body copy. Use `#8a8f98` for metadata, timestamps, and quiet navigation. Use `#23252a` and `#34343a` as the border system.

## Typography

Inter Variable carries nearly everything. The signature is the use of half-step weights: 510 for headings and active controls, 590 for emphasis. Avoid default heavy 600/700 styling unless the implementation cannot support variable weights.

Berkeley Mono should appear only as a technical accent: inline code references, command cards, keyboard hints, changelog metadata, or tiny labels. It should never become the body or headline voice.

The type is tight and compact. Body copy is usually 15px with 1.5 line height. Section headings are 24px to 32px. Display text can reach 48px, but the page should still feel like a product document rather than a marketing hero.

## Layout

Use a full-bleed dark canvas with a centered content column. The prose column should sit around 640px to 720px; wider technical showcases can expand to about 1080px. Keep the main changelog flow single-column and stacked.

The common page shape:

1. Sticky top navigation with logo, text links, login, and outlined sign-up pill.
2. Page title with compact tab navigation.
3. Dated changelog entries stacked vertically.
4. Inline product references, code/comment cards, and icon grids inside the content flow.
5. Minimal footer or compact link group when needed.

Use 48px section gaps and 8px to 16px internal component spacing. Keep the rhythm tight.

## Surfaces And Elevation

Do not rely on drop shadows. Separation comes from:

- A five-step surface ladder from `#08090a` to `#2d2e31`.
- 1px borders in `#23252a`, `#34343a`, or `#3e3e44`.
- Rare inset strokes for high-control UI.
- Small shifts in background value on hover or active state.

Cards, inputs, code blocks, and icon tiles should look machined into the page, not floating above it.

## Components

Use outlined pill buttons for the strongest actions. The primary action is transparent, with a `#f7f8f8` border and text. Secondary actions are ghost text buttons or softer outline pills.

Changelog entries should use compact metadata, crisp headings, and readable body copy. If you need a visual asset, place it inline with 4px to 8px radius and a subtle border. Date markers should be quiet and small.

Inline command cards and code references are important to the style. Use dark graphite surfaces, 1px borders, Berkeley Mono, and restrained spacing.

## Imagery

Use product screenshots, connector icon grids, small technical diagrams, or inline UI captures. Avoid lifestyle photography and large decorative illustration. When you need visual interest, prefer the UI itself: icon tiles, app glyphs, code-like snippets, and product screenshots.

## Interaction

Hover states should be understated:

- Text links move from Fog Text to Snow.
- Surface components step one gray level lighter.
- Inputs shift border color.
- Buttons keep their outline identity instead of filling with color.

Focus states can use a brighter border and a subtle 1px or 2px ring, but avoid colorful glows unless needed for accessibility.

## Implementation Feel

The result should feel like a technical changelog maintained by a serious product team. Dense, calm, precise, and readable. No theatrics. The design is strongest when it looks obvious, fast, and deeply intentional.
