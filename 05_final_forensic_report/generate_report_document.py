#!/usr/bin/env python3
"""
Forensic Report Document Compiler (PDF & DOCX Generator)
Case: Case Omega - Cyber Crime Investigation
Investigator: Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML)
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(REPORT_DIR, "Case_Omega_Forensic_Report.pdf")
DOCX_PATH = os.path.join(REPORT_DIR, "Case_Omega_Forensic_Report.docx")
TOPOLOGY_IMG = os.path.abspath(os.path.join(REPORT_DIR, "..", "01_first_responder_documentation", "scene_sketch_topology.png"))
TIMELINE_IMG = os.path.abspath(os.path.join(REPORT_DIR, "..", "04_timeline_and_correlation", "attack_timeline_chart.png"))

def build_docx():
    print("[*] Generating Word DOCX Report...")
    doc = Document()

    # Document Title Header
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run("DIGITAL FORENSIC INVESTIGATION REPORT\nCASE OMEGA: RANSOMWARE ATTACK ON HEALTHCARE NETWORK")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(16, 44, 87)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Law Enforcement & Judicial Admissibility Edition (Strictly Confidential)\n")
    run_sub.font.size = Pt(12)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(80, 80, 80)

    # Authorship Box
    table_author = doc.add_table(rows=5, cols=2)
    table_author.alignment = WD_TABLE_ALIGNMENT.CENTER
    author_info = [
        ("Lead Digital Forensic Examiner:", "Swaraj Bhattacharjee"),
        ("Student Roll Number:", "2301730011"),
        ("Academic Program:", "B.Tech Computer Science & Engineering (AI & ML)"),
        ("Section / Semester:", "Section A / Semester 7"),
        ("Investigation Date & Ref:", "17 November 2026 | DFIR-LE-2026-OMEGA-001")
    ]
    for i, (k, v) in enumerate(author_info):
        table_author.rows[i].cells[0].paragraphs[0].add_run(k).bold = True
        table_author.rows[i].cells[1].paragraphs[0].add_run(v)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 1. Executive Summary
    h1 = doc.add_heading("1. Executive Summary of Breach", level=1)
    doc.add_paragraph(
        "On 17 November 2026 at 02:42:10 AM IST, Omega Regional Health Network (St. Jude Medical Center) "
        "suffered a catastrophic ransomware intrusion. The malware, identified as OmegaLocker v4.2, encrypted "
        "42,118 electronic patient records, diagnostic radiological imagery (PACS), and transactional billing stores. "
        "The attack paralyzed clinical operations in the Emergency Triage Ward and Intensive Care Unit (ICU)."
    )
    doc.add_paragraph(
        "The intrusion originated from a physical social engineering drop: a patient transfer report on a rogue SanDisk Ultra 32GB "
        "USB drive (EVD-OMEGA-002) inserted into Nurse Station Terminal 04 (WS-NURSE-04). A weaponized shortcut executed an "
        "obfuscated PowerShell dropper which escalated privileges via CVE-2024-30088 and pivoted over SMB (Port 445) to the "
        "Primary EHR SQL Database Server (OMEGA-SRV-01). First Responder Swaraj Bhattacharjee contained the incident at 03:30 AM IST "
        "via VLAN 999 isolation without data loss or ransom payment."
    )

    # 2. First Responder Steps & Scene Documentation
    doc.add_heading("2. First Responder Steps & Scene Documentation", level=1)
    doc.add_paragraph(
        "Adhering to RFC 3227 and NIST SP 800-61 Rev. 2, first responders executed the following critical steps:"
    )
    p_steps = doc.add_paragraph()
    p_steps.add_run("1. Human Life-Safety Priority: ").bold = True
    p_steps.add_run("Verified ICU bedside monitors switched to autonomous analog failover.\n")
    p_steps.add_run("2. Anti-Power Cut Policy: ").bold = True
    p_steps.add_run("Kept target server powered ON to preserve in-memory AES keys and uncommitted transactions.\n")
    p_steps.add_run("3. Physical & Logical Isolation: ").bold = True
    p_steps.add_run("Severed Ethernet drops and black-holed Cisco switch port Gi1/0/14 to VLAN 999.\n")
    p_steps.add_run("4. Volatile Memory Dump: ").bold = True
    p_steps.add_run("Acquired live physical RAM using WinPmem v4.0 to hardware write-blocked storage.\n")
    p_steps.add_run("5. Scene Photography & Clock Calibration: ").bold = True
    p_steps.add_run("Documented physical terminals, applied tamper-evident tags, and calibrated 11.75s clock skew.")

    # Insert Scene Topology Image if exists
    if os.path.exists(TOPOLOGY_IMG):
        doc.add_paragraph().paragraph_format.space_before = Pt(8)
        doc.add_picture(TOPOLOGY_IMG, width=Inches(6.2))
        cap = doc.add_paragraph("Figure 1: Crime Scene Physical Layout and Forensic Network Topology")
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.runs[0].font.size = Pt(9)
        cap.runs[0].font.italic = True

    # 3. Evidence Collection & Chain of Custody
    doc.add_heading("3. Evidence Collection & Chain of Custody", level=1)
    doc.add_paragraph(
        "All digital evidence was acquired using hardware write-blockers (Tableau T8u) and validated via SHA-256 hashes:"
    )

    t_evd = doc.add_table(rows=4, cols=4)
    t_evd.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Tag ID", "Asset Description", "Forensic Tool", "SHA-256 Checksum"]
    for c_idx, h in enumerate(headers):
        t_evd.rows[0].cells[c_idx].paragraphs[0].add_run(h).bold = True

    evd_data = [
        ("EVD-OMEGA-001", "Primary Server Disk Image (.raw)", "dc3dd v7.2 / Tableau T8u", "29f29a9471a107cd05623ac0..."),
        ("EVD-OMEGA-002", "SanDisk Ultra 32GB USB Drive", "Forensic USB Bridge", "a1b2c3d4e5f6789012345678..."),
        ("EVD-OMEGA-003", "Live RAM Memory Dump (.raw)", "WinPmem v4.0 Kernel", "444cf39fb88b1c3badde2790...")
    ]
    for r_idx, row in enumerate(evd_data, start=1):
        for c_idx, val in enumerate(row):
            t_evd.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)

    # 4. Malware Analysis & Behavior
    doc.add_heading("4. Analysis of Malicious Application Behavior", level=1)
    doc.add_paragraph(
        "Static and dynamic triage of OmegaLocker v4.2 revealed high-speed multithreaded cryptographic destruction:"
    )
    p_mal = doc.add_paragraph()
    p_mal.add_run("• Cryptography: ").bold = True
    p_mal.add_run("AES-256-CBC session keys generated per file, sealed with hardcoded RSA-4096 public key.\n")
    p_mal.add_run("• Anti-Forensics: ").bold = True
    p_mal.add_run("Executed 'vssadmin delete shadows /all /quiet' and 'bcdedit /set recoveryenabled no'.\n")
    p_mal.add_run("• Persistence: ").bold = True
    p_mal.add_run("Installed Windows service 'OmegaSvc' and registry key 'Run\\OmegaHealthUpdate'.\n")
    p_mal.add_run("• Command & Control: ").bold = True
    p_mal.add_run("Outbound TLS beaconing to 185.220.101.45:443 (Tor Exit Relay) dropping 'README_RECOVERY_KEY.txt'.")

    # 5. Attack Timeline
    doc.add_heading("5. Forensic Timeline Reconstruction", level=1)
    doc.add_paragraph(
        "Multi-source correlation of Windows Security, Sysmon, USBSTOR, and Firewall logs mapped the complete attack progression:"
    )
    if os.path.exists(TIMELINE_IMG):
        doc.add_picture(TIMELINE_IMG, width=Inches(6.2))
        cap2 = doc.add_paragraph("Figure 2: Correlated Attack Timeline & Kill Chain Progression")
        cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap2.runs[0].font.size = Pt(9)
        cap2.runs[0].font.italic = True

    # 6. Legal Provisions
    doc.add_heading("6. Legal Provisions Applicable (Indian Jurisprudence)", level=1)
    doc.add_paragraph(
        "The perpetrators are liable for prosecution under both special cyber statutes and the general criminal code:"
    )
    p_legal = doc.add_paragraph()
    p_legal.add_run("• Information Technology Act, 2000:\n").bold = True
    p_legal.add_run("  - Section 43: Unauthorized access and injection of computer contaminant (ransomware).\n")
    p_legal.add_run("  - Section 66: Computer-related offences and destruction of critical data.\n")
    p_legal.add_run("  - Section 66C: Identity theft for harvesting administrative domain credentials.\n")
    p_legal.add_run("  - Section 66D: Cheating by personation using malicious weaponized files.\n")
    p_legal.add_run("  - Section 66F: CYBER TERRORISM - Threatening national health infrastructure and public safety (Punishable with Life Imprisonment).\n")
    p_legal.add_run("  - Section 70: Unauthorized access to Protected Systems.\n\n")

    p_legal.add_run("• Indian Penal Code (IPC) / Bharatiya Nyaya Sanhita (BNS):\n").bold = True
    p_legal.add_run("  - Section 378/379 IPC (Theft) [Sec 303 BNS]: Theft of proprietary healthcare databases.\n")
    p_legal.add_run("  - Section 383/384/385 IPC (Extortion) [Sec 308 BNS]: Extortion demand of 15 XMR.\n")
    p_legal.add_run("  - Section 420 IPC (Cheating) [Sec 318 BNS]: Fraudulent inducement via fake patient reports.\n")
    p_legal.add_run("  - Section 120B IPC (Criminal Conspiracy) [Sec 61 BNS]: Multi-party cybercrime syndicate.\n\n")

    p_legal.add_run("• Digital Evidence Admissibility:\n").bold = True
    p_legal.add_run("  - Section 65B Indian Evidence Act / Section 63 Bharatiya Sakshya Adhiniyam certificate duly executed by Swaraj Bhattacharjee.")

    # 7. Recommendations
    doc.add_heading("7. Recommendations for Cybersecurity Hardening", level=1)
    doc.add_paragraph(
        "1. Removable Media Block: Restrict USB mass storage endpoints via Active Directory GPO.\n"
        "2. Zero Trust Microsegmentation: Isolate nurse stations from backend database VLANs.\n"
        "3. Air-gapped Immutable Backups: Implement WORM-protected AWS S3 Object Lock and tape archives.\n"
        "4. Endpoint Detection & Response (EDR): Deploy behavioral EDR to detect vssadmin deletion and process injection.\n"
        "5. Privilege Escalation Remediation: Rapid patch management targeting kernel vulnerabilities."
    )

    # Sign-off
    doc.add_heading("8. Investigator Attestation", level=1)
    p_sign = doc.add_paragraph()
    p_sign.add_run("Certified and Submitted by:\n\n").italic = True
    p_sign.add_run("Swaraj Bhattacharjee\n").bold = True
    p_sign.add_run("Lead Digital Forensic Investigator | Roll: 2301730011\nB.Tech CSE (AI & ML), Section A\nOmega Cyber Forensic Unit | Kolkata, India")

    doc.save(DOCX_PATH)
    print(f"[+] Word DOCX Report generated successfully at: {DOCX_PATH}")

def build_pdf():
    print("[*] Generating Legal PDF Report...")
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=colors.HexColor('#0f294a')
    )
    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#555555')
    )
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f294a'),
        spaceBefore=10,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#222222')
    )
    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title Banner
    story.append(Paragraph("DIGITAL FORENSIC INVESTIGATION REPORT", title_style))
    story.append(Paragraph("CASE OMEGA: INVESTIGATING A RANSOMWARE ATTACK ON A HEALTHCARE NETWORK", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Law Enforcement & Judicial Admissibility Edition // Strictly Confidential", sub_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0f294a'), spaceAfter=10))

    # Author Credentials Table
    author_table_data = [
        [Paragraph("<b>Lead Forensic Examiner:</b>", body_style), Paragraph("Swaraj Bhattacharjee", body_style)],
        [Paragraph("<b>Student Roll Number:</b>", body_style), Paragraph("2301730011", body_style)],
        [Paragraph("<b>Academic Program & Sec:</b>", body_style), Paragraph("B.Tech CSE (AI & ML) - Section A", body_style)],
        [Paragraph("<b>Investigation Reference:</b>", body_style), Paragraph("DFIR-LE-2026-OMEGA-001 | 17 Nov 2026", body_style)]
    ]
    t_auth = Table(author_table_data, colWidths=[160, 380])
    t_auth.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f1f5f9')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_auth)
    story.append(Spacer(1, 10))

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary of Breach", h1_style))
    exec_summary_text = (
        "On 17 November 2026 at 02:42:10 AM IST, Omega Regional Health Network (St. Jude Medical Center) "
        "suffered a catastrophic cryptoviral ransomware attack by <b>OmegaLocker v4.2</b>. The incident impacted "
        "42,118 electronic patient records, PACS radiology imaging, and emergency triage workstations. "
        "The attack vector was traced to a rogue SanDisk Ultra 32GB USB flash drive (EVD-OMEGA-002) inserted into "
        "Nurse Station WS-NURSE-04, launching an obfuscated PowerShell dropper. The adversary escalated privileges to "
        "SYSTEM (CVE-2024-30088) and pivoted over SMB (Port 445) to Primary EHR Server OMEGA-SRV-01. "
        "First Responder <b>Swaraj Bhattacharjee</b> isolated the network via VLAN 999 at 03:30 AM IST, securing forensic bit-stream "
        "images and RAM dumps without data loss or ransom compliance."
    )
    story.append(Paragraph(exec_summary_text, body_style))
    story.append(Spacer(1, 8))

    # 2. First Responder Steps & Scene Documentation
    story.append(Paragraph("2. First Responder Protocol & Scene Documentation", h1_style))
    sop_summary = (
        "Following NIST SP 800-61 and ISO/IEC 27037 standards: (1) Human life-safety verified by ensuring ICU monitors ran in "
        "analog failover mode; (2) Critical servers kept powered ON to preserve ephemeral memory encryption keys; (3) Physical "
        "cables severed and switch port Gi1/0/14 black-holed to VLAN 999; (4) Volatile RAM captured via WinPmem v4.0; "
        "(5) Crime scene documented via 360-degree photography, evidence tagging, and clock skew calibration (11.75s drift)."
    )
    story.append(Paragraph(sop_summary, body_style))
    story.append(Spacer(1, 8))

    # Topology image if exists
    if os.path.exists(TOPOLOGY_IMG):
        story.append(RLImage(TOPOLOGY_IMG, width=520, height=260))
        story.append(Spacer(1, 4))
        story.append(Paragraph("<i>Figure 1: Crime Scene Physical Layout and Forensic Network Topology</i>", sub_style))
        story.append(Spacer(1, 8))

    # 3. Evidence Table
    story.append(Paragraph("3. Evidence Collection & Chain of Custody", h1_style))
    evd_table_data = [
        [Paragraph("<b>Tag ID</b>", bold_body), Paragraph("<b>Asset Description</b>", bold_body), Paragraph("<b>Forensic Method</b>", bold_body), Paragraph("<b>SHA-256 Checksum</b>", bold_body)],
        [Paragraph("EVD-001", body_style), Paragraph("Primary Server Disk (.raw)", body_style), Paragraph("dc3dd / Tableau T8u", body_style), Paragraph("29f29a9471a107cd...4400", body_style)],
        [Paragraph("EVD-002", body_style), Paragraph("SanDisk 32GB USB Flash Drive", body_style), Paragraph("Read-Only Forensic Bridge", body_style), Paragraph("a1b2c3d4e5f67890...def0", body_style)],
        [Paragraph("EVD-003", body_style), Paragraph("Volatile RAM Dump (.raw)", body_style), Paragraph("WinPmem v4.0 Kernel", body_style), Paragraph("444cf39fb88b1c3b...0282", body_style)],
    ]
    t_evd_pdf = Table(evd_table_data, colWidths=[55, 160, 135, 190])
    t_evd_pdf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f294a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0f294a')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_evd_pdf)
    story.append(Spacer(1, 8))

    # 4. Malware Analysis
    story.append(Paragraph("4. Malware Behavior Analysis (OmegaLocker v4.2)", h1_style))
    malware_summary = (
        "<b>Binary Characteristics:</b> PE32+ x86-64 executable with high entropy (7.91).<br/>"
        "<b>Encryption Mechanics:</b> Employs multithreaded AES-256-CBC per-file encryption sealed with hardcoded RSA-4096.<br/>"
        "<b>Defense Evasion:</b> Executes <i>vssadmin delete shadows /all /quiet</i> and disables recovery via <i>bcdedit</i>.<br/>"
        "<b>Persistence:</b> Adds registry autorun key <i>HKCU\\...\\Run\\OmegaHealthUpdate</i> and installs service <i>OmegaSvc</i>.<br/>"
        "<b>Threat Classification:</b> Ransomware-as-a-Service (RaaS) Double Extortion (CVSS 9.8 Critical)."
    )
    story.append(Paragraph(malware_summary, body_style))
    story.append(Spacer(1, 8))

    # 5. Timeline Image
    story.append(Paragraph("5. Attack Timeline Reconstruction", h1_style))
    if os.path.exists(TIMELINE_IMG):
        story.append(RLImage(TIMELINE_IMG, width=520, height=240))
        story.append(Spacer(1, 4))
        story.append(Paragraph("<i>Figure 2: Multi-Source Correlated Forensic Attack Timeline</i>", sub_style))
        story.append(Spacer(1, 8))

    # 6. Legal Provisions
    story.append(Paragraph("6. Applicable Legal Provisions (Indian Law)", h1_style))
    legal_text = (
        "<b>Information Technology Act, 2000:</b><br/>"
        "• Section 43 & Section 66: Unauthorized access, data impairment, and introduction of computer contaminant.<br/>"
        "• Section 66C: Identity theft for unauthorized use of administrative credentials.<br/>"
        "• Section 66D: Cheating by personation through weaponized document shortcuts.<br/>"
        "• Section 66F: <b>CYBER TERRORISM</b> - Endangering national healthcare systems and human life (Life Imprisonment).<br/>"
        "• Section 70: Unauthorized access to Protected Systems.<br/><br/>"
        "<b>Indian Penal Code (IPC) / Bharatiya Nyaya Sanhita (BNS):</b><br/>"
        "• Section 378/379 IPC [Sec 303 BNS]: Theft of electronic medical databases.<br/>"
        "• Section 383/384/385 IPC [Sec 308 BNS]: Extortion demand of 15 XMR under threat of data publication.<br/>"
        "• Section 420 IPC [Sec 318 BNS]: Cheating and dishonest inducement.<br/>"
        "• Section 120B IPC [Sec 61 BNS]: Criminal conspiracy.<br/><br/>"
        "<b>Admissibility:</b> Compliant with Section 65B Indian Evidence Act / Section 63 BSA as per <i>Arjun Panditrao Khotkar (2020)</i>."
    )
    story.append(Paragraph(legal_text, body_style))
    story.append(Spacer(1, 8))

    # 7. Recommendations
    story.append(Paragraph("7. Cybersecurity Hardening Recommendations", h1_style))
    recs_text = (
        "1. <b>Peripheral USB Lockdown:</b> Enforce strict Removable Storage GPOs across all clinical endpoints.<br/>"
        "2. <b>Network Microsegmentation:</b> Isolate nurse intake terminals from core EHR database subnets.<br/>"
        "3. <b>Immutable Backups:</b> Deploy AWS S3 Object Lock (WORM) and offline air-gapped tape storage.<br/>"
        "4. <b>EDR & Script Sandboxing:</b> Implement behavioral EDR to detect vssadmin shadow deletions and script execution.<br/>"
        "5. <b>Privilege Management:</b> Enforce Least Privilege and rapid patch cycles for kernel vulnerabilities."
    )
    story.append(Paragraph(recs_text, body_style))
    story.append(Spacer(1, 10))

    # Certification Sign-off
    story.append(Paragraph("8. Official Attestation & Examiner Sign-Off", h1_style))
    sign_text = (
        "I hereby certify that this forensic report is complete, scientifically valid, and prepared in accordance with "
        "recognized digital forensic standards. All digital artifacts remain bit-perfect and cryptographically verifiable.<br/><br/>"
        "<b>Examiner:</b> Swaraj Bhattacharjee<br/>"
        "<b>Roll Number:</b> 2301730011<br/>"
        "<b>Academic Degree:</b> B.Tech CSE AI ML, Section A<br/>"
        "<b>Designation:</b> Lead Forensic Examiner, Case Omega<br/>"
        "<b>Date:</b> 17 November 2026 | Kolkata, India"
    )
    story.append(Paragraph(sign_text, body_style))

    doc.build(story)
    print(f"[+] Legal PDF Report generated successfully at: {PDF_PATH}")

def main():
    print("=" * 65)
    print("  CASE OMEGA FORENSIC REPORT COMPILER (PDF / DOCX)")
    print("  Lead Investigator: Swaraj Bhattacharjee (Roll: 2301730011)")
    print("=" * 65)
    build_docx()
    build_pdf()
    print("=" * 65)
    print("[SUCCESS] Both DOCX and PDF legal-technical reports generated.")

if __name__ == "__main__":
    main()
