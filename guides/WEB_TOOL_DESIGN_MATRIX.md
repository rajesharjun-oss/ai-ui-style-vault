# Web Tool Design Matrix

Use this matrix to connect common product types to useful vault references. Treat these as starting points, then verify with `catalog.json`, `screen-catalog.json`, and the selected folders.

## Product Archetypes

| Product Type | Good Style Signals | Useful Style Starting Points | Useful Screen Page Types |
|---|---|---|---|
| AI assistant or AI workspace | Calm technical palette, clear prompt surfaces, trust-building editorial copy, strong empty states | `anthropic`, `claude`, `cursor`, `dimension`, `factory`, `elevenlabs` | Dashboard, Log In, Developers Page, Blog |
| Developer tool or API product | Dense docs-friendly typography, terminal/code motifs, restrained palette, precise CTAs | `cursor`, `factory`, `grafbase`, `browserbase`, `caldera`, `changelog` | Developers Page, Integration Page, Dashboard, Log In |
| SaaS dashboard or admin panel | High-density layout, clear hierarchy, tables, charts, filters, muted surfaces | `basedash`, `attio`, `dub`, `altitude`, `assurestor`, `august-health-ehr` | Dashboard, Profile & Account, Contacts, Log In |
| Finance, fintech, crypto, or analytics | High contrast, strong numerals, chart readability, serious trust tone | `fey`, `glassnode`, `fold`, `acctual`, `altitude`, `auros` | Dashboard, Product Details, Profile & Account, Paywall & Subscription |
| Ecommerce or product catalog | Product-first imagery, clear filters, price and CTA hierarchy, fast scanning | `apple`, `acne-studios`, `becane`, `emmalewisham`, `arsenijs-fabrica` | Product Page & Landing, Product Details, Catalog Page, 404 Page |
| Marketplace or service platform | Cards, provider profiles, search/filter UX, social proof, trust states | `awesomic`, `cord`, `dribbble`, `cosmos`, `creative-giants` | Catalog Page, Profile & Account, Product Details, Contacts |
| Health, wellness, or care product | Warm neutral palette, calm spacing, accessible type, reassurance over spectacle | `alden`, `ease-health`, `august-health-ehr`, `amaterasu` | Dashboard, Profile & Account, Paywall & Subscription, About |
| Education or learning app | Friendly color, progress states, approachable cards, lightweight gamification | `duolingo`, `goodnotes`, `evernote`, `foodnoms` | Dashboard, Blog, Profile & Account, Paywall & Subscription |
| Creative studio or portfolio | Editorial rhythm, image-led case studies, distinctive typography, strong whitespace | `active-theory`, `area-17`, `dash-digital-studio`, `branding`, `247studio` | About, Blog, Media Kit, Contacts |
| Corporate or enterprise landing page | Clear proof, calm hero, feature sections, integrations, customer logos, accessible CTAs | `ai-for-business`, `amplemarket`, `frontify`, `dock`, `atlassian` | Product Page & Landing, Integration Page, Careers, Contacts |

## Page Type Pairing

| Needed Page | Start In |
|---|---|
| Dashboard | `screens/refero/ios-apps/dashboard/` and `screens/refero/web/dashboard/` |
| Login | `screens/refero/ios-apps/login/` and `screens/refero/web/login/` |
| Product landing | `screens/refero/web/product-page-landing/` |
| Pricing or paywall | `screens/refero/ios-apps/paywall-subscription/` and `screens/refero/web/paywall-subscription/` |
| Product details | `screens/refero/ios-apps/product-details/` and `screens/refero/web/product-details/` |
| Profile/settings | `screens/refero/ios-apps/profile-account/` and `screens/refero/web/profile-account/` |
| Catalog/search results | `screens/refero/ios-apps/catalog-page/` and `screens/refero/web/catalog-page/` |
| Blog/editorial | `screens/refero/ios-apps/blog/` and `screens/refero/web/blog/` |
| About | `screens/refero/ios-apps/about/` and `screens/refero/web/about/` |
| Careers | `screens/refero/web/careers/` |
| Contacts/support | `screens/refero/ios-apps/contacts/` and `screens/refero/web/contacts/` |
| Developer docs | `screens/refero/web/developers-page/` |
| Integrations | `screens/refero/web/integration-page/` |
| Media kit | `screens/refero/web/media-kit/` |
| 404 | `screens/refero/web/404-page/` |

## Density Rules

For low-density marketing pages:

- Favor editorial rhythm, larger type, fewer controls, and strong section pacing.
- Use screen references for hero, feature, proof, pricing, and footer composition.

For medium-density SaaS tools:

- Favor restrained visual systems with clear cards, forms, tabs, and navigation.
- Use page references for dashboard, login, settings, and contacts.

For high-density operational tools:

- Prioritize legibility, stable spacing, clear table and filter behavior, and keyboard-friendly controls.
- Reduce ornamental effects even if the primary style uses them heavily.

For mobile-first tools:

- Use iOS screen references to understand state shape, compact hierarchy, onboarding, paywall, dashboard, and profile flows.
- Translate mobile patterns carefully when building responsive web.

## Selection Examples

Example: AI coding web tool

- Primary style: `cursor`, `factory`, or `dimension`
- Screens: Dashboard, Developers Page, Log In
- Adaptation: technical surfaces, command palette, code-aware typography, restrained motion

Example: fintech analytics dashboard

- Primary style: `fey`, `glassnode`, `altitude`, or `auros`
- Screens: Dashboard, Profile & Account, Product Details
- Adaptation: numbers first, chart readability, strong contrast, clear risk states

Example: creator marketplace

- Primary style: `awesomic`, `dribbble`, or `cosmos`
- Screens: Catalog Page, Product Details, Profile & Account
- Adaptation: visual cards, search, filters, portfolio previews, trust markers
