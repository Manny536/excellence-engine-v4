"""Typed validation for Excellence Engine V4.

The module is intentionally small and criteria-explicit. Mathematical truth is
never inferred from a HELD state. The validators inspect custody, evidence,
correction, source continuity, and claim-status discipline.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from excellence_engine_v4.status import HELD_STATES

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_STATUS = {
    "K_to_R_custody": "HELD-RETAINED",
    "kakeya_R3_dimension": "THEOREM-BACKGROUND",
    "sufficiency_packaging": "CLOSED",
    "faithful_kappa": "OPEN",
    "prime_carrying_L3": "LIVE",
    "K_sigma_lane": "CLOSED-NEGATIVE",
    "WP5b_bounded": "CLOSED-NEGATIVE",
    "coleman": "OPEN",
    "RH": "OPEN",
    "outcomes_final_001": "FINAL-PUBLIC-RESEARCH",
    "outcomes_architecture": "FORMAL",
    "bd_ai_cases": "REGISTERED-QUALITATIVE",
    "bd_ai_trajectory_reference": "SOURCE-REGISTERED",
    "bd_ai_benchmark": "OWED",
    "multiscale_configuration_net": "PROPOSED",
    "configuration_carrier_compactness": "OWED",
    "kakeya_limit_preservation": "OPEN",
    "l2c_analytic_realization": "OPEN",
    "net_gate_interpretability": "OPEN",
}

REQUIRED_FINDINGS = {
    "context_before_verdict",
    "no_peer_review_not_stop",
    "conjecture_custody",
    "neutrality_nonresponse",
    "defaults_replace_judgment",
    "scale_method_not_answer",
}

REQUIRED_OPEN_SEALS = {"RH", "Coleman", "CC-I", "CC-O", "BD_benchmark"}

FORBIDDEN_PROMOTION_TAGS = {
    "FORMAL:RH",
    "PROVEN:RH",
    "CLOSED-POSITIVE:RH",
    "FORMAL:Coleman",
    "PROVEN:Coleman",
    "CLOSED-POSITIVE:Coleman",
}


def load_json(relative: str | Path) -> dict[str, Any]:
    path = ROOT / relative
    return json.loads(path.read_text(encoding="utf-8"))


def validate_status_register(register: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if register.get("engine") != "V4 = K→R · HELD":
        errors.append("status:engine_identity")
    if register.get("h") != "< 1":
        errors.append("status:h_bound")

    entries = register.get("entries")
    if not isinstance(entries, list):
        return errors + ["status:entries_type"]

    ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    if len(ids) != len(set(ids)):
        errors.append("status:duplicate_id")

    mapping = {
        entry.get("id"): entry.get("status")
        for entry in entries
        if isinstance(entry, dict)
    }
    for claim_id, expected in REQUIRED_STATUS.items():
        actual = mapping.get(claim_id)
        if actual != expected:
            errors.append(f"status:{claim_id}:{actual!s}!={expected}")

    return errors


def _nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0


def validate_held_trace(trace: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "case_id",
        "designation",
        "object",
        "state",
        "status_tags",
        "h_eval",
        "evidence",
        "correction",
        "falsifier",
        "source_refs",
    }
    for field in sorted(required - set(trace)):
        errors.append(f"missing:{field}")

    if trace.get("state") not in HELD_STATES:
        errors.append("fail:state")

    obj = trace.get("object")
    if not isinstance(obj, dict) or not all(
        isinstance(obj.get(key), str) and obj.get(key).strip()
        for key in ("id", "label", "kind", "formulation")
    ):
        errors.append("fail:typed_object")

    tags = trace.get("status_tags")
    if not _nonempty_list(tags):
        errors.append("fail:status_tags")
        tags = []
    tag_set = set(tags)
    if {"OPEN:RH", "OPEN:Coleman"} - tag_set:
        errors.append("fail:open_seals")
    if FORBIDDEN_PROMOTION_TAGS & tag_set:
        errors.append("fail:premature_promotion")

    h_eval = trace.get("h_eval")
    if not (
        isinstance(h_eval, dict)
        and h_eval.get("bound") == "< 1"
        and h_eval.get("passed") is True
    ):
        errors.append("fail:h_bound")

    evidence = trace.get("evidence")
    if not isinstance(evidence, dict):
        errors.extend(["fail:evidence_supporting", "fail:evidence_counter"])
    else:
        if not _nonempty_list(evidence.get("supporting")):
            errors.append("fail:evidence_supporting")
        if not _nonempty_list(evidence.get("counter")):
            errors.append("fail:evidence_counter")

    correction = trace.get("correction")
    if not isinstance(correction, dict):
        errors.append("fail:correction")
    else:
        required_correction = {"trigger", "before", "after", "closed_lane", "continuity_preserved"}
        if required_correction - set(correction):
            errors.append("fail:correction")
        elif (
            correction.get("before") == correction.get("after")
            or correction.get("continuity_preserved") is not True
        ):
            errors.append("fail:correction")

    falsifier = trace.get("falsifier")
    if not isinstance(falsifier, str) or not falsifier.strip():
        errors.append("fail:falsifier")

    refs = trace.get("source_refs")
    if not (
        isinstance(refs, list)
        and len(refs) >= 2
        and all(isinstance(ref, str) and ref.startswith("https://") for ref in refs)
    ):
        errors.append("fail:source_refs")

    if trace.get("state") == "HELD-RELEASED":
        release = trace.get("release")
        if not (
            isinstance(release, dict)
            and isinstance(release.get("basis"), str)
            and release.get("basis").strip()
        ):
            errors.append("fail:release_basis")

    return sorted(set(errors))


def validate_outcome_case(case: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if case.get("governing_rule") != (
        "Protect the question. Expose the answer to evidence. Help build outcomes."
    ):
        errors.append("outcome:governing_rule")

    findings = case.get("findings")
    if not isinstance(findings, list) or set(findings) != REQUIRED_FINDINGS:
        errors.append("outcome:six_findings")

    seals = case.get("open_seals")
    if not isinstance(seals, list) or not REQUIRED_OPEN_SEALS.issubset(set(seals)):
        errors.append("outcome:open_seals")

    artifacts = case.get("artifact_ids")
    if not isinstance(artifacts, list) or not {
        "outcomes-final-pdf",
        "outcomes-final-docx",
    }.issubset(set(artifacts)):
        errors.append("outcome:artifact_pins")

    public_url = case.get("public_url")
    if not isinstance(public_url, str) or not public_url.startswith("https://"):
        errors.append("outcome:public_url")

    trace = case.get("held_trace")
    if not isinstance(trace, dict):
        errors.append("outcome:held_trace")
    else:
        errors.extend(f"trace:{error}" for error in validate_held_trace(trace))

    return sorted(set(errors))


def validate_bd_case(case: dict[str, Any]) -> list[str]:
    """Validate the observable BD-AI paired-turn case without hidden-state promotion."""
    errors: list[str] = []
    if case.get("case_id") != "BD-AI-CASE-01":
        errors.append("bd:case_id")
    if case.get("status") != "REGISTERED-QUALITATIVE":
        errors.append("bd:status")
    if case.get("evaluation_target") != "system_response":
        errors.append("bd:evaluation_target")

    threshold = case.get("threshold")
    if not isinstance(threshold, dict):
        errors.append("bd:threshold")
    else:
        features = threshold.get("evidence_features")
        if (
            threshold.get("symbol") != "τ_call"
            or threshold.get("crossed") is not True
            or not isinstance(features, list)
            or len(features) < 3
        ):
            errors.append("bd:threshold")

    turns = case.get("turns")
    if not isinstance(turns, list) or len(turns) != 2:
        errors.append("bd:turns")
    else:
        first, second = turns
        if not all(isinstance(turn, dict) for turn in turns):
            errors.append("bd:turns")
        else:
            if (
                first.get("q_relation") != ">="
                or first.get("application") != "below-threshold"
                or second.get("application") != "at-or-above-threshold"
                or second.get("probe_type") != "forced-binary"
            ):
                errors.append("bd:pressure_gap")
            if any(turn.get("new_substantive_evidence") is not False for turn in turns):
                errors.append("bd:new_evidence")

    observation = case.get("observation")
    if not isinstance(observation, dict):
        errors.append("bd:observation")
    else:
        if observation.get("pressure_gap") is not True:
            errors.append("bd:pressure_gap")
        if observation.get("internal_state_claim") is not False:
            errors.append("bd:internal_state_claim")
        if not isinstance(observation.get("latency_turns"), int):
            errors.append("bd:latency")

    for field in ("expected_response", "limits", "falsifiers"):
        value = case.get(field)
        if not isinstance(value, list) or len(value) < 3:
            errors.append(f"bd:{field}")

    refs = case.get("source_refs")
    if not (
        isinstance(refs, list)
        and len(refs) >= 2
        and all(isinstance(ref, str) and ref.startswith("https://") for ref in refs)
    ):
        errors.append("bd:source_refs")

    h_eval = case.get("h_eval")
    if not (
        isinstance(h_eval, dict)
        and h_eval.get("bound") == "< 1"
        and h_eval.get("passed") is True
    ):
        errors.append("bd:h_bound")

    return sorted(set(errors))


def validate_control_case(control: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    trace = control.get("input_trace")
    expected = control.get("expected_errors")
    if not isinstance(trace, dict):
        return ["control:input_trace"]
    if not _nonempty_list(expected):
        return ["control:expected_errors"]

    actual = set(validate_held_trace(trace))
    missing = set(expected) - actual
    unexpected = actual - set(expected)
    if missing:
        errors.extend(f"control:missing_expected:{item}" for item in sorted(missing))
    if unexpected:
        errors.extend(f"control:unexpected_error:{item}" for item in sorted(unexpected))
    if not actual:
        errors.append("control:unexpected_pass")
    return errors


COMPACTNESS_GATES = (
    "G0_CARRIER",
    "G1_DIRECTED",
    "G2_COMPACT",
    "G3_EXTRACT",
    "G4_CLOSED",
    "G5_TRANSFER",
)

COMPACTNESS_TERMINAL_STATES = {
    "PASS-LIMIT",
    "LIMIT-CANDIDATE",
    "BLOCKED-COMPACTNESS",
    "BLOCKED-CLOSURE",
    "BLOCKED-TRANSFER",
}


def validate_compactness_gate(receipt: dict[str, Any]) -> list[str]:
    """Validate finite-to-limit custody without certifying the mathematics."""
    errors: list[str] = []

    required = {
        "case_id",
        "designation",
        "claim_status",
        "terminal_status",
        "index",
        "configuration",
        "gates",
        "lean_receipt",
        "evaluator_independent",
        "promotion_authorized",
        "claim_boundaries",
        "falsifier",
        "kill_criterion",
        "source_refs",
        "h_eval",
    }
    missing = sorted(required - set(receipt))
    if missing:
        return [f"missing:{field}" for field in missing]

    if receipt.get("case_id") != "MULTISCALE-COMPACTNESS-GATE-001":
        errors.append("fail:case_id")
    if receipt.get("designation") != "PEAICE-EEV4-MULTISCALE-COMPACTNESS-GATE-001":
        errors.append("fail:designation")
    if receipt.get("claim_status") != "PROPOSED":
        errors.append("fail:claim_status")

    terminal = receipt.get("terminal_status")
    if terminal not in COMPACTNESS_TERMINAL_STATES:
        errors.append("fail:terminal_status")

    index = receipt.get("index")
    if not isinstance(index, dict):
        errors.append("fail:index")
        refinement = {}
    else:
        refinement = index.get("refinement")
        if not isinstance(refinement, dict):
            errors.append("fail:refinement")
            refinement = {}

    configuration = receipt.get("configuration")
    if not isinstance(configuration, dict):
        errors.append("fail:configuration")
        configuration = {}
    elif configuration.get("preserves_incidence_coupling") is not True:
        errors.append("fail:incidence_coupling")

    gates = receipt.get("gates")
    if not isinstance(gates, dict):
        return sorted(set(errors + ["fail:gates"]))

    statuses: dict[str, str | None] = {}
    for gate_name in COMPACTNESS_GATES:
        gate = gates.get(gate_name)
        if not isinstance(gate, dict):
            errors.append(f"fail:{gate_name.lower()}")
            statuses[gate_name] = None
            continue
        status = gate.get("status")
        if status not in {"PASS", "OWED", "FAIL", "BLOCKED"}:
            errors.append(f"fail:{gate_name.lower()}_status")
        statuses[gate_name] = status
        evidence = gate.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"fail:{gate_name.lower()}_evidence")
        elif status == "PASS" and not evidence:
            errors.append(f"fail:{gate_name.lower()}_evidence")
        obligation = gate.get("obligation")
        if not isinstance(obligation, str) or not obligation.strip():
            errors.append(f"fail:{gate_name.lower()}_obligation")

    if statuses.get("G1_DIRECTED") == "PASS" and refinement.get("join_certified") is not True:
        errors.append("fail:g1_join_certificate")

    if statuses.get("G1_DIRECTED") == "PASS" and statuses.get("G0_CARRIER") != "PASS":
        errors.append("fail:g1_before_g0")
    if statuses.get("G2_COMPACT") == "PASS" and not all(
        statuses.get(gate) == "PASS" for gate in COMPACTNESS_GATES[:2]
    ):
        errors.append("fail:g2_before_g1")
    if statuses.get("G2_COMPACT") == "PASS" and configuration.get("compactness_proved") is not True:
        errors.append("fail:g2_compactness_receipt")
    if statuses.get("G3_EXTRACT") == "PASS" and statuses.get("G2_COMPACT") != "PASS":
        errors.append("fail:g3_before_g2")
    if statuses.get("G4_CLOSED") == "PASS" and statuses.get("G3_EXTRACT") != "PASS":
        errors.append("fail:g4_before_g3")
    if statuses.get("G5_TRANSFER") == "PASS" and statuses.get("G4_CLOSED") != "PASS":
        errors.append("fail:g5_before_g4")

    all_pass = all(statuses.get(gate) == "PASS" for gate in COMPACTNESS_GATES)
    first_four_pass = all(statuses.get(gate) == "PASS" for gate in COMPACTNESS_GATES[:4])
    first_five_pass = all(statuses.get(gate) == "PASS" for gate in COMPACTNESS_GATES[:5])

    if terminal == "PASS-LIMIT" and not all_pass:
        errors.append("fail:terminal_pass_limit")
    elif terminal == "LIMIT-CANDIDATE" and not first_four_pass:
        errors.append("fail:terminal_limit_candidate")
    elif terminal == "BLOCKED-COMPACTNESS" and statuses.get("G2_COMPACT") == "PASS":
        errors.append("fail:terminal_blocked_compactness")
    elif terminal == "BLOCKED-CLOSURE" and not (
        first_four_pass and statuses.get("G4_CLOSED") != "PASS"
    ):
        errors.append("fail:terminal_blocked_closure")
    elif terminal == "BLOCKED-TRANSFER" and not (
        first_five_pass and statuses.get("G5_TRANSFER") != "PASS"
    ):
        errors.append("fail:terminal_blocked_transfer")

    lean_receipt = receipt.get("lean_receipt")
    if not isinstance(lean_receipt, dict):
        errors.append("fail:lean_receipt")
        lean_compiled = False
    else:
        lean_compiled = lean_receipt.get("compiled") is True
        expected_status = "COMPILED" if lean_compiled else "PLANNED / NOT COMPILED"
        if lean_receipt.get("status") != expected_status:
            errors.append("fail:lean_receipt_status")

    promotion_authorized = receipt.get("promotion_authorized") is True
    if promotion_authorized:
        if terminal != "PASS-LIMIT" or not all_pass:
            errors.append("fail:promotion_without_gates")
        if receipt.get("evaluator_independent") is not True:
            errors.append("fail:promotion_without_independent_receipt")
        if not lean_compiled:
            errors.append("fail:promotion_without_formal_receipt")

    boundaries = receipt.get("claim_boundaries")
    if not isinstance(boundaries, list) or len(boundaries) < 4:
        errors.append("fail:claim_boundaries")
    for field in ("falsifier", "kill_criterion"):
        value = receipt.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"fail:{field}")

    refs = receipt.get("source_refs")
    if not (
        isinstance(refs, list)
        and len(refs) >= 2
        and all(isinstance(ref, str) and ref.startswith("https://") for ref in refs)
    ):
        errors.append("fail:source_refs")

    h_eval = receipt.get("h_eval")
    if not (
        isinstance(h_eval, dict)
        and h_eval.get("bound") == "< 1"
        and h_eval.get("passed") is True
    ):
        errors.append("fail:h_bound")

    return sorted(set(errors))
