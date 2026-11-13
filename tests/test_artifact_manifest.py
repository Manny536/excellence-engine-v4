import json
from hashlib import sha256
from pathlib import Path

import pytest

def test_manifest_pins():
    data = json.loads((Path(__file__).resolve().parents[1] / "outcomes/artifacts/integrity-ledger.json").read_text())
    assert len(data["pins"]) >= 4
    for p in data["pins"]:
        assert len(p["sha256"]) == 64


@pytest.mark.parametrize(("example", "asset_count"), [("1.1", 9), ("1.2", 6)])
def test_compaction_example_evidence_manifest(example, asset_count):
    root = Path(__file__).resolve().parents[1]
    record_path = root / "evaluations/cross-model-compaction/examples" / example / "record.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    assert record["example"] == example
    asset_dir = root / record["asset_dir"]
    pins = {}
    for line in (asset_dir / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split()
        assert name not in pins
        pins[name] = digest
    assert len(record["assets"]) == asset_count
    assert pins.keys() == set(record["assets"])
    for name, digest in pins.items():
        assert sha256((asset_dir / name).read_bytes()).hexdigest() == digest, name
    for observation in record["observations"].values():
        assert set(observation.get("witnesses", [])) <= pins.keys()
