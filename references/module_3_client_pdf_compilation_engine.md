# Module 3: Client PDF Compilation Engine

*Source: Zubair Trabzada ("I Built An Entire AI Marketing Team With Claude Code In 16 Minutes")*

Delivering audit findings inside a terminal or raw markdown file signals amateur execution. To justify high-ticket $2,500–$5,000/month retainers, audit results must be compiled into a branded, executive-ready PDF report featuring visual score cards, critical callout banners, and prioritized roadmaps.

This module defines the input telemetry schema and CLI invocation for the canonical compilation script located at [`../bin/generate_audit_pdf.py`](../bin/generate_audit_pdf.py).

---

## 3.1 PDF Generator Architecture

The compiler at `bin/generate_audit_pdf.py` renders native multi-page corporate PDFs via `reportlab` (`SimpleDocTemplate`, `Table`, `ParagraphStyle`) and automatically falls back to a self-contained print-ready HTML deliverable if `reportlab` is absent in the host Python environment.

```
[Raw Subagent JSON Telemetry]
              │
              ▼
   bin/generate_audit_pdf.py
              │
  ┌───────────┴───────────┐
  ▼                       ▼
Cover Page & Scorecard   Key Findings & Roadmaps
  │                       │
  └───────────┬───────────┘
              ▼
   Client-Audit-Report.pdf
```

---

## 3.2 Input Telemetry JSON Contract (`audit.json`)

Aggregate the 5 subagent outputs from [Module 1](module_1_subagent_fleet_orchestration.md) and the weighted score from [Module 2](module_2_audit_scorecard_and_defect_taxonomy.md) into a single JSON file conforming to this schema:

```json
{
  "business_name": "Acme Med Spa",
  "url": "https://acmemedspa.example.com",
  "date": "October 19, 2026",
  "overall_score": 64,
  "grade": "C-",
  "summary": "Audit indicates critical conversion friction ($1,400 vs $1,500 cross-page pricing mismatch) and 100% missing meta descriptions across core service pages.",
  "findings": [
    {
      "severity": "CRITICAL",
      "title": "Cross-Page Package Pricing Conflict",
      "detail": "Service page lists Laser Package at $1,400 while /specials lists the identical package at $1,500.",
      "fix": "Unify pricing source of truth across all pages and checkout links immediately."
    },
    {
      "severity": "HIGH",
      "title": "Zero Custom Meta Descriptions",
      "detail": "All 5 core URLs omit <meta name='description'>, forcing erratic SERP snippets.",
      "fix": "Deploy unique 150-160 char commercial meta descriptions on every service URL."
    }
  ],
  "roadmap": [
    {
      "phase": "Week 1 (Quick Wins)",
      "focus": "Revenue Patch",
      "deliverables": "Fix cross-page checkout pricing conflicts, deploy custom meta descriptions across all URLs, embed live Google review widget."
    },
    {
      "phase": "Month 1-3 (Medium-Term)",
      "focus": "Entity Mirroring",
      "deliverables": "Scaffold dedicated secondary GBP category landing pages, deploy transparent pricing calculators, eliminate navbar link bloat."
    },
    {
      "phase": "Month 3-6 (Strategic)",
      "focus": "Market Monopoly",
      "deliverables": "Execute competitor backlink gap outreach, automated SMS review generation engine, launch local parasite citations."
    }
  ]
}
```

---

## 3.3 CLI Invocation

Run [`bin/generate_audit_pdf.py`](../bin/generate_audit_pdf.py) against the aggregated JSON payload:

```bash
# Compile native PDF (falls back to .html automatically if reportlab is unavailable)
python3 bin/generate_audit_pdf.py audit.json Client-Audit-Report.pdf

# Or compile standalone HTML report directly
python3 bin/generate_audit_pdf.py audit.json Client-Audit-Report.html
```
