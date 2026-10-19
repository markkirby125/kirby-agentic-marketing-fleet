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
3. **Key Page Identification**: Identify up to 4 vital secondary URLs:
   - Pricing URL (`/pricing`, `/rates`, `/packages`)
   - Services/Catalog URL (`/services`, `/treatments`, `/products`)
   - About/Trust URL (`/about`, `/our-team`, `/credentials`)
   - Specials/Promotions URL (`/specials`, `/offers`, `/discounts`)

---

## 1.2 The 5 Subagent Task Contracts

The orchestrator dispatches 5 specialized subagents concurrently via `invoke_subagent`. Each subagent receives an isolated prompt contract:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PARENT ORCHESTRATOR                             │
│                  Dispatches 5 Subagents in Parallel                    │
└────────────────────────────────────────────────────────────────────────┘
          │                 │                │                │
          ▼                 ▼                ▼                ▼
   [market-content]  [market-convers.] [market-compet.] [market-technic.]
   - Value Prop      - Pricing Parity  - Direct Tier    - Schema JSON-LD
   - Clarity         - Friction Points - Indirect Tier  - Meta Tags
   - Anti-Slop Copy  - CTA Visibility  - Aspirational   - Crawl/Speed
          │                 │                │                │
          └─────────────────┴────────┬───────┴────────────────┘
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
* **Objective**: Detect friction in the user journey, checkout abandonment risks, and cross-page pricing conflicts per [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) (§1.5, §1.6, §16, §17) and [`kirby-local-seo`](../../kirby-local-seo/SKILL.md) (Module 8).
* **Checks**:
  - **Cross-Page Pricing Parity**: Execute [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §16 (verify service pages match `/specials` and checkout 1:1).
  - **Form & Pricing Transparency**: Audit against [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §17 (transparent pricing tables vs. gated multi-field forms).
  - **Visual & Journey Friction**: Enforce [`kirby-text-first-cro`](../../kirby-text-first-cro/SKILL.md) §1.5 (hero carousel ban) and §1.6 (4-step linear process bar).
  - **CTA Clarity**: Verify benefit-driven primary CTAs (*"Book Free Consultation"*) vs. passive labels (*"Submit"*).

### Agent 3: `market-competitive` (Competitive Intelligence Analyst)
* **Objective**: Deconstruct the competitive landscape across 3 explicit tiers:
  - **Tier 1 (Direct Competitors)**: Operating in the same geographic radius or market segment with identical offerings.
  - **Tier 2 (Indirect Competitors)**: Alternative solutions satisfying the same core customer desire (e.g. at-home skincare kits vs. med spa clinic).
  - **Tier 3 (Aspirational Competitors)**: National or category-defining leaders setting the user experience benchmark.
* **Matrix Output**: Comparison of pricing visibility, review volume, tech stack, and unique selling propositions (USPs).

### Agent 4: `market-technical` (Technical SEO & Schema Analyst)
* **Objective**: Inspect HTML markup, meta tags, structured data, and search engine discoverability.
* **Checks**:
  - **Meta Description Coverage**: Audit whether all core pages feature unique, click-compelling meta descriptions, or if Google is auto-generating search snippets.
  - **Title Tag Architecture**: Verify that `<title>` tags lead with the primary commercial service entity and city (`[Service] in [City] | [Brand]`).
  - **JSON-LD Schema**: Verify syntax and presence of specific Schema entities (`MedicalBusiness`, `LocalBusiness`, `LegalService`, `OfferCatalog`, `hasMap` CID).

### Agent 5: `market-strategy` (Growth Strategist)
* **Objective**: Synthesize cross-cutting opportunities into a phased 30-60-90 day execution roadmap.
* **Structure**:
  - *Week 1 (Quick Wins)*: Low-effort, high-impact fixes (resolve pricing conflicts, inject meta descriptions, embed live Google reviews).
  - *Months 1–3 (Medium-Term)*: Dedicated service entity pages, pricing transparency tables, Astro static rebuild.
  - *Months 3–6 (Strategic)*: Competitor link gap outreach, PR syndication, automated review drip pipelines.
