# Style Selection Guide

Use this guide to choose the best visual direction for a website, web app, web tool, SaaS product, dashboard, or mobile app.

## Selection Inputs

Collect these facts from the target repository and user request:

- Product type: SaaS, dashboard, AI tool, developer tool, marketplace, ecommerce, finance, health, education, portfolio, media, or consumer app.
- Primary user: consumer, creator, operator, developer, executive, admin, patient, buyer, seller, or internal staff.
- Page needs: landing, dashboard, login, settings, profile, product details, catalog, pricing, blog, docs, integrations, contacts, careers, 404.
- Interaction density: low, medium, high, or command-center.
- Data density: editorial, card-based, table-heavy, chart-heavy, media-heavy, or form-heavy.
- Tone: calm, premium, playful, technical, editorial, cinematic, utilitarian, warm, clinical, or experimental.
- Accessibility constraints: contrast, motion sensitivity, keyboard workflow, language length, mobile use.
- Implementation stack: Tailwind, CSS modules, shadcn/ui, custom CSS, design tokens, native mobile, or other.

## Scoring

Score each candidate style bundle out of 100.

| Signal | Weight | What to Check |
|---|---:|---|
| Product/domain fit | 25 | `category`, `bestFor`, `tags`, and `summary` match the product. |
| Page coverage | 20 | Available screen references match the needed page types. |
| Interaction density | 15 | The style supports the product's amount of controls, tables, forms, and state. |
| Tone fit | 15 | `northStar`, theme, typography, imagery, and palette fit the brand direction. |
| Implementation fit | 10 | Tokens and code artifacts map cleanly to the target stack. |
| Accessibility fit | 10 | Contrast, type scale, motion, and spacing can support real use. |
| License risk | 5 | Reference can be used as inspiration without copying protected assets. |

Choose the highest-scoring option unless the target product has a hard constraint the score missed.

## Candidate Reading Order

For a style folder:

1. `style.json`
2. `README.md`
3. `DESIGN.md`
4. `implementation-prompt.md`
5. `tokens/colors.md`
6. `tokens/typography.md`
7. `tokens/spacing-shape.md`
8. `tokens/components.md`
9. `tokens/guidelines.md`
10. `code/design-tokens.json`
11. `code/css-variables.css`
12. `code/tailwind-v4.css`

For a screen folder:

1. `screen.json`
2. `README.md`
3. `implementation-prompt.md`
4. `tokens/page-elements.md`
5. `tokens/colors.md`
6. `code/design-tokens.json`
7. `code/css-variables.css`

## Style vs Screen References

Use style bundles for:

- Global color system
- Typography
- Radius and spacing
- Button and card styling
- Motion attitude
- Overall brand feel
- Design do/don't rules

Use screen references for:

- Page-level information architecture
- Common sections
- Empty states
- Form shape
- Navigation placement
- Dashboard density
- Mobile app screen behavior
- Product detail or catalog composition

## Combining References

Use one primary style. Add supporting references only for a concrete reason.

Good combination:

- Primary style: developer-tool visual system.
- Supporting screen: dashboard layout reference.
- Supporting screen: login layout reference.

Risky combination:

- Three unrelated brand styles mixed together.
- A cinematic landing style forced onto a dense admin panel.
- A playful consumer app style used for a high-trust finance workflow without restraint.

## Implementation Translation

Translate the chosen style into the target repo using this order:

1. Design tokens: colors, typography, radius, spacing, shadows, borders.
2. App shell: nav, sidebar, header, page width, background layers.
3. Core components: buttons, inputs, cards, tables, tabs, menus, modals.
4. Page compositions: dashboard, landing, login, settings, product details, etc.
5. States: loading, empty, error, success, disabled, hover, focus, active.
6. Responsive behavior: mobile, tablet, desktop, wide desktop.
7. Accessibility: contrast, semantic HTML, labels, focus order, reduced motion.

## Final Selection Output

Before coding, an agent should produce:

```text
Primary style: <name> at <path>
Supporting screens: <paths>
Why this fits: <short rationale>
Adaptation plan: <tokens/components/layouts to use>
Copy/asset policy: no logos, screenshots, proprietary text, or brand clone
Implementation notes: <target stack mapping>
```
