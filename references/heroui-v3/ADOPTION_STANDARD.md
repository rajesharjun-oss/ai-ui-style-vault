# HeroUI Adoption Standard

## Decision gate

Use HeroUI directly when the target stack and product needs justify it. The default compatible path is React 19+ with Tailwind CSS 4 and compatible React Aria peer dependencies.

Do not introduce HeroUI merely because a component exists.

## Selection rule

1. Complete Vault business/product research and select the domain pack.
2. Select the production theme and section recipes.
3. Determine the components and interaction states actually required.
4. Use `component-catalog.json` to shortlist HeroUI primitives.
5. Prefer the upstream package for accessibility-heavy primitives such as dialogs, menus, list boxes, autocomplete, date controls, sliders, selection groups and tables when stack compatibility is strong.
6. Restyle the primitives to the selected Vault design system.
7. Preserve loading, empty, invalid, disabled, selected, focus-visible, open/closed and recovery states as appropriate.

## Accessibility

HeroUI v3 states that it is built on React Aria. When adopting or adapting these components, preserve equivalent keyboard operation, focus management, screen-reader semantics, selection behavior and overlay dismissal.

Do not copy markup mechanically if doing so loses React Aria behavior.

## Visual ownership

HeroUI is an implementation primitive library, not the final brand system. Vault production themes, tokens, typography, spacing, density, domain rules and anti-generic QA remain authoritative.

The same HeroUI primitive may therefore look materially different across a tax platform, couture site, hotel booking flow or SaaS dashboard.

## Provenance and licensing

The inspected `packages/react/package.json` declares MIT, while the repository root `LICENSE` is Apache License 2.0. Treat exact upstream source as third-party material. Before vendoring exact code, verify which license applies to that source, retain applicable copyright and license notices, and mark modified files.

Package installation is preferred over copying source when practical.
