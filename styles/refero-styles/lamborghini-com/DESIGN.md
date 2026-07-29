# Lamborghini.com Design Reference

## Essence

The system feels like a black showroom built around speed, light, and precision. It uses stark contrast, full-screen automotive media, sharp rectangular controls, all-caps navigation, and a single yellow action color. The page should feel engineered, expensive, and cinematic rather than friendly or decorative.

## Color System

Use a very small palette. Nero black anchors navigation, hero sections, product sections, footer, and overlays. Bianco white supplies the main text and light editorial surfaces. Giallo yellow is the only high-energy accent and should be reserved for primary CTAs, tiny active states, and brand punctuation. Silver and Graphite handle secondary text, dividers, muted metadata, and disabled states.

## Typography

The native face is LamboType. If unavailable, use a condensed geometric substitute such as Arial Narrow, Inter Condensed, or a licensed brand-appropriate condensed sans. Most navigation and controls are uppercase with measured letter spacing. Hero text is large, compressed, and direct. Use type scale, weight, and casing to create hierarchy instead of ornamental effects.

## Shape And Space

Everything is sharp. Buttons, nav containers, cards, images, panels, and inputs use 0px radius. There are no soft card shells, no rounded SaaS panels, and no pill buttons. Layout density is compact to medium: tight controls, large section bands, wide model imagery, and strong horizontal separation.

## Layout Rhythm

Alternate full-bleed dark product moments with black spec strips and white or concrete editorial sections. Use the browser width aggressively. The page should not feel like a stack of cards inside a generic max-width container. Hero media can fill 80vh to 100vh, while spec and model sections use hard-edged grids and edge-to-edge bands.

## Components

- Fixed black top navigation with logo at left, all-caps model links centered, utility icons at right, and no shadow.
- Yellow primary CTA with square corners, black uppercase label, bold type, and compact padding.
- Ghost button with a one-pixel border, transparent fill, square corners, and uppercase label.
- Full-bleed hero image or video with the car as the primary visual subject and minimal overlay text.
- Model tile with full-bleed car photography, a black gradient only when needed for legibility, large white model name, and CTA row.
- Vehicle spec strip with black background, white numbers, silver labels, and thin graphite dividers.
- News or story cards on white or concrete sections with square images and restrained metadata.
- Configurator panel that uses split product render and control columns, sharp panel edges, and clean dividers.

## Implementation Direction

Start with a black shell and full-bleed media. Place the nav directly over or above the hero. Keep interactive elements rectangular. Use Giallo for the one action that matters most. Avoid decorative gradients, shadows, blur blobs, cartoon icons, rounded controls, and pastel support colors. Let the product photography create drama.
