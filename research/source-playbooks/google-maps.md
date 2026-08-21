# Google Maps Business Source Playbook

Use this playbook when the primary source is a Google Maps/Google Business Profile listing.

## Objective

Convert the listing into a high-confidence Business Source Report without importing assumptions from unrelated web results.

## Extract first

Capture the following exactly when visible:

- business name;
- category/categories;
- complete displayed address;
- displayed phone number;
- displayed business website URL;
- rating and review count as separate source values unless the source presents a combined string;
- all seven opening-hours lines in source order;
- service/amenity attributes such as dine-in, takeaway, delivery, drive-through, wheelchair access, outdoor seating or appointment requirements only when visibly supported;
- price range only when explicitly displayed;
- location/branch identity when multiple branches exist.

Do not compute `open now`, normalize address formatting, reformat phone numbers, round ratings or replace the website with the Maps URL.

## Reviews

When reviews are selected for the build, capture author, rating, relative time and full review text verbatim. Preserve typos, paragraph breaks, emoji, curly punctuation and unusual casing. Do not manufacture representative reviews or summarize a review and present it as a quote.

Review themes such as `fast service`, `spicy food` or `family friendly` may be inferred separately only after the verbatim evidence is stored.

## Photos and visual signals

Treat photos associated with the listing as business evidence, but record their exact source/provenance and whether the build is permitted to hotlink/use them. Do not silently replace failed images with stock or generated media.

From inspected imagery, the research agent may infer visual signals such as dominant colors, environment, cuisine/product category, storefront character or interior mood. These belong in `inference.brandSignals.visualSignals`, not verified facts.

## Restaurant/venue cautions

A food item visible in a review/photo is not automatically a complete menu item with a price, ingredients or availability. A user review mentioning a product is evidence that the reviewer discussed it, not proof that it is currently offered.

Do not create menu categories, delivery zones, reservation policies, branches, parking claims or prices unless supported by the source or another explicitly inspected evidence source.

## Evidence target

A strong Maps report should usually include evidence records for identity, contact/location, hours, rating/review count, primary offer/category, each operational attribute used in the build, and every asset family included in the allowlist.

## Blocked/partial access

If Maps content is blocked or only partial metadata is available, set `accessStatus` to `partial` or `blocked`. Try other user-authorized/public evidence sources, but retain them as distinct source records. Do not state that the Maps listing was inspected when it was not.

## Default asset stance

Prefer `allowlist-only` when the user expects the website to use only extracted business imagery. Use `verified-plus-generated-concept` only when generated concept imagery is explicitly allowed and it will be distinguished from official business media.
