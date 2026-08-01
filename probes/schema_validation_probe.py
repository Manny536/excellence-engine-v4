#!/usr/bin/env python3
"""Validate R1 case and control envelopes against Draft 2020-12 schemas."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def errors_for(instance: dict, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{'/'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    ]


def main() -> int:
    schema_dir = ROOT / "benchmarks/schemas"
    held_schema = load(schema_dir / "held-trace.schema.json")
    outcome_schema = load(schema_dir / "outcome-case.schema.json")
    control_schema = load(schema_dir / "control-case.schema.json")
    for schema in (held_schema, outcome_schema, control_schema):
        Draft202012Validator.check_schema(schema)

    outcome = load(ROOT / "benchmarks/cases/outcomes-001.json")
    reports = {
        "outcomes-001": errors_for(outcome, outcome_schema),
        "outcomes-001/held_trace": errors_for(outcome.get("held_trace", {}), held_schema),
    }
    for path in sorted((ROOT / "benchmarks/controls").glob("*.json")):
        reports[path.stem] = errors_for(load(path), control_schema)

    ok = all(not errors for errors in reports.values())
    result = {"probe": "schema_validation", "ok": ok, "reports": reports}
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
