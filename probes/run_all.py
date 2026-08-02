#!/usr/bin/env python3
"""Run the complete EEV4 probe suite with fail-fast receipts."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBES = [
    "object_identity_probe.py",
    "claim_status_probe.py",
    "held_trace_probe.py",
    "outcome_case_probe.py",
    "benevolence_drift_probe.py",
    "evidence_exposure_probe.py",
    "correction_survival_probe.py",
    "ledger_continuity_probe.py",
    "artifact_integrity_probe.py",
    "paper_references_probe.py",
    "control_cases_probe.py",
    "schema_validation_probe.py",
    "open_status_probe.py",
]


def main() -> int:
    failed = []
    for name in PROBES:
        completed = subprocess.run([sys.executable, str(ROOT / "probes" / name)], cwd=ROOT)
        if completed.returncode:
            failed.append(name)
    receipt = {"suite": "EEV4-R1", "ok": not failed, "failed": failed}
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
