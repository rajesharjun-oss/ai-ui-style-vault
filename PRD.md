# Product Requirements Document

## Product

**AI UI Style Vault** is a cross-agent product-design, content-design, and front-end engineering system for creating original, premium websites, web applications, dashboards, and app interfaces.

The vault is not a cloning library and it is not a replacement for business research, product thinking, real assets, browser testing, or human review.

## Problem

AI coding tools can generate functional interfaces quickly, but they often default to:

- Generic SaaS layouts and interchangeable marketing copy.
- Excessive paragraphs, cards, gradients, pills, and oversized headings.
- Weak information architecture and incomplete product states.
- Inconsistent imagery and motion used as decoration.
- Desktop-first output with mobile clipping or sticky-header overlap.
- Claims of completion without rendered visual inspection.
- Localhost links that are not actually reachable from the user’s computer.

The product must give AI agents a repeatable operating system that produces deliberate, product-specific work and validates the result before handoff.

## Primary Users

- Developers and vibe coders building websites or applications with AI.
- Product teams that want consistent design quality across AI coding agents.
- Agencies and consultants building sites for businesses.
- Codex, Claude Code, Gemini CLI, and other repository-aware coding agents.

## Product Goals

1. Make the agent behave as a coordinated senior product designer, content designer, and front-end engineer.
2. Require business and user understanding before implementation.
3. Provide discoverable, platform-native instructions for major coding agents.
4. Select one coherent visual system rather than mixing unrelated references.
5. Control content density and remove generic AI writing.
6. Require realistic assets and consistent art direction.
7. Require responsive, accessible components with complete states.
8. Require browser rendering, screenshot review, correction, and evidence.
9. Make handoff truthful about localhost, deployment, assets, assumptions, and remaining risks.

## Core Experience

For every build, the agent must:

1. Read the platform-native root instruction file.
2. Read `AGENTS.md`, `PROMPTS.md`, and the prompt selected by the routing rules.
3. Inspect the target repository and business sources.
4. Separate verified facts from assumptions.
5. Create the planning and design contracts.
6. Select one primary style and a restrained motion model.
7. Build an original interface using the target project’s stack.
8. Run code, content, accessibility, asset, and visual checks.
9. Render desktop and mobile views.
10. Revise visible problems before reporting completion.

## Cross-Agent Discovery Requirements

The repository must maintain:

- `AGENTS.md` for Codex and generic repository-aware agents.
- `CLAUDE.md` for Claude Code.
- `GEMINI.md` for Gemini CLI.
- `PROMPTS.md` as the human-readable prompt router.
- `prompts/prompt-index.json` as the machine-readable router.
- Task prompts under `prompts/`.

The platform adapters must point back to the canonical rules rather than duplicate and drift from them.

## Mandatory Task Prompts

The vault must include at least:

- A prompt for building a new premium business website.
- A prompt for refining or redesigning an existing business website.
- A prompt for rendered visual QA and revision.
- A general senior product-team prompt.

## Required Project Contracts

Before UI implementation, the target project must contain completed equivalents of:

- `BUSINESS_RESEARCH.md` when a real business is involved.
- `ASSET_PLAN.md` when imagery, video, illustration, or 3D is involved.
- `VAULT_SELECTION.md`.
- `BUILD_CONTRACT.md`.
- `CONTENT_PLAN.md`.
- `design-recipe.json`.

## Content Requirements

- One clear purpose and primary action per page.
- Concise first viewport.
- Specific, industry-appropriate language.
- Progressive disclosure for secondary detail.
- No repeated benefits or filler sections.
- No generic AI marketing phrases without evidence.
- Practical business information must be easy to find.
- Operational application screens must use task language, not promotional copy.

## Visual and Asset Requirements

- One primary production theme and style bundle.
- Original composition adapted to the actual business.
- Consistent image treatment, crop, lighting, and quality.
- Distinct imagery for distinct messages; avoid repeating one hero image throughout a page.
- Use process imagery to prove process claims.
- Use realistic product imagery for food, retail, hospitality, property, and other product-led businesses unless the brief explicitly requests illustration.
- Use user-provided, original, generated, owned, or clearly licensed assets only.
- Do not hotlink or copy protected target-site media.

## Engineering Requirements

- Preserve the target stack unless a change is justified.
- Semantic HTML and accessible interactions.
- Keyboard operation and visible focus.
- Responsive transformation defined for desktop, laptop, tablet, and mobile.
- Complete loading, empty, error, success, disabled, permission, destructive, and recovery states where relevant.
- Reduced-motion behaviour.
- Performance-conscious asset and animation choices.
- No placeholder, TODO-heavy, or console-debug output at handoff.

## Visual QA Requirements

A build is not complete from source-code inspection alone. The agent must:

- Render the interface in a browser.
- Check at least 1440×1000, 1280×800, and approximately 390×844.
- Inspect sticky headers, anchor offsets, clipping, wrapping, overflow, image quality, repeated imagery, hierarchy, content density, and mobile navigation.
- Test key interactions and states.
- Revise and recapture screenshots until no blocking visual issue remains.

## Localhost and Handoff Requirements

- Never imply that a server running in an isolated or remote environment is automatically reachable from the user’s computer.
- When operating on the user’s machine, start the server there, verify the exact port, and keep the process alive.
- When operating remotely, state the limitation and provide a deployable package, preview artifact, or exact local start command.
- Report the exact commands run, URLs verified, screenshots captured, assets used, assumptions made, and remaining risks.

## Out of Scope

- Pixel-for-pixel brand cloning.
- Republishing protected logos, screenshots, video, code, or premium prompt text.
- Guaranteeing premium output without business research, suitable assets, rendered QA, and revision.
- Treating motion, 3D, gradients, or complex effects as mandatory.

## Success Criteria

The vault succeeds when different supported agents can:

- Discover the correct instructions without the user manually pasting every rule.
- Produce the required project contracts before coding.
- Generate concise, product-specific interfaces.
- Pass automated content and repository checks.
- Show verified desktop and mobile renders.
- Explain what was verified, adapted, generated, and still provisional.
