#!/usr/bin/env python3
"""Correction survival — sufficiency closed but antecedent retained."""
from __future__ import annotations
from pathlib import Path
import json

def main() -> int:
    text = (Path(__file__).resolve().parents[1] / "STATUS.md").read_text()
    ok = "CLOSED" in text and "HELD" in text and "OPEN" in text
    print(json.dumps({"probe": "correction_survival", "ok": ok}))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
