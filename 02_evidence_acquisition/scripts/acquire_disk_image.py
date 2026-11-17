#!/usr/bin/env python3
"""
Forensic Acquisition Simulator (FTK Imager / dc3dd emulation)
Case: Case Omega - Healthcare Cyber Attack Investigation
Target: OMEGA-SRV-01 (Dell PowerEdge R750 EHR Server)
Investigator: Swaraj Bhattacharjee (Roll: 2301730011, B.Tech CSE AI ML)
"""

import os
import hashlib
import time
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "raw_images")
HASH_FILE = os.path.join(os.path.dirname(__file__), "..", "verification_hashes.sha256")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_disk_acquisition(image_name="server_ehr_partition.raw", size_kb=1024):
    """
    Simulates a bit-stream raw (.dd / .raw) image acquisition of the compromised
    EHR server volume, including simulated MBR, NTFS sector headers, and encrypted patient blocks.
    """
    image_path = os.path.join(OUTPUT_DIR, image_name)
    print(f"[*] Initializing Forensic Acquisition: {image_name}")
    print(f"[*] Source Device: \\\\.\\PhysicalDrive0 (Partition 2: C:\\EHR_DATABASE)")
    print(f"[*] Hardware Write Blocker: Tableau T8u Forensic USB 3.0 Bridge [ACTIVE]")
    print(f"[*] Acquisition Tool: dc3dd v7.2 / FTK Imager CLI Bridge")
    print(f"[*] Timestamp: {datetime.now().isoformat()}")
    print("-" * 65)

    # Synthetic forensic disk image content
    header = (
        b"\xEB\x52\x90NTFS    \x00\x02\x08\x00\x00\x00\x00\x00\x00\x00\xF8\x00\x00"
        b"[FORENSIC DISK IMAGE REPLICA - CASE OMEGA - EVIDENCE TAG: EVD-OMEGA-001]\n"
        b"[DEVICE: DELL POWEREDGE R750 - S/N: DELL-R750-OMEGA99 - VOLUME C:\\EHR]\n"
    )
    
    # Simulated file records in the sector stream
    sector_data = (
        b"\n--- [MFT RECORD 001: PATIENT_INDEX.DB.omega] ---\n"
        b"STATUS: ENCRYPTED BY OMEGA LOCKER RANSOMWARE\n"
        b"ORIGINAL_SIZE: 14209504 BYTES\n"
        b"CIPHER: AES-256-CBC | IV: 9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c\n"
        b"HEADER_MAGIC: OMEGALOCK_V42\n"
        + b"\x90\xAA\xBB\xCC\xDD\xEE\xFF" * 400 +
        b"\n--- [MFT RECORD 002: README_RECOVERY_KEY.txt] ---\n"
        b"ALL YOUR HEALTHCARE RECORDS ARE ENCRYPTED UNDER AES-256 + RSA-4096.\n"
        b"CONTACT: recovery@omega-blacklock.onion\n"
    )

    pad_size = (size_kb * 1024) - len(header) - len(sector_data)
    if pad_size < 0:
        pad_size = 1024
    
    padding = b"\x00" * pad_size

    # Write out the forensic disk image
    with open(image_path, "wb") as f:
        f.write(header)
        f.write(sector_data)
        f.write(padding)

    # Compute SHA-256 and MD5 hashes
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()
    with open(image_path, "rb") as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
            md5.update(chunk)

    sha256_digest = sha256.hexdigest()
    md5_digest = md5.hexdigest()

    file_size = os.path.getsize(image_path)
    print(f"[+] Acquisition Complete: {image_path}")
    print(f"[+] Total Sectors Acquired: {file_size // 512} sectors ({file_size} bytes)")
    print(f"[+] Acquisition MD5:    {md5_digest}")
    print(f"[+] Acquisition SHA-256:{sha256_digest}")
    print(f"[+] Bad Sectors / Read Errors Encountered: 0")
    print("-" * 65)

    return image_name, sha256_digest, md5_digest, file_size

def simulate_ram_acquisition(image_name="memory_dump_sample.raw", size_kb=512):
    """
    Simulates a live volatile physical RAM dump using WinPmem / LiME.
    """
    image_path = os.path.join(OUTPUT_DIR, image_name)
    print(f"[*] Initializing Volatile Memory Capture: {image_name}")
    print(f"[*] Acquisition Tool: WinPmem v4.0 (Live Kernel Memory Driver)")
    
    ram_header = (
        b"[LIVE PHYSICAL MEMORY SNAPSHOT - HOST: OMEGA-SRV-01]\n"
        b"[PID 4488: omegalocker.exe] [SOCKET: 192.168.10.100:49211 -> 185.220.101.45:443]\n"
        b"[IN-MEMORY AES KEY FOUND IN HEAP]: 4d6173746572456e63727970744b65793230323621402324255e262a28292d3d\n"
    )
    padding = b"\x90" * ((size_kb * 1024) - len(ram_header))
    
    with open(image_path, "wb") as f:
        f.write(ram_header)
        f.write(padding)

    sha256 = hashlib.sha256()
    with open(image_path, "rb") as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    
    digest = sha256.hexdigest()
    print(f"[+] Memory Capture Complete: {image_path}")
    print(f"[+] Memory SHA-256: {digest}")
    print("-" * 65)
    return image_name, digest

def main():
    print("=" * 65)
    print("  CASE OMEGA FORENSIC EVIDENCE ACQUISITION ENGINE")
    print("  Lead Investigator: Swaraj Bhattacharjee (Roll: 2301730011)")
    print("=" * 65)
    
    disk_img, disk_sha, disk_md5, disk_sz = simulate_disk_acquisition()
    ram_img, ram_sha = simulate_ram_acquisition()

    # Document hashes into manifest
    manifest_content = (
        f"# Case Omega Forensic Evidence Integrity Manifest\n"
        f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}\n"
        f"# Certified By: Swaraj Bhattacharjee (Lead Investigator, Roll: 2301730011)\n"
        f"# Verification Algorithm: FIPS 180-4 Secure Hash Standard (SHA-256)\n\n"
        f"{disk_sha}  raw_images/{disk_img}\n"
        f"{ram_sha}  raw_images/{ram_img}\n"
    )
    
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        f.write(manifest_content)

    print(f"[+] Hash verification manifest written to: {HASH_FILE}")
    print("[+] Acquisition verification status: VERIFIED & ADMISSIBLE (Sec 65B IEA)")

if __name__ == "__main__":
    main()
