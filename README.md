# AI UI Style Vault

A curated, repo-friendly library of UI style references for AI-assisted implementation.

This vault stores public source links, source-derived design notes, tokens, component guidance, screen-reference metadata, and ready-to-paste implementation prompts. It is meant to help Codex or another AI builder create original interfaces with a clear visual direction, without copying protected brand assets or proprietary layouts.

Current contents: 520 Refero Styles bundles and 48 Refero screen references.

## Quick Use

1. If an AI agent is choosing a design for a target repo, start with [AGENTS.md](AGENTS.md), [agent-index.json](agent-index.json), [guides/AGENT_USAGE.md](guides/AGENT_USAGE.md), and [guides/AGENT_BUILD_CHECKLIST.md](guides/AGENT_BUILD_CHECKLIST.md).
2. Open [CAPTURED_STYLES.md](CAPTURED_STYLES.md), [SCREEN_REFERENCES.md](SCREEN_REFERENCES.md), [catalog.json](catalog.json), or [screen-catalog.json](screen-catalog.json).
3. For a full visual system, choose a folder under `styles/refero-styles/<style-slug>/` and give the AI builder `implementation-prompt.md` plus the `tokens/` and `code/` folders.
4. For a specific page type, choose a folder under `screens/refero/<channel>/<page-type>/<screen-slug>/` and give the AI builder `implementation-prompt.md`, `screen.json`, and the linked screenshot references.
5. Copy [templates/VAULT_SELECTION.md](templates/VAULT_SELECTION.md) into the generated project and fill it before implementation.
6. Use every bundle as inspiration for an original UI. Do not copy logos, brand assets, screenshots, product copy, or proprietary layouts.

## Agent-Ready Selection

This repo is organized so an AI builder can inspect a target GitHub repository, choose the best matching visual direction, and adapt it to the product.

- [AGENTS.md](AGENTS.md): top-level agent instructions.
- [agent-index.json](agent-index.json): machine-readable entry point, scoring weights, archetypes, and output contract.
- [guides/AGENT_USAGE.md](guides/AGENT_USAGE.md): full workflow for using the vault with a target repo.
- [guides/AGENT_BUILD_CHECKLIST.md](guides/AGENT_BUILD_CHECKLIST.md): required build, asset, and visual QA gates for vault-led implementations.
- [guides/STYLE_SELECTION_GUIDE.md](guides/STYLE_SELECTION_GUIDE.md): scoring method and reading order for style and screen folders.
- [guides/WEB_TOOL_DESIGN_MATRIX.md](guides/WEB_TOOL_DESIGN_MATRIX.md): product archetypes mapped to useful starting points.
- [guides/SITE_INTERACTION_PATTERNS.md](guides/SITE_INTERACTION_PATTERNS.md): reusable website patterns for rotating heroes, mega menus, brand grids, split utility menus, and icon category drawers.

Recommended agent behavior:

1. Inspect the target repo and identify product type, audience, page needs, density, tone, and stack.
2. Shortlist styles from `catalog.json`.
3. Shortlist page references from `screen-catalog.json`.
4. Choose one primary style bundle and page-specific screen references.
5. Create a `VAULT_SELECTION.md` record from the template.
6. Read the selected folders deeply.
7. Implement an original UI using the target repo's conventions.
8. Run the visual and asset QA gates before handoff.

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
  AGENTS.md
  agent-index.json
  CAPTURED_STYLES.md
  SCREEN_REFERENCES.md
  catalog.json
  screen-catalog.json
  sources.json
  guides/
    AGENT_USAGE.md
    AGENT_BUILD_CHECKLIST.md
    SITE_INTERACTION_PATTERNS.md
    STYLE_SELECTION_GUIDE.md
    WEB_TOOL_DESIGN_MATRIX.md
  scripts/
    capture-autonomous-refero-batch.ps1
    capture-refero-style-ids.ps1
    generate-catalog.ps1
    generate-refero-screen-references.ps1
    validate-generated-site.ps1
    validate-agent-guides.ps1
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
    VAULT_SELECTION.md
```

## Maintenance

Regenerate the style catalog after adding styles:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-catalog.ps1
```

Capture public Refero style pages from a prepared ID list:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\capture-refero-style-ids.ps1 -IdsFile C:\tmp\refero-style-ids.txt -Limit 50
```

Generate screen references from downloaded public Refero search JSON files:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-refero-screen-references.ps1 -InputRoot C:\tmp -OutputRoot .\screens\refero -PerChannelPerType 2
```

Validate before committing:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-vault.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-screen-references.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-agent-guides.ps1
```

Validate a generated site before handoff:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-generated-site.ps1 -SiteRoot <site-root>
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
