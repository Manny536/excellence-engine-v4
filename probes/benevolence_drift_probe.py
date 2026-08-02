#!/usr/bin/env python3
"""Validate the registered BD-AI paired-turn observation and its boundaries."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_bd_case


def main() -> int:
    case = load_json("benchmarks/cases/bd-ai-case-01.json")
    errors = validate_bd_case(case)
    result = {
        "probe": "benevolence_drift",
        "case_id": case.get("case_id"),
        "status": case.get("status"),
        "evaluation_target": case.get("evaluation_target"),
        "pressure_gap": case.get("observation", {}).get("pressure_gap"),
        "ok": not errors,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
