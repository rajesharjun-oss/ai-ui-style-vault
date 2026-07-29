# Giga Design Reference

## North Star

Midnight horizon above matte obsidian

## Theme

dark style for AI interfaces.

## Color System

- Obsidian `#000000` for Deepest background, hero image overlay, footer canvas, shadow base pure black creates cinematic depth behind atmospheric photography
- Onyx `#0f0d0d` for Primary page canvas (--bg), card surface, default button fill the warm-tinted near-black that grounds the entire interface
- Charcoal `#171615` for Raised surface, dark button background (--button-dark-bg), elevated cards one step lighter than the canvas to signal depth without drawing attention
- Graphite `#262828` for Stepped feature panels, image containers, secondary surface layer visible in side-by-side comparison modules
- Void `#050404` for Near-black used in box-shadow tints and image depth effects effectively black but with a barely-warm undertone matching Onyx
- Paper `#ffffff` for Primary text, icons, light button text, filled button surface (--primary) pure white on near-black achieves 19:1 contrast, the highest readable tier
- Ash `#878686` for Secondary body text, descriptive copy, helper labels sits at ~50% luminance, legible without competing with headlines
- Smoke `#6f6e6e` for Tertiary text, decorative fills, disabled states, muted metadata low-contrast informational layer

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- gigaSansText Body text, buttons, navigation, links the workhorse. Weight 400 for paragraphs, 500 for button labels and emphasis. 16px at 1.5 line-height is the readable default; 14px at 1.43 handles dense UI chrome. `--font-gigasanstext`
- emilioDisplay Display headlines the signature voice. Ultra-light weight at 48-66px with tight -0.02em to -0.03em tracking creates a film-title-card feel. Most enterprise brands shout with 700-weight headlines; Giga whispers with 300, which is the entire personality in one choice. `--font-emiliodisplay`
- gigaSansDisplay Section subheadings, feature card titles, prominent UI labels bridges the gap between whisper-thin display and body text. Weight 500 at 22px carries mid-importance statements. `--font-gigasansdisplay`
- interText Large numerical and functional headings 44px with -0.03em tracking for stat callouts and mid-level headings. Acts as a contrast voice to the emilioDisplay serif displays. `--font-intertext`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 4px
- Density: comfortable
- Page max-width: 1280px
- Section gap: 80-120px
- Card padding: 20px
- Element gap: 20px

## Components

- Pill Button (Dark Fill): Primary navigation and CTA surface
- Pill Button (Light Fill): High-emphasis CTA the only solid-white button in the system
- Ghost Navigation Button: Minimal nav link styling
- Glass Badge Pill: Announcement chip floating over photography
- Translucent Card: Content card floating over dark/photographic backgrounds
- Solid Card: High-contrast content module on canvas
- Video Preview Card: Floating media player with metadata
- Logo Strip: Social proof band partner/customer logos

## Implementation Guidance

- Use weight 300 emilioDisplay at 48-66px for all primary headlines the whisper-thin display is the brand's signature voice
- Apply 9999px border-radius to all buttons, badges, tags, and interactive pills nothing rectangular should be clickable
- Set page background to #0f0d0d (Onyx) as default; use #000000 only for full-bleed photography containers and footer
- Use #ffffff for all primary text and icons on dark surfaces the 19:1 contrast is the readable standard, don't step down from it
- Place uppercase 11-12px geistMono labels with +0.009em tracking above section titles as technical eyebrows
- Use Ember Red (#fe2c02) only on a single accent card per viewport it is punctuation, not chrome
- Set body text at 16px gigaSansText weight 400 with 1.5 line-height for all paragraphs and descriptive copy

## Guardrails

- Don't use weight 600+ for headlines the system whispers at 300, shouting breaks the entire atmosphere
- Don't add drop shadows to cards depth comes from surface color stepping (#0f0d0d #171615 #262828), not elevation
- Don't use rectangular buttons or sharp corners on any interactive element all controls are pills
- Don't apply the Ember Red accent to more than one element per section overuse destroys its impact
- Don't use #000000 as page background use #0f0d0d; pure black is reserved for photographic backdrops
- Don't use chromatic colors for text white and grays only for typography; color is surface-only
- Don't mix serif and sans at the same hierarchy level emilioDisplay is for display, gigaSansText for everything else, never both at body size
