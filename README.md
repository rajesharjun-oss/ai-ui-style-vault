# AI UI Style Vault

A curated, repo-friendly library of UI style references for AI-assisted implementation.

This vault stores public source links, source-derived design notes, tokens, component guidance, and ready-to-paste implementation prompts. It is meant to help Codex or another AI builder create original interfaces with a clear visual direction, without copying protected brand assets or proprietary layouts.

Current contents: 240 Refero Styles bundles.

## Quick Use

1. Open [CAPTURED_STYLES.md](CAPTURED_STYLES.md) or [catalog.json](catalog.json).
2. Choose a style folder under `styles/refero-styles/<style-slug>/`.
3. Give an AI builder the folder plus `implementation-prompt.md`.
4. Use the tokens in `code/` and `tokens/` as visual direction for an original UI.

## Bundle Contents

Each captured style includes:

- `README.md`: quick summary and links to the bundle files.
- `source.md`: Refero URL, reference site, capture metadata, and media links.
- `DESIGN.md`: full AI-readable style reference.
- `implementation-prompt.md`: ready-to-use build prompt.
- `style.json`: structured metadata and token summary.
- `tokens/`: colors, typography, spacing, components, guidelines, layout, and imagery.
- `code/`: CSS variables, Tailwind v4 tokens, and portable design tokens JSON.
- `screenshots/README.md`: media references only; images and videos are linked, not vendored.

## Repository Structure

```text
ai-ui-style-vault/
  README.md
  CAPTURED_STYLES.md
  catalog.json
  sources.json
  scripts/
    generate-catalog.ps1
    validate-vault.ps1
    capture-autonomous-refero-batch.ps1
  templates/
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
```

## Maintenance

Regenerate the catalog after adding styles:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-catalog.ps1
```

Validate the vault before committing:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-vault.ps1
```

## Capture Policy

Save:

- Source URL and attribution.
- Source-derived design rules, tokens, and AI implementation guidance.
- Public media references as links.
- License and usage notes where available.

Avoid:

- Bypassing sign-in, paywalls, CAPTCHA, robots restrictions, or anti-abuse systems.
- Republishing paid or proprietary asset libraries.
- Downloading and vendoring screenshots, logos, videos, or brand assets without permission.
- Treating inspiration-only material as reusable licensed code.

## Suggested AI Prompt

```text
Use the selected style folder as visual direction for an original implementation.
Preserve the mood, spacing, rhythm, and token logic, but do not copy protected logos,
brand assets, exact text, screenshots, or proprietary layouts.

Build production-quality UI with responsive layout, accessibility, loading, empty, and error states,
server-side authorization where relevant, and clean implementation notes.
```