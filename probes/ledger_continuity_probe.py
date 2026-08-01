#!/usr/bin/env python3
"""Ledger continuity — SOURCE_MAP must name sibling labs."""
from __future__ import annotations
from pathlib import Path
import json

REQUIRED = ["kakeyalogic", "claude-v6", "LoveLabs-LCA", "grok-terminal"]

def main() -> int:
    text = (Path(__file__).resolve().parents[1] / "SOURCE_MAP.md").read_text()
    missing = [r for r in REQUIRED if r not in text]
    ok = not missing
    print(json.dumps({"probe": "ledger_continuity", "ok": ok, "missing": missing}))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
