# Fast-Casual Commerce Pack

A domain-specific product, content, visual, interaction, state, and engineering system for restaurant ordering, takeaway, pickup, delivery, cafe, bakery, and multi-branch food-commerce experiences.

This pack is designed to help an AI agent build a real ordering product rather than a promotional page with a large headline and a few food cards.

## Use this pack when the product needs

- A location-aware or branch-aware menu.
- Delivery, pickup, dine-in, or takeaway selection.
- Product categories, prices, availability, and modifiers.
- Product customisation, quantity selection, cart, checkout, or payment.
- Deals, coupon codes, loyalty, order confirmation, or order tracking.
- Delivery-zone validation or store-opening status.

## Required reading order

1. `pack.json`
2. `production-theme.json`
3. `page-blueprints.json`
4. `component-manifest.json`
5. `state-vocabulary.json`
6. `content-and-merchandising.md`
7. `food-photography-standard.md`
8. `accessibility-and-responsive.md`
9. `implementation-prompt.md`
10. `code/design-tokens.css`
11. `code/commerce-types.ts`
12. `code/cart-engine.ts`
13. `sample-data/menu.sample.json`
14. `templates/design-recipe.example.json`
15. `templates/COMMERCE_BUILD_CONTRACT.md`

## Product principle

The ordering journey is the product:

```text
Choose branch or address → choose fulfilment → browse menu → configure product → review cart → checkout → track order
```

Marketing content must support that journey rather than push it below several decorative sections.

## What the pack provides

- An original fast-casual production-theme archetype.
- Eleven page and flow blueprints.
- Commerce-specific component contracts.
- Operational state vocabulary and transition rules.
- Merchandising and copy guidance.
- Food-photography and asset standards.
- Accessibility and responsive behaviour.
- Framework-neutral TypeScript contracts and cart-calculation reference code.
- Sample menu data and planning templates.

## What the pack does not provide

- A copy of Dodo Pizza or another restaurant brand.
- Protected logos, photography, menu text, pricing, promotions, or proprietary code.
- A payment processor, geocoder, delivery provider, tax engine, or production backend.
- Permission to present generated imagery as official business photography.

The target project must connect real services and confirm business facts before launch.
