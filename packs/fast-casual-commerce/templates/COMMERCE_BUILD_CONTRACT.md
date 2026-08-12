# Commerce Build Contract

Complete this contract before implementing transactional restaurant-commerce features.

## Business and operating model

- Business:
- Market and currency:
- Timezone:
- Branch model:
- Primary customers:
- Primary conversion:
- Owner-confirmation contact:

## Capability classification

For each capability, mark one:

- `verified-and-supported`
- `design-only-prototype`
- `requires-integration`
- `requires-owner-confirmation`
- `out-of-scope`

| Capability | Classification | Source of truth | Notes |
|---|---|---|---|
| Branches and hours |  |  |  |
| Delivery |  |  |  |
| Pickup |  |  |  |
| Dine-in or takeaway |  |  |  |
| Menu and categories |  |  |  |
| Product variants |  |  |  |
| Modifiers |  |  |  |
| Availability |  |  |  |
| Pricing |  |  |  |
| Deals and coupons |  |  |  |
| Loyalty |  |  |  |
| Delivery zone |  |  |  |
| Fees and minimums |  |  |  |
| Scheduled ordering |  |  |  |
| Customer accounts |  |  |  |
| Payment |  |  |  |
| Order creation |  |  |  |
| Order tracking |  |  |  |
| Refund and cancellation |  |  |  |
| Support |  |  |  |

## Data contracts

- Branch source:
- Menu source:
- Availability source:
- Price source:
- Promotion source:
- Loyalty source:
- Address and zone source:
- Fee and tax source:
- Payment provider:
- Order API:
- Tracking API:
- Analytics and consent:

## Primary journey

Document the verified journey:

```text
branch or address → fulfilment → menu → customiser → cart → checkout → payment → confirmation → tracking
```

Remove unsupported steps rather than simulating them as real.

## Branch and fulfilment rules

- How branch is selected:
- How fulfilment is selected:
- How opening status is determined:
- What happens when branch changes:
- What happens when fulfilment changes:
- Scheduling support:
- Closed-store alternatives:

## Menu and product rules

- Category order:
- Product-card fields:
- Price-label rules:
- Required option groups:
- Optional modifier rules:
- Selection limits:
- Allergen and dietary source:
- Out-of-stock behaviour:
- Product-image source and provenance:

## Cart rules

- Persistence method:
- Anonymous and signed-in behaviour:
- Quantity limits:
- Edit and remove behaviour:
- Revalidation triggers:
- Conflict handling:
- Minimum order:
- Fees:
- Tax:
- Promotion stacking:
- Loyalty interaction:
- Offline behaviour:

## Checkout rules

- Guest checkout:
- Required customer fields:
- Address validation:
- Delivery instructions:
- Pickup instructions:
- Payment methods:
- Consent and terms:
- Idempotency method:
- Duplicate-submission prevention:
- Payment-pending recovery:
- Payment-failure recovery:
- Order-creation failure after payment authorisation:

## Confirmation and tracking

- Confirmation source:
- Order identifier:
- Receipt source:
- Status vocabulary:
- Estimate source:
- Tracking source:
- Delayed-order path:
- Cancellation path:
- Support path:

## Operational states

List the relevant states from `state-vocabulary.json` and describe the UI and recovery for each.

## Accessibility and responsive contract

- Keyboard path:
- Screen-reader status and error announcements:
- Focus management:
- 200% zoom behaviour:
- Mobile customiser:
- Mobile cart:
- Mobile checkout:
- Safe-area behaviour:
- Reduced-motion behaviour:
- Slow-network behaviour:

## Security and privacy

- Authentication:
- Payment-data boundary:
- Secrets management:
- Personal-data retention:
- Address privacy:
- CSRF and request integrity:
- Server-side price and availability validation:
- Rate limiting and abuse controls:
- Audit and monitoring:

## Asset and truthfulness contract

- Owner-provided assets:
- Licensed assets:
- Generated conceptual assets:
- Assets requiring replacement:
- Provisional data:
- Claims requiring owner confirmation:
- Features that must be labelled as prototype:

## Acceptance criteria

- [ ] Products, prices, availability, branch, and fulfilment are sourced correctly.
- [ ] Required product choices block addition until resolved.
- [ ] Cart totals and material recalculations are explicit.
- [ ] Checkout is idempotent and preserves valid data after failure.
- [ ] Payment pending is distinct from payment failed and order confirmed.
- [ ] Mobile sticky elements do not cover content or errors.
- [ ] All relevant operational states have recovery paths.
- [ ] Product photography is consistent and has documented provenance.
- [ ] Desktop, laptop, tablet, mobile, keyboard, zoom, screen-reader, and reduced-motion QA is complete.
- [ ] Handoff distinguishes integrated, prototype, provisional, and owner-confirmation items.
