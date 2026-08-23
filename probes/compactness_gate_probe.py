#!/usr/bin/env python3
"""Validate the multiscale compactness receipt and its negative controls."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json, validate_compactness_gate


def apply_mutation(target: dict[str, Any], mutation: dict[str, Any]) -> None:
    parts = mutation["path"].split(".")
    cursor: dict[str, Any] = target
    for part in parts[:-1]:
        cursor = cursor[part]
    cursor[parts[-1]] = mutation["value"]


def main() -> int:
    base = load_json("benchmarks/cases/multiscale-compactness-gate-001.json")
    base_errors = validate_compactness_gate(base)

    reports = []
    control_dir = ROOT / "benchmarks" / "controls" / "compactness"
    for path in sorted(control_dir.glob("*.json")):
        control = json.loads(path.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(base)
        mutations = control.get("mutations") or [control.get("mutation")]
        for mutation in mutations:
            apply_mutation(mutated, mutation)
        actual = validate_compactness_gate(mutated)
        expected = sorted(control["expected_errors"])
        reports.append({
            "control_id": control["control_id"],
            "ok": actual == expected,
            "expected_errors": expected,
            "actual_errors": actual,
        })

    ok = not base_errors and len(reports) == 3 and all(report["ok"] for report in reports)
    result = {
        "probe": "compactness_gate",
        "ok": ok,
        "base_terminal_status": base.get("terminal_status"),
        "base_errors": base_errors,
        "controls": reports,
        "validates": "gate structure and non-promotion only",
        "does_not_validate": "compactness, convergence, or a Kakeya theorem",
    }
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
