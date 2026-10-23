# Module 2: Audit Scorecard & Defect Severity Taxonomy

*Source: Zubair Trabzada ("I Built An Entire AI Marketing Team With Claude Code In 16 Minutes")*

To prevent subjective, hand-waving client reports, the Agentic Marketing Fleet enforces a strict, mathematical scorecard and severity taxonomy. Every client audit must output clear, evidence-based grades that justify high-ticket retainer engagements.

---

## 2.1 The 0–100 Weighted Scorecard Algorithm

The overall audit score is calculated across the 5 core diagnostic dimensions, weighted by business impact:

$$\text{Overall Score} = (C \times 0.25) + (V \times 0.25) + (T \times 0.20) + (K \times 0.15) + (S \times 0.15)$$

Where:
* $C$ = **Conversion & Funnel Optimization** (25% weight) — evaluated by Agent 2 (`market-conversion`) and cross-audited by Agent 6 (`market-seasonal`) for promotional conversion friction (`MISSING_DISCOUNT_TRANSPARENCY_BLOCK`, `UNCOLLAPSED_CHECKOUT_PROMO_BOX`, and `PROMO_PRICE_PARITY_MISMATCH`).
* $V$ = **Content, Messaging & Value Proposition** (25% weight) — evaluated by Agent 1 (`market-content`).
* $T$ = **Technical SEO & Schema Infrastructure** (20% weight) — evaluated by Agent 4 (`market-technical`) and cross-audited by Agent 6 (`market-seasonal`) for promotional crawl/indexability defects (`AI_SHOPPING_BOT_ROBOTS_BLOCK`, `YEAR_IN_SLUG_PROMO_CANNIBALIZATION`, `MISSING_LATE_MOVER_ACCELERATION`).
* $K$ = **Competitive Differentiation & Positioning** (15% weight) — evaluated by Agent 3 (`market-competitive`) and local merchant catalog parity ([kirby-local-seo](../../kirby-local-seo/SKILL.md)).
* $S$ = **Growth Strategy & Retention Loops** (15% weight) — evaluated by Agent 5 (`market-strategy`) and post-holiday retargeting loops ([kirby-paid-acquisition](../../kirby-paid-acquisition/SKILL.md)).

> [!NOTE]
> **Subagent Synthesis Invariant & Point Decrement Protocol**:
> 1. **Cross-Cutting Telemetry**: Agent 6 (`market-seasonal`) functions as a cross-cutting promotional specialist. Rather than inflating the dimensional denominator, Agent 6 defects directly decrement the corresponding primary dimensional score (baseline 100 points per dimension) using deterministic point penalties:
>    - **CRITICAL Defect**: −15 points
>    - **HIGH Defect**: −8 points
>    - **MEDIUM Defect**: −4 points
>    - **LOW Defect**: −1 point
> 2. **Deduplication Invariant**: Agent 2 (`market-conversion`) owns evergreen page-to-page pricing parity; Agent 6 (`market-seasonal`) owns multi-surface promotional parity (GMC feeds, GBP products, deep-link params). When both subagents detect pricing discrepancies, findings deduplicate on `PROMO_PRICE_PARITY_MISMATCH` before scoring to prevent double deductions against $C$.

### Grading Scale:
* **90–100 (Grade A)**: Category Leader. Highly optimized, frictionless conversion flow, robust schema.
* **80–89 (Grade B)**: Strong Competitor. Minor copy or technical gaps; solid fundamentals.
* **70–79 (Grade C+)**: Average Business. Leaking conversions; missing key structured data; average review engine.
* **60–69 (Grade C-)**: High-Risk Profile. Critical pricing conflicts, zero meta descriptions, high form friction. (Typical prime candidate for $3k–$5k/mo agency retainer).
* **< 60 (Grade D/F)**: Emergency State. Unresponsive, broken mobile UX, broken tracking, algorithmic penalties.

---

## 2.2 The 4-Tier Defect Severity Taxonomy

Findings returned by subagents must be sorted and highlighted using strict severity thresholds:

### Tier 1: CRITICAL Severity (Immediate Revenue Leak)
*Directly prevents sales, confuses buyers during purchase intent, or destroys search indexation.*
* **Examples**:
  - **Pricing Discrepancies**: The service landing page lists a treatment package at $1,400 (Save $400), while the specials/promotions page lists the exact same package at $1,500 (Save $300).
  - **Zero Meta Descriptions**: 100% of pages lack custom meta description tags, leaving Google to auto-generate erratic snippets and destroying SERP click-through rates.
  - **Broken Booking/Checkout**: Phone click-to-call link is dead, or contact form returns submission errors.
  - **Sitewide Noindex**: Production domain inadvertently ships `<meta name="robots" content="noindex">`.

