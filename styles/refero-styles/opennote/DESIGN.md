# Opennote Design Reference

## North Star

A warm leather journal on sunlit paper. The interface should feel hand-bound and editorial: cream paper, old-style serif headlines, careful sans-serif UI text, and small black line drawings floating in the margins.

## Theme

Light, warm, editorial, notebook-like, reflective, low-chrome.

## Palette

The base is Ivory Page `#fffdf8`, not pure white. It should read as paper. Ink Charcoal `#0a0a0a` is the main text and icon color. Graphite Rule `#e5e5e5` handles structural lines, borders, and card outlines.

Use Sepia `#512906` as the only filled interactive surface. It should feel like a leather tab or book label. Use Ink Violet `#242d64` for one full-bleed feature panel that interrupts the paper rhythm. Forest Ink `#0c3b1a` and Oxblood `#5e0831` can appear as rare accent text or decorative ink. Margin Yellow `#ffc934` is decorative only.

## Typography

Display type is serif. Use IowanOld if available; otherwise use Source Serif Pro, Tiempos Text, PT Serif, or a similar old-style serif. Headlines should be weight 400 and calm. Do not bold the serif. The serif owns every headline, feature title, hero line, and text above 24px.

SuisseIntl is the quiet UI companion. Use SuisseIntl, Inter, Sohne, or Helvetica Neue for body copy, navigation, buttons, captions, forms, and footer text. The sans-serif should not compete with the serif.

The biggest text is still restrained: 42px to 48px for hero and section headings, 32px for smaller feature headings, 16px body copy with 1.5 line height.

## Layout

Use a centered, editorial page structure with a max width around 1200px. The hero is a single column: small line illustration, two-line serif headline, one Sepia CTA. Keep 80px to 120px of vertical breathing room around the hero.

Below the hero, use a single logo strip directly on the ivory canvas, then alternate between centered paper-card sections and one darker Ink Violet feature panel. Sections should read like quiet spreads in a notebook, not a dashboard or dense SaaS grid.

## Surfaces And Elevation

There is no shadow system. Cards do not float. They sit on the page as bordered paper pieces.

Use:

- 1px Graphite Rule borders.
- Ivory Page for main cards.
- Soft Halo `#f9f9f9` for recessed panels.
- Ink Violet for a single dramatic reset panel.
- Sepia for the main filled CTA.

Avoid shadows, glows, glass, and thick layered backgrounds.

## Components

The Sepia CTA is the main action style. It uses Sepia fill, Ivory Page text, 10px radius, and compact padding. Secondary actions use transparent backgrounds, 1px Ash Border lines, and Ink Charcoal text.

Feature cards are simple paper cards: 1px border, 10px radius, 24px padding, no shadow, serif title, sans-serif body.

Tabs are text-only. The active tab is communicated by Ink Charcoal text and a small underline; inactive tabs use Smoke.

The header is transparent with a bottom hairline. No sticky shadow. No heavy nav chrome.

## Imagery

Use hand-drawn black line illustrations as marginal notes: science symbols, keys, notes, equations, compass marks, or abstract study sketches. Place them loosely in negative space at varied scales. They should never overlap important text.

Avoid photography, 3D renders, dense product screenshots, and stock-like visual blocks. The page itself is the visual object.

## Implementation Feel

The result should feel like a thoughtful AI notebook designed by someone who loves paper, research, and quiet tools. Warm, spacious, editorial, and precise. The charm is in restraint.
