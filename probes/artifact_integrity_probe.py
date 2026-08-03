#!/usr/bin/env python3
"""Artifact integrity — pins must be 64-char hex."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

HEX64 = re.compile(r"^[a-f0-9]{64}$")

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = root / "outcomes/artifacts/integrity-ledger.json"
    data = json.loads(path.read_text())
    bad = [p["id"] for p in data["pins"] if not HEX64.match(p["sha256"])]
    missing = []
    mismatched = []
    for pin in data["pins"]:
        if "path" not in pin:
            continue
        artifact = root / pin["path"]
        if not artifact.is_file():
            missing.append(pin["id"])
            continue
        actual = hashlib.sha256(artifact.read_bytes()).hexdigest()
        if actual != pin["sha256"]:
            mismatched.append(pin["id"])
    ok = not bad and not missing and not mismatched and len(data["pins"]) >= 5
    print(json.dumps({
        "probe": "artifact_integrity",
        "ok": ok,
        "bad": bad,
        "missing": missing,
        "mismatched": mismatched,
    }, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
