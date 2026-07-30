# Layout & Imagery

## Layout

The page model is a sequence of full-width horizontal bands: dark hero stats ticker light content sections with full-bleed photos footer. No max-width container constrains the layout - every band spans the full viewport. The hero is a split composition with oversized logo left and large display headline right, both vertically centered on a black canvas. Below the hero, content shifts to white canvas with generous vertical space (50-80px section gaps) and full-bleed photography serving as visual punctuation between text blocks. Navigation is a slim top bar (40-48px) with no sticky behavior indicated. The overall rhythm is editorial: large type, full-width imagery, hairline dividers, and wide white margins creating a magazine-like cadence rather than a dense product UI.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Hero Canvas | `#000000` | Dark hero band with oversized white logo and display headline |
| 2 | Page Canvas | `#ffffff` | Default light surface for all content sections below the hero |
| 3 | Accent Surface | `#0075ff` | Sparingly used filled surface for primary action buttons only |

## Elevation

The system deliberately avoids all but the faintest ambient shadow. A single 1px 1px 0px wash in #eeeeee appears on one button state. Components are defined by hairline 1px borders in #cccccc or #212529, not by drop-shadows. The flatness reinforces the editorial, print-inspired character of the type-first design - it reads as laid-out rather than assembled.

## Imagery

Photography is environmental and architectural: brick facades, city buildings, physical Tech Barcelona signage mounted on real walls. Shots are warm-toned with natural daylight, no lifestyle people, no abstract gradients. Full-bleed presentation with no border-radius, often used as section dividers between text blocks. The only non-photographic visual is the geometric pixel-art logo mark - a grid of white squares forming an abstract 'TC' monogram on the dark hero. Imagery density is low to moderate: most sections are text-dominant, with photographs appearing as full-width breaks rather than inline illustrations.
