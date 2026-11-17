# Standard Operating Procedure (SOP): Digital Forensics First Responder (DFIR)
**Document Ref:** SOP-DFIR-2026-OMEGA  
**Target Organization:** Omega Regional Health Network / St. Jude Memorial Healthcare System  
**Classification:** Incident Response & Law Enforcement Ready (Confidential)  
**Standard Compliance:** NIST SP 800-61 Rev. 2, ISO/IEC 27037:2012, CERT-In Cyber Incident Guidelines  
**Investigator / First Responder:** Swaraj Bhattacharjee (Roll No: 2301730011, B.Tech CSE AI ML, Sec A)  

---

## 1. Purpose & Scope
This Standard Operating Procedure (SOP) governs the tactical and forensic response actions mandated for Digital Evidence First Responders (DEFR) during an active or suspected ransomware outbreak impacting critical healthcare infrastructure, specifically Electronic Health Record (EHR) databases, Picture Archiving and Communication System (PACS) servers, and administrative clinical endpoints.

---

## 2. Order of Volatility (RFC 3227 & ISO 27037)
Evidence must be triaged and preserved strictly in descending order of volatility:
1. **CPU Registers, Cache, and Process Tables**
2. **System RAM (Main Physical Memory)** (Running processes, injected DLLs, unencrypted symmetric keys, active C2 sockets)
3. **Network State & Ephemeral Sockets** (`netstat -ano`, ARP cache, active TLS/SSH tunnels)
4. **Temporary File Systems & Swap/Pagefile** (`pagefile.sys`, `swapfile.sys`, `/tmp`)
5. **Non-Volatile Disk Storage** (HDD/SSD raw sector contents, master boot records, NTFS journal `$MFT`, `$LogFile`)
6. **Remote Logs & SIEM Feeds** (Firewall, Active Directory Domain Controllers, IDS/IPS alerts)
7. **Physical Evidence & Peripheral Media** (Inserted USB flash drives, network drops, physical server rack cabling)

---

## 3. Step-by-Step First Responder Protocol

```
+-----------------------------------------------------------------------------------+
|                            PHASE 1: INITIAL TRIAGE & SAFETY                      |
|  - Verify human life-safety (ICU telemetry, ventilators, infusion pumps priority) |
|  - Validate scope of ransomware propagation (file extension: .omega)              |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                        PHASE 2: ISOLATION WITHOUT POWER LOSS                     |
|  - DO NOT POWER OFF OR REBOOT HOSTS (Prevents loss of AES keys in RAM)            |
|  - Sever Physical Network (Disconnect RJ-45) & Disable Wireless (Wi-Fi / BT)      |
|  - Isolate VLAN at core switch level to contain lateral movement (SMB/PsExec)     |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       PHASE 3: VOLATILE MEMORY CAPTURE                           |
|  - Insert write-blocked forensic response drive (Drive E: /dev/sdb)               |
|  - Execute trusted standalone capture tool (e.g., WinPmem / LiME / DumpIt)        |
|  - Store RAM dump with timestamped SHA-256 integrity hash                         |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       PHASE 4: CRIME SCENE PHYSICAL DOCUMENTATION                |
|  - 360-degree photography (room, screen state, cables, connected USB/peripherals) |
|  - Sketch crime scene topology & label physical asset serial numbers              |
|  - Affix tamper-evident physical forensic tags                                    |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       PHASE 5: DEAD/STATIC DISK FORENSIC ACQUISITION             |
|  - Clean shutdown or hard-cut (pull power plug only if RAM already captured)     |
|  - Remove drive -> connect to hardware write blocker (Tableau / CRU WiebeTech)    |
|  - Perform bit-stream disk image (E01 or Raw DD) using FTK Imager / dc3dd         |
|  - Calculate pre- and post-acquisition SHA-256 hashes                            |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       PHASE 6: CHAIN OF CUSTODY & LEGAL HANDOFF                  |
|  - Package drives in anti-static Faraday bags with tamper-evident security tape   |
|  - Fill Chain of Custody form with signatures, timestamps, and hash receipts      |
|  - Section 65B (IEA) / Section 63 (BSA) electronic certificate preparation        |
+-----------------------------------------------------------------------------------+
```

