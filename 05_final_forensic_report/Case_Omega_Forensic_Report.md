# DIGITAL FORENSIC INVESTIGATION REPORT
## CASE OMEGA: INVESTIGATING A RANSOMWARE ATTACK ON A HEALTHCARE NETWORK
**Report Reference:** DFIR-LE-2026-OMEGA-001  
**Classification:** STRICTLY CONFIDENTIAL // LAW ENFORCEMENT & JUDICIAL ADMISSIBILITY  
**Target Entity:** St. Jude Hospital / Omega Regional Health Network  
**Jurisdiction:** Cyber Crime Police Station (CCPS), Special Crime Branch & CERT-In  

---

### INVESTIGATOR & AUTHOR DECLARATION
- **Lead Digital Forensic Examiner:** Swaraj Bhattacharjee
- **Roll Number:** 2301730011
- **Academic Program:** B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)
- **Section:** A
- **Investigation Date:** 17 November 2026
- **Forensic Standard Compliance:** ISO/IEC 27037:2012, NIST SP 800-61 Rev. 2, NIST SP 800-86, Section 65B Indian Evidence Act (IEA) / Section 63 Bharatiya Sakshya Adhiniyam (BSA)

---

## 1. EXECUTIVE SUMMARY

### 1.1 Incident Overview
On the morning of 17 November 2026, at approximately 02:42:10 AM IST, the digital health infrastructure of Omega Regional Health Network (St. Jude Medical Center) was subjected to a coordinated, high-impact cryptoviral cyber-attack (Ransomware). The malicious payload, identified as **OmegaLocker v4.2**, encrypted primary patient records, medical imaging repositories (PACS), and transactional billing databases, disrupting critical medical care services across Emergency and Intensive Care Units (ICU).

### 1.2 Root Cause & Initial Infection Vector
Forensic triage established that the initial breach occurred at **Nurse Station Terminal 04 (WS-NURSE-04)** in the Emergency Triage Ward. An unauthorized physical USB flash storage device (`SanDisk Ultra 32GB`, Serial: `SDCZ48-449102-K9`) was plugged into the terminal. The device contained a weaponized shortcut (`PATIENT_TRANSFER_REPORT.docx.lnk`) which, upon user interaction, spawned an obfuscated Base64 PowerShell dropper.

### 1.3 Scope of Compromise & Impact
- **Impacted Systems:** 1 Nurse Workstation (`WS-NURSE-04`), 1 Primary Electronic Health Records (EHR) SQL Database Server (`OMEGA-SRV-01`).
- **Encrypted Records:** An estimated 42,118 electronic patient records, including ICU diagnostic telemetry, prescription histories, and coronary angiographies.
- **Ransom Demand:** 15 Monero (XMR) (~$2,500 USD) deposited to privacy wallet `888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkFxbTNsFo5VN` with threat of exfiltrated patient PII release on the Darknet.
- **Current Operational Status:** Systems contained via VLAN 999 black-hole routing. Forensically sterile bit-stream disk images and volatile RAM dumps captured prior to evidence degradation. Zero ransom paid.

---

## 2. FIRST RESPONDER ACTIONS & SCENE DOCUMENTATION

### 2.1 First Responder Intervention Protocol
The Digital Evidence First Responder (DEFR), **Swaraj Bhattacharjee**, arrived at the scene at 03:45 AM IST following escalation by the Hospital Chief Medical Officer. Response strictly adhered to **RFC 3227** and **NIST SP 800-61**:
1. **Human Safety Prioritization:** Confirmed ICU bedside patient telemetry monitors were operating in autonomous analog failover mode.
2. **Volatile State Preservation:** The infected server (`OMEGA-SRV-01`) was kept powered ON to prevent cryptographic destruction of in-memory AES keys and volatile process memory.
3. **Network Containment:** Physical Ethernet cables were severed from WS-NURSE-04. The Core Switch (Cisco Catalyst 9300) port `Gi1/0/14` was isolated into non-routable Quarantine VLAN 999.
4. **Physical Scene Documentation:** 360-degree photography captured screen status, peripheral ports, cable routing, and ambient server room telemetry ($19.4^\circ\text{C}$, $38\%$ RH).
5. **Clock Skew Calibration:** Target server clock was benchmarked against National Physical Laboratory (NPL) atomic time: server clock was slow by $\Delta t = +11.75\text{ seconds}$.

### 2.2 Crime Scene & Network Topology
The crime scene encompasses two distinct physical locations:
- **Location 1 (Patient Triage Desk):** Nurse Station WS-NURSE-04 (IP: `192.168.10.45`), where physical USB drive `EVD-OMEGA-002` was introduced.
- **Location 2 (Restricted Server Room B204):** Enterprise Server Rack 02 containing Primary EHR Server `OMEGA-SRV-01` (IP: `192.168.10.100`).

*(Refer to visual topology document `scene_sketch_topology.svg` and `scene_sketch_topology.png`).*

---

## 3. EVIDENCE COLLECTION & CHAIN OF CUSTODY

### 3.1 Digital Evidence Item Inventory

