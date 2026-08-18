# HeroUI v3 Reference Integration

This directory makes the public `heroui-inc/heroui` v3 repository discoverable to AI agents using the AI UI Style Vault.

## What was captured

- All **82 React component families** exported by `packages/react/src/components/index.ts`.
- All **10 public hooks** exported by `packages/react/src/hooks/index.ts`.
- Source-path references to the matching `packages/styles/src/components/` variant definitions where applicable.
- State families, adoption modes, stack compatibility rules, accessibility expectations and provenance requirements.
- A selector that can shortlist HeroUI primitives for a requested interface capability without making HeroUI the visual design system by default.

## Why this is a reference/integration layer

HeroUI is a mature React/Tailwind/React Aria component library. The Vault should use it as an implementation accelerator when the project stack and design direction justify it. It must not cause every generated site to look like HeroUI.

Preferred order:

1. Decide product/domain/visual direction with the Vault.
2. Determine required components and states.
3. If React 19 + Tailwind CSS 4 is compatible, prefer installing `@heroui/react` and style it to the selected Vault system.
4. Otherwise use this catalog as a behavioral/accessibility reference and implement equivalent primitives in the target stack.
5. Vendor upstream source only when necessary and only while retaining all applicable license/copyright notices.

## Licensing/provenance

The inspected `packages/react/package.json` declares `MIT`, while the repository root `LICENSE` file is Apache License 2.0. Because those signals differ, the Vault takes a conservative approach: do not strip notices, keep upstream provenance, and verify the current license applying to any exact source file before vendoring it.

HeroUI names and trademarks are not a visual asset library for client work.

## Upstream strengths worth preserving

HeroUI v3 is built around React Aria behavior, compound component APIs, Tailwind CSS v4, accessible keyboard/focus/screen-reader behavior, and explicit interactive states. The Vault should inherit those engineering qualities while preserving its own business research, originality, content, visual-direction and anti-generic rules.
