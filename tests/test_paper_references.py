import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_paper_reference_surface_has_all_supplied_sources_and_boundaries():
    data = json.loads((ROOT / "registry/paper-references.json").read_text(encoding="utf-8"))
    records = data["references"]
    assert len(records) >= 7
    assert len({record["id"] for record in records}) == len(records)
    assert all(record["primary_url"].startswith("https://") for record in records)
    assert all(record["bridge_effect"] == "does-not-close" for record in records)
    assert all(record["claim_boundary"] for record in records)


def test_human_reference_surface_preserves_open_seals():
    text = (ROOT / "references/README.md").read_text(encoding="utf-8")
    assert "RH is `OPEN`" in text
    assert "Coleman Conjecture is `OPEN`" in text
    for key in range(1, 8):
        assert f"P{key}" in text
