# Crime Scene Documentation & First Responder Log
**Case Reference:** Case Omega – Healthcare Cyber Attack Investigation  
**Incident Location:** Omega Regional Health Network, Sector 5, Salt Lake, Kolkata, West Bengal, India  
**Date & Time of Response:** 17 November 2026, 03:45 AM IST  
**First Responder:** Swaraj Bhattacharjee (Roll No: 2301730011, B.Tech CSE AI ML, Sec A)  
**Accompanying Security Personnel:** Inspector R. Mukherjee (Cyber Crime Investigation Cell), Dr. A. Sen (Hospital Superintendent)  

---

## 1. Initial Scene Arrival & Ambient Conditions
- **Arrival Time:** 03:45:12 AM IST.
- **Scene Security:** Server Room B204 secured by digital badge access lock (badge logs preserved).
- **Physical Environment:** Server room ambient temperature at $19.4^\circ\text{C}$, humidity $38\%$. No physical signs of forced entry.
- **Nurse Station Terminal 04:** Located in Emergency Triage Ward. Screen was active and displayed a red modal desktop wallpaper and Notepad window titled `README_RECOVERY_KEY.txt`.
- **Primary EHR Server (OMEGA-SRV-01):** Dell PowerEdge rack server fan speeds were running at $95\%$ utilization; drive activity LEDs were blinking continuously.

---

## 2. Photographic & Visual Log

| Photo Reference | Subject / Viewpoint | Findings & Forensic Relevance |
|---|---|---|
| **IMG_OMEGA_001.JPG** | Nurse Station WS-NURSE-04 Monitor | Shows desktop locked by ransom note titled `OMEGA LOCKER v4.2`. Extension of patient files renamed to `.omega`. |
| **IMG_OMEGA_002.JPG** | Front USB Port of WS-NURSE-04 | SanDisk 32GB USB flash drive inserted. Flashing red access indicator light. Device labeled `PATIENT_RECORDS_BACKUP_2026`. |
| **IMG_OMEGA_003.JPG** | Server Room B204 - Rack 02 | Dell PowerEdge R750 server running OMEGA EHR SQL Database. Network cables connected to Switch Port 14. |
| **IMG_OMEGA_004.JPG** | Cisco Core Switch 9300 Panel | Port 14 LED flashing at high frequency indicating lateral SMB scanning traffic. |
| **IMG_OMEGA_005.JPG** | Tamper Evident Seals Applied | Barcode seal `#SEC-OMEGA-9901` placed across USB drive slot and chassis cover of seized terminals. |

---

## 3. Clock Skew Calibration
Digital evidence timestamps must be calibrated against UTC / National Physical Laboratory (NPL) atomic time:
- **Reference Atomic Time (UTC+5:30):** 03:52:00.000 AM IST
- **Target Server System Clock (OMEGA-SRV-01):** 03:51:48.250 AM IST
- **Clock Drift ($\Delta t$):** Target clock is running **11.75 seconds slow**.
- **Correction Rule:** Add $+11.75$ seconds to all raw timestamps extracted from `OMEGA-SRV-01` event logs.

---

## 4. Crime Scene Topology Walkthrough
The attack originated at **Nurse Station Terminal 04 (WS-NURSE-04)** in the Emergency Ward, where a malicious physical USB flash drive was inserted under the guise of an external patient transfer report. Upon insertion, an obfuscated script executed, established persistence, performed credential harvesting, and pivoted over SMB (port 445) to the **Core EHR Server (OMEGA-SRV-01)** in Server Room B204.

*(See generated scene sketch diagram `scene_sketch_topology.svg` and `scene_sketch_topology.png` for complete topological and spatial layout).*
