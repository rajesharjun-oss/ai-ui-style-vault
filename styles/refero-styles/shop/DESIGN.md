# Shop Style Reference

Shop is a light commerce-discovery system built for browsing. It combines a white canvas, soft mist product surfaces, pill-shaped search controls, large rounded cards, literal product imagery, and a single violet action color. It should feel effortless, modern, consumer-friendly, and fast to scan.

## Theme

Light, commerce, shopping, marketplace, consumer app, white canvas, pill search, rounded product cards, product photography.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Ink Black | `#171717` | `--color-ink-black` | Primary text, nav labels, product names, and high-contrast UI. |
| Carbon | `#000000` | `--color-carbon` | Literal icon fills, app-store badges, and deep graphic marks only. |
| Graphite | `#666666` | `--color-graphite` | Body copy, merchant details, helper text, and secondary labels. |
| Ash | `#999999` | `--color-ash` | Tertiary metadata, inactive nav, muted labels, and captions. |
| Hairline | `#d9d9d9` | `--color-hairline` | Dividers, subtle card outlines, and input borders. |
| Soft Gray | `#f5f5f5` | `--color-soft-gray` | Secondary card surfaces and product placeholders. |
| Product Mist | `#f0f4f5` | `--color-product-mist` | Product grid cards and image wells. |
| Mist Blue | `#f4f8fa` | `--color-mist-blue` | Hero background bands, search containers, and pale commerce sections. |
| Pure White | `#ffffff` | `--color-pure-white` | Page canvas, cards, overlays, and text on dark graphic marks. |
| Shop Violet | `#5433eb` | `--color-shop-violet` | Primary search action, active states, and focused ecommerce controls. |
| Checkout Green | `#008060` | `--color-checkout-green` | Payment success, trusted checkout marks, and positive status only. |

## Typography

### GTStandard-MRegular

Use for display, body, UI, navigation, product names, buttons, and metadata.

- Token: `--font-gtstandard`
- Fallback: Shopify Sans, Inter, system-ui
- Weight: 400 for most text; 600 only for short UI emphasis.
- Sizes: 12px, 13px, 14px, 16px, 18px, 20px, 32px, 48px, 80px
- Line height: 1.00 to 1.50
- Letter spacing: -0.02em at display sizes, -0.01em for product names, normal for body, +0.02em for micro labels.
- Role: friendly retail clarity.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.33 | 0.24px | `--text-caption` |
| Label | 13px | 1.30 | 0.13px | `--text-label` |
| Body SM | 14px | 1.43 | 0 | `--text-body-sm` |
| Body | 16px | 1.50 | 0 | `--text-body` |
| Product | 18px | 1.30 | -0.18px | `--text-product` |
| Subheading | 20px | 1.25 | -0.2px | `--text-subheading` |
| Heading | 32px | 1.10 | -0.64px | `--text-heading` |
| Display | 48px | 1.05 | -0.96px | `--text-display` |
| Display XL | 80px | 1.00 | -1.6px | `--text-display-xl` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 64px to 96px.
- Card padding: 20px to 28px.
- Element gap: 12px to 20px.

### Spacing Scale

`4, 8, 10, 12, 16, 20, 24, 28, 32, 40, 48, 64, 80, 96`

### Radius Scale

| Element | Radius |
|---|---:|
| Search | 9999px |
| Pills | 9999px |
| Buttons | 9999px |
| Product cards | 28px |
| Lower cards | 20px |
| Icons | 12px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Floating search | `--shadow-floating-search` | `rgba(23, 23, 23, 0.08) 0px 12px 40px 0px` |
| Product hover | `--shadow-product-hover` | `rgba(23, 23, 23, 0.08) 0px 8px 24px 0px` |

Default cards are flat. Use shadows for search overlays, hover states, or floating phone/app modules only.

## Components

### Violet Search Button

Shop Violet fill, Pure White icon/text, 9999px radius, square or pill shape, GTStandard 14px to 16px. Use for search submit and the single main action.

### Search Bar

Pure White fill, 9999px radius, subtle Hairline border or floating search shadow, left icon, Graphite placeholder, and violet submit control. This is the center of the interface.

### Category Pill

Pure White or Product Mist fill, Ink Black text, 9999px radius, 12px by 20px padding, 14px text. Active state can use Ink Black fill or Shop Violet indicator.

### Product Card

Product Mist or Soft Gray fill, 28px radius, product image centered or full-bleed, product name at 18px, merchant/price metadata at 13px to 14px. Keep flat until hover.

### Merchant Badge

Small circular logo, 32px to 48px, white or brand asset inside product cards. Use literal merchant artwork.

### App Store Badge

Carbon or Ink Black rounded badge with white platform text and icon. Use literal store badge style, not a custom colorful button.

### Feature Tile

Pure White or Mist Blue surface, 20px radius, 20px to 28px padding, Ink Black heading, Graphite body, and product screenshot or icon.

### Product Grid

Three-up or four-up card grid with wide gutters, 28px card radius, and consistent image wells. Product photography should dominate each card.

### Mobile App Mockup

Phone frame or app screen stack showing product feed, checkout, or tracking. Use white/mist panels, 28px cards, and violet action controls.

### Header Nav

White or Mist Blue header, Shop wordmark left, compact nav links, optional app-store/download CTA, and no heavy border.

### Trust Row

Compact row of merchant logos, payment marks, or app stats. Use Ink Black and Ash, with green only for verified/trusted checkout copy.

### Promo Band

Mist Blue background, large GT Standard heading, product imagery, and a single violet or black pill action. Avoid multiple accent colors.

## Layout

Use a 1200px centered rail on Pure White or Mist Blue sections. Hero should center on search and discovery: large headline, broad pill search bar, violet submit action, and a grid or collage of product cards. Product grids can be 3 or 4 columns on desktop. Mobile should preserve large card radii and scrollable horizontal product shelves. Keep sections airy, with 64px to 96px gaps and clear category groupings.

## Imagery

Use literal product photography, merchant logos, app screenshots, phone UI, shopping bags, fashion, beauty, home goods, and clean product cutouts. Product imagery should be bright, real, and inspectable. Avoid abstract illustration, 3D blobs, dark atmospheres, generic lifestyle hero photos, and decorative icon systems.

## Do

- Use Pure White or Mist Blue as page and section backgrounds.
- Use Shop Violet for the primary search or action control.
- Use Checkout Green only for trust, checkout, and payment success.
- Use product photography as the main visual asset.
- Use 28px radius for product cards.
- Use 9999px radius for search, category pills, and CTAs.
- Keep product metadata compact and muted.
- Use flat product cards by default.

## Don't

- Do not add a second accent color.
- Do not use violet for broad backgrounds or large cards.
- Do not use green for ordinary CTAs.
- Do not use sharp square product cards.
- Do not use heavy shadows on all cards.
- Do not replace product photography with abstract graphics.
- Do not make the page feel like enterprise SaaS.
