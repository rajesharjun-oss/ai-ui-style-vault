# Layout & Imagery

## Layout

Max-width 1280px centered container. The hero is full-bleed with the gradient background extending edge-to-edge, centered headline at 60px, subtitle at 18px, and a floating chat input card below. After the hero, the page settles into cream (#fcfbf8) sections with generous vertical spacing (64-80px between major sections). The logo bar is a single horizontal row of 5-6 monochrome logos. Feature explanations use a 2-column layout: left side has a UI mockup in a warm card, right side stacks 3 text-only feature descriptions vertically. Template gallery uses a 4-column grid of screenshot cards with minimal gaps. Navigation is a sticky top bar with backdrop blur, logo left, text links center, two pill buttons right. Footer is multi-column with warm beige (#eceae4) top border. Section rhythm: gradient hero white with logos cream feature sections white template grid stats footer.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#fcfbf8` | Page background, default surface for all content |
| 1 | Card | `#f7f4ed` | Elevated cards, chat input panels, feature containers - slightly warmer than canvas |
| 2 | Inverse | `#1c1c1c` | Dark pill buttons, inverse overlays, high-contrast moments |

## Elevation

- **Chat Input Card:** `oklab(0 0 0 / 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`
- **Input Field (inset):** `oklch(0 0 0 / 0.25) 0px 0px 0px 0.5px inset`

## Imagery

The hero uses a full-bleed horizontal gradient as an ambient backdrop - not an image but a color field transitioning from dark charcoal through blues, magentas, reds, and oranges, creating a sunrise/prism effect. Below the hero, the site is almost entirely text-dominant. Template gallery cards show small rectangular screenshots with 12px rounded corners, displayed in a 4-column grid. These screenshots are the only photographic content and serve as thumbnails, not atmosphere. Company logos in the social proof bar are monochrome SVGs in #1c1c1c. Feature sections use small UI mockups (chat input recreations) rather than illustrations or photography. The overall visual density is very low - most sections are pure typography on warm cream backgrounds with no decorative imagery at all. Icon style is minimal: thin outlined icons at approximately 1.5px stroke weight, monochrome in #1c1c1c or #5f5f5d.
