import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_topology_image():
    fig, ax = plt.subplots(figsize=(14, 9), facecolor="#0d1117")
    ax.set_facecolor("#0d1117")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Title box
    title_box = patches.FancyBboxPatch((2, 91), 96, 7, boxstyle="round,pad=0.5", facecolor="#161b22", edgecolor="#30363d", linewidth=2)
    ax.add_patch(title_box)
    ax.text(4, 94.5, "CASE OMEGA: FORENSIC CRIME SCENE & NETWORK TOPOLOGY", color="#58a6ff", fontsize=15, fontweight="bold", va="center")
    ax.text(68, 94.5, "First Responder: Swaraj Bhattacharjee (2301730011)", color="#8b949e", fontsize=10, va="center")

    # External WAN Zone
    wan_box = patches.FancyBboxPatch((3, 58), 28, 30, boxstyle="round,pad=0.5", facecolor="#172554", edgecolor="#3b82f6", linewidth=1.5, linestyle="--")
    ax.add_patch(wan_box)
    ax.text(5, 85, "EXTERNAL / WAN ZONE", color="#60a5fa", fontsize=11, fontweight="bold")

    # Adversary C2
    c2_box = patches.FancyBboxPatch((5, 72), 24, 10, boxstyle="round,pad=0.3", facecolor="#1e1e1e", edgecolor="#ef4444", linewidth=1.5)
    ax.add_patch(c2_box)
    ax.text(6, 78.5, "[X] Adversary C2 Server", color="#fca5a5", fontsize=10, fontweight="bold")
    ax.text(6, 75.5, "IP: 185.220.101.45 (Tor Exit)", color="#9ca3af", fontsize=8)
    ax.text(6, 73, "Domain: c2.omega-blacklock.onion", color="#ef4444", fontsize=7.5)

    # Cloud EHR Gateway
    cloud_box = patches.FancyBboxPatch((5, 60), 24, 10, boxstyle="round,pad=0.3", facecolor="#1e1e1e", edgecolor="#0ea5e9", linewidth=1.5)
    ax.add_patch(cloud_box)
    ax.text(6, 66.5, "AWS Cloud Health Gateway", color="#38bdf8", fontsize=10, fontweight="bold")
    ax.text(6, 63.5, "Region: ap-south-1 (Mumbai)", color="#9ca3af", fontsize=8)
    ax.text(6, 61, "CloudTrail / VPC Flow Logs Preserved", color="#22c55e", fontsize=7.5)

    # Perimeter Firewall
    fw_box = patches.FancyBboxPatch((37, 65), 14, 16, boxstyle="round,pad=0.5", facecolor="#1f2937", edgecolor="#f59e0b", linewidth=2)
    ax.add_patch(fw_box)
    ax.text(39, 77, "Perimeter FW", color="#fbbf24", fontsize=11, fontweight="bold")
    ax.text(39, 74, "FortiGate 200F", color="#e5e7eb", fontsize=9)
    ax.text(39, 71, "EVD-OMEGA-004", color="#9ca3af", fontsize=8)
    ax.text(39, 68, "Outbound Blocked", color="#ef4444", fontsize=8)

    # Core Switch
    sw_box = patches.FancyBboxPatch((58, 65), 14, 16, boxstyle="round,pad=0.5", facecolor="#1f2937", edgecolor="#10b981", linewidth=2)
    ax.add_patch(sw_box)
    ax.text(60, 77, "Core Switch", color="#34d399", fontsize=11, fontweight="bold")
    ax.text(60, 74, "Cisco Cat 9300", color="#e5e7eb", fontsize=9)
    ax.text(60, 71, "EVD-OMEGA-005", color="#9ca3af", fontsize=8)
    ax.text(60, 68, "Gi1/0/14 Quarantined", color="#f87171", fontsize=7.5)

    # Physical Crime Scene Container
    crime_box = patches.FancyBboxPatch((3, 4), 94, 48, boxstyle="round,pad=0.8", facecolor="#111827", edgecolor="#4b5563", linewidth=2)
    ax.add_patch(crime_box)
    ax.text(5, 49, "PHYSICAL SCENE: ST. JUDE MEDICAL CENTER (HOSPITAL LAN)", color="#e5e7eb", fontsize=12, fontweight="bold")

    # Nurse Station Ward
    nurse_room = patches.FancyBboxPatch((5, 8), 42, 38, boxstyle="round,pad=0.5", facecolor="#18181b", edgecolor="#f43f5e", linewidth=1.5)
    ax.add_patch(nurse_room)
    ax.text(7, 43, "EMERGENCY TRIAGE WARD - NURSE DESK 04", color="#fda4af", fontsize=10, fontweight="bold")

    # Nurse Workstation
    ws_box = patches.FancyBboxPatch((7, 23), 20, 16, boxstyle="round,pad=0.3", facecolor="#27272a", edgecolor="#f43f5e", linewidth=1.5)
    ax.add_patch(ws_box)
    ax.text(8.5, 35.5, "WS-NURSE-04 (Patient Desk)", color="#fecdd3", fontsize=9.5, fontweight="bold")
    ax.text(8.5, 32.5, "IP: 192.168.10.45", color="#9ca3af", fontsize=8)
    ax.text(8.5, 29.5, "HP EliteDesk 800 G6", color="#d1d5db", fontsize=8)
    ax.text(8.5, 26.5, "Status: Infected (.omega)", color="#ef4444", fontsize=8)
    ax.text(8.5, 24, "Tag: EVD-OMEGA-003", color="#9ca3af", fontsize=7.5)

    # Rogue USB Drive
    usb_box = patches.FancyBboxPatch((29, 23), 16, 16, boxstyle="round,pad=0.3", facecolor="#7f1d1d", edgecolor="#ef4444", linewidth=2)
    ax.add_patch(usb_box)
    ax.text(30.5, 35.5, "ROGUE USB (PATIENT)", color="#ffffff", fontsize=9.5, fontweight="bold")
    ax.text(30.5, 32.5, "SanDisk Ultra 32GB", color="#fecaca", fontsize=8)
    ax.text(30.5, 29.5, "Tag: EVD-OMEGA-002", color="#fee2e2", fontsize=8)
    ax.text(30.5, 26.5, "[INITIAL VECTOR]", color="#fef08a", fontsize=8, fontweight="bold")
    ax.text(30.5, 24, "Plugged Front USB 1", color="#ffffff", fontsize=7.5)

    # Server Room B204
    server_room = patches.FancyBboxPatch((50, 8), 45, 38, boxstyle="round,pad=0.5", facecolor="#18181b", edgecolor="#3b82f6", linewidth=1.5)
    ax.add_patch(server_room)
    ax.text(52, 43, "RESTRICTED SERVER ROOM B204", color="#bfdbfe", fontsize=10, fontweight="bold")

    # Primary EHR Server
    srv_box = patches.FancyBboxPatch((52, 21), 22, 19, boxstyle="round,pad=0.4", facecolor="#27272a", edgecolor="#ef4444", linewidth=2)
    ax.add_patch(srv_box)
    ax.text(53.5, 36.5, "OMEGA-SRV-01 (EHR DB)", color="#ef4444", fontsize=10.5, fontweight="bold")
    ax.text(53.5, 33.5, "Dell PowerEdge R750", color="#d1d5db", fontsize=8.5)
    ax.text(53.5, 30.5, "IP: 192.168.10.100", color="#9ca3af", fontsize=8)
    ax.text(53.5, 27.5, "Port 445 Compromised", color="#f87171", fontsize=8)
    ax.text(53.5, 24.5, "42,000 Records Encrypted", color="#f87171", fontsize=8)
    ax.text(53.5, 22, "Tag: EVD-OMEGA-001", color="#fbbf24", fontsize=7.5)

    # Forensic Station
    forensic_box = patches.FancyBboxPatch((76, 21), 17, 19, boxstyle="round,pad=0.4", facecolor="#27272a", edgecolor="#10b981", linewidth=1.5)
    ax.add_patch(forensic_box)
    ax.text(77.5, 36.5, "Forensic Jump Kit", color="#34d399", fontsize=9.5, fontweight="bold")
    ax.text(77.5, 33.5, "Tableau T8u Bridge", color="#d1d5db", fontsize=8)
    ax.text(77.5, 30.5, "FTK Imager / dc3dd", color="#9ca3af", fontsize=8)
    ax.text(77.5, 27.5, "Memory Dump Secured", color="#38bdf8", fontsize=8)
    ax.text(77.5, 24.5, "SHA-256 Validated", color="#10b981", fontsize=8)
    ax.text(77.5, 22, "Faraday Packaged", color="#e5e7eb", fontsize=7.5)

    # Connections & Attack Vectors
    # 1. USB -> Workstation
    ax.annotate("", xy=(27, 31), xytext=(29, 31), arrowprops=dict(arrowstyle="->", color="#ef4444", lw=2.5))
    # 2. Workstation -> Switch
    ax.plot([17, 17, 65, 65], [39, 52, 52, 65], color="#f43f5e", linestyle="--", linewidth=2)
    ax.text(26, 53.5, "Lateral SMB Pivot (Port 445 / PsExec)", color="#f43f5e", fontsize=8.5, fontweight="bold")
    # 3. Switch -> Server
    ax.plot([65, 63, 63], [65, 52, 40], color="#ef4444", linewidth=2.5)
    ax.text(64, 46, "Target Infiltration", color="#ef4444", fontsize=8.5, fontweight="bold")
    # 4. Switch -> FW
    ax.plot([58, 51], [73, 73], color="#10b981", linewidth=2)
    # 5. FW -> C2
    ax.plot([37, 29], [73, 73], color="#ef4444", linestyle="--", linewidth=2)
    ax.text(30, 75, "Outbound Beacon", color="#ef4444", fontsize=7.5)

    plt.tight_layout()
    output_path = r"01_first_responder_documentation/scene_sketch_topology.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    print(f"Topology image generated successfully at {output_path}")

if __name__ == "__main__":
    generate_topology_image()
