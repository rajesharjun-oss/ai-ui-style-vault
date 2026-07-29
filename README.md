# AI UI Style Vault

A curated, repo-friendly library of UI style references for AI-assisted implementation.

This vault stores public source links, source-derived design notes, tokens, component guidance, screen-reference metadata, and ready-to-paste implementation prompts. It is meant to help Codex or another AI builder create original interfaces with a clear visual direction, without copying protected brand assets or proprietary layouts.

Current contents: 256 Refero Styles bundles and 48 Refero screen references.

## Quick Use

1. Open [CAPTURED_STYLES.md](CAPTURED_STYLES.md), [SCREEN_REFERENCES.md](SCREEN_REFERENCES.md), [catalog.json](catalog.json), or [screen-catalog.json](screen-catalog.json).
2. For a full visual system, choose a folder under `styles/refero-styles/<style-slug>/` and give the AI builder `implementation-prompt.md` plus the `tokens/` and `code/` folders.
3. For a specific page type, choose a folder under `screens/refero/<channel>/<page-type>/<screen-slug>/` and give the AI builder `implementation-prompt.md`, `screen.json`, and the linked screenshot references.
4. Use every bundle as inspiration for an original UI. Do not copy logos, brand assets, screenshots, product copy, or proprietary layouts.

## Style Bundle Contents

Each captured Refero style includes:

- `README.md`: quick summary and links to the bundle files.
- `source.md`: Refero URL, reference site, capture metadata, and media links.
- `DESIGN.md`: full AI-readable style reference.
- `implementation-prompt.md`: ready-to-use build prompt.
- `style.json`: structured metadata and token summary.
- `tokens/`: colors, typography, spacing, components, guidelines, layout, and imagery.
- `code/`: CSS variables, Tailwind v4 tokens, and portable design tokens JSON.
- `screenshots/README.md`: media references only; images and videos are linked, not vendored.

## Screen Reference Contents

Each Refero screen reference includes:

- `README.md`: page-type summary, source channel, entity link, and usage note.
- `source.md`: Refero view/search/API links, capture metadata, and media references.
- `implementation-prompt.md`: page-type-specific AI build prompt.
- `screen.json`: structured app/site, page type, palette, media, font, pattern, and element metadata.
- `tokens/`: extracted colors and tagged page elements.
- `code/`: CSS variables and design tokens JSON derived from the screen metadata.
- `screenshots/README.md`: remote image/video URLs only; no vendored media.

## Repository Structure

```text
ai-ui-style-vault/
  README.md
  CAPTURED_STYLES.md
  SCREEN_REFERENCES.md
  catalog.json
  screen-catalog.json
  sources.json
  scripts/
    capture-autonomous-refero-batch.ps1
    generate-catalog.ps1
    generate-refero-screen-references.ps1
    validate-screen-references.ps1
    validate-vault.ps1
  styles/
    refero-styles/
      <style-slug>/
        README.md
        DESIGN.md
        source.md
        implementation-prompt.md
        style.json
        tokens/
        code/
        screenshots/
  screens/
    refero/
      page-types.json
      ios-apps/
      web/
        <page-type>/
          <screen-slug>/
            README.md
            source.md
            implementation-prompt.md
            screen.json
            tokens/
            code/
            screenshots/
  templates/
```

## Maintenance

Regenerate the style catalog after adding styles:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-catalog.ps1
```

Generate screen references from downloaded public Refero search JSON files:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-refero-screen-references.ps1 -InputRoot C:\tmp -OutputRoot .\screens\refero -PerChannelPerType 2
```

Validate before committing:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-vault.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-screen-references.ps1
```

## Capture Policy

Save:

- Source URL and attribution.
- Source-derived design rules, tokens, and AI implementation guidance.
- Public media references as links.
- License and usage notes where available.
- Page type, component, font, palette, and app/site metadata useful for AI implementation.

Avoid:

- Bypassing sign-in, paywalls, CAPTCHA, robots restrictions, or anti-abuse systems.
- Republishing paid or proprietary asset libraries.
- Downloading and vendoring screenshots, logos, videos, or brand assets without permission.
- Treating inspiration-only material as reusable licensed code.

## Suggested AI Prompt

```text
Use the selected vault folder as visual direction for an original implementation.
Preserve the mood, spacing, rhythm, page-type intent, and token logic, but do not copy protected logos,
brand assets, exact text, screenshots, or proprietary layouts.

Build production-quality UI with responsive layout, accessibility, loading, empty, and error states,
server-side authorization where relevant, and clean implementation notes.
```
