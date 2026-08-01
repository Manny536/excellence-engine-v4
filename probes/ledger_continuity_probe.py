#!/usr/bin/env python3
"""Require explicit ownership links for every EEV4 ledger surface."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "EEV4": "https://github.com/Manny536/excellence-engine-v4",
    "KakeyaLogic": "https://github.com/Manny536/kakeyalogic",
    "Claude V6": "https://github.com/Manny536/claude-v6",
    "LoveLabs-LCA": "https://github.com/Manny536/LoveLabs-LCA",
    "Grok Terminal": "https://github.com/Manny536/grok-terminal",
    "PeAIce Outcomes": "https://peaice.org/outcomes",
}


def main() -> int:
    source_map = (ROOT / "SOURCE_MAP.md").read_text(encoding="utf-8")
    missing = [label for label, ref in REQUIRED.items() if ref not in source_map]
    result = {
        "probe": "ledger_continuity",
        "ok": not missing,
        "missing": missing,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
