import copy
import hashlib
import json
import re
from pathlib import Path

from eev4.validation import load_json, validate_bd_case


ROOT = Path(__file__).resolve().parents[1]
OUTCOMES = ROOT / "outcomes"

EXPECTED_MARKDOWN = {
    "README.md",
    "benevolence-drift.md",
    "conjecture-custody.md",
    "correction-and-exit.md",
    "downstream-position.md",
    "governing-rule.md",
    "method-not-answer.md",
    "object-firewall.md",
    "six-findings.md",
    "artifacts/source-hashes.md",
    "cases/benevolence-drift-case-01.md",
    "cases/kakeya-object-correction.md",
    "cases/outcomes-001.md",
    "cases/trajectory-reference-public-record.md",
    "readings/claude-downstream-registration.md",
    "readings/claude-runtime-kernel.md",
    "readings/grok-companion.md",
    "readings/solance-v4-reading.md",
}

REQUIRED_MARKERS = {
    "README.md": ("OutcomeReceipt", "OutcomeValid(o,t)", "BD-AI_t", "HELD-RETAINED", "L²_C"),
    "governing-rule.md": ("Partner(q,a)", "Protect(q)", "Expose(a)", "Build(q,a)"),
    "six-findings.md": ("FindingGate", "OF-01", "OF-06", "SixGatePass"),
    "conjecture-custody.md": ("CustodiedClaim", "HELD-RETAINED", "Release discipline"),
    "method-not-answer.md": ("MethodInvariant", "TransferReceipt", "h < 1"),
    "object-firewall.md": ("ObjectSignature", "OFW-1", "K→R ≠ K⇒RH"),
    "correction-and-exit.md": ("CorrectionRecord", "BDCorrection", "DomainExit"),
    "downstream-position.md": ("ArtifactPin", "SourceReceipt", "Authority graph"),
    "benevolence-drift.md": ("BD-AI_t", "PressureGap", "Latency", "Intervention firewall"),
    "cases/benevolence-drift-case-01.md": ("BD-AI-CASE-01", "PressureGap", "Latency = 1"),
    "cases/kakeya-object-correction.md": ("OUT-KAKEYA-CORRECTION-001", "K_ctr(x₀)=ℝⁿ"),
    "cases/outcomes-001.md": ("outcomes-001", "Six findings receipt", "HELD-RETAINED"),
    "cases/trajectory-reference-public-record.md": ("TrajectoryReference", "H_miss", "H_act"),
    "readings/claude-downstream-registration.md": ("ModelReading", "DisagreementReceipt"),
    "readings/claude-runtime-kernel.md": ("Kernel-to-Outcome map", "HELD-CLOSED"),
    "readings/grok-companion.md": ("GrokReceipt", "REGISTERED-COMPANION"),
    "readings/solance-v4-reading.md": ("trajectory-recognition surplus", "OUT-READ-SOLANCE-001"),
    "artifacts/source-hashes.md": ("ArtifactPin", "BD-SNAP-14", "not vendored"),
}


def markdown_paths() -> list[Path]:
    return sorted(OUTCOMES.rglob("*.md"))


def test_outcomes_markdown_manifest_is_explicit() -> None:
    assert {str(path.relative_to(OUTCOMES)) for path in markdown_paths()} == EXPECTED_MARKDOWN


def test_every_outcomes_file_carries_its_formal_markers() -> None:
    for relative, markers in REQUIRED_MARKERS.items():
        text = (OUTCOMES / relative).read_text(encoding="utf-8")
        missing = [marker for marker in markers if marker not in text]
        assert not missing, f"{relative} missing {missing}"


def test_outcomes_readme_preserves_state_and_notation_boundaries() -> None:
    text = (OUTCOMES / "README.md").read_text(encoding="utf-8")
    assert "FINAL-PUBLIC-RESEARCH" in text
    assert "RH `OPEN`" in text and "Coleman Conjecture `OPEN`" in text
    assert "BD-AI benchmark `OWED`" in text
    assert "L²C" not in text
    assert "canonical" not in text.lower()


def test_relative_outcomes_links_resolve() -> None:
    for path in markdown_paths():
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            assert (path.parent / target).resolve().exists(), f"{path}: unresolved {target}"


def test_benevolence_drift_case_passes_typed_validator() -> None:
    case = load_json("benchmarks/cases/bd-ai-case-01.json")
    assert validate_bd_case(case) == []


def test_bd_validator_rejects_person_target_and_hidden_state_claim() -> None:
    case = copy.deepcopy(load_json("benchmarks/cases/bd-ai-case-01.json"))
    case["evaluation_target"] = "person"
    case["observation"]["internal_state_claim"] = True
    errors = validate_bd_case(case)
    assert "bd:evaluation_target" in errors
    assert "bd:internal_state_claim" in errors


def test_bd_evidence_register_pins_all_supplied_snapshots() -> None:
    register = json.loads(
        (OUTCOMES / "artifacts/benevolence-drift-evidence.json").read_text(encoding="utf-8")
    )
    snapshots = register["snapshots"]
    assert len(snapshots) == 14
    assert len({item["id"] for item in snapshots}) == 14
    assert len({item["sha256"] for item in snapshots}) == 14
    assert all(re.fullmatch(r"[a-f0-9]{64}", item["sha256"]) for item in snapshots)
    assert all(item["vendored"] is False for item in snapshots)
    source_ids = {item["id"] for item in register["sources"]}
    assert all(item["source_id"] in source_ids for item in snapshots)


def test_meta_probe_receipt_pins_vendored_artifact_and_preserves_firewall() -> None:
    receipt = json.loads(
        (OUTCOMES / "artifacts/peaice-meta-kakeyalogic-probe-001.receipt.json").read_text(
            encoding="utf-8"
        )
    )
    artifact = ROOT / receipt["artifact"]["path"]
    assert artifact.is_file()
    artifact_bytes = artifact.read_bytes()
    artifact_text = artifact_bytes.decode("utf-8")
    assert len(artifact_bytes) == receipt["artifact"]["bytes"]
    assert hashlib.sha256(artifact_bytes).hexdigest() == receipt["artifact"]["sha256"]
    assert set(re.findall(r'fixtureId:"(F-\d{3})"', artifact_text)) == {
        f"F-{index:03d}" for index in range(1, 12)
    }
    assert not re.findall(r'(?:src|href)=["\']([^"\']+)["\']', artifact_text, re.I)
    assert all(marker in artifact_text for marker in ("NOT_RUN", "PASS_SIMULATION", "h_eval_cap"))
    assert receipt["source"]["evidence_class"] == "ARTIFACT-SIMULATION"
    assert receipt["execution"]["status_for_this_receipt"] == "NOT_RUN"
    assert receipt["execution"]["permitted_interpretation"] == "PASS_SIMULATION-UI-ONLY"
    assert "BEHAVIORAL-PROBE-NOT-THEOREM" in receipt["claim_firewall"]
    assert receipt["probe_contract"]["h_eval_cap"] < 1
