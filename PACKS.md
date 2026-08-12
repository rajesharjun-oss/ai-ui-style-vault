# Domain Pack Router

Domain packs extend the core AI UI Style Vault with product-specific page blueprints, components, state models, content rules, asset standards, code contracts, and implementation prompts.

Agents must follow `AGENTS.md` first. A domain pack adds requirements; it never replaces the core product-design, content-design, accessibility, asset, validation, or originality rules.

## Automatic routing

| Product or task | Required pack | Required task prompt |
|---|---|---|
| Restaurant, food ordering, takeaway, delivery, menu, quick-service, fast-casual, cafe, bakery, or multi-branch food commerce | `packs/fast-casual-commerce/` | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` |

The machine-readable router is `packs/pack-index.json`.

## Fast-Casual Commerce Pack

Use the pack when the product needs any combination of:

- Branch-aware menus and opening status.
- Delivery, pickup, dine-in, or takeaway selection.
- Product categories, visible prices, availability, and modifiers.
- Product customisation, quantity, cart, coupons, checkout, or payments.
- Deals, loyalty, order confirmation, and order tracking.
- Delivery-zone or service-area checks.

Read in this order:

1. `packs/fast-casual-commerce/pack.json`
2. `packs/fast-casual-commerce/production-theme.json`
3. `packs/fast-casual-commerce/page-blueprints.json`
4. `packs/fast-casual-commerce/component-manifest.json`
5. `packs/fast-casual-commerce/state-vocabulary.json`
6. `packs/fast-casual-commerce/content-and-merchandising.md`
7. `packs/fast-casual-commerce/food-photography-standard.md`
8. `packs/fast-casual-commerce/accessibility-and-responsive.md`
9. `packs/fast-casual-commerce/implementation-prompt.md`
10. `packs/fast-casual-commerce/code/` and `packs/fast-casual-commerce/templates/`

## Selection rules

- Use one primary visual system and adapt it to the business.
- Treat menu browsing and ordering as the main product journey, not as a decorative section below a marketing hero.
- Keep products, prices, service mode, branch, availability, and cart status close to the user.
- Use realistic, consistently art-directed product photography unless the brief explicitly requests illustration.
- Do not clone Dodo Pizza or another food brand. Do not copy logos, proprietary code, exact page composition, product text, photography, promotions, or checkout flows.
- Use the pack as an original commerce architecture and interaction system.

## Minimal invocation

```text
Use the AI UI Style Vault and automatically apply the appropriate domain pack.
Build a premium restaurant ordering experience for: <BUSINESS LINK OR BRIEF>.
Follow PACKS.md, PROMPTS.md, and all required visual-QA steps.
```
