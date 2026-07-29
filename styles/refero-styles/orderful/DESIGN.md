# Orderful Design Reference

## North Star

An industrial command deck: a logistics dispatcher's printed control sheet in black ink and surgical vermillion. The page is restrained and operational, so the single red-orange action signal can shout.

## Theme

Light, enterprise, B2B, logistics, operational, monochrome with one vivid action signal.

## Palette

The main canvas is Vellum `#f5f5f5`, with Paper `#ffffff` cards and content surfaces. Typography is mostly Slate 900 `#101828` for display and Slate 600 `#4a5565` for body and labels. Ink Black `#000000` is best for hairlines, logo marks, and strong icon strokes.

Vermillion `#e42b0c` is scarce and action-only. It should appear as filled primary CTAs, selected conversion moments, connector nodes, or a thin accent border. The Sunset Flux gradient is reserved for the top navigation conversion button, not general decoration.

Carbon `#1f1f1f` is the inverted surface for product mockups, footers, or strong feature panels.

## Typography

Telegraf is the workhorse. Use it for display, headings, body, nav, buttons, cards, inputs, and footer text. The type voice is geometric and precise. Display text should use weight 300 to 500, never heavy 700 by default. Large type tightens with negative tracking.

ModernGothic is a secondary 14px register for specific body or link contexts. Use it sparingly.

Uppercase eyebrows use 12px, weight 500, and 0.3px tracking. Body copy sits at 16px to 18px, weight 400, line-height 1.5.

## Layout

Use a 1200px centered max-width and an implied 8-column grid. The hero is a split layout on a Vellum canvas: left side has the 72px headline, body copy, and vermillion CTA; right side has a product visual tile with dark ERP panels, connector nodes, and a brand-logo grid.

Below the hero, use a white trust-logo band, then Vellum sections with centered display headings and three-column feature card grids. Testimonial sections can use a two-column quote plus customer visual and a three-up stat row.

## Surfaces And Elevation

Surfaces are restrained:

- Vellum for the matte page base.
- Paper for cards and content panels.
- Carbon for dark emphasis panels or product UI.

Use a single subtle two-layer shadow only when needed. Most separation should come from 1px borders, white cards, and spacing. Do not create glossy elevation.

## Components

Primary action buttons use Vermillion fill, white text, 8px radius, uppercase telegraf, and a trailing arrow. Use at most one visible filled action per fold.

Feature cards are white, 8px radius, 1px Frost border, 32px padding, a 24px icon, a 24px heading, and body copy in Slate 600.

Stat blocks float without card chrome. The number is large, thin, and precise.

Navigation is a 64px white bar with a Frost bottom border, uppercase nav items, ghost login, and a single Sunset Flux conversion button.

## Imagery

Use product-led operational imagery: dashboard mockups, trading partner brand grids, connector lines, metrics, grayscale trust logos, tight customer headshots, and award badges. Avoid lifestyle photos, abstract 3D renders, and decorative gradients.

## Implementation Feel

The page should feel calm and information-rich. It is not sparse, but every section breathes. The entire system depends on discipline: monochrome first, vermillion only for action, and 8px geometry everywhere.
