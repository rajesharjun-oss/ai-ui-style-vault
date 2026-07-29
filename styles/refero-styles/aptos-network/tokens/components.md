# Components

### Floating Nav Pill
**Role:** Primary site navigation container

A centered, floating white pill containing logo, menu items, and CTA. Fill: Bone (#f9f9f0). Inset border: 1px Ink (#0f0e0b) via box-shadow inset -1px 0 0 0. Radius: 9999px. Horizontal padding: ~20px. Nav items in Season Serif weight 400 at 16px, Ink color, with chevron icons for dropdowns. Right-side CTA is a Charcoal (#21201c) filled pill with Bone text, 10px 20px padding, 9999px radius. The pill floats at the top of the viewport with ~30px top margin and 1px Ink bottom border.

### Filled Pill CTA
**Role:** Primary action button

Charcoal (#21201c) fill, Bone (#f9f9f0) text, Season Serif weight 420 at 16px, letter-spacing normal. Padding: 10px 20px. Radius: 9999px. No border, no shadow. Text is uppercase, tightly tracked. Used for all primary actions: GET STARTED, CTA triggers.

### Ghost Text Link
**Role:** Secondary inline action or nav item

No background, no border. Ink (#0f0e0b) text in Season Serif weight 400 at 16px, letter-spacing normal. Underline appears on hover only. 5px vertical padding. Used for nav items, inline links, and secondary actions.

### Full-Bleed Color Section
**Role:** Page section with solid muted-color background

Spans full viewport width, no max-width constraint. Background: Sage (#d5fad3), Warm Stone (#9d937c), Soft Sand (#ccc5a3), or Powder Blue (#badbee). No border, no shadow, no radius. Internal content is left-aligned text on the left half, decorative geometry on the right half. Vertical padding: 90-150px.

### Section Hairline Divider
**Role:** Horizontal divider between sections or within sections

1px line implemented as inset box-shadow: `inset 0 -1px 0 0 {color}`. Colors rotate: Ink (#0f0e0b), Soft Sand (#ccc5a3), Powder Blue (#badbee). No actual border property, no margin, full width of parent. Creates the impression of a printed line on paper.

### Display Headline
**Role:** Hero and section-opening title

Season Serif weight 335-340 at 90-120px, line-height 1.0, letter-spacing -0.030em (-2.7 to -3.6px). Color: Ink (#0f0e0b). Left-aligned. The whisper-weight display is the system's signature: most brands use 600-700 for 120px headlines; Aptos uses the lightest weight, creating authority through restraint. Two-line max.

### Body Copy Block
**Role:** Editorial prose section content

Season Serif weight 400 at 18px, line-height 1.4, letter-spacing 0. Color: Ink (#0f0e0b). Narrow column (~400px width), right-aligned within its half of the split layout. Sits below a section hairline divider. 30px row-gap between paragraphs.

### Code Panel
**Role:** Monospace code display

Background: Powder Blue (#badbee). Monospace text in Season Serif at 9-16px, weight 420. Dark text on light blue. Full-height panel on the right side of split sections. No padding frame - code bleeds to panel edges. 1px Ink inset border at panel edges.

### Striped Geometric Panel
**Role:** Decorative right-side pattern

Hard-edge striped pattern (not a smooth gradient): alternating 44px-wide vertical bands of two colors, distorted by a wave/curve mask. Color pairs: Ink + Powder Blue, Ink + Soft Sand. Implemented as linear-gradient with sharp color stops. 1px white or 1px color hairlines between bands. Occupies the right 40-50% of split sections.

### Nav Dropdown Item
**Role:** Submenu item within nav pill

Bone (#f9f9f0) text in Season Serif weight 400 at 16px, Ink on hover background. 5px vertical padding, 15px horizontal padding. No icon, no description text. Appears in a dropdown panel below the nav pill on click.

### Section Opening Label
**Role:** Small caption above headlines or between sections

Season Serif weight 420 at 9px, letter-spacing +0.010em (+0.09px). Ink color. All caps or sentence case. Used for eyebrow labels, category tags, and metadata. The 9px size with positive tracking creates a printed-caption feel.
