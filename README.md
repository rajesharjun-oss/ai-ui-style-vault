# AI UI Style Vault

A curated, repo-friendly library of UI style references for AI-assisted implementation.

This vault stores public source links, source-derived design notes, tokens, component guidance, screen-reference metadata, motion guidance, and ready-to-paste implementation prompts. It is meant to help Codex or another AI builder create original interfaces with a clear visual direction, without copying protected brand assets, proprietary layouts, screenshots, videos, or logos.

Current contents: 520 Refero Styles bundles, 118 Refero screen references, 512 motion references, 30 premium motion source entries, and 300 MotionSites prompt/background references.

## Quick Use

1. If an AI agent is choosing a design for a target repo, start with [AGENTS.md](AGENTS.md), [agent-index.json](agent-index.json), [guides/AGENT_USAGE.md](guides/AGENT_USAGE.md), and [guides/AGENT_BUILD_CHECKLIST.md](guides/AGENT_BUILD_CHECKLIST.md).
2. For an automated visual first pass, run `scripts/select-vault-style.ps1` with a brief and optional `-ProjectPath`; it writes a `VAULT_SELECTION.generated.md` report.
3. For landing pages, cinematic sites, product tours, scroll stories, or motion graphics websites, run `scripts/select-motion-references.ps1`; it writes a `MOTION_SELECTION.generated.md` report.
4. When more external premium inspiration, licensed motion assets, 3D scenes, Lottie/Rive files, or implementation examples are needed, run `scripts/select-premium-motion-sources.ps1`; it writes a `PREMIUM_MOTION_SOURCE_SELECTION.generated.md` report.
5. When the agent needs AI-builder prompt direction, landing-page prompt scaffolds, section prompts, app prompts, or animated background strategy, run `scripts/select-prompt-references.ps1`; it writes a `PROMPT_REFERENCE_SELECTION.generated.md` report.
6. Open [CAPTURED_STYLES.md](CAPTURED_STYLES.md), [SCREEN_REFERENCES.md](SCREEN_REFERENCES.md), [motion/MOTION_REFERENCES.md](motion/MOTION_REFERENCES.md), [motion/PREMIUM_MOTION_SOURCES.md](motion/PREMIUM_MOTION_SOURCES.md), [motion/MOTIONSITES_PROMPT_REFERENCES.md](motion/MOTIONSITES_PROMPT_REFERENCES.md), [catalog.json](catalog.json), [screen-catalog.json](screen-catalog.json), [motion/motion-catalog.json](motion/motion-catalog.json), [motion/premium-motion-sources.json](motion/premium-motion-sources.json), or [motion/motionsites-prompt-catalog.json](motion/motionsites-prompt-catalog.json).
7. For a full visual system, choose a folder under `styles/refero-styles/<style-slug>/` and give the AI builder `implementation-prompt.md` plus the `tokens/` and `code/` folders.
8. For a specific page type, choose a folder under `screens/refero/<channel>/<page-type>/<screen-slug>/` and give the AI builder `implementation-prompt.md`, `screen.json`, and the linked screenshot references.
9. For professional motion, pair the selected visual style with [motion/LANDING_PAGE_MOTION_GUIDE.md](motion/LANDING_PAGE_MOTION_GUIDE.md), selected motion patterns, MotionSites prompt references, and official implementation resources listed in the motion catalog.
10. Copy [templates/VAULT_SELECTION.md](templates/VAULT_SELECTION.md) into the generated project and fill it before implementation.
11. Use every bundle as inspiration for an original UI. Do not copy logos, brand assets, screenshots, videos, product copy, prompt bodies, animation sequences, or proprietary layouts.

## Agent-Ready Selection

This repo is organized so an AI builder can inspect a target GitHub repository, choose the best matching visual direction, and adapt it to the product.

