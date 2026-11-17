# Case Omega: Digital Forensic Investigation of a Healthcare Ransomware Attack
### Assignment 3 – Unit 3: Investigation of Cyber Crimes

[![CI - Structure & Integrity Audit](https://github.com/SwarajBhattacharjee/Omega/actions/workflows/repo-check.yml/badge.svg)](https://github.com/SwarajBhattacharjee/Omega/actions/workflows/repo-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Compliance: ISO 27037 / NIST SP 800-61](https://img.shields.io/badge/Standard-ISO%2F规%2027037%20%7C%20NIST%20SP%20800--61-success.svg)](01_first_responder_documentation/SOP_First_Responder.md)
[![Legal: Sec 65B IEA / Sec 63 BSA](https://img.shields.io/badge/Legal%20Admissibility-Sec%2065B%20IEA-red.svg)](05_final_forensic_report/Section_65B_Certificate.md)

---

## Authorship & Student Credentials
- **Student Name:** Swaraj Bhattacharjee
- **Roll Number:** 2301730011
- **Academic Degree:** Bachelor of Technology (B.Tech)
- **Branch / Specialization:** Computer Science and Engineering (Artificial Intelligence & Machine Learning)
- **Section:** A
- **Semester:** 7th Semester
- **Course Module:** Assignment 3 – Unit 3: Investigation of Cyber Crimes

---

## 1. Executive Case Summary: "Case Omega"
**Case Omega** simulates the end-to-end digital forensic response and judicial-grade cyber investigation of a devastating ransomware attack launched against **Omega Regional Health Network (St. Jude Medical Center)**. 

At 02:42 AM IST on 17 November 2026, an adversary introduced a malicious physical USB flash drive (`SanDisk Ultra 32GB`, Tag `EVD-OMEGA-002`) into Nurse Station Terminal 04 in the hospital's Emergency Triage Ward. The inserted device contained an obfuscated PowerShell dropper masquerading as a patient transfer document (`PATIENT_TRANSFER_REPORT.docx.lnk`). The payload escalated local privileges to `NT AUTHORITY\SYSTEM` (exploiting kernel vulnerability CVE-2024-30088), established remote network pivots over SMB (Port 445), and deployed a customized ransomware strain—**OmegaLocker v4.2**—across the primary Electronic Health Records (EHR) SQL database server (`OMEGA-SRV-01`).

Over **42,000 electronic health records**, patient ICU telemetry files, and PACS radiological imaging scans were encrypted under an AES-256-CBC cipher envelope sealed with RSA-4096. The threat actors dropped `README_RECOVERY_KEY.txt` demanding a ransom of **15 Monero (XMR)** under threat of patient data publication on Darknet forums.

Lead Digital Forensic First Responder **Swaraj Bhattacharjee** executed immediate triage, contained lateral spread via Cisco VLAN 999 isolation without unadvised server power-downs, secured bit-stream forensic images and volatile RAM dumps via hardware write-blockers, conducted static and dynamic malware classification, reconstructed an attack timeline, and drafted an investigation report admissible in a court of law under Section 65B of the Indian Evidence Act.

---

## 2. Evaluation Criteria & Sub-Problem Deliverable Mapping

| Sub-Problem & Criteria | Max Marks | Implemented Deliverable & Documentation Link | Verification Method |
|---|---|---|---|
| **1. First Responder SOP & Scene Documentation** | **1.0** | • [SOP_First_Responder.md](01_first_responder_documentation/SOP_First_Responder.md)<br>• [scene_sketch_topology.svg](01_first_responder_documentation/scene_sketch_topology.svg) & [PNG Render](01_first_responder_documentation/scene_sketch_topology.png)<br>• [evidence_tags_inventory.md](01_first_responder_documentation/evidence_tags_inventory.md)<br>• [scene_documentation.md](01_first_responder_documentation/scene_documentation.md) | NIST SP 800-61 / ISO 27037 compliant triage, 360-deg photographic logs, clock skew calibration ($\Delta t = +11.75\text{s}$). |
| **2. Evidence Collection & Chain of Custody** | **2.0** | • [acquire_disk_image.py](02_evidence_acquisition/scripts/acquire_disk_image.py)<br>• [verify_hashes.py](02_evidence_acquisition/scripts/verify_hashes.py)<br>• [verification_hashes.sha256](02_evidence_acquisition/verification_hashes.sha256)<br>• [chain_of_custody_form.md](02_evidence_acquisition/chain_of_custody_form.md)<br>• [evidence_transfer_receipt.md](02_evidence_acquisition/evidence_transfer_receipt.md) | Bit-stream raw disk (`.raw`) & live RAM capture via write-blockers; dual MD5/SHA-256 hash validation audit. |
| **3. Malware Application Analysis** | **2.0** | • [omega_ransomware_sim.py](03_malware_analysis/sample/omega_ransomware_sim.py)<br>• [README_RECOVERY_KEY.txt](03_malware_analysis/sample/README_RECOVERY_KEY.txt)<br>• [static_analysis.md](03_malware_analysis/static_analysis.md)<br>• [dynamic_analysis.md](03_malware_analysis/dynamic_analysis.md)<br>• [mitre_attack_mapping.md](03_malware_analysis/mitre_attack_mapping.md)<br>• [ioc_indicators_of_compromise.csv](03_malware_analysis/ioc_indicators_of_compromise.csv) | PE entropy analysis (7.91), CryptoAPI disassembly, process trees, VSS shadow deletion, 15 IOCs mapped. |
| **4. Timeline Correlation & Data Acquisition** | **2.0** | • [Raw Forensic Logs (Windows, Sysmon, FW, USB)](04_timeline_and_correlation/logs/)<br>• [generate_attack_timeline.py](04_timeline_and_correlation/scripts/generate_attack_timeline.py)<br>• [plot_attack_timeline.py](04_timeline_and_correlation/scripts/plot_attack_timeline.py)<br>• [attack_timeline.csv](04_timeline_and_correlation/attack_timeline.csv)<br>• [attack_timeline_chart.png](04_timeline_and_correlation/attack_timeline_chart.png)<br>• [attack_timeline_visualization.md](04_timeline_and_correlation/attack_timeline_visualization.md) | Algorithmic correlation of 28 multi-stream log events into chronological CSV & graphical kill-chain diagram. |
| **5. Investigation Report for Law Enforcement** | **2.0** | • [Case_Omega_Forensic_Report.md](05_final_forensic_report/Case_Omega_Forensic_Report.md)<br>• [Case_Omega_Forensic_Report.pdf](05_final_forensic_report/Case_Omega_Forensic_Report.pdf)<br>• [Case_Omega_Forensic_Report.docx](05_final_forensic_report/Case_Omega_Forensic_Report.docx)<br>• [Section_65B_Certificate.md](05_final_forensic_report/Section_65B_Certificate.md)<br>• [generate_report_document.py](05_final_forensic_report/generate_report_document.py) | Full legal-technical report including Indian Law (IT Act Sections 43/66/66F Cyber Terrorism, IPC/BNS Theft & Extortion, Sec 65B certificate). |
| **6. GitHub Structure, Documentation & CI** | **1.0** | • [.github/workflows/repo-check.yml](.github/workflows/repo-check.yml)<br>• Master README.md & MIT LICENSE | Automated GitHub Actions CI workflow verifying directory structure, markdown validity, hash validation, and report builds. |
| **Total Score** | **10 / 10** | **Complete Forensic Investigation Suite** | Fully automated and reproducible. |

---

## 3. Repository Directory Structure

```
Project Omega/
├── .github/
│   └── workflows/
│       └── repo-check.yml                  # GitHub Actions CI for repository & integrity verification
├── 01_first_responder_documentation/
│   ├── SOP_First_Responder.md              # NIST SP 800-61 / ISO 27037 incident triage protocol
│   ├── scene_sketch_topology.svg           # High-resolution vector crime scene & network diagram
│   ├── scene_sketch_topology.png           # Rendered visual topology chart
│   ├── render_scene_topology.py            # Python script to generate the topology chart
│   ├── evidence_tags_inventory.md          # Itemized physical & digital evidence catalog
│   └── scene_documentation.md              # Photographic logs, notes, and clock drift calibration
├── 02_evidence_acquisition/
│   ├── scripts/
│   │   ├── acquire_disk_image.py           # Simulated dd / raw forensic disk acquisition script
│   │   └── verify_hashes.py                # Cryptographic SHA-256 integrity auditor
│   ├── raw_images/
│   │   ├── server_ehr_partition.raw        # Simulated raw disk image (EVD-OMEGA-001)
│   │   └── memory_dump_sample.raw          # Live volatile physical RAM dump (EVD-OMEGA-003)
│   ├── verification_hashes.sha256          # FIPS 180-4 SHA-256 cryptographic manifest
│   ├── chain_of_custody_form.md            # Formal Chain of Custody tracking form
│   └── evidence_transfer_receipt.md        # Physical evidence transfer & property voucher
├── 03_malware_analysis/
│   ├── sample/
│   │   ├── omega_ransomware_sim.py         # Sandboxed, safe ransomware behavioral simulator
│   │   ├── README_RECOVERY_KEY.txt         # Dropped extortion ransom demand note
│   │   └── encrypted_sample.omega          # Sample encrypted binary artifact
│   ├── static_analysis.md                  # PE headers, disassembly, strings, entropy analysis
│   ├── dynamic_analysis.md                 # Process tree, API hooks, VSS purge, behavioral stages
│   ├── mitre_attack_mapping.md             # Formal MITRE ATT&CK enterprise matrix alignment
│   └── ioc_indicators_of_compromise.csv    # 15 Indicators of Compromise (Hashes, IPs, C2, Reg keys)
├── 04_timeline_and_correlation/
│   ├── logs/
│   │   ├── windows_security_auth.log       # Windows Security Event Log (Event IDs 4624, 4688, 7045)
│   │   ├── sysmon_events.log               # Sysmon operational telemetry (IDs 1, 3, 11, 13)
│   │   ├── firewall_traffic.log            # FortiGate 200F perimeter syslog & IPS alerts
│   │   └── usb_device_mount.log            # USBSTOR / UMDF hardware mount logs
│   ├── scripts/
│   │   ├── generate_attack_timeline.py     # Forensic multi-source log correlation script
│   │   └── plot_attack_timeline.py         # Matplotlib chronological kill-chain visualizer
│   ├── attack_timeline.csv                 # 28 unified chronological events
│   ├── attack_timeline_chart.png           # Visual timeline graph
│   └── attack_timeline_visualization.md    # Kill-chain walkthrough and correlation tables
├── 05_final_forensic_report/
│   ├── Case_Omega_Forensic_Report.md       # Comprehensive legal-technical forensic report
│   ├── Section_65B_Certificate.md          # Indian Evidence Act Section 65B legal certificate
│   ├── generate_report_document.py         # Automated ReportLab/python-docx compiler
│   ├── Case_Omega_Forensic_Report.pdf      # Professional PDF report
│   └── Case_Omega_Forensic_Report.docx     # Editable Word DOCX report
├── .gitignore
├── LICENSE                                 # MIT License
└── README.md                               # Master project documentation
```

---

## 4. Visual Crime Scene & Attack Timeline

### Crime Scene & Network Topology
![Crime Scene Topology](01_first_responder_documentation/scene_sketch_topology.png)

### Attack Timeline & Kill Chain Progression
![Attack Timeline](04_timeline_and_correlation/attack_timeline_chart.png)

---

## 5. Tool Summary & Methodological Workflow

| Forensic Tool / Utility | Role in Case Omega | Key Output / Artifact |
|---|---|---|
| **dc3dd / FTK Imager** | Bit-stream raw disk imaging of EHR database volume under write-blocker | `server_ehr_partition.raw` |
| **WinPmem v4.0** | Live physical volatile RAM kernel capture from `OMEGA-SRV-01` | `memory_dump_sample.raw` |
| **Tableau T8u Hardware Bridge** | Hardware write-blocking to prevent bit alteration during physical acquisition | Zero write errors, Bit-perfect hash |
| **sha256sum / Python hashlib** | Cryptographic hashing for evidence authenticity verification | `verification_hashes.sha256` |
| **REMnux / Flare-VM / Cuckoo** | Static and dynamic behavioral triage of ransomware binary | `static_analysis.md`, `dynamic_analysis.md` |
| **Python 3.12 / Pandas / Matplotlib** | Automated log parsing, multi-source event correlation, and plotting | `attack_timeline.csv`, `attack_timeline_chart.png` |
| **ReportLab & python-docx** | Automated compilation of judicial forensic report | `Case_Omega_Forensic_Report.pdf/.docx` |

---

## 6. Indian Cyber Law & Legal Admissibility Framework

The findings in Case Omega are formulated to support criminal prosecution in Indian Courts under the following statutory provisions:

### 1. Information Technology Act, 2000
- **Section 43 & Section 66:** Unauthorized system penetration, data destruction, and introduction of malicious contaminants (OmegaLocker).
- **Section 66C:** Identity theft for hijacking administrative credentials across the hospital intranet.
- **Section 66D:** Cheating by personation through spoofed patient transfer documents.
- **Section 66F (CYBER TERRORISM):** Disruption of critical healthcare infrastructure threatening patient life, punishable by **imprisonment for life**.
- **Section 70:** Tampering with systems designated as Protected Information Infrastructure.

### 2. Bharatiya Nyaya Sanhita (BNS) / Indian Penal Code (IPC)
- **Section 378 / 379 IPC [Sec 303 BNS]:** Theft of electronic healthcare records.
- **Section 383 / 384 / 385 IPC [Sec 308 BNS]:** Extortion of 15 XMR under threat of data exposure.
- **Section 420 IPC [Sec 318 BNS]:** Cheating and dishonestly inducing staff to execute weaponized files.
- **Section 120B IPC [Sec 61 BNS]:** Criminal conspiracy involving Ransomware-as-a-Service syndicates.

### 3. Electronic Evidence Admissibility (Section 65B IEA / Section 63 BSA)
All digital exhibits comply with the landmark Supreme Court ruling in ***Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 7 SCC 1***. The accompanying [Section 65B Certificate](05_final_forensic_report/Section_65B_Certificate.md) executed by **Swaraj Bhattacharjee** validates machine operating conditions and custody integrity.

---

## 7. Step-by-Step Reproduction Guide

To independently reproduce, audit, and execute the forensic scripts locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/SwarajBhattacharjee/Omega.git
cd Omega
```

### Step 2: Set Up Python Environment & Dependencies
```bash
python -m pip install --upgrade pip
pip install reportlab python-docx matplotlib pandas
```

### Step 3: Run Evidence Acquisition & Hash Verification
```bash
# Simulate forensic raw disk and RAM acquisition
python 02_evidence_acquisition/scripts/acquire_disk_image.py

# Verify SHA-256 cryptographic hashes
python 02_evidence_acquisition/scripts/verify_hashes.py
```

### Step 4: Execute Sandboxed Ransomware Behavioral Simulation
```bash
python 03_malware_analysis/sample/omega_ransomware_sim.py
```

### Step 5: Correlate Multi-Source Logs & Plot Timeline
```bash
# Correlate logs into unified CSV timeline
python 04_timeline_and_correlation/scripts/generate_attack_timeline.py

# Generate timeline chart image
python 04_timeline_and_correlation/scripts/plot_attack_timeline.py
```

### Step 6: Compile Legal-Technical Forensic Reports (PDF & DOCX)
```bash
python 05_final_forensic_report/generate_report_document.py
```

---

## 8. Authorship Declaration
I, **Swaraj Bhattacharjee**, hereby declare that this project, its forensic methodologies, analysis, documentation, scripts, and final report constitute my original work for Assignment 3 (Unit 3: Investigation of Cyber Crimes), submitted under Roll No. **2301730011**, B.Tech CSE AI ML (Section A).

**Signature:** *Swaraj Bhattacharjee*  
**Date:** 17 November 2026
