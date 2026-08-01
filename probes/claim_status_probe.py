#!/usr/bin/env python3
"""Claim status probe — OPEN seals must remain OPEN in status-register.yaml text."""
from __future__ import annotations
from pathlib import Path
import json

def main() -> int:
    text = (Path(__file__).resolve().parents[1] / "registry/status-register.yaml").read_text()
    ok = ("id: RH" in text and "status: OPEN" in text and
          "id: coleman" in text and "status: CLOSED-NEGATIVE" in text)
    print(json.dumps({"probe": "claim_status", "ok": ok}))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
