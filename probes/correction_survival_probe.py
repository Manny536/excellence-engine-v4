#!/usr/bin/env python3
"""Require a visible correction, a closed lane, and retained object continuity."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json


def main() -> int:
    case = load_json("benchmarks/cases/outcomes-001.json")
    register = load_json("registry/status-register.yaml")
    trace = case.get("held_trace", {})
    correction = trace.get("correction", {}) if isinstance(trace, dict) else {}
    statuses = {
        entry.get("id"): entry.get("status")
        for entry in register.get("entries", [])
        if isinstance(entry, dict)
    }

    errors = []
    lane = correction.get("closed_lane")
    if correction.get("before") == correction.get("after"):
        errors.append("fail:correction_delta")
    if correction.get("continuity_preserved") is not True:
        errors.append("fail:continuity")
    if trace.get("state") != "HELD-RETAINED":
        errors.append("fail:retained_state")
    if statuses.get(lane) != "CLOSED":
        errors.append(f"fail:closed_lane:{lane}")

    result = {
        "probe": "correction_survival",
        "ok": not errors,
        "closed_lane": lane,
        "retained_state": trace.get("state"),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
