# Guidelines

### Do
- Set every headline in KH Teka weight 400 with letter-spacing -0.06em at 60px and above, -0.03em at 60px and below; the negative tracking is the brand voice
- Use line-height 0.70-0.80 on display type (60px+) so descenders of one line touch the ascenders of the next - the type forms a wall, not a paragraph
- Reserve the four chromatic colors (#027b49, #f19ec8, #fa4d43, #fbb833) as full-bleed identity blocks for properties or named places; never use them for inline accents, icons, or text
- Use #1f1f1f near-black for all body text, borders, and pill-button fills rather than pure #000000; the softer black feels of-a-piece with the concrete canvas
- Let the four brand colors sit edge-to-edge with no card padding, no border, and no shadow - the color block is the component
- Pair every dark Pill Button (border-radius 100px, fill #1f1f1f) with a leading text question in the same line, so the button reads as an answer not an action
- Use 8-10px colored dots in the property's identity color as inline wayfinding marks next to its name

### Don't
- Do not assign the four chromatic colors to statuses (success/error/warning/info) - they are a fixed identity set, not a semantic palette
- Do not add box-shadows, gradients, or any elevation to cards, buttons, or images - the system is ruthlessly flat
- Do not introduce a second display typeface; KH Teka is the only voice and must own every visible word
- Do not round card corners - properties and sections are full-bleed rectangles; rounding is reserved exclusively for pills (100px) and the hamburger circle
- Do not use a line-height above 1.20 anywhere; display type must be crushed to 0.70-0.80, never relaxed to 1.4-1.6 'for readability'
- Do not use #027b49, #f19ec8, #fa4d43, or #fbb833 for body text, fine print, or button fills - they are surface colors, not content colors
- Do not wrap the hero display type in a max-width container that breaks it across lines naturally; let the headline run full-bleed and break on its own terms

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
