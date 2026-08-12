# Fast-Casual Commerce Code Contracts

These files are framework-neutral references, not a production backend.

- `design-tokens.css` provides semantic visual and layout tokens.
- `commerce-types.ts` defines branch, menu, options, cart, payment, and order contracts.
- `cart-engine.ts` demonstrates integer-money calculation, configuration validation, cart totals, conflict handling, and recalculation descriptions.

## Required production boundaries

- Treat all browser totals as provisional.
- Revalidate price, availability, branch, address, fulfilment, promotions, fees, tax, payment, and order creation on the server.
- Use idempotency keys for payment and order submission.
- Do not embed payment secrets, private API keys, delivery credentials, or administrative tokens in client code.
- Replace sample data and status with real integrations or label the experience clearly as a prototype.
- Localise currency, dates, address, tax, and legal content for the actual market.

Map the contracts into the target stack rather than forcing a new framework.
