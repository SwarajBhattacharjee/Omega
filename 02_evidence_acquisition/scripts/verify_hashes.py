#!/usr/bin/env python3
"""
Forensic Evidence Hash Verification & Integrity Auditor
Case: Case Omega - Healthcare Cyber Attack Investigation
Investigator: Swaraj Bhattacharjee (Roll: 2301730011)
"""

import os
import hashlib
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HASH_FILE = os.path.join(BASE_DIR, "verification_hashes.sha256")

def calculate_sha256(filepath):
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            sha.update(chunk)
    return sha.hexdigest()

def verify_manifest():
    print("=" * 70)
    print("  FORENSIC INTEGRITY AUDIT: HASH VERIFICATION (SHA-256)")
    print("  Investigator: Swaraj Bhattacharjee | Roll: 2301730011")
    print("=" * 70)

    if not os.path.exists(HASH_FILE):
        print(f"[!] Error: Manifest file not found at {HASH_FILE}")
        sys.exit(1)

    all_valid = True
    with open(HASH_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            continue

        expected_hash, rel_path = parts
        rel_path = rel_path.strip()
        full_path = os.path.join(BASE_DIR, rel_path)

        if not os.path.exists(full_path):
            print(f"[-] FILE MISSING: {rel_path} -> [FAILED]")
            all_valid = False
            continue

        actual_hash = calculate_sha256(full_path)
        if actual_hash.lower() == expected_hash.lower():
            print(f"[+] VERIFIED [MATCH]: {rel_path}")
            print(f"    Expected: {expected_hash}")
            print(f"    Actual:   {actual_hash}")
            print(f"    Integrity Status: BIT-PERFECT (Zero Tampering Detected)\n")
        else:
            print(f"[!] HASH MISMATCH [TAMPERED / CORRUPTED]: {rel_path}")
            print(f"    Expected: {expected_hash}")
            print(f"    Actual:   {actual_hash}\n")
            all_valid = False

    print("=" * 70)
    if all_valid:
        print("[SUCCESS] All digital forensic artifacts verified successfully.")
        print("[LEGAL STATUS] Admissible under Section 65B Indian Evidence Act / Section 63 BSA.")
    else:
        print("[ALERT] Forensic integrity check failed for one or more files.")
        sys.exit(1)

if __name__ == "__main__":
    verify_manifest()