- [AGENTS.md](AGENTS.md): top-level agent instructions.
- [agent-index.json](agent-index.json): machine-readable entry point, scoring weights, archetypes, and output contract.
- [guides/AGENT_USAGE.md](guides/AGENT_USAGE.md): full workflow for using the vault with a target repo.
- [guides/AGENT_BUILD_CHECKLIST.md](guides/AGENT_BUILD_CHECKLIST.md): required build, asset, and visual QA gates for vault-led implementations.
- [guides/STYLE_SELECTION_GUIDE.md](guides/STYLE_SELECTION_GUIDE.md): scoring method and reading order for style, screen, and motion folders.
- [guides/WEB_TOOL_DESIGN_MATRIX.md](guides/WEB_TOOL_DESIGN_MATRIX.md): product archetypes mapped to useful starting points.
- [guides/SITE_INTERACTION_PATTERNS.md](guides/SITE_INTERACTION_PATTERNS.md): reusable website patterns for rotating heroes, mega menus, brand grids, split utility menus, and icon category drawers.
- [motion/README.md](motion/README.md): entry point for landing-page motion and motion graphics website guidance.
- [motion/LANDING_PAGE_MOTION_GUIDE.md](motion/LANDING_PAGE_MOTION_GUIDE.md): professional motion strategy, patterns, library choices, performance rules, accessibility, and QA guidance.
- [motion/motion-catalog.json](motion/motion-catalog.json): machine-readable motion references, patterns, official implementation resources, and media policy.
- [motion/MOTION_REFERENCES.md](motion/MOTION_REFERENCES.md): human-readable motion-heavy style shortlist.
- [motion/PREMIUM_MOTION_SOURCES.md](motion/PREMIUM_MOTION_SOURCES.md): curated external sources for premium inspiration, licensed motion assets, 3D tools, Lottie/Rive, templates, and implementation examples.
- [motion/premium-motion-sources.json](motion/premium-motion-sources.json): machine-readable premium motion source catalog.
- [scripts/select-premium-motion-sources.ps1](scripts/select-premium-motion-sources.ps1): automated selector for external premium motion sources.
- [motion/MOTIONSITES_PROMPT_REFERENCES.md](motion/MOTIONSITES_PROMPT_REFERENCES.md): MotionSites prompt-card and animated-background references with license-safe usage rules.
- [motion/motionsites-prompt-catalog.json](motion/motionsites-prompt-catalog.json): machine-readable MotionSites prompt/background reference catalog.
- [scripts/select-prompt-references.ps1](scripts/select-prompt-references.ps1): automated selector for MotionSites prompt references.
- [scripts/select-vault-style.ps1](scripts/select-vault-style.ps1): automated first-pass selector that writes a `VAULT_SELECTION.generated.md` report from a brief and optional project path.
- [scripts/select-motion-references.ps1](scripts/select-motion-references.ps1): automated first-pass motion selector that writes a `MOTION_SELECTION.generated.md` report.

Recommended agent behavior:

1. Inspect the target repo and identify product type, audience, page needs, density, tone, stack, and motion needs.
2. Run `scripts/select-vault-style.ps1` for a first-pass visual shortlist, then review it manually.
3. When the build is a landing page, motion-heavy site, cinematic hero, product tour, scroll story, or animated UI, run `scripts/select-motion-references.ps1` and read `motion/LANDING_PAGE_MOTION_GUIDE.md`.
4. When the build needs more external inspiration, licensed assets, 3D scenes, Lottie/Rive files, motion templates, or implementation examples, run `scripts/select-premium-motion-sources.ps1` and record source/license notes.
5. When the build needs AI-builder prompt scaffolding, section prompts, app prompts, or animated background direction, run `scripts/select-prompt-references.ps1` and record source/access notes.
6. Shortlist styles from `catalog.json`.
6. Shortlist page references from `screen-catalog.json`.
7. Choose one primary style bundle, page-specific screen references, and motion patterns only where they help the product communicate.
8. Create a `VAULT_SELECTION.md` record from the template or review the generated selector report.
9. Read the selected folders deeply.
10. Implement an original UI using the target repo's conventions.
11. Run the visual, asset, motion, accessibility, and project checks before handoff.

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

## Motion Contents

The motion layer helps agents build professional landing pages and motion graphics websites without guessing choreography or copying another site's animation.

- `motion/README.md`: how to use the motion layer.
- `motion/LANDING_PAGE_MOTION_GUIDE.md`: motion models, patterns, library choice, timing tokens, reduced-motion contract, and QA rules.
- `motion/motion-catalog.json`: 512 motion-relevant style references, 34 high-signal motion systems, 346 references with preview video links, 21 motion patterns, and official implementation-resource links.
- `motion/MOTION_REFERENCES.md`: scan-friendly shortlist for motion-heavy styles and patterns.
- `motion/PREMIUM_MOTION_SOURCES.md`: 30 external premium motion sources grouped by inspiration, implementation, 3D/interactive tools, and licensed asset/template sources.
- `motion/premium-motion-sources.json`: machine-readable catalog for external premium motion source selection.
- `motion/MOTIONSITES_PROMPT_REFERENCES.md`: 300 MotionSites prompt-card and animated-background references for prompt direction.
- `motion/motionsites-prompt-catalog.json`: machine-readable MotionSites prompt/background reference catalog.

