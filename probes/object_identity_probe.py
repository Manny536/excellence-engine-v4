#!/usr/bin/env python3
"""Object identity probe — requires distinct status tags for firewall objects."""
from __future__ import annotations
import json
from pathlib import Path

def main() -> int:
    path = Path(__file__).resolve().parents[1] / "benchmarks/cases/kakeya-object-identity-001.json"
    data = json.loads(path.read_text())
    names = {o["name"] for o in data["objects"]}
    required = {"standard_kakeya", "centered_full_line_completion", "coleman_program"}
    ok = required <= names and data.get("firewall") == "no_silent_relabeling"
    print(json.dumps({"probe": "object_identity", "ok": ok, "names": sorted(names)}, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
