# TWOMUCH.STUDIO Design Reference

## North Star

floating museum of curiosities

## Theme

light style for Agency interfaces.

## Color System

- Gallery Plate `#e5e7eb` for Primary canvas and hairline dividers the infinite gray field that hosts floating objects and borders nearly every surface in the system
- Carbon `#000000` for Primary text, icon strokes, and the dark pill in the nav bar the only true black in the system, used for type and high-contrast marks
- Chalk `#f4f4f4` for Elevated surface above the canvas cards, panels, and lighter button fills that need to lift off the gray field
- Paper White `#ffffff` for Inset surfaces and inverse text on dark fills the cleanest white available for maximum contrast pop
- Concrete `#dedede` for Tertiary surface and muted button fill one step darker than Chalk, used where a surface needs weight without drama
- Voltage Lime `#e2ff70` for Primary action fill and highlight accent the only chromatic button/link background in the system, applied to the Menu pill and active link states to switch a control on
- Oxide Brown `#68340e` for Decorative content accent appears inside imagery and printed artifacts (labels, type on objects); not a UI color but a recurring editorial note

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- ABCMonumentGrotesk Sole typeface across all UI body, labels, nav, headings, buttons, icons, links. The single medium weight with uniformly negative tracking (~-0.48px) gives every label a compressed, display-poster feel regardless of size. Avoid pairing with a secondary face; the constraint IS the identity. `--font-abcmonumentgrotesk`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 4px
- Density: compact
- Section gap: 48-64px
- Card padding: 16-24px
- Element gap: 8px

## Components

- Floating Central Nav Bar: Primary site navigation
- Menu Pill Button: Primary action / navigation trigger
- Status Pip (Circular): Indicator dot
- Counter Badge: Sequential numbering indicator
- Ghost Link: Inline navigation link
- Object Tile (Floating Asset): Content showcase card
- Editorial Label Tag: Category, date, or metadata label
- Secondary Button (Neutral Pill): Non-primary action

## Implementation Guidance

- Apply Voltage Lime (#e2ff70) as a fill to exactly one action per screen it is a rationed accent, not a decorative color
- Use the 9999px pill radius for every interactive control, label, and tag the pill is the only shape language in the UI
- Set all type at weight 500 in ABCMonumentGrotesk with negative tracking near -0.48px, including headings do not introduce a bold or light weight
- Let objects float directly on Gallery Plate (#e5e7eb) without card backgrounds, shadows, or frames the canvas IS the container
- Keep the central nav bar the only persistent UI element; let every other surface be content
- Use 1px Gallery Plate hairlines for all borders and dividers never go thicker
- Pair Voltage Lime fills with Carbon text only; never put the lime against Paper White or Chalk (contrast pair #000 #e2ff70 = 18.8:1)

## Guardrails

- Do not introduce a second typeface, a second weight, or positive letter-spacing the monochrome grotesque is the voice
- Do not add drop shadows, glows, or elevation tiers the system is flat by design
- Do not use a chromatic fill other than Voltage Lime for any button or link Concrete and Chalk are the only neutral fills
- Do not frame imagery in rounded cards or bordered containers let objects touch the canvas directly
- Do not use the Oxide Brown (#68340e) as a UI color it belongs inside imagery and printed artifacts only
- Do not stack more than two surface levels on a single screen (e.g. Chalk card on Gallery Plate is fine; a third nested card is not)
- Do not center-align body copy or use large type sizes the system stays compact and left-aligned, max 22px
