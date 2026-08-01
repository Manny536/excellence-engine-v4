#!/usr/bin/env python3
"""Confirm every negative control fails for its declared reason."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import validate_control_case

EXPECTED_MODES = {
    "premature_dismissal",
    "premature_promotion",
    "evidence_insulation",
}


def main() -> int:
    reports = []
    seen_modes = set()
    for path in sorted((ROOT / "benchmarks/controls").glob("*.json")):
        control = json.loads(path.read_text(encoding="utf-8"))
        seen_modes.add(control.get("failure_mode"))
        errors = validate_control_case(control)
        reports.append({
            "control_id": control.get("control_id"),
            "ok": not errors,
            "errors": errors,
        })

    missing_modes = sorted(EXPECTED_MODES - seen_modes)
    ok = bool(reports) and not missing_modes and all(report["ok"] for report in reports)
    result = {
        "probe": "control_cases",
        "ok": ok,
        "missing_modes": missing_modes,
        "controls": reports,
    }
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
