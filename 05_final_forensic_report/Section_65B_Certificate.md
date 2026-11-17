# CERTIFICATE UNDER SECTION 65B OF THE INDIAN EVIDENCE ACT, 1872
### (Corresponding to Section 63 of Bharatiya Sakshya Adhiniyam, 2023)
**Case Title:** State / Central Bureau of Investigation vs. Unknown Cyber Threat Actors (OmegaLocker Syndicate)  
**FIR Reference:** FIR-CCPS-2026-0814  
**Date of Certification:** 17 November 2026  
**Certifying Examiner:** Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML, Sec A)  

---

## 1. STATEMENT OF CERTIFYING AUTHORITY
I, **Swaraj Bhattacharjee**, son/daughter of reputable citizen, residing in Kolkata, West Bengal, holding the academic qualification of Bachelor of Technology in Computer Science and Engineering (Artificial Intelligence and Machine Learning), Roll No: **2301730011**, Section A, acting in the official capacity of Lead Digital Forensic Examiner for **Case Omega**, do hereby depose, certify, and state on solemn affirmation as under:

1. That I have lawful control and management of the forensic imaging workstations, forensic write-blockers, and digital acquisition devices utilized during the digital forensic triage and seizure of electronic records at St. Jude Hospital / Omega Regional Health Network on 17 November 2026.
2. That the electronic records described herein were produced by computer systems, hard drives, and forensic capture interfaces during the period over which the said systems were used regularly to store, process, and extract digital evidence.
3. That throughout the material part of the said period, the computer devices and write-blocking hardware were operating properly, and there were no operational defects, malware corruption, or malfunctions that could alter the electronic records or compromise their cryptographic integrity.
4. That the digital outputs (bit-stream disk images, volatile memory snapshots, event log extractions) are exact, faithful, bit-for-bit mathematical duplicates of the electronic information resident upon the seized source computers.

---

## 2. SCHEDULE OF ELECTRONIC RECORDS

| Item Reference | Physical Source Device | Electronic Record Description | Tool Utilized | Cryptographic SHA-256 Checksum |
|---|---|---|---|---|
| **EVD-OMEGA-001** | Dell PowerEdge R750 Server (S/N: `DELL-R750-OMEGA99`) | Raw Bit-Stream Disk Image (`server_ehr_partition.raw`, 1,048,576 Bytes) | `dc3dd` v7.2 via Tableau T8u Hardware Bridge | `29f29a9471a107cd05623ac0333b68c43c71e5350cbd851f8be51529341f4400` |
| **EVD-OMEGA-002** | SanDisk Ultra 32GB USB Flash Drive (S/N: `SDCZ48-449102-K9`) | Initial Access Dropper & Shortcut File (`omega_payload.exe` sample) | Forensic Read-Only USB Bridge | `a1b2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0` |
| **EVD-OMEGA-003** | Dell PowerEdge R750 Server | Volatile Physical RAM Image (`memory_dump_sample.raw`, 524,288 Bytes) | WinPmem Kernel Driver v4.0 | `444cf39fb88b1c3badde2790f88cf229b853c393dd5f60518ccab52080050282` |
| **EVD-OMEGA-004** | FortiGate 200F Perimeter Firewall | Unified Syslog Network Stream & IPS Alert Records | Signed Syslog Forwarder | GPG Signed Stream Archive |

---

## 3. ADMISSIBILITY COMPLIANCE (APEX COURT JURISPRUDENCE)
This certificate is executed in strict adherence to the binding legal precedents established by the Hon'ble Supreme Court of India in:
- ***Anvar P.V. v. P.K. Basheer & Ors. (2014) 10 SCC 473***
- ***Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 7 SCC 1***

The electronic devices were secured under an unbroken Chain of Custody (CoC) and protected against any post-incident tampering by application of hardware write-blockers and dual-layer cryptographic verification (MD5 and SHA-256).

---

## 4. VERIFICATION & ATTESTATION
I hereby affirm that the statements made above are true and correct to the best of my knowledge, belief, and scientific evaluation. Nothing material has been concealed or omitted.

**Deponent / Forensic Examiner:**  
*Swaraj Bhattacharjee*  
**Name:** Swaraj Bhattacharjee  
**Roll No:** 2301730011  
**Program:** B.Tech CSE AI ML (Sec A)  
**Executed at:** Kolkata, West Bengal  
**Date:** 17 November 2026  
