# Default - Style Reference

> Mission control behind frosted glass: weight-400 headlines float over matte-black panels lit by thin blue ring-light accents.

**Theme:** dark

Default is a dark infrastructure UI system. It favors compact surfaces, restrained typography, hairline borders, matte black panels, and quiet blue active states. It should feel like mission control for workflow automation or technical operations, not like a neon cyberpunk dashboard or a broad marketing site.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Void | `#0b0c0e` | `--color-void` | Deep page canvas and terminal background |
| Graphite | `#131416` | `--color-graphite` | Primary card and panel surface |
| Charcoal | `#1f1f21` | `--color-charcoal` | Secondary surfaces, rails, borders, dividers |
| Ink | `#333333` | `--color-ink` | Secondary text and subdued labels |
| Smoke | `#3c3d3e` | `--color-smoke` | Button borders and subtle separators |
| Steel | `#71717a` | `--color-steel` | Muted body text, captions, helper text |
| Fog | `#858687` | `--color-fog` | Secondary text, inactive nav, icon strokes |
| Ash | `#9d9e9f` | `--color-ash` | Placeholder text, tertiary text, disabled states |
| Chalk | `#cececf` | `--color-chalk` | Secondary body text and table cell text |
| Bone | `#f2f2f2` | `--color-bone` | Primary CTA fill against dark surfaces |
| Snow | `#ffffff` | `--color-snow` | Primary headings, body text, icons, active ink |
| Signal Blue | `#3b82f6` | `--color-signal-blue` | Links, active nav, icon accents, active borders |
| Arc Blue | `#60a5fa` | `--color-arc-blue` | Informational text accents and workflow nodes |
| Ring Blue | `#93c5fd` | `--color-ring-blue` | Focus rings and selection outlines |
| Mint | `#4ade80` | `--color-mint` | Green outline accents and focused edges |
| Fern | `#22c55e` | `--color-fern` | Green wash and soft success-adjacent emphasis |
| Coral | `#f87171` | `--color-coral` | Red text accents and destructive-adjacent emphasis |
| Ember | `#ea580c` | `--color-ember` | Orange decorative chip in mockups |
| Iris | `#314ef0` | `--color-iris` | Brand chip tint in product screenshots |

## Tokens - Typography

- Font family: `Inter` variable for everything.
- OpenType features: enable `ss01` and `ss03`.
- Display behavior: 52px to 64px, weight 400, tight tracking.
- Body behavior: 13px to 18px with fractional weights for density.
- UI behavior: compact, engineered, and slightly compressed.

| Role | Size | Weight | Line height | Letter spacing | Use |
|------|------|--------|-------------|----------------|-----|
| Body Large | 14px | 400-500 | 1.43 | -0.32px | Compact body and table text |
| Body XL | 16px | 400 | 1.5 | 0 | Main content |
| Subheading | 18px | 450 | 1 | -0.61px | Compact subheads |
| Heading | 32px | 400 | 1.25 | -0.64px | Section headings |
| Heading Large | 42px | 400 | 1.2 | -0.88px | Large headings |
| Display | 52px | 400 | 1 | -1.3px | Hero headline |
| Display Large | 64px | 400 | 0.94 | -1.28px | Oversized display |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | compact |
| Base unit | 4px |
| Max width | 1080px |
| Section gap | 96px |
| Card padding | 28px |
| Element gap | 8px |
| Spacing scale | 4, 8, 12, 16, 20, 24, 28, 32, 36, 48, 52, 64, 68, 80, 96, 116px |
| XS radius | 5.26px |
| SM radius | 8.77px |
| Pills | 10px |
| Buttons | 10px |
| MD radius | 12px |
| Cards | 12px |
| LG radius | 16px |
| XL radius | 20px |
| 2XL radius | 24px |

## Components

- Primary pill button: Bone background, Ink text, 10px radius, compact height, no blue fill.
- Secondary pill button: transparent or Graphite background, Smoke border, Snow or Chalk text.
- Workflow node card: Graphite background, 8.77px radius, 12px padding, 0.5px white-alpha border.
- Card/panel: Graphite or Charcoal surface, 12px radius, 28px padding, 0.5px hairline.
- Navigation header: 72px height, transparent dark background, backdrop blur, 0.5px bottom border.
- Active link: Signal Blue text or tiny underline, not a large fill.
- Focus ring: Ring Blue at low alpha.
- Product mockups: use thin panels, dark tables, node diagrams, and subtle blue/mint/coral marks.

## Layout And Imagery

Use a 1080px max-width page with compact sections. Keep information density high but organized. Product imagery should look like operational software: dashboards, workflow nodes, table panels, logs, and diagram cards. Avoid wide empty marketing heroes unless there is a strong product visual behind the headline.

## Do

- Use weight 400 for all headlines 32px and above.
- Use Bone filled primary CTAs, not chromatic CTAs.
- Use 0.5px borders for card edges, dividers, and panel outlines.
- Enable Inter `ss01` and `ss03`.
- Stack surfaces from Void to Graphite to subtle white-alpha hover states.
- Use tight tracking at body sizes.
- Use Signal Blue only for active states, links, and icon accents.

## Do Not

- Do not use weight 600+ for headlines.
- Do not use blue or any chromatic color for CTA buttons.
- Do not use 1px or thicker borders for the default surface treatment.
- Do not turn the page into a neon cyberpunk interface.
- Do not use heavy drop shadows.
- Do not introduce large gradients.
- Do not make the UI loose, airy, or marketing-heavy.
