# Module 1: Subagent Fleet Orchestration & Prompt Contracts

*Source: Zubair Trabzada ("I Built An Entire AI Marketing Team With Claude Code In 16 Minutes")*

To prevent context window bloat and reasoning degradation, marketing audits must **never** be executed within a single monolithic agent prompt. Monolithic evaluation leads to shallow superficial observations, hallucinated technical metrics, and skipped pages.

This module establishes the deterministic multi-agent harness protocol: executing discovery, isolating subagent contexts, and enforcing structured JSON return contracts.

---

## 1.1 Discovery & Business Model Classification

Before dispatching the subagent fleet, the parent orchestrator executes discovery steps:
1. **Fetch Target URL**: Ingest raw HTML and headers of the homepage.
2. **Business Classification**: Classify the domain into one of five operational categories:
   - `LOCAL_SERVICE`: Med Spas, Roofers, Plumbers, Dentists, Lawyers. (Focus: GBP, NAP, local trust, localized pricing).
   - `SAAS`: Software-as-a-Service, developer tools. (Focus: Feature matrices, time-to-value, self-serve funnels).
   - `ECOMMERCE`: Physical goods, retail brands. (Focus: Catalog taxonomy, cart abandonment, social proof).
   - `CREATOR_COURSE`: Digital products, newsletters, coaching. (Focus: Personal authority, VSLs, lead magnets).
   - `B2B_ENTERPRISE`: High-ticket consulting, enterprise solutions. (Focus: RFP compliance, procurement disclosures).