### Detailed Operational Execution

#### Phase 1: Human Safety & Critical System Triage
- In healthcare facilities, medical devices (ventilators, hemodialysis monitors) take precedence over IT preservation. Verify whether any life-support equipment is networked to infected subnets.
- Coordinate with Hospital Clinical Engineering (Bio-Med) to transition critical patients to isolated analog monitoring if telemetry networks are compromised.

#### Phase 2: Containment & Isolation
- **Rule 1 (Golden Rule): Never power down or reboot a ransomware-infected host.** Rebooting flushes the volatility stack, destroys the in-memory master encryption key, and may trigger aggressive boot-sector overwrite payloads (e.g., Petya-style MBR wipers).
- **Physical Isolation:** Unplug RJ-45 Ethernet cables from the compromised Windows Server 2022 (`OMEGA-SRV-01`) and clinical nurse station terminals.
- **Wireless Isolation:** Turn off Wi-Fi toggles or disable antennas.
- **Switch-Level VLAN Quarantine:** Instruct Network Operations (NOC) to place Port `Gi1/0/14` into an isolated "Black Hole" VLAN (VLAN 999) to kill inbound/outbound TCP 445 (SMB) and TCP 3389 (RDP) traffic.

#### Phase 3: Volatile Memory Capture
- Attach an authenticated, forensically sterile external USB flash drive containing pre-compiled, static binaries:
  ```powershell
  # Example Volatile Memory Dump via WinPmem
  E:\tools\winpmem.exe -o E:\evidence\OMEGA_SRV01_RAM_20261117.raw --volume_mode 2
  ```
- Collect ephemeral network and process states:
  ```powershell
  E:\tools\netstat.exe -ano > E:\evidence\volatile_netstat.txt
  E:\tools\tasklist.exe /v > E:\evidence\volatile_processes.txt
  ```

#### Phase 4: Scene Documentation & Tagging
- Photograph the active screen showing the ransom note (`README_RECOVERY_KEY.txt`).
- Record the exact system clock time and compare with UTC / NTP atomic reference to establish Clock Skew delta ($\Delta t$).
- Affix tamper-evident barcode tags to the chassis, ports, and external peripherals.

#### Phase 5: Bit-Stream Disk Imaging
- Once volatile memory is secured, perform a hard power severance (pull power cord from PSU) if live imaging is prohibited, or perform live logical triage with FTK Imager Lite / `dc3dd`.
- Attach source disk to a write-blocker (Hardware Write Blocker: Tableau T8u Forensic USB 3.0 Bridge).
- Generate a bit-by-bit Raw Image (`.dd` / `.raw`) or Expert Witness Format (`.E01`).

#### Phase 6: Legal Preservation & Chain of Custody
- Complete the Evidence Transfer Form and Chain of Custody Log (adhering to Section 65B Indian Evidence Act / Section 63 Bharatiya Sakshya Adhiniyam).
- Secure media in locked, anti-static, climate-controlled Faraday bags ($18^\circ\text{C} - 22^\circ\text{C}$, $<40\%$ RH).

---

## 4. First Responder Equipment Checklist (Forensic Jump Kit)
1. **Hardware Write-Blockers:** Tableau T8u (USB), T35u (SATA/IDE), UltraBay 4.
2. **Forensic Storage Media:** Certified sanitized external NVMe drives (DoD 5220.22-M wiped).
3. **Forensic Acquisition Software:** FTK Imager Lite (USB portable), `dc3dd`, WinPmem, Volatility 3 standalone.
4. **Physical Supplies:** Anti-static ESD Faraday bags, tamper-evident security tape, evidence tags/labels, indelible forensic markers.
5. **Documentation Tools:** DSLR camera / secure smartphone camera (EXIF preserved), laser range finder, forensic field log notebook.
