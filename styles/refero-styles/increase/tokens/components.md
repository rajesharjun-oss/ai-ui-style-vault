# Components

### Announcement Bar
**Role:** Full-bleed top-of-page strip for time-bound news, awards, and feature launches.

Background #e4ff33 (Voltage), Inkwell Navy (#1a2b3b) text at 14px weight 500, 4px vertical padding, centered content with an inline chevron. The only place chartreuse earns full-bleed real estate - treat as rare, never decorative.

### Top Navigation
**Role:** Primary header carrying brand, product taxonomy, account actions.

White (#ffffff) background, 64-72px tall, brand wordmark left at 20px weight 700, nav links at 16px weight 500 Inkwell Navy with 8px gap. Right cluster: text-link 'Sign in' (Graphite #687887) and filled primary 'Sign up' (Inkwell Navy bg, white text, 8px radius, 10px 20px padding). Hairline 1px Silver (#caced2) bottom border.

### Primary Filled Button
**Role:** The default action affordance - sign-up, create, submit.

Inkwell Navy (#1a2b3b) background, white text at 16px weight 500, 8px radius, 10px vertical / 20px horizontal padding, subtle two-layer black shadow (0 1px 3px rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)). Trailing chevron is part of the variant grammar. Letter-spacing -0.16px.

### Ghost / Outlined Button
**Role:** Secondary actions - 'Contact sales', 'Sign in', 'Learn more'.

Transparent background, 1px Inkwell Navy border, Inkwell Navy text, 8px radius, 10px 20px padding, trailing chevron at right. When on white cards, the border is the only visual weight.

### Hero Headline
**Role:** Page-opening display line establishing product category.

Untitled Sans 90px / line-height 1.0, weight 500, Inkwell Navy, letter-spacing -5.4px (-0.06em). Set tight on two lines; the extreme negative tracking is the signature - the headline reads as a single dense block of type rather than airy display copy.

### Hero Subtext
**Role:** Supporting paragraph under the headline.

Untitled Sans 20px / line-height 1.4, weight 400, Graphite (#687887), letter-spacing -0.2px. Max width ~540px, two to three lines, left-aligned.

### Code Block Card
**Role:** Live API demonstration embedded in hero and feature sections.

Abyss (#0d1726) background, 12px radius, 20-24px padding, soft navy-tinted shadow. Syntax uses Input Mono 14px: keywords in Voltage (#e4ff33), strings in Mint Signal (#31f2bf), identifiers in light blue (#33bbff - content-only, not a UI token), numbers in white. Line numbers and line-height 1.54. The dark card sits as the visual counterweight to the white form card beside it.

### Product Feature Card
**Role:** Feature highlight in a 4-column grid (ACH, Cards, Bank accounts, Wires, etc.).

White (#ffffff) background, 12px radius, 1px Mist (#e1e5e9) border, 20-24px padding, faint tinted shadow. Mint Signal (#31f2bf) icon container at top-left - a 40-48px square with 1.5px stroke icon on a subtle mint-tinted surface. Title at 16px weight 500 Inkwell Navy, description at 13px Graphite, 8px vertical gap between.

### Icon Badge
**Role:** Reusable icon container for feature cards and inline labels.

40x40px (or 48x48px) square, 8px radius, Mint Signal (#31f2bf) 1.5px stroke icon centered on a near-white mint-tinted fill (rgba(49,242,191,0.08) effect). The mint-on-mint treatment is the visual signature of an 'active system feature'.

### Trust Logo Bar
**Role:** Social proof band beneath the hero.

Fog (#edf0f2) full-bleed band, centered row of monochrome navy wordmarks (gusto, stripe, ramp, check, AtoB, vantaca, coast) at 24-28px, all rendered in Inkwell Navy or Graphite, 48-64px gap between logos. No logos are colored - uniformity signals impartiality.

### Gradient Accent Visual
**Role:** Decorative hero backdrop and feature-section color washes.

Series of left-to-right linear gradients cycling through Voltage mint cyan blue (linear-gradient(90deg, #deff34, #8cf97c), linear-gradient(90deg, #65f75f, #12f0aa), linear-gradient(90deg, #45f4bc, #33dfdf), linear-gradient(90deg, #01d3d8, #02b7f1)). Used as 3D geometric blocks floating behind hero content, clipped with sharp angular edges - never soft-blurred.

### Form Input
**Role:** Text input in the hero demo card ('Send an ACH transfer').

White background, 1px Silver (#caced2) border, 8px radius, 12-16px padding, 16px body text Inkwell Navy. Label above at 13px weight 500 Graphite. Focus state: 2px Mint Signal border. Active/highlighted input shows a mint-tinted fill.

### Step Progress Indicator
**Role:** Multi-step flow visualization inside product cards.

Horizontal line with two filled mint nodes connected by a 2px Mint Signal stroke. A third node appears as a hollow mint circle indicating pending step. Label set in 14px Input Mono for numerical precision feel.
