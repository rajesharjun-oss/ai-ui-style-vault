# Fast-Casual Commerce Content and Merchandising Standard

The purpose of content in a restaurant-commerce experience is to help the customer decide, configure, trust, and complete an order. It is not to turn the menu into a marketing essay.

## Information priority

Use this order unless the verified business model requires otherwise:

1. Branch or service-area context.
2. Fulfilment mode and current availability.
3. Menu categories.
4. Product identity and photography.
5. Price and availability.
6. Required configuration.
7. Cart status and total.
8. Checkout, payment, and confirmation.
9. Deals, loyalty, brand story, and secondary marketing.

## Menu architecture

- Use category names customers already understand.
- Keep the number of top-level categories manageable; group rarely used or small categories only when the grouping remains obvious.
- Preserve the selected category while scrolling and after returning from a product customiser.
- Order categories by customer demand, business priority, or verified merchandising strategy—not alphabetically by default.
- Do not create a category containing one weak item merely to fill navigation.
- Keep branch-specific availability and pricing as the source of truth.

## Product-card content budget

A catalog card should normally contain:

- Product name: 2–8 words.
- Description: 8–24 words.
- Price or starting price.
- One concise availability or promotional label when needed.
- One clear action: `Add`, `Choose`, `Customise`, or another specific verb.

Do not include long ingredient stories, preparation essays, multiple badges, nutrition detail, and cross-sell copy on the card. Move secondary information into the product detail or customiser.

## Product names and descriptions

- Use the verified menu name.
- Describe the main ingredients or flavour in plain language.
- Do not invent claims such as “best-selling,” “artisan,” “organic,” “healthy,” or “award-winning.”
- Do not use vague copy such as “a taste sensation” when concrete ingredients are known.
- Keep dietary and allergen information factual and sourced.
- Make optional removals and additions clear in the customiser rather than implying them in marketing copy.

## Price rules

- Show the actual price whenever the business provides it.
- Use `From` only when the lowest valid configuration genuinely starts at that price.
- Associate price deltas with the exact option or modifier.
- Update line and cart totals immediately after valid selections.
- Distinguish subtotal, discounts, delivery or service fees, tax when applicable, loyalty redemption, and final total.
- Do not reveal unavoidable fees only after the customer reaches payment.
- Do not fabricate prices for a design prototype. Mark unconfirmed values as sample data in planning and handoff notes.

## Availability rules

- Do not make unavailable items look purchasable.
- Prefer a specific state such as `Out of stock`, `Unavailable at this branch`, or `Available from 12:00` only when verified.
- Preserve discoverability for temporarily unavailable products when useful, but disable purchase and explain the state.
- Revalidate availability after branch, address, fulfilment, time, or option changes.
- Do not silently remove an unavailable cart item.

## Deals and promotions

Every deal must state, when applicable:

- The customer benefit.
- Eligible products or order value.
- Eligible branch or service mode.
- Valid dates or times.
- Use limit.
- Promo code.
- Exclusions.
- How the cart total changes.

Do not use urgency language or countdowns unless the expiry is authoritative. Do not hide conditions behind a purchase action.

## Loyalty

Explain:

- What the balance represents.
- How value is earned.
- How value is redeemed.
- Eligibility and minimums.
- Expiry.
- Whether redemption affects promotions or fees.

Do not present points as currency without explaining conversion and restrictions.

## Cross-sell and recommendations

- Recommend only products that are available and relevant to the current item or cart.
- Place recommendations after the primary product decision, not before required options or unresolved conflicts.
- Limit suggestions to a small, prioritised set.
- Never use recommendations to obscure the cart total or checkout action.
- Label paid upgrades and price changes clearly.

## Store and fulfilment content

Keep these easy to find:

- Branch name and address.
- Current opening status.
- Verified hours by fulfilment mode when they differ.
- Delivery, pickup, dine-in, or takeaway availability.
- Minimum order and fees when applicable.
- Service-area eligibility.
- Contact and directions.
- Verified order estimate or scheduling option.

Do not promise delivery times, coverage, or opening status that the system cannot verify.

## Checkout language

Use task-specific labels:

- `Deliver to this address`
- `Pick up from this branch`
- `Apply code`
- `Review order`
- `Place order`
- `Try payment again`
- `Contact support`

Avoid vague labels such as `Continue`, `Submit`, or `Learn more` when a more specific action is available.

## Error and recovery content

Every error should explain:

1. What happened.
2. What it affects.
3. What the customer can do now.
4. Whether the cart, payment, or order was preserved.

Never imply an order was placed when only payment was attempted. Never imply payment failed when the status is merely pending.

## Content-density review

Before handoff, inspect the rendered experience and remove:

- Introductory paragraphs before products.
- Repeated category or product descriptions.
- Redundant promotional badges.
- Explanations of obvious controls.
- Marketing claims inside checkout.
- Large headings that displace menu or cart information.

A premium commerce interface is clear because it prioritises decisions, not because it contains more copy.
