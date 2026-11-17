# Digital & Physical Evidence Inventory Matrix
**Case Designation:** Case Omega – Cyber Crime Investigation  
**Incident:** Ransomware Incident at Omega Regional Health Network (St. Jude Medical Center)  
**Primary Investigator:** Swaraj Bhattacharjee (Roll No: 2301730011, B.Tech CSE AI ML, Sec A)  
**Date of Seizure:** 17 November 2026  
**Location:** Server Room B204 & Nurse Station Terminal 04, Omega Hospital, Sector 5, Kolkata  

---

## 1. Digital & Physical Evidence Log

| Item Tag ID | Item Description | Make / Model / Serial No. | Evidence Classification | Seized From / Location | MAC Address / Capacity | Initial State | Primary Hash (SHA-256) |
|---|---|---|---|---|---|---|---|
| **EVD-OMEGA-001** | Primary EHR Application & Database Server | Dell PowerEdge R750<br>S/N: `DELL-R750-OMEGA99` | Digital / Critical Infrastructure | Server Rack 02, Unit 12-14, Server Room B204 | `00:1A:2B:3C:4D:5E`<br>2x 2TB NVMe RAID-1 | Powered ON (Ransom screen displayed) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (See image manifest) |
| **EVD-OMEGA-002** | SanDisk Ultra 32GB USB 3.0 Flash Drive (Rogue Device) | SanDisk Ultra SDCZ48-032G<br>S/N: `SDCZ48-449102-K9` | Physical / Hardware Media | Plugged into Front USB Port 1 of Workstation WS-NURSE-04 | 32 GB Flash Storage | Inserted into running machine | `a1b2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0` (Payload sample) |
| **EVD-OMEGA-003** | Clinical Workstation (Patient Registration Terminal) | HP EliteDesk 800 G6<br>S/N: `HP-ED800-NURSE04` | Digital / Patient Intake Endpoint | Nurse Station Desk 04, Emergency Ward | `70:85:C2:55:01:A4`<br>512GB PCIe M.2 SSD | Locked (Screen showed `.omega` ransom demand) | `f4e3d2c1b0a9876543210fedcba9876543210fedcba9876543210fedcba98765` |
| **EVD-OMEGA-004** | Core Network Perimeter Firewall Appliance | Fortinet FortiGate 200F<br>S/N: `FG200F-KOL-7881` | Digital / Network Telemetry | Network Rack 01, Server Room B204 | `F4:F2:6D:88:91:20`<br>128GB Flash Log Storage | Powered ON (Active packet capture enabled) | Preserved via Syslog forwarding & signed snapshot |
| **EVD-OMEGA-005** | Core Distribution Switch | Cisco Catalyst 9300 48-Port<br>S/N: `CAT9300-48P-992` | Digital / Network Infrastructure | Network Rack 01, Port Gi1/0/14 isolated | `00:27:10:AA:BB:CC` | Isolated via VLAN Quarantine | Memory config dumped (`show running-config`) |
| **EVD-OMEGA-006** | Cloud EHR Gateway & PACS Access Point Logs | AWS EC2 / VPC Endpoint Logs<br>Instance ID: `i-0994a3bcde890f12` | Cloud Telemetry / Electronic Records | AWS Asia-Pacific (Mumbai) `ap-south-1` | Cloud Virtual Instance | Active CloudWatch log stream captured | Signed SHA-256 cloud trail archive |

---

## 2. Digital Evidence Categories & Forensic Value

1. **Host-Based Volatile Memory (`.raw` / `.vmem`):**
   - High value: Extracts decrypted symmetric master keys, injected memory threads, uncompiled script remnants, and active C2 sockets.
2. **Raw Physical Disk Images (`.raw` / `.dd` / `.E01`):**
   - High value: Preserves NTFS Master File Table (`$MFT`), Volume Shadow Copies (`VSS`), Prefetch files (`.pf`), Amcache, and Shimcache for timestamp reconstruction.
3. **Peripheral Storage Media (Rogue USB Drive):**
   - Critical value: Source of initial physical payload drop (Patient Intake malicious file execution vector). Contains dropper scripts and weaponized shortcuts (`.lnk`).
4. **Network Telemetry & Perimeter Logs:**
   - Essential value: Correlates outbound Command & Control (C2) beaconing, data exfiltration volume spikes prior to encryption, and lateral SMB scanning activity.
5. **Cloud Audit & Access Logs:**
   - Preserves API calls to healthcare cloud repositories, verifying whether medical records were staged or exfiltrated externally.

---

## 3. Physical Tagging and Packaging Standard
- All seized physical hardware items were labeled with tamper-evident, barcoded forensic evidence tags.
- Sealing tape applied over all screw joints, drive trays, and peripheral ports.
- Signed by First Responder **Swaraj Bhattacharjee** and witness **Dr. A. Sen, Chief Medical Officer (Omega Hospital)**.
