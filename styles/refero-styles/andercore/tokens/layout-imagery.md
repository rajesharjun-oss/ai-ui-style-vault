# Layout & Imagery

## Layout

The page runs at max-width 1200px centered, but most sections are full-bleed dark bands. The hero is a full-bleed photographic image with dark overlay, headline left-aligned in the lower-third. Content sections follow a single-column rhythm: section eyebrow badge heading body text, with primary CTAs right-aligned. Three-column feature grids appear inside dark sections at equal 32px gutters. The step progress flow uses a 2/3-left text, 1/3-right visual (chat + photo) split. Vertical spacing is generous: 80px between sections, 32px card padding, 24px element gaps. Navigation is a thin white fixed bar at the top - the only consistently light surface on an otherwise dark page.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas - Light | `#ffffff` | Navigation bar, light interstitial bands |
| 1 | Canvas - Dark | `#0b0405` | Primary content section background, full-bleed dark bands |
| 2 | Card Surface | `#150e0f` | Elevated panels and feature cards on dark sections |

## Elevation

No drop shadows. Structure is defined entirely by 1px hairline borders (#382e30 on dark, #e5e5e5 implied on light) and the 4-step surface value stack. Components sit flat against their canvas, separated by lines rather than lifted by blur - the industrial-control-room approach.

## Imagery

Photography is the dominant visual: industrial subjects (logistics trucks, construction sites, workers in hard hats) shot in golden-hour or moody low-light conditions. Images are full-bleed with dark gradient overlays so they merge into the #0b0405 section backgrounds. UI mockups (mini browser panels, chat interfaces) appear as flat dark-on-dark diagrams with red accent dots, never as realistic product screenshots. The Andercore 'A' mark functions as both logo and a small red UI token (avatar, connector node). No illustration style - everything is either photographic, diagrammatic, or pure typography on dark canvas.
