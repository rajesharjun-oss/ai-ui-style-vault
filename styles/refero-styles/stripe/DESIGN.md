# Stripe Style Reference

Stripe is a global commerce infrastructure style. It uses cool-white ledger surfaces, deep navy typography, precision 4px geometry, weight-300 type, quiet borders, and one indigo action color. The mood should be highly competent, calm, technical, and built for scale.

## Theme

Light, fintech, infrastructure, developer platform, ledger, global commerce, cool-white, precise, data-rich.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Deep Navy | `#0a2540` | `--color-deep-navy` | Primary text, dark panels, footer anchors, and code headings. |
| Slate Ledger | `#425466` | `--color-slate-ledger` | Body copy, navigation labels, and secondary headings. |
| Blue Gray | `#6b7c93` | `--color-blue-gray` | Muted body copy, metadata, captions, and helper labels. |
| Border Mist | `#e6ebf1` | `--color-border-mist` | Hairline dividers, card borders, and section rules. |
| Grid Line | `#d6dee8` | `--color-grid-line` | Charts, table rules, and subtle grid structure. |
| Cloud Ledger | `#f5f7fb` | `--color-cloud-ledger` | Page background and pale section canvas. |
| Paper White | `#ffffff` | `--color-paper-white` | Card, panel, terminal, and nav surfaces. |
| Indigo Action | `#635bff` | `--color-indigo-action` | Primary CTA, active links, arrows, and selected states. |
| Cyan Accent | `#00d4ff` | `--color-cyan-accent` | Small chart accents and data sparks only. |
| Green Ledger | `#00a86b` | `--color-green-ledger` | Positive status, growth indicators, and accepted payments. |
| Amber Notice | `#f6a609` | `--color-amber-notice` | Warnings, small badges, and narrow status strips. |

## Typography

### sohne-var

Use as the primary and nearly exclusive type family.

- Token: `--font-sohne-var`
- Fallback: Inter, system-ui, Helvetica Neue
- Weights: 300, 400, 500, 600
- Sizes: 13px, 14px, 15px, 16px, 17px, 24px, 31px, 51px, 56px, 82px
- Line height: 1.00 to 1.73
- Letter spacing: slightly negative at heading sizes, open at captions.
- Role: precise infrastructure voice for headings, copy, buttons, forms, and tables.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 13px | 1.54 | 0.2px | `--text-caption` |
| Body SM | 15px | 1.60 | 0 | `--text-body-sm` |
| Body | 16px | 1.56 | 0 | `--text-body` |
| Body LG | 17px | 1.73 | 0 | `--text-body-lg` |
| Heading SM | 24px | 1.25 | -0.24px | `--text-heading-sm` |
| Heading | 31px | 1.23 | -0.31px | `--text-heading` |
| Heading LG | 51px | 1.08 | -1.53px | `--text-heading-lg` |
| Display | 56px | 1.07 | -1.68px | `--text-display` |
| Display XL | 82px | 1.00 | -2.46px | `--text-display-xl` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1080px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96`

### Radius Scale

| Element | Radius |
|---|---:|
| Cards | 4px |
| Buttons | 4px |
| Inputs | 4px |
| Pills | 999px |
| Code panels | 4px |

## Components

### Indigo Primary Button

Indigo Action fill, Paper White text, 4px radius, 8px 16px padding, sohne-var 15px/500. Include a small right arrow when the action advances.

### Navy Secondary Button

Deep Navy fill, Paper White text, 4px radius, same size as primary. Use beside indigo only when a second high-confidence action is needed.

### Ghost Text Link

Transparent, Deep Navy or Indigo text, no border, 15px/500, small arrow icon. Use for inline product links and card actions.

### Top Navigation

Paper White or transparent nav over Cloud Ledger. Logo left, compact center links, and paired right CTAs. Use 14px to 15px sohne-var and no background blur.

### Hero Ledger Block

Two-column hero with display heading, short body copy, paired CTA buttons, and a right-side product mockup. Use Cloud Ledger canvas and one Indigo action.

### Product Mockup Card

Paper White surface, 4px radius, 1px Border Mist border, no shadow, dense internal chart/table/code content.

### Data Table

Paper White or transparent rows, 1px Border Mist row dividers, 13px to 14px text, Blue Gray metadata, Deep Navy values, small status chips.

### Code Panel

Deep Navy or Paper White panel with 4px radius, monospace-like spacing through sohne-var or a system mono fallback, muted line numbers, and indigo/cyan syntax accents.

### Metric Tile

Paper White, 4px radius, 1px Border Mist border, caption at 13px, value at 31px, optional Green Ledger delta.

### Globe Or Map Panel

Cool blue-gray world map or grid visualization on Cloud Ledger/Paper White. Use hairline grid and tiny Indigo or Cyan nodes.

### Payment Method Strip

Horizontal icon row, Paper White background, Border Mist separators, Deep Navy labels, muted Blue Gray captions.

### Footer Infrastructure Grid

Deep Navy footer or Cloud Ledger sitemap with tight link columns. Use Blue Gray links and white/navy headings depending on background.

## Layout

Use a centered 1080px content rail. Keep sections wide but structured with horizontal divider lines. Hero should be grid-based with type on the left and a product/data mockup on the right. Alternate Cloud Ledger backgrounds with Paper White cards. Use dense but breathable product modules: tables, charts, map panels, API snippets, and payment rails. Avoid decorative cards; every surface should communicate data, workflow, or product proof.

## Imagery

Use product UI, abstracted payment flows, ledger tables, world maps, charts, code snippets, terminal panels, and payment logos. Avoid lifestyle photography, oversized illustrations, gradients as main content, cartoon icons, and decorative blobs. The style can tolerate subtle cool gradients only inside product graphics, not as page decoration.

## Do

- Use sohne-var at weight 300 for large headings and most body text.
- Use Indigo Action for the main CTA and active states.
- Keep 4px radius on cards, buttons, inputs, and code panels.
- Use hairline dividers and table rules to create structure.
- Use Deep Navy for text and dark infrastructure panels.
- Use Cloud Ledger as the main cool-white page background.
- Keep data/product modules dense but aligned.
- Use small arrows on links and action buttons.

## Don't

- Do not add card shadows.
- Do not use a multicolor marketing palette.
- Do not make indigo a full-page background.
- Do not use rounded SaaS cards above 4px.
- Do not use expressive serif or display fonts.
- Do not use stock photography as primary imagery.
- Do not make body text heavier than 400.
- Do not add decorative gradients behind sections.
