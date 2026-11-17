#!/usr/bin/env python3
"""
Forensic Timeline Visualizer (Attack Chronology & Kill Chain Plot)
Case: Case Omega - Cyber Crime Investigation
Investigator: Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML)
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "attack_timeline.csv")
OUTPUT_PNG = os.path.join(os.path.dirname(__file__), "..", "attack_timeline_chart.png")

def plot_timeline():
    # Filter key forensic milestones
    milestones = [
        ("02:35:10", "Nurse Interactive Logon\n(WS-NURSE-04)", "Operational", "#3b82f6"),
        ("02:42:10", "Rogue USB Insertion\n(SanDisk Ultra EVD-002)", "Initial Access\n(T1200)", "#ef4444"),
        ("02:43:05", "PowerShell Dropper Executed\n(Base64 Obfuscated)", "Execution\n(T1059)", "#f97316"),
        ("02:45:18", "Privilege Escalation to SYSTEM\n(CVE-2024-30088)", "Priv Escalation\n(T1068)", "#eab308"),
        ("02:50:30", "Lateral SMB Pivot to Server\n(PsExec to OMEGA-SRV-01)", "Lateral Movement\n(T1021)", "#a855f7"),
        ("02:53:14", "Ransomware Service Installed\n(OmegaSvc / Registry Run)", "Persistence\n(T1547)", "#ec4899"),
        ("02:55:00", "C2 Outbound Beacon\n(185.220.101.45:443)", "Command & Control\n(T1071)", "#06b6d4"),
        ("03:00:22", "Shadow Copies Purged\n(vssadmin delete shadows)", "Defense Evasion\n(T1490)", "#e11d48"),
        ("03:02:11", "EHR Database Encrypted\n(42,000 Patient Records .omega)", "Impact\n(T1486)", "#dc2626"),
        ("03:30:00", "First Responder Isolation\n(VLAN 999 & Physical Handoff)", "Incident Response", "#10b981")
    ]

    fig, ax = plt.subplots(figsize=(15, 8), facecolor="#0d1117")
    ax.set_facecolor("#0d1117")

    y_pos = 0
    ax.plot([0, len(milestones) - 1], [0, 0], color="#30363d", linewidth=4, zorder=1)

    for idx, (t_str, desc, stage, color) in enumerate(milestones):
        offset = 1.8 if idx % 2 == 0 else -1.8
        # Milestone node
        ax.scatter(idx, 0, color=color, s=220, edgecolors="#ffffff", linewidth=2, zorder=3)
        # Leader line
        ax.plot([idx, idx], [0, offset], color=color, linestyle="--", linewidth=1.5, zorder=2)

        # Callout box
        box_y = offset + (0.3 if offset > 0 else -0.8)
        bbox_props = dict(boxstyle="round,pad=0.5", facecolor="#161b22", edgecolor=color, linewidth=1.8)
        text_content = f"{t_str} IST\n[{stage}]\n{desc}"
        ax.text(idx, box_y, text_content, ha="center", va="center", color="#f0f6fc",
                fontsize=8.5, fontweight="bold", bbox=bbox_props)

    ax.set_xlim(-0.8, len(milestones) - 0.2)
    ax.set_ylim(-3.5, 3.5)
    ax.axis("off")

    # Title header
    ax.text(len(milestones) / 2 - 0.5, 3.2, "CASE OMEGA: ATTACK RECONSTRUCTION & FORENSIC TIMELINE",
            ha="center", va="center", color="#58a6ff", fontsize=15, fontweight="bold")
    ax.text(len(milestones) / 2 - 0.5, 2.8, "Lead Examiner: Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML, Sec A)",
            ha="center", va="center", color="#8b949e", fontsize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=200, bbox_inches="tight")
    print(f"[+] Attack timeline visualization chart generated: {OUTPUT_PNG}")

if __name__ == "__main__":
    plot_timeline()
