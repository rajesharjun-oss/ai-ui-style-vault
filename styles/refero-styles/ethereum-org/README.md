# ethereum.org

Source: [Refero Style](https://styles.refero.design/style/f53b2759-5b4a-4509-9311-51ab74238326)
Reference site: [https://ethereum.org](https://ethereum.org)
Captured: 2026-07-31
Refero published: 2026-02-11T09:08:06.000Z
Refero modified: 2026-06-05T08:47:40.671Z
Theme: light
Category: Crypto

## Style Summary

Explore ethereum.org's light Crypto design system: Lavender Paper #ece0ff, Pure White #ffffff colors, Inter, IBM Plex Mono typography, and DESIGN.md for AI...

North star: Lilac architecture in flat editorial space - a printed open-source almanac where the Ethereum diamond floats above duotone crowds of people.

## What To Borrow

- Lavender Paper `#ece0ff` for Page canvas, soft card surfaces, hero wash - near-gray violet that reads as neutral paper across the entire site
- Pure White `#ffffff` for Card surface above canvas, icon strokes, inverse text on violet buttons, nav background
- Ash Gray `#cfcfcf` for Hairline dividers, card borders, input borders, separator rules - the dominant border tone at 2484 occurrences
- Onyx `#121212` for Primary text, heading fill, dark icon strokes - the only body-color the UI commits to
- Graphite `#616161` for Secondary body text, muted helper copy, nav subtext
- Fog `#8c8c8c` for Tertiary text, disabled nav items, low-priority borders
- Ethereum Violet `#6c24e0` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Deep Iris `#41128c` for Hover state on violet, dark accent surface, gradient origin - the violet pushed to its shadow end
- Hot Magenta `#f60e9d` for Secondary accent for inline links inside feature cards, tag pills, illustration accent
- Sapphire `#3d4ceb` for Tertiary accent for links, icon variants, illustration cool-tone accents
- Mint `#0f9972` for Green supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color

- Inter `--font-inter` for Sole workhorse - body at 16px/400, section headings at 24-30px/700, and display at 48-64px/900. The 900 weight at 60-64px is the signature: headlines are not politely bold, they are geometric slabs that anchor every section
- IBM Plex Mono `--font-ibm-plex-mono` for Used only for keyboard shortcut hints in the search bar (cmd/k label). Never used for body or heading

## Avoid

- Don't use drop shadows for elevation - hierarchy comes from flat surface tints, not depth
- Don't use 600 or 800 weight for headlines - the system commits to 900 or 700 only, and 900 only at display sizes
- Don't introduce new saturated colors beyond the existing four (#6c24e0, #f60e9d, #3d4ceb, #0f9972) - the palette is rationed
- Don't use pill-shaped buttons (9999px) for primary actions - that radius is reserved for search triggers and tags
- Don't stack text directly on the full-bleed illustration without the centered headline block underneath it
- Don't use centered body text - body paragraphs are always left-aligned at max 65ch width
- Don't use photography as the primary visual - illustration owns this system, photos should only appear in editorial context if at all

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
