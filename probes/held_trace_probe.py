#!/usr/bin/env python3
"""Validate the HELD trace embedded in the real Outcomes case."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_held_trace


def main() -> int:
    case = load_json("benchmarks/cases/outcomes-001.json")
    trace = case.get("held_trace", {})
    errors = validate_held_trace(trace) if isinstance(trace, dict) else ["fail:trace_type"]
    result = {
        "probe": "held_trace",
        "case_id": case.get("case_id"),
        "state": trace.get("state") if isinstance(trace, dict) else None,
        "ok": not errors,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
