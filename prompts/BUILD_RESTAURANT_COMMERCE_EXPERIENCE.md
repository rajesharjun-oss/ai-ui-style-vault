# Build a Premium Restaurant Commerce Experience

Use this prompt when a user asks for a restaurant, cafe, bakery, takeaway, pickup, delivery, online menu, food-ordering, quick-service, fast-casual, or multi-branch food-commerce website or application.

This prompt is mandatory together with:

- `AGENTS.md`
- `PRD.md`
- `PROMPTS.md`
- `PACKS.md`
- `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
- `packs/fast-casual-commerce/pack.json`
- `prompts/VISUAL_QA_AND_REVISION.md` after first render

## Goal

Build an original, product-first ordering experience that helps customers choose a branch or service area, select fulfilment, browse available products, configure items, review a cart, complete checkout, receive verified confirmation, and understand order status.

Do not build only a promotional landing page unless the business explicitly does not support online ordering.

## Phase 1 — Verify the commerce model

Research and record in `BUSINESS_RESEARCH.md`:

- Official business and branch names.
- Branch addresses and verified hours.
- Supported fulfilment modes.
- Delivery areas, minimums, fees, and scheduling when verified.
- Menu categories, products, variants, modifiers, prices, and availability source.
- Deals, coupons, loyalty, and eligibility rules.
- Payment methods and providers.
- Order-confirmation and tracking capabilities.
- Contact, support, refund, cancellation, allergen, and privacy information.
- Information requiring owner confirmation.

Do not infer prices, delivery coverage, opening status, loyalty value, preparation time, or product availability from design references.

## Phase 2 — Define transactional scope

Classify every requested capability as:

- `verified-and-supported`
- `design-only-prototype`
- `requires-integration`
- `requires-owner-confirmation`
- `out-of-scope`

Create `COMMERCE_BUILD_CONTRACT.md` and identify:

- Source of truth for branch, menu, availability, price, cart, promotions, tax, fees, payment, and order status.
- Guest and account paths.
- Fulfilment modes.
- Cart persistence.
- Checkout steps.
- Payment idempotency and recovery.
- Order creation and tracking.
- Exceptional states.
- Analytics and consent.

Do not imply a prototype action creates a real order.

## Phase 3 — Select the pack and visual direction

Read `PACKS.md`, `packs/pack-index.json`, and every required file in the Fast-Casual Commerce pack.

Create `VAULT_SELECTION.md` with:

- One primary production theme.
- One primary style bundle.
- Page-specific references only where needed.
- The Fast-Casual Commerce pack.
- One restrained motion model.
- Asset and photography direction.
- Originality boundaries.

Use commerce structure from the pack, not another restaurant’s protected expression.

## Phase 4 — Plan content and assets

Create `CONTENT_PLAN.md` and `ASSET_PLAN.md`.

Prioritise:

- Branch and fulfilment context.
- Categories and products.
- Prices and availability.
- Required choices.
- Cart total and conflicts.
- Checkout and confirmation.
- Practical information.

For product photography:

- Use one consistent catalog system.
- Use realistic food unless illustration is explicitly requested.
- Use process imagery for process claims.
- Do not repeat one hero image through the site.
- Record provenance and label generated imagery as conceptual.

## Phase 5 — Implement the ordering system

Implement only verified or clearly marked prototype capabilities.

Required architecture when ordering is in scope:

1. Branch or delivery-address selection.
2. Fulfilment selection.
3. Service-status handling.
4. Category navigation.
5. Product catalog with price and availability.
6. Product customiser with validation and live total.
7. Cart with quantity, edit, remove, discount, fee, total, and conflict handling.
8. Checkout with contact, fulfilment, address or branch, payment, consent, and final review.
9. Verified confirmation.
10. Order-status or a truthful explanation that tracking is unavailable.

Add deals, loyalty, scheduled ordering, saved addresses, map, or courier tracking only when supported.

## Phase 6 — Implement operational states

Use `packs/fast-casual-commerce/state-vocabulary.json`.

At minimum, cover the relevant states for:

- Loading and failed menu.
- Empty category.
- Out of stock.
- Store closed.
- Delivery unavailable.
- Outside delivery zone.
- Missing required option.
- Modifier unavailable.
- Minimum order not met.
- Coupon applied, invalid, and expired.
- Branch or address change.
- Cart recalculation and conflict.
- Payment pending and failed.
- Order confirmed, delayed, cancelled, and tracking unavailable.
- Offline cart.

Do not silently remove items or modifiers. Do not mark an order confirmed without a verified order identifier.

## Phase 7 — Accessibility and responsive implementation

Follow `packs/fast-casual-commerce/accessibility-and-responsive.md`.

The full flow must work with keyboard, screen reader, touch, 200% zoom, reduced motion, mobile software keyboard, narrow screens, slow network, and request failure.

Test sticky headers, category rails, bottom cart actions, customiser action bars, checkout buttons, safe areas, and browser zoom for overlap.

## Phase 8 — Visual QA and correction

After first render, execute `prompts/VISUAL_QA_AND_REVISION.md`.

Capture and inspect:

- Ordering home.
- Menu catalog and each category pattern.
- Product customiser.
- Cart.
- Checkout.
- Confirmation and tracking.
- Store-closed, unavailable, conflict, payment-failed, and empty states.
- Desktop, laptop, tablet, and mobile.

Correct:

- Menu delayed by decorative marketing.
- Hidden prices.
- Oversized type.
- Repeated or inconsistent imagery.
- Low-resolution or artificial-looking food.
- Sticky overlap.
- Cart or checkout content covered on mobile.
- Unclear totals or price changes.
- Broken or ambiguous actions.
- Unsupported business claims.

## Phase 9 — Validation and handoff

Run install, lint, typecheck, tests, build, accessibility, link, console, content, asset, and domain-pack checks when available.

Final handoff must distinguish:

- Real integrated functions.
- Prototype-only functions.
- Verified business data.
- Sample or provisional menu data.
- Generated, stock, licensed, and owner-provided assets.
- Required credentials or integrations.
- Exact local or deployed access instructions.
- Remaining risks and owner-confirmation items.

Reject completion when the result is only visually attractive but cannot support the verified ordering journey or recover safely from common commerce failures.
