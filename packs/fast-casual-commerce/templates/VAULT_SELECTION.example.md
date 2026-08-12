# Vault Selection — Fast-Casual Commerce Example

## Target

- Product: Ember Kitchen Ordering
- Build type: Multi-branch restaurant commerce prototype
- Primary users: Local delivery and pickup customers
- Primary action: Place a valid order
- Domain pack: `packs/fast-casual-commerce/`

## Primary visual system

- Production theme: Fast-Casual Commerce
- Path: `packs/fast-casual-commerce/production-theme.json`
- Why it fits: Product-first hierarchy, visible prices and availability, compact commerce typography, realistic food photography, restrained motion, and strong mobile ordering behaviour.

## Supporting references

Select actual vault references after running the style and screen selectors.

- Catalog screen reference: one reference for product-card density and category navigation.
- Product-detail screen reference: one reference for option hierarchy.
- Checkout screen reference: one reference for form and summary composition.

Do not mix unrelated brand styles. Do not copy another restaurant’s exact menu card, navigation, checkout, photography, or motion.

## Commerce blueprints

- `restaurant-ordering-home`
- `menu-catalog`
- `product-customizer`
- `cart-review`
- `checkout`
- `order-confirmation`
- `order-tracking`
- `branch-locator`
- `delivery-zone-checker`

Include deals and loyalty only when verified.

## Content direction

- Products and prices before brand story.
- Product names 2–8 words.
- Product descriptions 8–24 words.
- Specific action labels.
- Branch, fulfilment, hours, fees, minimums, and availability remain easy to find.
- No unsupported delivery-time, product-quality, or popularity claims.

## Asset direction

- One consistent square catalog-photography system.
- Separate product-detail, process, store, and fulfilment imagery.
- Owner-provided or clearly licensed assets preferred.
- Generated food imagery is conceptual, recorded in `ASSET_PLAN.md`, and requires owner confirmation.
- No repeated hero image across unrelated sections.

## Motion direction

- Model: Microinteraction-led
- Intensity: Subtle
- Patterns: Button press, loading button, selected-category transition, cart drawer, total change
- Reduced motion: Immediate final states, no cart-flight, no parallax, no animated order progress

## Adaptation and originality

Use the pack’s product hierarchy, component contracts, states, and responsive rules. Create original brand tokens, layouts, copy, assets, and motion. Do not copy Dodo Pizza or another food business.

## QA

- Menu, customiser, cart, checkout, confirmation, and exceptional states rendered.
- Desktop, laptop, tablet, mobile, 200% zoom, keyboard, screen reader, and reduced motion checked.
- Cart recalculation, payment pending, payment failure, store closed, delivery-zone failure, and unavailable product recovery checked.
