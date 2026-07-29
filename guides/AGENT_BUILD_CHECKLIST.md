# Agent Build Checklist

Use this checklist whenever an AI builder uses this vault to design or rebuild a website, web app, dashboard, or app screen.

The goal is to keep the workflow clear: business sources provide facts, while this vault provides the design direction. A finished build should feel intentionally adapted from selected vault references, not copied from the target business website.

## Required Order

1. Inspect the target product or business.
   - Treat maps, websites, social pages, app stores, and search results as factual context only.
   - Extract audience, offer, location, services, credibility signals, page needs, and constraints.
   - Do not copy protected logos, screenshots, marketing copy, image assets, videos, page structure, or brand-specific layouts.

2. Select vault references before implementation.
   - Pick one primary style bundle for global visual direction.
   - Pick page-specific screen references for required page types.
   - Read the selected files deeply, including `DESIGN.md`, `implementation-prompt.md`, `tokens/`, `code/`, `screen.json`, and `tokens/page-elements.md`.

3. Create a selection record before building.
   - Copy `templates/VAULT_SELECTION.md` into the generated project or target repo.
   - Fill in primary style, supporting references, fit rationale, adaptation plan, asset policy, and QA plan.
   - If this record is missing, the build is not ready to hand off.

4. Implement an original UI.
   - Use target repo conventions, framework, routing, components, and build commands.
   - Translate vault tokens into the local design system.
   - Tailor content hierarchy, navigation, forms, states, and responsiveness to the actual product.
   - Preserve useful token logic, spacing rhythm, mood, component behavior, and page-type structure.

5. Verify with visual and asset checks before handoff.
   - Run available lint, typecheck, tests, and build commands.
   - Run the generated-site validator when the output is a static or browser-rendered site.
   - Capture or inspect desktop and mobile views.
   - Fix layout overlap, clipped text, anchor jumps, broken forms, and copied asset risks before saying done.

## Visual QA Gate

Check at least these viewports when a browser-rendered UI exists:

- Desktop: 1440 x 1000 or wider.
- Laptop: 1280 x 800.
- Mobile: 390 x 844 or similar.

Review these problem areas:

- Headers and navs: fixed or sticky elements must not cover section headings, forms, cards, or anchor targets.
- Hero: first viewport must show the product or offer and leave the next section discoverable when appropriate.
- Section anchors: every nav link must land with the heading visible.
- Typography: long headings must wrap cleanly and not collide with surrounding content.
- Cards and panels: no nested-card clutter, accidental clipping, or text escaping the container.
- Forms: labels, legends, checkboxes, selects, textareas, errors, and buttons must have clear spacing and focus states.
- Media: images must render, crop intentionally, and not obscure important content.
- Mobile menu: must open, close, and not trap the page in a broken state.
- Footer: should not overlap content and should keep useful navigation visible.

## Asset QA Gate

Generated builds must pass this policy unless the user explicitly supplies assets or grants permission:

- Do not vendor or hotlink protected logos, screenshots, videos, or product photography from the target business site.
- Do not use external image URLs from the business domain as `img src`.
- Use original generated assets, user-provided assets, locally owned assets, or clearly licensed media.
- Keep public source links in research notes, not as copied design assets.

Useful checks:

```powershell
rg --fixed-strings 'src="http' <site-root>
rg --fixed-strings "src='http" <site-root>
rg --fixed-strings 'wp-content' <site-root>
rg -n "TODO|PLACEHOLDER|lorem|console\.log" <site-root>
```

## Generated Site Validator

For static or browser-rendered outputs, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-generated-site.ps1 -SiteRoot <site-root>
```

If the target business has a known asset host, include it:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-generated-site.ps1 -SiteRoot <site-root> -BlockedAssetHost "example.com/wp-content"
```

If a local server is running, include the URL:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-generated-site.ps1 -SiteRoot <site-root> -Url "http://127.0.0.1:5199"
```

## Handoff Requirements

Before final response, confirm:

- The selected vault references are documented.
- The business source was used only for factual context.
- No protected target-site assets were copied.
- Visual QA covered desktop and mobile.
- Any fixed or sticky header behavior was checked against anchor targets.
- Forms and fieldsets were checked for label and legend spacing.
- The site or app is running locally when requested.
- Remaining risks or manual checks are clearly stated.

## Reject Conditions

Do not hand off as complete when any of these are true:

- No vault reference was selected.
- No `VAULT_SELECTION.md` or equivalent selection record exists.
- The build hotlinks or vendors target-site images without permission.
- A fixed or sticky header covers content.
- A form label or legend is clipped.
- Desktop or mobile layout has obvious overlap.
- The build contains placeholder-only sections, lorem ipsum, TODO-heavy UI, or console debugging.
