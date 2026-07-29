# AI Implementation Prompt

Build a dark Linear-style changelog or release-notes interface using the Changelog style reference.

Use a full-bleed `#08090a` page background. Build all depth with stepped near-black surfaces: `#141516`, `#1c1c1f`, `#23252a`, and `#2d2e31`. Use 1px borders for separation instead of blurred shadows. The page should feel like a precise engineering notebook or developer console, not a colorful SaaS landing page.

Typography:

- Use Inter Variable as the main UI font, with Inter or system-ui as fallback.
- Use weight 510 for headings and active UI where available.
- Use weight 590 for emphasis instead of generic bold.
- Use Berkeley Mono only for code references, command examples, date labels, keyboard hints, and technical metadata.
- Keep body text around 15px to 16px, line-height 1.5 to 1.6.
- Use 24px to 32px for changelog headings and up to 48px for a page title.

Layout:

- Create a sticky top navigation with a dark background, bottom hairline border, muted nav links, and an outlined pill CTA.
- Center the main content in a 640px to 720px readable column, with wider sections allowed up to 1080px.
- Use a compact tab row near the page title.
- Stack dated changelog entries vertically with about 48px between major entries.
- Use modest inline media, command cards, and app connector icon grids inside the content column.

Components:

- Primary action: transparent pill, 9999px radius, `#f7f8f8` border, `#f7f8f8` text, 14px Inter weight 510, padding around 8px 16px.
- Ghost text action: no border, muted `#8a8f98` text, hover to `#f7f8f8`.
- Search input: `#141516` background, `#23252a` border, 4px radius, compact height, muted placeholder.
- Changelog heading: Inter 24px to 32px, weight 510, `#f7f8f8`, tight tracking if supported.
- Date marker: tiny muted label with optional 6px dot, `#8a8f98`, placed above each entry.
- Command card: `#1c1c1f` background, `#23252a` border, 4px radius, Berkeley Mono content.
- Icon grid: 64px tiles, `#1c1c1f` background, 8px radius, 1px border, centered white glyphs.

Rules:

- Do not use filled colorful CTAs.
- Do not add gradient buttons.
- Do not introduce large accent colors.
- Do not use glassmorphism or heavy drop shadows.
- Do not exceed 8px radius on cards, screenshots, or code blocks.
- Do not use Berkeley Mono for paragraphs or major headings.
- Keep the system compact, monochrome, and technical.

The final UI should read as a polished product changelog: dense but legible, quiet but premium, and clearly designed for developer-facing release content.
