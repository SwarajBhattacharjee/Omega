#!/usr/bin/env python3
"""
Forensic Timeline Correlation & Multi-Source Log Aggregator
Case: Case Omega - Healthcare Cyber Attack Investigation
Investigator: Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML)
"""

import os
import csv
import re
from datetime import datetime

LOGS_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
OUTPUT_CSV = os.path.join(os.path.dirname(__file__), "..", "attack_timeline.csv")

def parse_logs():
    events = []

    # 1. Parse Windows Security Logs
    sec_log = os.path.join(LOGS_DIR, "windows_security_auth.log")
    if os.path.exists(sec_log):
        with open(sec_log, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) IST \| EventID: (\d+) \| Source: ([^|]+) \| Computer: ([^|]+) \| (.*)$", line)
                if match:
                    ts, eid, src, comp, rest = match.groups()
                    events.append({
                        "timestamp": ts,
                        "source": "Windows Security Event Log",
                        "host": comp.strip(),
                        "event_id": eid.strip(),
                        "category": "Authentication / Process Execution",
                        "details": rest.strip(),
                        "attack_stage": classify_stage(rest)
                    })

    # 2. Parse Sysmon Logs
    sysmon_log = os.path.join(LOGS_DIR, "sysmon_events.log")
    if os.path.exists(sysmon_log):
        with open(sysmon_log, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) IST \| SysmonID: (\d+ [^|]+) \| Computer: ([^|]+) \| (.*)$", line)
                if match:
                    ts, sid, comp, rest = match.groups()
                    events.append({
                        "timestamp": ts,
                        "source": "Microsoft Sysmon",
                        "host": comp.strip(),
                        "event_id": f"Sysmon-{sid.split()[0]}",
                        "category": "Deep Process & Telemetry",
                        "details": rest.strip(),
                        "attack_stage": classify_stage(rest)
                    })

    # 3. Parse USB Device Logs
    usb_log = os.path.join(LOGS_DIR, "usb_device_mount.log")
    if os.path.exists(usb_log):
        with open(usb_log, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) IST \| EventID: (\d+) \| Source: ([^|]+) \| Computer: ([^|]+) \| (.*)$", line)
                if match:
                    ts, eid, src, comp, rest = match.groups()
                    events.append({
                        "timestamp": ts,
                        "source": "USBSTOR / DriverFrameworks",
                        "host": comp.strip(),
                        "event_id": f"USB-{eid}",
                        "category": "Hardware Peripheral Insertion",
                        "details": rest.strip(),
                        "attack_stage": "Initial Access (T1200)"
                    })

    # 4. Parse Firewall Logs
    fw_log = os.path.join(LOGS_DIR, "firewall_traffic.log")
    if os.path.exists(fw_log):
        with open(fw_log, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                # date=2026-11-17 time=02:43:06 devname="FG200F-KOL-7881" ...
                m_date = re.search(r'date=(\S+)', line)
                m_time = re.search(r'time=(\S+)', line)
                m_msg = re.search(r'msg="([^"]+)"', line)
                m_src = re.search(r'srcip=(\S+)', line)
                m_dst = re.search(r'dstip=(\S+)', line)
                if m_date and m_time:
                    ts = f"{m_date.group(1)} {m_time.group(1)}"
                    msg = m_msg.group(1) if m_msg else line
                    src_ip = m_src.group(1) if m_src else "Unknown"
                    dst_ip = m_dst.group(1) if m_dst else "Unknown"
                    events.append({
                        "timestamp": ts,
                        "source": "FortiGate 200F Firewall",
                        "host": f"Perimeter Gateway (Src: {src_ip})",
                        "event_id": "FW-TRAFFIC",
                        "category": "Network Traffic / C2 Beaconing",
                        "details": f"{msg} | Connection {src_ip} -> {dst_ip}",
                        "attack_stage": "Command & Control / Exfiltration (T1071)"
                    })

    # Sort all events chronologically
    events.sort(key=lambda x: x["timestamp"])
    return events

def classify_stage(text):
    t = text.lower()
    if "usb" in t or "volume" in t:
        return "Initial Access (T1200)"
    if "shortcut" in t or "explorer" in t or "powershell" in t:
        return "Execution (T1204 / T1059)"
    if "special privileges" in t or "privilege" in t or "cve" in t:
        return "Privilege Escalation (T1068)"
    if "psexec" in t or "4624" in t or "network logon" in t:
        return "Lateral Movement (T1021)"
    if "omegasvc" in t or "registryvalueset" in t or "run" in t:
        return "Persistence (T1547 / T1053)"
    if "vssadmin" in t or "bcdedit" in t or "delete shadows" in t:
        return "Defense Evasion (T1490)"
    if "destinationip: 185.220.101.45" in t or "outbound" in t:
        return "Command & Control (T1071)"
    if ".omega" in t or "encrypt" in t or "recovery_key" in t:
        return "Impact (T1486)"
    return "Operational Telemetry"

def export_timeline():
    print("=" * 70)
    print("  FORENSIC LOG CORRELATION & ATTACK TIMELINE ENGINE")
    print("  Investigator: Swaraj Bhattacharjee (Roll: 2301730011)")
    print("=" * 70)

    events = parse_logs()
    print(f"[*] Correlated {len(events)} events across Windows, Sysmon, USB, and Firewall logs.")

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["timestamp", "attack_stage", "source", "host", "event_id", "category", "details"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for ev in events:
            writer.writerow(ev)

    print(f"[+] Attack timeline successfully written to: {OUTPUT_CSV}")
    print("\n--- Summary of Attack Milestones ---")
    stages = set()
    for ev in events:
        if ev["attack_stage"] not in stages:
            print(f"[{ev['timestamp']} IST] -> {ev['attack_stage']} on {ev['host']}")
            stages.add(ev["attack_stage"])

    print("=" * 70)

if __name__ == "__main__":
    export_timeline()
