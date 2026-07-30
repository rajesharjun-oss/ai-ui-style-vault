# Components

### Primary CTA Pill Button
**Role:** The single dominant purchase action on the page

Background #0071e3, text #ffffff, border-radius 9999px, padding 11px 22px. This is the only chromatic action button in the system - every other interaction is monochrome or ghost. Weight 400 at 17px SF Pro Text, letter-spacing -0.022em. Used exclusively for "Comprar" (Buy).

### Ghost Pill Button
**Role:** Secondary actions and navigation controls

Background transparent, text #ffffff at 80% opacity, border-radius 9999px, no visible border. Padding 11px 22px. Weight 400 at 17px. Used for "Ver el video" (Watch the video) and feature-explorer controls. Borderless by default - relies on text-only affordance.

### Glassmorphic Floating Bar
**Role:** Price + Buy composite floating on hero

Background rgba(66,66,69,0.72), text #ffffff at 80% opacity, border-radius 36px (or 980px for extreme rounding), padding 11px 22px, backdrop-filter blur(20px) saturate(1). This is the glass-pill pricing component anchored at hero bottom-right. The 72% charcoal fill over the hero image is what makes this read as frosted glass.

### Text Link with Arrow
**Role:** Inline learn-more navigation

Color #2997ff, weight 400 at 17px, no underline by default, includes a or glyph. The arrow glyph is part of the link, not a separate element. Tracking matches body copy at -0.022em.

### Dark Card Surface
**Role:** Feature card on dark backgrounds

Background #000000 or transparent, border-radius 28px, no shadow, padding 28px. Used in the "Lo principal." feature grid. The 28px radius is the system's signature softness - applied to every card-like container including product cards.

### Light Card Surface
**Role:** Feature card on light backgrounds (alternating sections)

Background #ffffff or #f5f5f7, border-radius 28px, no shadow, padding 28px. Text color shifts to #1d1d1f on these cards. The radius stays constant at 28px regardless of theme.

### Section Header
**Role:** Major section opener (Lo principal., Mas de cerca., etc.)

Left-aligned heading at 40px SF Pro Display weight 600, letter-spacing 0, color #f5f5f7. Optional right-aligned "Ver el video" link in #2997ff. Vertical padding 40-60px above the section content.

### Chip Badge with Prismatic Gradient
**Role:** Product family identifier (M5, M5 Pro, M5 Max)

Square badge approximately 200px, border-radius 20% (creating subtle rounded square), background uses the prismatic gradient linear-gradient(108deg, #0090f7, #ba62fc 33%, #f2416b 66%, #f55600), with white Apple logo and chip name overlay. The gradient creates an iridescent finish effect - the badge itself is the decorative element.

### Nav Link
**Role:** Top-level navigation item

Color #cccccc at 80% opacity, weight 400 at 12px SF Pro Text, letter-spacing -0.010em, no underline. Padding 10px. The 80% opacity is critical - full white nav text would feel aggressive against the black bar.

### Search Input (Global)
**Role:** Top-right search field

Background #000000, text #f5f5f7, placeholder #86868b, border #86868b at 1px, border-radius 210px (extreme pill shape), padding 0 22px left and 0 42px right (icon gutter). The 210px radius on a 36px-tall input creates a pure pill silhouette.

### Eyebrow Product Label
**Role:** Pre-headline product identifier

Weight 400 at 17px SF Pro Text, color #f5f5f7, letter-spacing -0.022em. Sits directly above the hero h1 ("MacBook Pro" above "La velocidad viene de familia."). The weight 400 at this size creates quiet product identification rather than screaming.

### Finishes Swatch
**Role:** Product color/finish picker item

Circular or rounded square swatches at ~40px, filled with finish-specific colors (#c8d8e0 Sky Blue, #f0e4d3 Starlight, #2e3642 Midnight, #e3e4e5 Silver). No border by default, border-radius 20% or 999px. These are product selectors, not decorative.

### Promo Banner Bar
**Role:** Secondary global message strip below nav

Background #1d1d1f (dark) or #ffffff (light), text #f5f5f7 or #1d1d1f, weight 400 at 14px, centered or left-aligned, includes inline "Comprar" link in #2997ff. Height ~52px (96px combined with nav). The thin strip communicates promotional urgency without competing with the hero.
