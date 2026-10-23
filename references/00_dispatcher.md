# Agentic Marketing Fleet - Dispatcher

Automated agency-scale marketing audit and strategy engine powered by context-isolated, parallel CLI subagents in Claude Code, Gemini CLI, or Antigravity. Codified from Zubair Trabzada's agency fleet architecture (*AI Workshop*).

Traditional digital marketing agencies bill $5,000 to $10,000/month for standard marketing audits, competitive analyses, and technical roadmaps. By deploying an autonomous coding agent CLI configured with modular `skill.md` directives and Python PDF generation, an operator can execute a complete 6-subagent marketing audit and compile an executive-ready client deliverable in under 2 minutes for zero operational cost.

When executing tasks under this skill, **do not guess**. Review the module index below and read the specific module file(s) relevant to the task using your file-reading tools.

---

## 📚 Module Index

- **Module 1: Subagent Fleet Orchestration & Prompt Contracts** — The 6-agent parallel dispatch architecture (`market-content`, `market-conversion`, `market-competitive`, `market-technical`, `market-strategy`, `market-seasonal`), discovery URL ingestion, business model classification, and isolated task contracts.  
  👉 Read `./module_1_subagent_fleet_orchestration.md`

- **Module 2: Audit Scorecard & Defect Severity Taxonomy** — The 0–100 weighted evaluation framework, composite grading, and 4-tier defect classification (`Critical`, `High`, `Medium`, `Low`) with real-world failure patterns and §2.3 Seasonal & Promotional Defect Taxonomy (Ep. 1206 audit rules).  
  👉 Read `./module_2_audit_scorecard_and_defect_taxonomy.md`

- **Module 3: Client PDF Compilation Engine** — Python ReportLab / WeasyPrint script architecture that compiles multi-agent markdown telemetry into a styled, publication-grade executive PDF deck.  
  👉 Read `./module_3_client_pdf_compilation_engine.md`

- **Module 4: Agency Retainer Monetization & Outreach Playbook** — The "Trojan Horse" free diagnostic audit outreach protocol, cold Loom video scripts, and the 3-phase action plan ($2,500–$5,000/mo retainer) converting audit findings into signed recurring contracts.  
  👉 Read `./module_4_agency_retainer_monetization_playbook.md`

---

## 🧭 The 4-Phase Fleet Lifecycle

```
[Phase 1: Discovery & Model Tagging]
       │
       ▼
[Phase 2: Parallel 6-Agent Fleet Dispatch]
 ┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
 │market-content│market-convers│market-compet.│market-technic│market-season.│market-strateg│
 └──────┬───────┴──────┬───────┴──────┬───────┴──────┬───────┴──────┬───────┴──────┬───────┘
        └──────────────┴──────────────┴──────┬───────┴──────────────┴──────────────┘
                                             ▼
                 [Phase 3: Synthesis, Scoring (0-100) & Severity Triaging]
                                             │
                                             ▼
                [Phase 4: Client PDF Generation & 3-Tier Retainer Conversion]
```

1. **Phase 1: Discovery & Pre-Analysis**  
   - Fetch the target root URL and key secondary paths (`/pricing`, `/services`, `/about`, `/specials`).
   - Classify business model: `SaaS`, `E-Commerce`, `Local Service`, `Creator/Course`, or `Enterprise B2B`.
   - Map baseline entity claims, brand name, and operating locations.

2. **Phase 2: Parallel Subagent Fleet Execution**  
   - Dispatch 6 context-isolated subagents simultaneously using native subagent capabilities (`invoke_subagent`).
   - Each subagent operates within strict boundaries, preventing context contamination:
     - **Agent 1 (`market-content`)**: Value propositions, narrative clarity, anti-slop copy audit.
     - **Agent 2 (`market-conversion`)**: Checkout friction, pricing parity across pages, CTA placement.
     - **Agent 3 (`market-competitive`)**: 3-tier competitor decomposition (Direct, Indirect, Aspirational).
     - **Agent 4 (`market-technical`)**: Meta descriptions, title tags, Schema.org JSON-LD, crawl speed.
     - **Agent 5 (`market-strategy`)**: 30-60-90 day growth priorities and quick wins.
     - **Agent 6 (`market-seasonal`)**: Promotional page audit, Discount Transparency Block validation, checkout promo clutter check, GMC price parity, and AI shopping bot access.

3. **Phase 3: Synthesis & Scorecard Compilation**  
   - Ingest outputs from all 6 subagents.
   - Calculate composite 0–100 health score.
   - Categorize all identified defects into `Critical`, `High`, `Medium`, and `Low` severity tiers.

4. **Phase 4: Deliverable Generation & Agency Retainer Pitch**  
   - Execute Python compiler (`bin/generate_audit_pdf.py` or `./module_3_client_pdf_compilation_engine.md`).
   - Deliver executive PDF report to client alongside the 3-stage monetization roadmap.

---

## 🔗 Cross-Skill Routing Invariants

- **On-Page Conversion & Hero Optimization**: For deep remediation of hero sections, removing carousels, and structuring text-first layouts, route to `../../kirby-text-first-cro/SKILL.md`.
- **Local Map Pack & GBP Optimization**: For local businesses requiring Google Business Profile alignment and SAB domination, route to `../../kirby-local-seo/SKILL.md` and `../../kirby-scrappy-local-launch/SKILL.md`.
- **Technical Schema & AEO Entity Engineering**: For deploying JSON-LD schema (`LocalBusiness`, `MedicalBusiness`, `Product`), route to `../../kirby-aiseo-skill/SKILL.md` and `../../kirby-technical-aeo/SKILL.md`.
- **High-Converting Sales Copywriting**: For rewriting landing page copy using the 17-step Direct Response framework, route to `../../kirby-direct-response-copywriting/SKILL.md`.
- **Link Outreach & Parasite Distribution**: For executing competitor backlink gap closure, route to `../../kirby-off-page-seo/SKILL.md` and `../../kirby-saas-syndicate/SKILL.md`.
- **Seasonal Directory & Timing Architecture**: For evergreen promotional directories, January archival handoffs, and late-mover crawl acceleration, route to `../../kirby-seo-deployment/SKILL.md` (Module 7 §7.18) and `../../kirby-seo-timing-benchmarks/SKILL.md` (Reference 05 §5.5).
