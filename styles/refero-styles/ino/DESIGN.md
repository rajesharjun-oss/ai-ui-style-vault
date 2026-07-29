# INO Design Reference

## Essence

INO is a disciplined white-gallery commerce system for jewelry and small luxury objects. It removes almost every expressive flourish so the product, metal, and photography do the work. The interface feels clinical but not cold, precise but not technical, and quiet enough for small objects to feel valuable.

## Color System

The palette is strictly neutral. White is the page canvas and negative space. Ink is the primary text and icon color. Chalk supports product fields and subtle gallery blocks. Fog handles secondary surfaces, overlays, and item separators. Stone is reserved for captions, metadata, disabled states, and quiet utility text. Do not add a brand accent color.

## Typography

The native face is Sequel100Wide at weight 400 only. Use it everywhere: navigation, labels, product names, prices, metadata, footers, and small body copy. If unavailable, use a wide geometric sans fallback such as Eurostile Extended, Neue Haas Grotesk Display, Inter Tight, or Arial. The type scale is intentionally tiny: 11px to 18px. Hierarchy comes from spacing, uppercase tracking, and placement, not weight or huge headlines.

## Shape And Space

The geometry is mostly square and quiet. Product cards have zero padding and no visible frame. Images sit on pale fields with no shadow. Buttons and utility controls can use small 4px radius. Navigation indicators use circles. Section spacing is comfortable and gallery-like, but cards themselves are restrained and almost bare.

## Layout Rhythm

Use a white canvas, generous gaps, and a product-first grid. The signature layout detail is bottom navigation: a row of page or collection labels anchored near the bottom, each with a small circle indicator. Product grids are organized, quiet, and low copy. Detail pages should let the product image dominate, with metadata arranged in small uppercase rows.

## Components

- Bottom navigation with uppercase labels, tiny type, and circle indicators.
- Product gallery card with pale background, zero internal padding, no shadow, and minimal name/price text.
- Micro product label with uppercase Sequel100Wide, 11px to 12px, and wide tracking.
- Object detail split with large product image and sparse data column.
- Circle indicator for active, hover, and pagination states.
- Utility link row with price, material, collection, or account links in small type.
- Add to cart button with thin border, 4px radius, and no strong color fill.
- Footer material ticker or metadata row, using tiny uppercase labels and Stone text.

## Implementation Direction

Start with a white surface and resist adding decoration. Keep all type small. Use product imagery on chalk or fog surfaces, with object photos carefully centered. Use bottom navigation instead of a conventional loud header when possible. Avoid large hero marketing sections, saturated CTAs, shadows, gradients, rounded ecommerce cards, decorative icons, and expressive typography.
