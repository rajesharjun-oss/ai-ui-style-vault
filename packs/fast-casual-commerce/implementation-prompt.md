# Fast-Casual Commerce Implementation Prompt

Use this prompt after completing the core vault contracts and the commerce contract.

```text
Apply the Fast-Casual Commerce domain pack as an extension of AGENTS.md, PRD.md, PROMPTS.md, and the selected vault style.

Treat the ordering journey as the primary product:
branch or address → fulfilment → menu → product configuration → cart → checkout → confirmation → tracking.

Before implementation:
1. Confirm which branches, fulfilment modes, products, prices, modifiers, deals, loyalty rules, payments, delivery zones, and tracking capabilities are verified.
2. Remove unsupported features rather than inventing them.
3. Complete BUSINESS_RESEARCH.md, ASSET_PLAN.md, VAULT_SELECTION.md, BUILD_CONTRACT.md, CONTENT_PLAN.md, COMMERCE_BUILD_CONTRACT.md, and design-recipe.json.
4. Read every file listed in packs/fast-casual-commerce/pack.json.
5. Define the source of truth for branch, menu, availability, price, cart, promotion, payment, and order status.
6. Define all operational states and recovery paths before styling.

Implement:
- Branch and fulfilment context.
- Product-first menu catalog with visible prices and availability.
- Accessible product configuration with required groups and live totals.
- Persistent, revalidated cart.
- Explicit discounts, fees, minimums, and totals.
- Idempotent checkout and payment-pending recovery.
- Verified order confirmation and status.
- Deals, loyalty, delivery-zone, or tracking features only when supported.
- Responsive desktop, laptop, tablet, and mobile transformations.
- Reduced-motion, keyboard, screen-reader, slow-network, and failure behaviour.

Art direction:
- Use realistic, consistent product photography unless illustration is explicitly requested.
- Use separate catalog, process, store, fulfilment, and lifestyle imagery for their actual purposes.
- Do not reuse one photograph across unrelated sections.
- Do not present generated imagery as official business photography.
- Do not clone another restaurant’s layout, assets, product copy, promotions, or motion identity.

Reject generic output:
- No oversized marketing hero that delays menu access.
- No hidden prices.
- No paragraph-heavy product cards.
- No cartoon food in a realistic brief.
- No inconsistent image angles or crops.
- No decorative motion during checkout.
- No unsupported delivery promises, opening status, deals, loyalty value, or tracking.

Before handoff:
1. Run the project checks and python scripts/validate-domain-packs.py in the vault.
2. Render menu, customiser, cart, checkout, confirmation, exceptional states, and mobile navigation.
3. Execute prompts/VISUAL_QA_AND_REVISION.md.
4. Verify sticky elements, safe areas, keyboard flow, focus, live regions, totals, cart recalculation, and payment recovery.
5. Report verified facts, provisional data, asset provenance, integrations, checks, screenshots, and remaining owner-confirmation items.
```
