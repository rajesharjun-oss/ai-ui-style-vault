# Layout & Imagery

## Layout

Full-bleed layout with a 1440px max-width container. The header is a single thin row (logo left, nav right) sitting directly on the bone canvas with no border. The hero pattern is a full-viewport-width editorial image with no text overlay - the image IS the hero. Below the hero, a single-line caption row spans the same width with artist name flush left, publication/year flush right. Subsequent sections use centered single-image blocks (magazine covers) on bone with ~44px vertical breathing room. No multi-column grids, no card grids, no sidebars. The entire page reads as a vertical scroll through a curated gallery - one artwork per screen, generous whitespace between.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Bone Canvas | `#e7e7e7` | Page background - all content sits on this single warm-white surface |
| 2 | Ink Layer | `#000000` | All type, borders, and graphic marks on the bone canvas |

## Elevation

The design has no shadows and no elevation tokens. Hierarchy is achieved exclusively through scale (56px display vs 10px metadata), tracking (Garamond -1.0px vs Grotesk +0.38em), and whitespace (44px section gaps). Adding any shadow or fill would break the editorial-gallery language.

## Imagery

The site is image-dominant - large commissioned photography and magazine covers are the primary content. Treatment: full-bleed, edge-to-edge, no cropping frames, no overlays, no rounded corners. Photography is high-production editorial work (floral compositions, portrait, fashion) presented raw and uncropped. No illustration, no icons beyond a small search glyph. The images are always editorial fine-art photography; the system does not need to support product shots, lifestyle, or stock imagery.
