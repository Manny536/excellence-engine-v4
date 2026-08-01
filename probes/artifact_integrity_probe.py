#!/usr/bin/env python3
"""Artifact integrity — pins must be 64-char hex."""
from __future__ import annotations
import json, re
from pathlib import Path

HEX64 = re.compile(r"^[a-f0-9]{64}$")

def main() -> int:
    path = Path(__file__).resolve().parents[1] / "outcomes/artifacts/integrity-ledger.json"
    data = json.loads(path.read_text())
    bad = [p["id"] for p in data["pins"] if not HEX64.match(p["sha256"])]
    ok = not bad and len(data["pins"]) >= 4
    print(json.dumps({"probe": "artifact_integrity", "ok": ok, "bad": bad}, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
