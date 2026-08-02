#!/usr/bin/env python3
"""Validate the seven supplied paper snapshots and their claim boundaries."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "registry/paper-references.json"

EXPECTED_HASHES = {
    "P1-wang-wu-restriction-decoupling": "0c91de80d905de5738297728f1812ba417e7ade22a644867a6312dd414e4732d",
    "P2-slater-hilbert-schmidt": "532a5f9f1022f25d1321d0a722e3ebd6287b088c9316e3c5e3b72e629e20b916",
    "P3-wang-zahl-kakeya-r3": "631e8b2118e3d03ded2d5fe79f9acdf74353877d143e9887a3c31278cd13ed01",
    "P4-ochs-chen-brox-pock-ipiano": "2e813b768a477005ac6c556ad8b1b6bdce86f40e4fc03481fde4beeb2d1a3e81",
    "P5-poltoratski-krein-spectral-shift": "76aaca9bb84cb8186d05b5ef75328059ba6ca2fe957e8750c31c49cb5a8acb32",
    "P6-guth-wang-zahl-streamlined-kakeya": "1bc7df83c394cb74038af673c4a25e98b3e018039c75f3b26501ed496028dce9",
    "P7-chaosbook-spectral-determinants": "d58124668a6d5c28befeefa8e83204991089242c8758ac184e8bb5f577ac1c5f",
}

EXPECTED_STATUSES = {
    "P1-wang-wu-restriction-decoupling": "THEOREM-BACKGROUND",
    "P2-slater-hilbert-schmidt": "STRUCTURAL-ANALOGY",
    "P3-wang-zahl-kakeya-r3": "THEOREM-BACKGROUND",
    "P4-ochs-chen-brox-pock-ipiano": "KNOWN",
    "P5-poltoratski-krein-spectral-shift": "KNOWN",
    "P6-guth-wang-zahl-streamlined-kakeya": "THEOREM-BACKGROUND",
    "P7-chaosbook-spectral-determinants": "KNOWN",
}


def main() -> int:
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    records = data.get("references", [])
    by_id = {record.get("id"): record for record in records}
    ids = [record.get("id") for record in records]

    missing = sorted(set(EXPECTED_HASHES) - set(by_id))
    duplicates = sorted({reference_id for reference_id in ids if ids.count(reference_id) > 1})
    hash_drift = sorted(
        reference_id
        for reference_id, expected in EXPECTED_HASHES.items()
        if reference_id in by_id
        and by_id[reference_id].get("source_snapshot", {}).get("sha256") != expected
    )
    status_drift = sorted(
        reference_id
        for reference_id, expected in EXPECTED_STATUSES.items()
        if reference_id in by_id and by_id[reference_id].get("reference_status") != expected
    )
    bridge_drift = sorted(
        reference_id
        for reference_id, record in by_id.items()
        if record.get("bridge_effect") != "does-not-close"
    )
    missing_boundaries = sorted(
        reference_id
        for reference_id, record in by_id.items()
        if not record.get("claim_boundary", "").strip()
    )

    problems = {
        "missing": missing,
        "duplicates": duplicates,
        "hash_drift": hash_drift,
        "status_drift": status_drift,
        "bridge_drift": bridge_drift,
        "missing_boundaries": missing_boundaries,
    }
    ok = all(not values for values in problems.values())
    print(json.dumps({"probe": "paper_references", "ok": ok, **problems}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
