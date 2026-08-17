# Mandatory Business Research Gate

This gate applies whenever the user asks the vault to build, redesign or extend a website for a real business, brand, creator, professional practice, venue, product, service or organisation.

## Core rule

**Understand the business before selecting the design.**

Do not choose a style bundle, production theme, 3D scene, motion recipe, hero composition, imagery system, sitemap or conversion flow merely from a business name, handle, logo, category guess or one inaccessible social link.

The design must be a consequence of verified business understanding.

## Required research outcome

Before any visual-direction or AI-agent-recipe selection, create `BUSINESS_RESEARCH.md` and establish enough evidence to answer all of the following:

1. What is the official or publicly used business/brand name?
2. What does the business actually do?
3. What products, services, experiences or content does it offer?
4. Who are the primary customers, users, guests, viewers or clients?
5. What geographic market, location or service area is relevant, if any?
6. What is the most valuable primary action the website should drive?
7. What practical questions must a visitor be able to answer?
8. What visual, cultural, tonal and brand signals are repeatedly observable in the business's own public presence?
9. What proof, work, products, people, venues, process or results can be supported by evidence?
10. Which facts are verified, which are reasonable inferences, and which require owner confirmation?

A business category alone is not sufficient research.

## Source strategy

Start with the user's supplied sources, then expand to current public evidence when needed. Depending on the business, useful sources may include:

- official website;
- Instagram, TikTok, YouTube, Facebook, LinkedIn or X;
- Google/Maps or other business listings;
- booking, ordering, marketplace or ticketing pages;
- interviews, press, portfolio pages or event listings;
- reputable directories and customer-review signals;
- other pages clearly controlled by or referring to the same business.

Cross-check identity before combining facts from different sources.

## Blocked-source rule

If a supplied Instagram, TikTok or other page cannot be inspected:

1. Do not infer the entire business from the username, page title or inaccessible URL.
2. Search for alternative public sources that can establish the same business facts.
3. Search for indexed snippets, official cross-links, public business listings or other controlled profiles.
4. Record exactly what was and was not verifiable.
5. If the minimum research outcome still cannot be established, **stop before design selection and implementation**.
6. Ask the user for screenshots, a screen recording, profile bio, catalogue/menu/service list, brand deck or other evidence sufficient to understand the business.

Do not compensate for missing research by building a generic concept.

## Minimum design-readiness gate

`researchStatus` may be `ready`, `partial` or `blocked`.

A real-business build may proceed to `VAULT_SELECTION.md` only when `researchStatus = ready`.

`ready` requires, at minimum:

- business/category understood from evidence;
- core offer understood;
- target audience/customer understood well enough to design for;
- primary conversion or user task identified;
- major content types identified;
- meaningful brand/visual signals identified or explicitly documented as unavailable;
- no central business assumption being presented as fact.

`partial` means useful facts exist but one or more central questions remain unresolved. Continue research.

`blocked` means the agent cannot reliably determine what the business is or what the site should achieve. Request evidence; do not select a vault design.

## Required sequence

For a real-business website, the mandatory order is:

`environment inspection → business research → research gate → product/content strategy → asset strategy → vault/style/3D recipe selection → contracts → implementation → render → visual QA → validation → handoff`

Never reorder this to choose a visually attractive vault direction first.

## 3D-specific consequence

For 3D/motion builds, no scene archetype, art direction, model, video, shader, environment, or MotionSites/reference recipe may be selected until the business research gate is `ready`.

The business evidence must determine:

- whether 3D materially helps;
- which subjects are semantically relevant;
- which visual metaphors are defensible;
- which motion language fits the brand and task;
- what should remain ordinary DOM/UI rather than spectacle.

The semantic-relevance gate is applied **after** business understanding, not as a substitute for it.

## Handoff evidence

The final handoff must state:

- research status;
- sources used;
- key verified business facts;
- unresolved owner-confirmation items;
- how those findings caused the selected design and motion direction.

A build that cannot explain that causal link is not a vault-compliant business website.