3. **Key Page Identification**: Identify vital secondary and AI-discovery URLs:
   - Pricing URL (`/pricing`, `/rates`, `/packages`)
   - Services/Catalog URL (`/services`, `/treatments`, `/products`)
   - About/Trust URL (`/about`, `/our-team`, `/credentials`)
   - Specials/Promotions URL (`/specials`, `/offers`, `/discounts`)
   - AI Self-Corroboration & SSOT Facts URLs (`/trust` Self-Corroboration Hub and `/facts` or `/about#facts` SSOT `"My Business Facts"` page; [`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 2 §2.38, §2.51)

---

## 1.2 The 6 Subagent Task Contracts

The orchestrator dispatches 6 specialized subagents concurrently via `invoke_subagent`. Each subagent receives an isolated prompt contract:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PARENT ORCHESTRATOR                             │
│                  Dispatches 6 Subagents in Parallel                    │
└────────────────────────────────────────────────────────────────────────┘
      │              │              │              │              │
      ▼              ▼              ▼              ▼              ▼
[market-cont.] [market-conv.] [market-comp.] [market-tech.] [market-seas.]
- Value Prop   - Price Parity - Direct Tier  - Schema LD    - Promo Parity
- Clarity      - Friction     - Indirect     - Meta Tags    - Discount Blk
- Anti-Slop    - CTA Visib.   - Aspirational - Crawl/Speed  - AI Bot Access
      │              │              │              │              │
      └──────────────┴──────────────┼──────────────┴──────────────┘
                                    ▼
                            [market-strategy]
                            - Quick Wins (W1)
                            - Medium-Term (M1-3)
                            - Strategic (M3-6)
```

### Agent 1: `market-content` (Content & Messaging Analyst)
* **Objective**: Evaluate brand messaging, above-the-fold value propositions, and clarity of customer communication.
* **Checks**:
  - Does the hero heading communicate what the business does in under 3 seconds?
  - Does the copy focus on customer outcomes or self-centered platitudes (*"We pride ourselves on excellence"*)?
  - Are proof assets (awards, customer counts, case studies) prominently displayed?
* **Return Schema**:
  ```json
  {
    "domain": "content_messaging",
    "score": 0-100,
    "findings": [{"severity": "CRITICAL|HIGH|MEDIUM|LOW", "issue": "...", "fix": "..."}]
  }
  ```

### Agent 2: `market-conversion` (Conversion Rate Optimization Analyst)
* **Objective**: Detect friction in the user journey, checkout abandonment risks, and cross-page pricing conflicts per [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) (§1.5, §1.6, §1.9, §16, §17) and [`kirby-local-seo`](../../kirby-local-seo/SKILL.md) (Module 8).
* **Checks**:
  - **Cross-Page Pricing Parity**: Execute [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §16 (verify service pages match `/specials` and checkout 1:1).
  - **Form & Pricing Transparency**: Audit against [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §17 (transparent pricing tables vs. gated multi-field forms).
  - **Visual & Journey Friction**: Enforce [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §1.5 (hero carousel ban) and §1.6 (4-step linear process bar).
  - **Above-the-Fold Viewport-Match / Visual Semantics Check**: Verify that primary conversion and trust actuators — booking/quote CTA, interactive calculator, clickable `tel:`, price floor, and verified review proof — are visible immediately in the first viewport without scrolling ([`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §1.9).
  - **CTA Clarity**: Verify benefit-driven primary CTAs (*"Book Free Consultation"*) vs. passive labels (*"Submit"*).

### Agent 3: `market-competitive` (Competitive Intelligence Analyst)
* **Objective**: Deconstruct the competitive landscape across 3 explicit tiers:
  - **Tier 1 (Direct Competitors)**: Operating in the same geographic radius or market segment with identical offerings.
  - **Tier 2 (Indirect Competitors)**: Alternative solutions satisfying the same core customer desire (e.g. at-home skincare kits vs. med spa clinic).
  - **Tier 3 (Aspirational Competitors)**: National or category-defining leaders setting the user experience benchmark.
* **Matrix Output**: Comparison of pricing visibility, trailing 90-day review velocity & recency (vs. top-3 Map Pack competitors; [`kirby-local-seo`](../../kirby-local-seo/SKILL.md) Module 3), tech stack, and unique selling propositions (USPs).
* **Core-Update Outlier Forensics (during an active rollout only):** Do not recommend structural changes to the client site mid-rollout. Run the Ahrefs outlier workflow and its tracker-desync/single-variable caveats in [`kirby-seo-telemetry`](../../kirby-seo-telemetry/SKILL.md) Module 16 §16.3–16.4 and report as Tier 3 hypotheses.
* **Footprint Check (Logo-Swap Litmus):** Flag a client or competitor site that is a theme-kit clone of other sites (`../../kirby-seo-deployment/SKILL.md` Module 7 §7.3).
* **Bare `[Brand Name]` Page-1 SERP Slot Ownership & Homonym Disambiguation Audit:** Check how many of the 10 Page-1 organic slots for the bare `[Brand Name]` query (no category/city modifier) the business controls (root domain, GBP, official socials, verified directories). Keep diagnostics separate: lost Page-1 slots signal **homonym collisions** or **stale/unclaimed directory profiles**, whereas real branded demand is measured solely via GSC branded query volume (Agent 4).

### Agent 4: `market-technical` (Technical SEO & Schema Analyst)
* **Objective**: Inspect HTML markup, meta tags, structured data, and search engine discoverability.
* **Checks**:
  - **Meta Description Coverage**: Audit whether all core pages feature unique, click-compelling meta descriptions, or if Google is auto-generating search snippets.
  - **Title Tag Architecture**: Verify that `<title>` tags lead with the primary commercial service entity and city (`[Service] in [City] | [Brand]`).
  - **JSON-LD Schema & Review Schema Ban**: Verify syntax and presence of specific Schema entities (`MedicalBusiness`, `LocalBusiness`, `LegalService`, `OfferCatalog`, `hasMap` CID), and flag any `AggregateRating` or `Review` JSON-LD on `/trust`, `/facts`, or pages summarizing aggregated third-party reviews as a defect (strict ban — plain-text HTML + outbound links only per [`kirby-technical-aeo`](../../kirby-technical-aeo/SKILL.md) Phase 4 and [`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 2 §2.38).
  - **Branded Search vs. Backlink Ratio (Navneet Panda Reference Queries)**: Compare 90-day GSC branded impressions/clicks against referring-domain count (or mark `[Pending Connection]`); flag high referring domains paired with near-zero GSC branded search volume as a core-update vulnerability (directional, single-source — Tier 3 hypothesis; [`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 1 §1.11.1), distinct from Agent 3's bare-brand homonym/SERP-slot check.
  - **AI Trust & SSOT Discovery Surfaces**: Verify `/trust` (Self-Corroboration Hub) and `/facts` or `/about#facts` (SSOT `"My Business Facts"`) resolve `200 OK` without `noindex` or AI-crawler blocks ([`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 2 §2.38, §2.51).

### Agent 5: `market-strategy` (Growth Strategist)
* **Objective**: Synthesize cross-cutting opportunities into a phased 30-60-90 day execution roadmap.
* **Structure**:
  - *Week 1 (Quick Wins)*: Low-effort, high-impact fixes (resolve pricing conflicts, inject meta descriptions, embed live Google reviews).
  - *Months 1–3 (Medium-Term)*: Dedicated service entity pages, pricing transparency tables, Astro static rebuild, `/trust` & SSOT `/facts` deployment.
  - *Mid-rollout (Nov 10–~Dec 1, 2026):* roadmap items stay queued per [`kirby-seo-telemetry`](../../kirby-seo-telemetry/SKILL.md) Module 16 §16.2; run the pre-publication semantic drift gate in [`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 20 (via [`kirby-grounded-seo-auditor`](../../kirby-grounded-seo-auditor/SKILL.md) Module 04 §2) before any content batch.
  - *Months 3–6 (Strategic & AI Visibility Lag Calibration)*: Competitor link gap outreach, PR syndication, automated trailing 90-day review velocity pipelines, and **`3–5×` multi-run + multi-turn fan-out probing** tracking **Synthesis Recommendation Share** + conversions across engine lag windows — **Google AI Overviews / Gemini (`2–4 weeks`)** vs. **ChatGPT Search / Thinking (`60–120 days`)** ([`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) Module 2 §2.16.1B, §2.28B; [`kirby-seo-timing-benchmarks`](../../kirby-seo-timing-benchmarks/SKILL.md) Reference 04 §4.8).

### Agent 6: `market-seasonal` (Seasonal & Promotion Readiness Auditor)
*Source: Edward Sturm Ep. 1206 (David Quaid, Harpreet Singh, Gagan Ghotra).*
* **Objective**: Audit promotional landing pages, seasonal campaign readiness, price parity, and AI shopping engine accessibility during peak promotional cycles.
* **Checks**:
  - **Discount Transparency Block**: Verify that promotional landing pages feature an unambiguous, high-contrast Discount Transparency Block with dual strikethrough pricing, explicit net dollar and percentage savings, and auto-apply deep-link query parameters (`?promo=BF2026`) matching [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §1.7.
  - **Checkout Promo Box Clutter**: Verify that coupon input fields on checkout carts are collapsed by default behind an understated text link to prevent coupon excursion bounces ([`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §16.1).
  - **Multi-Surface Pricing Parity**: Verify that advertised discount rates match Google Merchant Center feeds, GBP Product cards ([`kirby-local-seo`](../../kirby-local-seo/SKILL.md) Module 6 §6.14), and final checkout cart totals with 1:1 numerical precision.
  - **AI Shopping & Search-Grounding Bot Access**: Audit `robots.txt` and edge WAF rules to verify that AI search and commercial shopping bots (`Google-Extended`, `OAI-SearchBot`, `PerplexityBot`, `GPTBot`) are permitted to crawl promotional catalogs, `/trust`, and `/facts` ([`kirby-aiseo-skill`](../../kirby-aiseo-skill/SKILL.md) §1.22).
  - **Late-Mover Crawl Acceleration**: Verify that temporary promotional links are injected into the global navigation header and homepage Viewport 1 above the fold ([`kirby-seo-timing-benchmarks`](../../kirby-seo-timing-benchmarks/SKILL.md) Reference 05 §5.5), and that URLs reside in evergreen directories without calendar years in live slugs ([`kirby-seo-deployment`](../../kirby-seo-deployment/SKILL.md) Module 7 §7.18).