| Evidence Tag ID | Physical Asset | Serial Number | Forensic Acquisition Method | SHA-256 Master Checksum |
|---|---|---|---|---|
| **EVD-OMEGA-001** | Primary EHR Server RAID-1 NVMe | `DELL-R750-OMEGA99` | Bit-stream raw image (`dc3dd`) via Tableau T8u hardware write-blocker | `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400` |
| **EVD-OMEGA-002** | Rogue USB Flash Storage | `SDCZ48-449102-K9` | Physical seizure in anti-static Faraday pouch | `a1b2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0` |
| **EVD-OMEGA-003** | Volatile RAM Memory Dump | `OMEGA-SRV-01-RAM` | Live kernel acquisition via WinPmem v4.0 to sterile NVMe | `444cf39fb88b1c3badde2790f88cf229b853c393dd5f60518ccab52080050282` |
| **EVD-OMEGA-004** | Perimeter Firewall Logs | `FG200F-KOL-7881` | Cryptographically signed Syslog export | Signed GPG Syslog Stream |

### 3.2 Chain of Custody & Hash Integrity Verification
Every seized item was packaged using tamper-evident security tape (`#SEC-9901`, `#SEC-9902`). Independent cryptographic audits conducted at the Cyber Crime Police Station (CCPS) and Central Forensic Science Laboratory (CFSL) confirmed $100\%$ bit-for-bit hash equality (`SHA-256`), eliminating all claims of evidentiary tampering.

---

## 4. MALWARE APPLICATION ANALYSIS: OMEGALOCKER v4.2

### 4.1 Static Analysis Findings
- **Executable Format:** PE32+ (x86-64 GUI/CLI hybrid), compiled 2026-11-16 22:14:08 UTC.
- **Packing & Entropy:** Section `.data` exhibited entropy of $7.91 / 8.00$, confirming custom compression/encryption wrapper.
- **Cryptographic Engine:** Uses Microsoft CryptoAPI (`ADVAPI32.DLL`, `BCRYPT.DLL`) to generate ephemeral 256-bit AES keys in CBC mode, sealed by an embedded 4096-bit RSA public key.
- **Target Extensions:** `.db`, `.sql`, `.mdf`, `.ldf`, `.dcm` (DICOM medical imagery), `.pdf`, `.docx`.

