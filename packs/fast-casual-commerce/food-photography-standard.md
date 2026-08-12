# Food Photography and Asset Standard

Food-commerce imagery is part of the product interface. Inconsistent, repeated, low-resolution, misleading, or obviously synthetic images reduce trust and make product comparison harder.

## Asset provenance

Allowed sources:

- Business-owner-provided photography with permission.
- Original commissioned photography.
- Original generated imagery recorded as conceptual.
- Owned local assets.
- Clearly licensed stock or marketplace assets with licence notes.

Do not:

- Hotlink business, competitor, Maps, social-media, delivery-platform, or reference-site images.
- Copy another brand’s product photography.
- Present generated or stock imagery as official business photography.
- Use screenshots as product images.
- Reuse a reference brand’s logo, packaging, uniforms, interior, or branded props.

Record every major asset in `ASSET_PLAN.md` with source, ownership or licence, intended use, crop, mobile treatment, and fallback.

## Shot taxonomy

Use different imagery for different claims:

### Catalog product photography

Purpose: compare products and choose.

- Use a consistent camera angle across the catalog.
- Use a consistent background or controlled background family.
- Keep product scale and crop consistent.
- Show the product clearly, not buried under props.
- Prefer square or near-square source images for cards.

### Product-detail photography

Purpose: inspect the selected product.

- Use a larger crop with visible ingredients and texture.
- Keep the image representative of the configurable base product.
- Do not show paid extras as included unless clearly labelled.

### Process photography

Purpose: prove preparation, freshness, craft, open kitchen, oven, or quality claims.

- Show the actual process being claimed: dough preparation, topping, baking, packing, handoff, or kitchen activity.
- Do not use another finished-product hero image to illustrate process.
- Avoid staged imagery that conflicts with the verified business operation.

### Store and location photography

Purpose: help customers recognise and trust the branch.

- Use exterior, entrance, counter, seating, pickup area, or relevant accessibility views.
- Keep address and directions as text; do not make an image the only location cue.

### Delivery and pickup photography

Purpose: explain fulfilment.

- Use packaging, handoff, pickup shelf, counter, or delivery context only when it reflects the business.
- Do not imply a delivery fleet, packaging standard, or app feature that is not verified.

### Lifestyle photography

Purpose: show occasion and audience.

- Use sparingly.
- Keep the product and customer context believable.
- Do not let lifestyle imagery replace menu photography.

## Catalog consistency matrix

Before implementation, define and preserve:

| Attribute | Decision |
|---|---|
| Camera angle | Overhead, three-quarter, or another single primary angle |
| Background | One neutral surface or controlled family |
| Lighting | One temperature and direction |
| Product scale | Consistent percentage of frame |
| Crop | Consistent safe area and card ratio |
| Colour treatment | One calibrated grade |
| Shadow | Consistent natural or removed treatment |
| Props | Minimal and repeatable |
| Resolution | Sufficient for high-density displays |
| File format | AVIF/WebP with suitable fallback where required |

Do not combine overhead studio products, dark restaurant plates, phone photographs, cartoon renders, and glossy generated images in one catalog without a deliberate system and strong reason.

## Technical requirements

- Provide explicit width and height or aspect ratio to prevent layout shift.
- Use responsive `srcset` or framework image optimisation where available.
- Compress without visible food-detail damage.
- Lazy-load offscreen images; do not lazy-load the primary first-viewport image when it harms perceived loading.
- Use appropriate colour profiles.
- Test low-bandwidth and failed-image states.
- Provide meaningful alternative text for informative images and empty alt text for purely decorative images.
- Keep text out of the image unless the image is itself a verified promotional asset and accessible text is also provided.

## Generated imagery requirements

When generated imagery is used:

- Record the prompt purpose and generation date in `ASSET_PLAN.md`.
- Label it as conceptual in handoff notes.
- Remove third-party logos, protected packaging, illegible text, impossible ingredients, duplicated toppings, malformed utensils, and inconsistent shadows.
- Keep the same art direction across the set.
- Do not use generated imagery to prove a factual claim about the business’s kitchen, branch, staff, packaging, or product appearance.
- Obtain owner confirmation before presenting generated products as representative of the menu.

## Quality gates

Reject or replace an image when:

- It is visibly soft, stretched, compressed, or upscaled.
- The crop cuts off the product unpredictably.
- Lighting or background conflicts with the catalog system.
- The product does not match the listed ingredients or configuration.
- The same image is repeated across unrelated sections.
- It looks cartoonish when the brief requires realistic food.
- It contains another brand’s protected visual identity.
- It falsely implies an operational fact.

## Rendered review

At desktop, laptop, and mobile sizes, check:

- Product images remain comparable.
- Images do not dominate price and action.
- Text overlays remain readable.
- No important product detail is lost in crop.
- Low-resolution assets are obvious and replaced.
- Process claims use process imagery.
- Mobile cards do not force tiny images or excessive vertical scrolling.
