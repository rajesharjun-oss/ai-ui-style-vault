# Champions4good Design Reference

## Essence

Champions4good is a dark-first sports club poster. It uses a Deep Plum canvas, one loud lavender accent, and huge ultra-condensed type that fills the screen like a vintage broadside. Supporting interface pieces stay small and quiet so the display type can dominate.

## Color System

Deep Plum is the main canvas for hero and dark sections. Lavender Shock is the only major chromatic color on that plum ground. Paper White creates strong rhythm breaks after dark sections. Espresso Brown and Ink Teal provide warm and cool dark card surfaces. Mint Signal and Amber Pulse are small functional punctuation colors for badges, tags, and transition moments. They should not become full-surface colors.

## Typography

Druk Condensed Super Desktop is the brand voice. Use it for display and section headings, especially at 58px and above. Neue Montreal handles navigation, buttons, body, and supporting copy at 12px to 16px. The large Druk headlines use very tight line-height, usually 0.78 to 0.85, so stacked words feel compressed and poster-like.

## Shape And Space

The UI is mostly pills and soft cards. Buttons and toggles use 9999px radius. Tags use 6px radius. Cards use 14px radius with 20px padding. There are no shadows. Layout uses flat color layering and abrupt section contrast instead of elevation.

## Layout Rhythm

Start with a full-bleed Deep Plum hero, transparent nav, sport toggle pills, and enormous lavender Druk words pushed close to the viewport edges. Break dark sections with Paper White sections using black Druk display text. Keep content left aligned, especially display headings. Avoid centered display stacks.

## Components

- Hero display headline: Druk Condensed at 151px to 317px, Lavender Shock on Deep Plum, line-height 0.78 to 0.85.
- Sport toggle pill: 80x48px pill, active lavender fill, inactive lavender outline, simple sport line icon.
- Filled lavender button: compact pill, Lavender Shock fill, Deep Plum text, Neue Montreal 14px weight 500.
- Navigation bar: transparent over hero, 64px height, logo left, links centered, pill action right.
- Wordmark logo: stacked Druk text in Lavender Shock with a compact sport mark.
- Light section display block: Paper White section with black or charcoal Druk type at 187px.
- Card surface: 14px radius, 20px padding, Espresso Brown on dark or Paper White on light.
- Badge or tag: 6px radius, Mint Signal, Amber Pulse, or Lavender Shock fill with dark text.
- Footer link list: Neue Montreal 14px, left-aligned columns, tight row gaps.

## Implementation Direction

Use typography as the imagery. Keep chromatic variety low. Make Lavender Shock powerful only because it is rare and placed against Deep Plum. Use mint and amber as small punctuation. Avoid shadows, gradients, serif type, card-heavy SaaS layouts, photography-heavy hero sections, and any display line-height above 1.0.
