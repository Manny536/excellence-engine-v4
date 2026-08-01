#!/usr/bin/env python3
"""HELD trace probe — criteria-explicit, stdlib-only."""
from __future__ import annotations
import json
from pathlib import Path

REQUIRED = ("case_id", "object", "state", "status_tags", "h_lt_1")
STATES = {"RECEIVED","HELD-ACTIVE","HELD-REVISED","HELD-RETAINED","HELD-RELEASED","HELD-CLOSED"}

def validate_trace(trace: dict) -> list[str]:
    errors = []
    for k in REQUIRED:
        if k not in trace:
            errors.append(f"missing:{k}")
    if trace.get("state") not in STATES:
        errors.append("invalid:state")
    if trace.get("h_lt_1") is not True:
        errors.append("fail:h_lt_1")
    if not isinstance(trace.get("status_tags", []), list) or not trace.get("status_tags"):
        errors.append("fail:status_tags")
    return errors

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    sample = {
        "case_id": "outcomes-001",
        "object": "Kakeya as antecedent Riemann",
        "state": "HELD-RETAINED",
        "status_tags": ["HELD", "PROPOSED", "OPEN:RH", "OPEN:Coleman"],
        "h_lt_1": True,
        "evidence_for": ["dependency tower"],
        "evidence_against": ["sufficiency packaging closed"],
        "falsifier": "exact Xi carrier without Kakeya incidence",
    }
    errs = validate_trace(sample)
    case = root / "benchmarks/cases/outcomes-001.json"
    out = {"probe": "held_trace", "ok": not errs and case.is_file(), "errors": errs}
    print(json.dumps(out, indent=2))
    return 0 if out["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