### Tier 2: HIGH Severity (Significant Competitive Disadvantage)
*Suppresses organic visibility or introduces severe friction in the prospect evaluation process.*
* **Examples**:
  - **Zero Schema.org Markup**: Complete absence of `LocalBusiness`, `MedicalBusiness`, or `Service` JSON-LD structured data.
  - **Gated Pricing Barrier**: Hiding all service pricing behind an intrusive 5-field contact form with mandatory comment boxes.
  - **Rotating Hero Carousel**: Multi-slide image slider in the hero viewport, increasing page cognitive load and bounce rates.
  - **Closed Hours Suppression**: Business listed as "Closed" in the evening, causing Google to dynamically filter it out of local map results.

### Tier 3: MEDIUM Severity (Missed Growth Opportunities)
*Depresses conversion velocity or limits geographic reach.*
* **Examples**:
  - **Static Copy-Pasted Reviews**: Using plain text quotes instead of an embedded, verifiable Google Business Profile review widget.
  - **Generic Corporate Copy**: Leading with supplier brands or corporate slogans (*"We pride ourselves on customer satisfaction"*) rather than unique local selling propositions.
  - **Navbar Link Bloat**: 50+ navigation links dividing and diluting internal PageRank equity.

### Tier 4: LOW Severity (Cosmetic & Polish)
*Minor polish items that elevate brand perception.*
* **Examples**:
  - Outdated seasonal CTAs (e.g. promoting "July Specials" in October).
  - Unbranded business email (e.g. using `@yahoo.com` or `@gmail.com` instead of `@company.com`).
  - Missing OpenGraph social preview images.

---

## 2.3 Seasonal & Promotional Defect Taxonomy (Ep. 1206 Audit Rules)

*Source: Edward Sturm Ep. 1206 (David Quaid, Harpreet Singh, Gagan Ghotra).*

When auditing e-commerce, local businesses, or SaaS brands running promotional campaigns or preparing for Q4 events, subagents must classify seasonal defects using dedicated diagnostic codes:

| Defect Code | Severity | Root Cause & Failure Mechanism | Corrective Protocol |
|---|---|---|---|
| `MISSING_DISCOUNT_TRANSPARENCY_BLOCK` | **CRITICAL** | Promotional page uses vague copy (*"Up to 50% Off Select Items"*) lacking explicit strikethrough MSRP and net savings. Drives up to 68% coupon-hunting bounces. | Deploy text-dominant Discount Transparency Block per `../../kirby-text-first-cro/SKILL.md` §1.7. |
| `UNCOLLAPSED_CHECKOUT_PROMO_BOX` | **CRITICAL** | Exposed, un-collapsed coupon code field on final checkout screen triggers 18–25% cart abandonment excursion to coupon aggregators. | Collapse coupon field behind understated text link per `../../kirby-text-first-cro/SKILL.md` §16.1. |
| `PROMO_PRICE_PARITY_MISMATCH` | **CRITICAL** | Promotional rates conflict between landing pages, Google Merchant Center feeds, GBP product cards, and checkout cart totals. | Enforce 1:1 numerical price parity per `../../kirby-text-first-cro/SKILL.md` §16 and `../../kirby-local-seo/SKILL.md` Module 6 §6.14. |
| `AI_SHOPPING_BOT_ROBOTS_BLOCK` | **HIGH** | `robots.txt` blocks commercial AI crawlers (`Google-Extended`, `PerplexityBot`, `GPTBot`) from indexing promotional catalog directories. | Update robots.txt bot governance permissions per `../../kirby-aiseo-skill/SKILL.md` §1.22. |
| `YEAR_IN_SLUG_PROMO_CANNIBALIZATION` | **HIGH** | New seasonal landing pages deploy year-modified slugs (e.g., `/deals/black-friday-2026/` instead of evergreen `/deals/black-friday/`), cannibalizing evergreen hub authority. | Re-architect into year-less evergreen directories with January archival snapshots per `../../kirby-seo-deployment/SKILL.md` Module 7 §7.18. |
| `MISSING_LATE_MOVER_ACCELERATION` | **MEDIUM** | Time-sensitive promotional pages launched without global header navigation links or homepage Viewport 1 anchors, suffering 20h+ crawl delays. | Deploy 4-step Late-Mover Crawl Acceleration protocol per `../../kirby-seo-timing-benchmarks/SKILL.md` Reference 05 §5.5. |
