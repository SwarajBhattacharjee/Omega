# Forensic Attack Timeline & Multi-Source Event Correlation
**Case Name:** Case Omega – Investigating a Ransomware Attack on a Healthcare Network  
**Target:** St. Jude Hospital / Omega Regional Health Network  
**Investigator:** Swaraj Bhattacharjee (Roll No: 2301730011, B.Tech CSE AI ML, Sec A)  
**Time Standard:** Indian Standard Time (IST, UTC+5:30)  

---

## 1. Visual Kill Chain Chronology

```
[02:35:10 IST] ──> Operational Staff Logon (WS-NURSE-04)
        │
[02:42:10 IST] ──> Initial Access: Rogue USB Inserted (SanDisk Ultra 32GB, EVD-OMEGA-002)
        │
[02:43:05 IST] ──> Execution: Weaponized LNK -> Base64 Obfuscated PowerShell Dropper
        │
[02:45:18 IST] ──> Privilege Escalation: Kernel Exploit CVE-2024-30088 -> NT AUTHORITY\SYSTEM
        │
[02:50:30 IST] ──> Lateral Movement: Harvested Admin Tokens -> SMB (Port 445) PsExec to OMEGA-SRV-01
        │
[02:53:14 IST] ──> Persistence: Rogue Windows Service 'OmegaSvc' & Registry Run Keys Installed
        │
[02:55:00 IST] ──> Command & Control: TLS 1.3 Outbound Beaconing to 185.220.101.45:443
        │
[03:00:22 IST] ──> Defense Evasion: Shadow Copies Purged via 'vssadmin delete shadows /all /quiet'
        │
[03:02:11 IST] ──> Impact: Multithreaded AES-256 Encryption of EHR SQL DB & 42,000 Patient Records
        │
[03:30:00 IST] ──> First Responder Intervention: Swaraj Bhattacharjee enacts VLAN 999 Quarantine
```

---

## 2. Chronological Multi-Source Correlation Matrix

| Timestamp (IST) | Host Affected | Log Source & Event ID | MITRE ATT&CK Phase | Correlated Forensic Observation |
|---|---|---|---|---|
| **02:35:10** | `WS-NURSE-04` | Windows Security (4624) | Pre-Incident Baseline | Legitimate interactive desktop login by nurse on duty (`nurse_on_duty`). |
| **02:42:10** | `WS-NURSE-04` | USBSTOR / UMDF (2003, 10000) | Initial Access (`T1200`) | Physical insertion of SanDisk Ultra 32GB (`SDCZ48-449102-K9`) assigned drive letter `E:`. |
| **02:42:14** | `WS-NURSE-04` | Windows Security (4663) | Initial Access (`T1200`) | User accessed file `E:\PATIENT_TRANSFER_REPORT.docx.lnk`. |
| **02:43:02** | `WS-NURSE-04` | Windows Security (4688) | Execution (`T1204.002`) | User clicked malicious shortcut, invoking `cmd.exe`. |
| **02:43:05** | `WS-NURSE-04` | Windows Security (4688) | Execution (`T1059.003`) | Hidden execution of `powershell.exe -ExecutionPolicy Bypass -Enc aQB3...`. |
| **02:43:06** | Perimeter FW | FortiGate 200F (HTTPS) | Command & Control (`T1071`) | Outbound TCP 443 handshake to untrusted Tor exit IP `185.220.101.45`. |
| **02:43:08** | `WS-NURSE-04` | Sysmon Event 1 | Execution (`T1204`) | Process creation: `C:\ProgramData\omega_dropper.exe`. |
| **02:45:18** | `WS-NURSE-04` | Windows Security (4672) | Privilege Escalation (`T1068`)| Exploitation of local kernel flaw elevating session to `NT AUTHORITY\SYSTEM`. |
| **02:50:30** | `OMEGA-SRV-01`| Windows Security (4624) | Lateral Movement (`T1021.002`)| Network logon (Type 3) from `192.168.10.45` over SMB (Port 445). |
| **02:51:00** | `OMEGA-SRV-01`| Service Control (7045) | Lateral Movement (`T1021`) | Remote execution tool `PSEXESVC` installed. |
| **02:53:14** | `OMEGA-SRV-01`| Service Control (7045) | Persistence (`T1547.001`) | Installation of auto-start service `OmegaSvc` pointing to `omega_payload.exe`. |
| **02:54:10** | `OMEGA-SRV-01`| Sysmon Event 1 | Execution (`T1059`) | Process launch: `omega_payload.exe --encrypt-all`. |
| **02:54:35** | `OMEGA-SRV-01`| Sysmon Event 13 | Persistence (`T1547.001`) | Registry key set: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\OmegaHealthUpdate`. |
| **02:55:00** | `OMEGA-SRV-01`| Sysmon Event 3 | Command & Control (`T1071`) | High-volume TLS socket to `185.220.101.45:443`. |
| **03:00:22** | `OMEGA-SRV-01`| Windows Security (4688) | Defense Evasion (`T1490`) | Execution: `vssadmin.exe delete shadows /all /quiet`. |
| **03:01:05** | `OMEGA-SRV-01`| Windows Security (4688) | Defense Evasion (`T1490`) | Execution: `bcdedit.exe /set recoveryenabled no`. |
| **03:02:11** | `OMEGA-SRV-01`| Sysmon Event 11 | Impact (`T1486`) | Mass file encryption: `PATIENT_RECORDS_2026.MDF.omega`. |
| **03:02:15** | `OMEGA-SRV-01`| Sysmon Event 11 | Impact (`T1486`) | Ransom note dropped: `README_RECOVERY_KEY.txt`. |
| **03:10:44** | Perimeter FW | FortiGate IPS (IPS Alert) | Detection | Signature `Ransomware.OmegaLocker.C2.Beacon` triggered; traffic dropped. |
| **03:30:00** | Perimeter FW | Management Audit Log | Incident Response | First Responder **Swaraj Bhattacharjee** initiates VLAN 999 isolation and preserves physical scene. |

---

## 3. Visual Artifact Reference
The visual timeline plot has been compiled and saved to [attack_timeline_chart.png](file:///c:/Users/Swaraj%20Bhattacharjee/Desktop/College/Notes/Sem%207/Project%20Omega/04_timeline_and_correlation/attack_timeline_chart.png). Raw event correlation data is stored in [attack_timeline.csv](file:///c:/Users/Swaraj%20Bhattacharjee/Desktop/College/Notes/Sem%207/Project%20Omega/04_timeline_and_correlation/attack_timeline.csv).
