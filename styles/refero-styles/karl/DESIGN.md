# Karl Design Notes

Karl is a full-bleed illustrated portfolio system. It behaves less like a traditional website and more like a sequence of poster scenes: saturated yellow background, flat vector illustration, a large blue globe, and chunky white display type arranged as signage.

## Visual Principles

- The yellow canvas is the page. Do not place it inside white or gray wrappers.
- The blue globe is a compositional focal surface, not a reusable card.
- The site is flat by design. Depth comes from illustration layers.
- Text is part of the illustration, especially when rotated or stacked along an arc.
- Navigation is deliberately quiet: simple uppercase Arial links centered at the top.

## Color System

The palette is tiny and strict. Signal Yellow carries every section. Globe Azure creates the main focal shape. Charcoal Ink handles nav, linework, and dark text. Cloud White handles clouds, windows, and display text on blue. Roof Coral belongs inside the artwork only.

## Typography

Changa One is the personality face. It should carry hero text, intro statements, and section moments at one weight: 400. Use tight line-heights for display text so stacked lines feel overprinted.

Arial is only for nav chrome. Keep it at 14px, uppercase, regular weight, and `#333333`.

## Layout

Use full viewport-height scenes with hard cuts between sections. Avoid max-width content containers, card rows, feature columns, and neutral page bands. The page should feel like a vertical scroll through illustrated panels.

## Implementation Cues

- Anchor a large blue circle to the bottom center of the viewport.
- Place white Changa One text on the blue globe.
- Rotate headline lines slightly when they need to follow the globe arc.
- Add flat vector houses, clouds, and linework around the scene.
- Keep nav at the top center with no background box.
- Avoid shadows, gradients, opacity tricks, and blur.
