# Monologue Style Reference

> A dark editorial canvas with a single cyan signal: huge italic serif typography, mono system labels, and a tangible product device floating on black.

## Theme

Dark.

Monologue feels like a velvet-black software object staged in a literary studio. It uses near-black surfaces, white text, a ghosted giant wordmark, and one cold cyan accent. Instrument Serif italic provides the dramatic editorial voice. DM Mono handles UI chrome, metadata, button text, feature labels, and brand stamps. The page is quiet until the product device appears with its white shell, teal screen, and layered physical shadows.

## Core Principles

1. Make the italic serif headline the brand signature.
2. Use DM Mono for all system annotations and controls.
3. Keep the palette dark and nearly achromatic.
4. Use Electric Cyan only as a small pulse.
5. Let a giant ghost wordmark create atmosphere.
6. Reserve heavy shadows for physical objects, not ordinary cards.
7. Use fully rounded pills for actions and tags.
8. Use generous card radii when surfaces should feel tangible.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Black | `#000000` | `--color-void-black` | Page canvas and uninterrupted dark field |
| Obsidian | `#010101` | `--color-obsidian` | Slightly shifted black surface |
| Midnight Surface | `#191919` | `--color-midnight-surface` | Cards, panels, overlay containers |
| Graphite | `#282828` | `--color-graphite` | Interactive surfaces and hairline borders |
| Charcoal | `#363636` | `--color-charcoal` | Nested cards and grouped containers |
| Slate | `#3f3f3f` | `--color-slate` | Deep shadow surface and tertiary elevation |
| Steel Gray | `#7f7f7f` | `--color-steel-gray` | Muted labels, secondary UI, dividers |
| Ghost Gray | `#c0c0c0` | `--color-ghost-gray` | Faint wordmark and subtle surface luminosity |
| Paper White | `#ffffff` | `--color-paper-white` | Primary text, download button, product shell |
| Deep Teal | `#062f34` | `--color-deep-teal` | Product card base and teal shadow stop |
| Electric Cyan | `#19d0e8` | `--color-electric-cyan` | Accent text, accent borders, video/product glow |
| Sky Signal | `#44ccff` | `--color-sky-signal` | Secondary cyan gradient stop and screen illumination |

## Typography

Use three primary roles:

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Display | Instrument Serif | Playfair Display, EB Garamond, Cormorant Garamond | Italic headings, ghost wordmark, editorial labels |
| Mono | DM Mono | JetBrains Mono, IBM Plex Mono, Space Mono | UI chrome, labels, tags, metadata, buttons, stamp |
| Body | Geist | Inter, system-ui | Paragraphs and descriptions |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 10px | 400 | 1.4 | 0.21px |
| Mono label | 12px to 14px | 400 | 1.2 to 1.5 | 0.015em to 0.021em |
| Body | 17px | 400 | 1.4 | normal |
| Subheading | 20px | 400 | 1.2 | -0.2px |
| Heading small | 32px | 400 | 1.1 | 0.26px |
| Heading | 48px | 400 | 1.1 | -1.44px |
| Heading large | 72px | 400 | 1 | -2.16px |
| Display | 96px | 400 | 0.9 | -3.84px |
| Wordmark | 393px to 403px | 400 | 1.1 to 1.4 | tight |

Instrument Serif should usually be italic. Use negative tracking at 48px and above so it feels compact and editorial.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | compact |
| Base unit | 1px to 4px derived |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 10px |
| Small radius | 4px |
| Medium radius | 8px |
| Large radius | 12px |
| Card radius | 18px |
| Product device radius | 40px |
| Button and tag radius | 100000px |

Use very large pill radius for pills and the download CTA. Use generous device radius so the product visual feels physical and approachable.

## Layout

Use a full-bleed dark canvas with content constrained around 1200px. The hero is split: editorial headline and download CTA on the left, video card or product accent on the right, ghost wordmark behind everything. Later sections alternate between centered editorial text and two-column feature rows.

Recommended flow:

1. Full dark hero with ghost wordmark.
2. Left editorial headline and body copy.
3. White pill download CTA.
4. Product device card with teal screen and stamp badge.
5. Feature annotations in two-column rows.
6. Email composition or product screenshot cards.
7. Minimal testimonial block.
8. Language support row.

