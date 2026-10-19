# Module 2: Audit Scorecard & Defect Severity Taxonomy

*Source: Zubair Trabzada ("I Built An Entire AI Marketing Team With Claude Code In 16 Minutes")*

To prevent subjective, hand-waving client reports, the Agentic Marketing Fleet enforces a strict, mathematical scorecard and severity taxonomy. Every client audit must output clear, evidence-based grades that justify high-ticket retainer engagements.

---

## 2.1 The 0–100 Weighted Scorecard Algorithm

The overall audit score is calculated across the 5 core diagnostic dimensions, weighted by business impact:

$$\text{Overall Score} = (C \times 0.25) + (V \times 0.25) + (T \times 0.20) + (K \times 0.15) + (S \times 0.15)$$

Where:
* $C$ = **Conversion & Funnel Optimization** (25% weight)
* $V$ = **Content, Messaging & Value Proposition** (25% weight)
* $T$ = **Technical SEO & Schema Infrastructure** (20% weight)
* $K$ = **Competitive Differentiation & Positioning** (15% weight)
* $S$ = **Growth Strategy & Retention Loops** (15% weight)

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
