import copy
import json
from pathlib import Path
from typing import Any

from eev4.validation import load_json, validate_compactness_gate


ROOT = Path(__file__).resolve().parents[1]
CASE_PATH = ROOT / "benchmarks" / "cases" / "multiscale-compactness-gate-001.json"
CONTROL_DIR = ROOT / "benchmarks" / "controls" / "compactness"


def apply_mutation(target: dict[str, Any], mutation: dict[str, Any]) -> None:
    parts = mutation["path"].split(".")
    cursor: dict[str, Any] = target
    for part in parts[:-1]:
        cursor = cursor[part]
    cursor[parts[-1]] = mutation["value"]


def test_current_compactness_receipt_is_valid_and_non_promoting() -> None:
    receipt = load_json(CASE_PATH.relative_to(ROOT))
    assert validate_compactness_gate(receipt) == []
    assert receipt["terminal_status"] == "BLOCKED-COMPACTNESS"
    assert receipt["claim_status"] == "PROPOSED"
    assert receipt["configuration"]["compactness_proved"] is False
    assert receipt["lean_receipt"]["compiled"] is False
    assert receipt["promotion_authorized"] is False


def test_compactness_controls_fail_for_exact_declared_reasons() -> None:
    base = json.loads(CASE_PATH.read_text(encoding="utf-8"))
    paths = sorted(CONTROL_DIR.glob("*.json"))
    assert len(paths) == 3

    for path in paths:
        control = json.loads(path.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(base)
        mutations = control.get("mutations") or [control.get("mutation")]
        for mutation in mutations:
            apply_mutation(mutated, mutation)
        assert validate_compactness_gate(mutated) == sorted(control["expected_errors"])


def test_compactness_spec_preserves_claim_boundaries() -> None:
    text = (ROOT / "engine" / "multiscale-compactness-gate.md").read_text(encoding="utf-8")
    required = {
        "BLOCKED-COMPACTNESS",
        "G0 CARRIER",
        "G1 DIRECTED",
        "G2 COMPACT",
        "G3 EXTRACT",
        "G4 CLOSED",
        "G5 TRANSFER",
        "PLANNED / NOT COMPILED",
        "No Kakeya admissibility or observable-transfer theorem is established.",
    }
    missing = sorted(marker for marker in required if marker not in text)
    assert not missing, f"compactness specification missing {missing}"


def test_status_register_keeps_compactness_claims_open_or_owed() -> None:
    register = load_json("registry/status-register.yaml")
    mapping = {entry["id"]: entry["status"] for entry in register["entries"]}
    assert mapping["multiscale_configuration_net"] == "PROPOSED"
    assert mapping["configuration_carrier_compactness"] == "OWED"
    assert mapping["kakeya_limit_preservation"] == "OPEN"
    assert mapping["l2c_analytic_realization"] == "OPEN"
    assert mapping["net_gate_interpretability"] == "OPEN"


def test_compactness_cannot_pass_before_directedness() -> None:
    receipt = load_json(CASE_PATH.relative_to(ROOT))
    receipt["gates"]["G1_DIRECTED"]["status"] = "OWED"
    receipt["gates"]["G2_COMPACT"]["status"] = "PASS"
    receipt["gates"]["G2_COMPACT"]["evidence"] = ["Synthetic compactness claim."]
    receipt["configuration"]["compactness_proved"] = True
    assert "fail:g2_before_g1" in validate_compactness_gate(receipt)
