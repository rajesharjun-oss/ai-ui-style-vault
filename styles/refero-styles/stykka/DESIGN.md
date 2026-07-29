# Stykka Design Reference

## North Star

Build a white, quiet, photo-led showroom. The interface should feel like a measured Scandinavian workshop: useful, exact, tactile, and restrained. The screen is mostly white space, black type, black hairlines, and large interior photography.

The UI should not compete with the product imagery. All warmth comes from wood, light, kitchens, surfaces, and rooms inside the photos.

## Theme

- Mode: light.
- Canvas: white.
- Text: black.
- Borders: black 1px rules where structure is needed.
- Accent: none. The photos are the accent.
- Elevation: none.

## Color System

Use an achromatic system:

- Gallery White: `#ffffff` for the page, section background, and empty space.
- Press Black: `#000000` for text, borders, inverse surfaces, footer, and hover fills.
- Plate Gray: very light neutral only when a placeholder or inactive surface is unavoidable.

Do not add brand blues, greens, oranges, or warm UI accents. If the page needs visual energy, use stronger photography, not color decoration.

## Typography

Primary font: Inter.  
Fallback: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.  
Supporting mono: Azeret Mono for rare spec-style callouts.

Type should be crisp, tightly tracked at larger sizes, and mostly regular weight.

- Caption: 11px, line-height 1.2, letter-spacing 0.23px, weight 400 or 500.
- Small label: 14px, line-height 1.25, letter-spacing 0.29px, weight 500.
- Body small: 14px, line-height 1.25, letter-spacing 0.29px, weight 400.
- Body: 16px, line-height 1.5, letter-spacing -0.37px, weight 400.
- Subheading: 22px, line-height 1.2, letter-spacing -0.79px, weight 400.
- Heading small: 24px, line-height 1.2, letter-spacing -0.89px, weight 400.
- Heading: 30px, line-height 1.1, letter-spacing -1.2px, weight 400.
- Display: 46px, line-height 1.05, letter-spacing -1.93px, weight 400.
- Mono callout: 18px, line-height 1.0, letter-spacing -0.18px, weight 400.

The signature move is a large, regular-weight display headline. Avoid bold display type.

## Layout

- Maximum content width: 1280px.
- Grid feel: strict 10px rhythm.
- Section gap: 60-80px.
- Element gap: 10px.
- Hero: full viewport width and roughly full viewport height.
- Nav: absolute over the hero, no solid background.
- Content sections: white, measured, and open.
- Footer: full-width black band.

Desktop composition should use 3- or 4-column grids for cards and image groups. Tablet can collapse to 2 columns. Mobile should collapse to 1 column with the same hard image edges and restrained type.

## Imagery

Photography is the main visual system.

- Use real kitchens, worktops, materials, rooms, and close product details.
- Keep images hard-edged with 0px radius.
- Avoid image shadows, floating frames, tinted overlays, and masks.
- Use 10-15px gutters.
- Prefer full-bleed hero imagery and simple editorial grids.

## Navigation

Use a transparent absolute nav over the hero:

- Left cluster: about, journal, inspiration, design.
- Center: Stykka-style wordmark text.
- Right cluster: language selector and outlined CTA.
- Text: black on bright photography, white only if the hero image requires it.
- No nav background, shadow, blur, or bottom border.

## Components

Outlined CTA buttons:

- Transparent fill.
- 1px black border.
- 8px radius.
- Inter 16px, weight 500.
- Padding around 10px 18px.
- Hover: black fill, white text.
- No shadow or scale animation.

Feature grid cards:

- Not true cards. Use image, title, and body text with no enclosing surface.
- Image first, hard edge.
- Title in small uppercase label style.
- Body in 16px regular.
- No shadows, borders, or colored panels.

Inline links:

- Black text.
- 1px underline.
- Underline offset around 3px.
- No color change required.

Footer:

- Full black background.
- White text.
- Minimal wordmark and links.
- Use same calm spacing as the page.

## Motion

Motion should be almost invisible. Use short hover transitions on button inversion and underline movement. Avoid parallax, springy cards, animated blobs, or decorative page motion.

## AI Build Notes

When implementing this style, start with photography and spacing. If the design feels empty, add a better image or better alignment before adding visual effects.

