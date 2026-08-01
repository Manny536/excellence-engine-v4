from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eev4.validation import (
    load_json,
    validate_control_case,
    validate_held_trace,
    validate_outcome_case,
    validate_status_register,
)

def test_exact_status_contract() -> None:
    assert validate_status_register(load_json("registry/status-register.yaml")) == []


def test_outcomes_case_and_trace_pass() -> None:
    case = load_json("benchmarks/cases/outcomes-001.json")
    assert validate_outcome_case(case) == []
    assert validate_held_trace(case["held_trace"]) == []


def test_controls_fail_for_declared_reasons() -> None:
    paths = sorted((ROOT / "benchmarks/controls").glob("*.json"))
    assert len(paths) == 3
    for path in paths:
        control = json.loads(path.read_text(encoding="utf-8"))
        assert validate_control_case(control) == []


def test_premature_promotion_is_rejected() -> None:
    trace = copy.deepcopy(load_json("benchmarks/cases/outcomes-001.json")["held_trace"])
    trace["status_tags"] = ["HELD", "FORMAL:RH", "FORMAL:Coleman"]
    errors = validate_held_trace(trace)
    assert "fail:premature_promotion" in errors
    assert "fail:open_seals" in errors


def test_evidence_insulation_is_rejected() -> None:
    trace = copy.deepcopy(load_json("benchmarks/cases/outcomes-001.json")["held_trace"])
    trace["evidence"]["counter"] = []
    assert "fail:evidence_counter" in validate_held_trace(trace)


def test_correction_must_change_the_formulation() -> None:
    trace = copy.deepcopy(load_json("benchmarks/cases/outcomes-001.json")["held_trace"])
    trace["correction"]["after"] = trace["correction"]["before"]
    assert "fail:correction" in validate_held_trace(trace)