Use motion references as choreography guidance only. Build original animation from the target product, user-provided assets, generated assets, owned assets, or clearly licensed media. Use MotionSites prompt references as source-linked direction only; do not republish full prompt bodies, premium prompt text, screenshots, videos, assets, generated outputs, or copied code.

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
  motion/
    README.md
    LANDING_PAGE_MOTION_GUIDE.md
    MOTION_REFERENCES.md
    motion-catalog.json
  scripts/
    capture-autonomous-refero-batch.ps1
    capture-refero-style-ids.ps1
    generate-catalog.ps1
    generate-motion-catalog.ps1
    generate-refero-screen-references.ps1
    select-motion-references.ps1
    select-vault-style.ps1
    validate-generated-site.ps1
    validate-agent-guides.ps1
    validate-motion-catalog.ps1
    validate-prompt-references.ps1
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

Generate a first-pass vault selection report for a target repo or brief:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\select-vault-style.ps1 -Brief "Premium B2B analytics dashboard with login, pricing, integrations, and contacts" -ProjectPath <target-repo> -OutputPath <target-repo>\VAULT_SELECTION.generated.md
```

Generate motion references from the captured style catalog:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-motion-catalog.ps1
```

Generate a first-pass motion selection report for a target repo or brief:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\select-motion-references.ps1 -Brief "Cinematic SaaS landing page with scroll product story and animated product tour" -ProjectPath <target-repo> -OutputPath <target-repo>\MOTION_SELECTION.generated.md
```

Generate a first-pass premium motion source report for external inspiration or licensed assets:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\select-premium-motion-sources.ps1 -Brief "Cinematic 3D SaaS landing page with licensed hero motion assets" -ProjectPath <target-repo> -OutputPath <target-repo>\PREMIUM_MOTION_SOURCE_SELECTION.generated.md
```

Generate a first-pass MotionSites prompt reference report:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\select-prompt-references.ps1 -Brief "Premium AI SaaS landing page with animated hero, pricing, dashboard preview, and abstract background" -IncludeBackgrounds -OutputPath <target-repo>\PROMPT_REFERENCE_SELECTION.generated.md
```

Generate screen references from downloaded public Refero search JSON files:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate-refero-screen-references.ps1 -InputRoot C:\tmp -OutputRoot .\screens\refero -PerChannelPerType 5
```

Validate before committing:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-vault.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-screen-references.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-motion-catalog.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\validate-prompt-references.ps1
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
- Motion model, animation signals, motion patterns, official implementation docs, and reduced-motion notes.

Avoid:

- Bypassing sign-in, paywalls, CAPTCHA, robots restrictions, or anti-abuse systems.
- Republishing paid or proprietary asset libraries.
- Downloading and vendoring screenshots, logos, videos, animation files, or brand assets without permission.
- Copying reference-site animation sequences or proprietary brand motion.
- Treating inspiration-only material as reusable licensed code.

## Suggested AI Prompt

```text
Use the selected vault folder as visual direction for an original implementation.
Preserve the mood, spacing, rhythm, page-type intent, token logic, and useful motion attitude, but do not copy protected logos,
brand assets, exact text, screenshots, videos, animation sequences, or proprietary layouts.

For landing pages or motion-heavy sites, also run the motion selector, read the motion guide,
choose a small set of motion patterns, and implement reduced-motion fallbacks.

Build production-quality UI with responsive layout, accessibility, loading, empty, and error states,
server-side authorization where relevant, and clean implementation notes.
```


## 3D & Immersive Web capability pack

`packs/3d-immersive-web/` covers purposeful 3D sites, configurators, spatial portfolios, showrooms, digital twins, globes and AR/XR. It includes 21 style families, 39 interactions, 30 source records, 34 technique records and 0 Refs.Gallery metadata links.

```bash
python scripts/select-3d-references.py "premium product configurator"
python scripts/validate-3d-immersive-pack.py
```
