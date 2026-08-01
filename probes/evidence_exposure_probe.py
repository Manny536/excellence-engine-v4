#!/usr/bin/env python3
"""Require inspectable supporting and counterevidence on the Outcomes trace."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import load_json


def _valid_items(items: object) -> bool:
    return (
        isinstance(items, list)
        and bool(items)
        and all(
            isinstance(item, dict)
            and all(isinstance(item.get(key), str) and item[key].strip() for key in ("id", "claim", "status"))
            for item in items
        )
    )


def main() -> int:
    trace = load_json("benchmarks/cases/outcomes-001.json").get("held_trace", {})
    evidence = trace.get("evidence", {}) if isinstance(trace, dict) else {}
    supporting = evidence.get("supporting")
    counter = evidence.get("counter")
    errors = []
    if not _valid_items(supporting):
        errors.append("fail:evidence_supporting")
    if not _valid_items(counter):
        errors.append("fail:evidence_counter")
    result = {
        "probe": "evidence_exposure",
        "ok": not errors,
        "supporting_count": len(supporting) if isinstance(supporting, list) else 0,
        "counter_count": len(counter) if isinstance(counter, list) else 0,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
