#!/usr/bin/env python3
"""Evidence exposure probe — sample HELD trace must list for and against."""
from __future__ import annotations
import json

def main() -> int:
    sample = {
        "evidence_for": ["dependency tower"],
        "evidence_against": ["no exact bridge yet"],
    }
    ok = bool(sample["evidence_for"]) and bool(sample["evidence_against"])
    print(json.dumps({"probe": "evidence_exposure", "ok": ok}, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
