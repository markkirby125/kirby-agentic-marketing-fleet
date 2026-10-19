# Module 3: Client PDF Compilation Engine

*Source: Zubair Trabzada ("I Built An Entire AI Marketing Team With Claude Code In 16 Minutes")*

Delivering audit findings inside a terminal or raw markdown file signals amateur execution. To justify high-ticket $2,500–$5,000/month retainers, audit results must be compiled into a branded, executive-ready PDF report featuring visual score cards, critical callout banners, and prioritized roadmaps.

This module provides the deterministic Python compilation script that transforms raw fleet findings into publication-grade client deliverables.

---

## 3.1 PDF Generator Architecture

The compiler is located at `bin/generate_audit_pdf.py` and runs natively in Python using `reportlab`.

```
[Raw Subagent JSON Telemetry]
              │
              ▼
   generate_audit_pdf.py
              │
  ┌───────────┴───────────┐
  ▼                       ▼
Cover Page & Scorecard   Key Findings & Roadmaps
  │                       │
  └───────────┬───────────┘
              ▼
   Client-Audit-Report.pdf
```

### Script Implementation (`bin/generate_audit_pdf.py`):

```python
#!/usr/bin/env python3
"""
Autonomous Marketing Audit PDF Report Compiler
Compiles structured multi-agent audit findings into executive PDF deliverables.
"""

import os
import sys
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def build_pdf_report(data_json_path, output_pdf_path):
    with open(data_json_path, 'r', encoding='utf-8') as f:
        audit = json.load(f)

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = getSampleStyleSheet()
    
    # Custom Corporate Typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0F172A')
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # 1. Header Banner
    story.append(Paragraph(f"MARKETING & GROWTH AUDIT REPORT", title_style))
    story.append(Paragraph(f"Target: <b>{audit.get('business_name', 'Client')}</b> | URL: {audit.get('url')} | Date: {audit.get('date')}", body_style))
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563EB'), spaceAfter=15))

    # 2. Executive Scorecard Box
    score = audit.get('overall_score', 65)
    grade = audit.get('grade', 'C-')
    
    score_data = [
        [
            Paragraph(f"<font size=12><b>OVERALL SCORE</b></font><br/><font size=32><b>{score}/100</b></font><br/><b>Grade: {grade}</b>", body_style),
            Paragraph(f"<b>Executive Summary:</b><br/>{audit.get('summary', 'Audit indicates critical conversion friction and technical SEO gaps that directly depress customer acquisition.')}", body_style)
        ]
    ]
    score_table = Table(score_data, colWidths=[2.2*inch, 5.3*inch])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 15))

    # 3. Critical Findings Section
    story.append(Paragraph("Key Findings & Critical Vulnerabilities", h2_style))
    
    findings_data = [["Severity", "Finding Description", "Recommended Immediate Action"]]
    for item in audit.get('findings', []):
        sev = item.get('severity', 'MEDIUM')
        sev_color = '#DC2626' if sev == 'CRITICAL' else ('#EA580C' if sev == 'HIGH' else '#2563EB')
        findings_data.append([
            Paragraph(f"<font color='{sev_color}'><b>{sev}</b></font>", body_style),
            Paragraph(f"<b>{item.get('title')}</b><br/>{item.get('detail')}", body_style),
            Paragraph(f"{item.get('fix')}", body_style)
        ])

    findings_table = Table(findings_data, colWidths=[1.1*inch, 3.4*inch, 3.0*inch])
    findings_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(findings_table)
    story.append(Spacer(1, 15))

    # 4. Phased Roadmap Section
    story.append(Paragraph("Prioritized Implementation Roadmap", h2_style))
    roadmap_data = [
        ["Phase", "Focus", "High-Impact Deliverables"],
        ["Week 1 (Quick Wins)", "Revenue Patch", "Fix checkout pricing inconsistencies, deploy missing meta descriptions, embed live GBP widget."],
        ["Month 1-3 (Medium-Term)", "Entity Authority", "Scaffold dedicated secondary service pages, install transparent pricing calculator, eliminate navbar link bloat."],
        ["Month 3-6 (Strategic)", "Market Domination", "Execute competitor link gap acquisition, automate SMS review drip engine, launch local parasite syndication."]
    ]
    roadmap_table = Table(roadmap_data, colWidths=[1.6*inch, 1.8*inch, 4.1*inch])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(roadmap_table)

    doc.build(story)
    print(f"Audit PDF successfully compiled: {output_pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: generate_audit_pdf.py <input_data.json> <output_report.pdf>")
        sys.exit(1)
    build_pdf_report(sys.argv[1], sys.argv[2])
```
