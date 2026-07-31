# Components

### Primary Pill Button
**Role:** The sole filled action in the system

Electric Indigo (#1500ff) background, Paper (#fdfdfd) text at 14-16px weight 500, fully rounded 9999px radius, 12px 24px padding. This is the only place the brand color lives - every other interactive element defers to it. Appears once per viewport maximum to preserve its impact.

### Ghost Pill Button
**Role:** Secondary action that doesn't compete with the primary

Transparent background, 1px Paper (#fdfdfd) border at ~30% opacity or full opacity, Paper text at 14px weight 500, 9999px radius, 10px 20px padding. Used for 'Sign up' and 'Join over 1M users' - the outlined variant lets the primary indigo button own the hierarchy.

### Navigation Bar
**Role:** Minimal top-level site navigation

Transparent background floating on the Obsidian canvas. Logo at left in Paper white, text-only nav links (Features, Marketplace, What's new, Reviews) centered in Pearl (#d4d4d4) at 14px, auth actions (Log in, Sign up) at right. No background fill, no shadow, no border - the nav exists purely as type on the void.

### Display Headline
**Role:** Hero-level typography that defines the page

96px Savee Font weight 500, Paper (#fdfdfd), line-height 0.96, letter-spacing -0.04em. The extreme tightness and massive scale make it read as a single sculptural block. Centered horizontally with generous top/bottom breathing room (64-80px). The hero is centered single-column - no split layout, no side imagery.

### Editorial Body Block
**Role:** Long-form persuasive text at unusual scale

36px Savee Font weight 400, Paper (#fdfdfd), line-height 1.13, letter-spacing -0.01em. This is body copy at headline scale - 36px is massive for prose, creating a magazine-like reading experience. Left-aligned, max-width ~800px, sits below the hero with 48-64px separation.

### Partner Logo Strip
**Role:** Social proof band

Single horizontal row of grayscale brand logos (Apple, Google, Nike, Adobe, Pentagram, Airbnb, MWS) in Ash (#a3a3a3) or Pearl (#d4d4d4), evenly distributed across the full content width. Preceded by a small caption in Stone (#737373) at 13px. No logos colored, no hover effects - the strip is quiet authority.

### Product Preview Frame
**Role:** Large product screenshot or video container below the hero

Charcoal (#151515) background surface filling most of the viewport width, 14px border-radius, no border, no shadow. The subtle lift from canvas (#050505) to surface (#151515) is the only elevation cue - no drop shadows are used anywhere in the system.

### Text Link
**Role:** Inline navigation within body copy

Inherits body color (Paper or Pearl) with underline on hover only. No chromatic links - even interactive text stays in the neutral palette, reserving Electric Indigo exclusively for the primary CTA.

### Subhead Caption
**Role:** Descriptive subtext under headlines

16-18px Savee Font weight 400, Pearl (#d4d4d4), centered, line-height 1.50. Sits 16-24px below the display headline. The muted color creates a clear visual step-down from the headline without using a different size or weight.

### Full-Width Section Spacer
**Role:** Vertical rhythm between page sections

64-80px of pure Obsidian canvas with no visual element. Sections breathe into the void - no dividers, no background color shifts, no gradient transitions. The darkness itself is the separator.

### Footer Divider
**Role:** Low-contrast structural edge

1px horizontal line in Slate (#2f2f2f) or Silver (#e5e5e5) at ~10% opacity, spanning the content width. The only structural border in the entire system - used to separate the footer from the page body.
