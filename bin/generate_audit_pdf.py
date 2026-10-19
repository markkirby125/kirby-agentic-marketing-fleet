#!/usr/bin/env python3
"""
Autonomous Marketing Audit Report Compiler
Compiles structured multi-agent audit findings into executive PDF or HTML deliverables.
"""

import json
import sys
from datetime import datetime

DEFAULT_SUMMARY = (
    "Audit indicates significant revenue leakage across checkout pricing integrity "
    "and unindexed metadata. Remediation provides immediate conversion lift."
)

DEFAULT_ROADMAP = [
    {
        "phase": "Week 1 (Quick Wins)",
        "focus": "Revenue Patch",
        "deliverables": (
            "Fix cross-page checkout pricing conflicts, deploy custom meta descriptions "
            "across all URLs, embed live Google review widget."
        ),
    },
    {
        "phase": "Month 1-3 (Medium-Term)",
        "focus": "Entity Mirroring",
        "deliverables": (
            "Scaffold dedicated secondary GBP category landing pages, deploy transparent "
            "pricing calculators, eliminate navbar link bloat."
        ),
    },
    {
        "phase": "Month 3-6 (Strategic)",
        "focus": "Market Monopoly",
        "deliverables": (
            "Execute competitor backlink gap outreach, automated SMS review generation "
            "engine, launch local parasite citations."
        ),
    },
]


def get_roadmap(audit):
    return audit.get("roadmap") or DEFAULT_ROADMAP


def get_score_meta(audit):
    score = int(audit.get("overall_score", 65))
    grade = audit.get("grade", "C-")
    color = "#10B981" if score >= 80 else ("#F59E0B" if score >= 70 else "#EF4444")
    date_str = audit.get("date") or datetime.now().strftime("%B %d, %Y")
    summary = audit.get("summary") or DEFAULT_SUMMARY
    return score, grade, color, date_str, summary


