import json
from pathlib import Path

def test_manifest_pins():
    data = json.loads((Path(__file__).resolve().parents[1] / "outcomes/artifacts/integrity-ledger.json").read_text())
    assert len(data["pins"]) >= 4
    for p in data["pins"]:
        assert len(p["sha256"]) == 64
