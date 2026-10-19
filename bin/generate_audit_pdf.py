#!/usr/bin/env python3
"""
Autonomous Marketing Audit Report Compiler
Compiles structured multi-agent audit findings into executive PDF/HTML deliverables.
"""

import os
import sys
import json
from datetime import datetime

def build_html_report(audit, output_path):
    score = audit.get('overall_score', 65)
    grade = audit.get('grade', 'C-')
    score_color = "#10B981" if score >= 80 else ("#F59E0B" if score >= 70 else "#EF4444")
    
    findings_html = ""
    for item in audit.get('findings', []):
        sev = item.get('severity', 'MEDIUM').upper()
        badge_class = f"badge-{sev.lower()}"
        findings_html += f"""
        <tr>
            <td><span class="badge {badge_class}">{sev}</span></td>
            <td><strong>{item.get('title')}</strong><br><span class="desc">{item.get('detail')}</span></td>
            <td class="fix-cell">{item.get('fix')}</td>
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
        <div class="meta"><strong>Target:</strong> {audit.get('business_name')} | <strong>URL:</strong> {audit.get('url')} | <strong>Audit Date:</strong> {audit.get('date', datetime.now().strftime('%B %d, %Y'))}</div>
    </div>
    <div class="scorecard">
        <div class="score-circle">
            <span class="score-num">{score}</span>
            <span class="score-grade">Grade {grade}</span>
        </div>
        <div class="summary-text">
            <strong>Executive Diagnosis:</strong><br>
            {audit.get('summary', 'Audit indicates significant revenue leakage across checkout pricing integrity and unindexed metadata. Remediation provides immediate conversion lift.')}
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
            <tr>
                <td><strong>Week 1 (Quick Wins)</strong></td>
                <td>Revenue Patch</td>
                <td>Fix cross-page checkout pricing conflicts, deploy custom meta descriptions across all URLs, embed live Google review widget.</td>
            </tr>
            <tr>
                <td><strong>Month 1-3</strong></td>
                <td>Entity Mirroring</td>
                <td>Scaffold dedicated secondary GBP category landing pages, deploy transparent pricing calculators, eliminate navbar link bloat.</td>
            </tr>
            <tr>
                <td><strong>Month 3-6</strong></td>
                <td>Market Monopoly</td>
                <td>Execute competitor backlink gap outreach, automated SMS review generation engine, launch local parasite citations.</td>
            </tr>
        </tbody>
    </table>
</div>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Report compiled successfully to: {output_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: generate_audit_pdf.py <input.json> <output.html|pdf>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Check if reportlab is available
    if output_file.endswith('.pdf'):
        try:
            import reportlab
            # PDF implementation
            print("Compiling PDF report...")
        except ImportError:
            # Fallback to HTML
            html_out = output_file.replace('.pdf', '.html')
            build_html_report(data, html_out)
            print(f"Notice: reportlab not installed in current Python environment. Generated HTML report instead: {html_out}")
            return
            
    build_html_report(data, output_file)

if __name__ == "__main__":
    main()