## Components

### Brand Wordmark Background

Render the wordmark in Instrument Serif italic at around 400px. Use Ghost Gray to Paper White tinting, position it absolutely, and let it overflow the viewport edges. It is atmosphere, not a content heading.

### Product Device Card

White product shell, about 360px wide, 40px radius. Inside, place a dark teal gradient screen with dot-matrix texture and a speaker grille. Use layered inset and outset shadows to make it feel physical. A stamp badge overlaps the top edge.

### Every Stamp Badge

Dark navy or deep teal badge, around 140px wide, with a scalloped or wavy postage-like edge. Use DM Mono text in white. Add heavy inset shadow so it feels embossed. Attach it to the top of the product device.

### Download Button

Paper White fill, black text, optional Apple icon, DM Mono 12px, fully rounded. Keep it around 120px wide and 32px tall. This is the primary high-contrast action.

### Watch Video Card

Small top-right secondary action. Use a teal-tinted dark surface, 8px radius, video thumbnail, play affordance, and an italic serif label. It should feel secondary and atmospheric.

### Section Heading

Instrument Serif italic, 64px to 72px, Paper White, negative tracking around -0.04em. Left-align for editorial sections. Pair with a 17px body description in Steel Gray or low-opacity white.

### Feature Annotation Row

Two-column layout. Left side uses a DM Mono label at 12px to 14px, then a Geist 17px description. Right side shows a dark product screenshot card. Keep row gaps around 10px.

### Email Composition Card

Midnight Surface or Graphite card with 8px to 12px radius. Show a simplified email drafting UI with DM Mono fields and Geist content. A teal-to-dark gradient can appear in the content area.

### Testimonial Block

Centered quote using Instrument Serif italic at 24px to 28px. Add a small avatar placeholder and DM Mono identity metadata below. No card background.

### Language Pill Row

Horizontal row of DM Mono language names at 12px. Use no background or border. Anchor the row with an italic serif label. Keep 20px gaps.

### Accent Text Link

Electric Cyan text used inline or as a tiny emphasis. Use at most a few times per viewport. Never turn it into a full CTA background.

### Ghost Button

Transparent fill, 1px white or gray border, white DM Mono 12px text, 8px radius, compact padding. Use for secondary actions only.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Void | `#000000` | Base canvas |
| 1 | Midnight | `#191919` | Product cards and panels |
| 2 | Graphite | `#282828` | Interactive surfaces and hairlines |
| 3 | Charcoal | `#363636` | Nested card backgrounds |
| 4 | Paper | `#ffffff` | Inverted light surface and product device |

## Elevation

Ordinary cards should stay restrained. The product device and stamp are exceptions: they need layered inset and outset shadows to feel tangible. Keep text shadowless.

Use:

- Subtle raised card outline for simple panels.
- Strong inset/outset stack for the product device.
- Inset embossed shadow for the stamp badge.
- Teal inset and soft highlight shadows for the teal product card.

## Imagery

Imagery is product-centric. Avoid people and lifestyle photography. Use the product device, email composition screens, dot-matrix textures, dark water-like texture, teal screen glow, and typography as atmosphere.

## Do

- Use Instrument Serif italic at 64px to 96px for major section headlines.
- Let the wordmark bleed beyond the viewport around 400px.
- Use DM Mono for labels, metadata, tags, buttons, and stamps.
- Keep Electric Cyan to 2 or 3 appearances per viewport.
- Use fully rounded pills for tags and the download CTA.
- Use 18px to 40px radii for product cards and device objects.
- Reserve complex shadows for the product device and stamp.

## Don't

- Do not use warm or bright accent colors.
- Do not use heavy shadows on text or ordinary flat cards.
- Do not use Inter or a geometric sans for headings.
- Do not use Instrument Serif below 28px as routine UI text.
- Do not use cyan as a large button background or broad wash.
- Do not use sharp corners below 4px.
- Do not center-align body paragraphs except in testimonials.

## AI Builder Notes

When in doubt, make the page quieter and the type more decisive. The composition should feel like a dark literary object with one cyan pulse, not a typical neon SaaS landing page.
