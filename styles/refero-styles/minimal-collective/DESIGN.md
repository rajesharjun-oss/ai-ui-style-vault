# Minimal Collective Design Reference

## Essence

Minimal Collective is severe, editorial, and gallery-like. The interface trusts black space, large typography, crisp white lines, and a few carefully placed images. It avoids conventional web friendliness. No accent color, no soft depth, no gradient wash, and no decorative UI should appear. The page should feel curated and intentional.

## Color System

Use only black, white, and muted gray. Black is the canvas and primary surface. White is the main text and line color. Gray is for secondary text, disabled states, and quiet metadata. Do not introduce a CTA color. If an element needs emphasis, use scale, placement, contrast, or white outline.

## Typography

Use PolySans as the sole typeface if available. If not, use a disciplined geometric sans such as Suisse Int'l, Neue Haas Grotesk, Inter, or Arial. The system uses a single regular weight. Hierarchy comes from size, tracking, whitespace, and placement. Large display text can be enormous and tightly tracked. Labels and nav items remain small, uppercase, and letter-spaced.

## Shape And Space

The system is mostly sharp, with small functional radii only where needed. Ghost pills may use 999px radius, but image frames, page sections, and large surfaces stay square. Spacing is spacious and deliberate. Hairline borders do the structural work.

## Layout Rhythm

Build the page as a black editorial stage. Use a fixed or corner-oriented nav, very large headline text, overlapped photography, sparse metadata, and horizontal hairline dividers. Avoid card stacks. Images can overlap text or sit partly off-grid, but the composition should still feel exact.

## Components

- Minimal top navigation with white logo/type left, sparse uppercase links, and a ghost pill action.
- Giant hero headline with PolySans regular, tight negative tracking, and white on black.
- Overlapping editorial image stack with square image crops and no shadow.
- Ghost pill button with white border, transparent fill, uppercase label, and no colored hover.
- Category badge with white hairline border and uppercase label.
- Case study row with large title, muted metadata, one image, and a dividing line.
- Image mosaic with uneven but intentional overlap.
- Corner footer navigation with small labels and hairline rules.

## Implementation Direction

Start with a pure black canvas. Add one huge text moment, one or two photos, and a few thin lines. Keep copy short. Do not add gradients, color accents, shadows, rounded cards, stock icon sets, or dense UI controls. If the page feels empty, solve with stronger composition rather than extra decoration.
