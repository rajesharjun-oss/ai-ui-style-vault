# AI Implementation Prompt

Build a Threads-inspired interface using this source-derived style bundle.

Reference site: https://www.threads.com
Theme: light
Category: Media
North star: newspaper column on frosted glass

Use these palette anchors:

- Ink Black `#000000` for Primary text, icon strokes, structural borders, and the filled Log in button - the load-bearing color that carries almost every interface element
- Paper White `#fafafa` for Page canvas and the topmost surface layer - warm off-white that softens the contrast of pure black text
- Mist Gray `#efefef` for Secondary surface beneath the elevated feed container - the shadow-tinted plane that gives the feed column its lifted feel
- Cloud Gray `#d5d5d5` for Post dividers and card outline borders - the thinnest structural separator between stacked feed items
- Ash Gray `#969696` for Secondary borders on buttons, muted metadata text, and placeholder strokes - the middle-tone neutral for inactive controls
- Graphite `#424242` for Body text borders, secondary icon fills, and medium-emphasis strokes - sits between Ink Black and Ash Gray for tertiary text and outlines
- Meta Blue `#385898` for Outlined link borders, hyperlink text, verified-badge fill, and icon accents - the single chromatic note in the system, used for interactive emphasis without ever filling a large surface

Use these typography anchors:

- system-ui `--font-system-ui` for Entire interface - system-ui at 15px/400 for post body text, 15px/600 for usernames, 13px/400 for timestamps and metadata, 12px/400 for fine print. The choice of system-ui rather than a webfont keeps rendering native to each platform; the narrow size range (12-17px) and tight 1.33-1.4 line-height create the compact, information-dense rhythm of a social feed where many posts share a single screen

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 640px.
- Section gap: .
- Card padding: 16px.
- Element gap: 12px.

Build these component patterns where relevant:

- Feed Container: Central scrollable surface that holds all posts
- Log In Button: Primary authentication action in the top-right
- Post Card: Individual feed entry
- Circular Avatar: User identity mark in post headers and sidebar
- Verified Badge: Identity confirmation next to usernames
- Post Engagement Bar: Like, comment, repost, share actions beneath each post
- Link Preview Card: Embedded article preview within a post
- Sidebar Icon Button: Navigation targets in the left rail
- Compose Button: Quick post creation entry from sidebar
- Top Header Bar: Page-level title and entry to authentication
- Post Overflow Menu Trigger: Per-post action menu
- Inline Hashtag / Mention: Interactive text within post body

Do:

- Use Ink Black (#000000) for all primary text and structural icon strokes - let the weight of black carry the hierarchy
- Apply Meta Blue (#385898) exclusively to hyperlinks, verification badges, and icon accents - never as a filled surface or large block of color
- Set border-radius to 1000px on every avatar, button, and badge to keep the pill/circle vocabulary consistent
- Separate posts with a 1px Cloud Gray (#d5d5d5) bottom border, not with card backgrounds or spacing alone
- Wrap the feed in a single 640px-max-width container with 18px radius and the 12px 4%-opacity shadow halo
- Type body copy at 15px/400 system-ui with 1.4 line-height; reserve 600 weight for usernames and navigation labels
- Keep all interactive controls borderless - express state through color shifts (Ash Gray Ink Black) rather than fills or borders

Avoid:

- Don't introduce a second chromatic color - the system is monochrome plus one blue, and adding another breaks the newspaper discipline
- Don't use colored or gradient fills on buttons, cards, or surfaces - the only filled surface is the Ink Black Log in button
- Don't use shadows on individual post cards - the single elevation halo belongs to the feed container only
- Don't render text larger than 20px - the system operates in a 12-17px window and oversized type breaks the compact rhythm
- Don't use a webfont when system-ui renders natively - replacing it with a custom face shifts the personality away from neutral utility
- Don't put borders or backgrounds on sidebar icon buttons - they must read as a column of marks on a blank rail
- Don't round card corners above 8px for embedded link previews or media - large radii on those elements compete with the feed container's own 18px curve

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #fafafa
- border: #d5d5d5
- accent / link: #385898
- secondary text: #424242
- primary action: #385898 (outlined action border)

**Example Component Prompts**

1. **Feed Container**: Max-width 640px, centered. Background #fafafa. Border-radius 18px. Box-shadow: 0 0 12px rgba(0,0,0,0.04), 0 0 0 48px #fafafa. Contains a vertical stack of post cards separated by 1px #d5d5d5 borders.

2. **Post Card**: Background #fafafa (inherited from container). Padding 16px. Header row: 40px circular avatar (1000px radius, image fill) + username in 15px/600 system-ui #000000 + verified badge (10px circle filled #385898 with white check) + timestamp in 13px/400 #424242 + three-dot menu (Ash Gray #969696) flush right. Body text in 15px/400 system-ui #000000, line-height 1.4. Engagement bar: four line icons (heart, comment, repost, share) in #969696 with counts in 13px/400 #424242.

3. **Log In Button**: Pill shape, border-radius 1000px. Background #000000, text #fafafa. Padding 8px 16px. system-ui 15px/600. No border.

4. **Link Preview Card**: Full-width within post body. 1px border #d5d5d5, border-radius 8px. Optional full-width image on top. Below: site name in 13px/400 #424242, then headline in 15px/400 #000000. Text padding 12px.

5. **Sidebar Icon Button**: 48px square touch target. Centered 24px line icon in #969696. No background, no border. Threads wordmark logo at top of same rail, 56px square.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