### 4.2 Dynamic Behavior & Attack Flow
1. **Defense Evasion:** Executed `vssadmin.exe delete shadows /all /quiet` to destroy all local Volume Shadow Copies, preventing native recovery.
2. **Boot Policy Manipulation:** Issued `bcdedit /set {default} recoveryenabled no` to prevent automatic startup repair.
3. **Database Unlocking:** Terminated `MSSQLSERVER` and `EHRHealthService` services to release active write locks on `.mdf` files.
4. **Encryption Loop:** Iterated through file systems, encrypting contents and appending `.omega` extension. Dropped `README_RECOVERY_KEY.txt` in all traversed directories.
5. **Persistence:** Created Windows Service `OmegaSvc` (`C:\ProgramData\omega_payload.exe`) and added registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\OmegaHealthUpdate`.
6. **Command and Control:** Attempted TLS beaconing to Tor Exit Node `185.220.101.45:443` (`c2.omega-blacklock.onion`).

### 4.3 MITRE ATT&CK Matrix Mapping
The attack successfully traversed seven distinct MITRE ATT&CK phases:
- **Initial Access:** `T1200` (Hardware Additions - USB)
- **Execution:** `T1204.002` (Malicious File Execution), `T1059.003` (Windows Command Shell)
- **Privilege Escalation:** `T1068` (Kernel Privilege Escalation CVE-2024-30088)
- **Lateral Movement:** `T1021.002` (SMB Admin Shares / PsExec)
- **Persistence:** `T1547.001` (Registry Run Keys), `T1053.005` (Scheduled Task)
- **Defense Evasion:** `T1490` (Inhibit System Recovery)
- **Impact:** `T1486` (Data Encrypted for Impact)

---

## 5. ATTACK TIMELINE & CORRELATION
Through algorithmic multi-source log aggregation (Windows Security Events, Sysmon, USBSTOR, and Firewall traffic), the chronological sequence of the attack was reconstructed:

- **02:35:10 IST:** Nurse on duty authenticates interactively to `WS-NURSE-04`.
- **02:42:10 IST:** SanDisk Ultra USB inserted; driver registers drive `E:`.
- **02:43:02 IST:** Malicious `.lnk` clicked; hidden PowerShell dropper launched.
- **02:45:18 IST:** Local kernel exploit triggers privilege elevation to `NT AUTHORITY\SYSTEM`.
- **02:50:30 IST:** Adversary pivots laterally over SMB (Port 445) to Primary EHR Server `192.168.10.100`.
- **02:53:14 IST:** Persistent service `OmegaSvc` registered on `OMEGA-SRV-01`.
- **02:55:00 IST:** Outbound C2 socket established to `185.220.101.45:443`.
- **03:00:22 IST:** Local backups deleted (`vssadmin delete shadows`).
- **03:02:11 IST:** Database files encrypted with `.omega` extension; ransom notes dropped.
- **03:30:00 IST:** First Responder **Swaraj Bhattacharjee** enforces VLAN 999 quarantine, halting further propagation.

---

## 6. LEGAL PROVISIONS APPLICABLE (INDIAN JURISPRUDENCE)

The actions executed by the perpetrators constitute severe cognizable, non-bailable criminal violations under the **Information Technology Act, 2000** and the **Indian Penal Code (IPC)** / **Bharatiya Nyaya Sanhita (BNS), 2023**:

### 6.1 Information Technology Act, 2000 (Amended 2008)
1. **Section 43 (Penalty for Damage to Computer System):**  
   Applicable for unauthorized access, extraction, copying, and introduction of computer contaminant (ransomware) into hospital servers.
2. **Section 66 (Computer Related Offences):**  
   Imposes criminal penalty (imprisonment up to 3 years and fines) for dishonestly and fraudulently impairing computer data integrity.
3. **Section 66C (Identity Theft):**  
   Applicable for the unauthorized harvesting and reuse of administrative credentials to laterally pivot from workstation to server.
4. **Section 66D (Cheating by Personation using Computer Resource):**  
   Applicable for masquerading as authorized healthcare diagnostic tools via fraudulent `.lnk` files.
5. **Section 66F (Cyber Terrorism) – *CRITICAL PROVISION*:**  
   Given that the target is a **critical healthcare network** whose disruption directly endangered human life in the Emergency and ICU wards, the attack constitutes Cyber Terrorism under Section 66F(1)(B), punishable with **imprisonment for life**.
6. **Section 70 (Protected Systems):**  
   Hospital EHR systems designated as critical healthcare information infrastructure fall under Protected Systems protections.

### 6.2 Indian Penal Code (IPC) / Bharatiya Nyaya Sanhita (BNS)
1. **Section 378 / 379 IPC (Theft) [Sec 303 BNS]:**  
   Theft of proprietary electronic medical data and hospital databases.
2. **Section 383 / 384 / 385 IPC (Extortion) [Sec 308 BNS]:**  
   Coercive extortion of 15 Monero (XMR) under threat of permanent data destruction and public exposure of patient medical records.
3. **Section 420 IPC (Cheating and Dishonestly Inducing Delivery of Property) [Sec 318 BNS]:**  
   Fraudulent social engineering inducement leading to payload execution.
4. **Section 120B IPC (Criminal Conspiracy) [Sec 61 BNS]:**  
   Concerted criminal conspiracy among Ransomware-as-a-Service (RaaS) affiliates and dark web operators.

### 6.3 Digital Evidence Admissibility (Section 65B IEA / Section 63 BSA)
All digital outputs, disk images, and memory dumps comply fully with the conditions laid down in the landmark Supreme Court ruling ***Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 7 SCC 1***. A standalone Certificate under Section 65B of the Indian Evidence Act / Section 63 of Bharatiya Sakshya Adhiniyam has been executed by Lead Examiner **Swaraj Bhattacharjee**.

---

## 7. RECOMMENDATIONS FOR CYBERSECURITY HARDENING

Based on the forensic root cause analysis, the following technical and procedural safeguards are recommended:

1. **Hardware Peripheral Lockdown (USB Control):**  
   Implement Active Directory Group Policy Objects (GPOs) and endpoint protection agents to enforce strict device-level USB blocking across all clinical terminals (`Disable-StorageAccess -RemovableMedia`).
2. **Network Microsegmentation & Zero Trust:**  
   Enforce zero-trust network architecture dividing clinical nurse stations from backend EHR SQL clusters. Deny lateral SMB (TCP 445) and RDP (TCP 3389) between endpoints.
3. **Immutable, Air-Gapped Backups (3-2-1-1-0 Rule):**  
   Deploy write-once-read-many (WORM) immutable cloud object storage (AWS S3 Object Lock in Compliance Mode) and offline air-gapped tape/disk archives.
4. **Endpoint Detection and Response (EDR) & Script Hardening:**  
   Deploy behavior-based EDR agents capable of intercepting anomalous `vssadmin` executions, disabling PowerShell Constrained Language Mode, and enforcing AppLocker script-whitelisting.
5. **Vulnerability & Patch Management:**  
   Immediately remediate local privilege escalation vulnerabilities (e.g., CVE-2024-30088) across all workstation endpoints.

---

## 8. INVESTIGATOR SIGN-OFF & CERTIFICATION

I, **Swaraj Bhattacharjee**, hereby declare on solemn affirmation that the contents of this digital forensic report are true and correct to the best of my scientific knowledge, training, and examination of the seized physical and electronic evidence. The integrity of all master forensic evidence has remained uncompromised throughout this investigation.

**Examiner Signature:**  
*Swaraj Bhattacharjee*  
**Name:** Swaraj Bhattacharjee  
**Roll No:** 2301730011  
**Program:** B.Tech CSE (AI & ML), Section A  
**Date:** 17 November 2026  
**Place:** Cyber Crime Investigation Cell, Kolkata, India  
