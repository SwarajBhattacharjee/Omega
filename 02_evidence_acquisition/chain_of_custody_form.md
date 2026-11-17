# Chain of Custody (CoC) Record
**Agency / Institution:** Cyber Forensic Division, Omega Regional Health Investigation Unit  
**Case Title:** Case Omega – Investigating Ransomware Outbreak at St. Jude Hospital  
**FIR / Incident Ref No.:** FIR-CCPS-2026-0814  
**Investigating Officer:** Swaraj Bhattacharjee  
**Designation:** Lead Digital Forensic Examiner (Roll: 2301730011, B.Tech CSE AI ML, Sec A)  
**Governing Standard:** ISO/IEC 27037:2012 / NIST SP 800-86 / Indian Evidence Act Section 65B  

---

## 1. Evidence Item Identification
- **Evidence Tag Number:** `EVD-OMEGA-001`
- **Item Description:** Bit-Stream Forensic Disk Image (`server_ehr_partition.raw`) acquired from Primary EHR Database Server (Dell PowerEdge R750, S/N: `DELL-R750-OMEGA99`).
- **Physical Media:** Enclosed within Anti-Static ESD Faraday Enclosure #F-8812.
- **Acquisition Tool Used:** dc3dd v7.2 via Tableau T8u Hardware Write Blocker.
- **Source Drive Geometry:** 2,048 Sectors (1,048,576 Bytes, Sector Size: 512 bytes).
- **Master Verification Hashes:**
  - **SHA-256:** `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400`
  - **MD5:** `d1d80e89c7543d03de415f58ea1a1f87`

---

## 2. Chain of Custody Transfer & Tracking Log

| Date & Time (IST) | Released By (Print & Sign) | Received By (Print & Sign) | Purpose of Transfer / Action Taken | Physical Storage Location & Condition | Tamper Seal Status |
|---|---|---|---|---|---|
| **17/11/2026 04:15 AM** | **Swaraj Bhattacharjee**<br>(Lead Investigator) | **Swaraj Bhattacharjee**<br>(Forensic Lab Custody) | Initial on-site forensic acquisition via write-blocker | Mobile Forensic Workstation MFW-01, Secured Case | Seal #SEC-9901 Intact |
| **17/11/2026 06:30 AM** | **Swaraj Bhattacharjee**<br>(Lead Investigator) | **Insp. R. Mukherjee**<br>(Cyber Crime PS, Kolkata) | Handoff of master raw disk image copy for legal evidence registration | Secured Evidence Locker #B4, CCPS Evidence Vault | Seal #SEC-9901 Verified & Signed |
| **17/11/2026 08:00 AM** | **Insp. R. Mukherjee**<br>(Cyber Crime PS) | **Dr. P. Roy**<br>(Senior Scientific Officer, CFSL) | Handoff to Central Forensic Science Lab for independent hash verification & analysis | CFSL Digital Evidence Safe Room (Temp: 20C, Humidity: 35%) | Seal #SEC-9901 Intact; Re-hashed match 100% |
| **17/11/2026 10:00 AM** | **Dr. P. Roy**<br>(CFSL) | **Swaraj Bhattacharjee**<br>(Forensic Analyst) | Authorization to clone working copy (Bit-Stream Image Copy 2) for malware extraction | Forensic Isolation Sandbox Lab #3 | Working clone verified; Master remains locked |

---

## 3. Hash Integrity Audit Verification
Upon each physical transfer, the receiving party re-computed the cryptographic SHA-256 hash using an isolated Linux workstation (`sha256sum /dev/sdb`):
- **Transfer 1 (Scene -> MFW):** `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400` [MATCH]
- **Transfer 2 (MFW -> CCPS Vault):** `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400` [MATCH]
- **Transfer 3 (CCPS -> CFSL):** `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400` [MATCH]

---

## 4. Attestation & Signatures
I hereby certify that the evidence detailed above was collected, acquired, packaged, sealed, and transferred in full compliance with ISO/IEC 27037 standards and Section 65B of the Indian Evidence Act. At no point was the evidence subjected to unmonitored access, write-enabled media, or network exposure.

**Lead Forensic Investigator:**  
**Name:** Swaraj Bhattacharjee  
**Roll No:** 2301730011  
**Course:** B.Tech CSE AI ML (Sec A)  
**Signature:** *Swaraj Bhattacharjee*  
**Date:** 17 November 2026  
