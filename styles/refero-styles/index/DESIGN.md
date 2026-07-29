# Index - Style Reference

> Blueprint on a backlit drafting table: a dark wireframe interface with one muted periwinkle annotation pen.

**Theme:** dark

Index is a schematic dark interface. It looks like a technical wireframe drawn in negative space: matte black surfaces, dashed containment, periwinkle annotation marks, and large architectural headlines. The system is almost entirely achromatic. The design should feel drawn, measured, and engineered rather than decorated.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Void | `#000000` | `--color-void` | Page background, structural borders, deep canvas |
| Carbon | `#1c1c1c` | `--color-carbon` | Elevated surface, hero wash, section backgrounds |
| Graphite | `#4d4d4d` | `--color-graphite` | Tertiary borders, disabled outlines, dense dividers |
| Steel | `#808080` | `--color-steel` | Secondary body copy, muted borders, metadata |
| Ash | `#ababab` | `--color-ash` | Helper text, captions, tertiary text |
| Paper | `#ffffff` | `--color-paper` | Primary text, logo marks, button borders, active ink |
| Periwinkle Annotation | `#7089ba` | `--color-periwinkle-annotation` | Data nodes, check icons, illustration line accents, tiny washes |

## Tokens - Typography

- Primary family: `Raveo Variable`.
- Fallback: Inter Variable, Manrope, or a grotesque with a 900+ weight axis.
- Display behavior: 70px, weight 1000, line height 1.1, tight tracking.
- Body behavior: Raveo 400 at 14px to 16px.
- Micro labels: `Geist Mono`, 9px to 12px, weight 500, tracked uppercase.

| Role | Size | Weight | Line height | Letter spacing | Use |
|------|------|--------|-------------|----------------|-----|
| Micro | 9px | 500 | 1.6 | 0.02em | Eyebrows, version tags, step labels |
| Caption | 12px | 400 | 1.2 | 0 | Small labels |
| Body Small | 14px | 400 | 1.6 | -0.14px | Supporting copy |
| Body | 16px | 400 | 1.6 | -0.16px | Main body copy |
| Subheading | 24px | 1000 | 1.4 | -0.24px | Strong subheads |
| Heading | 32px | 1000 | 1.2 | -0.32px | Section headings |
| Display | 70px | 1000 | 1.1 | -2.8px | Hero and major statements |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | compact |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 10px |
| Spacing scale | 4, 5, 6, 8, 9, 10, 12, 16, 18, 20, 24, 28, 34, 44, 50, 100px |
| Nav radius | 6px |
| Feature tile radius | 20px |
| Icon container radius | 50px |
| Tags | 100px |
| Buttons | 100px |

## Components

- Dashed section container: the primary layout primitive, wrapping content in 1px dashed containment.
- Hero spotlight banner: Carbon surface with subtle radial wash, centered stack, Raveo 1000 headline, mono eyebrow, body copy, and outline button.
- Outlined pill button: 100px radius, 1px Paper border, no fill, Raveo 500 label.
- Eyebrow chip: dashed outline, pill radius, Geist Mono 9px uppercase tracking.
- Step card: no fill, no shadow, periwinkle icon above label and description.
- Feature split panel: left text and checklist, right square wireframe illustration.
- Periwinkle check item: tiny #7089ba icon plus white text.
- Top navigation: transparent over hero, white logo, centered nav links, login, and outline CTA.
- Illustration module: geometric wireframe graphics with periwinkle line art and tiny white data dots.

## Layout And Imagery

Use a dark 1200px page with section wrappers that feel like CAD or blueprint frames. Let dashed borders, mono tags, and wireframe illustrations provide structure. Avoid filled cards, drop shadows, and normal SaaS gradients.

## Do

- Use Raveo Variable weight 1000 for display headlines at 32px and above.
- Wrap major content sections in dashed 1px containers.
- Set the hero display at 70px, line-height 1.1, letter-spacing -0.04em.
- Ration #7089ba to annotation roles only.
- Use Geist Mono 9px with tracking for eyebrows and labels.
- Keep buttons as outlined pills with no fill.
- Keep depth matte and flat through surface changes, not shadows.

## Do Not

- Do not introduce colors outside the neutral stack and #7089ba.
- Do not use lower display weight for the big Raveo headlines.
- Do not replace dashed borders with solid borders.
- Do not add drop shadows, glows, or blur effects to cards or buttons.
- Do not center-align long body copy.
- Do not use #7089ba as a button fill.
- Do not add intermediate type sizes that break the scale.