def build_pdf_report(audit, output_path):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        HRFlowable,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )

    score, grade, _, date_str, summary = get_score_meta(audit)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.5 * inch,
        leftMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0F172A"),
    )
    h2_style = ParagraphStyle(
        "H2",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=12,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155"),
    )

    story = [
        Paragraph("EXECUTIVE MARKETING & GROWTH AUDIT", title_style),
        Paragraph(
            f"Target: <b>{audit.get('business_name', 'Client')}</b> | "
            f"URL: {audit.get('url', 'N/A')} | Date: {date_str}",
            body_style,
        ),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2563EB"), spaceAfter=14),
    ]

    score_data = [
        [
            Paragraph(
                f"<font size=11><b>OVERALL SCORE</b></font><br/>"
                f"<font size=28><b>{score}/100</b></font><br/><b>Grade: {grade}</b>",
                body_style,
            ),
            Paragraph(f"<b>Executive Diagnosis:</b><br/>{summary}", body_style),
        ]
    ]
    score_table = Table(score_data, colWidths=[2.2 * inch, 5.3 * inch])
    score_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
                ("PADDING", (0, 0), (-1, -1), 12),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.extend([score_table, Spacer(1, 14)])

    story.append(Paragraph("Critical Findings & Vulnerabilities", h2_style))
    findings_data = [["Severity", "Finding Description", "Required Action Plan"]]
    for item in audit.get("findings", []):
        sev = item.get("severity", "MEDIUM").upper()
        sev_color = "#DC2626" if sev == "CRITICAL" else ("#EA580C" if sev == "HIGH" else "#2563EB")
        findings_data.append(
            [
                Paragraph(f"<font color='{sev_color}'><b>{sev}</b></font>", body_style),
                Paragraph(f"<b>{item.get('title', '')}</b><br/>{item.get('detail', '')}", body_style),
                Paragraph(f"{item.get('fix', '')}", body_style),
            ]
        )

    findings_table = Table(findings_data, colWidths=[1.1 * inch, 3.4 * inch, 3.0 * inch])
    findings_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E293B")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("PADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.extend([findings_table, Spacer(1, 14)])

    story.append(Paragraph("Phased Retainer Roadmap", h2_style))
    roadmap_data = [["Phase", "Focus", "Deliverables"]]
    for row in get_roadmap(audit):
        roadmap_data.append(
            [
                Paragraph(f"<b>{row.get('phase', '')}</b>", body_style),
                Paragraph(f"{row.get('focus', '')}", body_style),
                Paragraph(f"{row.get('deliverables', '')}", body_style),
            ]
        )
    roadmap_table = Table(roadmap_data, colWidths=[1.6 * inch, 1.8 * inch, 4.1 * inch])
    roadmap_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("PADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(roadmap_table)

    doc.build(story)
    print(f"Audit PDF report compiled successfully to: {output_path}")


def build_html_report(audit, output_path):
    score, grade, score_color, date_str, summary = get_score_meta(audit)

    findings_html = ""
    for item in audit.get("findings", []):
        sev = item.get("severity", "MEDIUM").upper()
        badge_class = f"badge-{sev.lower()}"
        findings_html += f"""
        <tr>
            <td><span class="badge {badge_class}">{sev}</span></td>
            <td><strong>{item.get('title', '')}</strong><br><span class="desc">{item.get('detail', '')}</span></td>
            <td class="fix-cell">{item.get('fix', '')}</td>
        </tr>
        """

    roadmap_html = ""
    for row in get_roadmap(audit):
        roadmap_html += f"""
        <tr>
            <td><strong>{row.get('phase', '')}</strong></td>
            <td>{row.get('focus', '')}</td>
            <td>{row.get('deliverables', '')}</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Marketing Audit - {audit.get('business_name', 'Client')}</title>
<style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #1e293b; background: #f8fafc; margin: 0; padding: 40px; }}
    .container {{ max-width: 900px; margin: 0 auto; background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
    .header {{ border-bottom: 2px solid #2563eb; padding-bottom: 20px; margin-bottom: 30px; }}
    h1 {{ margin: 0 0 10px 0; font-size: 26px; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px; }}
    .meta {{ font-size: 14px; color: #64748b; }}
    .scorecard {{ display: flex; align-items: center; background: #f1f5f9; border-radius: 8px; padding: 24px; margin-bottom: 30px; }}
    .score-circle {{ width: 110px; height: 110px; border-radius: 50%; background: {score_color}; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: bold; margin-right: 30px; flex-shrink: 0; }}
    .score-num {{ font-size: 32px; line-height: 1; }}
    .score-grade {{ font-size: 14px; margin-top: 4px; }}
    .summary-text {{ font-size: 15px; line-height: 1.6; color: #334155; }}
    h2 {{ font-size: 18px; color: #0f172a; margin-top: 30px; margin-bottom: 15px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; }}
    table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
    th, td {{ padding: 12px 14px; text-align: left; font-size: 13px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }}
    th {{ background: #0f172a; color: white; font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.5px; }}
    .desc {{ color: #475569; font-size: 12px; display: inline-block; margin-top: 4px; }}
    .badge {{ display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; text-transform: uppercase; }}
    .badge-critical {{ background: #fee2e2; color: #991b1b; }}
    .badge-high {{ background: #ffedd5; color: #9a3412; }}
    .badge-medium {{ background: #dbeafe; color: #1e40af; }}
    .badge-low {{ background: #f1f5f9; color: #475569; }}
    .fix-cell {{ color: #0f766e; font-weight: 500; }}
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>Executive Marketing & Growth Audit</h1>
        <div class="meta"><strong>Target:</strong> {audit.get('business_name', 'Client')} | <strong>URL:</strong> {audit.get('url', 'N/A')} | <strong>Audit Date:</strong> {date_str}</div>
    </div>
    <div class="scorecard">
        <div class="score-circle">
            <span class="score-num">{score}</span>
            <span class="score-grade">Grade {grade}</span>
        </div>
        <div class="summary-text">
            <strong>Executive Diagnosis:</strong><br>
            {summary}
        </div>
    </div>
    <h2>Critical Findings & Vulnerabilities</h2>
    <table>
        <thead>
            <tr>
                <th style="width: 15%;">Severity</th>
                <th style="width: 50%;">Finding Description</th>
                <th style="width: 35%;">Required Action Plan</th>
            </tr>
        </thead>
        <tbody>
            {findings_html}
        </tbody>
    </table>
    <h2>Phased Retainer Roadmap</h2>
    <table>
        <thead>
            <tr>
                <th style="width: 25%;">Phase</th>
                <th style="width: 25%;">Focus</th>
                <th style="width: 50%;">Deliverables</th>
            </tr>
        </thead>
        <tbody>
            {roadmap_html}
        </tbody>
    </table>
</div>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Audit HTML report compiled successfully to: {output_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage: generate_audit_pdf.py <input.json> <output.pdf|output.html>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if output_file.endswith(".pdf"):
        try:
            import reportlab  # noqa: F401
        except ImportError:
            html_out = output_file[:-4] + ".html"
            build_html_report(data, html_out)
            print(
                f"Notice: reportlab not installed in current Python environment. "
                f"Generated HTML deliverable instead: {html_out}"
            )
            return
        build_pdf_report(data, output_file)
        return

    build_html_report(data, output_file)


if __name__ == "__main__":
    main()
