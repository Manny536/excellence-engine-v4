#!/usr/bin/env python3
"""Validate PeAIce Outcomes as the first-class EEV4 case."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_outcome_case


def main() -> int:
    case = load_json("benchmarks/cases/outcomes-001.json")
    errors = validate_outcome_case(case)
    result = {
        "probe": "outcome_case",
        "case_id": case.get("case_id"),
        "ok": not errors,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
