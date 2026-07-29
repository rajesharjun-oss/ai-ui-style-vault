# Layout & Imagery

## Layout

Max-width 1200px centered on a white canvas. The hero is a centered-headline layout: large Roobert 700 headline, one sentence of subtext, and a single cyan CTA button, with a tabbed product screenshot panel directly below spanning ~70% of content width. Below the hero, a horizontal logo marquee runs full-bleed with a subtle overflow mask. Feature sections follow a 2-column text-left / product-right alternating pattern at desktop widths, switching to centered stacks at mobile. The "Built for any kind of work" and AI sections use full-width tab controls (0px radius) as in-section navigation, with content panels that swap beneath them. Sections are separated by 80px vertical gaps with no visual dividers - white space is the only separator. A 3-column card grid appears in the tools/features section. Navigation is a sticky top bar with logo left, nav links center-right, and the cyan CTA pinned to the far right.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Page Canvas | `#ffffff` | Default page background; all sections begin here |
| 2 | Card Surface | `#ffffff` | Elevated cards defined by #bebebe or #e8e8e8 border (0.5-1px solid), not shadow |
| 3 | Warm Off-White | `#f6f5ee` | Alternate section background per CSS token --_color---background-warm; used for warm-tinted feature bands |
| 4 | Dark Shell | `#111213` | Dark nav bar, dark footer sections, full-bleed dark feature blocks |
| 5 | Teal Wash | `#45bfdb` | Brand-colored surface for feature callouts and highlighted section bands |

## Elevation

Goodnotes uses zero box-shadow throughout. Elevation is expressed purely through borders: cards sit on white with a 0.5-1px solid #bebebe or #e8e8e8 outline. This makes the UI feel like paper stacked on paper - no depth illusion, just crisp-edged layering consistent with the notebook metaphor.

## Imagery

Goodnotes uses contained product UI screenshots as the primary visual device - no lifestyle photography, no abstract illustration. Screenshots are shown as overlapping layered document stacks (strategic expansion proposal v1/v2/v3 effect) or as a single dominant app view inside a rounded-card frame. On the handwriting section, a tablet-canvas screenshot with actual hand-drawn strokes, arrows, and annotations appears at roughly 40% of the section width. Illustration is absent; all visual complexity is offloaded to the real product UI. Icons (toolbar actions) are filled, compact, and monochromatic at 15-20px - no outlined or multicolor icon style. Partner/customer logos in the marquee strip are black-on-white, unglamoured. The overall density is image-moderate: one large product screenshot per section, surrounded by generous white space, with text doing explanatory work rather than decorative imagery.
